---
description: "Performance, load, and reliability (SLO/SRE) planning for production readiness. Use when defining service level objectives, load characterization, capacity, latency budgets, stress/soak/spike test plans, false-positive baselines, and reliability targets. USE FOR: SLO/SLA definition, load testing plan, performance budget, capacity planning, reliability/SRE backlog, latency targets, error-budget policy. DO NOT USE FOR: executing load tests (use Azure Load Testing tooling), security threat modeling, RAI assessment, privacy/compliance planning, or authoring/restating PRD requirements (cite the PRD's existing NFR/FR ids instead)."
argument-hint: "[journeys=critical-user-flows] [traffic=assumptions]"
---

Execute the HVE skill **performance-slo-planner**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/performance-slo-planner/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/performance-slo-planner/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
