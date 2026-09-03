---
description: "Start responsible AI assessment planning from a completed Security Plan using the RAI Planner agent in from-security-plan mode (recommended)"
---

Adopt the **RAI Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/rai-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# RAI Plan from Security Plan

Activate the RAI Planner in **from-security-plan mode**, the recommended workflow for projects that have already completed a security assessment.

Use project slug `<project-slug>`.

## Startup

Before any phase work, check `state.json` for `disclaimerShownAt`. If `disclaimerShownAt` is `null` or `state.json` does not yet exist, display the RAI Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim and set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution following the Session Start Display protocol in ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md. When `replaceDefaultFramework` is `false` or `state.json` does not yet exist, announce the default NIST AI RMF 1.0 framework. When `replaceDefaultFramework` is `true`, announce the custom framework by its name from `riskClassification.framework.name` in `state.json`.

## Requirements

### Security Plan Discovery

Scan `.copilot-tracking/security-plans/` for directories containing `state.json` files.

Present discovered security plans:

- ✅ Found plans with project slug, current phase, and completion status
- ❌ No security plans found

If zero security plans are found, fall back to capture mode and explain the switch.

If multiple security plans exist, present the list and ask the user to select one.

### State Extraction

Read the selected security plan `state.json` and extract:

1. Project name and system description
2. `aiComponents` array with component details
3. `threatCount` for RAI threat ID sequence continuation
4. Technology stack, deployment targets, and data classification
5. Compliance requirements already identified
6. Operational bucket assignments relevant to AI components

Security plan artifacts are **read-only**. Never modify files under `.copilot-tracking/security-plans/`.

### State Initialization

Create the project directory at `.copilot-tracking/rai-plans/<project-slug>/`.

Initialize `state.json` with:

- `entryMode` set to `"from-security-plan"`
- `currentPhase` set to `1`
- `securityPlanRef` pointing to the security plan state.json path
- Pre-populated fields from the extracted security plan
- `raiThreatCount` starting at the security plan's `threatCount` value to continue the ID sequence

### Phase 1 Entry

Present the extracted AI system scope from the security plan as a checklist.

Highlight what the security plan already covers and identify AI-specific context that it does not address, such as:

- Model architecture and training data provenance
- Fairness and bias assessment needs
- Transparency and explainability requirements
- Intended versus unintended use scenarios
- Vulnerable populations and downstream effects

Ask 3 to 5 clarifying questions targeting these AI-specific gaps.

Also ask whether the user has evaluation standards, risk indicator categories, prohibited use frameworks, or output format requirements to supply for storage in `.copilot-tracking/rai-plans/references/`.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
