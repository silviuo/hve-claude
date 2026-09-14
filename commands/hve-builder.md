---
description: "Create, improve, refactor, replace, review, or validate prompts, instructions, agents, subagents, and skills. Use for Copilot customization cleanup, extending HVE workflows with project-specific capabilities, and parent-owned correction of material review or behavior-test findings."
argument-hint: "[targets=...] [mode=create,improve,refactor] [requirements=...]"
---

Execute the HVE skill **hve-builder**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/hve-builder/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/hve-builder/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
