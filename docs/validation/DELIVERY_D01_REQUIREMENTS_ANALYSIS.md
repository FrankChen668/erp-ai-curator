# D01 — Requirements Analysis Curation Test

Date: 2026-08-29

## 1. Single purpose

Test one thing:

> **Can ERP AI Curator find a small set of external AI resources genuinely worth using or learning for project requirements analysis?**

This is not:

- a routing test;
- an adapter A/B test;
- a generic ERP knowledge task;
- a Skill installation task;
- a request for the Agent to invent its own requirements framework.

## 2. Raw task

Use exactly:

> 一个实施顾问拿到了客户访谈纪要、现状流程、RFP/需求清单和若干附件，希望借助 AI 更快形成结构化需求、待澄清问题、冲突/遗漏、As-Is/To-Be、Fit-Gap/Fit-to-Standard 和可追溯的需求文档。请寻找少量真正值得采用或学习的 AI Skill、Tool、方法、教程和实战资源，重点看如何基于真实材料工作、如何避免模型脑补、如何保留来源和待确认项。

Target audience is generalized ERP / enterprise-information-system delivery, not SAP-only and not software-product BA-only.

## 3. Session discipline

Use a fresh local Codex session.

Before searching, read only current authority:

- `docs/PROJECT_NORTH_STAR.md`
- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CURRENT_EXECUTION_PLAN_V3.md`
- `docs/validation/DELIVERY_SCENARIO_VALIDATION_V3.md`
- this file

Do not read before final recommendation:

- T02 old requirements/Fit-Gap results;
- Starter Pack;
- old candidate lists;
- prior owner recommendation outputs.

This protects discovery recall from answer leakage.

## 4. Research behaviour

Search for serious external resources that can improve actual delivery work.

Useful evidence may come from:

- original/official documentation;
- GitHub Skills/Agents/Tools;
- practitioner guides;
- real BA / ERP / consulting workflows;
- workshops/templates;
- high-quality videos/articles;
- community counter-evidence.

Current WeChat Search → Reader may be used only if a concrete Chinese practitioner-evidence gap matters.

Do not call WeChat just because it is installed.

Do not use Bilibili/Xiaohongshu adapters in this run.

Do not install anything.

## 5. What a serious candidate should help with

At least one of these materially:

- interview/meeting material → structured requirements;
- preserve quotes/source references;
- separate fact / assumption / open decision;
- identify omissions/conflicts/ambiguity;
- As-Is / To-Be;
- Fit-Gap / Fit-to-Standard;
- requirement IDs / decisions / design / test traceability;
- turn confirmed findings into BRD/FRD/User Story/AC/spec outputs;
- verification against system/demo/sandbox/source materials.

A candidate that merely says “AI can summarize meetings/write BRD” is weak.

## 6. Falsification

Before recommending a serious candidate, check the important failure mode that could change adoption:

- only generic prompting?
- SAP/Oracle/product-specific when the task is broader?
- marketing/training sales page rather than reusable material?
- model guesses standard capability instead of verifying it?
- no provenance/traceability?
- uploads confidential content without clear boundary?
- stale or abandoned dependency?
- heavy setup with little incremental value?

No numeric scoring.

## 7. Output

### Main recommendation

- Resource
- Type
- Why it wins for this delivery task
- What the consultant can actually do/get
- Best fit
- Important limitations
- Original link
- Evidence actually read

### Fact anchor

Optional. Use only for current/product/method facts that need authoritative anchoring.

### Practical companion

Default 0–1.

If present, explain:

- what concrete workflow/template/prompt/case it adds;
- why it is more useful than another official manual;
- source trust/limitations;
- original link;
- evidence actually read.

If none:

`No strong practical companion found`

### Second solution

Only if it serves a materially different boundary.

### Important rejected candidates

Max 3. One decisive reason each.

### Coverage gaps

State actual acquisition/access gaps.

### External resources vs Curator synthesis

List separately:

- `External resources recommended`
- `Curator synthesis` — only if any usage guidance was created by the Agent itself.

Do not mix them.

### Curation conclusion

1. Would I directly send this package to an ERP/enterprise-system colleague? `Yes / Maybe / No`
2. Strongest practical value
3. Biggest uncertainty
4. Did any source adapter materially contribute? `Yes / No`, with the acquired evidence if Yes

### Acquisition trace

Observable actions only:

- source types used;
- original content actually opened/read;
- adapter invoked or not;
- stop point.

## 8. Stop condition

Stop once there is enough evidence to make a stable small recommendation package.

Do not:

- run D03;
- run Codex/WorkBuddy scenarios;
- modify the repository;
- install candidates;
- create new validation rules;
- declare the product/Skill PASS.
