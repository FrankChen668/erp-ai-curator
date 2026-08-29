# ERP AI Resource Starter Pack V0

Verified: 2026-08-29

Purpose: preserve a **small set of current, high-confidence discovery candidates** while real-user validation is still pending.

Important: inclusion here means “current source verified and plausibly useful”, **not** “validated by target users”. This is a starter asset pack, not product proof.

## 1. Editable draw.io diagrams

### jgraph/drawio-mcp
- Link: https://github.com/jgraph/drawio-mcp
- Type: official draw.io Agent/MCP/Skill repository
- Best for: generating editable draw.io diagrams from coding agents
- Why keep: original vendor repository; current; supports agent workflows rather than static image output
- Verified: repository active and not archived; updated/pushed in 2026
- Limitation: exact capabilities depend on chosen integration path; evaluate relevant linked materials, not only the top README

### Agents365-ai/drawio-skill
- Link: https://github.com/Agents365-ai/drawio-skill
- Type: community Agent Skill
- Best for: richer diagram presets such as BPMN, cross-functional swimlanes, architecture and code-to-diagram workflows
- Why keep: active project; explicit BPMN/diagram presets; Chinese documentation available
- Verified: pushed 2026-08-28; active repository
- Limitation: richer but heavier than the official path; community project, not draw.io official

## 2. Rapid reviewable prototypes

### JimLiu/baoyu-design
- Link: https://github.com/JimLiu/baoyu-design
- Type: community Agent Skill
- Best for: UI mockups, wireframes, prototypes and reviewable self-contained HTML
- Why keep: directly targets local Agent workflows; supports Cursor / Claude Code style usage; strong practical output orientation
- Verified: active public repository in 2026
- Limitation: general design skill, not ERP-specific; task fit still depends on the quality of the input requirement

### kurenn/claude-prototype
- Link: https://github.com/kurenn/claude-prototype
- Type: Claude Code Skill
- Best for: zero-build-step interactive web prototypes
- Why keep: explicit prototype-focused workflow; produces runnable HTML rather than static screenshots
- Verified: active public repository, pushed 2026-08
- Limitation: small community footprint; keep as a candidate rather than a default recommendation until real-user comparison

## 3. Claude Code / Codex model routing

### OpenRouter Ori Harness
- Link: https://openrouter.ai/blog/announcements/ori-harness/
- Type: official OpenRouter setup tool / guide
- Best for: users who want the simplest current OpenRouter setup for Claude Code, Codex, OpenCode or Hermes
- Why keep: published 2026-08-04; OpenRouter now explicitly positions `ori claude` / `ori codex` as an optimized setup path
- Limitation: high-volatility topic; always re-check the current official page at recommendation time

### OpenRouter Codex CLI guide
- Link: https://openrouter.ai/blog/tutorials/codex-cli-openrouter/
- Type: official configuration guide
- Best for: users who need to understand or manually control Codex CLI custom provider configuration
- Why keep: documents `config.toml`, custom model provider and Responses API setup
- Limitation: treat as CLI guidance; do not automatically generalize to every Codex desktop/app surface

## 4. SAP Fit-to-Standard / requirements

### SAP Cloud ALM — AI-Assisted Requirement Generation
- Link: https://help.sap.com/docs/cloud-alm/applicationhelp/ai-assisted-requirement-generation-65a0305515864d94bb9b02d39eb259f8
- Type: official SAP product capability / implementation guidance
- Best for: converting Fit-to-Standard workshop transcripts and documentation into structured requirements
- Why keep: directly connected to Fit-to-Standard requirement work rather than generic AI ideation
- Verified: current SAP Help content; SAP implementation portal lists this capability and recent validity reviews
- Limitation: value depends on SAP Cloud ALM access and project context; this is not a general-purpose open-source Skill

### SAP Joule for Consultants — Project Lifecycle
- Link: https://learning.sap.com/courses/introducing-sap-joule-for-consultants/applying-sap-joule-for-consultants-across-the-sap-project-lifecycle
- Type: official SAP learning material
- Best for: understanding where Joule for Consultants can support SAP Activate phases, including Explore / fit-gap work
- Why keep: consultant-specific and lifecycle-specific rather than generic prompting advice
- Limitation: practical value depends on access to Joule for Consultants; may serve as a method reference rather than directly usable tooling

## 5. What is deliberately NOT in V0

Not included yet:
- large link collections;
- weakly sourced Chinese reposts;
- resources selected mainly by Star count;
- Oracle-specific AI learning methods where no strong public method has been found;
- PM-oriented resources without enough task-specific evidence;
- developer resources beyond currently reviewed architecture/diagram themes;
- anything requiring a database/refresh system to maintain.

## 6. How this pack should evolve

A resource moves from “starter candidate” toward “validated recommendation” only when one or more real-origin tasks (`REAL_USER` / `OWNER_REAL`) show that it actually helps the target role.

Future updates should be driven by repeated real needs, not by the desire to grow the list.
