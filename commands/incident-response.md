---
description: "Run a structured Azure incident response workflow for triage, diagnosis, mitigation, and root cause analysis. Use when operations or security teams need guided incident handling for Azure service symptoms."
argument-hint: "incident-description=... [severity={1|2|3|4}] [phase={triage|diagnose|mitigate|rca}] [chat={true|false}]"
---

Execute the HVE skill **incident-response**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/security/incident-response/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/security/incident-response/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
