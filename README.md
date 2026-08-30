# ERP AI Curator

面向 **SAP / Oracle / ERP / ToB / 企业信息化从业者** 的 AI 实践 Curator。

> **面对一个真实工作任务，帮用户找到最值得学习/采用的现成 AI 实践与资源，并判断是否真的需要新增 Tool / Skill / MCP / 工作流。**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 想直接试用

当前版本：**0.8.0 — Controlled User Trial**。

- 试用指南：`docs/USER_TRIAL_GUIDE_V1.md`
- Skill：`skills/curating-erp-ai-resources/`

当前发布边界：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

0.8.0 的核心变化不是增加能力，而是**删除 runtime 复杂度**：

```text
理解真实任务
→ 判断用户是在找实践、做采用选择，或两者都有
→ practitioner-first discovery
→ 核验 serious candidates
→ 选少量最值得看的/用的并停止
```

Runtime 不再要求 Agent 先执行 A/B/C 分类、adoption-consistency 或 decision-boundary 框架。

只保留两个按需 reference：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

如果用户当前工具已经够用，直接劝退新增能力；如果用户明确要找最佳实践/教程，即使无需新增工具，也仍然完成 practitioner curation。

## 项目维护者从这里开始

- `docs/PROJECT_MAP.md` — 当前导航权威
- `docs/PROJECT_NORTH_STAR.md` — 产品目标与边界
- `docs/OWNER_EXECUTION_RULES.md` — Cloud / Local / Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段
- `docs/validation/EVIDENCE_STATUS.md` — 证据状态
- `skills/curating-erp-ai-resources/SKILL.md` — 当前 runtime Skill

## 当前最重要的未验证问题

> **Curator 是否能比普通 AI / 用户自己搜索更稳定地找到高价值 practitioner 实践、减少噪声和错选，并让真实用户愿意再次使用？**

这只能由真实用户自然使用验证，不能靠继续堆 Skill 规则或内部 benchmark 自证。

## 当前不做

真实使用未证明必要前，不建设：

- 大型资源数据库 / 自动 Refresh；
- 固定场景 taxonomy；
- 统一评分 / Gate；
- 多 Agent 编排；
- creator/UP 主排行榜；
- 每个候选强制 runtime；
- 用户工具测试协议。

## Public / open-source note

仓库当前公开，但尚未包含 repository `LICENSE`。如果要正式声明 public/open-source release complete，需要 Owner 明确许可方式。
