---
description: "Create or assess an evidence-grounded, falsifiable outcome hypothesis: a testable prediction of what measurable business result will change, for whom, by when, and how leading and lagging indicators will prove or disprove it. Use when framing measurable outcomes, turning an MVP, POC, feature, or technical initiative into a beneficiary result, defining targets and indicators, or judging whether evidence is strong enough to invest. Also applies to business outcome hypotheses, value hypotheses, and outcome statements."
argument-hint: "[context=artifact-or-summary] [mode=create|assess]"
---

Execute the HVE skill **outcome-hypothesis**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/outcome-hypothesis/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/outcome-hypothesis/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
