# V3 OWNER_REAL Replay 01 — Falsification, not validation

Date: 2026-08-29

Purpose: replay OR01–OR06 under `AI_LEVERAGE_MODEL_V3.md` and deliberately check whether the new model changes old resource-first answers.

This is **OWNER_REAL model replay**, not independent REAL_USER validation.

## Summary

The V3 model materially changes the old behavior:

- OR01 / OR03 remain clear **Mode B** cases;
- OR02 changes from “find prototype Skills” to **Mode C first**;
- OR04 must split **SAP-native capability** from generalized/custom ERP work;
- OR05 changes from “find a learning resource” to **Mode A/C first**;
- OR06 changes from “find a graph tool” to **diagnose static / runtime / governance first**.

This is the behavior we wanted to test: V3 should be willing to recommend **less tooling** than the old resource-first model.

---

## OR01 — Editable draw.io business process diagram

### Original need

Need an AI/Agent approach that can generate editable `.drawio` business-process diagrams, not only static images.

### V3 diagnosis

**Mode B — specialized capability has clear incremental value.**

Why:

- the deliverable is not merely “a diagram”; it must remain native/editable in draw.io;
- the user wants a reusable Agent workflow, not a one-off picture;
- a general LLM can produce XML, but a draw.io-specific integration reduces format/layout/iteration friction enough to justify specialization.

### Current main recommendation

`jgraph/drawio-mcp`

https://github.com/jgraph/drawio-mcp

Current check on 2026-08-29: active public repository under `jgraph`, updated recently, with a dedicated draw.io integration path.

Agents365 drawio-skill remains an advanced alternative when codebase/IaC/SQL extraction or heavier diagram workflows are specifically required.

### V3 correction vs old model

Still Mode B, but do **not** automatically give two links. Start with the official draw.io-oriented option unless the user has an advanced capability gap.

---

## OR02 — Rapid reviewable interactive prototype

### Original need

Turn requirements into a reviewable interactive prototype for stakeholder discussion.

### V3 diagnosis

**Mode C — first run a low-cost experiment with the user's existing coding Agent.**

Why:

- a modern coding Agent can already create self-contained HTML prototypes from requirements;
- “interactive prototype” by itself does not prove a dedicated design Skill is necessary;
- the real question is whether repeated prototype work needs better visual quality, design-system discipline, discovery flow or feedback iteration.

### Minimum experiment

Before installing anything new:

1. give the current Agent the real requirements;
2. ask for a self-contained interactive HTML prototype;
3. perform one stakeholder-style revision round;
4. observe whether the pain is visual quality / consistency / interaction / iteration speed.

### Upgrade signal

If this becomes repeated work and generic Agent output is consistently weak, then evaluate a specialized design Skill such as:

`JimLiu/baoyu-design`

https://github.com/JimLiu/baoyu-design

Current repository description explicitly targets local Agent UI mockups, prototypes, decks and wireframes as self-contained HTML.

### V3 correction vs old model

The old model searched for prototype resources immediately. V3 says **do not add a Skill until the generic baseline exposes a real gap.**

---

## OR03 — Claude Code / Codex third-party or lower-cost model routing

### Original need

Use OpenRouter / third-party / lower-cost models with Claude Code or Codex without following stale setup instructions.

### V3 diagnosis

**Mode B — specialized, volatile setup path is clearly required.**

Why:

- this is not a task a generic prompt can solve once and remain correct;
- harness/provider compatibility and environment variables change;
- using an outdated setup can directly break the tool.

### Current recommendation

OpenRouter **Ori Harness** as the default first setup path.

https://openrouter.ai/blog/announcements/ori-harness/

Checked 2026-08-29: OpenRouter published Ori on 2026-08-04 and explicitly supports `ori claude`, `ori codex`, `ori opencode`, and `ori hermes`.

Manual OpenRouter Claude Code / Codex documentation remains troubleshooting/reference material rather than the default user path.

### Critical limitation

OpenRouter's current Claude Code documentation states that full compatibility is only guaranteed with the Anthropic first-party provider. “Can route another model” must not be rewritten as “Claude Code officially supports every model through OpenRouter”.

### V3 correction vs old model

Still Mode B. This is exactly the kind of high-volatility problem where targeted current-source verification is justified.

---

## OR04 — AI for Fit-to-Standard / Fit-Gap / requirements analysis

### Original need

Find a concrete way for AI to improve requirements discovery / Fit-to-Standard / Fit-Gap work, beyond generic “AI can help write requirements”.

### V3 diagnosis

**Do not give one ERP-wide answer. The environment changes the Mode.**

### SAP Cloud ALM / SAP Activate context

**Mode B.**

Current SAP Cloud ALM has AI-assisted requirement generation based on Fit-to-Standard workshop transcripts/documentation. SAP Activate updates in July 2026 explicitly added AI-assisted procedures around workshop documentation and requirement generation.

This is a genuine specialized leverage point because the capability is embedded in the implementation workflow.

### Java / custom supply-chain / custom finance / non-SAP ERP context

**Mode A or C first.**

The SAP-native capability is not transferable as a product recommendation.

For a custom ERP implementation, first test a general grounded workflow:

`workshop transcript / notes → decision & gap extraction → requirement draft → trace back to evidence → human review`

Only search for a specialized Tool when a repeated gap appears, for example:

- transcript ingestion at scale;
- requirement traceability;
- direct ALM integration;
- domain-document retrieval;
- structured change/version management.

### V3 correction vs old model

The old resource-first model could easily turn “ERP Fit-Gap” into “recommend SAP official materials”. V3 forces the question:

> Is this actually an SAP-native task, or a generalized implementation-method problem?

---

## OR05 — Learn an unfamiliar ERP module quickly

### Original need

Use AI to build an understanding of business process → configuration chain → key objects/master data → common issues → validation path for an unfamiliar module.

### V3 diagnosis

**Mode A first; Mode B only when a specialized knowledge source adds unique value.**

Why:

- this task is mostly structured inquiry + source grounding;
- a strong general model with the right documents can already execute the learning loop;
- searching for a dedicated “module learning Skill” can add complexity without improving the outcome.

### Minimum general-AI working method

For any ERP / custom enterprise system:

1. establish the end-to-end business process;
2. identify roles, documents, master data and key objects;
3. map configuration / rule points;
4. connect interfaces and downstream effects;
5. identify typical exceptions;
6. create a validation checklist;
7. require every important claim to point back to available source material.

### When specialization becomes Mode B

If working in SAP and the organization has SAP Joule for Consultants, its SAP-specific knowledge base can provide unique value that a general web model may not have.

For Oracle / Java custom systems, do not invent a specialized recommendation just because the task sounds “ERP”.

### V3 correction vs old model

Old behavior searched for prompt frameworks / courses first. V3 says the default is **use the general model well before adding another resource layer.**

---

## OR06 — Understand an existing Agent project's architecture / graph

### Original need

Understand a Vibe-Coded Agent project's technical architecture and execution flow, and determine whether Graph Engineering is passive visualization or an invasive workflow change.

### V3 diagnosis

**Mode C first — clarify which graph is actually needed before choosing a tool.**

There are at least three different jobs:

1. **Static structure** — modules, dependencies, components, code organization;
2. **Runtime behavior** — model/tool calls, retries, latency, traces, execution paths;
3. **Workflow governance** — legal steps, evidence, gates, resumability, routing rules.

These should not share one recommendation.

### Lowest-cost path

If the immediate need is simply “help me understand what I built”, start with static inspection / mapping.

A codebase mapping Skill or draw.io architecture output can be useful here.

Do **not** introduce Agent Graph / Graph Engineering just to produce a picture.

### Upgrade signals

- Need real execution evidence → introduce tracing / observability;
- Need verifiable routing, recovery and workflow contracts → then consider Agent Graph / Graph Engineering.

### V3 correction vs old model

The product should diagnose the job class before it searches. “Graph” is not a resource category.

---

# Replay conclusion

## What changed

Under the old resource-first interpretation, all six problems naturally attracted resource searches.

Under V3:

- clear specialized leverage: OR01, OR03;
- specialized leverage only in a specific product context: OR04 SAP branch;
- general AI / low-cost experiment first: OR02, OR05;
- diagnose before tooling: OR06.

This is a meaningful falsification result because V3 did **not** preserve every old recommendation behavior.

## What this does not prove

- It does not prove V3 works for independent users;
- it does not prove Mode A/C recommendations are better until users try them;
- it does not prove a Skill is required;
- it does not justify building a scenario library around these six cases.

## Next evidence

Use new REAL_USER questionnaire/work-request inputs when available. Until then, additional cloud work should focus on testing the **general decision mechanism** against diverse owner-real work problems, not expanding the resource inventory.
