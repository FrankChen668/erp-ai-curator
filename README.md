# ERP AI Curator

面向 **泛 ERP / 企业信息化从业者** 的 AI 工作方式导航项目。

目标用户不局限于 SAP / Oracle 顾问，也包括：

- SAP / Oracle 标准实施、二开与集成；
- Java / .NET 等技术栈建设的定制供应链、财务、采购、制造等企业系统；
- 实施 / 业务顾问、项目经理、产品经理、解决方案人员、开发人员。

## 当前产品目标

面对一个真实工作任务，先判断：

> **AI 应该怎样介入？普通通用 AI 是否已经够用？如果值得引入专门能力，现成的 Skill / Tool / 方法 / 教程中什么最值得采用？**

当前主链路：

`理解任务 → 诊断 AI 杠杆 → 选择通用 AI / 专门方案 / 低成本试验 → 必要时定向搜索 → 比较与核验 → 可执行建议`

因此项目不是 AI 工具大全，也不是“搜索几个链接”的资源搜索器。

## 当前状态

**Product discovery / working-model reset。尚未发布新的正式 Skill。**

已经确认：

- V0.2–V0.4 的重 Gate / 评分 / candidate JSON / validator 路线不作为下一版默认架构；
- 旧 Phase 2/3 把产品逐渐收窄成“资源搜索 + 0–2 推荐”，这一假设已被 V3 工作模型修正；
- 新模型以 **AI Leverage Discovery** 为核心：先判断是否值得引入专门 AI 工作方式，再决定要不要搜索资源；
- 不通过提前罗列 SAP / Oracle / 财务 / 供应链 / 开发场景来获得泛化；
- 官方资料只在它本身最有用，或需要核验高风险动态事实时重点使用；
- 企业数据、源码、本地/云端、权限和合规限制属于真实可用性约束；
- 云端负责产品判断、研究、文档和 GitHub；低能力本地 Agent 不进入关键决策链路。

## 三种合法结果

1. **通用 AI 已足够**：不推荐额外 Skill / Tool；
2. **专门方案有明显价值**：给 1 个主推荐，确有差异时给第 2 个；
3. **暂不值得引入复杂方案**：先给低成本试验路径。

`0–2` 只是正式资源推荐位的默认数量，不再是产品本身。

## 当前权威文档

- `docs/AI_LEVERAGE_MODEL_V3.md`：当前产品工作模型
- `docs/PROJECT_NORTH_STAR.md`：当前项目 North Star
- `docs/SKILL_BLUEPRINT_V3.md`：未来 Skill 的最小设计蓝图，**尚未实现**
- `docs/ADVERSARIAL_REVIEW_V3.md`：V3 对抗性审查
- `docs/validation/PROTOCOL_V3.md`：当前真实任务验证协议
- `docs/validation/REAL_TASK_INTAKE.md`：真实问题进入项目的方法
- `docs/validation/REAL_TASK_BANK_V0.md`：真实来源任务与证据缺口
- `docs/validation/V3_OWNER_REAL_REPLAY_01.md`：V3 对现有 OWNER_REAL 问题的反证回放
- `docs/validation/EVIDENCE_STATUS.md`：当前已证明 / 未证明内容
- `docs/history/`：V0.2–V0.4 历史设计与审查记录
- `archive/`：冻结的早期设计资产

## 关于现有 Skill

`skills/curating-erp-ai-resources/` 是历史 V0.x 实现，冻结，仅作为历史资产和失败样本。

新的正式 Skill 尚未实现。

过去的 Phase 2/3 设计文档继续保留用于追溯，但若与 V3 冲突，以当前 V3 文档和 North Star 为准。

## 当前反偏航原则

不要为了“系统完整”提前建设：

- 大型资源数据库；
- 固定场景 taxonomy；
- 自动 Refresh；
- 统一评分；
- Gate / candidate JSON；
- 固定搜索次数；
- 多 Agent 编排。

任何机制进入主线前都必须回答：

> **它是否能让泛 ERP 用户更快选到更合适的 AI 工作方式？**
