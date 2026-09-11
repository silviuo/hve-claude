# hve-claude — Microsoft hve-core workflows as a Claude Code plugin

[microsoft/hve-core](https://github.com/microsoft/hve-core) ("Hypervelocity Engineering") is Microsoft's agentic SDLC framework built for GitHub Copilot. This repo converts its full command set to Claude Code and packages it as an installable, updatable **plugin**: 80 slash commands (the RPI lifecycle, git & PR flows, security / supply-chain / RAI planning, design thinking, backlog tooling) plus 58 subagents.

## Install

**Option A — interactive.** Inside a running Claude Code session (type these at the Claude Code prompt after launching `claude` — they are not shell commands):

```
/plugin marketplace add silviuo/hve-claude
/plugin install hve@hve-claude
```

**Option B — declarative.** Add this to `~/.claude/settings.json` (no TUI needed; Claude Code fetches the marketplace and provisions the plugin on the next session start):

```json
{
  "extraKnownMarketplaces": {
    "hve-claude": {
      "source": { "source": "github", "repo": "silviuo/hve-claude" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": {
    "hve@hve-claude": true
  }
}
```

Either way, start a new session and the commands are available everywhere: `/rpi`, `/rpi-research`, `/git-commit`, … (always also reachable namespaced: `/hve:rpi`). See [HVE-COMMANDS.md](HVE-COMMANDS.md) for the full reference and cheat sheet.

> Notes: the `claude plugin` CLI has no `marketplace add`/`install` subcommands — use one of the two options above. If you previously installed the standalone user-level version (files in `~/.claude/commands` and `~/.claude/agents`), remove those copies before installing the plugin, otherwise every command appears twice and the user-level names shadow the plugin's.

## Update

A scheduled GitHub Action ([sync-upstream.yml](.github/workflows/sync-upstream.yml)) re-converts from upstream hve-core every Monday (and on manual dispatch) and commits the result. The plugin version always changes when content changes — Claude Code's plugin cache is keyed by version, so a content-only sync would otherwise never reach installed copies. Versioning is monotonic: upstream's version is adopted when it is newer, the patch is bumped when content changed without an upstream release, and the exact upstream version is recorded in `plugin.json` → `metadata.upstreamVersion`. Your Claude Code picks updates up via the plugin system:

```
/plugin marketplace update hve-claude
```

or — for the full VS Code-extension experience — enable auto-update for this marketplace in `/plugin` → **Marketplaces** (auto-update is off by default for third-party marketplaces). Claude Code then checks for marketplace updates shortly after session startup, and the next session uses the new version. The complete chain: upstream hve-core changes → weekly Action re-converts and commits here → your Claude Code pulls the update automatically.

## Repo layout

| Path | Contents |
|---|---|
| `.claude-plugin/plugin.json` | Plugin manifest (version tracks upstream hve-core) |
| `.claude-plugin/marketplace.json` | Makes this repo its own one-plugin marketplace |
| `commands/` | 80 generated slash commands |
| `agents/` | 58 generated subagents |
| `hve/` | Pristine mirror of hve-core's skills / instructions / prompts / agents trees + key docs — commands read playbooks, references, and templates from here |
| `tools/convert_hve.py` | The converter (see below) |
| `HVE-COMMANDS.md` | Full command reference + cheat sheet |

Everything under `commands/`, `agents/`, and `hve/` is **generated** — don't edit by hand; changes are overwritten on the next sync. Fix the converter instead.

## The converter

`tools/convert_hve.py` turns a fresh hve-core clone into Claude Code artifacts. Two targets:

```bash
# Plugin layout (what this repo ships; used by the GitHub Action)
python tools/convert_hve.py /path/to/hve-core --target plugin

# Standalone install into your personal ~/.claude (no plugin system involved)
python tools/convert_hve.py /path/to/hve-core --target user
```

Conversion highlights: Copilot `${input:x}` variables become `$ARGUMENTS` parsing notes; `#file:` directives are stripped; prompt→agent bindings become "read and follow this agent spec" pointers; every cross-reference between prompts, skills, agents, and instruction files is rewritten to its installed location (`${CLAUDE_PLUGIN_ROOT}/…` for the plugin target, `~/.claude/…` for the user target); adapter notes tell Claude where skill playbooks live, since Claude does not auto-load Copilot skills by name.

## Attribution & license

All workflow content originates from [microsoft/hve-core](https://github.com/microsoft/hve-core) (MIT, © Microsoft Corporation) — see [hve/LICENSE](hve/LICENSE) and [LICENSE](LICENSE). This repo adds the conversion tooling and packaging; it is not affiliated with or endorsed by Microsoft. Upstream is described by its authors as highly opinionated and rapidly evolving — treat this port accordingly.
