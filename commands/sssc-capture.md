---
description: "Start supply chain security planning from existing knowledge using the SSSC Planner agent in capture mode"
---

Adopt the **SSSC Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/sssc-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# SSSC Capture

## Startup

Display the SSSC Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim at the start of every new project and whenever `disclaimerShownAt` is `null` in `state.json`, before any questions or analysis. After displaying the disclaimer, set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution `OpenSSF Scorecard • SLSA Build Levels • OpenSSF Best Practices Badge • Sigstore • SBOM`. Display both the disclaimer and the attribution before any questions or analysis.

Activate the SSSC Planner in **capture mode** for project slug `<project-slug>`.

The SSSC Planner consults the `supply-chain-security` skill for framework and capabilities-inventory reference content (OpenSSF Scorecard, SLSA, Best Practices Badge, Sigstore, SBOM); do not restate those tables in this prompt.

## Inputs

* `<project-slug>`: (Optional) Kebab-case project identifier for the artifact directory. When omitted, ask for a suitable project name and derive the slug.

## Requirements

### Pre-Scan

Before initialization, scan the shared supporting context sources defined in `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/sssc-planner.instructions.md` to pre-populate Phase 1.

Present pre-scan results as a checklist:

* ✅ Discovered context with file paths and brief descriptions
* ❌ Expected sources that were not found

### Initialization

Create the project directory at `.copilot-tracking/sssc-plans/<project-slug>/`.

Write `state.json` with `entryMode` set to `"capture"`, `currentPhase` set to `1`, preserving `disclaimerShownAt` if already set, and remaining fields at their schema defaults.

If the user has provided existing supply chain notes, workflow inventories, or compliance documentation, extract relevant details and pre-populate Phase 1 fields where possible.

### Phase 1 Entry

Present a short summary sentence describing the assessment scope, then invite the user into a Phase 1 conversation with 3 to 5 focused questions covering:

* Project name and supply chain security purpose
* Programming languages, frameworks, and package managers
* CI/CD platform and runner topology
* Release strategy and artifact distribution channels
* Deployment targets and registry destinations
* Existing security tooling (Dependabot, CodeQL, secret scanning, signing)
* Compliance targets (Scorecard threshold, SLSA Build level, Best Practices Badge tier)

Use facilitative phrasing — invite confirmation and refinement rather than dictating answers — and mark each question with ❓ pending, ✅ complete, or ❌ blocked or skipped as the conversation progresses.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
