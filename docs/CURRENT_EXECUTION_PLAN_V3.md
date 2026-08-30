# ERP AI Curator — Current Execution Plan

Date: 2026-08-30
Status: **CURRENT — CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / 企业信息化工作任务，判断当前 AI / 工具链是否已经够用；如果不够，从互联网上已经存在的实践、Tool / Skill / MCP / 方法 / 教程中筛出少量真正值得优先学习和采用的方案。**

Main chain:

```text
real task + current baseline + hard constraints
→ AI leverage / capability-gap judgement
→ practitioner evidence when needed
→ original implementation verification
→ decision-changing official facts
→ compact adoption recommendation
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. 当前方法结论

历史异构任务、边界回归与 Curation Pack 01 已足以支持一个稳定的 pre-user 方法骨架：

1. 从真实任务、材料、当前 baseline、交付物和硬约束开始；
2. A/B/C 由 capability gap + adoption cost 决定；
3. external adoption question 优先 practitioner experience，再核验 implementation/current facts；
4. source-grounded analysis 优先于模型记忆；
5. runtime/local test 只在 decision-changing 时出现；
6. 0 个资源合法；强匹配优先于覆盖率；
7. 结论稳定即停止。

没有证据支持重建 Gate、评分、taxonomy、资源数据库或多 Agent pipeline。

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.0**
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

0.7.0 在真实 baseline、A/B/C、证据角色、C 边界、权限/系统访问和 Curator/执行教练边界上已完成预用户校准。

**默认不再继续预用户修改 Skill。**

只有真实用户暴露明确缺陷或宿主兼容 blocker，才触发下一版。

## 4. Curation Pack 01 — closed

Authority: `docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Pack：

- Case 001 — ERP 操作手册：B；
- Case 002 — Oracle EBS AI 开发：B；
- Case 003 — 多顾问周报/PPT 汇总：A；
- Case 004 — SAP Bug 诊断/系统 evidence access：A → conditional B。

结论：

> **STOP INTERNAL PACK EXPANSION. MOVE TO CONTROLLED REAL-USER USE.**

这些仍是 REAL_USER_ORIGIN，不是用户采用证据。

## 5. 当前里程碑 — Controlled REAL_USER_USE

受控试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

Release verdict：`docs/validation/RELEASE_READINESS_ADVERSARIAL_20260830.md`。

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

North Star 成功标准是用户结果，不是 Skill/Harness 完成度。

当前最大问题：

> **Curator 是否能持续给出比普通 AI/用户自己搜索更高信任、更低噪声的采用判断，并且这个差异足以让真实用户再次使用？**

需要 REAL_USER_USE 回答：

- 是否减少搜索/选型成本；
- 是否减少错装/错选工具；
- 是否漏掉企业环境/版本/权限；
- 是否降低后续返工；
- 用户是否愿意再次使用。

## 7. Cloud / Local Agent 边界

Cloud owns：

- 对自然真实反馈做证据审查；
- 必要的当前 Web/GitHub 核验；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 只在真实决策依赖以下内容时接力：

- 本地项目文件/repo/runtime；
- 企业 ERP 环境；
- 当前系统元数据/日志/权限；
- Cloud 无法获得且会改变结论的受保护 evidence。

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
- source-adapter framework activation；
- card-specific permanent rules；
- user test protocol as Curator default output。

## 10. 下一步

> **把 0.7.0 投给少量真实用户自然使用。**

如果没有真实反馈，Cloud 不用内部 busywork 替代它。

如果出现真实反馈，Cloud 立即：

`classify evidence → identify recurring/narrow defect → fix only if needed → update Evidence Status`。
