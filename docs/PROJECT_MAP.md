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
- [Release Readiness — Adversarial](validation/RELEASE_READINESS_ADVERSARIAL_20260830.md) — controlled trial 的原始发布裁决。
- [Curation Pack 01 Adversarial Review](validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md) — 四个真实来源 Case 的历史收口复审。
- [Real User Use Validation](REAL_USER_PILOT_V1.md) — 真实用户使用/反馈如何成为产品价值证据。
- [Project-wide Calibration](PROJECT_CALIBRATION_20260830.md) — 项目全面盘点与 Harness 整改记录。
- [0.8.0 Runtime Simplification](validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md) — 当前 runtime 简化裁决与回归。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接。
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — **历史/分析层的详细判断模型；不再作为 0.8.0 runtime contract 或每次运行必读材料。**
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险库；按需用于项目设计复审，不是 runtime checklist。
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — practitioner/creator discovery 的辅助研究记录；runtime 使用更小的 `practitioner-discovery.md`。

## 3. 两个“完成”不能混淆

### Build / readiness milestone — complete for controlled trial

- Skill **0.8.0** 已完成 runtime simplification；
- Curation Pack 01 已提供历史异构任务证据；
- 用户试用入口已具备；
- 可以继续真实用户使用，不再通过扩规则证明产品成熟。

### North Star outcome milestone — not validated

尚未证明 Curator 比普通 AI / 自搜索稳定更省判断成本、更少错选、更能找到值得学的 practitioner 实践。

这些只能由 `REAL_USER_USE` 证据验证。

## 4. 真实问题 Curator 输出与产品验证分开

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 完成搜索、筛选和推荐。

Pack 01 历史 Case：

- [Case 001 — ERP 操作手册](curation-cases/CASE_001_ERP_OPERATING_MANUAL.md)
- [Case 002 — Oracle EBS AI 开发](curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md)
- [Case 003 — 多顾问周报汇总](curation-cases/CASE_003_WEEKLY_REPORT_CONSOLIDATION.md)
- [Case 004 — SAP Bug 诊断/系统访问](curation-cases/CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md)

旧 A/B 标签保留为当时分析结果，不再定义 0.8.0 runtime。

### Lane B — REAL_USER_USE VALIDATION

真实用户实际收到推荐后，自然学习、采用、修改、忽略或拒绝，并给出具体反馈。

不要为了获得 Lane B 证据，把用户变成替项目跑测试的人。

## 5. 当前发布层级

### GO — controlled user trial

可以把 0.8.0 给少量真实 ERP/ToB/企业信息化用户，在已知/批准的 Agent Skills 宿主里自然使用。

### HOLD — organization-wide standard

在重复 REAL_USER_USE 证据和宿主兼容性出现前，不定义为部门统一标准。

### HOLD — public/open-source release claim

仓库当前没有 `LICENSE`。公开/开源发布前，Owner 需要明确许可方式。

## 6. 历史/条件性设计 — 不作为当前执行入口

以下文档保留用于理解演化或未来条件触发，不得覆盖当前权威：

- `PROJECT_WORKFLOW.md` — SUPERSEDED 历史阶段协议；
- `SKILL_BLUEPRINT_V3.md` — SUPERSEDED Skill 设计记录；
- `AI_LEVERAGE_MODEL_V3.md` — 分析/历史判断模型，不要求 runtime 执行分类；
- `SOURCE_ADAPTER_ARCHITECTURE_V3.md` / `SOURCE_ADAPTER_LIFECYCLE_V3.md` — 条件性来源获取设计；
- `phase-01-skill-research/` — 优秀 Skill 研究证据；
- `validation/` 中已关闭/失效的协议、回归与结果 — 仅按 `EVIDENCE_STATUS.md` 指定 authority 使用；
- `archive/` — 历史 runtime / resource-library 资产；
- `tests/fixtures/v0.4-regression/` — 旧 fixture，只作历史材料。

历史文件中的 `CURRENT`、`NEXT`、`PASS` 与本 Map 或 Current Plan 冲突时，一律视为历史语境。

## 7. Skill / Harness 设计原则

当前采用：

- Agent Skills progressive disclosure：主 Skill 只放核心工作流，详细材料按需加载；
- OpenAI Skill Creator：默认模型已经很聪明，只添加模型真正需要的上下文；高自由度判断任务少加硬约束；
- Anthropic Skill Creator：description 负责触发，流程保持通用，用真实 prompt 观察行为；
- Harness Engineering：给 Agent 地图，不给越来越长的补丁说明；确定性事实才机械约束。

外部来源：

- https://agentskills.io/specification
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://openai.com/index/harness-engineering/

内部研究：

- `docs/phase-01-skill-research/SKILL_PATTERN_STUDY.md`
- `docs/phase-01-skill-research/DESIGN_SYNTHESIS.md`

## 8. 新会话读取顺序

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有具体任务需要时再读 Skill、Trial Guide、Real User Use Validation 或历史分析材料。
