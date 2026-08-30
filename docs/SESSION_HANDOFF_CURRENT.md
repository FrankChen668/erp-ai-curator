# ERP AI Curator — Current Session Handoff

Date: 2026-08-30
Status: **CURRENT / CONTROLLED REAL-USER USE**

> 新会话先读 `docs/PROJECT_MAP.md`，不要从历史聊天恢复当前状态。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

## 2. 当前产品

ERP AI Curator 是**真实 ERP / ToB / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心目标：

> **替用户找到最值得学习/采用的现成 AI 实践与资源，并判断是否真的需要新增能力。**

不是工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. Current Skill — 0.8.0

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

0.8.0 是一次 runtime simplification。

主流程只有：

```text
理解真实任务
→ 判断用户要找实践、做采用选择，或两者都有
→ practitioner-first discovery
→ 核验 serious candidates
→ 选择少量高匹配资源/做法并停止
```

不再要求 runtime 先产生 A/B/C，也不再加载 adoption-consistency / decision-boundaries。

只保留两个按需 reference：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

关键行为仍然必须成立：

- 明确找最佳实践/教程时，真正给 practitioner 资源，不用官网+自写教程代替；
- 当前工具已经够用时，不因为 Curator 身份强推 Tool/Skill；
- author self-practice 不冒充独立验证；
- official 主要核验当前事实；
- 强匹配优先，少推荐，结论稳定即停；
- 诊断/理解默认 read-only，权限最小化。

## 4. Why 0.8.0

流程图真实试用缺陷证明 practitioner discovery 必须加强；但继续对每个缺陷增加分类、reference 和自检会形成 patch-on-patch。

对照 OpenAI / Anthropic Skill Creator 的简洁、适当自由度和 progressive disclosure 原则，当前结论是：

> **项目研究/治理可以复杂；runtime Skill 只保留模型真正需要的程序性知识。**

Authority：`docs/validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md`。

## 5. Historical evidence

Curation Pack 01 保持关闭。旧 A/B/C 标签仅是历史分析记录，不再定义 runtime：

- Case 001 — ERP 操作手册；
- Case 002 — Oracle EBS AI 开发；
- Case 003 — 周报/PPT 汇总；
- Case 004 — SAP Bug/system evidence access。

不要重新启动 pre-user case accumulation。

## 6. Current release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

当前真正未验证的是：Curator 是否比普通 AI/自搜索更稳定地找到高价值实践、减少噪声/错选，并让用户愿意再次使用。

## 7. Cloud / Local / Owner

Cloud 能做就继续，包括 Web/GitHub discovery、真实反馈审查、窄缺陷修正和 authority/Harness 维护。

Local Agent 只在真实决策依赖本地 repo/runtime/ERP 环境/受保护 evidence，或必须验证某个宿主的 Skill/reference 行为时接力。

Owner 当前唯一潜在明确裁决项仍是 repository license（仅当要声明 open-source release complete 时）。

## 8. Do not revive without evidence

- Gate / scoring / taxonomy / validator；
- synthetic benchmark loop；
- resource DB / auto refresh；
- creator ranking；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- user tool-test protocol；
- card-specific permanent rules。
