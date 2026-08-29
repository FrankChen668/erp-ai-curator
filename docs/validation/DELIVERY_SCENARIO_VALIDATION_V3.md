# ERP AI Curator — Delivery Scenario Validation V3

Date: 2026-08-29

## 1. Why this replaces the standard-module diagnostic as the current priority

The current validation priority is **project delivery work**, not ERP knowledge learning for its own sake.

ERP AI Curator originated from a practical internal-training/resource-curation need: help implementation consultants, project/product people and developers use AI better in real delivery work, and quickly find a small number of resources worth learning or sharing.

Therefore the most important validation surface is:

> **Can Curator help people complete or improve real project-delivery outputs, and can it find genuinely useful external resources for those outputs?**

Learning an unfamiliar SAP/Oracle module remains a valid secondary scenario, but it is not the next mainline test.

## 2. Two scenario families

### A. Delivery-output scenarios

The user is trying to produce or improve a project artifact/outcome.

Examples:

- requirements analysis;
- solution design;
- data processing/reconciliation;
- PPT/document creation;
- interactive prototype;
- testing / issue analysis when real evidence exists.

### B. Tool-onboarding scenarios

The user wants to learn a tool that can materially improve delivery work.

Examples:

- Codex;
- WorkBuddy;
- other Agent / AI tools only when they are relevant to actual delivery work.

Tool onboarding is not a generic software tutorial catalog. The question is:

> **What is the shortest reliable path from “I heard of this tool” to “I can use it in ERP/project delivery”?**

## 3. Current representative scenario bank

These are validation prompts, not a permanent taxonomy.

### D01 — Requirements analysis

> 一个实施顾问拿到了客户访谈纪要、现状流程、RFP/需求清单和若干附件，希望借助 AI 更快形成结构化需求、待澄清问题、冲突/遗漏、As-Is/To-Be、Fit-Gap/Fit-to-Standard 和可追溯的需求文档。请寻找少量真正值得采用或学习的 AI Skill、Tool、方法、教程和实战资源，重点看如何基于真实材料工作、如何避免模型脑补、如何保留来源和待确认项。

Desired evidence:

- practical workflow, not generic “AI writes BRD” claims;
- source-grounded requirement extraction;
- decision/open-question discipline;
- fit/gap or solution handoff;
- real prompts/templates/examples where available.

### D02 — Solution design

> 需求基本确认后，项目团队需要把业务需求转成可评审的方案设计：业务流程、系统边界、功能/配置、接口、数据、异常、权限、实施约束和待决策项。请寻找少量优秀的 AI Skill、Tool、方法、教程和真实实践资源，帮助顾问/产品经理形成更完整、可核验的方案，而不是让 AI 直接编造架构。

Desired evidence:

- requirement → design trace;
- architecture/flow/interface/data reasoning;
- review/checklist/decision records;
- distinguish generated proposal vs confirmed design.

### D03 — Data processing / reconciliation

> 项目交付中经常拿到 Excel/CSV/系统导出数据，需要清洗、多表匹配、字段映射、差异核对、异常定位、统计分析并形成可复核结果。请寻找值得泛 ERP 人员学习的 AI Skill、Tool、方法、教程和实战资源，尤其关注可重复、可校验、不会破坏原始数据的工作流。

Desired evidence:

- spreadsheet/CSV workflow;
- reconciliation and exception handling;
- reproducibility;
- auditability;
- privacy/data-boundary guidance;
- when coding/Agent is better than chat/manual Excel.

### D04 — PPT / project communication

> 实施顾问、项目经理或产品经理已经有需求、方案、数据或项目材料，希望借助 AI 快速形成可用于客户汇报/项目评审的高质量 PPT，同时保持业务逻辑、证据、图表和版式可编辑。请寻找真正值得采用的 AI Tool、Skill、方法、教程和最佳实践。

Desired evidence:

- source material → storyline → slide structure → visual artifact;
- editable PPT/slide output where relevant;
- diagram/chart generation;
- review and correction workflow;
- not just “one-click pretty slides”.

### D05 — Interactive prototype

> 将需求、业务规则和方案快速转成可点击、可评审的交互原型，用于需求澄清和方案评审。寻找优秀 AI Tool/Skill/方法和真实实战资源，关注业务状态、异常、角色、字段和评审闭环，而非只生成漂亮页面。

This scenario has historical T01 evidence. Re-run only when a fresh comparison question exists; do not repeatedly mine the same answer set.

### T01 — Codex for project delivery

> 面向没有深厚编程基础、但从事 ERP/企业信息化交付的顾问、产品经理、项目经理和开发人员，寻找当前最值得学习的 Codex 官方教程、使用方法和实战最佳实践。目标不是学 Codex 功能大全，而是尽快会用于：分析项目资料/代码、生成或修改交付物、执行本地任务、审查结果、与 GitHub 协作以及安全使用 Agent。

Expected source mix:

- current OpenAI official documentation for capabilities/setup/safety;
- high-quality practitioner examples for actual workflow and pitfalls;
- GitHub Skills/workflows only when they materially help.

### T02 — WorkBuddy for project delivery

> 面向 ERP/企业信息化项目人员，寻找当前最值得学习的 WorkBuddy 官方教程、使用说明和高质量实战最佳实践。目标是尽快会把它用于需求/资料整理、内容采集、方案/PPT/原型等项目工作；明确它与普通网页版 AI、本地 Agent/Codex 的边界和适用场景。

Expected source mix:

- WorkBuddy original/official material for current capability/setup;
- Chinese practitioner content where it gives concrete operation steps/cases;
- WeChat/Bilibili/Xiaohongshu acquisition adapters only when qualified and materially useful.

## 4. Priority order

Do not test every scenario at once.

Current order:

1. **D01 Requirements analysis** — highest direct consultant value and strong practitioner-content opportunity.
2. **D03 Data processing / reconciliation** — tests a very different, highly repeatable delivery workflow.
3. **T01 Codex for project delivery** — tests official-tutorial + practitioner-best-practice curation.
4. **T02 WorkBuddy for project delivery** — tests Chinese-tool/current-tutorial discovery and local-source acquisition value.
5. D02 Solution design.
6. D04 PPT/project communication.
7. D05 prototype only if a fresh question remains after existing T01 evidence.

This ordering is provisional. Real survey/user problems should replace representative prompts when available.

## 5. Validation method

### For explicit resource-curation tasks

Do not force a full Mode A/B/C diagnosis when the user explicitly asks to find current tutorials/Skills/Tools/resources.

Use:

```text
real delivery problem
→ define the actual output/job
→ discover serious candidates
→ read original/current sources
→ find practitioner evidence when adoption matters
→ falsify important candidates
→ curate a small package
→ stop
```

### For AI-work-method tasks

Keep the V3 leverage question:

> Is the current AI/tool stack already sufficient, or does a specialized method/Tool/Skill add material value?

Do not recommend another dependency by default.

## 6. Source strategy for delivery scenarios

A strong package may combine:

- official/original fact anchor;
- GitHub Tool/Skill/project;
- practitioner guide/case;
- video/tutorial;
- community counter-evidence.

No platform quota.

For current product/tool facts (Codex, WorkBuddy, Figma, etc.), current official/original sources have high value.

For actual adoption/workflow, practitioner evidence often matters more.

Chinese practitioner content is especially useful when it provides:

- screenshots/steps;
- prompts/templates;
- real project case;
- inputs and outputs;
- failure modes;
- learning cost;
- local enterprise constraints.

But Chinese language is not a quality signal by itself.

## 7. Output boundary

Curator should return a small share-worthy package.

External resources and Curator synthesis must be separated.

Never present a newly invented prompt/framework as if it were a discovered external resource.

Preferred output:

- Main recommendation;
- optional fact anchor;
- optional practical companion (default 0–1);
- optional second solution only for a different boundary;
- important rejected candidates (max 3);
- coverage gaps;
- share-worthiness / uncertainty.

## 8. Adapter policy during these tests

Source adapters remain optional acquisition capabilities.

Current qualified pilot path:

- WeChat search → original article reader.

Do not invoke it mechanically.

Use only when a concrete practitioner-content gap could change the package.

Bilibili/Xiaohongshu remain non-blocking until independently qualified.

## 9. First next local test

Run **D01 Requirements analysis** first.

Purpose:

> Test whether the current Curator/source strategy can find a strong project-delivery resource package without falling back to official-only material, generic prompt lists, or self-invented methods.

This is a curation-quality test first. Do not make it another adapter A/B unless the result exposes a specific source-access question.

## 10. Stop / anti-drift

Stop if validation turns into:

- generic ERP knowledge learning as the mainline;
- tool catalog construction;
- one scenario per software product;
- mandatory platform coverage;
- endless A/B variants;
- invented Curator methods presented as external resources;
- measuring link count instead of delivery usefulness.

The project exists to improve real project delivery work, not to maximize research machinery.
