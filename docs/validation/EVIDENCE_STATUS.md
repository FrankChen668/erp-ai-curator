# Current Evidence Status

Date: 2026-08-31
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
- **P06 — Excel/CSV/system export → reconcile/validate**: closed; plain code-first default / Huashu optional. Authorities: `DELIVERY_P06_DATA_RECONCILIATION.md`, `P06_LOCAL_RUNTIME_RESULT_01.md`, `evidence/p06/`.
- **P03 — requirements/rules → clickable prototype**: closed; spec-first code prototype default; Figma Make conditional. Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.
- **P07 — codebase/program understanding**: closed; traceable read-only repo exploration default; conditional semantic/LSP or ERP-native access. Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Invalidated evidence remains invalid:

- `P03_PROTOTYPE_CURATION_RESULT_01.md`
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

## 3. Stable cross-task method insights

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Stable insights:

1. start from the real job, current toolchain, artifacts, deliverable and hard constraints;
2. specialized capability only for a concrete gap whose benefit justifies adoption cost;
3. external practice/adoption questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests only when their result can change the recommendation;
6. strong match and stopping discipline outrank coverage.

These are product/method insights, not a requirement that Runtime expose A/B/C classification.

## 4. Flowchart 0.7.x defect — accepted negative behavior evidence

Triggering prompt:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed 0.7.0 failure:

- treated the task primarily as no-new-tool;
- mainly used official/standard sources;
- wrote a generic flowchart tutorial;
- failed to surface expected Chinese product-manager/ToB/practitioner resources.

Authority: `CURATOR_071_PRACTITIONER_DISCOVERY_PATCH.md`.

## 5. 0.8.0 simplification — accepted engineering evidence

Authority: `CURATOR_080_RUNTIME_SIMPLIFICATION.md`.

0.8.0 removed mandatory A/B/C classification and two runtime references while preserving the core Curator path. This is engineering/scope evidence, not user-value evidence.

## 6. Codex Desktop 0.8.0 diagnostic log — accepted diagnostic evidence

A later run of the same natural flowchart request first used old local 0.6.1/0.6.2 context, then synced 0.8.0 in the same conversation. It is therefore **not** a clean isolated 0.8.0 evaluation.

Post-sync logs nevertheless directly proved:

- `SKILL.md 0.8.0` and both references were read;
- AI/product/ToB/ERP intent disappeared from search queries;
- practitioner pools were not actually expanded;
- practitioner candidates appeared but were mostly not opened;
- final sources remained official/standard/implementation-heavy.

Separate host risks were observed but not proven causal: possible primary-source policy conflict, Graph Engineering Skill collision, and unused Browser/Chrome fallback.

Authority: `CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`.

## 7. Fresh 0.8.1 result — accepted candidate-selection defect evidence

The same natural flowchart request improved practitioner discovery but produced:

- a Japanese Qiita practitioner article as primary practice;
- a workflow centered on editable draw.io XML;
- `html-svg-diagrams` as a companion Skill plus install command;
- no demonstrated need for a new Skill;
- mismatch between editable draw.io target and SVG-oriented capability.

This showed three selection defects: audience/ecosystem fit, artifact fit, and adoption restraint.

Authority: `CURATOR_082_CANDIDATE_SELECTION_PATCH.md`.

## 8. Fresh 0.8.2 result — accepted runtime-responsibility defect evidence

After syncing `main@d44bdcc`, the user again asked the natural practice-only request.

Observed answer:

- primary recommendation: `mermaid-visualizer` from skills.sh/GitHub;
- summarized its workflow as identify relationships → choose diagram type → control layout/detail → generate Mermaid → validate → place in Markdown;
- highlighted ~1.6K installs, ~3.6K GitHub Stars and security audit status;
- provided `npx skills add ... --skill mermaid-visualizer`;
- noted it had not installed because the user only asked to search.

This is stronger evidence than the prior selection defect because 0.8.2 already explicitly stated that a best-practice/tutorial request alone does **not** justify an installable Tool/Skill recommendation.

The failure therefore cannot be explained only as a missing `no incidental install` guardrail.

Most plausible architecture-level interpretation supported by repeated behavior:

> **The single Runtime Skill description itself mixed practice curation with Tool/Skill/MCP adoption. Practice-only prompts repeatedly collapsed into capability selection despite downstream body guardrails.**

This supports separating Runtime trigger responsibilities. It does not prove exactly how the host model internally weighted metadata versus body instructions.

Authority: `CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`.

## 9. Current Runtime — 0.9.0

Release class:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.9.0**

One product now uses two Runtime Skills:

### Practice Curator

`skills/curating-erp-ai-resources/`

- best practices/tutorials/workflows/cases/resources;
- practitioner-first discovery and selection;
- no default Tool/Skill/MCP adoption decision;
- reference: `practitioner-discovery.md`.

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- whether current toolchain is enough;
- whether to add/install/choose/compare Tool/Skill/MCP/plugin/Agent/workflow;
- concrete gap → minimum useful capability or explicit no-upgrade;
- reference: `evidence-and-safety.md`.

0.9.0 does **not** add a third Router Skill, A/B/C runtime taxonomy, scoring/Gate, platform quota, creator ranking, or host-policy workaround.

Authority: `CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`.

This is an architecture correction, not product-value evidence and not proof that Codex Desktop trigger behavior is fixed.

## 10. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities: `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`, `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`.

Findings remain: no over-tooling signal in that old regression, some under-tooling, and no clear repeatable Curator uplift over ordinary Agent.

### Curation Pack 01 — REAL_USER_ORIGIN Lane A closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain evidence records only and do not define 0.9.0 Runtime.

## 11. Release readiness

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository currently has no `LICENSE` file; public/open-source release completion requires explicit Owner licensing choice.

## 12. REAL_USER_USE VALIDATION — active Lane B

Authority: `docs/REAL_USER_PILOT_V1.md`.

Accepted product-value evidence requires a real colleague to receive a recommendation and naturally learn/adopt/modify/reject/ignore it with a concrete reason or outcome.

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more useful result than ordinary AI/self-search, both for practice discovery and capability adoption, and is that difference valuable enough that real users return?**

Highest-value next evidence after 0.9.0:

- practice-only request stays in Practice Curator and does not turn into Skill installation;
- explicit capability request starts from the current baseline/concrete gap and can legally conclude no-upgrade.

Do not substitute more pre-user cards, synthetic benchmark loops, Owner/Agent opinion, user tool-test protocols or internal validator success for product evidence.

## 13. Evidence acceptance rule

External claims must remain traceable to acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
