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

Authorities: `DELIVERY_P06_DATA_RECONCILIATION.md`, `P06_LOCAL_RUNTIME_RESULT_01.md`, `evidence/p06/`.

### P03 — requirements/rules → clickable prototype

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — codebase/program → understand logic / reverse FS / defect hypotheses

> **CLOSED — traceable read-only repo exploration default; conditional LSP/semantic or ERP-native MCP upgrade**

Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

## 3. Invalidated evidence remains invalid

- `P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED / NOT PRODUCT EVIDENCE**.

## 4. Cross-task method conclusion — accepted for controlled-trial readiness

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Stable method insights:

1. start from the real job, current toolchain, artifacts, deliverable and hard constraints;
2. specialized capability only for a concrete capability gap whose benefit justifies adoption cost;
3. external adoption/practice questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests only when their result can change the recommendation;
6. strong match and stopping discipline outrank resource coverage.

These insights support controlled trial readiness; they do not require runtime A/B/C classification.

## 5. Flowchart controlled-use defect — accepted negative evidence

Triggering prompt:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed 0.7.0 failure:

- treated the task primarily as no-new-tool;
- mainly used official/standard sources;
- wrote a generic flowchart tutorial;
- failed to surface the expected Chinese product-manager/ToB/practitioner resources.

Authority: `CURATOR_071_PRACTITIONER_DISCOVERY_PATCH.md`.

## 6. 0.8.0 simplification — accepted engineering evidence

Authority: `CURATOR_080_RUNTIME_SIMPLIFICATION.md`.

0.8.0 removed mandatory A/B/C classification and two runtime references while preserving the core Curator path. This is engineering/scope evidence, not user-value evidence.

## 7. Codex Desktop diagnostic log — accepted diagnostic evidence

A later Codex Desktop run showed that 0.8.0 and its references were actually loaded after sync, but the run was contaminated by earlier 0.6.1/0.6.2 context and official-heavy searches.

Post-sync logs still directly proved:

- AI/product/ToB/ERP intent disappeared from search queries;
- practitioner pools were not actually expanded;
- practitioner candidates appeared but were mostly not opened;
- final sources remained official/standard/implementation-heavy.

Separate host risks were observed but not proven causal: possible primary-source policy conflict, Graph Engineering Skill collision, and unused Browser/Chrome fallback.

Authority: `CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`.

## 8. Fresh 0.8.1 result — accepted candidate-selection defect evidence

A fresh 0.8.1 result for the same natural flowchart request improved practitioner discovery but produced this pattern:

- recommended a Japanese Qiita practitioner article as the primary practice;
- summarized a workflow around natural language → structured intermediate representation → editable draw.io XML → human validation → local iteration;
- additionally recommended `html-svg-diagrams` and supplied an install command;
- the user had not asked to add a Skill;
- the recommended Skill's core output focus was SVG, while the selected practice/target artifact emphasized editable draw.io.

This is useful negative evidence because it shows discovery improved, but selection still lost three important product dimensions:

1. **audience/ecosystem fit** — the project/user context is Chinese ERP/ToB/product-manager oriented, yet a foreign-language practitioner was promoted without showing material superiority over local candidates;
2. **artifact fit** — SVG-oriented capability was treated as a companion to editable draw.io without proving the bridge;
3. **adoption restraint** — a best-practice request triggered an installable Skill recommendation without a demonstrated capability gap.

This does **not** mean Japanese/foreign resources are undesirable. The defect is failure to rank by audience/artifact fit and failure to justify adding a capability.

Authority: `CURATOR_082_CANDIDATE_SELECTION_PATCH.md`.

## 9. Current Skill — 0.8.2

`skills/curating-erp-ai-resources/SKILL.md`:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.8.2**

0.8.2 adds only three narrow selection constraints:

1. **audience/ecosystem fit** — when the user's language/region/professional ecosystem is clear, comparable practitioner evidence from that ecosystem is preferred; cross-language resources can lead when materially stronger or local coverage is weak;
2. **artifact fit** — recommended resources/capabilities must actually support the required deliverable; adjacent output formats cannot be silently treated as equivalent;
3. **no incidental install** — a tutorial/best-practice request alone does not justify recommending an installable Tool/Skill.

0.8.2 does **not** add language quotas, country bans, creator scoring, new runtime references, A/B/C, Gate/scoring, Browser mandates or platform quotas.

## 10. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities: `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`, `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`.

Findings remain: no over-tooling signal in that regression, some under-tooling, and no clear repeatable Curator uplift over ordinary Agent.

### Curation Pack 01 — REAL_USER_ORIGIN Lane A closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain evidence records only and do not define 0.8.2 runtime.

## 11. Release readiness

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository currently has no `LICENSE` file; public/open-source release completion requires explicit Owner licensing choice.

## 12. REAL_USER_USE VALIDATION — active Lane B

Authority: `docs/REAL_USER_PILOT_V1.md`.

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more useful set of practitioner practices/resources than an ERP practitioner would get from ordinary AI or self-search, and is that difference valuable enough that real users return?**

Continue natural use. For similar curation requests, observe whether candidate selection now preserves audience/ecosystem fit, artifact fit and adoption restraint.

Do not substitute more pre-user cards, synthetic benchmark loops or internal validator success for product evidence.

## 13. Evidence acceptance rule

External claims must remain traceable to acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
