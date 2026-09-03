---
description: "Jira issue workflows for search, issue updates, transitions, comments, field discovery, and interactive credential setup via the Jira REST API. Use when you need to configure Jira access, search with JQL, inspect an issue, create or update work items, move an issue between statuses, post comments, or discover required fields for issue creation."
argument-hint: "[setup|search|get|create|update|transition|comment|fields] [arguments]"
---

Execute the HVE skill **jira**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/jira/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/jira/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
