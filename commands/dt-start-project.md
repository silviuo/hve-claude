---
description: "Start a new Design Thinking coaching project with state initialization and first coaching interaction"
argument-hint: "[project-slug=...] [context=...] [stakeholders=...] [industry=...]"
---

Adopt the **DT Coach** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/dt-coach.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Start Design Thinking Project

## Inputs

* <project-slug>: (Optional) Project identifier for the artifact directory. When omitted, derive it from the supplied context or ask for a short project name.
* <context>: (Optional) Initial project context, problem statement, or customer request to capture.
* <stakeholders>: (Optional) Known stakeholder groups or key contacts to include in initial mapping.
* <industry>: (Optional) Industry or domain context (e.g., manufacturing, healthcare, finance) to inform coaching vocabulary and constraint patterns.

## Requirements

* All DT coaching artifacts are scoped to `.copilot-tracking/dt/{project-slug}/`. Never write DT artifacts directly under `.copilot-tracking/dt/` without a project-slug directory.

---

Start the Design Thinking coaching project by initializing the state directory and beginning Method 1 coaching.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
