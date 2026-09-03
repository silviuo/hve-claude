---
description: "Authors Vally conformance test stimuli for an existing prompt, instructions, agent, or skill artifact"
argument-hint: "[files=...] [kind=auto] [mode=from-artifact]"
---

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# Vally Test Write

## Inputs

* (Optional) files - <files>: Target artifact file(s) to author conformance test stimuli for. Defaults to the current open file or attached file(s).
* (Optional) kind - <kind>: Artifact kind (`prompt`, `instructions`, `agent`, or `skill`). Defaults to `auto` for detection from the artifact path and frontmatter.

## What this prompt does

Dispatches the `Vally Test Author` subagent in `from-artifact` mode for each resolved file. The subagent drafts a conformance stimulus YAML block per documented behavior the artifact already claims and appends each block to the Vally eval file it resolves from its own routing rules.

The subagent runs a Safety Self-Check before any write using its seven-category refusal taxonomy (jailbreak, prompt-injection, harmful-elicitation, tos-violation, coc-violation, model-refusal-elicitation, pii-extraction). A matched category triggers the canonical refusal block and skips the write for that stimulus.

Search for and apply `${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/content-policy-citation.instructions.md`. The prompt authors benign conformance tests only; it must not draft or append stimuli that function as policy-boundary probes, payload examples, hidden-instruction disclosure attempts, PII or secret extraction, terms-of-service evasion, or refusal-text scoring.

## Required Protocol

1. Resolve `files` from the `files=` argument when supplied, otherwise from the current open file or attached file(s) in the conversation.
2. For each resolved file, dispatch the `Vally Test Author` subagent with `mode=from-artifact`, `files=<resolved>`, and `kind=<resolved or auto>`.
3. Surface the subagent's Response Format output for each dispatch: target eval file path, stimuli appended count, duplicates skipped, refusals triggered, and JSON report path.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
