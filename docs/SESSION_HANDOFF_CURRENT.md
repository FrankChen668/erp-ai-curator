# ERP AI Curator — Current Session Handoff

Date: 2026-08-30
Status: **CURRENT / CONTROLLED REAL-USER USE**

> 新会话不要从历史聊天或旧 validation 文档恢复状态。先读 `docs/PROJECT_MAP.md`。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

只有具体任务需要时再读 runtime Skill、Trial Guide、Real User Use Validation、AI Leverage、Adversarial Review 或历史材料。

## 2. 当前产品

ERP AI Curator 是**真实 ERP / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心问题：

> **当前 AI / 工具链是否已经够用？如果不够，什么已经存在的实践、Tool / Skill / MCP / 方法 / 教程最值得在当前任务和约束下优先学习/采用？**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.0**
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

关键 runtime 边界：

- 真实 baseline first；
- capability gap + adoption cost 决定 A/B/C；
- `信息不足 != C`；
- practitioner-first，但 author self-practice 不冒充独立验证；
- 默认“当前任务下优先推荐”，不滥用“最佳/唯一/已验证”；
- 0 资源合法，默认最多 1 个主资源；
- C 不自动让用户测试工具；
- runtime/local test 只在 decision-changing 时做；
- Curator != execution coach / test coordinator。

## 4. Curation Pack 01 — CLOSED

Authority：`docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`。

- Case 001 — ERP 操作手册：B；
- Case 002 — Oracle EBS AI 开发：B；
- Case 003 — 周报/PPT 汇总：A；
- Case 004 — SAP Bug / system evidence access：A → conditional B。

结论：

> **STOP INTERNAL PACK EXPANSION. MOVE TO CONTROLLED REAL-USER USE.**

这四条都是 REAL_USER_ORIGIN，不是用户采用证据。

## 5. 当前发布裁决

Authority：`docs/validation/RELEASE_READINESS_ADVERSARIAL_20260830.md`。

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

不要再把“能投用户试用”写成“产品目标已经验证完成”。

## 6. 两个目标层级

### 已完成

- 方法/Skill/Harness 的 pre-user 构建；
- 0.7.0 的受控试用准备；
- A/B/system-access 基本区分度；
- 用户试用入口。

### 未完成

North Star 用户结果：

- 是否比普通 AI/自搜索省判断成本；
- 是否少选错工具；
- 是否降低配置/返工；
- 是否更可信；
- 用户是否愿意再次使用。

这些只能由 REAL_USER_USE 证明。

## 7. 当前下一步

> **把 0.7.0 给少量真实 ERP/企业信息化用户自然使用。**

用户不需要执行项目测试协议，也不要求长问卷。

只记录自然出现的：采用/修改/拒绝/忽略 + 原因 + 漏项/收益。

如果真实反馈暴露明确缺陷，Cloud 继续做窄修正；否则不继续内部润色 Skill。

## 8. Cloud / Local / Owner

Cloud 能做就继续直接做，包括：真实反馈证据审查、当前 Web/GitHub 核验、窄缺陷修正、GitHub authority 维护。

Local Agent 只在真实决策依赖本地 repo/runtime/ERP 环境/受保护 evidence 时接力。

Owner 当前只有一个潜在明确裁决项：**如果要声明 public/open-source release complete，需要选择 repository license。** Agent 不擅自选择许可证。

## 9. 绝对不要复活

除非真实 evidence 证明必要，不要重新启动：

- V0.4 Gate/scoring/taxonomy/validator；
- synthetic benchmark loop；
- 更多 pre-user Curation Card；
- resource DB / auto refresh；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- user tool-test protocol；
- 已失效 P03/P07 Result 01；
- 历史 `PROJECT_WORKFLOW.md` 的旧 CURRENT/NEXT。
