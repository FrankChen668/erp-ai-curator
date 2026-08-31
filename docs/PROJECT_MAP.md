# ERP AI Curator — Project Map

Date: 2026-08-31
Status: **CURRENT NAVIGATION AUTHORITY**

> 给人和 Agent 的“地图”，不是第二本说明书。遇到冲突时先按下面层级判断，不从历史文档反推当前状态，更不能用历史 curation 直接替代当前用户的 fresh discovery。

## 1. 当前权威层级

1. [Project North Star](PROJECT_NORTH_STAR.md) — 产品为什么存在、最终用户结果和两类 Runtime 职责。
2. [Owner Execution Rules](OWNER_EXECUTION_RULES.md) — Cloud / Local Agent / Owner 接力边界。
3. [Current Execution Plan](CURRENT_EXECUTION_PLAN_V3.md) — 当前阶段与下一步。
4. [Evidence Status](validation/EVIDENCE_STATUS.md) — 哪些结论有证据、哪些仍未验证。
5. Runtime Skills：
   - [Practice Curator](../skills/curating-erp-ai-resources/SKILL.md)
   - [Capability Advisor](../skills/advising-erp-ai-capabilities/SKILL.md)

若冲突：`North Star > Owner Rules > Current Plan > Evidence Status > Runtime Skill implementation detail`。发现冲突应修仓库，不允许 Agent 自行挑一个版本继续。

## 2. 当前阶段辅助文档

- [Controlled User Trial Guide](USER_TRIAL_GUIDE_V1.md) — **真实试用用户/管理员入口**。
- [0.9.1 Fresh Curation / Evidence Isolation](validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md) — **当前最新 Runtime 窄修正；处理 historical-evidence contamination、freshness 和 broad-search recall bias。**
- [0.9.0 Runtime Responsibility Split](validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md) — 一个产品、两个单职责 Skill 的架构裁决。
- [0.8.2 Candidate Selection Patch](validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md) — audience/artifact fit 与 incidental install 历史修正。
- [0.8.1 Practitioner Execution Patch](validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md) — query intent / practitioner candidate investigation 历史修正。
- [0.8.0 Runtime Simplification](validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md) — Runtime 简化裁决与回归。
- [Release Readiness — Adversarial](validation/RELEASE_READINESS_ADVERSARIAL_20260830.md) — controlled trial 原始发布裁决。
- [Curation Pack 01 Adversarial Review](validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md) — 四个真实来源 Case 的历史收口复审。
- [Real User Use Validation](REAL_USER_PILOT_V1.md) — **真实用户使用/反馈**如何成为产品价值证据。
- [Project-wide Calibration](PROJECT_CALIBRATION_20260830.md) — 全面盘点与 Harness 整改记录。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接。
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — 历史/分析层模型；不作为当前 Runtime contract。
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险库；不是 Runtime checklist。
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — practitioner/creator discovery 辅助策略。

## 3. 当前 Runtime 架构 — 0.9.1

### Practice Curator

`skills/curating-erp-ai-resources/`

- 触发：最佳实践、教程、真实工作流/案例、practitioner 资源；
- 输出：1–3 个值得先学的高匹配实践/资源；
- 当前 external curation 必须由本次 fresh discovery / fresh inspection 成立；
- 项目历史 curation/validation 只能作为 lead，不是当前外部证据；
- 快速变化的 AI 工作流考虑当前/近期适用性；
- 宽搜漏掉明显用户生态时选择性做 targeted recall；
- 不默认进入 Tool/Skill/MCP 采用判断。

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- 触发：当前工具够不够、要不要新增/安装/选择/比较 Tool/Skill/MCP/plugin/Agent/workflow；
- 输出：现有工具已够 / 最小值得补的能力 / 条件式升级；
- 不承担泛最佳实践资源策展。

没有第三个 Router Skill。

## 4. 两个“完成”不能混淆

### Build / readiness milestone — complete for controlled trial

- Runtime **0.9.1** 已完成职责拆分后的 fresh-curation / evidence-isolation 修正；
- Curation Pack 01 已提供历史异构任务证据；
- 用户试用入口已具备；
- 可以继续真实用户使用，不再通过内部扩规则证明产品成熟。

### North Star outcome milestone — not validated

尚未证明 Curator 比普通 AI / 自搜索稳定更省判断成本、更少错选、更能找到当前值得学的 practitioner 实践。

这些只能由 `REAL_USER_USE` 证据验证。

## 5. 两条证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 完成搜索、筛选和推荐。

Pack 01 历史 Case：

- [Case 001 — ERP 操作手册](curation-cases/CASE_001_ERP_OPERATING_MANUAL.md)
- [Case 002 — Oracle EBS AI 开发](curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md)
- [Case 003 — 多顾问周报汇总](curation-cases/CASE_003_WEEKLY_REPORT_CONSOLIDATION.md)
- [Case 004 — SAP Bug 诊断/系统访问](curation-cases/CASE_004_SAP_BUG_DIAGNOSIS_SYSTEM_ACCESS.md)

这些是历史项目 evidence，不定义当前 Runtime 的候选池或当前资源排序。

### Lane B — REAL_USER_USE VALIDATION

真实用户实际收到推荐后自然学习、采用、修改、忽略或拒绝，并给出具体反馈。

不要为了获得 Lane B 证据，把用户变成替项目跑测试的人。

## 6. 当前发布层级

### GO — controlled user trial

可以把 Runtime 0.9.1 给少量真实 ERP/ToB/企业信息化用户，在已知/批准的 Agent Skills 宿主里自然使用。

### HOLD — organization-wide standard

在重复 REAL_USER_USE 证据和宿主兼容性出现前，不定义为部门统一标准。

### HOLD — public/open-source release claim

仓库当前没有 `LICENSE` 文件。公开/开源发布前，Owner 需要明确许可方式。

## 7. 历史/条件性设计 — 不作为当前执行入口

- `PROJECT_WORKFLOW.md` — SUPERSEDED；
- `SKILL_BLUEPRINT_V3.md` — SUPERSEDED；
- `AI_LEVERAGE_MODEL_V3.md` — 分析/历史判断模型；
- `SOURCE_ADAPTER_ARCHITECTURE_V3.md` / `SOURCE_ADAPTER_LIFECYCLE_V3.md` — 条件性来源获取设计；
- `phase-01-skill-research/` — 优秀 Skill 研究证据；
- `validation/` 已关闭/失效材料 — 仅按 `EVIDENCE_STATUS.md` 指定 authority 使用；
- `archive/` 与旧 fixture — 历史材料。

历史文件中的 `CURRENT`、`NEXT`、`PASS` 与本 Map 或 Current Plan 冲突时，一律视为历史语境。

## 8. Skill / Harness 设计原则

- Agent Skills progressive disclosure；
- description/name 是主要触发层，避免一个 description 承担互相冲突的默认职责；
- current external curation 与 historical project evidence 分离；
- OpenAI/Anthropic Skill Creator：只加入真正需要的程序性知识，保持职责清晰；
- Harness Engineering：给 Agent 地图，不给越来越长的补丁说明；确定性事实才机械约束。

外部参考：

- https://agentskills.io/specification
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://openai.com/index/harness-engineering/

## 9. 新会话读取顺序

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有具体任务需要时再读 Runtime Skill、Trial Guide、Real User Use Validation 或历史材料。历史项目 evidence 不得自动替代当前用户 external discovery。
