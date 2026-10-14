---
description: "Stage user-selected paths, confirm the exact staged set, and create one local Conventional Commit, or generate a commit message for staged changes without committing. Use when you want a guarded commit or a ready-to-paste message."
argument-hint: "[mode={commit|message-only}]"
---

Execute the HVE skill **git-commit**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/git-commit/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/git-commit/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
