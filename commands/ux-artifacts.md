---
description: "Produce evidence-labelled UX needs, journey, structure, inclusion, and engineering-handoff assets. Use when a practitioner needs a durable UX artifact rather than coaching."
argument-hint: "[mode=frame-needs|map-journey|sketch-structure|decide-inclusion|prepare-handoff] [project=...] [subject=...] [source=...] [destination=figma|mural] [destination-kind=...] [destination-target=...] [destination-change=create|update|append]"
---

Execute the HVE skill **ux-artifacts**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/ux-artifacts/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/ux-artifacts/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
