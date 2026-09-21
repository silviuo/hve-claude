---
description: "Guided, conversational walkthrough that explains code, UI, UX, features, or .copilot-tracking artifacts with navigable evidence links, a deep review before explaining, and a reconciled decisions-and-changes ledger. Use when the user wants to understand how something works or why it was changed."
argument-hint: "[target=...] [detail={brief|normal|deep}] [chat]"
---

Execute the HVE skill **rpi-walkthrough**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-walkthrough/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/rpi/rpi-walkthrough/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
