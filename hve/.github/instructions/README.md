---
title: GitHub Copilot Instructions
description: Repository-specific coding guidelines and conventions for GitHub Copilot
author: HVE Core Team
ms.date: 2026-07-16
ms.topic: reference
keywords:
  - copilot
  - instructions
  - coding standards
  - guidelines
estimated_reading_time: 5
---

## GitHub Copilot Instructions

Repository-specific guidelines that GitHub Copilot automatically applies when
editing files. Instructions ensure consistent code style and conventions across
the codebase.

## How Instructions Work

1. Instruction files declare which file patterns they apply to using `applyTo`
   in frontmatter
2. GitHub Copilot reads instructions when editing matching files
3. Suggestions follow the documented standards automatically

Custom agents and the `hve-builder` skill respect these instructions and can create new ones.
See [Contributing Instructions](../../docs/contributing/instructions.md) for authoring guidance.

## Available Instructions

### Language and Technology

| File                                                                                                                           | Applies To                                     | Purpose                                  |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bash/bash.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bash/bash.instructions.md)                                       | `**/*.sh`                                      | Bash script implementation standards     |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bicep/bicep.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bicep/bicep.instructions.md)                                   | `**/bicep/**`                                  | Bicep infrastructure as code patterns    |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/diff-computation.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/diff-computation.instructions.md) | Code review agents                             | Diff computation for code review         |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/review-artifacts.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/review-artifacts.instructions.md) | `**/.copilot-tracking/reviews/code-reviews/**` | Code review artifact persistence         |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp.instructions.md)                               | `**/*.cs`                                      | C# implementation and coding conventions |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp-tests.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp-tests.instructions.md)                   | `**/*.cs`                                      | C# test code standards                   |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/powershell.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/powershell.instructions.md)               | `**/*.ps1, **/*.psm1, **/*.psd1`               | PowerShell scripting conventions         |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/pester.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/pester.instructions.md)                       | `**/*.Tests.ps1`                               | Pester testing conventions               |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-script.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-script.instructions.md)                               | `**/*.py`                                      | Python scripting implementation          |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-tests.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-tests.instructions.md)                                 | `**/*.py`                                      | Python test code standards               |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust.instructions.md)                                       | `**/*.rs`                                      | Rust development conventions             |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust-tests.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust-tests.instructions.md)                           | `**/*.rs`                                      | Rust test code standards                 |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/terraform/terraform.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/terraform/terraform.instructions.md)                   | `**/*.tf, **/*.tfvars, **/terraform/**`        | Terraform infrastructure as code         |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/uv-projects.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/uv-projects.instructions.md)                                   | `**/*.py, **/*.ipynb`                          | Python virtual environments using uv     |

### Documentation and Content

| File                                                                             | Applies To                                                         | Purpose                               |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/markdown.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/markdown.instructions.md)           | `**/*.md`                                                          | Markdown formatting standards         |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/writing-style.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/writing-style.instructions.md) | `**/*.md`                                                          | Voice, tone, and language conventions |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/hve-builder.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/hve-builder.instructions.md)     | `**/*.prompt.md, **/*.agent.md, **/*.instructions.md, **/SKILL.md` | HVE artifact authoring standards      |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/docusaurus-edits.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/docusaurus-edits.instructions.md)             | `docs/**`                                                          | Docusaurus documentation authoring    |

### Git and Workflow

| File                                                                               | Applies To                   | Purpose                              |
|------------------------------------------------------------------------------------|------------------------------|--------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/commit-message.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/commit-message.instructions.md) | Commit actions               | Conventional commit message format   |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/git-merge.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/git-merge.instructions.md)           | Git operations               | Merge, rebase, and conflict handling |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/pull-request.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/pull-request.instructions.md)                       | `**/.copilot-tracking/pr/**` | HVE Core pull request conventions    |

### Repository Workflow

| File                                                                                     | Applies To                              | Purpose                                          |
|------------------------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/copilot-tracking.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/copilot-tracking.instructions.md)   | `.copilot-tracking/**`                  | Intermediate tracking artifact conventions       |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/licensing-posture.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/licensing-posture.instructions.md) | `**/skills/**, **/.copilot-tracking/**` | Licensing, reproduction, and attribution posture |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/skill-security-model.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/skill-security-model.instructions.md)             | `**/${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/**/SECURITY.md`      | Per-skill STRIDE security model rules            |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/workflows.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/workflows.instructions.md)                                   | `**/.github/workflows/*.yml`            | GitHub Actions workflow conventions              |

### GitHub Integration

| File                                                                                                             | Applies To                                                                                                                                  | Purpose                              |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/community-interaction.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/community-interaction.instructions.md) | `**${CLAUDE_PLUGIN_ROOT}/agents/backlog-manager.md`, `**/${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/project-planning/backlog-management/references/github.md` | GitHub-facing communication patterns |

### Planning and Governance Agents

The instructions below are scoped to specific planning agents and their `.copilot-tracking/` working directories rather than to general source edits.

#### Accessibility

| File                                                                                                                       | Applies To                                                                  | Purpose                                     |
|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-identity.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-identity.instructions.md)               | `**/.copilot-tracking/accessibility/**`                                     | Accessibility Planner identity and workflow |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-license-posture.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-license-posture.instructions.md) | `**/${CLAUDE_PLUGIN_ROOT}/hve/.github/skills/accessibility/**, **/.copilot-tracking/accessibility/**` | Accessibility licensing overlay             |

#### Privacy

| File                                                                                 | Applies To                              | Purpose                               |
|--------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/privacy/privacy-identity.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/privacy/privacy-identity.instructions.md) | `**/.copilot-tracking/privacy-plans/**` | Privacy Planner identity and workflow |

#### Responsible AI

| File                                                                                                 | Applies To                                              | Purpose                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md)               | `**/.copilot-tracking/rai-plans/**`                     | RAI Planner identity and workflow |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-license-posture.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-license-posture.instructions.md) | `**/skills/rai**/**, **/.copilot-tracking/rai-plans/**` | RAI licensing overlay             |

#### Project Planning (ADRs)

| File                                                                                                   | Applies To                                                    | Purpose                                    |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-identity.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-identity.instructions.md)         | `**/.copilot-tracking/adr-plans/**, **/docs/planning/adrs/**` | ADR Creator identity and state machine     |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-standards.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-standards.instructions.md)       | `**/.copilot-tracking/adr-plans/**, **/docs/planning/adrs/**` | Embedded ADR standards (MADR, Y-Statement) |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-byo-template.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-byo-template.instructions.md) | `**/.copilot-tracking/adr-plans/**, **/docs/planning/adrs/**` | BYO ADR template contract                  |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-handoff.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-handoff.instructions.md)           | `**/.copilot-tracking/adr-plans/**, **/docs/planning/adrs/**` | ADR Govern-phase handoff protocol          |

#### Security

| File                                                                                     | Applies To                                                 | Purpose                                |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/identity.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/identity.instructions.md)                   | `**/.copilot-tracking/security-plans/**`                   | Security Planner identity and workflow |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/standards-mapping.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/standards-mapping.instructions.md) | `**/.copilot-tracking/security-plans/**`                   | OWASP and NIST standards references    |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/sssc-planner.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/sssc-planner.instructions.md)           | `**/.copilot-tracking/sssc-plans/**`                       | SSSC Planner identity and workflow     |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-standards.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-standards.instructions.md)         | `**/security/vex/**, **/.copilot-tracking/security/vex/**` | OpenVEX document standards             |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-generation.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-generation.instructions.md)       | Security reviewer agents                                   | VEX generation rules                   |

#### Shared Planner Scaffolds

| File                                                                                                   | Applies To                                                         | Purpose                                           |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/hve-core-location.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/hve-core-location.instructions.md)                   | `**`                                                               | Fallback location guidance for hve-core artifacts |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/content-policy-citation.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/content-policy-citation.instructions.md)       | `**/*.agent.md, **/*.prompt.md, **/*.instructions.md, **/SKILL.md` | Content-policy and terms-of-service guardrails    |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/coaching-patterns.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/coaching-patterns.instructions.md)                   | Planning agents                                                    | Exploration-first coaching patterns               |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/planner-identity-base.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/planner-identity-base.instructions.md)           | Planning agents                                                    | Shared planner identity scaffold                  |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md)               | Planning and review agents                                         | Professional-review disclaimer language           |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/telemetry-overlay.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/telemetry-overlay.instructions.md)                   | Planning and review agents                                         | Telemetry vocabulary overlay                      |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/untrusted-content-boundary.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/untrusted-content-boundary.instructions.md) | Planning and DT/UX agents                                          | Untrusted-content boundary rules                  |

#### Experimental

| File                                                                                                 | Applies To                    | Purpose                                       |
|------------------------------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------|
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/experiment-designer.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/experiment-designer.instructions.md) | `**/.copilot-tracking/mve/**` | MVE experiment designer conventions           |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/graphify.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/graphify.instructions.md)                       | `**/graphify-out/**`          | Graphify knowledge-graph evidence conventions |
| [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/pptx.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/pptx.instructions.md)                               | `**/.copilot-tracking/ppt/**` | PowerPoint builder conventions                |

The `experimental/mural/` directory holds the Mural workflow instruction set (bootstrap, seeding, writeback, and log-hygiene rules) scoped to the DT, RAI, and UX/UI agents; see [${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-bootstrap.instructions.md](${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-bootstrap.instructions.md) as the entry point.

### GitLab Workflow Entry Points

This README indexes instruction files. GitLab delivery support is currently discoverable through the local skill and provider-aware project-planning agents.

* Use [../skills/project-planning/gitlab/SKILL.md](../skills/project-planning/gitlab/SKILL.md) when delivery context lives in GitLab and you need merge request, pipeline, or job operations.
* Keep GitLab delivery workflows distinct from backlog planning unless GitLab is also the system of record for work tracking.

## XML-Style Blocks

Instructions use XML-style comment blocks for structured content:

* **Purpose**: Enables automated extraction, better navigation, and consistency
* **Format**: Kebab-case tags in HTML comments on their own lines
* **Examples**: `<!-- <example-bash> -->`, `<!-- <schema-config> -->`
* **Nesting**: Allowed with distinct tag names
* **Closing**: Always required with matching tag names

````markdown
<!-- <example-terraform> -->
```terraform
resource "azurerm_resource_group" "example" {
  name     = "example-rg"
  location = "eastus"
}
```
<!-- </example-terraform> -->
````

## Creating New Instructions

Activate the `hve-builder` skill:

1. Open Copilot Chat and ask to create or improve an instruction artifact
2. Provide context (files, folders, or requirements)
3. HVE Builder resolves the mode, write boundary, and applicable conventions
4. HVE Builder uses one behavior gate with route-specific execution: Major mutations and behavior-bearing review targets execute testing, while eligible no-runtime review targets and Minor or Medium mutations are satisfied-and-skipped
5. Known target files and caller-supplied canonical references remain bounded lifecycle reads; open-ended exploration and decision-critical research activate `rpi-research`
6. The retained `prompt-builder`, `prompt-analyze`, and `prompt-refactor` skills remain compatibility aliases
7. The final response reports each gate and an overall Pass, Revise, Deferred, or Blocked outcome

For manual creation, see [Contributing Instructions](../../docs/contributing/instructions.md).

## Directory Structure

```text
${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/
├── accessibility/                    # Accessibility planning
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-identity.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/accessibility/accessibility-license-posture.instructions.md
├── coding-standards/                 # Language and technology conventions
│   ├── bash/
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bash/bash.instructions.md
│   ├── bicep/
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/bicep/bicep.instructions.md
│   ├── code-review/
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/diff-computation.instructions.md
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/code-review/review-artifacts.instructions.md
│   ├── csharp/
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp.instructions.md
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/csharp/csharp-tests.instructions.md
│   ├── powershell/
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/pester.instructions.md
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/powershell/powershell.instructions.md
│   ├── rust/
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust.instructions.md
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/rust/rust-tests.instructions.md
│   ├── terraform/
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/terraform/terraform.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-script.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/python-tests.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/coding-standards/uv-projects.instructions.md
├── experimental/                     # Experimental workflows
│   ├── mural/
│   │   ├── destinations/
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-bootstrap.instructions.md
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-destinations.instructions.md
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-human-record.instructions.md
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-log-hygiene.instructions.md
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-seeding-patterns.instructions.md
│   │   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-writeback-hygiene.instructions.md
│   │   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/mural/mural-writing-style.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/experiment-designer.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/graphify.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/experimental/pptx.instructions.md
├── hve-core/                         # HVE Core workflow
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/commit-message.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/copilot-tracking.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/git-merge.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/licensing-posture.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/markdown.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/hve-builder.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/hve-core/writing-style.instructions.md
├── privacy/                          # Privacy planning
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/privacy/privacy-identity.instructions.md
├── project-planning/                 # Project planning and ADRs
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-byo-template.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-handoff.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-identity.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/adr-standards.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/project-planning/community-interaction.instructions.md
├── rai-planning/                     # Responsible AI planning
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-identity.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/rai-planning/rai-license-posture.instructions.md
├── security/                         # Security planning
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/identity.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/sssc-planner.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/standards-mapping.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-generation.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/security/vex-standards.instructions.md
├── shared/                           # Shared across packages
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/coaching-patterns.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/content-policy-citation.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/disclaimer-language.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/hve-core-location.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/planner-identity-base.instructions.md
│   ├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/telemetry-overlay.instructions.md
│   └── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/shared/untrusted-content-boundary.instructions.md
├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/docusaurus-edits.instructions.md
├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/pull-request.instructions.md
├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/skill-security-model.instructions.md
├── ${CLAUDE_PLUGIN_ROOT}/hve/${CLAUDE_PLUGIN_ROOT}/hve/.github/instructions/workflows.instructions.md
└── README.md
```

---

<!-- markdownlint-disable MD036 -->
*🤖 Crafted with precision by ✨Copilot following brilliant human instruction,
then carefully refined by our team of discerning human reviewers.*
<!-- markdownlint-enable MD036 -->
