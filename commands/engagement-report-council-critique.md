---
description: "Run one independent Council critique against engagement-report research evidence. Use as the manual separate-session fallback when independent critic agents are unavailable."
argument-hint: "report-date=YYYY-MM-DD report-type=slug critic-run=slug draft=... research=... coverage=... audience=... template=..."
---

Execute the HVE skill **engagement-report-council-critique**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/engagement-reporting/engagement-report-council-critique/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/engagement-reporting/engagement-report-council-critique/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
