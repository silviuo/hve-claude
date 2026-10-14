---
description: "Create a qualitative risk register and mitigation plan using a Probability x Impact matrix. Use when a project needs structured risk identification, scoring, ownership, and response planning."
argument-hint: "[project-name=...] [focus-area=...]"
---

Execute the HVE skill **risk-register**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/security/risk-register/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/security/risk-register/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
