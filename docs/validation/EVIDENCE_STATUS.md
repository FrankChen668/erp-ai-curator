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

Boundary: this remains one bounded synthetic fixture, not universal production proof.

### P03 — requirements/rules → clickable prototype / UI demo

Status:

> **CLOSED — SPEC-FIRST CODE PROTOTYPE DEFAULT; FIGMA MAKE CONDITIONAL UPGRADE**

Authority:

- `P03_PROTOTYPE_CURATION_RESULT_02.md`

Supported judgement:

- the primary quality control is to turn roles, permissions, fields, validation, states, transitions and exception paths into a bounded interaction contract before generating UI;
- a competent code-capable Agent can be the default path for a reviewable local HTML/React prototype when the goal is requirement clarification rather than production UI;
- Figma Make has material added value when existing Figma/design-system context and shared Figma review matter;
- Lovable or similar hosted builders are conditional when hosted app behavior/backend/state/external sharing justify their cloud/platform constraints;
- inspected prototype Skills solve useful adjacent transformations, but none showed enough direct requirements/rules → prototype advantage to become mandatory;
- runtime A/B was not justified because the unresolved decision was adoption boundary/workflow, not raw generation capability.

Evidence boundary:

- Chinese practical workflow evidence, independent practitioner failure evidence, current platform facts and original Skill implementations are all retained with concrete URLs and limitations;
- no independent ERP-specific controlled benchmark proves prototype business correctness;
- human rule/exception review remains required.

## 3. Invalidated evidence — DO NOT USE FOR PRODUCT CONCLUSIONS

### P03 prototype sprint result

File:

- `P03_PROTOTYPE_CURATION_RESULT_01.md`

Status:

> **INVALIDATED — NOT PRODUCT EVIDENCE**

Its prior verdict remains withdrawn. It has **not** been rehabilitated by the new P03 close; only Result 02 is authoritative.

Reason:

- practitioner/source claims were retained without a sufficient concrete URL/citation/acquisition trail;
- current tool capability claims were not tied to traceable current-fact sources;
- the file was produced during a long-context sprint where researched evidence cannot be reliably separated from model synthesis.

### P07 codebase sprint result

File:

- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

Status:

> **INVALIDATED — NOT PRODUCT EVIDENCE**

Reason:

- broad claims about major code-Agent ecosystems, practitioner workflows and legacy-system practice lack concrete retained source links/citations;
- there is no auditable evidence chain sufficient to support a `CLOSED` verdict.

Its prior verdict is withdrawn. P07 must be rerun from scratch if selected next.

## 4. Cross-card conclusion — still not complete

P03 Result 02 restores one trustworthy heterogeneous artifact class, but the project still has not earned the earlier validation-complete claim.

Do **not** yet claim:

- “Curator-method validation complete”;
- “Minimal Curator V0.1 is validated”;
- “current authoritative phase is REAL USER PILOT”.

Reason: the current plan still requires one trustworthy engineering-type heterogeneous card after P03.

## 5. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` remains an **experimental candidate**.

P03 supports its leverage-first direction — especially “general AI/Agent may be enough” and “specialized capability only for a concrete missing capability” — but one new card does not independently validate the whole Skill.

Do not add prototype-specific rules merely to encode this one result.

## 6. Main uncertainty now

The dominant uncertainty is:

> **Does the Curator decision method remain stable on an engineering-type task where repository context, correctness and technical evidence matter more than visible artifact generation?**

Next controlled card:

> **P07 — codebase/program → understand logic, generate FS, find defects**

P07 is preferred over P10 because its invalid prior close creates a direct opportunity to test whether the corrected evidence discipline can survive a materially different engineering task without reusing the old conclusion.

After a trustworthy P07 close, reassess whether heterogeneous evidence is sufficient to package a minimal user-facing Curator and move into real-user adoption validation.

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
