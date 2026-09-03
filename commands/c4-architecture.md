---
description: "Model and document existing or planned software architectures with the C4 model across System Context, Container, and Component levels plus deployment diagrams, then emit diagrams through a selected renderer. Use when an architect needs audience-appropriate software architecture documentation; use the 'architecture-diagrams' skill for infrastructure topology."
---

Execute the HVE skill **c4-architecture**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/c4-architecture/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/c4-architecture/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
