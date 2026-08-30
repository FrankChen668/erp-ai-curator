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
- free-text is treated as semantic evidence and may contain platform-side wording cleanup;
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

Why accepted:

- concrete external URLs are retained;
- evidence roles are explicit;
- limitations/counter-evidence and Bilibili coverage gaps are recorded;
- stop rationale is tied to a stable adoption decision.

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

Boundary:

- this remains one bounded synthetic fixture, not universal production proof.

## 3. Invalidated evidence — DO NOT USE FOR PRODUCT CONCLUSIONS

### P03 prototype sprint result

File:

- `P03_PROTOTYPE_CURATION_RESULT_01.md`

Status:

> **INVALIDATED — NOT PRODUCT EVIDENCE**

Reason:

- practitioner/source claims were retained without a sufficient concrete URL/citation/acquisition trail;
- current tool capability claims were not tied to traceable current-fact sources;
- the file was produced during a long-context sprint where researched evidence cannot be reliably separated from model synthesis.

Its prior verdict is withdrawn. P03 must be rerun from scratch.

### P07 codebase sprint result

File:

- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

Status:

> **INVALIDATED — NOT PRODUCT EVIDENCE**

Reason:

- broad claims about major code-Agent ecosystems, practitioner workflows and legacy-system practice lack concrete retained source links/citations;
- there is no auditable evidence chain sufficient to support a `CLOSED` verdict.

Its prior verdict is withdrawn. P07 is not closed.

## 4. Withdrawn cross-card conclusion

The following conclusion is no longer supported:

> “P01 + P04 + P06 + P03 + P07 provide sufficient heterogeneous evidence to declare Curator-method validation complete.”

Because P03 and P07 are invalidated, the project has **not** yet earned that transition.

Therefore also withdraw:

- “Minimal Curator V0.1 is validated”;
- “current authoritative phase is REAL USER PILOT”.

## 5. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` remains a useful **experimental candidate** because its leverage-first direction is consistent with the North Star.

However:

- it is not validated Minimal Curator V0.1;
- P03/P07-specific behavior claims are not accepted evidence;
- future changes must be driven by trustworthy card evidence, not by making the Skill appear complete.

## 6. Main uncertainty now

The dominant uncertainty is again:

> **Does the Curator decision method generalize cleanly to another materially different delivery artifact class when the evidence chain is trustworthy?**

Next card:

> **P03 — requirements / rules → clickable prototype / UI demo**

After a trustworthy P03 close, execute one engineering-type card such as P07 or P10 before deciding whether the method is ready for a minimal real-user pilot.

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
