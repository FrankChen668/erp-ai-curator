# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.
> Rebase audit: `docs/REBASE_AUDIT_20260830.md`.
> Cross-card reassessment: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

## 1. Demand evidence — accepted

The 2026-08 training survey remains the primary REAL_USER demand source.

Supported conclusions:

- 83 responses;
- implementation consultants and project managers are the main audience;
- many respondents already use AI;
- the main gap is practical delivery quality, not AI introduction;
- repeated work problems include requirements, PRD/FS, prototypes, diagrams, PPT, Excel/data, code/debugging, testing, project management and Agent usage;
- typical inputs are real project artifacts rather than abstract prompts.

Authority: `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Boundary: the survey validates demand, not recommendation outcome.

## 2. Accepted task evidence

### P01 — workshop/minutes → requirement package

> **KEEP FOR PRACTICAL PILOT — high task fit / low independent validation**

### P04 — business logic → editable process diagram

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority: `P04_PRACTITIONER_CURATION_RESULT_02.md`.

### P06 — Excel/CSV/system export → reconcile and validate

> **CLOSED — plain code-first default / Huashu optional**

Authorities:

- `DELIVERY_P06_DATA_RECONCILIATION.md`
- `P06_LOCAL_RUNTIME_RESULT_01.md`
- `evidence/p06/`

### P03 — requirements/rules → clickable prototype

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — codebase/program → understand logic / reverse FS / defect hypotheses

> **CLOSED — traceable read-only repo exploration default; conditional LSP/semantic or ERP-native MCP upgrade**

Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

## 3. Invalidated evidence remains invalid

- `P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.

Only Result 02 is authoritative for P03/P07.

## 4. Cross-card method conclusion — accepted for pilot readiness

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Status:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The heterogeneous trustworthy cards repeatedly support a minimal recurring method:

1. start from the real job, artifacts, deliverable and material constraints;
2. treat ordinary AI/existing Agent as the baseline;
3. discover specialized capability only for a concrete bottleneck;
4. use practitioner workflow/failure evidence when external adoption evidence matters;
5. ground generated work in source/project/system evidence and expose unknowns;
6. run local/runtime tests only when their result can change the recommendation;
7. stop when the colleague’s next action is stable.

## 5. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md`:

> **Minimal Curator V0.1 — real-user pilot candidate / version 0.6.2**

This means method readiness, not product validation.

0.6.2 is a narrow Harness consistency patch. It does not add new ERP scenario knowledge; it adds an on-demand consistency check when a concrete capability gap is already visible but the run is still preparing to recommend no specialized capability.

Authority:

- `CURATOR_062_HARNESS_PATCH.md`

## 6. 0.6.1 boundary regression — closed internal evidence

Authorities:

- `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Bounded findings from five paired isolated Baseline-vs-Curator cases:

- no over-tooling signal;
- under-tooling appeared in Case 5 and Case 38, with a lighter signal in Case 8;
- `C` misuse as “information missing” was not confirmed;
- recurring multi-problem decomposition defect was not confirmed;
- Curator showed no clear repeatable adoption-decision advantage over ordinary Baseline Agent in this bounded exercise;
- the under-tooling misses were already covered by permanent method rules, so a missing domain-rule defect was not established.

Harness interpretation: the repeated miss is still useful engineering feedback because an existing rule can be too easy for an Agent to skip. 0.6.2 therefore improves decision-boundary legibility/enforcement without encoding the case answers.

Evidence boundary: the regression and 0.6.2 patch are internal engineering evidence, not REAL_USER adoption/product evidence.

## 7. Current dominant uncertainty

The main uncertainty remains:

> **Will real ERP / enterprise-information-system colleagues act on the recommendation, and does it materially reduce wrong-tool selection, search/setup effort or avoidable downstream rework?**

Authority for the current phase: `docs/REAL_USER_PILOT_V1.md`.

## 8. Next accepted evidence

Prefer:

- a real colleague’s real task;
- recommendation actually given by Minimal Curator 0.6.2;
- what the colleague actually tried/rejected/changed;
- concrete artifact/result or failure reason;
- observed search/setup/rework/adoption effect;
- missed constraints or unsafe/wrong recommendation if any.

Do **not** substitute:

- another invented card;
- another synthetic boundary/smoke/readiness regression without a real-use defect;
- owner/agent opinion that the output “looks good”;
- more resource collection without user action.

## 9. Evidence acceptance rule remains

External claims must remain traceable to concrete acquired evidence. Search snippets are discovery only. Author self-tests are not independent validation. Runtime evidence is bounded to what was actually tested.

During the real-user phase, internal testing is justified only to fix a concrete defect exposed by real use or remove a concrete pilot blocker.
