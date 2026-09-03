---
description: "Run an OWASP vulnerability assessment against the current codebase"
argument-hint: "[scope=path/to/dir] [mode={audit|diff|plan}] [targetSkill={owasp-top-10|owasp-llm|owasp-agentic|owasp-mcp|owasp-infrastructure|owasp-cicd|secure-by-design}]"
---

Adopt the **Security Reviewer** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/security-reviewer.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Vulnerability Scan

> [!CAUTION]
> This prompt is an **assistive tool only** and does not replace professional security tooling (SAST, DAST, SCA, penetration testing, compliance scanners) or qualified human review. All AI-generated vulnerability findings **must** be reviewed and validated by qualified security professionals before use. AI outputs may contain inaccuracies, miss critical threats, or produce recommendations that are incomplete or inappropriate for your environment.

## Inputs

* <mode>: (Optional, defaults to audit) Scanning mode: `audit`, `diff`, or `plan`.
* <targetSkill>: (Optional) Single skill to assess. Bypasses codebase profiling when provided. Available skills: `owasp-agentic`, `owasp-llm`, `owasp-top-10`, `owasp-mcp`, `owasp-infrastructure`, `owasp-cicd`, `secure-by-design`.
* <scope>: (Optional) Specific directories or paths to focus on. When omitted, assesses the full codebase.
* <plan>: (Optional) Implementation plan document path. Inferred from attached files or conversation context when not provided.

## Requirements

1. Route `<mode>` to the agent's corresponding mode. When omitted, default to `audit`.
2. When `<scope>` is provided, limit analysis to files within the specified directories or paths.
3. When `<targetSkill>` is provided, bypass codebase profiling and assess only the specified skill.
4. When `<plan>` is provided and mode is `plan`, pass the document path to the agent for plan-mode analysis.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
