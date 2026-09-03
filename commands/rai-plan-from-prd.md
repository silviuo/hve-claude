---
description: "Start responsible AI assessment planning from PRD/BRD artifacts using the RAI Planner agent in from-prd mode"
---

Adopt the **RAI Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/rai-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# RAI Plan from PRD/BRD

Activate the RAI Planner in **from-prd mode** to plan for AI-specific risk assessment for project slug `<project-slug>`.

## Startup

Before any phase work, check `state.json` for `disclaimerShownAt`. If `disclaimerShownAt` is `null` or `state.json` does not yet exist, display the RAI Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim and set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution following the Session Start Display protocol in ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md. When `replaceDefaultFramework` is `false` or `state.json` does not yet exist, announce the default NIST AI RMF 1.0 framework. When `replaceDefaultFramework` is `true`, announce the custom framework by its name from `riskClassification.framework.name` in `state.json`.

## Requirements

### PRD/BRD Discovery

Scan for product and business requirements documents:

**Primary paths:**

- `.copilot-tracking/prd-sessions/` for PRD artifacts
- `.copilot-tracking/brd-sessions/` for BRD artifacts

**Secondary scan:**

Search the workspace for files matching `*prd*`, `*brd*`, `*product-requirements*`, or `*business-requirements*` patterns.

Present discovered artifacts:

- ✅ Found artifacts with file paths and brief descriptions
- ❌ Missing artifact locations

If zero artifacts are found, fall back to capture mode and explain the switch.

### AI System Scope Extraction

Extract from the discovered artifacts:

1. Project name and AI system purpose
2. AI components and model types
3. Technology stack and deployment targets
4. Data classification and data flow
5. Stakeholder roles (developers, operators, affected individuals)
6. Intended use scenarios and user populations

### State Initialization

Create the project directory at `.copilot-tracking/rai-plans/<project-slug>/`.

Initialize `state.json` with:

- `entryMode` set to `"from-prd"`
- `currentPhase` set to `1`
- Pre-populated fields from the extracted scope

### Phase 1 Entry

Present the extracted AI system scope as a checklist with markers:

- ✅ Items confirmed from PRD/BRD
- ❓ Items that need clarification or are missing

Ask 3 to 5 clarifying questions that target AI-specific gaps not covered by the requirements documents, such as model selection rationale, training data provenance, fairness considerations, and unintended use scenarios.

Also ask whether the user has evaluation standards, risk indicator categories, prohibited use frameworks, or output format requirements to supply for storage in `.copilot-tracking/rai-plans/references/`.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
