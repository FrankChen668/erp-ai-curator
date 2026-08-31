# ERP AI Curator

面向 **SAP / Oracle / ERP / ToB / 企业信息化从业者** 的 AI 工作方式 Curator。

> **面对真实工作任务，帮用户找到真正值得学习的现成 AI 实践；当用户明确要做能力选型时，再判断当前工具是否够用、是否值得新增 Tool / Skill / MCP / 工作流。**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 想直接试用

当前 Runtime 版本：**0.9.1 — Controlled User Trial**。

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

0.9.1 继续修 Practice Curator 的真实执行缺陷，但不增加新框架：

- 正常外部策展必须做**本次 fresh discovery**，不能直接沿用仓库中的历史验证包/旧推荐排序；
- 历史项目证据只能作为搜索线索，最终推荐资源必须在本次重新打开核验；
- 对快速变化的 AI 工作流主动检查近期候选和当前适用性；
- 宽泛搜索明显漏掉用户职业/语言生态时，对最可能改变答案的 1–3 个 practitioner pool 做定向补搜，而不是做平台配额；
- 普通用户回答不把项目内部 validation 文档当外部推荐依据展示。

## 项目维护者从这里开始

- `docs/PROJECT_MAP.md` — 当前导航权威
- `docs/PROJECT_NORTH_STAR.md` — 产品目标与边界
- `docs/OWNER_EXECUTION_RULES.md` — Cloud / Local / Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段
- `docs/validation/EVIDENCE_STATUS.md` — 证据状态
- `docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md` — 0.9.0 Runtime 职责拆分
- `docs/validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md` — 0.9.1 fresh curation / evidence isolation

## 当前最重要的未验证问题

> **Curator 是否能比普通 AI / 用户自己搜索更稳定地找到高价值、当前仍适用的 practitioner 实践，并在能力选型时减少错装/错选，且这个差异足以让真实用户再次使用？**

0.9.1 是真实执行缺陷修正，不是产品价值证明。

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
