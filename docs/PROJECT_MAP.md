# ERP AI Curator — Project Map

Date: 2026-08-30
Status: **CURRENT NAVIGATION AUTHORITY**

> 给人和 Agent 的“地图”，不是第二本说明书。遇到冲突时，先按下面的层级判断，不从历史文档反推当前状态。

## 1. 当前权威层级

1. [Project North Star](PROJECT_NORTH_STAR.md) — 产品为什么存在、做什么/不做什么。
2. [Owner Execution Rules](OWNER_EXECUTION_RULES.md) — 云端持续推进、本地 Agent/Owner 何时接力。
3. [Current Execution Plan](CURRENT_EXECUTION_PLAN_V3.md) — 当前阶段、近阶段目标与下一步。
4. [Evidence Status](validation/EVIDENCE_STATUS.md) — 哪些结论有证据、哪些仍未验证。
5. [Current Skill](../skills/curating-erp-ai-resources/SKILL.md) — 可分发运行时工作流。

若这五者冲突：`North Star > Owner Rules > Current Plan > Evidence Status > runtime Skill implementation detail`。发现冲突应修仓库，不允许 Agent 自行挑一个顺眼的版本继续。

## 2. 当前阶段辅助文档

- [Real User Pilot](REAL_USER_PILOT_V1.md) — **真实用户使用/反馈**如何成为产品验证证据。
- [Session Handoff](SESSION_HANDOFF_CURRENT.md) — 新会话最小交接，只保存当前状态，不承担历史说明。
- [AI Leverage Model](AI_LEVERAGE_MODEL_V3.md) — 当前方法的详细解释；不是每次运行必读。
- [Adversarial Review](ADVERSARIAL_REVIEW_V3.md) — 风险清单；按需用于设计复审，不是 runtime checklist。
- [Creator Prior Strategy](CREATOR_PRIOR_STRATEGY_V3.md) — practitioner/creator discovery 的辅助策略。

## 3. 真实问题 Curator 输出与产品验证必须分开

### Lane A — REAL_USER_ORIGIN CURATION

来源是真实同事/问卷/Owner 的真实问题，但由 Cloud 先完成搜索、筛选和推荐。

产物放在：`docs/curation-cases/`

它可以证明：

- 产品确实能处理真实来源问题；
- 哪些方法/资源值得形成推荐；
- Curator 是否出现明显边界错误。

它**不能证明**：用户真的采用、节省时间、减少返工或比普通 AI 更有价值。

### Lane B — REAL_USER_USE VALIDATION

真实同事收到推荐后自然学习、采用、修改或拒绝，并给出具体反馈。

这才属于产品价值验证，依据 [Real User Pilot](REAL_USER_PILOT_V1.md) 记录。

不要为了获得 Lane B 证据，把用户变成“替项目跑测试的人”。

## 4. 历史/条件性设计 — 不作为当前执行入口

以下文档保留用于理解演化或未来条件触发，不得覆盖当前权威：

- `PROJECT_WORKFLOW.md` — 已标记 SUPERSEDED 的历史阶段协议；
- `SKILL_BLUEPRINT_V3.md` — Skill 实现前的历史设计蓝图；
- `SOURCE_ADAPTER_ARCHITECTURE_V3.md` / `SOURCE_ADAPTER_LIFECYCLE_V3.md` — 条件性来源获取设计，只有重复出现材料获取瓶颈且会改变推荐时才重新激活；
- `phase-01-skill-research/` — 优秀 Skill 研究证据与设计来源；
- `validation/` 中已关闭/失效的协议、回归与结果 — 仅按 `EVIDENCE_STATUS.md` 指定的 authority 使用；
- `archive/` — 历史 runtime / resource-library 资产。

历史文件中的 `CURRENT`、`NEXT`、`PASS` 等词如果与本 Map 或 Current Plan 冲突，一律视为历史语境。

## 5. Skill / Harness 设计原则

当前采用的外部设计原则：

- Agent Skills 规范：`SKILL.md` 只放核心工作流，详细内容放按需 references；主文件建议控制在 5,000 tokens / 500 lines 内。
  - https://agentskills.io/specification
- Anthropic `skill-creator`：description 是主要触发机制；主 Skill 保持通用、progressive disclosure、真实 Prompt 观察行为。
  - https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- OpenAI `skill-creator`：Skill 包只保留直接支持运行的必要文件，不把 README/CHANGELOG/创建过程塞进 runtime Skill。
  - https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- OpenAI Harness Engineering：给 Agent “地图而不是 1000 页手册”；对真正重要的不变量做机械约束，而不是继续堆说明。
  - https://openai.com/index/harness-engineering/

## 6. 新会话读取顺序

默认只读：

```text
PROJECT_MAP
→ PROJECT_NORTH_STAR
→ OWNER_EXECUTION_RULES
→ CURRENT_EXECUTION_PLAN_V3
→ EVIDENCE_STATUS
```

只有任务需要时再读 Skill、Pilot、AI Leverage、Adversarial Review 或历史材料。

这条顺序用于降低上下文污染和历史结论复活。