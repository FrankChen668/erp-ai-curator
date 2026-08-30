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

## 4. Cross-task method conclusion — accepted for controlled-trial readiness

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

The heterogeneous evidence supports stable method insights:

1. start from the real job, current toolchain, artifacts, deliverable and hard constraints;
2. specialized capability only for a concrete capability gap whose benefit justifies adoption cost;
3. external adoption/practice questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests only when their result can change the recommendation;
6. strong match and stopping discipline outrank resource coverage.

These insights support controlled trial readiness; they do not require the runtime Skill to expose A/B/C classification.

## 5. Flowchart controlled-use defect — accepted negative evidence

Triggering prompt:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed 0.7.0 failure:

- quickly treated the task as no-new-tool;
- mainly used OMG/Camunda/Microsoft/ASQ official/standard sources;
- wrote a generic flowchart tutorial and prompt;
- failed to surface the expected Chinese product-manager/ToB/practitioner resources.

Authority: `CURATOR_071_PRACTITIONER_DISCOVERY_PATCH.md`.

This is accepted negative REAL_USER_USE behavior evidence. It did not prove the later correction worked in the original host.

## 6. 0.8.0 simplification — accepted engineering evidence

Authority: `CURATOR_080_RUNTIME_SIMPLIFICATION.md`.

0.8.0 removed mandatory A/B/C classification and two runtime references while preserving the core Curator path. This is engineering/scope evidence, not user-value evidence.

## 7. Codex Desktop execution log — accepted diagnostic evidence

A later Codex Desktop run of the same natural flowchart request supplied detailed execution logs.

Important boundary:

> **The run was not a clean 0.8.0 isolated run.** It first loaded local 0.6.1, modified a proposed 0.6.2 and performed an initial official-heavy search; only after user correction did it fetch `main` at `d6165fa`, restore the Skill package to exact 0.8.0 and continue in the same context.

Therefore this run cannot prove that a fresh 0.8.0 host run would fail identically.

However, the post-sync logs directly prove:

- `SKILL.md 0.8.0`, `practitioner-discovery.md` and `evidence-and-safety.md` were actually read;
- the second discovery batch used broad domain queries but did not preserve the original AI/product/ToB/ERP work-method intent;
- no explicit Bilibili, WeChat, Xiaohongshu, Zhihu, 人人都是产品经理 or 掘金/CSDN query was executed;
- search results did include Chinese practitioner/creator candidates, but they were mostly not opened;
- the final answer again relied on official/standard/implementation sources and used no independent practitioner or author self-practice source;
- Codex Web policy exposed a potential `technical questions → primary sources only` conflict, but the log does not prove that this policy caused the final selection;
- Graph Engineering was additionally loaded because the task was considered multi-step, indicating a separate possible host Skill-collision issue;
- Browser/Chrome capabilities existed but were not used; the log does not establish whether they would materially improve source acquisition.

Authority: `CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`.

## 8. Fresh 0.8.1 result — accepted candidate-selection defect evidence

A fresh 0.8.1 result for the same natural flowchart request improved practitioner discovery but produced this pattern:

- recommended a Japanese Qiita practitioner article as the primary practice;
- summarized a workflow around natural language → structured intermediate representation → editable draw.io XML → human validation → local iteration;
- additionally recommended `html-svg-diagrams` and supplied an install command;
- the user had not asked to add a Skill;
- the recommended Skill's core output focus was SVG, while the selected practice/target artifact emphasized editable draw.io.

This shows discovery improved, but selection still lost three important product dimensions:

1. **audience/ecosystem fit** — the project/user context is Chinese ERP/ToB/product-manager oriented, yet a foreign-language practitioner was promoted without showing material superiority over local candidates;
2. **artifact fit** — SVG-oriented capability was treated as a companion to editable draw.io without proving the bridge;
3. **adoption restraint** — a best-practice request triggered an installable Skill recommendation without a demonstrated capability gap.

This does **not** mean Japanese/foreign resources are undesirable. The defect is failure to rank by audience/artifact fit and failure to justify adding a capability.

Authority: `CURATOR_082_CANDIDATE_SELECTION_PATCH.md`.

## 9. Current Skill — 0.8.2

`skills/curating-erp-ai-resources/SKILL.md`:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.8.2**

0.8.2 keeps the simplified runtime and adds only three narrow candidate-selection boundaries:

1. **audience/ecosystem fit** — when the user's language/region/professional ecosystem is clear, comparable practitioner evidence from that ecosystem is preferred; cross-language resources can lead when materially stronger or local coverage is weak;
2. **artifact fit** — recommended resources/capabilities must actually support the required deliverable; adjacent output formats cannot be silently treated as equivalent;
3. **no incidental install** — a tutorial/best-practice request alone does not justify recommending an installable Tool/Skill.

0.8.2 does **not** add language quotas, country bans, creator scoring, A/B/C runtime classification, new references, Browser mandates, host-policy workarounds or platform quotas.

## 10. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities:

- `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Findings remain:

- no over-tooling signal;
- under-tooling appeared in Case 5/38 and lightly in Case 8;
- C-as-missing-information and recurring decomposition defects were not confirmed;
- no clear repeatable Curator uplift over ordinary Agent was demonstrated.

This informed later Harness changes but does not prove product value.

### Curation Pack 01 — REAL_USER_ORIGIN Lane A closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain useful as evidence records:

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md` — historical B;
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md` — historical B;
- `docs/curation-cases/CASE_003_WEEKLY_REPORT_CONSOLIDATION.md` — historical A;
- `docs/curation-cases/CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md` — historical A → conditional B.

These labels do not define 0.8.2 runtime.

## 11. Release readiness

Original release-readiness authority: `RELEASE_READINESS_ADVERSARIAL_20260830.md`.

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository currently has no `LICENSE` file; public/open-source release completion requires an explicit Owner licensing decision and is not inferred by the Agent.

## 12. REAL_USER_USE VALIDATION — active Lane B

Authority: `docs/REAL_USER_PILOT_V1.md`.

Accepted product-value evidence requires a real colleague to actually receive the recommendation and naturally learn/adopt/modify/reject/ignore it, with a concrete reason or outcome.

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more useful set of practitioner practices/resources than an ERP practitioner would get from ordinary AI or self-search, and is that difference valuable enough that real users would return?**

Continue natural use. For similar resource requests, observe whether candidate selection preserves audience/ecosystem fit, artifact fit and adoption restraint.

Do not substitute more pre-user cards, synthetic benchmark loops, Owner/Agent opinion, user tool-test protocols or internal validator success for this evidence.

## 13. Evidence acceptance rule

External claims must remain traceable to actually acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
