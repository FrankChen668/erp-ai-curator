# Real-origin Task Bank V0

Date: 2026-08-29

Purpose: preserve **real-origin demand** separately from representative/synthetic tests.

This bank stores real work problems, not resource categories. Existing recommendations created under the resource-first model are historical evidence only; V3 must re-diagnose the AI leverage before reusing them.

## OWNER_REAL tasks already evidenced

| ID | Role | Real work problem | V3 intake type | Old discovery evidence |
|---|---|---|---|---|
| OR01 | implementation / product consultant | Need an AI/Agent approach that can generate **editable draw.io business process diagrams**, not only static images | explicit-resource / AI-work-method | jgraph/drawio-mcp; Agents365 drawio-skill |
| OR02 | consultant / product manager | Need to rapidly create a **reviewable interactive prototype** from requirements for stakeholder discussion | AI-work-method | baoyu-design; claude-prototype |
| OR03 | product manager / advanced Agent user (developer-adjacent) | Need a **current low-cost / third-party model path** for Claude Code / Codex without following stale configuration tutorials | explicit-resource | OpenRouter Ori and related current setup evidence |
| OR04 | implementation consultant | Need AI to improve **requirements analysis / Fit-to-Standard / Fit-Gap**, beyond generic “AI can help” advice | AI-work-method | SAP official capability/material; one Oracle practitioner-course candidate |
| OR05 | implementation consultant | Need a structured AI-assisted way to **learn an unfamiliar SAP/Oracle module**: process, config chain, key objects, not generic prompting | AI-work-method | partial SAP official support; Oracle public gap |
| OR06 | product manager / Agent project owner (developer-adjacent) | Need to understand an existing Vibe-Coded Agent project's architecture / execution graph and determine whether “Graph Engineering” is passive visualization or an invasive workflow change | AI-work-method / uncertain | static map vs runtime tracing vs workflow-governance distinction |

## Important reinterpretation under V3

The original problems remain valid OWNER_REAL evidence.

The old column “Curator need” has been removed because it assumed every useful case must end in external-resource discovery.

V3 must first decide:

- **Mode A** — general AI is already enough;
- **Mode B** — a specialized AI method / Tool / Skill clearly adds value;
- **Mode C** — do a low-cost experiment before adopting complexity.

Only Mode B necessarily enters external discovery.

## What these tasks prove

They show that real enterprise-information-system work repeatedly raises questions about **how AI should be used**, not only “which link should I click”.

They do not yet prove:

- V3 is correct;
- Skill is the right final form;
- broad REAL_USER adoption;
- equal value across all roles;
- the old discovered resources are still the best answer.

## Missing evidence — do not fabricate

### Independent project-manager evidence

There are OWNER_REAL problems with product/project context, but they come from the Product Owner, not independent project-manager respondents.

### Independent developer evidence

OR03 and OR06 are developer-adjacent owner needs. They are not independent developer-user validation.

### Generalized-ERP breadth

The current task bank is still historically biased toward SAP / Oracle and Agent-tool topics.

The new product boundary explicitly includes:

- Java / .NET custom supply-chain and finance systems;
- ERP extensions and integrations;
- enterprise-system product / project / development work.

This scope expansion is a product definition, **not yet broad REAL_USER evidence**. Do not invent cases just to make the bank look balanced.

## Trigger-negative evidence

Previous owner questions show that direct explanation, code review, artifact generation and domain research should not automatically invoke AI-work-method navigation.

Under V3 the boundary is now expressed more precisely as:

> **Is the user asking to execute the current task, or choose a reusable AI working approach?**

See `OWNER_REAL_TRIGGER_NEGATIVES_01.md` as historical boundary evidence.

## Intake rule going forward

When a real question arrives:

1. preserve the original wording;
2. tag `REAL_USER` or `OWNER_REAL`;
3. record role only when known;
4. classify intent: `direct execution / AI-work-method / explicit-resource / uncertain`;
5. AI-work-method / explicit-resource / relevant uncertain cases run `PROTOCOL_V3.md`;
6. record Mode A/B/C and the actual working recommendation;
7. record business judgement and observed usage when available.

Do not rewrite real questions into neat scenario prompts before storing them.
