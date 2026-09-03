---
description: "Build traceable internal-review proposal, RFI, RFP, tender, bid, and questionnaire responses from supplied questions and approved sources. Use to analyze questions, contribute business or product evidence, or draft qualified responses."
argument-hint: "[operation=analyze|contribute|draft] [domain=business|product|shared] [source=<approved-artifact-path>]"
---

Execute the HVE skill **proposal-response**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/proposal-response/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/proposal-response/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
