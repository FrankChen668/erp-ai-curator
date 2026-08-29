# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator exists for **real ERP / enterprise-information-system delivery work**.

Its basic unit is not a broad label such as `requirements analysis`, `PPT`, `prototype`, `data processing`, nor a tool name.

Use:

```text
real project situation
+ actual input artifacts
+ concrete action
+ expected reviewable deliverable
+ time / privacy / environment constraints
→ decide how AI should help
→ discover only the external Skill / Tool / method / tutorial / case that adds material value
→ read original evidence
→ compare task fit, maturity and adoption cost separately
→ return a small practical package
```

Curator owns judgement. Source adapters only acquire evidence.

Curator-created usage guidance must be labelled as synthesis, not presented as an external resource.

## 2. Demand source — survey-driven Problem Cards

Current REAL_USER demand evidence:

- 83 survey responses;
- implementation consultants and project managers are the main audience;
- 78 respondents supplied at least one non-empty concrete work problem in Q18;
- 224 non-empty issue slots were normalized into repeated work patterns.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

The survey shows the main need is not AI introduction. Many users already use AI; the harder problem is:

> **How do I use AI reliably on the material already on my desk to produce something I can review, edit and hand over with less rework?**

Typical inputs include Word/PDF, PPT, Excel, meeting transcripts, screenshots, code and logs.

## 3. Current first-wave Problem Cards

Do not curate all at once.

- P01 — workshop/minutes → requirement package
- P02 — requirements → PRD / FS / functional design
- P03 — requirements/rules → clickable prototype
- P04 — business logic → editable process / architecture diagram
- P05 — source materials → customer-ready PPT
- P06 — Excel/CSV → clean / reconcile / validate
- P07 — codebase → logic / FS / debug
- P10 — requirement → test scenarios / cases

This is a provisional queue, not a permanent taxonomy.

## 4. Source strategy

Current source authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

Rules:

- original/current evidence before recommendation;
- official/original is a fact anchor, not an automatic winner;
- practitioner content matters when it adds real operating steps, prompts, templates, examples, failure modes or adoption lessons;
- Creator Prior may improve discovery order but never determines recommendation;
- popularity/engagement is a weak discovery signal only;
- specific original content must still be read;
- open discovery must remain available so niche creators can win;
- task fit and source maturity must be judged separately.

Adversarial creator test:

> **If author name and engagement metrics were hidden, would this specific resource still deserve recommendation?**

## 5. Source-adapter state

```text
WeChat discovery → CONDITIONAL
WeChat reader → KEEP FOR PILOT
Bilibili first provider → CONDITIONAL / credential blocked
Bilibili alternative → deferred
Xiaohongshu first provider → REMOVED
Xiaohongshu replacement → none approved
```

Adapters are optional acquisition capabilities, not product goals.

Do not expand adapter footprint merely for platform coverage.

## 6. Completed — P01 / J02

Status: **CURATION COMPLETE / KEEP FOR PRACTICAL PILOT**

Result authority:

- `docs/validation/P01_CURATION_RESULT_01.md`

P01 found a low-setup practitioner working method for:

> workshop notes / transcripts → source-grounded requirement brief + traceability + conflict log + open questions

Main resource:

- `Convert Notes to Requirements Working Skill`

Cloud adversarial review confirmed:

- strong task fit;
- explicit source/speaker traceability;
- conflict and ambiguity discipline;
- practical templates/checklists;
- no requirement to install a new Agent/Skill.

But maturity is limited:

- the source itself calls the method a public working interpretation, not an official BABOK/SAP/vendor method;
- only one observed file commit exists;
- it was introduced in a batch of related working skills;
- no independent ERP-project adoption evidence was established.

Use the maturity label:

> **high task fit / low independent validation**

Also corrected from the local run:

- `T-/P-/R-/A-` numbering;
- multi-file ERP packaging conventions;
- generic confidence fields;
- combined next-morning output schema;

are **Curator synthesis/application guidance**, not direct claims from the main resource.

P01 proves useful discovery behaviour, not real-user outcome improvement.

Creator Prior and WeChat uplift were not tested because neither was needed.

## 7. Immediate next test — P04A editable business process diagram

Status: **NEXT / LOCAL**

Protocol:

- `docs/validation/DELIVERY_P04A_EDITABLE_PROCESS_DIAGRAM.md`

Concrete job:

> A consultant has confirmed business requirements / process description, roles, major documents/system touchpoints and exception scenarios. By tomorrow they need an editable process diagram for customer review. AI may generate the first draft, but the result must remain editable and correctable rather than a flat image.

Why P04A next:

- it is a different artifact type from P01;
- survey respondents repeatedly mention flow/process diagram work and manual formatting effort;
- it naturally tests executable Skills, draw.io/BPMN/Visio workflows and practical tutorials;
- it gives Creator Prior / Chinese practitioner discovery a natural opportunity without forcing any platform;
- it directly tests editability and semantic fidelity, two major user acceptance conditions.

Do **not** broaden P04A into architecture-diagram catalogs in this run.

## 8. P04A success evidence

The final package should make it possible to answer:

- What source material does the consultant provide?
- What actual steps/tool calls produce the first diagram?
- What structured editable artifact is returned?
- Can roles/swimlanes, decisions, exceptions and system handoffs be represented?
- How does the workflow avoid inventing missing process relationships?
- How does a consultant review and correct the output?
- What install/learning/privacy cost exists?
- Is the workflow faster than manual drawing after correction cost is included?

Image-generation-only tools cannot be the main recommendation.

## 9. Cloud / local / Owner split

### Cloud / ChatGPT

Owns:

- product direction;
- first-principles/adversarial review;
- survey interpretation;
- source/provider/creator research;
- maturity and evidence interpretation;
- GitHub maintenance;
- final KEEP / CONDITIONAL / REMOVE decisions.

### Local Codex

Owns:

- fresh curation runs;
- observable source evidence;
- use of already approved installed adapters when the task genuinely needs them;
- local runtime/install tests only when explicitly assigned.

It does not redefine V3 or install arbitrary adapters.

### Product Owner

Only unavoidable login/privacy/business-semantics decisions and final human usefulness judgement.

## 10. Anti-drift

Stop if work turns into:

- broad consulting-stage labels detached from actual artifacts;
- AI/tool feature catalogs;
- generic ERP knowledge learning as the mainline;
- mandatory platform coverage;
- influencer ranking / closed creator whitelist;
- endless A/B machinery;
- link-count scoring;
- calling a polished personal method an industry best practice without maturity evidence;
- Curator synthesis presented as discovered content;
- local PASS treated as real-user outcome validation;
- more validation framework without better practical resources.

The project advances only when the next action helps a real ERP colleague solve a real delivery problem better.
