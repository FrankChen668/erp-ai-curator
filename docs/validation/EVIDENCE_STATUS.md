# Current Evidence Status

Date: 2026-08-30
Status: **CURRENT EVIDENCE AUTHORITY**

> Navigation: `docs/PROJECT_MAP.md`  
> Product: `docs/PROJECT_NORTH_STAR.md`  
> Execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`

## 1. Demand evidence — accepted

The 2026-08 training survey remains the primary REAL_USER demand source.

Supported conclusions:

- 83 responses;
- implementation consultants and project managers are the main audience;
- many respondents already use AI;
- the main gap is practical delivery quality, not AI introduction;
- repeated problems include requirements, PRD/FS, prototype/diagram/PPT, Excel/data, code/debugging, testing, project management and Agent usage;
- typical inputs are real project artifacts rather than abstract prompts.

Authority: `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Boundary: **the survey validates demand and real problem provenance; it does not validate a Curator recommendation or product value.**

## 2. Accepted task/method evidence

Accepted historical authorities remain unchanged:

- P01 — workshop/minutes → requirement package: high task fit / low independent validation;
- P04 — business logic → editable process diagram: CLOSED;
- P06 — Excel/CSV/system export → reconcile and validate: CLOSED, plain code-first default;
- P03 — requirements/rules → clickable prototype: CLOSED via Result 02;
- P07 — codebase/program → understand logic / reverse FS / defect hypotheses: CLOSED via Result 02.

Invalidated P03/P07 Result 01 files remain **INVALIDATED / NOT PRODUCT EVIDENCE**.

## 3. Cross-task method conclusion — accepted for controlled trial readiness

The heterogeneous evidence supports a stable method skeleton:

1. start from the real job, current baseline, artifacts, deliverable and hard constraints;
2. specialized capability only for a concrete capability gap whose benefit justifies adoption cost;
3. external adoption questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests only when their result can change the recommendation;
6. strong match and stopping discipline outrank resource coverage.

This supports **controlled user trial readiness**, not product-value completion.

## 4. Current Skill — 0.7.0

`skills/curating-erp-ai-resources/SKILL.md`:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.7.0**

0.7.0 consolidates:

- current baseline instead of bare-model comparison;
- `information missing != C`;
- C does not automatically produce a user test protocol;
- “best/unique/validated” as high-evidence language;
- decision-relative recommendation;
- runtime Skill separated from project/history documentation;
- adoption consistency and read-only/system-access boundaries.

Engineering/scope evidence is not user-value evidence.

## 5. Closed 0.6.1 boundary regression — internal evidence only

Authority: `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`.

Findings remain:

- no over-tooling signal;
- under-tooling appeared in Case 5/38 and lightly in Case 8;
- C-as-missing-information and recurring decomposition defects were not confirmed;
- no clear repeatable Curator uplift over ordinary Agent was demonstrated.

This informed later Harness changes but does not prove product value.

## 6. Curation Pack 01 — REAL_USER_ORIGIN Lane A closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Cases:

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md` — B;
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md` — B;
- `docs/curation-cases/CASE_003_WEEKLY_REPORT_CONSOLIDATION.md` — A;
- `docs/curation-cases/CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md` — A → conditional B.

Status:

> **PACK 01 CLOSED — METHOD DISCRIMINATION SUFFICIENT FOR CONTROLLED USER TRIAL.**

What it supports:

- Curator can return no-new-tool A;
- B can be tied to an observable capability gap;
- system/ERP access is conditional on actual evidence access needs;
- author self-practice can be kept separate from independent evidence;
- current outputs do not require users to become project testers.

What it does not support:

- user adoption;
- time/rework savings;
- superiority over ordinary AI/self-search;
- organization-wide standardization.

## 7. Release readiness

Authority: `RELEASE_READINESS_ADVERSARIAL_20260830.md`.

Verdict:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

Controlled trial readiness is supported by method convergence, Pack 01 discrimination, user-facing trial instructions and deterministic project/Harness checks.

Broad release remains unsupported because REAL_USER_USE and cross-host compatibility are unvalidated.

The public repository currently has no `LICENSE` file; public/open-source release completion requires an explicit Owner licensing decision and is not inferred by the Agent.

## 8. REAL_USER_USE VALIDATION — active Lane B

Authority: `docs/REAL_USER_PILOT_V1.md`.

Accepted product-value evidence requires a real colleague to actually receive the recommendation and naturally learn/adopt/modify/reject/ignore it, with a concrete reason or outcome.

Strong signals include:

- saved search/selection/setup effort;
- concrete adoption/rejection reason;
- missed capability/privacy/permission/version constraint;
- downstream work/rework effect if actually used;
- willingness to bring another real problem.

Do not manufacture Lane B by making users run a test protocol for the project.

## 9. Current dominant uncertainty

> **Does Curator consistently provide a higher-trust, lower-noise adoption decision than an ERP practitioner would get from ordinary AI or self-search, and is that difference valuable enough that real users would return?**

This remains unresolved and is now the primary product question.

## 10. Next accepted evidence

Prefer natural REAL_USER_USE from controlled trial users.

Do not substitute:

- more pre-user curation cards;
- synthetic benchmark loops;
- Owner/Agent opinion that output “looks good”;
- user tool-test protocols designed mainly to prove Curator;
- internal validator success.

## 11. Evidence acceptance rule

External claims must remain traceable to actually acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
