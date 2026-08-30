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

- **P01 — workshop/minutes → requirement package**: keep for practical curation; high task fit / low independent validation.
- **P04 — business logic → editable process diagram**: closed; recommendation stable with explicit coverage gaps. Authority: `P04_PRACTITIONER_CURATION_RESULT_02.md`.
- **P06 — reconcile/validate Excel/CSV/system export**: closed; plain code-first default / Huashu optional. Authorities: `DELIVERY_P06_DATA_RECONCILIATION.md`, `P06_LOCAL_RUNTIME_RESULT_01.md`, `evidence/p06/`.
- **P03 — requirements/rules → clickable prototype**: closed; spec-first code prototype default, Figma Make conditional. Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.
- **P07 — codebase/program understanding**: closed; traceable read-only repo exploration default, conditional semantic/LSP or ERP-native access. Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Invalidated evidence remains invalid:

- `P03_PROTOTYPE_CURATION_RESULT_01.md`
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

## 3. Stable cross-task method insights

1. start from the real job, current toolchain, artifacts, deliverable and hard constraints;
2. do not add specialized capability unless a concrete gap matters enough to justify adoption cost;
3. external practice/adoption questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests matter only when they can change the recommendation;
6. strong match and stopping discipline outrank coverage.

These are product/method insights, not a requirement that runtime expose an A/B/C framework.

## 4. First flowchart controlled-use defect — accepted negative evidence

Triggering prompt:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed 0.7.0 failure:

- quickly treated the task as no-new-tool;
- mainly used OMG/Camunda/Microsoft/ASQ official/standard sources;
- wrote a generic flowchart tutorial and prompt;
- failed to surface the expected Chinese product-manager/ToB/practitioner resources.

Authority: `CURATOR_071_PRACTITIONER_DISCOVERY_PATCH.md`.

## 5. 0.8.0 simplification — accepted engineering evidence

0.8.0 removed mandatory A/B/C classification and two runtime references while preserving the core Curator path.

Authority: `CURATOR_080_RUNTIME_SIMPLIFICATION.md`.

This is engineering/scope evidence, not user-value evidence.

## 6. 0.8.0 Codex Desktop execution log — accepted diagnostic evidence

A later Codex Desktop run of the same natural flowchart request supplied detailed execution logs.

Important boundary:

> **The run was not a clean 0.8.0 isolated run.** It first loaded local 0.6.1, modified a proposed 0.6.2 and performed an initial official-heavy search; only after user correction did it fetch `main` at `d6165fa`, restore the Skill package to 0.8.0 and continue in the same context.

Therefore this run cannot prove that a fresh 0.8.0 host run would fail identically.

However, the post-sync logs directly prove several runtime/host behaviors:

- `SKILL.md 0.8.0`, `practitioner-discovery.md` and `evidence-and-safety.md` were actually read;
- the second discovery batch used broad domain queries such as `流程图 最佳实践...` and `企业流程图 画法...` but did not preserve the original AI/product/ToB/ERP work-method intent;
- no explicit Bilibili, WeChat, Xiaohongshu, Zhihu, 人人都是产品经理 or 掘金/CSDN query was executed;
- search results did include Chinese practitioner/creator candidates, but they were mostly not opened;
- the final answer again relied on official/standard/implementation sources and used no independent practitioner or author self-practice source;
- Codex Web policy exposed a potential `technical questions → primary sources only` conflict, but the log does not prove that this policy caused the final selection;
- Graph Engineering was additionally loaded because the task was considered multi-step, indicating a separate possible host Skill-collision issue;
- Browser/Chrome capabilities existed but were not used; the log does not establish whether they would materially improve source acquisition.

This supports two narrow Curator execution corrections and three separate host-risk hypotheses. Authority: `CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`.

## 7. Current Skill — 0.8.1

`skills/curating-erp-ai-resources/SKILL.md`:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.8.1**

0.8.1 adds only:

1. **query intent preservation** — when the user asks how AI/Agent/Tool improves a task, practitioner discovery must retain at least one serious `AI/tool × role/industry/artifact` query instead of collapsing into pure domain advice;
2. **candidate investigation** — explicit best-practice/tutorial requests must inspect at least one practitioner/creator candidate before synthesis, or explicitly report `coverage/policy gap` when host/search/access prevents it.

0.8.1 does **not** add:

- platform quotas;
- creator scoring;
- A/B/C runtime classification;
- new references;
- Browser mandates;
- host-policy workarounds;
- Graph Engineering exclusions.

Those would require separate evidence.

## 8. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities:

- `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Findings remain: no over-tooling signal; some under-tooling; no clear repeatable Curator uplift over ordinary Agent.

### Curation Pack 01 — REAL_USER_ORIGIN closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain evidence records only and do not define 0.8.1 runtime.

## 9. Release readiness

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository still has no `LICENSE`; open-source release completion requires explicit Owner licensing choice.

## 10. REAL_USER_USE VALIDATION — active

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more useful set of practitioner practices/resources than ordinary AI or self-search, and is that difference valuable enough that real users return?**

Next high-value evidence is a **fresh Codex Desktop context** using the same natural prompt after syncing 0.8.1, with no pre-search or Skill modification. Record actual queries, loaded references, opened practitioner candidates and final source roles.

Do not substitute more internal cards, synthetic benchmark loops or further Skill polishing for this evidence.
