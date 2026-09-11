"""Convert microsoft/hve-core artifacts into Claude Code commands/agents/content.

Two output targets:

  python tools/convert_hve.py <hve-core-clone> --target plugin
      Regenerates this plugin repo's commands/, agents/, and hve/ mirror with
      ${CLAUDE_PLUGIN_ROOT}-based references, and syncs the plugin version from
      upstream's plugin.json. Used by the sync-upstream GitHub Action and for
      local development of the plugin.

  python tools/convert_hve.py <hve-core-clone> --target user [--dst <dir>]
      Writes straight into a personal Claude Code config dir (default ~/.claude):
      commands/, agents/, hve/ with ~/.claude-based references. Standalone
      install without the plugin system.

Conversion fixes baked in: ${input:x} -> <x> with $ARGUMENTS notes, path-attached
'#file:' directives stripped, instruction refs resolved by longest-suffix relpath
(handles duplicate basenames like pull-request.instructions.md), agent bindings,
and skill-location adapter notes (Claude does not auto-load skills by name).
"""
import argparse, json, re, shutil, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("src", help="path to a fresh microsoft/hve-core clone")
ap.add_argument("--target", choices=["plugin", "user"], default="plugin")
ap.add_argument("--dst", default=None,
                help="output root (default: repo root for plugin, ~/.claude for user)")
args = ap.parse_args()

SRC = Path(args.src)
REPO_ROOT = Path(__file__).resolve().parent.parent
if args.dst:
    DST = Path(args.dst)
elif args.target == "plugin":
    DST = REPO_ROOT
else:
    DST = Path.home() / ".claude"
HVE = DST / "hve"

if args.target == "plugin":
    ROOT_TOKEN = "${CLAUDE_PLUGIN_ROOT}"
    TREE_PREFIX = ROOT_TOKEN + "/hve/.github/"
    AGENTS_PREFIX = ROOT_TOKEN + "/agents/"
    COMMANDS_PREFIX = ROOT_TOKEN + "/commands/"
    PATH_NOTE = (
        "`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal "
        "text was not expanded, resolve it by locating the installed hve plugin root "
        "(Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).\n"
    )
else:
    TREE_PREFIX = "~/.claude/hve/.github/"
    AGENTS_PREFIX = "~/.claude/agents/"
    COMMANDS_PREFIX = "~/.claude/commands/"
    PATH_NOTE = ""

if not (SRC / ".github" / "skills").is_dir():
    sys.exit(f"error: {SRC} does not look like an hve-core clone")

report = {"warnings": []}

# ---------------------------------------------------------------- frontmatter
def parse_fm(text):
    """Return (dict, body). Minimal YAML: scalars, quoted, >-/| folded. Lists ignored."""
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    fm = {}
    i = 1
    while i < end:
        m = re.match(r"^([A-Za-z][A-Za-z0-9-]*):\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in (">-", ">", "|", "|-"):
            folded = []
            i += 1
            while i < end and (lines[i].startswith("  ") or lines[i].strip() == ""):
                folded.append(lines[i].strip())
                i += 1
            fm[key] = " ".join(x for x in folded if x)
            continue
        if val == "":  # list or nested block: skip its indented lines
            i += 1
            while i < end and lines[i].startswith(" "):
                i += 1
            fm[key] = ""
            continue
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        fm[key] = val
        i += 1
    body = "\n".join(lines[end + 1:])
    return fm, body

def yq(s):  # yaml-safe double-quoted scalar
    return json.dumps(s, ensure_ascii=False)

# ---------------------------------------------------------------- copy tree
# Wipe only generated subtrees; root files (README, HVE-COMMANDS.md, .claude-plugin,
# tools/) survive. In plugin mode commands/ and agents/ are fully generated, so wipe
# them too; in user mode they may hold the user's own files, so only overwrite.
for sub in [".github", "docs"]:
    if (HVE / sub).exists():
        shutil.rmtree(HVE / sub)
if args.target == "plugin":
    for sub in ["commands", "agents"]:
        if (DST / sub).exists():
            shutil.rmtree(DST / sub)
HVE.mkdir(parents=True, exist_ok=True)
for sub in ["skills", "instructions", "agents", "prompts"]:
    shutil.copytree(SRC / ".github" / sub, HVE / ".github" / sub)
for sub in ["security", "rpi"]:
    shutil.copytree(SRC / "docs" / sub, HVE / "docs" / sub)
for f in ["CODE_OF_CONDUCT.md", "LICENSE", "TRANSPARENCY-NOTE.md"]:
    if (SRC / f).exists():
        shutil.copy2(SRC / f, HVE / f)

(DST / "commands").mkdir(exist_ok=True)
(DST / "agents").mkdir(exist_ok=True)

# ---------------------------------------------------------------- build maps
agent_files = sorted((SRC / ".github/agents").rglob("*.agent.md"))
prompt_files = sorted((SRC / ".github/prompts").rglob("*.prompt.md"))
skill_files = sorted((SRC / ".github/skills").rglob("SKILL.md"))
instr_files = sorted((SRC / ".github/instructions").rglob("*.instructions.md"))

def slug_of(p):  # foo-bar.agent.md -> foo-bar
    return p.name[:-len(".agent.md")]

agent_slugs = {}
agent_name_to_slug = {}
for p in agent_files:
    s = slug_of(p)
    if s in agent_slugs:
        report["warnings"].append(f"agent slug collision: {s}")
    agent_slugs[s] = p
    fm, _ = parse_fm(p.read_text(encoding="utf-8"))
    if fm.get("name"):
        agent_name_to_slug[fm["name"]] = s

prompt_bases = {}
for p in prompt_files:
    b = p.name[:-len(".prompt.md")]
    if b in prompt_bases:
        report["warnings"].append(f"prompt name collision: {b}")
    prompt_bases[b] = p

instr_map = {}        # basename -> relpath (last wins; ambiguous ones warned)
instr_relpaths = []   # relpaths with a directory part, longest first
for p in instr_files:
    rel = p.relative_to(SRC / ".github/instructions").as_posix()
    if p.name in instr_map:
        report["warnings"].append(
            f"instruction basename collision: {p.name} (full-relpath refs still resolve correctly)")
    instr_map[p.name] = rel
    if "/" in rel:
        instr_relpaths.append(rel)
instr_relpaths.sort(key=len, reverse=True)

# ---------------------------------------------------------------- rewriting
RX_AGENT = re.compile(r"[A-Za-z0-9_./\\-]*?([A-Za-z0-9_-]+)\.agent\.md")
RX_PROMPT = re.compile(r"[A-Za-z0-9_./\\-]*?([A-Za-z0-9_-]+)\.prompt\.md")
RX_INSTR = re.compile(r"[A-Za-z0-9_./\\~-]*?([A-Za-z0-9_-]+\.instructions\.md)")
RX_INPUT = re.compile(r"\$\{input:([A-Za-z0-9_-]+)(?::[^}]*)?\}")
RX_HASHFILE = re.compile(r"#file:(?=[~./A-Za-z$])")
RESOLVED_MARKS = (".claude/", "${CLAUDE_PLUGIN_ROOT}")

def resolved(s):
    return any(m in s for m in RESOLVED_MARKS)

def rewrite(text):
    def sub_agent(m):
        if resolved(m.group(0)):
            return m.group(0)
        s = m.group(1)
        return AGENTS_PREFIX + s + ".md" if s in agent_slugs else m.group(0)
    def sub_prompt(m):
        if resolved(m.group(0)):
            return m.group(0)
        b = m.group(1)
        return COMMANDS_PREFIX + b + ".md" if b in prompt_bases else m.group(0)
    def sub_instr(m):
        whole = m.group(0).replace("\\", "/")
        if resolved(whole):
            return m.group(0)
        # longest-suffix match against known relpaths disambiguates duplicate
        # basenames (e.g. hve-core/pull-request.instructions.md vs the root one)
        for rel in instr_relpaths:
            if whole == rel or whole.endswith("/" + rel):
                return TREE_PREFIX + "instructions/" + rel
        b = m.group(1)
        return TREE_PREFIX + "instructions/" + instr_map[b] if b in instr_map else m.group(0)
    text = RX_AGENT.sub(sub_agent, text)
    text = RX_PROMPT.sub(sub_prompt, text)
    text = RX_INSTR.sub(sub_instr, text)
    text = text.replace(".github/skills/", TREE_PREFIX + "skills/")
    text = text.replace(".github/instructions/", TREE_PREFIX + "instructions/")
    text = text.replace(".github/agents/", TREE_PREFIX + "agents/")
    text = text.replace(".github/prompts/", TREE_PREFIX + "prompts/")
    # collapse accidental doubles from refs that already carried the prefix
    text = text.replace(TREE_PREFIX + TREE_PREFIX, TREE_PREFIX)
    text = RX_INPUT.sub(r"<\1>", text)
    text = RX_HASHFILE.sub("", text)  # strip Copilot #file: directive off paths
    return text

# 1) rewrite every md file in the pristine tree
tree_count = 0
for p in list((HVE / ".github").rglob("*.md")) + list((HVE / "docs").rglob("*.md")):
    t = p.read_text(encoding="utf-8")
    t2 = rewrite(t)
    if t2 != t:
        p.write_text(t2, encoding="utf-8", newline="\n")
        tree_count += 1

# ---------------------------------------------------------------- commands from prompts
ARGS_NOTE = (
    "> **Arguments:** $ARGUMENTS\n"
    "> Parse space-separated `key=value` pairs from the arguments above as the named "
    "inputs of this command; bare text without a `key=` prefix is the required primary "
    "input. Unspecified optional inputs are unset.\n"
)
FOOTER = (
    "\n---\n\n"
    "*HVE conversion note: \"skills\" referenced by name live at "
    f"`{TREE_PREFIX}skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the "
    "SKILL.md, resolve its relative paths against its own directory). Agents live at "
    f"`{AGENTS_PREFIX}<name>.md`; instruction files under "
    f"`{TREE_PREFIX}instructions/`. Read referenced files before applying them. "
    "Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. "
    + PATH_NOTE + "*\n"
)
GENERIC_AGENTS = {"", "agent"}
cmd_count = 0
for base, p in sorted(prompt_bases.items()):
    fm, body = parse_fm(p.read_text(encoding="utf-8"))
    out = ["---"]
    if fm.get("description"):
        out.append(f"description: {yq(fm['description'])}")
    if fm.get("argument-hint"):
        out.append(f"argument-hint: {yq(fm['argument-hint'])}")
    out.append("---")
    out.append("")
    agent = fm.get("agent", "").strip().strip("\"'")
    if agent not in GENERIC_AGENTS:
        s = agent_name_to_slug.get(agent) or (agent if agent in agent_slugs else None)
        if s:
            out.append(
                f"Adopt the **{agent}** agent for this command: first Read "
                f"`{AGENTS_PREFIX}{s}.md` and follow its goal, success criteria, "
                f"guidance, and state contract while executing the request below. "
                f"Where it delegates work to named subagents, launch them with the "
                f"Agent tool using the matching agent name.\n"
            )
        else:
            report["warnings"].append(f"{base}: unknown agent '{agent}'")
    if "${input:" in body or fm.get("argument-hint"):
        out.append(ARGS_NOTE)
    out.append(rewrite(body).strip())
    out.append(FOOTER)
    (DST / "commands" / f"{base}.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    cmd_count += 1

# ---------------------------------------------------------------- commands from user-invocable skills
skill_cmd_count = 0
for p in skill_files:
    fm, _ = parse_fm(p.read_text(encoding="utf-8"))
    if fm.get("user-invocable", "").strip().lower() != "true":
        continue
    name = fm.get("name") or p.parent.name
    rel = p.parent.relative_to(SRC / ".github/skills").as_posix()  # cat/skill
    if name in prompt_bases:
        report["warnings"].append(f"skill/prompt command collision: {name}")
        continue
    out = ["---"]
    if fm.get("description"):
        out.append(f"description: {yq(fm['description'])}")
    if fm.get("argument-hint"):
        out.append(f"argument-hint: {yq(fm['argument-hint'])}")
    out.append("---")
    out.append("")
    out.append(f"Execute the HVE skill **{name}**.")
    out.append("")
    out.append(f"1. Read `{TREE_PREFIX}skills/{rel}/SKILL.md` and follow it completely as the playbook for this invocation.")
    out.append(f"2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `{TREE_PREFIX}skills/{rel}/`.")
    out.append("3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.")
    out.append("4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.")
    if PATH_NOTE:
        out.append("")
        out.append(PATH_NOTE.rstrip())
    out.append("")
    (DST / "commands" / f"{name}.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    skill_cmd_count += 1

# ---------------------------------------------------------------- agents
SKILL_NOTE_AGENT = (
    "HVE \"skills\" referenced by name are not auto-loaded in Claude Code: locate them with "
    f"Glob at `{TREE_PREFIX}skills/*/<skill-name>/SKILL.md`, Read the SKILL.md, and "
    "follow it, resolving its relative `references/` and `templates/` paths against its own "
    "directory. " + PATH_NOTE
)
agent_count = 0
for s, p in sorted(agent_slugs.items()):
    fm, body = parse_fm(p.read_text(encoding="utf-8"))
    desc = fm.get("description", "") or f"HVE {s} agent"
    out = ["---", f"name: {s}", f"description: {yq(desc)}", "---", ""]
    disp = fm.get("name", s)
    out.append(
        f"You are the HVE **{disp}** agent (converted from microsoft/hve-core). "
        f"Follow the specification below. References to other agents are Claude "
        f"subagents in `{AGENTS_PREFIX.rstrip('/')}/`; if you cannot launch subagents yourself, "
        f"perform their work inline following their specification files.\n"
    )
    out.append(SKILL_NOTE_AGENT)
    out.append(rewrite(body).strip())
    out.append("")
    (DST / "agents" / f"{s}.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
    agent_count += 1

# ---------------------------------------------------------------- plugin version sync
# Claude Code's plugin cache is keyed by version (cache/<mkt>/<plugin>/<version>/),
# so the version MUST change whenever shipped content changes or installs stay
# stale forever. The plugin version is therefore monotonic: it adopts the upstream
# version when upstream's is newer, never goes backward, and the sync workflow
# bumps the patch when content changed while the version did not. The upstream
# hve-core version is recorded in metadata.upstreamVersion.
upstream_version = None
if args.target == "plugin":
    src_manifest = SRC / "plugin.json"
    manifest_path = DST / ".claude-plugin" / "plugin.json"
    if src_manifest.exists() and manifest_path.exists():
        def sv(v):  # "3.2.2" / "3.3.0-rc1" -> (3, 2, 2) for ordering
            try:
                return tuple(int(x) for x in v.split("-")[0].split("."))
            except ValueError:
                return (0,)
        upstream_version = json.loads(src_manifest.read_text(encoding="utf-8")).get("version")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        current = manifest.get("version", "0.0.0")
        changed = False
        if upstream_version and sv(upstream_version) > sv(current):
            manifest["version"] = upstream_version
            changed = True
        if upstream_version and manifest.setdefault("metadata", {}).get("upstreamVersion") != upstream_version:
            manifest["metadata"]["upstreamVersion"] = upstream_version
            changed = True
        if changed:
            manifest_path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8", newline="\n")

print(json.dumps({
    "target": args.target,
    "dst": str(DST),
    "prompt_commands": cmd_count,
    "skill_commands": skill_cmd_count,
    "agents": agent_count,
    "tree_md_rewritten": tree_count,
    "upstream_version": upstream_version,
    "warnings": report["warnings"],
}, indent=2))
