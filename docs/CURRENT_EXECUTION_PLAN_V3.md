# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator is a bounded Curator / Orchestrator for **real ERP / enterprise-information-system delivery work**.

Its job is:

> **Given a real project job with actual inputs and an expected deliverable, help the practitioner choose a useful AI working approach; when external resources are needed, find and curate a small number of resources worth learning, trying or sharing.**

The basic unit is not a capability label such as `requirements analysis`, `PPT` or `data processing`.

The basic unit is:

```text
real project situation
+ actual input artifacts
+ next required deliverable
+ review / time / privacy constraints
→ decide how AI can help
→ find only the external resources that materially improve that job
→ practical, share-worthy recommendation
```

Curator owns judgement. Source adapters only acquire evidence.

Curator-created usage guidance must be labelled as synthesis, not presented as a discovered external resource.

## 2. Practical grounding

Current validation authority for real delivery jobs:

- `docs/validation/DELIVERY_JOB_MAP_V3.md`

It covers recurring work such as:

- workshop preparation;
- post-workshop requirement package;
- solution / blueprint design;
- Excel/CSV cleaning, mapping and reconciliation;
- customer / steering PPT;
- interactive prototype;
- test/UAT/defect analysis;
- weekly issue/action closure;
- training / handover;
- Codex / WorkBuddy adoption for delivery.

This is **not** a permanent product taxonomy and must not become one Skill per job.

The priority is practical project delivery, not ERP knowledge learning for its own sake.

## 3. What is already supported

### Curation behaviour

- official/original sources are fact anchors, not automatic recommendation winners;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- practical content must add real workflow/example/failure/adoption evidence;
- Chinese practitioner coverage mixes access, indexing and true quality/scarcity;
- Curator synthesis must be separated from discovered resources.

### Source adapters

Local qualification:

- WeChat discovery: `CONDITIONAL`;
- WeChat public article reader: `KEEP FOR PILOT`;
- first Bilibili provider: `CONDITIONAL / credential blocked`;
- first Xiaohongshu provider: `REMOVE`.

WeChat Search → Reader multi-Skill routing: `PASS` for this bounded chain only.

This proves composition feasibility, not user-value uplift.

### Uplift test

The first mixed-task A/B produced `NO MATERIAL UPLIFT` because the treatment was not used and the task mixed standard-module learning with codebase archaeology.

Do not repeat that mixed-task design.

## 4. Current provider state

```text
wechat_discover_public_articles
  zjp1997720/wechat-article-search → CONDITIONAL

wechat_read_public_article
  Githun1314/agent-wechat-reader → KEEP FOR PILOT

bilibili
  XZXZZX-Ai/bilibili-mcp → CONDITIONAL / credential blocked
  sandraschi/bilibili-mcp → cloud-reviewed alternative; local test deferred

xiaohongshu
  xpzouying/xiaohongshu-mcp → REMOVED
  replacement → none approved
```

Do not expand adapter footprint until a real delivery job demonstrates a material source-access gap.

## 5. Current validation strategy

Stop validating broad categories.

Use concrete delivery jobs with real inputs and outputs.

Current high-value set:

1. `J02` — after a customer workshop, create a reviewable requirements package;
2. `J04` — clean/reconcile Excel/CSV/project data and produce an auditable exception result;
3. `J05` — turn project material into an editable customer/steering deck;
4. `J06` — turn confirmed requirements into a reviewable interactive prototype; historical evidence already exists, so only revisit when there is a fresh question;
5. `J10` — learn Codex / WorkBuddy through actual delivery jobs rather than feature tours.

`J03` solution design follows when J02 is stable because it consumes requirement outputs.

Real survey/user problems should replace representative prompts whenever available.

Do not mechanically run every job.

## 6. Immediate next local task — J02 Post-Workshop Requirements Package

Protocol:

- `docs/validation/DELIVERY_J02_POST_WORKSHOP_REQUIREMENTS.md`

Real job:

> A consultant finishes a two-hour customer requirements workshop today. They have a transcript/notes, an As-Is process diagram, an RFP/requirement list, several Excel/Word attachments and screenshots. Tomorrow morning they must deliver a first reviewable package containing structured requirements, source/quote/owner, open questions, conflicts/assumptions, As-Is→To-Be changes, preliminary Fit/Partial/Gap with verification boundary, and a traceability foundation.

The test asks:

> **Can Curator find a small set of external resources that a real consultant could learn tonight and use on tomorrow's project material?**

This is a curation-quality test, not another routing/A-B test.

Normal Web/GitHub/current public sources may be used. WeChat Search → Reader is optional only when a real Chinese-practice evidence gap matters.

Do not force adapter use.

## 7. J02 success evidence

A useful result must make it possible to answer:

- What real project inputs can I give the method/tool?
- What concrete workflow/output does it provide?
- Which part of tomorrow's deliverable becomes easier?
- What still requires consultant/customer/system verification?
- What setup/privacy/learning cost exists?
- Why is this better than simply asking a generic chatbot to summarize the meeting?

The result should fail if it is mainly:

- generic prompt lists;
- feature tours;
- vendor marketing;
- abstract BA theory;
- self-invented Curator frameworks disguised as resources;
- links with no input→workflow→output path.

## 8. Cloud / local / Owner split

### Cloud / ChatGPT

Owns product direction, first-principles/adversarial review, source/provider research, evidence interpretation, GitHub maintenance and final KEEP/REMOVE/product decisions.

### Local Codex

Owns local-runtime execution, installed Skill/MCP use, fresh curation runs and observable evidence.

Local Codex does not redefine V3 or install unassigned adapters.

### Product Owner

Only unavoidable login/privacy/business-semantics decisions and final human usefulness judgement.

## 9. What happens after J02

Cloud reviews the actual package first.

Do **not** automatically run the next scenario.

If J02 output is genuinely practical:

- preserve the useful resources;
- identify what discovery behaviour produced them;
- then move to a different artifact type such as J04 data reconciliation or J10 Codex/WorkBuddy onboarding.

If J02 is still abstract:

- fix the resource-search / output contract;
- do not create more test machinery.

The project goal is to start accumulating a small number of **actually useful delivery resources**, not to maximize validation documents.

## 10. Anti-drift

Stop if work turns into:

- generic ERP knowledge learning as the mainline;
- capability labels detached from actual artifacts;
- a tool/resource catalog;
- one test per software product;
- mandatory platform coverage;
- endless A/B machinery;
- link-count scoring;
- source adapters making final recommendations;
- Curator synthesis presented as external resources;
- local PASS treated as independent-user validation;
- more validation documents without a better delivery package.

The project advances only when the next action helps a real ERP colleague do real project work better.