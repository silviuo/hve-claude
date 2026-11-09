---
description: "Create, update, review or render presentation-first HTML slide decks. Use for slide content research, deck styling, VS Code-style walkthroughs, presenter controls, or render-only standalone HTML delivery from authored sources in repository and installed workflows."
argument-hint: "[mode=create|update|review|render] [deck=...] [output=...] [topic=...]"
---

Execute the HVE skill **hve-slides**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/experimental/hve-slides/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/experimental/hve-slides/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
