---
description: "Update the Session Log canvas after a Copilot release changes session events, session storage, system prompt structure, or the canvas SDK. Diffs the installed session-events schema against the canvas baseline, then guides the fixes, fixtures, docs, and baseline refresh. Use after updating Copilot or when the canvas shows unknown events or missing data."
argument-hint: "[mode=check|update] [schema=<path|version|latest>]"
---

Execute the HVE skill **session-log-canvas-update**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/session-log-canvas-update/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/session-log-canvas-update/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
