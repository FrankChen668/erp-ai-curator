# ERP AI Curator — Project Map

Date: 2026-08-31
Status: **CURRENT NAVIGATION AUTHORITY**

> 这是人和 Agent 的项目地图，不是第二本说明书。历史文件中的 `CURRENT`、`NEXT`、`PASS` 不能反推今天的项目状态。

## 1. 当前权威层级

1. [Project North Star](PROJECT_NORTH_STAR.md) — 产品为什么存在、最终用户结果、Runtime 职责。
2. [Owner Execution Rules](OWNER_EXECUTION_RULES.md) — Cloud / Local Agent / Owner 接力边界。
3. [Current Execution Plan](CURRENT_EXECUTION_PLAN_V3.md) — 当前阶段、冻结边界与下一步。
4. [Evidence Status](validation/EVIDENCE_STATUS.md) — 哪些结论有证据、哪些仍未验证。
5. Runtime Skills：
   - [Practice Curator](../skills/curating-erp-ai-resources/SKILL.md)
   - [Capability Advisor](../skills/advising-erp-ai-capabilities/SKILL.md)

若冲突：`North Star > Owner Rules > Current Plan > Evidence Status > Runtime Skill implementation detail`。发现冲突应修仓库，不允许 Agent 自行挑一个版本继续。

## 2. 当前状态

### Runtime

当前版本：**0.9.2 / FROZEN**。

- Practice Curator：fresh external discovery、historical evidence lead-only、final resource fresh inspection、candidate-pool concentration recall correction、task/artifact fit anti-dilution、无默认 Tool/Skill/MCP adoption。
- Capability Advisor：current baseline → concrete gap → minimum useful upgrade or explicit no-upgrade。

### Release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

产品价值仍 **UNVALIDATED**。

### 当前真正里程碑

[Real User Use Validation](REAL_USER_PILOT_V1.md) 是产品价值 authority。

尚未证明：Curator 比普通 AI / 用户自搜索更稳定地减少搜索、筛选和选型成本，并且这个差异足以让真实 ERP/ToB 用户继续使用。

## 3. Source acquisition：上一阶段已关闭，架构问题部分未决

P0–P4 source-acquisition investigation 已关闭。当前不再执行旧的 `P0 → P1 → P2 → P3` 平台 qualification 阶段。

保留的事实：

- broad Web 对部分中文 practitioner 生态存在真实 recall/acquisition 缺口；
- targeted normal Web 是最低成本 fallback；
- WeChat provider `PILOT / UNSTABLE`；
- Bilibili provider `CONDITIONAL`；
- 当前 Xiaohongshu provider `REMOVED`，不等于平台无价值；
- per-platform provider engineering 的成本已被证明可能偏离产品价值。

当前架构原则：

> **REUSE BEFORE BUILD**

Authority：

- [Reuse-Before-Build Source Composition](validation/REUSE_BEFORE_BUILD_SOURCE_COMPOSITION_20260831.md)
- [Source Composition Uncertainty](validation/SOURCE_COMPOSITION_UNCERTAINTY_20260831.md)

P5 未完成 `discovery → original-page reading → Curator judgement` 全链路，因此：

> **MATURE-SKILL COMPOSITION EFFECTIVENESS — INCONCLUSIVE / OPEN**

不允许从 P5 推导“已解决”或“已失败”。进一步证据只在真实 ERP/ToB 任务出现 decision-changing source gap 时收集。

## 4. 当前用户与试用入口

- [Controlled User Trial Guide](USER_TRIAL_GUIDE_V1.md) — 用户/管理员试用入口。
- [Real User Use Validation](REAL_USER_PILOT_V1.md) — 真实使用后的产品价值证据。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接。

## 5. 两条证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 完成搜索、筛选和推荐。

当前 controlled-trial case：

- [Case 005 — Workshop / 会议材料 → 可评审需求包](curation-cases/CASE_005_WORKSHOP_TO_REQUIREMENT_PACKAGE.md)

历史 Pack 01：

- [Case 001 — ERP 操作手册](curation-cases/CASE_001_ERP_OPERATING_MANUAL.md)
- [Case 002 — Oracle EBS AI 开发](curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md)
- [Case 003 — 多顾问周报汇总](curation-cases/CASE_003_WEEKLY_REPORT_CONSOLIDATION.md)
- [Case 004 — SAP Bug 诊断/系统访问](curation-cases/CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md)

这些是 Lane A / 历史项目 evidence，不定义未来用户的候选池或当前资源排序，也不证明用户采用。

### Lane B — REAL_USER_USE VALIDATION

真实用户实际收到推荐后，自然学习、采用、修改、忽略或拒绝，并给出具体反馈。

不要为了获得 Lane B 证据，把用户变成替项目跑测试的人。

## 6. 当前 Runtime 设计依据

- [0.9.2 Ecosystem Recall / Task-Fit Correction](validation/CURATOR_092_ECOSYSTEM_RECALL_TASK_FIT.md)
- [0.9.1 Fresh Curation / Evidence Isolation](validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md)
- [0.9.0 Runtime Responsibility Split](validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md)
- [0.8.2 Candidate Selection Patch](validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md)
- [0.8.1 Practitioner Execution Patch](validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md)
- [0.8.0 Runtime Simplification](validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md)

这些文件解释当前 Runtime 为什么长成这样，但不替代 Current Plan / Evidence Status。

## 7. 历史 / 已降权设计

以下材料保留为历史或分析证据，不是当前执行 contract：

- `PROJECT_WORKFLOW.md` — SUPERSEDED；
- `SKILL_BLUEPRINT_V3.md` — SUPERSEDED；
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — 分析/历史模型；
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险库；
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — discovery 辅助策略；
- [Project-wide Calibration](PROJECT_CALIBRATION_20260830.md) — 整改记录；
- [Release Readiness — Adversarial](validation/RELEASE_READINESS_ADVERSARIAL_20260830.md) — 历史发布裁决记录；
- [Source Acquisition Pilot](validation/SOURCE_ACQUISITION_PILOT_20260831.md) — **P0–P4 已关闭的阶段设计/证据入口**；
- [Source Adapter Architecture V3](SOURCE_ADAPTER_ARCHITECTURE_V3.md) — **旧 per-platform pilot architecture，已被 reuse-before-build 方向降权**；
- [Source Adapter Lifecycle V3](SOURCE_ADAPTER_LIFECYCLE_V3.md) — **旧 adapter lifecycle 设计，不是当前 Runtime/maintenance contract**。

不要因为旧文件标题里写着 `CURRENT` / `pilot architecture` 就提升其 authority。

## 8. Skill / Harness 原则

- Agent Skills progressive disclosure；
- `name + description` 是主要触发层；
- current external curation 与 historical project evidence 分离；
- source acquisition failure 与 source quality judgement 分离；
- 判断型规则放 instructions，确定性事实才机械检查；
- Harness 给 Agent **map, not a huge manual**；
- 新规则、字段、脚本、adapter、framework 进入主线前先问：删除它以后，用户结果会不会明显变差？不能证明就不加。

## 9. 新会话读取顺序

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有具体任务需要时再读 Runtime Skill、Trial Guide、Real User Use Validation、source-composition authority 或历史材料。
