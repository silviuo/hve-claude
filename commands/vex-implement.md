---
description: "Plan the work to stand up VEX in a target project as a backlog for Task-* implementors - Brought to you by microsoft/hve-core"
argument-hint: "[scope=path/to/dir] [product=pkg:npm/@org/name]"
---

Adopt the **SSSC Planner** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/sssc-planner.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# VEX Implement

> [!CAUTION]
> This prompt is an **assistive tool only** and does not replace professional security tooling (SAST, DAST, SCA, penetration testing, compliance scanners) or qualified human review. All VEX implementation planning must be reviewed and validated by qualified security professionals before the target project adopts or publishes the resulting workflow and document changes. The merge commit author is the accountable author of record. AI-produced planning may miss repository-specific constraints, release workflow details, or ownership requirements.

## Inputs

* <scope>: (Optional) Directory or path focus for the target project. When omitted, the planner uses the current repository context.
* <product>: (Optional) Product identifier in PURL format for the planned VEX document and rollout steps. When omitted, infer it from repository context when possible.

## Requirements

1. Drive the SSSC Planner's VEX planning capability to produce an implementation plan and backlog for standing up VEX in the target project.
2. Keep the work in planning mode only; do not implement the VEX changes directly in the target project.
3. Use the `vex` skill as the reference source for the implement playbook and the VEX rules so the backlog can encode the required stand-up steps.
4. Produce backlog work items that cover scaffolding the OpenVEX document under `security/vex`, wiring the `vex-detect` and `vex-draft` workflows, referencing the PR-body scaffold asset, wiring release attestation, and setting CODEOWNERS where appropriate.
5. Make the handoff explicit: the Planner authors the plan and backlog, and the downstream Task-* agents execute the implementation using the `vex` skill.
6. If the target project already has VEX-related assets, incorporate them as context and avoid redundant planning steps.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
