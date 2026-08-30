# ERP AI Curator — Project Map

Date: 2026-08-30
Status: **CURRENT NAVIGATION AUTHORITY**

> 给人和 Agent 的“地图”，不是第二本说明书。遇到冲突时，先按下面的层级判断，不从历史文档反推当前状态。

## 1. 当前权威层级

1. [Project North Star](PROJECT_NORTH_STAR.md) — 产品为什么存在、最终用户结果是什么。
2. [Owner Execution Rules](OWNER_EXECUTION_RULES.md) — 云端持续推进、本地 Agent/Owner 何时接力。
3. [Current Execution Plan](CURRENT_EXECUTION_PLAN_V3.md) — 当前阶段、近阶段目标与下一步。
4. [Evidence Status](validation/EVIDENCE_STATUS.md) — 哪些结论有证据、哪些仍未验证。
5. [Current Skill](../skills/curating-erp-ai-resources/SKILL.md) — 可分发运行时工作流。

若这五者冲突：`North Star > Owner Rules > Current Plan > Evidence Status > runtime Skill implementation detail`。发现冲突应修仓库，不允许 Agent 自行挑一个顺眼的版本继续。

## 2. 当前阶段辅助文档

- [Controlled User Trial Guide](USER_TRIAL_GUIDE_V1.md) — **真实试用用户/管理员入口**。
- [0.8.2 Candidate Selection Patch](validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md) — 当前最新 runtime 窄修正；处理 audience/ecosystem fit、artifact fit 和 incidental install。
- [0.8.1 Practitioner Execution Patch](validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md) — query intent / practitioner candidate investigation 修正。
- [0.8.0 Runtime Simplification](validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md) — runtime 简化裁决与回归。
- [Release Readiness — Adversarial](validation/RELEASE_READINESS_ADVERSARIAL_20260830.md) — controlled trial 的原始发布裁决。
- [Curation Pack 01 Adversarial Review](validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md) — 四个真实来源 Case 的历史收口复审。
- [Real User Use Validation](REAL_USER_PILOT_V1.md) — **真实用户使用/反馈**如何成为产品价值证据。
- [Project-wide Calibration](PROJECT_CALIBRATION_20260830.md) — 全面盘点、对抗性修正与 Harness 整改记录。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接。
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — 历史/分析层模型；不作为 0.8.2 runtime contract。
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险库；不是 runtime checklist。
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — practitioner/creator discovery 的辅助策略。

## 3. 两个“完成”不能混淆

### Build / readiness milestone — complete for controlled trial

- Skill **0.8.2** 保持 simplified runtime，只加入真实使用证据支持的窄修正；
- Curation Pack 01 已提供历史异构任务证据；
- 用户试用入口已具备；
- 可以继续真实用户使用，不再通过扩规则证明产品成熟。

### North Star outcome milestone — not validated

North Star 要解决的是用户结果：更快判断 AI 做法、少选错工具、少浪费搜索/配置/返工成本。

这些需要 `REAL_USER_USE` 证据。目前不能因为 Skill/Harness/Case ready 就宣布产品目标完成。

## 4. 真实问题 Curator 输出与产品验证必须分开

### Lane A — REAL_USER_ORIGIN CURATION

来源是真实同事/问卷/Owner 的真实问题，但由 Curator 完成搜索、筛选和推荐。

Pack 01 历史 Case 保留为分析证据，不要求 0.8.2 runtime 复现旧 A/B/C 标签。

### Lane B — REAL_USER_USE VALIDATION

真实同事实际收到推荐后，自然学习、采用、修改、忽略或拒绝，并给出具体反馈。

这才属于产品价值验证，依据 [Real User Use Validation](REAL_USER_PILOT_V1.md) 记录。不要为了获得 Lane B 证据，把用户变成“替项目跑测试的人”。

## 5. 当前发布层级

### GO — controlled user trial

可以把 0.8.2 给少量真实 ERP/ToB/企业信息化用户，在已知/批准的 Agent Skills 宿主里自然使用。

### HOLD — organization-wide standard

在重复 REAL_USER_USE 证据和宿主兼容性出现前，不把它定义为部门统一标准。

### HOLD — public/open-source release claim

仓库当前没有 `LICENSE` 文件。公开/开源发布前，Owner 需要明确许可方式；不要由 Agent 擅自选择。

## 6. 历史/条件性设计 — 不作为当前执行入口

以下文档保留用于理解演化或未来条件触发，不得覆盖当前权威：

- `PROJECT_WORKFLOW.md` — SUPERSEDED 历史阶段协议 tombstone；
- `SKILL_BLUEPRINT_V3.md` — SUPERSEDED Skill 设计记录；
- `AI_LEVERAGE_MODEL_V3.md` — 分析/历史判断模型；
- `SOURCE_ADAPTER_ARCHITECTURE_V3.md` / `SOURCE_ADAPTER_LIFECYCLE_V3.md` — 条件性来源获取设计，只有重复出现 material acquisition gap 且会改变推荐时才重新激活；
- `phase-01-skill-research/` — 优秀 Skill 研究证据与设计来源；
- `validation/` 中已关闭/失效材料 — 仅按 `EVIDENCE_STATUS.md` 指定 authority 使用；
- `archive/` — 历史 runtime / resource-library 资产；
- `tests/fixtures/v0.4-regression/` — 历史回归材料。

## 7. Skill / Harness 设计原则

- Agent Skills progressive disclosure；
- OpenAI Skill Creator：默认模型足够聪明，只添加真正需要的程序性知识；
- Anthropic Skill Creator：description 负责触发，保持通用，用真实 prompt 观察行为；
- Harness Engineering：给 Agent 地图，不给越来越长的补丁说明；确定性事实才机械约束。

## 8. 新会话读取顺序

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有具体任务需要时再读 Skill、Trial Guide、Real User Use Validation 或历史材料。
