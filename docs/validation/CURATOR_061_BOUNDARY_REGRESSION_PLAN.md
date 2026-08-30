# Minimal Curator V0.1 / Skill 0.6.1 — Boundary Regression Plan

Date: 2026-08-30
Status: **BOUNDED REGRESSION — NOT REAL_USER ADOPTION EVIDENCE**

## 1. Why this regression exists

A first local pass over real survey feedback showed a potentially important failure mode: the Curator successfully avoided unnecessary Tool/Skill recommendations, but it may have become too conservative and collapsed materially different cases into `A` or `C`.

The unresolved question is therefore not “can the Curator avoid tool hype?” It is:

> **Can Skill 0.6.1 avoid over-tooling without becoming under-tooling — i.e. can it still recognize when a specialized capability is materially worth considering?**

This regression is justified only as a bounded check of that observed defect candidate. It is not product/adoption validation and must not restart internal card accumulation.

## 2. Important semantic check

`A/B/C` is an **adoption decision**, not an information-completeness status.

- `A` — existing AI/Agent is enough for the real task at reasonable cost;
- `B` — a specialized capability has a material, observable advantage worth its adoption cost;
- `C` — a more complex option may help, but current scale/cost/constraints do not justify adoption yet; use a low-cost trial and define an upgrade trigger.

If critical information is missing and different answers would change A/B/C, the run should expose those unknowns and give conditional branches. Do **not** automatically use `C` as a synonym for “insufficient information”.

This paragraph is an evaluation clarification for the regression. It does not itself modify `SKILL.md`.

## 3. Test design — isolated paired runs

For each case, create **two completely fresh contexts** with no shared history.

### Pass A — Baseline

Input:

- only the raw survey case below;
- ordinary Agent/system capabilities available in the local environment.

Do not load:

- `skills/curating-erp-ai-resources/`;
- P03/P04/P06/P07 conclusions;
- cross-card validation docs;
- this project’s historical recommended answers.

Instruction:

> Recommend the most practical AI working method for this real ERP/enterprise-system task. Decide whether the current/general AI setup is sufficient or whether a specialized Tool/Skill/MCP/method is worth considering. Keep the answer actionable, expose critical unknowns, and research current external options only when useful.

### Pass B — Curator 0.6.1

Create another fresh context.

Load only the current distributable runtime package:

- `skills/curating-erp-ai-resources/SKILL.md`;
- `skills/curating-erp-ai-resources/references/decision-boundaries.md` only if the Skill calls for it;
- `skills/curating-erp-ai-resources/references/evidence-and-safety.md` only if the Skill calls for it.

Do not load:

- P03/P04/P06/P07 validation conclusions;
- `CROSS_CARD_METHOD_REASSESSMENT_20260830.md`;
- old Result 01 files;
- this regression plan’s evaluator section before the recommendation is complete.

Then give exactly the same raw survey case and ask the Agent to follow the Skill normally.

### Fairness requirements

- Baseline and Curator receive the same raw case text.
- Both may use current web/GitHub research if they independently decide it is necessary.
- Neither may invent missing ERP versions, environments, screenshots, logs, permissions or production access.
- No runtime test unless the run itself concludes a concrete runtime result could change the adoption decision.
- Do not force either pass to produce a particular A/B/C distribution.

## 4. Raw survey cases

No personal identity fields are included.

### Case 65 — project weekly report integration

Role: implementation consultant.

Problem:

> 多个顾问各自编写周报PPT需要进行整合、汇总整体进度、检查和确认报告中数据的准确性，整理耗时长。

Scene: 项目周报。

Current method/difficulty: 人工处理。

Materials: Excel, PPT.

Expected output: 自动整合周报。

### Case 8 — three issues in one response, with detailed manual-production scenario

Role: implementation consultant.

Problem 1:

> 项目蓝图阶段，需要快速将几十页会议纪要和访谈记录，按“现状-问题-需求”结构整理成需求调研报告，人工梳理耗时且容易遗漏。

Problem 2:

> 上线前数据迁移时，需要校验新旧系统大量数据的一致性，写SQL对比脚本和Excel比对公式费时费力，希望能快速生成校验规则。

Problem 3:

> 用户编写操作手册时，需要将系统功能截图配上文字说明，截图、标注、排版占用了大量时间，希望能简化制作流程。

Detailed scene/current difficulty focuses on Problem 3: multiple departments require separate ERP manuals, typically tens of manuals and 50–80 pages each; consultants manually capture screens, paste into Word/PPT, add arrows/boxes/numbers, write steps, then repeatedly replace screenshots and text when UI changes. Main pain points are screenshot/text version drift, heavy repetitive work, and fragmented departmental versions.

Materials: Word/PDF, Excel, PPT, meeting notes/transcripts, system screenshots, database/SQL.

Expected output for the detailed scenario: editable Word/Markdown operating-manual draft with annotated screenshots, generated step descriptions, role-based structure, and the ability to update changed sections with limited rework.

### Case 5 — Oracle EBS development AI working method/tool

Role: developer.

Problem:

> 找到一款更适合EBS开发的AI工具。

Scene: code development.

Current method/difficulty:

> 分步骤，分需求，让AI协助开发，我最终整合。

Materials: system screenshots, code/logs, database/SQL.

Expected output: 完整的可用的代码。

### Case 75 — non-ABAP consultant wants faster bug localization

Role: implementation consultant.

Relevant problem:

> 由于不是ABAP开发出身，每次程序遇到Bug，如果开发老师在忙其他模块的开发，不能及时debug定位bug原因，我都需要花费大量时间跟踪程序，希望AI能够快速定位程序报错原因（或者具体代码行）。

Scene: unit testing and post-go-live onsite support.

Current method/difficulty:

> 等开发顾问有时间处理，或者自己一点点跟踪程序，最大的困难是看不懂复杂程序的代码。

Materials: Word/PDF, code/logs.

Expected output: 定位程序BUG原因。

Note: the same respondent also listed meeting-minutes polishing and data cleanup as separate problems. The run must not silently bind those problems to the bug-localization scenario.

### Case 38 — AI-assisted system diagnosis/performance/automatic remediation

Role: implementation consultant.

Problems:

> 如何使用AI 嵌入到系统环境排查问题？
>
> 如何使用AI 进行大数据性能优化？
>
> 如何让AI 自动排查系统异常并解决？

Scene: operations/maintenance.

Current method/difficulty:

> 异常数据，需要按照ETL 代码逻辑，带入异常数据进行排查原因，比较耗时。

Materials: Word/PDF, Excel, PPT, meeting notes/transcripts, system screenshots, code/logs, database/SQL.

Expected output: 方案初稿、问题分析、代码BUG排查及解决方法、汇报PPT。

## 5. Output required from each pass

Do not make the response artificially long. Capture:

1. **Task framing** — what task(s) the response actually sees;
2. **Decision** — existing AI enough / specialized capability worth considering / low-cost trial first / materially unresolved due to named missing facts;
3. **Decision-changing reasons** — maximum 4;
4. **Recommended workflow** — `input → operation → output → review`;
5. **Specialized resource** — none, or at most 1 primary option by default;
6. **Critical unknowns/conditions** — only facts that would change the recommendation;
7. **Immediate next action**.

Do not include a self-evaluation of whether the Skill is good.

## 6. Independent evaluator — run only after all paired answers are frozen

Use a fresh evaluator context. It may read:

- all 10 frozen answers;
- current `SKILL.md` and two active references;
- this section of the regression plan.

It must not rewrite the answers.

For each case compare Baseline vs Curator on:

### A. Task decomposition

- Did it separate multiple distinct tasks/deliverables instead of merging them?
- Did it bind detailed scenario text to the correct problem?

### B. Adoption discrimination

- Did it distinguish “general AI is enough” from “specialized access/format/system capability is materially useful”?
- Did it confuse missing information with `C`?
- Did it over-recommend tools?
- Did it under-recommend tools even when a concrete capability gap was visible?

### C. Incremental value over ordinary Agent

Identify a **specific decision improvement**, not better prose:

- avoided an unnecessary adoption;
- discovered a material specialized capability;
- identified a decisive constraint/unknown;
- produced a more useful conditional branch;
- reduced search/setup/rework risk.

If there is no meaningful difference, say so.

### D. Enterprise safety proportionality

- Did it surface data/permission/write boundaries when material?
- Did safety warnings dominate a low-risk case unnecessarily?
- For diagnosis/understanding, did it preserve read-only/least-privilege reasoning where relevant?

### E. Actionability

- Is the next step concrete enough to execute?
- Did the Curator turn “need more information” into an endless intake checklist?

## 7. Cross-case decision

The evaluator must answer:

1. Where did 0.6.1 clearly outperform Baseline in adoption judgement?
2. Where did it add little/no value?
3. Is there evidence of **over-tooling**?
4. Is there evidence of **under-tooling**?
5. Is `C` being misused as “information missing”?
6. Does multi-problem input create a recurring decomposition defect?
7. Is any observed defect already covered by current `SKILL.md`/references but simply ignored by the Agent?
8. Does a defect justify a **minimal Skill change**, or only better execution/eval instructions?

Do not recommend changing `SKILL.md` merely because wording could be improved.

A Skill change is justified only if a recurring error is plausibly caused by a missing/ambiguous permanent rule and survives across more than one case or creates a high-severity risk.

## 8. Evidence status / stop rule

This regression can produce:

- a bounded defect finding;
- a bounded regression result;
- a minimal Skill correction candidate.

It cannot produce:

- REAL_USER adoption evidence;
- proof of time savings;
- proof that the product is validated;
- a reason to resume broad internal validation-card accumulation.

After the paired regression and evaluator result are returned, Cloud/ChatGPT owns the adversarial review and decides whether `0.6.1` remains unchanged or receives one narrow patch.
