---
description: "Coordinate Git merge, rebase, and rebase --onto workflows with conflict resolution, optional review pauses, and a completion summary. Use when integrating a branch locally and resolving conflicts without pushing."
argument-hint: "operation={merge|rebase|rebase-onto} branch=<ref> [onto=<ref>] [upstream=<ref>] [conflict-stop={true|false}]"
---

Execute the HVE skill **git-merge**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/git-merge/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/git-merge/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
