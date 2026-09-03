---
description: "Coach a UX practitioner through problem framing, running a design critique, or making an evidence-backed case to a skeptical stakeholder. Use when the practitioner has a live UX task and wants to think it through rather than receive an answer."
argument-hint: "[moment=problem-framing|critique|stakeholder-advocacy] [project=...] [subject=...]"
---

Execute the HVE skill **ux-coaching**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/ux-coaching/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/ux-coaching/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
