# Cross-Card Method Reassessment — 2026-08-30

## Verdict

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The trustworthy evidence base is now heterogeneous enough to stop adding validation cards by default.

The correct next state is:

> **Minimal Curator V0.1 — Pilot Candidate**

This means the recurring decision method is stable enough to expose to real colleagues. It does **not** mean the product has proven adoption, time savings, lower rework or recommendation quality in real use.

## Evidence reviewed

Demand / product authority:

- `docs/PROJECT_NORTH_STAR.md`
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

Trusted task evidence:

- P01 — post-workshop requirements: high task fit / low independent validation;
- P04 — business logic → editable process diagram: closed;
- P06 — ERP-like multi-file reconciliation: closed with bounded runtime delta;
- P03 — requirements/rules → clickable prototype: clean Result 02 closed;
- P07 — codebase/program → logic/FS/defect hypotheses: clean Result 02 closed.

Candidate implementation reviewed:

- `skills/curating-erp-ai-resources/SKILL.md` version 0.5.1.

Invalidated P03/P07 Result 01 files were not used as evidence.

## Recurring method that survives heterogeneous cards

### 1. Start from the real job, not a tool category

Across requirements, diagrams, data, prototype and code work, useful decisions depend on:

```text
real situation
+ actual artifacts
+ concrete action/problem
+ expected deliverable
+ material constraints
```

Broad labels such as “prototype”, “Excel” or “code understanding” are insufficient adoption units.

### 2. General AI / existing Agent is the baseline, not the fallback

Repeated evidence rejects automatic specialized-tool adoption:

- P06: plain deterministic code matched Huashu on record-level reconciliation; only a reusable control-total discipline transferred;
- P03: code-capable Agent is sufficient for the first reviewable prototype when requirements are structured;
- P07: ordinary repo-aware Agent is sufficient for initial local-repository exploration when scoped and evidence-linked;
- P04: a low-friction general-AI → editable Draw.io path is viable when process semantics are already clear.

Therefore the Curator should ask **what capability is actually missing** before discovering Tools/Skills.

### 3. Specialized capability is justified by a concrete bottleneck

The cards show materially different upgrade triggers rather than a fixed tool hierarchy:

- editable process output / enterprise process structure;
- design-system/Figma collaboration;
- deterministic reconciliation controls;
- symbol/cross-module navigation;
- system-native SAP source/ATC/where-used access;
- local/privacy/platform constraints.

This supports capability-gap reasoning, not scenario-to-tool lookup tables.

### 4. Source-grounded work and explicit verification are cross-card controls

The recurring quality boundary is not “better prompt”. It is grounding important statements in the strongest available evidence:

- original requirement/source material;
- process facts;
- source rows/control totals;
- prototype interaction contract;
- code/tests/logs/system metadata.

Generated artifacts are review objects, not automatic business truth.

### 5. Practitioner evidence matters when the decision is about adoption

P04, P03 and P07 all changed or sharpened once real practitioner workflow/failure evidence was retained instead of relying mainly on product documentation or author self-tests.

The stable evidence order is therefore:

```text
practitioner workflow / failure evidence
→ original implementation
→ only decision-changing current official facts
→ limitations / counter-evidence
```

This is a default evidence strategy, not a source quota.

### 6. Runtime testing is conditional, not ceremonial

- P06 had a real unresolved adoption question, so a bounded runtime delta changed confidence and preserved one useful discipline without forcing Skill adoption.
- P03 and P07 did not have representative artifacts/runtime that could resolve the key adoption boundary, so synthetic A/B would have been low-value.

The recurring rule is:

> **Run a local/runtime delta only when a concrete result could change the recommendation.**

### 7. Stop when the colleague’s next action is stable

P03/P04/P07 all reached a point where more source accumulation was unlikely to change what the colleague should do first.

The product should optimize for a small actionable package, not exhaustive search coverage.

## Candidate Skill adversarial review

### What is correct and should remain

The current Skill already captures the recurring method well:

- real-task-first intake;
- A/B/C leverage decision;
- ordinary AI may be enough;
- external discovery only when needed;
- practitioner → implementation → official fact evidence order;
- source-role/limitation traceability;
- minimum safety checks for executable third-party resources;
- runtime testing only when decision-changing;
- small actionable output;
- explicit anti-drift rules.

### Material defect found

The Skill’s **status and “current evidence patterns” section are stale**. It still says P03/P07 have no accepted result and lists only P01/P04/P06 as trusted evidence.

This is factual drift created by the corrected reruns. It must be fixed before pilot so the Skill does not instruct itself to ignore current authorities.

### Overfitting risk found

Keeping a growing catalog of P01/P03/P04/P06/P07-specific recommendations inside the permanent Skill would turn a general decision method into a scenario memory table and could bias future curation.

Correction:

- remove card-specific behavior summaries from the permanent Skill;
- retain only the recurring cross-card principles;
- keep detailed task evidence in `docs/validation/`.

### No material method contradiction found

No trusted card requires reversing the candidate’s core principles.

Notably:

- “general AI first” does **not** mean “general AI always wins”; P04 process-builder and P07 SAP-native MCP remain valid specialized upgrades when a real capability gap exists;
- “practitioner-first” does **not** mean official facts are unimportant; current setup/privacy/security facts still matter when they change adoption;
- “runtime is exceptional” does **not** mean never test; P06 demonstrates when it is worth doing.

## Why another validation card is not the best next action

The dominant uncertainty has moved.

Before P03/P07 reruns:

> **Can the Curator evidence discipline survive different task classes?**

Now:

> **Will real ERP colleagues find the Curator recommendation useful enough to act on, and does it reduce wrong-tool selection, setup/search effort or downstream rework?**

P10 or another synthetic/curated card would provide diminishing evidence about that question.

Under the North Star’s proxy-goal counterfactual, another internal card can be completed perfectly while leaving the current real-user uncertainty untouched. Therefore it should not be the default next step.

## Promotion decision

Promote the candidate from:

> `experimental candidate — validation incomplete`

to:

> **`Minimal Curator V0.1 — real-user pilot candidate`**

Interpretation:

- method readiness: sufficient for pilot;
- product/user outcome: not validated;
- resource/tool recommendations: still task-specific and evidence-bounded;
- pilot failures may still force method correction.

## Required narrow changes before pilot

1. update `SKILL.md` status/version;
2. remove stale P03/P07 invalidation statements from the Skill;
3. replace card-specific “current behavior patterns” with recurring cross-card principles;
4. define one small real-user pilot capture contract;
5. update current execution/evidence/handoff documents so no file claims P07 or cross-card reassessment is still pending.

No new framework, scoring model, taxonomy, database, benchmark or Agent orchestration is justified.

## Stop decision

Cross-card method reassessment is complete.

> **The next decision-changing evidence must come from real-user use, not another default internal validation card.**
