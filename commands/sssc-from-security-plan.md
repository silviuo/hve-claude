---
description: "Extend a Security Planner assessment with supply chain coverage using the SSSC Planner agent in from-security-plan mode"
---

Adopt the **SSSC Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/sssc-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# SSSC from Security Plan

## Startup

Display the SSSC Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim at the start of every new project and whenever `disclaimerShownAt` is `null` in `state.json`, before any questions or analysis. After displaying the disclaimer, set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution `OpenSSF Scorecard • SLSA Build Levels • OpenSSF Best Practices Badge • Sigstore • SBOM`. Display both the disclaimer and the attribution before any questions or analysis.

Activate the SSSC Planner in **from-security-plan mode** for project slug `<project-slug>` to extend an existing Security Planner assessment with supply chain security coverage.

The SSSC Planner consults the `supply-chain-security` skill for framework and capabilities-inventory reference content (OpenSSF Scorecard, SLSA, Best Practices Badge, Sigstore, SBOM); do not restate those tables in this prompt.

## Inputs

* `<project-slug>`: (Optional) Project slug for the SSSC plan directory. When omitted, derive from the discovered security plan project name.

## Requirements

### Pre-Scan

Scan the workspace for Security Planner artifacts and supporting context:

**Primary paths:**

* `.copilot-tracking/security-plans/` for Security Planner project subdirectories. Look for `state.json` within each subdirectory. If multiple plans exist, present all candidates to the user for selection.

Also scan the shared supporting context sources defined in `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/sssc-planner.instructions.md`.

Present pre-scan results as a checklist:

* ✅ Discovered security plans and supporting context with file paths and brief descriptions
* ❌ Expected sources that were not found

If zero Security Planner artifacts are found, fall back to capture mode and explain the switch.

### Scope Extraction

Read the selected Security Planner `state.json` and completed artifacts. Extract:

1. Technology stack and deployment targets
2. Compliance requirements and regulatory drivers
3. Threat model findings and operational buckets
4. Identified security controls and gaps
5. Cross-domain mapping from application-level threats to dependency and build pipeline priorities

### Initialization

Create the project directory at `.copilot-tracking/sssc-plans/<project-slug>/`.

Write `state.json` with `entryMode` set to `"from-security-plan"`, `currentPhase` set to `1`, `securityPlannerLink` set to the path of the source security plan, preserving `disclaimerShownAt` if already set, and remaining fields populated from the extracted security plan context.

### Phase 1 Entry

Present the extracted scope as a checklist with markers:

* ✅ Items confirmed from the Security Planner artifacts
* ❓ Items that need clarification or are missing

Then invite the user into a Phase 1 conversation with 3 to 5 facilitative clarifying questions targeting supply chain gaps not covered by the security plan, such as package manager inventory, CI/CD pipeline topology, release strategy, signing posture, SBOM tooling, and Best Practices Badge readiness. Use confirmation-and-refinement phrasing rather than directives.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
