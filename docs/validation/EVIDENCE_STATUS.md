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
- **P04 — business logic → editable process diagram**: historical task curation closed with explicit coverage gaps. Authority: `P04_PRACTITIONER_CURATION_RESULT_02.md`.
- **P06 — Excel/CSV/system export → reconcile/validate**: closed; plain code-first default / Huashu optional. Authorities: `DELIVERY_P06_DATA_RECONCILIATION.md`, `P06_LOCAL_RUNTIME_RESULT_01.md`, `evidence/p06/`.
- **P03 — requirements/rules → clickable prototype**: closed; spec-first code prototype default; Figma Make conditional. Authority: `P03_PROTOTYPE_CURATION_RESULT_02.md`.
- **P07 — codebase/program understanding**: closed; traceable read-only repo exploration default; conditional semantic/LSP or ERP-native access. Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Important 0.9.1 boundary: a historical task result such as P04 remains valid as **project research evidence at the time it was produced**; it does not automatically define a future user's current candidate pool or ranking.

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
- highlighted installs/Stars/security metadata;
- provided an install command;
- noted it had not installed because the user only asked to search.

This was stronger negative evidence because 0.8.2 already said a best-practice request does not justify an installable Tool/Skill recommendation.

Authority: `CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`.

## 9. Runtime 0.9.0 split — accepted architecture evidence

0.9.0 separated:

- `curating-erp-ai-resources` — practice/resource curation;
- `advising-erp-ai-capabilities` — capability adoption.

The next natural flowchart run no longer collapsed directly into Skill installation, which is a positive implementation signal for the responsibility split.

This does **not** by itself validate 0.9.0 or product value.

Authority: `CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`.

## 10. Fresh 0.9.0 run — accepted freshness/evidence-isolation defect evidence

The 0.9.0 practice-only run returned a more plausible practitioner answer, but its execution log proved the candidate pool was materially influenced by historical project evidence.

Directly supported facts:

- only one Web Search call was made, with four broad AI/draw.io/ERP queries;
- no targeted Bilibili, WeChat, Xiaohongshu or Zhihu discovery was executed;
- the two final `woshipm.com` articles were found through local `rg` against historical project validation, not the current Web Search;
- those two external pages were then opened directly;
- `Castaldo-Solutions/process-builder` also came from historical P04 material and was **not reopened in the current run**;
- the final user answer exposed `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md` as a project-side supporting link;
- the run did not show a current Web access/login/anti-bot/policy failure that forced this behavior.

This supports three defect classes:

1. **historical-evidence contamination** — previous project recommendation influenced the current candidate pool/ranking;
2. **freshness gap** — fast-moving AI practice was not explicitly challenged against recent/current alternatives;
3. **broad-search recall bias** — obvious Chinese practitioner pools were missed without a targeted recall correction.

A same-day Cloud targeted sanity search immediately surfaced recent candidates absent from the Local Agent's current pool, including a 2026-07 Bilibili drawio-skill update and a 2026-06 supply-chain/WMS product-manager CodeX→Draw.io workflow. This proves only that fresh discovery could materially change the serious candidate pool; it does not prove those candidates should rank first.

Authority: `CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md`.

## 11. Current Runtime — 0.9.1

Release class:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.9.1**

### Practice Curator

`skills/curating-erp-ai-resources/`

Current invariants:

- normal external curation starts with fresh current discovery;
- project history/prior validation is lead-only, not current external evidence;
- every final external recommendation is reopened/read in the current run unless the user explicitly requests reuse;
- fast-changing AI workflows include current/recent evidence checks;
- broad Web recall that misses the user's obvious practitioner ecosystem gets a targeted correction on the one/few pools most likely to change the answer;
- internal validation/history is not surfaced as user-facing external evidence unless explicitly requested;
- no default Tool/Skill/MCP adoption decision.

Reference: `practitioner-discovery.md`.

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

Behavior remains the 0.9.0 responsibility split: current baseline → concrete gap → minimum useful capability or explicit no-upgrade.

Reference: `evidence-and-safety.md`.

0.9.1 does **not** introduce newest-wins, platform quotas, resource DB/auto-refresh, a third Router Skill, A/B/C runtime taxonomy, scoring/Gate, creator ranking, or host-policy workaround.

Authority: `CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md`.

This is a runtime correction, not product-value evidence and not proof that the Local Agent host behavior is fixed.

## 12. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities: `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`, `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`.

Findings remain: no over-tooling signal in that old regression, some under-tooling, and no clear repeatable Curator uplift over ordinary Agent.

### Curation Pack 01 — REAL_USER_ORIGIN Lane A closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain evidence records only and do not define current Runtime behavior or current external resource ranking.

## 13. Release readiness

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository currently has no `LICENSE` file; public/open-source release completion requires explicit Owner licensing choice.

## 14. REAL_USER_USE VALIDATION — active Lane B

Authority: `docs/REAL_USER_PILOT_V1.md`.

Accepted product-value evidence requires a real colleague to receive a recommendation and naturally learn/adopt/modify/reject/ignore it with a concrete reason or outcome.

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more current and useful result than ordinary AI/self-search, and is that difference valuable enough that real users return?**

Highest-value next evidence after 0.9.1:

- practice-only request starts from current external discovery rather than internal project history;
- broad search recall gaps are corrected selectively, without platform quotas;
- every final external recommendation is freshly inspected;
- freshness/current applicability is considered where material;
- internal validation files stay out of normal user-facing recommendation evidence;
- explicit capability request still starts from current baseline/concrete gap and can conclude no-upgrade.

Do not substitute more pre-user cards, synthetic benchmark loops, Owner/Agent opinion, user tool-test protocols or internal validator success for product evidence.

## 15. Evidence acceptance rule

External claims must remain traceable to acquired current evidence. Search snippets are discovery only. Historical project curation is lead/history evidence, not independent current practitioner evidence. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled/current facts.
