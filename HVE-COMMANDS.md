# HVE Commands for Claude Code

Distributed as the `hve` Claude Code plugin (repo: silviuo/hve-claude). Ported from [microsoft/hve-core](https://github.com/microsoft/hve-core) v3.2.2 (MIT) on 2026-09-02 and re-synced weekly (see [Updating](#updating)).
HVE ("Hypervelocity Engineering") is Microsoft's agentic SDLC framework built for GitHub Copilot; this port makes its command set available as Claude Code slash commands, with the same workflows and the same durable artifacts.

## Install

```
/plugin marketplace add silviuo/hve-claude
/plugin install hve@hve-claude
```

## Where everything lives

| Location | Contents |
|---|---|
| `commands/` | One slash command per user-invocable hve skill |
| `agents/` | One Claude subagent per hve `.agent.md` file (planners, reviewers, orchestrators and their subagents) |
| `hve/.github/` | Pristine mirror of hve's skills / instructions / agents trees — commands read their playbooks, references, and templates from here |
| `tools/convert_hve.py` | The converter (plugin + user targets; see [Updating](#updating)) |
| `.copilot-tracking/` *(in your working repo)* | Durable workflow artifacts (research, plans, change logs, reviews) — same convention as upstream |

Installed as a plugin, the commands are available in every repo you open with Claude Code — bare (`/rpi-plan`) when the name is free, and always namespaced (`/hve:rpi-plan`). Artifacts land in the repo you run them from.

## What was changed during conversion

The content is upstream hve-core, with only mechanical adaptations to run outside GitHub Copilot:

1. **`${input:name}` variables → `$ARGUMENTS`** — Copilot's named-input syntax became a parsing note: commands take space-separated `key=value` pairs; bare text is the primary input.
2. **`#file:` directives stripped** — Copilot's file-import syntax was replaced with plain paths that Claude reads directly.
3. **Skills become commands** — every hve skill marked `user-invocable: true` becomes a slash command that reads and follows its `SKILL.md`. Until upstream retired its prompt files in October 2026, prompts were converted into commands too (see [Retired commands](#retired-commands)).
4. **All cross-references rewritten** — every link between skills, agents, and instruction files points to its new location; the mirror keeps relative links intact. Includes a fix for two upstream files that share the basename `pull-request.instructions.md`.
5. **Skill-loading adapter notes added** — Copilot auto-loads "skills" by name; Claude does not, so every converted agent and command carries a note pointing to the skill playbooks at `~/.claude/hve/.github/skills/*/<name>/SKILL.md`.
6. **Copilot chat-only features dropped** — handoff buttons and `disable-model-invocation` flags have no Claude equivalent; the workflows' own "Next Steps" guidance replaces them.

---

## Command reference

### RPI workflow — the core lifecycle

Research → Plan → Implement → Review → Follow-up, with durable artifacts under `.copilot-tracking/` so work survives context resets.

| Command | Arguments | What it does |
|---|---|---|
| `/rpi-research` | `[topic=...]` `[posture=balanced\|focused\|expansive]` `[chat]` | Research-only: gathers evidence in wider/deeper/contrarian waves, writes a dated artifact under `.copilot-tracking/research/` |
| `/rpi-plan` | `[task=...]` `[research=...]` `[draft=...]` `[decisions=...]` `[critique=standard\|deep\|skip]` | Builds an evidence-based implementation plan plus phase details from the research |
| `/rpi-plan-critique` | `[plan=...]` `[evidence=...]` `[depth=standard\|deep]` | Independent read-only critique of a plan before implementation |
| `/rpi-implement` | `[plan=...]` `[phase=...]` `[task=...]` | Executes the approved plan, recording amendments, divergences, and a changes log |
| `/rpi-review` | `[task=...]` `[plan=...]` `[changes=...]` `[depth=standard\|deep]` | Compares plan vs. implementation evidence, records findings, routes follow-up work |
| `/rpi-walkthrough` | `[target=...]` `[detail=brief\|normal\|deep]` `[chat]` | Guided walkthrough explaining code, features, or `.copilot-tracking` artifacts with evidence links |
| `/rpi-challenger` | `[subject=...]` `[artifacts=...]` `[focus=...]` | Adversarial questioning of a task, decision, plan, or artifact to expose assumptions before acting |

For the whole lifecycle with state tracking in one go, use the `rpi-agent` agent (see [Using hve agents](#using-hve-agents)).

### Git & pull requests

| Command | Arguments | What it does |
|---|---|---|
| `/git-commit` | `[mode=commit\|message-only]` | Stages the paths you choose, confirms the staged set, and creates one Conventional Commit; `mode=message-only` only writes the message |
| `/git-merge` | `operation=merge\|rebase\|rebase-onto` `branch=<ref>` `[onto=<ref>]` | Coordinates merge / rebase / `rebase --onto` workflows with conflict handling (asks for the branch; no default) |
| `/git-setup` | — | Interactive, verification-first, non-destructive Git configuration assistant |
| `/pull-request` | `[base=auto]` `[draft=false]` `[action=prepare\|create\|update]` | Drafts or opens a GitHub PR with changed-area preflight checks; Azure DevOps repos are routed to the backlog-management PR protocol |
| `/pr-reference` | — | Generates PR reference XML: commit history + unified diffs between branches, with filtering |

### Code review

| Command | Arguments | What it does |
|---|---|---|
| `/code-review` | — | Multi-perspective review (functional, security, standards, accessibility, readiness…) with depth tiers and structured findings, fanning out to reviewer subagents |

### Security & supply chain

| Command | Arguments | What it does |
|---|---|---|
| `/security-planning` | — | Reference set: STRIDE, NIST control families, standards mapping, threat-model (.tm7) generation |
| `/incident-response` | `incident-description=...` `[severity=1-4]` `[phase=triage\|diagnose\|mitigate\|rca]` | Incident response workflow for Azure operations scenarios |
| `/risk-register` | `[project-name=...]` `[focus-area=...]` | Qualitative risk register using a Probability × Impact matrix |
| `/supply-chain-security` | — | Reference for OpenSSF Scorecard, SLSA, Sigstore, SBOM, posture taxonomies |

Security reviews, security / supply-chain / Responsible AI planning, and VEX scans run through agents: see [Using hve agents](#using-hve-agents).

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
| `/dt-figma-export` | `project-slug=...` `[output-type=figjam\|design\|both]` | Exports DT artifacts to FigJam/Figma (needs Figma MCP server) |
| `/ux-artifacts` | `[mode=frame-needs\|map-journey\|...]` | Produces evidence-labelled UX needs/journey/structure/handoff artifacts |
| `/ux-coaching` | `[moment=problem-framing\|critique\|...]` | Coaches through UX problem framing, critiques, stakeholder advocacy |
| `/demo-setup` | — | Repeatable HVE demo setup: simulates DT Coach sessions with a customer persona and scaffolds a hi-fi prototype |

Design Thinking coaching itself (starting or resuming a project, the methods, space handoffs, the canonical deck) runs through the `dt-coach` agent.

### Architecture, accessibility & data

| Command | Arguments | What it does |
|---|---|---|
| `/c4-architecture` | — | C4 model documentation (Context/Container/Component + deployment diagrams) |
| `/architecture-diagrams` | — | Cloud infrastructure / data-catalog diagrams as ASCII or Mermaid |
| `/accessibility-coverage-matrix` | `scope=...` `frameworks=wcag-22\|...` `mode=build\|...` | Builds/refreshes an accessibility coverage matrix (WCAG 2.2, ARIA APG, 508…) |
| `/synth-data-generate` | `subject=...` `[example_data=...]` | Generates synthetic data with realistic patterns and relationships |

### Engagement reporting

| Command | Arguments | What it does |
|---|---|---|
| `/engagement-reporting` | `[report type]` `[reporting period]` | Source-grounded internal or external weekly engagement status reports, with optional Outlook draft |
| `/engagement-report-council-critique` | `report-date=...` `report-type=...` `draft=...` `research=...` | One independent Council critique of a report draft against research evidence |

### HVE authoring & testing (meta — for building your own prompts/skills/agents)

| Command | Arguments | What it does |
|---|---|---|
| `/hve-builder` | `[targets=...]` `[mode=create\|improve\|refactor\|...]` | Authors, reviews, or validates prompt-engineering artifacts |
| `/hve-artifact-authoring` | `[targets=...]` `[artifact-type=agent\|prompt\|instruction\|skill]` | Creates and validates HVE-style artifacts with current frontmatter and validation conventions |
| `/hve-slides` | `[deck=slides/<name>]` `[mode=create\|update\|review]` | Presentation-first HTML slide decks about HVE Core |
| `/vally-tests` | `[mode=from-artifact\|corpus-import]` `[files=...]` `[path=...]` | Authors Vally conformance tests from an artifact or imports a CSV/XLSX corpus; refuses jailbreak/injection stimuli |

### Experimental & misc

| Command | Arguments | What it does |
|---|---|---|
| `/cspell-config` | — | Creates/updates the project cspell configuration |
| `/copilot-otel-metrics` | `[local-setup\|local-stack\|org-distribution\|azure-capture]` | Sets up Copilot OpenTelemetry capture with Grafana/Azure dashboards |

---

## Using hve agents

Some hve workflows have no slash command: in Copilot you start them by picking the agent from the agent picker. In Claude Code, ask for the agent in plain words:

- **Interactive agents** (they ask you questions as they go): ask Claude to adopt the agent in the main conversation, for example `Adopt the hve rpi-agent agent and follow its spec: add retry logic to the export service`. Claude reads `agents/rpi-agent.md` and follows it.
- **Self-contained jobs**: ask Claude to launch the agent as a subagent, for example `Run the hve:security-reviewer agent on src/api in audit mode`.

| Agent | Use it for |
|---|---|
| `rpi-agent` | One task through Research → Plan → Implement → Review → Follow-up with persisted state, in manual or automatic mode |
| `code-review` | Reviewing the PR you name, the open PR for your branch, a branch diff, or local changes |
| `security-reviewer` | OWASP audits (`mode`, `scope`, `targetSkill`, `plan` inputs); ask for an LLM and agentic, web application, or Secure by Design review |
| `security-planner` | Security planning from existing notes (`capture`) or from a PRD/BRD (`from-prd`) |
| `sssc-planner` | Supply chain security planning from nothing, a PRD, a BRD, or a completed security plan; VEX stand-up planning |
| `sssc-reviewer` | VEX scans (`scope`, `product`) and triage of an existing Trivy, OSV-Scanner, or SPDX report (`report=<path>`) |
| `rai-planner` | Responsible AI assessment planning from nothing, a PRD/BRD, or a completed security plan |
| `dt-coach` | Design Thinking coaching: start or resume a project, the next method, methods 4–6, space handoffs to RPI, the canonical deck |
| `pptx` | Creating, updating, or managing PowerPoint decks |

All agents, including the reviewer and assessor subagents these orchestrators launch, are in `agents/`.

## Retired commands

Upstream hve-core retired all of its prompt files on 2026-10-07 ([microsoft/hve-core#3111](https://github.com/microsoft/hve-core/pull/3111)), so the commands converted from them left this plugin with the first sync after that (v3.2.8). Upstream's replacement for each, from its [migration guide](https://github.com/microsoft/hve-core/blob/main/docs/getting-started/package-migration.md#retired-prompt-commands):

| Retired command | Use instead |
|---|---|
| `/rpi` | The `rpi-agent` agent; describe the task. Or run the phases yourself with `/rpi-research` → `/rpi-plan` → `/rpi-implement` → `/rpi-review` |
| `/pr-review` | The `code-review` agent |
| `/git-commit-message` | `/git-commit mode=message-only` |
| `/ado-create-pull-request` | `/pull-request action=create` (routes Azure DevOps repos to the backlog-management PR protocol) |
| `/ado-get-build-info` | Ask for the build status; the `backlog-management` skill carries the Azure DevOps build reference |
| `/vally-test-write` | `/vally-tests mode=from-artifact files=<path>` |
| `/evals-import` | `/vally-tests mode=corpus-import path=<corpus>` |
| `/prompt-builder` / `/prompt-analyze` / `/prompt-refactor` | `/hve-builder` in create/improve, review, or refactor mode |
| `/security-review`, `/security-review-llm`, `/security-review-web`, `/security-review-sbd` | The `security-reviewer` agent; ask for the kind of review |
| `/security-capture`, `/security-plan-from-prd` | The `security-planner` agent; start without a PRD/BRD, or point it at one |
| `/sssc-capture`, `/sssc-from-prd`, `/sssc-from-brd`, `/sssc-from-security-plan`, `/vex-implement` | The `sssc-planner` agent; say which input to start from, or ask it to plan VEX |
| `/vex-scan`, `/vex-triage` | The `sssc-reviewer` agent; ask for a VEX scan, or to triage an existing report |
| `/rai-capture`, `/rai-plan-from-prd`, `/rai-plan-from-security-plan` | The `rai-planner` agent; say which input to start from |
| `/dt-start-project`, `/dt-resume-coaching`, `/dt-method-*`, `/dt-handoff-*`, `/dt-canonical-deck` | The `dt-coach` agent; describe what you want |
| `/pptx` | The `pptx` agent |

---

## Cheat sheet

### Argument syntax

All commands take space-separated `key=value` pairs; bare text without `key=` is the primary input:

```
/rpi-research topic=how OptosysCloud handles auth token refresh
/rpi-plan task=add retry logic to the export service
/git-merge operation=rebase branch=origin/main
/backlog-plan triage
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

- Coordinated with state tracking instead: the `rpi-agent` agent (see [Using hve agents](#using-hve-agents)); ask it to resume and it continues from its recorded phase.
- `/clear` between phases is the intended pattern — each phase reads the previous phase's artifact, not the chat history.
- Understand unfamiliar code first: `/rpi-walkthrough target=src/billing detail=deep`.
- Stress-test a decision before building: `/rpi-challenger subject=<the plan or assumption>`.

### Common flows

| Goal | Flow |
|---|---|
| Commit my work properly | `/git-commit` (or `/git-commit mode=message-only` to review the message first) |
| Open a PR | `/pull-request action=prepare` → review body → `/pull-request action=create` |
| Review a PR | The `code-review` agent with the PR number, or `/code-review` for local changes |
| Security audit | The `security-reviewer` agent on `src` → findings → `/rpi-plan task=fix <finding>` |
| CVE / SBOM triage | The `sssc-reviewer` agent: VEX scan with `product=pkg:npm/...` → review drafted OpenVEX |
| PRD → backlog | `/functional-planner <prd path> platform=ado` → `/backlog-execute run <handoff> --dry-run` |
| Plan performance/SLOs | `/performance-slo-planner journeys=<critical flows>` |
| Idea → build | The `dt-coach` agent: start a project → methods → solution-space handoff → `/rpi-research` |

### Where things end up

- **Research artifacts**: `.copilot-tracking/research/YYYY-MM-DD-*.md`
- **Plans / phase details / critiques**: `.copilot-tracking/plans/`
- **Change logs & divergences**: `.copilot-tracking/changes/`
- **Reviews**: `.copilot-tracking/reviews/`
- All inside the repo you run the command from. Add `.copilot-tracking/` to `.gitignore` if you don't want them committed.

### Gotchas

- **Name collisions**: `/code-review` also exists as a Claude Code built-in skill. The plugin version is always reachable namespaced: `/hve:code-review`. A user-level command with the same bare name shadows the plugin's bare name too.
- **Integrations**: Azure DevOps flows (`/pull-request` on ADO repos, `/backlog-*` with `platform=ado`), `/jira`, `/dt-figma-export`, and Mural-related flows expect the matching MCP server to be connected, exactly as they would in Copilot.
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
