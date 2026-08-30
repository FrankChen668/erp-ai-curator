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

## 3. Cross-task method conclusion — accepted for controlled trial

Authority: `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Stable method insights remain:

1. start from the real job, current toolchain, artifacts, deliverable and hard constraints;
2. do not add specialized capability unless a concrete gap matters enough to justify adoption cost;
3. external practice/adoption questions prioritize practitioner workflow/review/failure evidence;
4. source/project/system grounding outranks model memory for important domain facts;
5. runtime/local tests are only useful when they can change the recommendation;
6. strong match and stopping discipline outrank coverage.

These are product/method insights, not a requirement that runtime expose an A/B/C framework.

## 4. Real controlled-use defect — accepted negative evidence

Triggering prompt:

> “使用这个 skill 给我找下做流程图的最佳实践”

Observed 0.7.0 failure:

- quickly treated the task as no-new-tool;
- mainly used OMG/Camunda/Microsoft/ASQ official/standard sources;
- wrote a generic flowchart tutorial and prompt;
- failed to surface the expected Chinese product-manager/ToB/practitioner resources.

Cloud follow-up immediately found high-match public Bilibili/draw.io practitioner content, so the failure was runtime discovery behavior, not content scarcity.

Authority: `CURATOR_071_PRACTITIONER_DISCOVERY_PATCH.md`.

This is accepted **negative REAL_USER_USE product-behavior evidence**. It does not prove any later version fixed user value in the original host.

## 5. Current Skill — 0.8.0

`skills/curating-erp-ai-resources/SKILL.md`:

> **CONTROLLED USER TRIAL — USER-USE VALUE UNVALIDATED / version 0.8.0**

0.8.0 is a simplification response to a second-order risk exposed by the 0.7.x evolution:

> repeated local fixes were making the runtime Skill itself too complex.

The current runtime therefore removes mandatory A/B/C classification and deletes two runtime references:

- `adoption-consistency.md`
- `decision-boundaries.md`

It keeps only the essential execution path:

```text
understand the real task
→ identify whether the user wants practice discovery, adoption advice, or both
→ practitioner-first discovery when material
→ verify serious candidates/current facts
→ select a few high-fit recommendations and stop
```

Runtime references now only cover:

- practitioner discovery;
- evidence/safety for external/executable/high-risk recommendations.

Authority: `CURATOR_080_RUNTIME_SIMPLIFICATION.md`.

Engineering/scope simplification is not user-value evidence.

## 6. Closed internal evidence remains bounded

### 0.6.1 boundary regression

Authorities:

- `CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
- `CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Findings remain: no over-tooling signal; some under-tooling; no clear repeatable Curator uplift over ordinary Agent.

### Curation Pack 01 — REAL_USER_ORIGIN closed

Authority: `CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Historical case labels remain useful as evidence records:

- Case 001 — ERP operating manual: historical B;
- Case 002 — Oracle EBS development: historical B;
- Case 003 — weekly report/PPT consolidation: historical A;
- Case 004 — SAP bug/system evidence access: historical A → conditional B.

0.8.0 does not reopen Pack 01 and does not require runtime to reproduce those labels.

## 7. Release readiness

Original readiness authority: `RELEASE_READINESS_ADVERSARIAL_20260830.md`.

Current verdict remains:

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

The public repository still has no `LICENSE`; open-source release completion requires explicit Owner licensing choice.

## 8. REAL_USER_USE VALIDATION — active

Authority: `docs/REAL_USER_PILOT_V1.md`.

Strong product-value evidence comes from real users naturally receiving recommendations and learning/adopting/modifying/rejecting/ignoring them with concrete reasons or outcomes.

Current dominant uncertainty:

> **Does Curator consistently provide a higher-trust, lower-noise, more useful set of practitioner practices/resources than ordinary AI or self-search, and is that difference valuable enough that real users return?**

Prefer natural evidence about:

- whether selected practitioner links are actually useful;
- saved search/filtering effort;
- over-tooling or missed specialized capability;
- missed environment/privacy/version constraints;
- whether users return with another problem.

Do not substitute more internal cards, synthetic benchmark loops, user test protocols or validator success for this evidence.

## 9. Evidence acceptance rule

External claims must remain traceable to actually acquired evidence. Search snippets are discovery only. Author self-practice is not independent validation. Runtime evidence is bounded to what was actually tested. Stable practice insight must be separated from version-coupled facts.
