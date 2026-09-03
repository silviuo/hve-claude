---
description: "Start security planning from existing notes using the Security Planner agent (capture mode)"
---

Adopt the **Security Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/security-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Security Capture

## Startup

Display the Security Planning CAUTION block from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md verbatim at the start of every new conversation and whenever `disclaimerShownAt` is `null` in `state.json`, before any questions or analysis. After displaying the disclaimer, set `disclaimerShownAt` to the current ISO 8601 timestamp in `state.json`.

After the disclaimer, display the framework attribution `OWASP ASVS • OWASP Top 10 • NIST SSDF`. Display both the disclaimer and the attribution before any questions or analysis.

## Inputs

* <project-slug>: (Optional) Kebab-case project identifier for the artifact directory. When omitted, asks for a suitable project name and derives the slug.

## Requirements

* Initialize capture mode by creating the project directory at `.copilot-tracking/security-plans/{project-slug}/` and writing `state.json` with `entryMode: "capture"`, `currentPhase: 1`, and empty or default values for remaining fields.
* If the user provides existing security notes, threat assessments, or documentation as input, extract relevant information and pre-populate Phase 1 fields before asking clarifying questions.
* Begin the Phase 1 interview about the project's security posture with 3-5 focused questions covering: project name and purpose, technology stack, deployment target (cloud, on-prem, hybrid), types of data processed or stored, and known compliance requirements.

## Entry Behavior

Start security planning in capture mode. Initialize the project directory and begin the Phase 1 scoping interview.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
