---
description: "Coordinate a resumable RPI session through Research, Plan, Implement, Review, and Follow-up with durable session state and RPI Workflow canvas integration. Use when a task needs multi-phase RPI lifecycle coordination."
argument-hint: "[task=...] [mode={automatic|manual}] [phase={Research|Plan|Implement|Review|Follow-up}] [critique={standard|deep|skip}] [review={run|skip}] [subagents={auto|none}]"
---

Execute the HVE skill **rpi**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
