---
description: "Run one complete black-box behavior test of a prompt, instruction, agent, subagent, or skill with explicit fidelity and independent grading. Use as the final behavior gate after hve-builder freezes a candidate, or directly to test an existing artifact without changing it."
argument-hint: "[targets=...] [types=...] [profile={high|medium|low}] [fidelity={simulation|native}] [purpose=...] [retain-sandbox]"
---

Execute the HVE skill **hve-builder-tester**.

1. Read `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/hve-builder-tester/SKILL.md` and follow it completely as the playbook for this invocation.
2. Resolve the skill's relative file references (`references/`, `templates/`, `../`) against its own directory: `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/hve-core/hve-builder-tester/`.
3. Arguments: $ARGUMENTS — parse space-separated `key=value` inputs; bare text is the primary input or topic.
4. Create the durable artifacts the skill specifies (for example under `.copilot-tracking/`) inside the current working repository, never inside the plugin or `~/.claude`.

`${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
