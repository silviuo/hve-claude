---
description: "Resume a Design Thinking coaching session - reads coaching state and re-establishes context"
argument-hint: "project-slug=..."
---

Adopt the **DT Coach** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/dt-coach.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Resume Design Thinking Coaching

## Inputs

* <project-slug>: (Required) Kebab-case project identifier for the artifact directory (e.g., `factory-floor-maintenance`).

## Requirements

* All DT coaching artifacts are scoped to `.copilot-tracking/dt/{project-slug}/`. Never write DT artifacts directly under `.copilot-tracking/dt/` without a project-slug directory.

## Required Steps

### Step 1: Locate Project State

1. Use `<project-slug>` as the project directory identifier.
2. Look for the coaching state file at `.copilot-tracking/dt/{project-slug}/coaching-state.md`.
3. If the state file is not found, list directories under `.copilot-tracking/dt/` to check for alternative matches.
4. If multiple projects exist and the slug is ambiguous, list available projects with their last session dates and ask the user to select one.
5. If no state file exists for any project, inform the user and suggest running the `dt-start-project` prompt to initialize a new project.

### Step 2: Read and Summarize State

1. Read the coaching state file and verify it parses as valid YAML with required fields: `project`, `current`, `methods_completed`, `transition_log`.
2. Extract the current method, space, and phase from the `current` block.
3. Read `methods_completed` to determine overall progress through the 9 methods.
4. Review the most recent `transition_log` entry for the last method change and its rationale.
5. Review the most recent `session_log` entry for a summary of previous session work.
6. Scan the `artifacts` list for available project artifacts to reference.
7. If the state file is corrupted or missing required fields, inform the user which fields are unreadable, and offer to reconstruct state from existing artifacts in the project directory or reinitialize from scratch.

### Step 3: Context Recovery

1. Present a human-readable context summary to the user: "Last session you were working on Method [N] ([name]), in the [phase] phase. Here's where you left off: [session log summary]."
2. Include overall progress: which methods are complete and which remain.
3. Reference the most recent transition rationale if it provides useful context.
4. List key artifacts from the project directory that relate to the current method.
5. Review recent session log entries to gauge the coaching intensity level and adjust hint escalation accordingly, starting at the level consistent with prior sessions rather than resetting to Level 1.
6. Ask the user to confirm the summary is accurate before proceeding.

### Step 4: Resume Coaching

1. After the user confirms the context summary, transition into active coaching at the current method and phase.
2. Read the relevant method instruction file for the current method to refresh method-specific knowledge.
3. Continue the conversation naturally as though picking up where the previous session ended, not mechanically reciting method steps.
4. Proceed with Phase 2 (Active Coaching) of the dt-coach protocol from the restored state.

---

Resume the Design Thinking coaching session for project "<project-slug>" by following the Required Steps.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
