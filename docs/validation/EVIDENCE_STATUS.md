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

Authority:

- `SURVEY_DERIVED_PROBLEM_CARDS_01.md`

Boundary:

- closed-choice aggregates are direct demand evidence;
- free-text is semantic evidence and may contain platform-side wording cleanup;
- the survey validates demand, not recommendation outcome.

## 2. Accepted task evidence

### P01 — workshop/minutes → requirement package

> **KEEP FOR PRACTICAL PILOT — high task fit / low independent validation**

Do not present P01 as independently validated industry best practice.

### P04 — business logic → editable process diagram

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority: `P04_PRACTITIONER_CURATION_RESULT_02.md`.

### P06 — Excel/CSV/system export → reconcile and validate

> **CLOSED — plain code-first default / Huashu optional**

Authorities:

- `DELIVERY_P06_DATA_RECONCILIATION.md`
- `P06_LOCAL_RUNTIME_RESULT_01.md`
- `evidence/p06/`

Bounded evidence: plain deterministic code matched the Skill on record-level outcomes in the synthetic fixture; Huashu added one useful control-total discipline but not enough Skill-specific gain for mandatory adoption.

### P03 — requirements/rules → clickable prototype

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — codebase/program → understand logic / reverse FS / defect hypotheses

> **CLOSED — traceable read-only repo exploration default; conditional LSP/semantic or ERP-native MCP upgrade**

Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

## 3. Invalidated evidence remains invalid

- `P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.

Only Result 02 is authoritative for P03/P07. The clean reruns do not rehabilitate unsupported old reports.

## 4. Cross-card method conclusion — accepted for pilot readiness

Authority:

- `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`

Status:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The heterogeneous trustworthy cards repeatedly support a minimal recurring method:

1. start from the real job, artifacts, deliverable and material constraints;
2. treat ordinary AI/existing Agent as the baseline;
3. discover specialized capability only for a concrete bottleneck;
4. when external adoption evidence is needed, prioritize practitioner workflow/failure evidence, then original implementation, then decision-changing current official facts;
5. ground generated work in source/project/system evidence and expose unknowns;
6. run local/runtime tests only when their result can change the recommendation;
7. stop when the colleague’s next action is stable.

No trusted card requires a contradictory permanent method.

## 5. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md` is now:

> **Minimal Curator V0.1 — real-user pilot candidate**

This promotion means **method readiness**, not product validation.

The Skill was deliberately kept generic: card-specific P03/P04/P06/P07 recommendations remain in validation documents rather than being accumulated as permanent scenario rules.

## 6. Current dominant uncertainty

The main uncertainty is no longer whether the Curator can produce plausible decisions on another internal card.

It is:

> **Will real ERP / enterprise-information-system colleagues act on the recommendation, and does it materially reduce wrong-tool selection, search/setup effort or avoidable downstream rework?**

Authority for the next evidence phase:

- `docs/REAL_USER_PILOT_V1.md`

## 7. Next accepted evidence

Prefer:

- a real colleague’s real task;
- recommendation actually given by Minimal Curator V0.1;
- what the colleague actually tried/rejected/changed;
- concrete artifact/result or failure reason;
- observed search/setup/rework/adoption effect;
- missed constraints or unsafe/wrong recommendation if any.

Do **not** substitute:

- another invented card;
- another smoke/readiness test;
- owner/agent opinion that the output “looks good”;
- more resource collection without user action.

## 8. Evidence acceptance rule remains

External claims must remain traceable to concrete acquired evidence. Search snippets are discovery only. Author self-tests are not independent validation. Runtime evidence is bounded to what was actually tested.

During the real-user phase, synthetic/internal testing is justified only to fix a defect exposed by real use or remove a concrete pilot blocker.
