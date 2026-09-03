---
description: "Generate a conventional commit message from all branch changes"
---

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Generate Commit Message

Follow all instructions from ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/commit-message.instructions.md

## Input

<useTerminal> - When `true` use the `run_in_terminal` tool with `git --no-pager diff --staged`.

## Protocol

* Use <useTerminal> to either use `git` or `get_changed_files` tool to get the diff of staged changes.
* Review the complete diff and build a high quality commit message following the commit message instructions.
* Output to the user this commit message inside a markdown code block.
* Inform the user that they should copy it as-is or modify it and use it for their commit message.

---

Proceed to generate the commit message

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
