---
description: "Review a pull request or local change set by routing to the consolidated Code Review agent"
argument-hint: "[pr=...] [base=...] [head=...] [scope=...]"
---

Adopt the **Code Review** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/code-review.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# PR Review

## Inputs

* <chat>: (Optional, defaults to true) Include conversation context for review scope discovery.
* <pr>: (Optional) Pull request number or URL to review.
* <base>: (Optional) Base branch or ref for the diff. Defaults to the repository default branch.
* <head>: (Optional) Head branch or ref for the diff. Defaults to the current branch.
* <scope>: (Optional) Additional scope hints such as paths, perspectives, or depth.

## Requirements

1. Resolve the review target using this priority: explicitly provided `<pr>`, the `<base>`/`<head>` diff, then the current branch against the default branch.
2. Hand off to the Code Review agent, which bootstraps change context with the shared PR-reference diff flow, confirms scope, selects perspectives and depth, and consolidates skill-backed findings into one report.
3. Keep emission human-gated: in interactive mode the agent writes a human-editable draft and pauses for explicit confirmation and a PR-state check before any native or external emission.
4. Summarize the verdict, severity counts, and the path to the persisted review report.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
