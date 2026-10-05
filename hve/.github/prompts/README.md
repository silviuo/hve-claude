---
title: GitHub Copilot Prompts
description: Coaching and guidance prompts for specific development tasks that provide step-by-step assistance and context-aware support
author: Edge AI Team
ms.date: 2026-09-28
ms.topic: hub-page
estimated_reading_time: 3
keywords:
  - github copilot
  - prompts
  - ai assistance
  - coaching
  - guidance
  - development workflows
---

## GitHub Copilot Prompts

This directory contains **coaching and guidance prompts** designed to provide step-by-step assistance for specific development tasks. Unlike instructions that focus on systematic implementation, prompts offer educational guidance and context-aware coaching to help you learn and apply best practices. Prompts are organized by workflow focus area: planning and RPI, source control, pull requests and review, prompt engineering, Design Thinking, Responsible AI, security, accessibility, data science, and experimental tools.

Backlog and work item workflows are not prompts. They are user-invocable skills that discover the active tracker at runtime and work the same way against Azure DevOps, GitHub, and Jira. See [Backlog & Work Item Management](#backlog--work-item-management).

## How to Use Prompts

Prompts can be invoked in GitHub Copilot Chat using `/prompt-name` syntax (for example, `/rpi` or `/git-commit`). They provide:

* **Educational Guidance**: Step-by-step coaching approach
* **Context-Aware Assistance**: Project-specific guidance and examples
* **Best Practices**: Established patterns and conventions
* **Interactive Support**: Conversational assistance for complex tasks

## Available Prompts

### Onboarding, Research & Planning

* **[RPI](${CLAUDE_PLUGIN_ROOT}/commands/rpi.md)** - Coordinates one task through Research, Plan, Implement, Review, and Follow-up with the RPI Agent and matching `rpi-*` skills

Use `/rpi-research`, `/rpi-plan`, `/rpi-implement`, or `/rpi-review` when you need one bounded RPI phase. Resume longer work from the durable artifacts owned by that workflow rather than from a generic conversation checkpoint.

### Source Control & Commit Quality

* **[Git Commit (Select + Commit)](${CLAUDE_PLUGIN_ROOT}/commands/git-commit.md)** - Stages selected whole paths and confirms the exact staged set before creating a Conventional Commit
* **[Git Commit Message Generator](${CLAUDE_PLUGIN_ROOT}/commands/git-commit-message.md)** - Generates a compliant commit message for currently staged changes
* **[Git Merge](${CLAUDE_PLUGIN_ROOT}/commands/git-merge.md)** - Git merge, rebase, and rebase --onto workflows with conflict handling
* **[Git Setup](${CLAUDE_PLUGIN_ROOT}/commands/git-setup.md)** - Verification-first Git configuration assistant

### Pull Requests & Code Review

* **[Pull Request](../skills/hve-core/pull-request/SKILL.md)** - Prepare, create, or update a concise pull request with targeted preflight checks
* **[PR Review](${CLAUDE_PLUGIN_ROOT}/commands/pr-review.md)** - Review a pull request or local change set via the consolidated Code Review agent

### Prompt Engineering & Evaluation

* **[Vally Test Write](${CLAUDE_PLUGIN_ROOT}/commands/vally-test-write.md)** - Author Vally conformance test stimuli for an existing prompt, instructions, agent, or skill
* **[Evals Import](${CLAUDE_PLUGIN_ROOT}/commands/evals-import.md)** - Import a CSV or XLSX corpus into Vally eval suites with safety lint and dedupe

Use the `hve-builder` skill to create, improve, refactor, review, or validate prompt-engineering artifacts. The retained `prompt-builder`, `prompt-analyze`, and `prompt-refactor` skills are compatibility aliases that route legacy requests to `hve-builder`; they are not prompt files or independent lifecycle owners. Vally conformance authoring remains owned by `Vally Test Author` and the `vally-tests` skill.

### Backlog & Work Item Management

These workflows are skills rather than prompts. Each resolves the active tracker at runtime, so the same command serves Azure DevOps, GitHub, and Jira instead of requiring a per-platform variant.

* **[Backlog Plan](../skills/project-planning/backlog-plan/SKILL.md)** - Read-only discovery, assigned work, task planning, triage assessment, sprint planning, and session resume
* **[Backlog Execute](../skills/project-planning/backlog-execute/SKILL.md)** - Create and update tracker items, either one at a time or from a reviewed handoff file
* **[Functional Planner](${CLAUDE_PLUGIN_ROOT}/agents/functional-planner.md)** - Turn PRD and BRD artifacts into a planned item hierarchy before anything is written to a tracker
* **[Backlog Manager](${CLAUDE_PLUGIN_ROOT}/agents/backlog-manager.md)** - Orchestrate the above across a longer multi-step backlog session

### Platform Setup & Delivery Context

* **[Jira Skill](../skills/project-planning/jira/SKILL.md)** - Configure local Jira access and use the CLI directly
* **[GitLab Skill](../skills/project-planning/gitlab/SKILL.md)** - Inspect merge requests, comments, pipelines, jobs, and logs for GitLab-hosted delivery workflows

### Azure DevOps Pull Requests & Builds

* **[ADO Create Pull Request](${CLAUDE_PLUGIN_ROOT}/commands/ado-create-pull-request.md)** - Create Azure DevOps PRs with generated description, linked work items, and reviewers
* **[ADO Get Build Info](${CLAUDE_PLUGIN_ROOT}/commands/ado-get-build-info.md)** - Retrieve build status and logs for a PR or build number

### Design Thinking

* **[DT Start Project](${CLAUDE_PLUGIN_ROOT}/commands/dt-start-project.md)** - Start a new Design Thinking coaching project with state initialization
* **[DT Resume Coaching](${CLAUDE_PLUGIN_ROOT}/commands/dt-resume-coaching.md)** - Resume a coaching session by reading state and re-establishing context
* **[DT Method Next](${CLAUDE_PLUGIN_ROOT}/commands/dt-method-next.md)** - Assess project state and recommend the next method with sequencing validation
* **[DT Canonical Deck](${CLAUDE_PLUGIN_ROOT}/commands/dt-canonical-deck.md)** - Canonical deck workflow with snapshot generation and optional customer-card PowerPoint build
* **[DT Figma Export](${CLAUDE_PLUGIN_ROOT}/commands/dt-figma-export.md)** - Export Design Thinking artifacts to a FigJam board or Figma Design file
* **[DT Handoff - Problem Space](${CLAUDE_PLUGIN_ROOT}/commands/dt-handoff-problem-space.md)** - Compile Methods 1-3 outputs into an RPI-ready artifact for `rpi-research`
* **[DT Handoff - Solution Space](${CLAUDE_PLUGIN_ROOT}/commands/dt-handoff-solution-space.md)** - Compile Methods 4-6 outputs into an RPI-ready artifact for `rpi-research`
* **[DT Handoff - Implementation Space](${CLAUDE_PLUGIN_ROOT}/commands/dt-handoff-implementation-space.md)** - Compile Methods 7-9 outputs into an RPI-ready artifact for `rpi-research`

> **Note:** The per-method coaching prompts (`dt-method-04-*`, `dt-method-05-*`, `dt-method-06-*`) are driven by the DT Coach agent mid-session and are not typically invoked directly.

### Responsible AI

* **[RAI Capture](${CLAUDE_PLUGIN_ROOT}/commands/rai-capture.md)** - Start RAI assessment planning from existing knowledge (capture mode)
* **[RAI Plan from PRD](${CLAUDE_PLUGIN_ROOT}/commands/rai-plan-from-prd.md)** - Start RAI assessment planning from PRD/BRD artifacts (from-prd mode)
* **[RAI Plan from Security Plan](${CLAUDE_PLUGIN_ROOT}/commands/rai-plan-from-security-plan.md)** - Start RAI assessment planning from a completed Security Plan (recommended)

### Security

* **[Security Capture](${CLAUDE_PLUGIN_ROOT}/commands/security-capture.md)** - Start security planning from existing notes (capture mode)
* **[Security Plan from PRD](${CLAUDE_PLUGIN_ROOT}/commands/security-plan-from-prd.md)** - Start security planning from PRD/BRD artifacts (from-prd mode)
* **[Security Review](${CLAUDE_PLUGIN_ROOT}/commands/security-review.md)** - OWASP vulnerability assessment against the current codebase with configurable mode, scope, and skill selection
* **[Security Review - Web](${CLAUDE_PLUGIN_ROOT}/commands/security-review-web.md)** - OWASP Top 10 web vulnerability assessment without codebase profiling
* **[Security Review - LLM](${CLAUDE_PLUGIN_ROOT}/commands/security-review-llm.md)** - OWASP LLM and Agentic vulnerability assessments with codebase profiling
* **[Security Review - Secure by Design](${CLAUDE_PLUGIN_ROOT}/commands/security-review-sbd.md)** - Secure by Design principles assessment per UK and Australian government guidance
* **[SSSC Capture](${CLAUDE_PLUGIN_ROOT}/commands/sssc-capture.md)** - Start supply chain security planning from existing knowledge (capture mode)
* **[SSSC from BRD](${CLAUDE_PLUGIN_ROOT}/commands/sssc-from-brd.md)** - Start supply chain security planning from BRD artifacts
* **[SSSC from PRD](${CLAUDE_PLUGIN_ROOT}/commands/sssc-from-prd.md)** - Start supply chain security planning from PRD artifacts
* **[SSSC from Security Plan](${CLAUDE_PLUGIN_ROOT}/commands/sssc-from-security-plan.md)** - Extend a Security Planner assessment with supply chain coverage
* **[VEX Scan](${CLAUDE_PLUGIN_ROOT}/commands/vex-scan.md)** - Full VEX pipeline: scan dependencies, enrich CVEs, analyze exploitability, and draft an OpenVEX document
* **[VEX Triage](${CLAUDE_PLUGIN_ROOT}/commands/vex-triage.md)** - Triage CVEs from an existing scan report or SBOM and draft an OpenVEX document
* **[VEX Implement](${CLAUDE_PLUGIN_ROOT}/commands/vex-implement.md)** - Plan the work to stand up VEX in a target project as a backlog for `rpi-implement`
* **[Incident Response](${CLAUDE_PLUGIN_ROOT}/commands/incident-response.md)** - Incident response workflow for Azure operations with triage, diagnostics, mitigation, and RCA phases
* **[Risk Register](${CLAUDE_PLUGIN_ROOT}/commands/risk-register.md)** - Generate a qualitative risk assessment with a P×I matrix and mitigation plans

### Accessibility

* **[Accessibility Coverage Matrix](${CLAUDE_PLUGIN_ROOT}/commands/accessibility-coverage-matrix.md)** - Build, refresh, report, or probe an accessibility coverage matrix across criteria, surfaces, and methods

### Data Science

* **[Synthetic Data Generation](${CLAUDE_PLUGIN_ROOT}/commands/synth-data-generate.md)** - Generate synthetic data for any subject with realistic patterns and relationships

### Experimental & Tools

* **[PowerPoint](${CLAUDE_PLUGIN_ROOT}/commands/pptx.md)** - Create, update, or manage PowerPoint slide decks
* **[cspell Config](${CLAUDE_PLUGIN_ROOT}/commands/cspell-config.md)** - Create or update the project cspell configuration with project words and ignores

## Prompts vs Instructions vs Custom Agents

* **Prompts** (this directory): Coaching and educational guidance for learning
* **[Instructions](../instructions/README.md)**: Systematic implementation and automation
* **[Agents](../../docs/contributing/custom-agents.md)**: Specialized AI assistance with enhanced capabilities

## Quick Start

1. **Coordinating a complete task?** Use [RPI](${CLAUDE_PLUGIN_ROOT}/commands/rpi.md) with `/rpi task="<outcome>"`
2. **Working on one RPI phase?** Use `/rpi-research`, `/rpi-plan`, `/rpi-implement`, or `/rpi-review`
3. **Authoring an HVE artifact?** Use `hve-builder`; use the Vally prompts above only for conformance-test authoring or corpus import
4. **Committing changes?** Use [Git Commit Message Generator](${CLAUDE_PLUGIN_ROOT}/commands/git-commit-message.md) or [Git Commit](${CLAUDE_PLUGIN_ROOT}/commands/git-commit.md)
5. **Handling merge conflicts?** Use [Git Merge](${CLAUDE_PLUGIN_ROOT}/commands/git-merge.md)
6. **Setting up Git?** Use [Git Setup](${CLAUDE_PLUGIN_ROOT}/commands/git-setup.md)
7. **Tracking your work?** Use the [Backlog Plan](../skills/project-planning/backlog-plan/SKILL.md) skill in `my-work` mode, then `task-plan` mode
8. **Creating Azure DevOps PRs?** Use [ADO Create Pull Request](${CLAUDE_PLUGIN_ROOT}/commands/ado-create-pull-request.md)
9. **Checking build status?** Use [ADO Get Build Info](${CLAUDE_PLUGIN_ROOT}/commands/ado-get-build-info.md)
10. **Creating or updating tracker items?** Use the [Backlog Execute](../skills/project-planning/backlog-execute/SKILL.md) skill
11. **Working on PRs?** Use the [Pull Request](../skills/hve-core/pull-request/SKILL.md) skill
12. **Responding to Azure incidents?** Use [Incident Response](${CLAUDE_PLUGIN_ROOT}/commands/incident-response.md)
13. **Discovering or triaging a backlog?** Use the [Backlog Plan](../skills/project-planning/backlog-plan/SKILL.md) skill in `discover` or `triage` mode
14. **Need GitLab delivery context?** Review the [GitLab Skill](../skills/project-planning/gitlab/SKILL.md) for setup and command guidance
15. **Running a security review?** Use [Security Review](${CLAUDE_PLUGIN_ROOT}/commands/security-review.md) for full OWASP assessment

## Related Resources

* **[Contributing Guide](../../CONTRIBUTING.md)** - Complete guide to contributing to the project
* **[Instructions](../instructions/README.md)** - Comprehensive guidance files for development standards
* **[Agents](../../docs/contributing/custom-agents.md)** - Specialized AI assistance with enhanced capabilities

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
