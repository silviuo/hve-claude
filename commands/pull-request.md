---
description: "Generate pull request descriptions from branch diffs"
argument-hint: "[branch=origin/main] [createPullRequest=false] [excludeMarkdown={true|false}]"
---

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Pull Request

## Inputs

* <branch>: (Optional, defaults to origin/main) Base branch reference for diff generation
* <createPullRequest>: (Optional, determined through conversation provided by user) When true, then explicitly include following instructions for creating pull request with MCP tools.
* <excludeMarkdown>: (Optional) When true, exclude markdown diffs from pr-reference generation

## Requirements

Read and follow all instructions from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/pull-request.instructions.md to generate a pull request body of changes using the pr-reference Skill with parallel subagent review.

Before producing `.copilot-tracking/pr/pr.md` or creating a pull request, search for and apply `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/content-policy-citation.instructions.md`.

---

Generate a new pr.md file following the pull-request instructions.

* Analyzes branch diffs against the base branch and reviews changes using parallel subagents.
* Produces `.copilot-tracking/pr/pr.md` with the final PR description, along with temporary analysis artifacts in `.copilot-tracking/pr/subagents/`.
* Creates a pull request via MCP tools when explicitly requested.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
