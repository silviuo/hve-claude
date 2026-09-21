---
description: "Follow an approved RPI plan, keep it current as new information comes to light, check off completed work, and keep a condensed changes log. Use when implementation is ready to begin or resume."
argument-hint: "[plan=...] [phase=...] [task=...]"
---

Execute the HVE skill **rpi-implement**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-implement/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-implement/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
