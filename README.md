# ERP AI Curator

面向 SAP / Oracle / ERP 项目人员的 AI 资源决策项目。

## 项目目标

当实施顾问、项目经理、开发人员的真实工作问题**确实需要选择外部资源**时，替用户完成：

`理解任务 → 搜索 → 打开原始内容 → 横向比较 → 淘汰 → 输出少量强资源`

默认输出 0–2 个 Skill / Tool / 教程 / 方法；没有强匹配时允许 0 个。

项目不是 AI 工具大全，也不是通用 ERP Agent。

## 当前状态

**Product discovery / real-task evidence gathering。尚未发布新的正式 Skill。**

已经确认：

- V0.2–V0.4 的重 Gate / 评分 / candidate JSON / validator 路线不作为下一版默认架构；
- Phase 4 本地 Agent Pilot 已关闭且不合并；
- 当前验证从真实问题出发，不再用合成 Eval 代替产品证据；
- 云端负责研究、判断、文档和 GitHub；低能力本地 Agent 不进入产品决策链路；
- 最终产品形态**不预设一定是 Skill**，也可能是轻量资源包 + 检索方法；只有真实使用证明 Skill 有额外价值后才固化。

## 关键入口

- `docs/PROJECT_NORTH_STAR.md`：当前项目边界与 North Star
- `docs/validation/PROTOCOL_V2.md`：真实任务优先的验证协议
- `docs/validation/REAL_TASK_INTAKE.md`：问卷 / 访谈 / 实际求助如何进入项目
- `docs/validation/REAL_TASK_BANK_V0.md`：当前真实来源任务与证据缺口
- `docs/validation/EVIDENCE_STATUS.md`：当前已证明 / 未证明内容
- `docs/discovery/STARTER_PACK_V0.md`：少量当前已核验候选资源，**不是用户验证通过清单**
- `docs/history/`：V0.2–V0.4 历史设计与审查记录
- `archive/`：冻结的早期设计资产

## 关于现有 Skill

`skills/curating-erp-ai-resources/` 是历史 V0.x 实现，**冻结，仅作为历史资产和失败样本，不代表当前产品方案。**

新的 `erp-ai-curator` Skill 尚未进入正式实现阶段。

## 当前主线

> **真实工作问题 → 判断是否需要 Curator → 真搜索 / 真阅读 / 真比较 → 0–2 推荐 → 记录分享/使用反馈。**

在真实证据不足前，不建设大型资源数据库、自动 Refresh、统一评分体系、多 Agent 编排或复杂 validator。
