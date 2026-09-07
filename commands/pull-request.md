---
description: "Drafts or opens a GitHub pull request, runs changed-area preflight checks, and commits validated preflight repairs. Use when a user asks to prepare, create, or update a pull request."
argument-hint: "[base=auto] [draft=false] [action=prepare|create|update]"
---

Execute the HVE skill **pull-request**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/pull-request/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/pull-request/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
