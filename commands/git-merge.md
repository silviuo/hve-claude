---
description: "Coordinate Git merge, rebase, and rebase --onto workflows with conflict handling"
---

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Git Merge & Rebase Orchestrator

Follow all instructions from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/git-merge.instructions.md

## Overview

Manage Git merge, rebase, and rebase --onto sequences with standardized stop controls, conflict workflows, and completion summaries.

## Inputs

* <operation> – Selects the workflow (`merge`, `rebase`, or `rebase-onto`).
* <branch> – Branch or ref that receives the merge or becomes the rebase target.
* <onto> – Optional new base required when `<operation>` is `rebase-onto`.
* <upstream> – Optional upstream branch or commit that bounds the commits to move during `rebase-onto`.
* <conflictStop> – When `true`, pause after each conflict fix for user review before continuing.

No pushes occur automatically.

---

Proceed with git operation following the outlined steps above and the Required Protocol for Git Merge & Rebase.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
