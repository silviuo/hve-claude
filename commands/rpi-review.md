---
description: "Compare RPI planning and implementation evidence, record review findings, and route follow-up work. Use when an implementation needs acceptance review."
argument-hint: "[task=...] [plan=...] [details=...] [changes=...]"
---

Execute the HVE skill **rpi-review**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-review/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-review/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
