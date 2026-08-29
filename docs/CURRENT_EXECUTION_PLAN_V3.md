# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator is a bounded Curator / Orchestrator for **real ERP / enterprise-information-system delivery work**.

Its job is:

> **Given a real project job with actual inputs and an expected deliverable, help the practitioner choose a useful AI working approach; when external resources are needed, find and curate a small number of resources worth learning, trying or sharing.**

The basic unit is not `requirements analysis`, `PPT`, `prototype`, `data processing` or a tool name.

The basic unit is:

```text
real project situation
+ actual input artifacts
+ concrete action that must be completed
+ expected deliverable
+ review / time / privacy constraints
→ decide how AI can help
→ find external Skills / Tools / tutorials / methods / cases that materially improve the job
→ small practical recommendation package
```

Curator owns judgement. Source adapters only acquire evidence.

Curator-created usage guidance must be labelled as synthesis, not presented as a discovered resource.

## 2. Survey is now the primary demand source

Current REAL_USER demand evidence:

- 83 survey responses from the target delivery population;
- 37 implementation consultants, 30 project managers, 8 developers, 5 presales, 3 other;
- 78 respondents supplied at least one non-empty concrete problem in Q18, producing 224 non-empty issue slots after removing obvious blanks/`无`/`-`.

Because the survey export may contain platform-side wording cleanup, do not treat every free-text sentence as verbatim. Use repeated semantic work patterns.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

This evidence overrides representative scenario invention when choosing what to curate next.

## 3. First-principles interpretation of the survey

Most respondents already use AI. The main gap is not AI awareness.

Strong signals:

- research/Q&A already used by 93.98%;
- document work 81.93%;
- PPT/reporting 71.08%;
- unstable AI output quality 63.86%;
- lack of real project cases/methods 44.58%;
- AI in project implementation is the top training request at 84.34%.

Typical inputs are actual delivery artifacts:

- Word/PDF 85.54%;
- PPT 65.06%;
- Excel 60.24%;
- meeting minutes/transcripts 59.04%;
- screenshots 40.96%;
- code/logs 26.51%.

Therefore the core product question is:

> **Given the material already on my desk, what proven AI workflow/resource helps me produce tomorrow's deliverable with less rework and acceptable quality?**

## 4. Current problem-card queue

Do not curate all problems at once.

First wave from repeated survey demand:

1. **P01 — workshop/minutes → requirement package**
2. **P02 — requirements → PRD/FS/functional design**
3. **P03 — requirements/rules → clickable prototype**
4. **P04 — business logic → editable process/architecture diagram**
5. **P05 — source materials → customer-ready PPT**
6. **P06 — Excel/CSV → clean/reconcile/validate**
7. **P07 — codebase → logic/FS/debug**
8. **P10 — requirement → test scenarios/cases**

Second wave only after useful resources are actually accumulating:

- troubleshooting/log/error analysis;
- solution completeness/adversarial review;
- manuals/training material;
- PM weekly/risk/action closure;
- local knowledge/Skill reuse;
- Codex/WorkBuddy onboarding bound to one real delivery job.

This queue is provisional and not a permanent taxonomy.

## 5. What counts as a useful resource

The survey repeatedly says AI output is unstable and requires heavy human rework.

Therefore a resource is valuable only when it improves one or more of:

- source grounding / provenance;
- correctness and completeness;
- editable output;
- repeatability;
- real project input support;
- verification/review workflow;
- reduction in manual formatting or repetitive work;
- lower correction cost;
- enterprise privacy/safety fit.

“Can generate X” is not enough.

A polished demo or generic prompt list is weak if it does not survive real project material.

## 6. Immediate next local task

Use **P01 / J02: post-workshop requirement package**.

Protocol already exists:

- `docs/validation/DELIVERY_J02_POST_WORKSHOP_REQUIREMENTS.md`

Concrete job:

> A consultant finishes a two-hour customer workshop. They have transcript/notes, As-Is process material, RFP/requirement list, Excel/Word attachments and screenshots. By tomorrow morning they need a first reviewable package containing structured requirements, source/quote/owner, open questions, conflicts/assumptions and preliminary Fit/Gap inputs.

The Curator must find a small set of external resources that can plausibly be learned tonight and applied to that material tomorrow.

This is a curation-quality test, not another routing/A-B test.

WeChat Search → Reader remains optional only when a real practitioner-evidence gap matters.

Do not force source-adapter use.

## 7. After P01

Cloud reviews the package before any next task.

Do not mechanically run P02–P10.

If P01 is practical:

- preserve the good resources as actual product assets;
- identify which discovery behaviour found them;
- then choose one **different work unit** from the survey, preferably P03/P04/P05/P06 rather than another requirements variation.

If P01 remains abstract:

- fix discovery/output behaviour;
- do not add more validation framework.

The project should now start accumulating **useful resources and practical recipes**, not more scenario documents.

## 8. Source adapters

Current state:

```text
WeChat discovery → CONDITIONAL
WeChat reader → KEEP FOR PILOT
Bilibili first provider → CONDITIONAL / credential blocked
Bilibili alternative → deferred
Xiaohongshu first provider → REMOVED
Xiaohongshu replacement → none approved
```

Adapters are evidence acquisition capabilities, not product goals.

Do not expand adapter footprint unless a survey-derived problem exposes a material source-access gap that changes the recommendation package.

## 9. Cloud / local / Owner split

### Cloud / ChatGPT

Owns:

- product direction;
- first-principles/adversarial review;
- survey interpretation;
- source/provider research;
- evidence interpretation;
- GitHub maintenance;
- final KEEP/REMOVE/product decisions.

### Local Codex

Owns only local-runtime execution:

- fresh curation runs;
- installed Skill/MCP use;
- observable source evidence;
- local installation/runtime tests when explicitly assigned.

It does not redefine V3 or install arbitrary adapters.

### Product Owner

Only unavoidable login/privacy/business semantics and final human usefulness judgement.

## 10. Anti-drift

Stop if work turns into:

- broad consulting-stage labels detached from real tasks;
- AI/tool feature catalogs;
- generic ERP knowledge learning as mainline;
- one test per software product;
- mandatory platform coverage;
- endless A/B machinery;
- link-count scoring;
- Curator synthesis presented as external resources;
- local PASS treated as user outcome validation;
- more validation documents without a better resource package.

The project advances only when the next action helps a real ERP colleague solve a real delivery problem better.
