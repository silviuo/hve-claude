---
description: "Run a full VEX pipeline that scans dependencies, enriches CVEs, analyzes exploitability, and drafts an OpenVEX document for review - Brought to you by microsoft/hve-core"
argument-hint: "[scope=path/to/dir] [product=pkg:npm/@org/name]"
---

Adopt the **SSSC Reviewer** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/sssc-reviewer.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# VEX Scan

> [!CAUTION]
> This prompt is an **assistive tool only** and does not replace professional security tooling (SAST, DAST, SCA, penetration testing, compliance scanners) or qualified human review. All AI-drafted VEX status determinations — especially `not_affected` — **must** be reviewed and validated by qualified security professionals before the OpenVEX document is merged or published. The merge commit author is the accountable author of record. AI outputs may contain inaccuracies, miss exploitable paths, or misjudge reachability.

## Inputs

* <scope>: (Optional) Directory or path focus to limit the dependency scan. When omitted, scans the full repository.
* <product>: (Optional) Product identifier in PURL format for the generated statements (for example, `pkg:npm/@microsoft/hve-core`). Inferred from the manifest when not provided.

## Requirements

1. Use the SSSC Reviewer's VEX assessment capability to run the full VEX pipeline (scan, enrich, analyze, and draft an OpenVEX document), following the `vex` skill playbook and the VEX generation and standards instructions.
2. When `<scope>` is provided, limit the dependency scan to files within the specified directories or paths.
3. When `<product>` is provided, use it as the PURL product identifier for the generated VEX statements.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
