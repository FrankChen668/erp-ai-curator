# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Supported by evidence

### Real-user demand evidence now exists

The training survey export contains **83 responses** from the target delivery population:

- implementation consultant: 37 (44.58%);
- project manager: 30 (36.14%);
- developer: 8 (9.64%);
- presales: 5 (6.02%);
- other: 3 (3.61%).

This is genuine `REAL_USER demand evidence`, although the exported free text may contain platform-side wording cleanup or summarization.

Therefore:

- closed-choice aggregates are treated directly;
- free-text answers are used for repeated semantic work patterns, not assumed verbatim;
- user identifiers are not retained in project evidence.

Under Q18, 78 respondents supplied at least one non-empty concrete-work-problem entry after excluding obvious blank/`无`/`-` values, producing 224 non-empty issue slots. This supports a move from representative scenario design to survey-derived Problem Cards.

See `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

### The main user need is practical delivery, not AI introduction

Strong survey signals:

- frequent AI use: 51.81%; daily-work-tool use: 27.71%;
- current use: research/Q&A 93.98%, document writing 81.93%, PPT/reporting 71.08%;
- main friction: unstable AI output quality 63.86%, lack of real project cases/methods 44.58%, data-security/environment limits 38.55%;
- desired training: AI in project implementation 84.34%, project management 62.65%, Agent practice 50.60%.

Therefore the main problem is not “what is AI?” but:

> **How do I use AI reliably on my actual project material to produce a deliverable I can review, edit and hand over?**

### Curation behaviour

- official/original sources are fact anchors, not automatic recommendation winners;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- practical/community content is useful only when it adds real workflow/example/failure/adoption evidence;
- Chinese practitioner coverage must distinguish access, indexing and true quality/scarcity;
- Curator-created synthesis must not be presented as an external resource.

### Adapter lifecycle / routing

Controlled Windows + Codex qualification:

- WeChat discovery: `CONDITIONAL`;
- WeChat original reader: `KEEP FOR PILOT`;
- first Bilibili provider: `CONDITIONAL / credential blocked`;
- first Xiaohongshu provider: `REMOVE`.

WeChat Search → Reader bounded multi-Skill routing: **PASS**.

This proves acquisition composition feasibility, not general user-value uplift.

### First uplift test

`CURATION_UPLIFT_AB_TEST_01` produced **NO MATERIAL UPLIFT for that exact mixed task** because Run B did not invoke WeChat.

Positive evidence: the Curator did not mechanically call an installed adapter.

## 2. Current product unit

The main validation unit is now a **survey-derived Problem Card**, not a broad label such as `requirements analysis`, `PPT` or `data processing`.

Each card captures:

```text
real situation
+ typical project inputs
+ concrete work action
+ expected deliverable
+ acceptance conditions
+ current workaround/pain
+ important constraints
→ resources worth learning/trying/sharing
```

The survey repeatedly exposes problems such as:

- workshop/minutes → requirement package;
- requirements → PRD/FS/functional design;
- requirements/rules → interactive prototype;
- business logic → editable process/architecture diagram;
- source material → customer-ready PPT;
- Excel/CSV → clean/reconcile/validate;
- codebase → logic/FS/debug;
- requirement → test scenarios/cases;
- screenshots/steps → operation manual;
- daily inputs → weekly report/risk/action closure;
- experience/materials → reusable local knowledge/Skills.

Authority: `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

## 3. Current provider state

```text
WeChat discovery → CONDITIONAL
WeChat reader → KEEP FOR PILOT
Bilibili first provider → CONDITIONAL / credential blocked
Bilibili alternative → cloud-reviewed, local test deferred
Xiaohongshu first provider → REMOVED
Xiaohongshu replacement → none approved
```

No adapter expansion is justified merely by platform coverage.

## 4. What remains unproven

- Curator consistently produces strong, share-worthy resource packages for survey-derived concrete problems;
- a colleague can actually apply the recommended resource on real project materials with lower rework;
- WeChat practitioner evidence materially improves one of those packages;
- source-adapter value generalizes;
- Codex/WorkBuddy/PM-Skill onboarding can be curated around real jobs rather than feature tours;
- V3 should be packaged as a production Skill.

Important distinction:

> The survey provides **REAL_USER demand validation**, not yet **REAL_USER outcome validation**.

We know the problems are real. We do not yet know that Curator recommendations solve them well.

## 5. Immediate validation

Use **P01 / J02: workshop → reviewable requirement package** as the next concrete problem because it is highly repeated and has clear input/output boundaries.

The question is not “can AI do requirements analysis?”.

The question is:

> A consultant has a customer workshop transcript/notes, As-Is process material, RFP/requirement list and attachments. By tomorrow morning they need structured requirements, open questions, conflicts/assumptions and traceable evidence. What external Skills/Tools/tutorials/practitioner methods are worth learning tonight and applying tomorrow?

Run one curation test, then stop for cloud review.

Do not automatically run the rest of the problem-card queue.

## 6. Evidence asset state

| Asset | Evidence type | Current status |
|---|---|---|
| Survey export 2026-08 | REAL_USER demand evidence | strong, current |
| Survey-derived Problem Cards 01 | normalized demand evidence | current |
| T01 prototype curation | OWNER_REAL behaviour evidence | recall issue exposed |
| T02 requirements/Fit-Gap curation | OWNER_REAL behaviour evidence | fit-vs-maturity issue exposed |
| Source Adapter Qualification 01 | local runtime evidence | provider decisions proven |
| Source Adapter Routing Result 01 | local runtime evidence | WeChat bounded composition PASS |
| Curation Uplift A/B Test 01 | paired value test | NO MATERIAL UPLIFT for mixed task |
| Independent REAL_USER outcome/use results | primary solution validation | still insufficient |

## 7. Main risks

- translating survey answers back into broad consulting categories and losing concrete work units;
- treating “generate X” as success without judging rework, correctness, editability and traceability;
- over-tooling;
- adapter sprawl/platform checklist drift;
- Chinese-content halo;
- Curator synthesis mistaken for discovered resources;
- local PASS mistaken for user outcome validation;
- building more validation machinery instead of accumulating genuinely useful resources.

Do not implement a production Skill merely because routing works or because user demand exists.
