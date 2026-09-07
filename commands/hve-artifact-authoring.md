---
description: "Create and validate HVE Core agents, prompts, instructions, and skills with current frontmatter, package membership, delegation, tracking, documentation, and validation conventions. Use when authoring a GitHub Copilot customization artifact in this repository."
argument-hint: "[targets=...] [artifact-type=agent|prompt|instruction|skill] [requirements=...]"
---

Execute the HVE skill **hve-artifact-authoring**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/coding-standards/hve-artifact-authoring/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/coding-standards/hve-artifact-authoring/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
