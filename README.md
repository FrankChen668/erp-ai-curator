# ERP AI Curator

面向 **SAP / Oracle / ERP / ToB / 企业信息化从业者** 的 AI 实践 Curator。

> **面对一个真实工作任务，帮用户找到最值得学习/采用的现成 AI 实践与资源，并判断是否真的需要新增 Tool / Skill / MCP / 工作流。**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 想直接试用

当前版本：**0.8.1 — Controlled User Trial**。

- 试用指南：`docs/USER_TRIAL_GUIDE_V1.md`
- Skill：`skills/curating-erp-ai-resources/`

当前发布边界：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

0.8.0 完成 runtime simplification；0.8.1 只修复一条由真实 Codex Desktop 日志直接证明的执行缺陷：

- AI/Agent 工作方式请求不能在搜索时退化成纯领域“最佳实践”；
- 明确找教程/实践时，必须真正调查 practitioner/creator 候选；
- 如果宿主搜索策略、访问或 coverage 阻止 practitioner evidence，应明确 `coverage/policy gap`，不能用官网替代后声称 curation 完成。

Runtime 仍保持简洁：

```text
理解真实任务
→ 判断用户是在找实践、做采用选择，或两者都有
→ practitioner-first discovery
→ 核验 serious candidates
→ 选少量最值得看的/用的并停止
```

只保留两个按需 reference：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

## 项目维护者从这里开始

- `docs/PROJECT_MAP.md` — 当前导航权威
- `docs/PROJECT_NORTH_STAR.md` — 产品目标与边界
- `docs/OWNER_EXECUTION_RULES.md` — Cloud / Local / Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段
- `docs/validation/EVIDENCE_STATUS.md` — 证据状态
- `skills/curating-erp-ai-resources/SKILL.md` — 当前 runtime Skill

## 当前最重要的未验证问题

> **Curator 是否能比普通 AI / 用户自己搜索更稳定地找到高价值 practitioner 实践、减少噪声和错选，并让真实用户愿意再次使用？**

0.8.1 修正的是已观察到的 runtime 行为，不证明产品价值已经验证。

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
