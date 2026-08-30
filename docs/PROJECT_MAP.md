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

- [Controlled User Trial Guide](USER_TRIAL_GUIDE_V1.md) — 真实试用用户/管理员入口。
- [0.8.1 Practitioner Execution Patch](validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md) — **当前最新 runtime 纠偏；依据 Codex Desktop 实际执行日志。**
- [0.8.0 Runtime Simplification](validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md) — runtime 简化裁决与回归。
- [Release Readiness — Adversarial](validation/RELEASE_READINESS_ADVERSARIAL_20260830.md) — controlled trial 的原始发布裁决。
- [Curation Pack 01 Adversarial Review](validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md) — 四个真实来源 Case 的历史收口复审。
- [Real User Use Validation](REAL_USER_PILOT_V1.md) — 真实用户使用/反馈如何成为产品价值证据。
- [Project-wide Calibration](PROJECT_CALIBRATION_20260830.md) — 项目全面盘点与 Harness 整改记录。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接。
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — 历史/分析层判断模型；不作为 0.8.1 runtime contract。
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险库；不是 runtime checklist。
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — practitioner/creator discovery 的辅助研究记录。

## 3. 当前 Skill / milestone

- Skill：**0.8.1**
- Release：**CONTROLLED USER TRIAL GO / BROAD RELEASE NO**
- Product value：**UNVALIDATED**

0.8.0 完成“去框架化”；0.8.1 只修两条由真实日志证明的执行缺陷：

- AI-enabled-workflow 查询语境不能在搜索时丢失；
- 明确找最佳实践/教程时必须真正调查 practitioner 候选，或明确宿主 coverage/policy gap。

尚未证明 Curator 比普通 AI / 自搜索稳定更省判断成本、更少错选、更能找到值得学的 practitioner 实践。

## 4. 两条证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 完成搜索、筛选和推荐。它不能证明用户已经采用或获得价值。

### Lane B — REAL_USER_USE VALIDATION

真实用户实际收到推荐后自然学习、采用、修改、忽略或拒绝，并给出具体反馈。不要为了获得 Lane B 证据，把用户变成替项目跑测试的人。

## 5. 历史/条件性设计 — 不作为当前执行入口

- `PROJECT_WORKFLOW.md` — SUPERSEDED；
- `SKILL_BLUEPRINT_V3.md` — SUPERSEDED；
- `AI_LEVERAGE_MODEL_V3.md` — 分析/历史模型；
- `SOURCE_ADAPTER_ARCHITECTURE_V3.md` / `SOURCE_ADAPTER_LIFECYCLE_V3.md` — 条件性设计；
- `phase-01-skill-research/` — 优秀 Skill 研究证据；
- `archive/` 与旧 validation/fixture — 历史材料。

## 6. Skill / Harness 设计原则

- Agent Skills progressive disclosure；
- OpenAI Skill Creator：默认模型足够聪明，只添加真正需要的程序性知识；
- Anthropic Skill Creator：description 负责触发，保持通用，用真实 prompt 观察行为；
- Harness Engineering：给 Agent 地图，不给越来越长的补丁说明；确定性事实才机械约束。

## 7. 新会话读取顺序

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有具体任务需要时再读 Skill、Trial Guide、Real User Use Validation 或历史分析材料。
