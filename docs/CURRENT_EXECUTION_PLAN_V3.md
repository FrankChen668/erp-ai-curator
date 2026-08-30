# ERP AI Curator — Current Execution Plan

Date: 2026-08-30
Status: **CURRENT — CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / 企业信息化工作任务，判断当前 AI / 工具链是否已经够用；如果不够，或用户明确要找现成实践资源，从互联网上已经存在的实践、Tool / Skill / MCP / 方法 / 教程中筛出少量真正值得优先学习和采用的方案。**

Main chain:

```text
real task + current baseline + hard constraints
→ distinguish adoption decision vs explicit practice-resource intent
→ AI leverage / capability-gap judgement
→ practitioner discovery when requested/decision-changing
→ original implementation verification
→ decision-changing official facts
→ compact adoption/resource recommendation
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. 当前方法结论

历史异构任务、边界回归与 Curation Pack 01 已足以支持稳定的 pre-user 方法骨架：

1. 从真实任务、材料、当前 baseline、交付物和硬约束开始；
2. A/B/C 由 capability gap + adoption cost 决定；
3. **是否新增工具**和**是否明确要求找最佳实践/教程**是两个不同 intent；
4. 用户明确找实践/教程时，即使 A，也要完成 practitioner curation；
5. external practice/adoption question 优先 practitioner experience，再核验 implementation/current facts；
6. source-grounded analysis 优先于模型记忆；
7. runtime/local test 只在 decision-changing 时出现；
8. 强匹配优先于覆盖率，结论稳定即停止。

没有证据支持重建 Gate、评分、taxonomy、资源数据库或多 Agent pipeline。

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.1**
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

### 0.7.1 — real controlled-trial defect correction

真实用户用 0.7.0 请求“给我找做流程图的最佳实践”，结果：

- 很快判 A；
- 主要引用 OMG / Camunda / Microsoft / ASQ 等官方/规范；
- 自己写了通用流程图教程和 Prompt；
- 没有真正筛出 Bilibili/公众号/小红书/产品经理/ToB practitioner 实战资源。

公开 Web 随后能直接发现多个高度相关、互动量明显的 Bilibili 实操资源，因此这不是“互联网缺资源”，而是 runtime discovery 没有执行到位。

根因：0.7.0 中 `A — 外部资源默认 0` 容易被误执行为“判 A 后无需继续实践资源发现”。

0.7.1 修正：

> **A/B/C 只决定是否新增专门能力；用户明确请求最佳实践/教程时，practitioner discovery 是任务本身。**

新增按需 reference：

- `skills/curating-erp-ai-resources/references/practitioner-discovery.md`

它规定中文泛 ERP / ToB / 产品经理/顾问语境的 practitioner discovery、互动信号、候选准入、平台 coverage 与 link-first 输出顺序。

## 4. Curation Pack 01 — closed

Authority: `docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Pack：

- Case 001 — ERP 操作手册：B；
- Case 002 — Oracle EBS AI 开发：B；
- Case 003 — 多顾问周报/PPT 汇总：A；
- Case 004 — SAP Bug 诊断/系统 evidence access：A → conditional B。

结论仍是：

> **STOP INTERNAL PACK EXPANSION. MOVE TO CONTROLLED REAL-USER USE.**

0.7.1 不重新打开 pre-user case accumulation；它由真实受控试用缺陷触发。

## 5. 当前里程碑 — Controlled REAL_USER_USE

受控试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

允许：

- 少量真实 ERP/企业信息化用户；
- 用户用自己的自然问题；
- 已知/批准的 Agent Skills 宿主；
- 自然接受、修改、拒绝或忽略建议；
- 记录真正会改变产品判断的反馈。

不要求：

- 固定 benchmark；
- 用户跑工具测试协议；
- 长问卷或评分；
- 为了覆盖类别继续制造 Case。

## 6. 当前最重要的未验证目标

North Star 成功标准仍是用户结果，不是 Skill/Harness 完成度。

当前最大问题：

> **Curator 是否能持续给出比普通 AI/用户自己搜索更高信任、更低噪声、更值得点击的采用/学习建议，并且这个差异足以让真实用户再次使用？**

需要 REAL_USER_USE 回答：

- 是否真正发现用户自己不容易筛到的高价值实践；
- 是否减少搜索/选型成本；
- 是否减少错装/错选工具；
- 是否漏掉企业环境/版本/权限；
- 是否降低后续返工；
- 用户是否愿意再次使用。

## 7. Cloud / Local Agent 边界

Cloud owns：

- 对自然真实反馈做证据审查；
- 当前 Web/GitHub practitioner discovery 与事实核验；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 只在真实决策依赖以下内容时接力：

- 本地项目文件/repo/runtime；
- 企业 ERP 环境；
- 当前系统元数据/日志/权限；
- Cloud 无法获得且会改变结论的受保护 evidence；
- 需要在某个具体宿主中验证 Skill/reference 路由是否真正执行。

Agent 可用性本身不是派活理由。

## 8. Release boundary

### GO

- controlled user trial。

### HOLD

- organization-wide mandatory standard；
- “产品价值已验证”声明；
- 全宿主兼容声明；
- public/open-source release completion。

公开/open-source 发布还需要 Owner 明确 repository license；Agent 不擅自选择。

## 9. Anti-drift

真实用户未暴露必要性前，不新增：

- synthetic validation loop；
- fixed scenario taxonomy；
- scoring/Gate；
- resource database/refresh；
- mandatory runtime benchmark；
- multi-Agent orchestration；
- creator ranking；
- source-adapter framework as default architecture；
- card-specific permanent rules；
- user test protocol as Curator default output。

0.7.1 practitioner discovery 是**真实缺陷修复**，不是 creator database 或平台配额。

## 10. 下一步

1. 完成 0.7.1 窄修正并通过 Project Contract；
2. 用同一个真实失败 Prompt 做一次 bounded regression，验收 practitioner-link discovery / prioritization / official-role；
3. 原宿主真实重跑结果若随后返回，用作 cross-host/runtime evidence；
4. 继续 controlled REAL_USER_USE，不恢复内部 case 扩张。
