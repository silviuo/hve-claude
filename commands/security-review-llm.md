---
description: "Run OWASP LLM and Agentic vulnerability assessments with codebase profiling"
argument-hint: "[scope=path/to/component]"
---

Adopt the **Security Reviewer** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/security-reviewer.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# LLM and Agentic Vulnerability Scan

> [!CAUTION]
> This prompt is an **assistive tool only** and does not replace professional security tooling (SAST, DAST, SCA, penetration testing, compliance scanners) or qualified human review. All AI-generated vulnerability findings **must** be reviewed and validated by qualified security professionals before use. AI outputs may contain inaccuracies, miss critical threats, or produce recommendations that are incomplete or inappropriate for your environment.

## Inputs

* <scope>: (Optional) Specific component or directory path to focus the assessment on.

## Requirements

* Override skill selection with `owasp-llm, owasp-agentic`. The profiler still runs to supply codebase context, but skill detection is bypassed in favor of these two skills.
* When `<scope>` is provided, limit analysis to files within the specified directory or component.
* Run in `audit` mode using the standard assessment and verification workflow.
* Assess both skills independently through separate Skill Assessor invocations, then consolidate findings in a single report.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
