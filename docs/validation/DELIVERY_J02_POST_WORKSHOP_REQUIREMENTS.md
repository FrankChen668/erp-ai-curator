# J02 — Post-Workshop Requirements Package Curation Test

Date: 2026-08-29

## 1. Real job

This test is anchored to a common implementation-consultant delivery job:

> **客户需求访谈/Workshop 已经结束。顾问手里有真实材料，第二天需要产出可给客户和项目组继续评审的需求包。**

The question is not “what is requirements analysis?”.

The question is:

> **What external AI Skill / Tool / tutorial / method can materially help the consultant turn real project evidence into a better, faster, reviewable delivery package?**

## 2. Raw task

Use exactly:

> 你是一名泛 ERP / 企业信息化实施顾问。今天刚完成一场约 2 小时的客户需求访谈，手里已有：会议纪要/转写文本、客户现状流程图、一份 RFP/需求清单、2–3 个 Excel/Word 附件和少量系统截图。明天上午要给项目组形成第一版可评审需求包，包括：①结构化需求清单；②每条需求的来源/原话/责任人；③待澄清问题；④冲突、遗漏和假设；⑤As-Is → To-Be 变化点；⑥初步 Fit / Partial Fit / Gap，但标准能力必须标记“待系统/官方资料验证”；⑦需求 ID 与后续方案/测试可追溯的基础结构。请寻找少量真正值得顾问立即学习或采用的现成 AI Skill、Tool、教程、方法或实战资源。重点不是“AI 能总结会议”，而是如何基于真实材料、保留证据、暴露不确定性，并形成明天能拿去评审的交付物。

Do not broaden this into generic BA theory.
Do not change it into SAP-only Fit-to-Standard training.
Do not solve the fictional project yourself; curate reusable external resources for this job.

## 3. What counts as useful

A serious candidate should materially improve at least one difficult part of the real job:

- multi-file / transcript intake;
- requirement extraction with provenance;
- quote/source/owner retention;
- fact vs assumption vs decision vs open question;
- conflict / omission / ambiguity detection;
- As-Is / To-Be change capture;
- disciplined Fit/Partial/Gap with verification boundary;
- requirement ID / decision / design / test traceability;
- reviewable BRD/FRD/requirement-log style output;
- safe handling of confidential project material.

Weak candidates include:

- generic “10 prompts for BA” lists;
- meeting summarizers with no evidence trace;
- marketing claims without a reusable workflow;
- resources that encourage the model to decide ERP standard capability from memory;
- broad BA textbooks with no AI-enabled practical path.

## 4. Research behaviour

Use a fresh local Codex session.

Before searching read only current authority:

- `docs/PROJECT_NORTH_STAR.md`
- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CURRENT_EXECUTION_PLAN_V3.md`
- `docs/validation/DELIVERY_JOB_MAP_V3.md`
- this file

Do not read old T02 requirements/Fit-Gap outputs, Starter Pack or historical candidates before final recommendation.

Search serious current resources across:

- original/official documentation;
- GitHub Skills/Agents/Tools;
- practitioner guides / consulting / BA workflows;
- workshops / templates;
- high-quality videos/articles;
- Chinese practitioner content when it offers real steps/examples.

Current WeChat Search → Reader can be used only when a concrete Chinese-practice evidence gap matters.

Do not call it merely because it is installed.

Do not use Bilibili/Xiaohongshu adapters in this run.
Do not install anything.

## 5. Practicality test

For each finalist, answer from the actual source:

1. What project input can the consultant give it?
2. What useful output/workflow does it provide?
3. What part of tomorrow's deliverable does it improve?
4. What human/system verification is still required?
5. What setup/learning/privacy cost exists?

If these cannot be answered, the resource is too abstract for this test.

## 6. Falsification

Check the failure mode most likely to break real use:

- no provenance/traceability;
- hallucinated Fit/Gap;
- only toy inputs;
- confidential-data risk;
- product/vendor lock-in;
- stale/unmaintained dependency;
- too heavy for a one-day consulting workflow;
- polished article but no reproducible steps;
- generic software-product BA workflow that does not transfer to ERP delivery.

No numeric scoring.

## 7. Output

### Main recommendation

- Resource
- Type
- Why it wins for this exact post-workshop job
- Input → workflow → output
- Which deliverables it helps produce tomorrow
- What still needs consultant/system verification
- Adoption/privacy cost
- Important limitations
- Original link
- Evidence actually read

### Practical companion

Default 0–1.

Prefer a real hands-on workflow/case/template/video/article over another official feature page.

Explain:

- exact practical steps it adds;
- what artifact/example it shows;
- source limitation;
- original link;
- evidence actually read.

If none:

`No strong practical companion found`

### Optional second solution

Only if it solves a materially different boundary, such as local/private processing vs cloud collaboration.

### Important rejected candidates

Max 3.

### Coverage gaps

### Tomorrow-morning usefulness

Answer:

1. If I send this package to an ERP consultant tonight, can they use it on tomorrow's real project material? `Yes / Maybe / No`
2. What exact part of their work becomes easier?
3. What is still missing before this becomes operationally useful?

### External resources vs Curator synthesis

Keep separate.

### Acquisition trace

Observable sources/actions only.

## 8. Stop condition

Stop when there is a small, stable, directly usable package.

Do not continue into solution design/data/PPT/Codex/WorkBuddy tests.
Do not modify the repository.
Do not install candidates.
Do not create new frameworks.
Do not declare ERP AI Curator PASS.