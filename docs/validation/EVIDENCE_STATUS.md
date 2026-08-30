# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Demand evidence

The 2026-08 survey remains the primary REAL_USER demand source.

Supported conclusions:

- implementation consultants and project managers are the main audience;
- many respondents already use AI;
- the main gap is practical delivery quality, not AI introduction;
- users repeatedly want real methods/cases for requirements, PRD, prototypes, diagrams, PPT, Excel/data, testing, project management and Agent usage;
- typical inputs are actual project artifacts rather than abstract prompts.

Authority:

- `SURVEY_DERIVED_PROBLEM_CARDS_01.md`

The survey validates demand, not solution outcome.

## 2. Source-strategy position

For practical delivery questions, practitioner guides/reviews/cases should normally be the first discovery lane; original Tool/Skill and official docs are supporting verification layers.

This is practical-value-first, not independent-third-party-at-all-costs.

Do not use platform access failure, popularity metrics, source counts or author self-tests as substitutes for evidence quality.

## 3. P01

Status: **KEEP FOR PRACTICAL PILOT**

Retained:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

## 4. P04 — CLOSED

Status:

> **CLOSE P04 — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `P04_PRACTITIONER_CURATION_RESULT_02.md`

P04 demonstrated the desired behavior: practitioner-first search, targeted evidence delta, evidence-role discipline, explicit remaining coverage gap, then stop once the recommendation was stable.

Do not rerun P04 technical/runtime work unless later real adoption exposes a new material risk.

## 5. P06 data reconciliation — CLOSED

Status:

> **PLAIN CODE-FIRST DEFAULT / HUASHU OPTIONAL**

Authorities:

- `DELIVERY_P06_DATA_RECONCILIATION.md`
- `P06_LOCAL_RUNTIME_RESULT_01.md`
- `evidence/p06/`

### Final supported judgement

For ordinary ERP Excel/CSV/system-export reconciliation, a competent local code-first Agent is sufficient as the default implementation path **if** the workflow includes explicit reconciliation controls.

Required method discipline:

- deterministic/replayable transformation and comparison;
- explicit source/target row-count and amount checks;
- back-check source control totals/subtotals when available rather than simply excluding them;
- conservative key normalization and explicit mapping;
- ambiguous/non-unique matches routed to review instead of guessed;
- exceptions and source-row traceability preserved.

Current spreadsheet-native AI remains a legitimate lower-friction option for one-off lower-risk workbook work.

`alchaincyf/huashu-excel` remains useful as an optional audit/checklist method for recurring or high-consequence reconciliation, but current evidence does not justify mandatory adoption.

### Runtime evidence

The bounded local A/B used the same synthetic ERP-like input in isolated contexts and hidden ground truth.

Independent verification found:

- both baseline and with-Skill matched all 9 expected record-level statuses;
- both produced the same reconciliation CSV;
- baseline omitted a source control-total back-check;
- Huashu exposed a legacy `TOTAL` difference of 10;
- the pinned Huashu scripts initially failed to classify three `SUBTOTAL WHxx` rows correctly, requiring manual reclassification;
- Windows default console encoding also required a UTF-8 adjustment.

Therefore the material lesson is not “Huashu has no value”. It is:

> **the valuable audit discipline is portable into plain code-first execution and the bounded evidence does not show enough Skill-specific advantage to justify adding Huashu as a required dependency.**

### Evidence boundary

This is one synthetic bounded fixture, not independent ERP production validation of either method.

Do not generalize it into:

- “Huashu never helps”;
- “plain Agent always succeeds”;
- “all Excel work should use Python”.

Reopen only if real-user adoption shows a materially different workload, scale, audit requirement or failure pattern.

## 6. Runtime-testing policy

Runtime testing remains exceptional.

P06 justified one bounded runtime delta because a new self-authored Skill was competing with an already-capable plain code-first workflow on a correctness-sensitive task and the result could change adoption advice.

The test is now complete. Do not expand it into a benchmark suite.

## 7. Main remaining uncertainties

Product-level uncertainties now matter more than P06 technical uncertainty:

- whether practitioner-first curation remains stable on another heterogeneous job such as P03 prototype generation;
- whether curated packages are genuinely useful to colleagues on real material;
- which feeder ecosystems deserve recurring discovery prior;
- whether a minimal user-facing Curator product is worth packaging after a few heterogeneous cards.

## 8. Main risk now

The dominant risk is:

> **continuing to accumulate validation artifacts instead of proving that Curator recommendations generalize across different real jobs and are useful to colleagues.**

Next planned controlled card is P03. After P03 and one engineering-type card, reassess whether to shift from research/validation toward a minimal user-facing Curator.
