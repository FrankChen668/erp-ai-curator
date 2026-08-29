# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator is a **bounded Curator / Orchestrator hypothesis** for泛 ERP / 企业信息化项目工作。

Its job is:

> **Given a real project-delivery problem, help the user choose a useful AI working approach; when external resources are needed, find and curate a small number of resources worth learning, trying or sharing.**

Current flow:

```text
real delivery problem
→ understand expected output + constraints
→ compare current AI/tool baseline when needed
→ decide whether external discovery is needed
→ normal Web/GitHub first
→ approved read-only source adapters only when a material evidence gap exists
→ compare original evidence + practitioner value
→ small actionable recommendation package
```

Curator owns judgement. Source adapters only acquire evidence.

Curator-created usage guidance must be labelled as synthesis, not presented as a discovered external resource.

## 2. Current validation focus

The mainline is **project delivery**, not ERP knowledge learning for its own sake.

Primary scenario families:

### Delivery-output work

- requirements analysis;
- solution design;
- data processing / reconciliation;
- PPT / project communication;
- interactive prototype;
- testing / issue analysis when supported by real tasks.

### Tool onboarding for delivery

- Codex;
- WorkBuddy;
- other AI/Agent tools only when they materially support delivery work.

Current scenario authority:

`docs/validation/DELIVERY_SCENARIO_VALIDATION_V3.md`

The previously proposed SAP EWM standard-module diagnostic is **deferred / secondary**, not the current next task.

## 3. What is already supported

### Curation behaviour

- official/original sources are fact anchors, not automatic recommendation winners;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- practical companion content must add real workflow/example/failure/adoption evidence;
- Chinese practitioner coverage mixes access gap, index bias and true quality/scarcity;
- Curator synthesis must be separated from external resources.

### Source-adapter lifecycle

Local qualification produced real provider decisions:

- WeChat discovery: **CONDITIONAL**;
- WeChat public article reader: **KEEP FOR PILOT**;
- first Bilibili provider: **CONDITIONAL / credential blocked**;
- first Xiaohongshu provider: **REMOVE**.

### Bounded composition

WeChat multi-Skill routing: **PASS** for this chain only.

```text
Curator evidence need
→ WeChat Search
→ mp.weixin.qq.com candidate
→ WeChat Reader
→ original body + metadata
→ Curator judgement
→ stop
```

This proves bounded composition, not arbitrary Skill orchestration or user-value uplift.

### First uplift test

`CURATION_UPLIFT_AB_TEST_01` produced **NO MATERIAL UPLIFT for that exact mixed task** because Run B did not invoke WeChat.

Useful finding:

- conditional routing discipline held;
- pairwise search/model variance is real;
- the mixed standard-ERP/custom-codebase task was a poor validation surface.

Do not repeat that test.

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

Do not expand adapter footprint until a delivery task demonstrates a material source-access gap.

## 5. Next phase — Delivery Scenario Validation

Status: **NEXT / LOCAL**

Do not test all scenarios at once.

Priority:

1. **D01 Requirements analysis**
2. **D03 Data processing / reconciliation**
3. **T01 Codex for project delivery**
4. **T02 WorkBuddy for project delivery**
5. D02 Solution design
6. D04 PPT/project communication
7. D05 prototype only when a fresh question remains after historical T01 evidence

Real survey/user problems should replace representative prompts when available.

## 6. Immediate next local task — D01 Requirements Analysis

Question:

> Can Curator find a small, genuinely useful resource package for AI-assisted requirements analysis in project delivery without collapsing into generic prompt lists, official-only references, or self-invented methods?

Raw scenario:

> 一个实施顾问拿到了客户访谈纪要、现状流程、RFP/需求清单和若干附件，希望借助 AI 更快形成结构化需求、待澄清问题、冲突/遗漏、As-Is/To-Be、Fit-Gap/Fit-to-Standard 和可追溯的需求文档。请寻找少量真正值得采用或学习的 AI Skill、Tool、方法、教程和实战资源，重点看如何基于真实材料工作、如何避免模型脑补、如何保留来源和待确认项。

This is a **curation-quality test first**, not another adapter A/B.

Normal Web/GitHub and current accessible sources may be used. The qualified WeChat chain may be used only when a concrete practitioner-evidence gap matters.

Do not force source-adapter use.

## 7. D01 success evidence

A useful result should show:

- at least one serious external resource/method worth trying;
- source-grounded handling of real project material;
- explicit treatment of assumptions/open questions/conflicts;
- traceability from input material to requirements/decisions;
- practical adoption guidance based on original/practitioner evidence;
- honest limitations and maturity uncertainty.

It should not rely on:

- generic “AI can write BRD” claims;
- prompt collections with no real workflow;
- vendor marketing alone;
- Curator-invented frameworks disguised as discovered resources;
- platform/link volume.

## 8. Cloud / local / Owner split

### Cloud / ChatGPT

Owns product direction, first-principles/adversarial review, source/provider research, evidence interpretation, GitHub docs/PRs and final KEEP/REMOVE/package decisions.

### Local Codex

Owns local runtime execution, installed Skill/MCP use, isolated search/curation runs and observable evidence.

Local Codex does not redefine V3 or install unassigned adapters.

### Product Owner

Only unavoidable login/privacy/business-semantics decisions and final human usefulness judgement.

## 9. Non-blocking tracks

Bilibili replacement, Xiaohongshu provider research and standard-module learning are deferred.

Do not install more source adapters before delivery-scenario evidence justifies them.

## 10. Anti-drift checks

Stop if work turns into:

- generic ERP knowledge learning as the mainline;
- a tool/resource catalog;
- one test per software product;
- mandatory platform coverage;
- endless A/B machinery;
- link-count scoring;
- source adapters making final recommendations;
- Curator synthesis presented as external resources;
- local PASS treated as independent-user validation.

The project advances only when the next action reduces uncertainty about **real project-delivery usefulness**.
