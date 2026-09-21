---
description: "Independently assess an RPI plan against supplied evidence without editing it. Use for a current initial or planner-authorized recovery critique run."
argument-hint: "[plan=...] [evidence=...] [output=...] [depth={standard|deep}]"
---

Execute the HVE skill **rpi-plan-critique**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-plan-critique/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-plan-critique/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
