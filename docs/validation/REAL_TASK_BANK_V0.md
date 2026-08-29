# Real-origin Task Bank V0

Date: 2026-08-29

Purpose: separate **real-origin demand** from representative/synthetic eval cases.

This file is intentionally small. It only records tasks that have already appeared as genuine working needs in the project context. It does not invent missing PM/developer demand to make the matrix look balanced.

## OWNER_REAL tasks already evidenced

| ID | Role | Real work problem | Curator need | Current evidence |
|---|---|---|---|---|
| OR01 | implementation / product consultant | Need an AI/Agent approach that can generate **editable draw.io business process diagrams**, not only static images | find current Skill/Tool worth using | jgraph/drawio-mcp is the default high-confidence option; Agents365 drawio-skill is differentiated for advanced extraction / diagram workflows |
| OR02 | consultant / product manager | Need to rapidly create a **reviewable interactive prototype** from requirements for stakeholder discussion | find practical Skill/Tool, preferably low-friction | baoyu-design and claude-prototype represent differentiated broad-vs-lightweight prototype workflows |
| OR03 | product manager / advanced Agent user (developer-adjacent) | Need a **current low-cost / third-party model path** for Claude Code / Codex without following stale configuration tutorials | find current official/primary setup resources and distinguish supported vs merely workable paths | strong current evidence; OpenRouter Ori is now the preferred setup entry; volatile facts must be rechecked at run time |
| OR04 | implementation consultant | Need AI to improve **requirements analysis / Fit-to-Standard / Fit-Gap** work, with something more concrete than generic AI workshop material | find directly applicable methods/tools/cases | SAP has concrete current official capabilities; Oracle deep scan found one high-task-fit but medium-trust practitioner course for requirements/design/UAT |
| OR05 | implementation consultant | Need a structured AI-assisted way to **learn an unfamiliar SAP/Oracle module**: business process, configuration chain, key objects, not generic “ask AI” advice | find method/prompt framework/tool that actually supports module learning | SAP has partial official candidates; Oracle AI-assisted module-learning method remains a public gap after deeper search |
| OR06 | product manager / Agent project owner (developer-adjacent) | Need to understand an existing Vibe-Coded Agent project's architecture / execution graph and determine whether “Graph Engineering” is passive visualization or an invasive workflow change | find the right class of tool: static map vs runtime tracing vs workflow graph | strong task-understanding evidence: codebase-map/drawio for static understanding, observability for runtime traces, agent-graph only for governed workflow design |

## What these tasks prove

They prove that the project is addressing genuine recurring work needs, not only synthetic test cases.

They do **not** yet prove:

- shareability to a broader target population;
- equal value for PMs and developers;
- that Skill is the right product form;
- that current candidate recommendations are the final winners.

## Missing evidence — do not fabricate

### Project manager

There are now several OWNER_REAL problems with product-manager context, but they come from the Product Owner rather than independent project-manager respondents.

This is useful demand evidence, **not independent PM validation**.

Potential areas such as meeting/action tracking, risk/issue management, status reporting and change impact remain hypotheses until actual PM demand is captured.

### Developer

We still do **not** have enough independent `REAL_USER` developer-origin tasks to claim developer validation.

OR03 and OR06 are developer-adjacent owner needs; they must not be relabeled as developer-user evidence just because they concern coding agents or codebases.

## Trigger-negative evidence

Real owner questions also show that many ERP/AI tasks should **not** activate the Curator at all. Examples and reasoning are recorded in:

`docs/validation/OWNER_REAL_TRIGGER_NEGATIVES_01.md`

This evidence is part of product validation because avoiding unnecessary resource search is a core product behavior.

## Intake rule going forward

When a real question arrives from survey/interview/work chat:

1. preserve the original wording;
2. tag source as `REAL_USER` or `OWNER_REAL`;
3. tag role only if known;
4. first decide whether external-resource discovery is actually needed;
5. if yes, run Protocol V2 and produce 0–2 recommendations;
6. record business judgement and, when available, actual usage behavior.

Do not rewrite a real question into a cleaner eval prompt before storing it. The messy wording is part of the product reality.
