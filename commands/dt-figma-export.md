---
description: "Export Design Thinking artifacts to a FigJam board or Figma Design file through the Figma MCP server. Use when a team wants collaborative visual review of Method 1, 3, 4, 5, or 6 artifacts, or accepts a DT Coach board-export offer."
argument-hint: "project-slug=... [board-title=...] [method=latest] [output-type={figjam|design|both}]"
---

Execute the HVE skill **dt-figma-export**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/dt-figma-export/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/design-thinking/dt-figma-export/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
