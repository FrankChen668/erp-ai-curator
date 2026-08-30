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

### P01 — workshop/minutes → requirement package

> **KEEP FOR PRACTICAL CURATION — high task fit / low independent validation**

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

## 4. Cross-task method conclusion — accepted

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

The heterogeneous evidence supports a stable method skeleton:

1. start from the real job, current baseline, artifacts, deliverable and hard constraints;
2. specialized capability only for a concrete capability gap whose benefit justifies adoption cost;
3. external adoption questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests only when their result can change the recommendation;
6. strong match and stopping discipline outrank resource coverage.

Historical verdict wording “METHOD READY FOR REAL-USER PILOT” remains valid only as a historical readiness checkpoint; current stage naming is defined below.

## 5. Current Skill — 0.7.0

`skills/curating-erp-ai-resources/SKILL.md`:

> **Curation pilot — user-use value unvalidated / version 0.7.0**

0.7.0 is a project-wide calibration, not new product validation. It consolidates lessons from 0.6.1–0.6.3 and the project audit:

- current baseline instead of bare-model comparison;
- `information missing != C`;
- C no longer automatically produces a user test protocol;
- “best/unique/validated” treated as high-evidence language;
- default recommendation is decision-relative: the practice/resource most worth prioritizing for the current task and constraints;
- runtime Skill is separated from project/history documentation.

Supporting historical Harness decisions remain:

- `CURATOR_062_HARNESS_PATCH.md`
- `CURATOR_063_BEST_PRACTICE_BOUNDARY_PATCH.md`

Current project calibration authority:

- `docs/PROJECT_CALIBRATION_20260830.md`

This is engineering/scope evidence, not user-value evidence.

## 6. Closed 0.6.1 boundary regression — internal evidence only

Authorities:

- `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Findings:

- no over-tooling signal;
- under-tooling appeared in Case 5/38 and lightly in Case 8;
- C-as-missing-information and recurring decomposition defects were not confirmed;
- no clear repeatable Curator uplift over ordinary Agent was demonstrated.

The regression informed Harness design but does **not** prove product value.

## 7. REAL_USER_ORIGIN CURATION — current Lane A

These cases originate from real survey/user problems, but the curation was produced by Cloud, not by an observed end-user interaction:

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md`
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md`

Status:

> **REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE**

They can support claims about task provenance, curation method behavior and evidence quality. They cannot support claims about adoption, time savings, reduced rework or superiority over ordinary AI/self-search.

## 8. REAL_USER_USE VALIDATION — current Lane B

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

This remains unresolved.

## 10. Next accepted evidence

Near-stage Cloud work may add a small number of **high-discrimination REAL_USER_ORIGIN** cases because those are real demand inputs and can falsify runtime behavior.

Current bounded plan: Case 003 (A/no-new-tool control) + Case 004 (system-access/permission boundary), then stop bulk curation and reassess Pack 01.

Product-value claims still require Lane B.

Do not substitute:

- synthetic benchmark loops;
- Owner/Agent opinion that output “looks good”;
- more resource links without a real problem;
- user tool-test protocols designed mainly to prove Curator;
- internal validator success.

## 11. Evidence acceptance rule

External claims must remain traceable to actually acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
