# ERP AI Curator — Current Session Handoff

Date: 2026-08-30
Status: **CURRENT / MINIMAL HANDOFF**

> 新会话不要从历史聊天或旧 validation 文档恢复状态。先读 `docs/PROJECT_MAP.md`。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

只有具体任务需要时再读 runtime Skill、Pilot、AI Leverage、Adversarial Review 或历史材料。

## 2. 当前产品

ERP AI Curator 是**真实 ERP / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心问题：

> **当前 AI / 工具链是否已经够用？如果不够，什么已经存在的实践、Tool / Skill / MCP / 方法 / 教程最值得在当前任务和约束下优先学习/采用？**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.0**
- stage: **Curation pilot — user-use value unvalidated**

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

## 4. 两条 Lane

### REAL_USER_ORIGIN CURATION

真实问题来源，由 Cloud 完成研究/推荐。当前：

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md`
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md`

这些**不是用户使用证据**。

### REAL_USER_USE VALIDATION

真实同事实际收到并自然学习/采用/修改/拒绝推荐。Authority：`docs/REAL_USER_PILOT_V1.md`。

只有这条 Lane 用于证明产品真实价值。

## 5. 当前近阶段

Authority：`docs/CURRENT_EXECUTION_PLAN_V3.md`。

完成 bounded Curation Pack 01：

1. Case 001/002 已完成；
2. Cloud 下一步直接做 Case 003：多顾问周报/PPT 汇总与数据准确性；
3. 再做 Case 004：程序 Bug / ERP 系统真实访问边界；
4. 然后停止批量 curation，做 Pack 01 adversarial review。

不要提前预设 A/B/C。

## 6. Owner execution rule

Cloud 能做就继续直接做。只有以下情况停：

- genuine Owner decision；
- Local Agent-only file/repo/runtime/ERP environment；
- external evidence barrier。

停时必须明确下一 actor、任务、返回结果和 Cloud 后续动作。

## 7. 绝对不要复活

除非当前 evidence 证明必要，不要重新启动：

- V0.4 Gate/scoring/taxonomy/validator 流程；
- synthetic benchmark loop；
- resource DB / auto refresh；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- user tool-test protocol；
- 已失效 P03/P07 Result 01；
- 历史 `PROJECT_WORKFLOW.md` 的旧 CURRENT/NEXT。
