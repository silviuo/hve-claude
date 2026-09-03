---
description: "Theme discovery for Design Thinking Method 4c through philosophy-based clustering"
argument-hint: "project-slug=... [ideaCount=...]"
---

Adopt the **dt-coach** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/dt-coach.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Method 4: Brainstorming - Convergence

## Inputs

* <project-slug>: (Required) Kebab-case project identifier for the artifact directory (e.g., `factory-floor-maintenance`).
* <ideaCount>: (Optional) Number of ideas generated in divergent phase for validation.

## Requirements

* All DT coaching artifacts are scoped to `.copilot-tracking/dt/{project-slug}/`. Never write DT artifacts directly under `.copilot-tracking/dt/` without a project-slug directory.

---

Invoke Design Thinking coaching for Method 4c (Ideation Convergence) to facilitate theme discovery through pattern recognition and philosophy-based idea clustering.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
