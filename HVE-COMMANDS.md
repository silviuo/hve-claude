# HVE Commands for Claude Code

Distributed as the `hve` Claude Code plugin (repo: silviuo/hve-claude). Ported from [microsoft/hve-core](https://github.com/microsoft/hve-core) v3.2.2 (MIT) on 2026-09-02.
HVE ("Hypervelocity Engineering") is Microsoft's agentic SDLC framework built for GitHub Copilot; this port makes its full command set available as Claude Code slash commands, with the same workflows and the same durable artifacts.

## Install

```
/plugin marketplace add silviuo/hve-claude
/plugin install hve@hve-claude
```

## Where everything lives

| Location | Contents |
|---|---|
| `commands/` | 80 slash commands — 49 converted from hve prompts, 31 from hve's user-invocable skills |
| `agents/` | 58 Claude subagents converted from hve `.agent.md` files (planners, reviewers, orchestrator subagents) |
| `hve/.github/` | Pristine mirror of hve's skills / instructions / prompts / agents trees — commands read their playbooks, references, and templates from here |
| `tools/convert_hve.py` | The converter (plugin + user targets; see [Updating](#updating)) |
| `.copilot-tracking/` *(in your working repo)* | Durable workflow artifacts (research, plans, change logs, reviews) — same convention as upstream |

Installed as a plugin, the commands are available in every repo you open with Claude Code — bare (`/rpi`) when the name is free, and always namespaced (`/hve:rpi`). Artifacts land in the repo you run them from.

## What was changed during conversion

The content is upstream hve-core, with only mechanical adaptations to run outside GitHub Copilot:

1. **`${input:name}` variables → `$ARGUMENTS`** — Copilot's named-input syntax became a parsing note: commands take space-separated `key=value` pairs; bare text is the primary input.
2. **`#file:` directives stripped** — Copilot's file-import syntax was replaced with plain paths that Claude reads directly.
3. **Agent bindings converted** — prompts bound to a Copilot chat agent (e.g. `RPI Agent`, `Security Planner`) now instruct Claude to read and follow the converted spec in `~/.claude/agents/`.
4. **All cross-references rewritten** — every link between prompts, skills, agents, and instruction files points to its new location; the mirror keeps relative links intact. Includes a fix for two upstream files that share the basename `pull-request.instructions.md`.
5. **Skill-loading adapter notes added** — Copilot auto-loads "skills" by name; Claude does not, so every converted agent and command carries a note pointing to the skill playbooks at `~/.claude/hve/.github/skills/*/<name>/SKILL.md`.
6. **Copilot chat-only features dropped** — handoff buttons and `disable-model-invocation` flags have no Claude equivalent; the workflows' own "Next Steps" guidance replaces them.

---

## Command reference

### RPI workflow — the core lifecycle

Research → Plan → Implement → Review → Follow-up, with durable artifacts under `.copilot-tracking/` so work survives context resets.

| Command | Arguments | What it does |
|---|---|---|
| `/rpi` | `task=...` `[continue=...]` `[followUp=...]` | Coordinates one task through the whole lifecycle (manual or automatic mode), tracking state, artifacts, and ranked follow-ups |
| `/rpi-quick` | `[task=...]` `[continue=...]` `[followUp=...]` | Compact full flow: sequences all phases in one command |
| `/rpi-research` | `[topic=...]` `[chat]` | Research-only: gathers evidence in wider/deeper/contrarian waves, writes a dated artifact under `.copilot-tracking/research/` |
| `/rpi-plan` | `[task=...]` `[research=...]` `[draft=...]` `[decisions=...]` | Builds an evidence-based implementation plan plus phase details from the research |
| `/rpi-plan-critique` | `[plan=...]` `[details=...]` `[evidence=...]` | Independent read-only critique of a plan before implementation |
| `/rpi-implement` | `[plan=...]` `[phase=...]` `[task=...]` | Executes the approved plan, recording amendments, divergences, and a changes log |
| `/rpi-review` | `[task=...]` `[plan=...]` `[changes=...]` | Compares plan vs. implementation evidence, records findings, routes follow-up work |
| `/rpi-walkthrough` | `[target=...]` `[detail=brief\|normal\|deep]` | Guided walkthrough explaining code, features, or `.copilot-tracking` artifacts with evidence links |
| `/rpi-challenger` | `[subject=...]` `[focus=...]` | Adversarial questioning of a task, decision, plan, or artifact to expose assumptions before acting |

### Git & pull requests

| Command | Arguments | What it does |
|---|---|---|
| `/git-commit` | — | Stages all changes, generates a conventional commit message, commits |
| `/git-commit-message` | — | Generates a conventional commit message from branch changes (no commit) |
| `/git-merge` | — | Coordinates merge / rebase / `rebase --onto` workflows with conflict handling |
| `/git-setup` | — | Interactive, verification-first, non-destructive Git configuration assistant |
| `/pull-request` | `[branch=origin/main]` `[createPullRequest=false]` | Generates a PR description from branch diffs using the pr-reference workflow |
| `/pr-review` | `[pr=...]` `[base=...]` `[head=...]` `[scope=...]` | Reviews a PR or local change set via the consolidated Code Review agent |
| `/pr-reference` | — | Generates PR reference XML: commit history + unified diffs between branches, with filtering |

### Code review

| Command | Arguments | What it does |
|---|---|---|
| `/code-review` | — | Multi-perspective review (functional, security, standards, accessibility, readiness…) with depth tiers and structured findings, fanning out to reviewer subagents |

### Security

| Command | Arguments | What it does |
|---|---|---|
| `/security-review` | `[scope=...]` `[mode=audit\|diff\|plan]` `[targetSkill=owasp-...]` | OWASP vulnerability assessment of the codebase; pick the framework via `targetSkill` |
| `/security-review-web` | `[scope=...]` | OWASP Top 10 web assessment (no codebase profiling) |
| `/security-review-llm` | `[scope=...]` | OWASP LLM + Agentic AI vulnerability assessment with codebase profiling |
| `/security-review-sbd` | `[scope=...]` | Secure by Design assessment per UK/AU government guidance |
| `/security-capture` | — | Security planning from existing notes (Security Planner, capture mode) |
| `/security-plan-from-prd` | — | Security planning derived from PRD/BRD artifacts |
| `/security-planning` | — | Reference set: STRIDE, NIST control families, standards mapping, threat-model (.tm7) generation |
| `/incident-response` | `[description]` `[severity=1-4]` `[phase=triage\|diagnose\|mitigate\|rca]` | Incident response workflow for Azure operations scenarios |
| `/risk-register` | `[project-name]` `[focus-area]` | Qualitative risk register using a Probability × Impact matrix |

### Supply chain security & VEX

| Command | Arguments | What it does |
|---|---|---|
| `/sssc-capture` | — | Supply chain security planning from existing knowledge (SSSC Planner) |
| `/sssc-from-prd` / `/sssc-from-brd` | — | Supply chain planning derived from PRD / BRD artifacts |
| `/sssc-from-security-plan` | — | Extends an existing Security Plan with supply chain coverage |
| `/supply-chain-security` | — | Reference for OpenSSF Scorecard, SLSA, Sigstore, SBOM, posture taxonomies |
| `/vex-scan` | `[scope=...]` `[product=pkg:...]` | Full VEX pipeline: scan dependencies, enrich CVEs, analyze exploitability, draft OpenVEX |
| `/vex-triage` | `report=path.json` `[product=...]` | Triage CVEs from an existing scan report or SBOM, skipping the scan |
| `/vex-implement` | `[scope=...]` `[product=...]` | Plans the backlog to stand up VEX in a target project |

### Responsible AI

| Command | Arguments | What it does |
|---|---|---|
| `/rai-capture` | — | Responsible AI assessment planning from existing knowledge |
| `/rai-plan-from-prd` | — | RAI planning from PRD/BRD artifacts |
| `/rai-plan-from-security-plan` | — | RAI planning from a completed Security Plan (recommended path) |

### Project planning & backlog

| Command | Arguments | What it does |
|---|---|---|
| `/backlog-plan` | `[discover\|my-work\|task-plan\|triage\|sprint\|resume]` | Read-only backlog planning for ADO, GitHub, and Jira |
| `/backlog-execute` | `[add\|run]` `[--dry-run]` `[--autonomy ...]` | Mutating backlog execution: create items or apply a reviewed handoff to a tracker |
| `/backlog-templates` | — | Shared work-item templates for ADO/GitHub handoffs (used by the planners) |
| `/functional-planner` | `[prd path]` `[platform=ado\|github\|jira]` | Turns a PRD into a validated work-item hierarchy handoff |
| `/jira` | `[setup\|search\|get\|create\|update\|transition\|comment\|fields]` | Jira workflows via REST API, including credential setup and JQL search |
| `/outcome-hypothesis` | `[context=...]` `[mode=create\|assess]` | Creates or assesses a falsifiable business-outcome hypothesis with indicators |
| `/performance-slo-planner` | `[journeys=...]` `[traffic=...]` | SLO/SRE planning: latency budgets, capacity, load/stress/soak test plans |
| `/proposal-response` | `[operation=analyze\|contribute\|draft]` | Builds traceable RFI/RFP/tender/questionnaire responses from approved sources |

### Design thinking & UX

| Command | Arguments | What it does |
|---|---|---|
| `/dt-start-project` | `project-slug=...` `[context=...]` | Starts a Design Thinking coaching project with persistent state |
| `/dt-resume-coaching` | `project-slug=...` | Resumes a DT coaching session from saved state |
| `/dt-method-next` | `[project-slug=...]` | Assesses project state and recommends the next DT method |
| `/dt-method-04-ideation` / `-04-convergence` | `project-slug=...` | Method 4: divergent ideation, then theme clustering |
| `/dt-method-05-concepts` / `-05-evaluation` | `project-slug=...` | Method 5: concept articulation, then stakeholder evaluation |
| `/dt-method-06-planning` / `-06-building` / `-06-testing` | `project-slug=...` | Method 6: prototype approach, scrappy building, hypothesis testing |
| `/dt-handoff-problem-space` / `-solution-space` / `-implementation-space` | `project-slug=...` | Compiles DT phases into research-ready input for `/rpi-research` |
| `/dt-canonical-deck` | `[project-slug=...]` `[action=offer\|build\|run]` | Canonical deck snapshots and optional PowerPoint build |
| `/dt-figma-export` | `project-slug=...` | Exports DT artifacts to FigJam/Figma (needs Figma MCP server) |
| `/ux-artifacts` | `[mode=frame-needs\|map-journey\|...]` | Produces evidence-labelled UX needs/journey/structure/handoff artifacts |
| `/ux-coaching` | `[moment=problem-framing\|critique\|...]` | Coaches through UX problem framing, critiques, stakeholder advocacy |

### Architecture, accessibility & data

| Command | Arguments | What it does |
|---|---|---|
| `/c4-architecture` | — | C4 model documentation (Context/Container/Component + deployment diagrams) |
| `/architecture-diagrams` | — | Cloud infrastructure / data-catalog diagrams as ASCII or Mermaid |
| `/accessibility-coverage-matrix` | `scope=...` `frameworks=wcag-22\|...` `mode=build\|...` | Builds/refreshes an accessibility coverage matrix (WCAG 2.2, ARIA APG, 508…) |
| `/synth-data-generate` | — | Generates synthetic data with realistic patterns and relationships |

### Azure DevOps integration *(needs an ADO MCP server)*

| Command | Arguments | What it does |
|---|---|---|
| `/ado-create-pull-request` | — | Creates an ADO PR with generated description, linked work items, reviewers |
| `/ado-get-build-info` | — | Retrieves ADO build status and logs for a PR or build number |

### HVE authoring & testing (meta — for building your own prompts/skills/agents)

| Command | Arguments | What it does |
|---|---|---|
| `/hve-builder` | `[targets=...]` `[mode=create\|improve\|refactor\|...]` | Authors, reviews, or validates prompt-engineering artifacts |
| `/hve-builder-tester` | `[targets=...]` `[profile=high\|medium\|low]` | Black-box behavior testing of artifacts with independent grading |
| `/prompt-builder` / `/prompt-analyze` / `/prompt-refactor` | `[promptFiles=...]` | Compatibility aliases routing to hve-builder modes |
| `/vally-tests` / `/vally-test-write` | `[files=...]` | Authors Vally conformance tests incl. jailbreak/injection refusal stimuli |
| `/evals-import` | `[path=...]` | Imports a CSV/XLSX corpus into Vally eval suites |

### Experimental & misc

| Command | Arguments | What it does |
|---|---|---|
| `/pptx` | `{action=create\|update\|cleanup\|from-existing}` | Creates or manages PowerPoint decks |
| `/cspell-config` | — | Creates/updates the project cspell configuration |
| `/graph-research` | `topic=...` | RPI research over an existing graphify knowledge graph |
| `/copilot-otel-metrics` | `[local-setup\|local-stack\|org-distribution\|azure-capture]` | Sets up Copilot OpenTelemetry capture with Grafana/Azure dashboards |

---

## Cheat sheet

### Argument syntax

All commands take space-separated `key=value` pairs; bare text without `key=` is the primary input:

```
/rpi task=add retry logic to the export service
/rpi-research topic=how OptosysCloud handles auth token refresh
/security-review scope=src/api mode=audit targetSkill=owasp-top-10
/vex-scan scope=. product=pkg:npm/@myorg/myapp
```

### The RPI loop (recommended daily driver)

```
/rpi-research topic=<what you need to learn>     # evidence → .copilot-tracking/research/
/clear                                           # reset context; the artifact survives
/rpi-plan task=<the change>                      # plan + phase details from research
/rpi-plan-critique                               # optional: independent plan critique
/clear
/rpi-implement                                   # execute plan, log changes/divergences
/clear
/rpi-review                                      # verify vs plan, route follow-ups
```

- One-shot instead: `/rpi-quick task=...` (all phases, one command).
- Coordinated with state tracking: `/rpi task=...`, resume later with `/rpi continue=yes`, pick a review follow-up with `/rpi followUp=1`.
- `/clear` between phases is the intended pattern — each phase reads the previous phase's artifact, not the chat history.
- Understand unfamiliar code first: `/rpi-walkthrough target=src/billing detail=deep`.
- Stress-test a decision before building: `/rpi-challenger subject=<the plan or assumption>`.

### Common flows

| Goal | Flow |
|---|---|
| Commit my work properly | `/git-commit` (or `/git-commit-message` to review first) |
| Open a PR | `/pull-request branch=origin/main` → review body → push/create |
| Review a PR | `/pr-review pr=123` or `/code-review` for local changes |
| Security audit | `/security-review scope=src` → findings → `/rpi task=fix <finding>` |
| CVE / SBOM triage | `/vex-scan product=pkg:npm/...` → review drafted OpenVEX |
| PRD → backlog | `/functional-planner <prd path> platform=ado` → `/backlog-execute run <handoff> --dry-run` |
| Plan performance/SLOs | `/performance-slo-planner journeys=<critical flows>` |
| Idea → build | `/dt-start-project project-slug=x` → dt methods → `/dt-handoff-solution-space` → `/rpi` |

### Where things end up

- **Research artifacts**: `.copilot-tracking/research/YYYY-MM-DD-*.md`
- **Plans / phase details / critiques**: `.copilot-tracking/plans/`
- **Change logs & divergences**: `.copilot-tracking/changes/`
- **Reviews**: `.copilot-tracking/reviews/`
- All inside the repo you run the command from. Add `.copilot-tracking/` to `.gitignore` if you don't want them committed.

### Gotchas

- **Name collisions**: `/code-review` and `/security-review` also exist as Claude Code built-in skills. The plugin versions are always reachable namespaced: `/hve:code-review`, `/hve:security-review`. A user-level command with the same bare name shadows the plugin's bare name too.
- **Integrations**: `/ado-*`, `/jira`, `/dt-figma-export`, and Mural-related flows expect the matching MCP server to be connected, exactly as they would in Copilot.
- **New commands need a fresh session** — an already-open session won't see newly added command files.
- The mirror at `~/.claude/hve/` is generated — don't hand-edit it; changes will be lost on re-sync.

### Updating

This plugin tracks upstream through a scheduled GitHub Action in the repo
(`.github/workflows/sync-upstream.yml`): every Monday (or on manual dispatch) it
re-converts from microsoft/hve-core, commits the result, and syncs the plugin
version. On your machine:

```
/plugin marketplace update hve-claude
```

or enable auto-update for this marketplace in `/plugin` → **Marketplaces** (off by
default for third-party marketplaces) — Claude Code then refreshes it shortly after
session startup, VS Code-extension style.

For a standalone install without the plugin system:

```bash
git clone --depth 1 https://github.com/microsoft/hve-core.git /tmp/hve-core
python tools/convert_hve.py /tmp/hve-core --target user   # writes into ~/.claude
```

Don't combine both installs — the user-level copies shadow the plugin's bare command names and everything shows up twice.
