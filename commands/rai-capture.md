---
description: "Start responsible AI assessment planning from existing knowledge using the RAI Planner agent in capture mode"
---

Adopt the **RAI Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/rai-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# RAI Capture

Activate the RAI Planner in **capture mode** for project slug `<project-slug>`.

## Startup

Before any phase work, check `state.json` for `disclaimerShownAt`. If `disclaimerShownAt` is `null` or `state.json` does not yet exist, display the RAI Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim and set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution following the Session Start Display protocol in ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md. When `replaceDefaultFramework` is `false` or `state.json` does not yet exist, announce the default NIST AI RMF 1.0 framework. When `replaceDefaultFramework` is `true`, announce the custom framework by its name from `riskClassification.framework.name` in `state.json`.

## Requirements

Initialize capture mode at `.copilot-tracking/rai-plans/<project-slug>/`.

Write `state.json` with `entryMode` set to `"capture"`, `currentPhase` set to `1`, preserving `disclaimerShownAt` if already set, and all remaining fields at their schema defaults.

If the user has provided existing AI system notes, model descriptions, or risk context, extract relevant details and pre-populate the system definition where possible.

Begin the Phase 1 AI System Scoping interview with up to 7 focused questions covering:

- AI system purpose and intended outcomes
- AI components and model types (ML models, LLMs, vision, speech)
- Technology stack and deployment context
- Data inputs, outputs, and data flow
- Stakeholder roles (developers, operators, affected individuals)
- Intended and unintended use scenarios
- Known AI-specific risks or concerns
- User-supplied evaluation standards, risk indicator categories, prohibited use frameworks, or output format requirements to store in `.copilot-tracking/rai-plans/references/`

Present a short summary sentence of the assessment scope before asking questions.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
