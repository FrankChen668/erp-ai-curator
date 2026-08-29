# Real-origin Task Bank V0

Date: 2026-08-29

Purpose: separate **real-origin demand** from representative/synthetic eval cases.

This file is intentionally small. It only records tasks that have already appeared as genuine working needs in the project context. It does not invent missing PM/developer demand to make the matrix look balanced.

## OWNER_REAL tasks already evidenced

| ID | Role | Real work problem | Curator need | Current evidence |
|---|---|---|---|---|
| OR01 | implementation / product consultant | Need an AI/Agent approach that can generate **editable draw.io business process diagrams**, not only static images | find current Skill/Tool worth using | strong discovery candidates exist: jgraph/drawio-mcp, Agents365 drawio-skill |
| OR02 | consultant / product manager | Need to rapidly create a **reviewable interactive prototype** from requirements for stakeholder discussion | find practical Skill/Tool, preferably low-friction | candidate set exists; baoyu-design is high-confidence discovery candidate; claude-prototype remains candidate pending comparison |
| OR03 | developer / advanced Agent user | Need a **current low-cost / third-party model path** for Claude Code / Codex without following stale configuration tutorials | find current official/primary setup resources and distinguish supported vs merely workable paths | strong evidence; volatile and must be rechecked at run time; OpenRouter Ori is a newer official entry point than older manual guides |
| OR04 | implementation consultant | Need AI to improve **requirements analysis / Fit-to-Standard / Fit-Gap** work, with something more concrete than generic AI workshop material | find directly applicable methods/tools/cases | SAP side has concrete current official capabilities; Oracle side remains weak/empty in public sources |
| OR05 | implementation consultant | Need a structured AI-assisted way to **learn an unfamiliar SAP/Oracle module**: business process, configuration chain, key objects, not generic “ask AI” advice | find method/prompt framework/tool that actually supports module learning | SAP has partial official candidates; Oracle public method remains weak; 0 recommendation may be correct for the narrow AI-learning-method request |

## What these tasks prove

They prove that the project is addressing genuine recurring work needs, not only synthetic test cases.

They do **not** yet prove:

- shareability to a broader target population;
- equal value for PMs and developers;
- that Skill is the right product form;
- that current candidate recommendations are the final winners.

## Missing evidence — do not fabricate

### Project manager

We do not yet have enough independently recorded real-origin PM tasks in this repository to claim PM validation.

Potential areas such as meeting/action tracking, risk/issue management, status reporting and change impact are **hypotheses until actual PM demand is captured**.

### Developer

OR03 provides one real developer/advanced-Agent need. Architecture/codebase visualization is currently strong discovery evidence but should not automatically be counted as real-origin developer validation unless it came from an actual developer request.

## Intake rule going forward

When a real question arrives from survey/interview/work chat:

1. preserve the original wording;
2. tag source as `REAL_USER` or `OWNER_REAL`;
3. tag role only if known;
4. first decide whether external-resource discovery is actually needed;
5. if yes, run Protocol V2 and produce 0–2 recommendations;
6. record business judgement and, when available, actual usage behavior.

Do not rewrite a real question into a cleaner eval prompt before storing it. The messy wording is part of the product reality.
