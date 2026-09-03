---
description: "Retrieve Azure DevOps build status and logs for a pull request or build number"
---

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# ADO Build Info & Log Extraction (Targeted or Latest PR Build)

**MANDATORY**: Activate the `backlog-management` skill by name and follow its Azure DevOps build-info reference (`references/ado-build-info.md`). That reference is packaged with the skill, not with this prompt, so resolve it by name rather than by path.

When the skill does not resolve, warn the user that the build-info protocol is unavailable and stop before any Azure DevOps call. Do not reconstruct it here.

## Inputs

* <project>: Azure DevOps project name should be identified if not provided.
* <pr>: Pull request (number, ID, or generic terms "my pr", "current pr", etc) and can represent the [PR number].
* <build>: Build (number, ID, or generic terms "most recent", "current", "failed, etc) and can represent the [build ID].
* <info>: The type of information to retrieve along with considering the user's prompt.

---

If the user provided additional detail then be sure to include them when retrieving build information.

Proceed with build information retrieval by following the Required Protocol.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
