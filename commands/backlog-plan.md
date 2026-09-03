---
description: "Read-only backlog planning for Azure DevOps, GitHub, and Jira. Use to discover, triage, sprint-plan, or resume without mutating a tracker."
argument-hint: "[discover|my-work|task-plan|triage|sprint|resume] [scope or query]"
---

Execute the HVE skill **backlog-plan**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/backlog-plan/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/backlog-plan/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
