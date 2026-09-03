---
description: "Set up GitHub Copilot OpenTelemetry capture: configure the VS Code export settings, generate a local Grafana stack and dashboard, or generate the Azure collector, infrastructure, and dashboard for an organization."
argument-hint: "[local-setup|local-stack|org-distribution|azure-capture]"
---

Execute the HVE skill **copilot-otel-metrics**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/experimental/copilot-otel-metrics/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/experimental/copilot-otel-metrics/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
