---
description: "Create, update, or manage PowerPoint slide decks"
argument-hint: "[source=PPTX or content] {action=create|update|cleanup|from-existing} [requirements=...]"
---

Adopt the **PowerPoint Builder** agent for this command: first Read `${CLAUDE_PLUGIN_ROOT}/agents/pptx.md` and follow its goal, success criteria, guidance, and state contract while executing the request below. Where it delegates work to named subagents, launch them with the Agent tool using the matching agent name.

> **Arguments:** $ARGUMENTS
> Parse space-separated `key=value` pairs from the arguments above as the named inputs of this command; bare text without a `key=` prefix is the required primary input. Unspecified optional inputs are unset.

# PowerPoint Slide Deck

## Inputs

* <source>: (Optional) Source PPTX file or content directory to work from. Defaults to creating a new deck.
* <action>: (Optional) Action to perform: `create`, `update`, `cleanup`, or `from-existing`. Defaults to `create` when omitted.
* <requirements>: (Optional) Additional requirements, objectives, or constraints for the slide deck.

## Requirements

1. Establish a working directory under `.copilot-tracking/ppt/` for all artifacts.
2. Organize content, images, and scripts as separate artifacts before generating slides.
3. Generate slide decks programmatically using Python with `python-pptx`.
4. Validate each iteration against the quality checklist before presenting results.
5. Iterate on fixes until the deck passes all validation checks.

---

*HVE conversion note: "skills" referenced by name live at `${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/*/<skill-name>/SKILL.md` (Glob for the category, Read the SKILL.md, resolve its relative paths against its own directory). Agents live at `${CLAUDE_PLUGIN_ROOT}/agents/<name>.md`; instruction files under `${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/`. Read referenced files before applying them. Durable artifacts (e.g. `.copilot-tracking/`) belong in the current working repository. `${CLAUDE_PLUGIN_ROOT}` is this plugin's install directory. If the literal text was not expanded, resolve it by locating the installed hve plugin root (Glob for `**/hve/.claude-plugin/plugin.json` under `~/.claude/plugins/`).
*
