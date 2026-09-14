---
description: "Review a pull request or local change set by routing to the consolidated Code Review agent"
argument-hint: "[pr=...] [base=...] [head=...] [profile=...] [scope=...]"
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
* <profile>: (Optional) Review profile: `standard`, `full`, or `custom`. Defaults to `standard` for every resolved target.
* <scope>: (Optional) Additional scope hints such as paths, perspectives, or depth.

## Requirements

1. Resolve the review target using this priority: explicitly provided `<pr>`, an open PR or MR mapped from the current branch, the `<base>`/`<head>` diff, then local changes.
2. Hand off the resolved target and any explicit `<profile>` to the Code Review agent. When the profile is omitted, use `standard` independently of the target. The `standard` profile recommends Functional, Standards, and Readiness findings, adding Security and Accessibility when their signals fire. Orientation runs once as a workflow stage and is not a findings perspective.
3. Require the resolved PR or branch head SHA to match checked-out `HEAD` before diff generation. On mismatch, stop and ask the user to check out the target head instead of reviewing the current checkout under another target's metadata.
4. Bootstrap change context with the shared PR-reference diff flow using the exact target base, serialize the immutable reviewed head SHA and exact worker output paths, confirm scope, select perspectives and depth, and consolidate skill-backed findings into one report.
5. Keep emission human-gated: in interactive mode the agent writes a human-editable draft and pauses for explicit confirmation and a PR-state check against the reviewed head SHA before any native or external emission.
6. Summarize the verdict, severity counts, and the path to the persisted review report.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
