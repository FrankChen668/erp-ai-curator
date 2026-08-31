# ERP AI Curator

面向 **SAP / Oracle / ERP / ToB / 企业信息化从业者** 的 AI 工作方式 Curator。

> **面对真实工作任务，帮用户找到真正值得学习的现成 AI 实践；当用户明确要做能力选型时，再判断当前工具是否够用、是否值得新增 Tool / Skill / MCP / 工作流。**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 想直接试用

当前 Runtime 版本：**0.9.2 — Controlled User Trial**。

- 试用指南：`docs/USER_TRIAL_GUIDE_V1.md`
- Practice Curator：`skills/curating-erp-ai-resources/`
- Capability Advisor：`skills/advising-erp-ai-capabilities/`

当前发布边界：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

0.9.0 把两个长期互相污染的 Runtime 职责拆开：

```text
找最佳实践 / 教程 / 案例
→ curating-erp-ai-resources

判断现有工具够不够 / 要不要新增 Tool、Skill、MCP
→ advising-erp-ai-capabilities
```

0.9.1 建立 fresh curation / evidence isolation：

- 正常外部策展必须做**本次 fresh discovery**，不能直接沿用仓库中的历史验证包/旧推荐排序；
- 历史项目证据只能作为搜索线索，最终推荐资源必须在本次重新打开核验；
- 对快速变化的 AI 工作流主动检查近期候选和当前适用性；
- 普通用户回答不把项目内部 validation 文档当外部推荐依据展示。

0.9.2 做两个窄修正：

- 当中文 practitioner 候选过度集中在单一平台，或其余候选主要是官方/厂商/GitHub/英文来源时，对最可能改变排序的 1–2 个额外中文 practitioner pool 做定向召回修正；这不是平台配额；
- 邻近但不同的交付物不能因为带 SAP/ERP 标签就挤进 Top 推荐，官方文档默认作为能力核验而不是 practitioner Top 3 填充物。

## 项目维护者从这里开始

- `docs/PROJECT_MAP.md` — 当前导航权威
- `docs/PROJECT_NORTH_STAR.md` — 产品目标与边界
- `docs/OWNER_EXECUTION_RULES.md` — Cloud / Local / Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段
- `docs/validation/EVIDENCE_STATUS.md` — 证据状态
- `docs/validation/CURATOR_092_ECOSYSTEM_RECALL_TASK_FIT.md` — 0.9.2 ecosystem recall / task-fit correction
- `docs/validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md` — 0.9.1 fresh curation / evidence isolation

## 当前最重要的未验证问题

> **Curator 是否能比普通 AI / 用户自己搜索更稳定地找到高价值、当前仍适用的 practitioner 实践，并在能力选型时减少错装/错选，且这个差异足以让真实用户再次使用？**

0.9.2 仍是 Runtime 缺陷修正，不是产品价值证明。

## 当前不做

真实使用未证明必要前，不建设：

- 第三个 Router Skill；
- 大型资源数据库 / 自动 Refresh；
- 固定场景 taxonomy；
- 统一评分 / Gate；
- 多 Agent 编排；
- creator/UP 主排行榜；
- 每个候选强制 runtime；
- 用户工具测试协议。

## Public / open-source note

仓库当前公开，但尚未包含 repository `LICENSE`。如果要正式声明 public/open-source release complete，需要 Owner 明确许可方式。
