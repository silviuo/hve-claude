---
description: "Coordinate one task through the Research, Plan, Implement, Review, and Follow-up RPI workflow"
argument-hint: "task=... [continue=...] [followUp=...]"
---

Adopt the **RPI Agent** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/rpi-agent.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# RPI

## Inputs

* <task>: (Required) Task description or target outcome.
* <continue>: (Optional) Resume the active task from its durable RPI artifacts.
* <followUp>: (Optional) Select a distinct follow-up item from a prior review.

## Requirements

1. Use `<task>` as the primary task context and start with research readiness.
2. Sequence `rpi-research`, `rpi-plan`, `rpi-implement`, and `rpi-review` as needed. Planning owns independent critique, implementation owns amendments and divergence records, and review owns outcome routing.
3. For `<continue>`, resume the active task at the earliest stage affected by existing evidence. For `<followUp>`, route the selected item to research, planning, implementation, or a distinct new task.
4. Summarize current lifecycle stage, artifact paths, validation evidence, review execution status and outcome, and the routed follow-up.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
