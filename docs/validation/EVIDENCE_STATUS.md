# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.
> Rebase audit: `docs/REBASE_AUDIT_20260830.md`.

## 1. Demand evidence — accepted

The 2026-08 training survey remains the primary REAL_USER demand source.

Supported conclusions:

- 83 responses;
- implementation consultants and project managers are the main audience;
- many respondents already use AI;
- the main gap is practical delivery quality, not AI introduction;
- repeated work problems include requirements, PRD/FS, prototypes, diagrams, PPT, Excel/data, code/debugging, testing, project management and Agent usage;
- typical inputs are real project artifacts rather than abstract prompts.

Authority:

- `SURVEY_DERIVED_PROBLEM_CARDS_01.md`

Boundary:

- closed-choice aggregates are direct demand evidence;
- free-text is semantic evidence and may contain platform-side wording cleanup;
- the survey validates demand, not recommendation outcome.

## 2. Accepted card evidence

### P01 — workshop/minutes → requirement package

Status:

> **KEEP FOR PRACTICAL PILOT**

Classification:

> **high task fit / low independent validation**

Do not present P01 as independently validated industry best practice.

### P04 — business logic → editable process diagram

Status:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `P04_PRACTITIONER_CURATION_RESULT_02.md`

### P06 — Excel/CSV/system export → reconcile and validate

Status:

> **CLOSED — PLAIN CODE-FIRST DEFAULT / HUASHU OPTIONAL**

Authorities:

- `DELIVERY_P06_DATA_RECONCILIATION.md`
- `P06_LOCAL_RUNTIME_RESULT_01.md`
- `evidence/p06/`

Supported bounded judgement:

- a competent local code-first Agent is sufficient as the default for the tested ERP-like reconciliation when explicit reconciliation controls are included;
- required discipline includes deterministic/replayable execution, row/amount checks, control-total/subtotal back-checks when available, conservative normalization/mapping, no-guess handling of ambiguity and traceability;
- Huashu contributed useful control-check discipline but did not show enough Skill-specific advantage in the bounded fixture to justify mandatory adoption.

Boundary: this remains one bounded synthetic fixture, not universal production proof.

### P03 — requirements/rules → clickable prototype / UI demo

Status:

> **CLOSED — SPEC-FIRST CODE PROTOTYPE DEFAULT; FIGMA MAKE CONDITIONAL UPGRADE**

Authority:

- `P03_PROTOTYPE_CURATION_RESULT_02.md`

Supported judgement:

- turn roles, permissions, fields, validation, states, transitions and exception paths into a bounded interaction contract before generating UI;
- a competent code-capable Agent is the default for a reviewable local prototype when the goal is requirement clarification;
- Figma Make is a conditional upgrade when Figma/design-system/shared review context matters;
- hosted builders are conditional when hosted app behavior/state/sharing justify their cloud/platform constraints;
- inspected prototype Skills solve adjacent transformations but are not mandatory.

Evidence boundary: no independent ERP-specific benchmark proves generated prototype business correctness; human rule/exception review remains required.

### P07 — codebase/program → understand logic / reverse FS / defect hypotheses

Status:

> **CLOSED — TRACEABLE READ-ONLY REPO EXPLORATION DEFAULT; CONDITIONAL LSP/SEMANTIC OR ERP-NATIVE MCP UPGRADE**

Authority:

- `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`

Supported judgement:

- for ordinary local Git repositories, start with one concrete question and a scoped read-only repo-aware Agent workflow;
- build understanding hierarchically: global structure → relevant flow/modules → detailed code/test/log evidence;
- distinguish observed code fact, inference and business-confirmation-required unknowns;
- code can evidence implemented behavior but does not automatically prove business intent;
- introduce LSP/symbol/semantic tooling only when text search/cross-symbol navigation is a demonstrated bottleneck;
- Serena is a conditional semantic-navigation trial, not a mandatory default; independent evidence is mixed;
- CodeGraph is task-relevant but currently has insufficient independent evidence for default adoption;
- when authoritative code/metadata/tests live outside the local filesystem, a system-native connector can materially change the task; current SAP ADT MCP / ABAP tooling is the clearest example;
- live SAP write/activation capability increases the need for read-only/least-privilege exploration rather than increasing Agent autonomy;
- no synthetic runtime A/B was justified without a representative real legacy/system-native repository.

Evidence boundary:

- no controlled ERP benchmark compares native repo-aware Agents with Serena/CodeGraph on the same real legacy estate;
- reverse-generated FS must preserve source traceability and explicitly flag inferred/unknown business meaning;
- defects and performance claims remain hypotheses until verified by tests/logs/static analysis/runtime/metrics as appropriate.

## 3. Invalidated evidence — DO NOT USE FOR PRODUCT CONCLUSIONS

### P03 prototype sprint result

- `P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.

Only Result 02 is authoritative.

### P07 codebase sprint result

- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.

Only Result 02 is authoritative. The clean rerun does not rehabilitate the unsupported prior report.

## 4. Cross-card conclusion — reassessment is now due

The earlier “validation complete / Minimal Curator V0.1 / REAL USER PILOT” claim remains withdrawn **until a fresh cross-card reassessment is performed**.

What has changed:

- P03 now has a trustworthy rerun;
- P07 now has a trustworthy engineering-type rerun;
- the corrected evidence discipline has therefore been exercised across prototype, diagram, data and engineering/code artifact classes.

What has not yet been decided:

> **Whether this heterogeneous evidence is now sufficient to package a minimal user-facing Curator and enter a bounded real-user adoption pilot.**

That is the immediate next product decision. Do not add another validation card by default before making it.

## 5. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` remains an **experimental candidate** pending the cross-card reassessment.

Repeated trustworthy evidence now supports several directions already present in it:

- start from the real task rather than a tool category;
- ask whether ordinary AI/Agent is already enough before searching for specialized capability;
- upgrade only for a concrete capability/bottleneck;
- separate practitioner evidence, original implementation/current facts and limitations/counter-evidence;
- do not require runtime testing when it cannot change the adoption decision.

Do not yet rename it “validated Minimal Curator V0.1” until the cross-card reassessment checks whether the Skill faithfully encodes the recurring method without card-specific overfitting.

## 6. Main uncertainty now

> **Is the recurring Curator method sufficiently stable and minimal to expose to real colleagues, or are there still contradictions/overfitting in the candidate Skill that must be corrected first?**

Immediate next action:

1. reread P01/P04/P06/P03/P07 trustworthy evidence and the candidate Skill;
2. extract only recurring decision rules across heterogeneous cards;
3. adversarially test for contradictions, card-specific rules and hidden framework creep;
4. decide whether to enter a bounded REAL_USER pilot or perform one narrowly scoped correction first.

## 7. Evidence acceptance rule

A card cannot be marked `CLOSED` merely because its conclusion is plausible.

For external-research cards, retained authority must allow an auditor to determine:

- what concrete source was used;
- whether it was actually read or only discovered;
- what evidence role it plays;
- what material claim it supports;
- what limitations or counter-evidence remain;
- why further search/test is unlikely to change the adoption decision.

Source-less synthesis may be useful reasoning, but it is not accepted product evidence.
