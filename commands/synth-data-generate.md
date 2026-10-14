---
description: "Generate synthetic datasets in a Jupyter notebook after the dataops synthetic-data preflight passes. Use when creating new synthetic data or preparing a guarded local replacement candidate from an approved source."
argument-hint: "subject=... [example_data=...]"
---

Execute the HVE skill **synth-data-generate**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/data-science-engineering/synth-data-generate/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/data-science-engineering/synth-data-generate/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
