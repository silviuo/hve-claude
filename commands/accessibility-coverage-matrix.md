---
description: "Build, refresh, report, or probe an accessibility coverage matrix across criteria, surfaces, and evidence methods. Use when assessing coverage with the accessibility runtime harness and generated evidence bundle."
argument-hint: "scope=... frameworks={wcag-22|aria-apg|coga|section-508|en-301-549} mode={build|refresh|report|probe} [baseUrl=...] [serve={auto|external}]"
---

Execute the HVE skill **accessibility-coverage-matrix**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/accessibility/accessibility-coverage-matrix/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/accessibility/accessibility-coverage-matrix/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
