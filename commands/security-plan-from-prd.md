---
description: "Start security planning from PRD/BRD artifacts using the Security Planner agent (from-prd mode)"
---

Adopt the **security-planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/security-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Security Plan from PRD/BRD

## Startup

Before startup behavior, require the Security Planner to locate the available instruction file named `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md`, read `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md` in full, and use its `Security Planning` section as the canonical disclaimer text. If the instruction cannot be found or loaded, halt before questions, analysis, state initialization, or phase work instead of improvising or omitting the disclaimer.

Check the project `state.json`. If it does not exist or `disclaimerShownAt` is `null`, display the canonical Security Planning CAUTION block verbatim, set `disclaimerShownAt` to the current ISO 8601 timestamp, append the matching `noticeLog` entry, and persist state before continuing. If the field is non-null, suppress automatic redisplay during normal continuation. If the user requests redisplay, show the full disclaimer, update `disclaimerShownAt`, and append a notice with `details.reason: "user-requested-redisplay"`.

After the disclaimer, display the framework attribution `OWASP ASVS • OWASP Top 10 • NIST SSDF`. Display both the disclaimer and the attribution before any questions or analysis.

Activate the Security Planner in **from-prd mode** to bootstrap a security plan from existing product definition artifacts.

## Inputs

* <project-slug>: (Optional) Project slug for the security plan directory. When omitted, derive from the discovered PRD/BRD project name.

## Requirements

### PRD/BRD Discovery

Scan these directories as the primary discovery path:

* `.copilot-tracking/prd-sessions/` for product requirements documents
* `.copilot-tracking/brd-sessions/` for business requirements documents

If the primary paths yield no matches, perform a secondary scan of `.copilot-tracking/` for files whose names match `prd-*.md`, `*-prd.md`, `brd-*.md`, `*-brd.md`, or `product-definition*.md`. Exclude generic matches like `requirements.txt` or files outside product-scoping contexts.

Present all discovery results to the user for confirmation before proceeding. Example results:

```text
Found 3 candidates:
  ✅ .copilot-tracking/prd-sessions/contoso-api/prd-final.md
  ✅ .copilot-tracking/brd-sessions/contoso-api/brd-v2.md
  ❌ .copilot-tracking/plans/npm-requirements.md (false positive, discard)
```

If zero artifacts are found after both scans: inform the user that no PRD/BRD artifacts were discovered, offer to switch to capture mode using the `/security-capture` prompt, or ask the user to provide a file path manually. Do not proceed to scope extraction without at least one confirmed artifact.

### Scope Extraction

From confirmed artifacts, extract:

* Project name and description
* Technology stack and frameworks
* Deployment targets (cloud provider, regions, environments)
* Data classification and sensitivity levels
* Compliance requirements mentioned in the artifacts
* Stakeholder roles identified

If the project name cannot be derived from the discovered artifacts and `<project-slug>` is empty, prompt the user for a project slug before proceeding to state initialization.

### State Initialization

Create the project directory at `.copilot-tracking/security-plans/{project-slug}/` and initialize `state.json` with:

* `entryMode` set to `"from-prd"`
* `currentPhase` set to `1`
* Pre-populated fields from extracted PRD/BRD data (project slug, technology inventory, deployment targets, compliance requirements)

### Phase 1 Entry

Present the extracted scope to the user as a checklist using ❓ (pending) and ✅ (confirmed) markers. Ask 3-5 clarifying questions targeting:

* Gaps in the extracted information
* Security-specific concerns not covered in the PRD/BRD
* Data handling and privacy requirements
* Integration points and external dependencies

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
