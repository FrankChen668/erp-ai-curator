# P04A — Business Description → Editable Process Diagram Curation Test

Date: 2026-08-30

## 1. Real job

A generalized ERP / enterprise-information-system consultant has already collected business requirements and rough process steps.

They need to turn that material into an **editable business process diagram** for a customer workshop / blueprint / solution review without spending hours manually dragging boxes and connectors.

This is not a generic “AI diagramming” question.

The real question is:

> **What existing AI Skill / Tool / workflow / tutorial can help a consultant turn real business logic into a reviewable, editable process diagram while preserving roles, decisions, exceptions and system boundaries?**

## 2. Raw task

Use exactly:

> 你是一名泛 ERP / 企业信息化实施顾问。现在手里已有一段确认过的业务需求/流程描述、角色信息、主要单据/系统节点和若干异常场景。明天要和客户评审一张业务流程图。希望借助 AI 快速生成第一版，但最终必须可编辑、可修正、可复用，不能只生成一张漂亮图片。请寻找少量真正值得顾问立即学习或采用的现成 AI Skill、Tool、教程、方法或实战资源，重点比较：①能否从文本/需求生成流程；②是否能输出或进入可编辑格式（优先 draw.io / BPMN / Visio 或等价结构化格式）；③角色/泳道、决策分支、异常、系统边界能否表达；④如何避免 AI 编造流程关系；⑤生成后如何快速评审和迭代；⑥学习/安装/隐私成本。最终只保留真正值得发给同事直接试的少量资源。

Do not broaden this into architecture-diagram catalogs.
Do not recommend image-generation-only tools as the main solution.
Do not solve a fictional process yourself; curate reusable external resources for this job.

## 3. Survey / demand anchor

This task comes from survey-derived P04:

- consultants repeatedly need business process / end-to-end / solution diagrams;
- manual drag / resize / formatting consumes time;
- prior-project diagrams often exist but are hard to reuse consistently;
- the acceptance condition is an editable review artifact, not merely a generated image.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

## 4. Research behaviour

Use a fresh local Codex session.

Read only current authority before searching:

1. `docs/PROJECT_NORTH_STAR.md`
2. `docs/SOURCE_STRATEGY_V3.md`
3. `docs/CREATOR_PRIOR_STRATEGY_V3.md`
4. `docs/CURRENT_EXECUTION_PLAN_V3.md`
5. P04 section of `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`
6. this file

Do not read historical prototype / flowchart candidate answers before final recommendation if they would leak known candidates.

Search serious current resources across:

- original GitHub repos / Skills / MCPs;
- official product docs where current capabilities need verification;
- practitioner tutorials with actual prompts / steps / screenshots / files;
- AI PM / consultant / Agent creators when topic fit is real;
- Chinese practitioner content when it materially lowers adoption cost.

Creator Prior is optional discovery guidance, not a whitelist.

Current WeChat Search → Reader may be used only if a concrete Chinese-practice evidence gap matters.

Do not force it.

Do not use unapproved Bilibili / Xiaohongshu adapters.
Do not install any candidate in this curation run.

## 5. Serious-candidate requirements

A candidate is strong only if the original evidence lets you answer most of the following:

- What input does the consultant provide?
- What exact workflow transforms the input?
- What editable artifact is produced?
- Can the user continue editing in draw.io / BPMN / Visio / structured diagram source / another reviewable format?
- Can the workflow represent roles or swimlanes?
- Can it represent decisions / branching?
- Can it represent exception / failure paths?
- Can it preserve system boundaries or handoffs?
- What does it do when information is missing?
- How does a human review/correct the generated logic?
- What setup / runtime / privacy cost exists?

Weak candidates:

- AI image generators that produce only PNG/JPG;
- generic Mermaid introductions with no workflow for real business-process material;
- “one-click diagram” marketing with no editable output proof;
- prompt lists without actual examples/artifacts;
- tools that beautify diagrams but do not help convert business logic;
- highly complex Agent stacks whose setup cost exceeds the work saved.

## 6. Editable-output rule

The main recommendation must produce or reliably hand off to a **structured editable representation**.

Strong output examples include:

- `.drawio` / diagrams.net XML;
- BPMN XML;
- native Visio-compatible structured output;
- Mermaid / PlantUML / another text-based diagram language **only if** the practical workflow makes iterative editing and customer review realistic;
- editable Figma / whiteboard diagram objects when the source proves this path.

A rendered image alone is insufficient for the main recommendation.

## 7. Semantic-fidelity rule

The practical value is not “the boxes look good”.

The workflow should help preserve or explicitly surface:

- roles / departments;
- process sequence;
- decision criteria;
- exception branches;
- document/system handoffs;
- unknown / unresolved relationships.

Prefer resources that tell the AI to flag missing relationships rather than invent them.

## 8. Falsification

For every serious finalist, check the failure mode that could break real use:

- output is not truly editable;
- generated XML/source is brittle or fails import;
- no support for swimlanes/branches/exceptions;
- tool invents steps/relationships from vague prose;
- installation introduces broad write permissions / browser automation / risky dependencies;
- stale integration or abandoned repo;
- setup is heavier than drawing manually;
- claimed AI feature requires paid/private product access not visible in the source;
- result is mainly visual polish rather than business-logic accuracy.

No numeric score.

## 9. Output

### Main recommendation

- Resource
- Type
- Why it wins for this exact job
- Input → workflow → editable output
- Which process semantics it can represent
- How review/correction works
- Adoption / install / privacy cost
- Important limitations
- Original link
- Evidence actually read

### Practical companion

Default 0–1.

Prefer a real tutorial/case that shows concrete operation, prompt, generated file or before/after workflow.

Explain:

- what exact practical step it adds;
- what artifact/example it proves;
- source limitation;
- original link;
- evidence actually read.

If none:

`No strong practical companion found`

### Optional second solution

Only if it serves a materially different boundary, for example:

- local Agent + draw.io file generation;
- SaaS collaborative diagram workflow;
- BPMN-specialized path.

### Important rejected candidates

Max 3. Give one decisive reason each.

### Creator observation

If a specific creator's content actually passes curation, record only:

- creator/account;
- platform;
- topic strength observed;
- why this specific content was useful;
- whether it is worth adding as a discovery seed.

Do not create a creator ranking.

If no creator prior materially contributed:

`No creator-prior contribution in this run`

### Tomorrow usefulness

Answer:

1. If I send this package to an ERP consultant tonight, can they create a first editable process diagram tomorrow? `Yes / Maybe / No`
2. What exact manual work becomes easier?
3. What still requires consultant review?
4. What is the biggest adoption risk?

### External resources vs Curator synthesis

Keep separate.

### Acquisition trace

Observable source/actions only:

- sources actually used;
- original content actually opened/read;
- Creator Prior used or not;
- WeChat adapter used or not;
- stop point.

## 10. Stop condition

Stop when there is a small stable package that answers the actual editable-diagram job.

Do not:

- install candidates;
- run P03/P05/P06;
- expand source adapters;
- build a creator database;
- modify the ERP AI Curator repository;
- declare the overall product PASS.
