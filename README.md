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

但当用户明确要求寻找外部资源时，**资源采编本身是核心产品能力之一**：不仅要找到当前可信的能力来源，也要尽量找到真正有实操价值的 GitHub 项目、教程、公众号/视频/社区经验与最佳实践，并替用户做取舍。

## 当前状态

**Product discovery / working-model reset。尚未发布新的正式 Skill。**

已经确认：

- V0.2–V0.4 的重 Gate / 评分 / candidate JSON / validator 路线不作为下一版默认架构；
- 旧 Phase 2/3 把产品逐渐收窄成“资源搜索 + 0–2 推荐”，这一假设已被 V3 工作模型修正；
- 新模型以 **AI Leverage Discovery** 为核心：先判断是否值得引入专门 AI 工作方式，再决定要不要搜索资源；
- 对明确的资源发现任务，不再把“官方资料”当天然主推荐：官方/原始资料主要承担事实锚点，GitHub、社区实战、中文教程、视频和独立测评可以承担实践价值；
- T01/T02 暴露出中国实践平台的获取覆盖问题，当前正在验证一种更轻的方案：**Curator 负责判断，Codex 按证据需要调用已安装的微信/小红书/B站来源 Skill/MCP 做只读采集**；这仍是 Pilot，不是已确认永久架构；
- 不通过提前罗列 SAP / Oracle / 财务 / 供应链 / 开发场景来获得泛化；
- 企业数据、源码、本地/云端、权限和合规限制属于真实可用性约束；
- 云端负责产品判断、研究、文档和 GitHub；本地 Agent 仅在必须访问本地环境、安装/运行具体工具或做机械验证时参与，不承担最终产品判断。

## 三种合法结果

1. **通用 AI 已足够**：不推荐额外 Skill / Tool；
2. **专门方案有明显价值**：给 1 个主推荐，确有差异时给第 2 个；
3. **暂不值得引入复杂方案**：先给低成本试验路径。

`0–2` 只是正式方案推荐位的默认数量，不限制用于支撑主方案的事实锚点或少量实战伴随资源。

## 当前权威文档

- `docs/AI_LEVERAGE_MODEL_V3.md`：当前产品工作模型
- `docs/PROJECT_NORTH_STAR.md`：当前项目 North Star
- `docs/SKILL_BLUEPRINT_V3.md`：未来 Skill 的最小设计蓝图，**尚未实现**
- `docs/SOURCE_STRATEGY_V3.md`：当前资源发现与来源组合策略
- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`：微信/小红书/B站等来源能力的条件式组合 Pilot 架构
- `docs/ADVERSARIAL_REVIEW_V3.md`：V3 对抗性审查
- `docs/validation/ADVERSARIAL_REVIEW_SOURCE_STRATEGY_V3.md`：来源策略专项对抗性审查
- `docs/validation/ADVERSARIAL_REVIEW_SOURCE_ADAPTER_V3.md`：来源适配器架构专项对抗性审查
- `docs/validation/PROTOCOL_V3.md`：当前真实任务验证协议
- `docs/validation/V3_SYSTEMATIC_TEST_PLAN.md`：V3 判断与增量价值系统测试方案
- `docs/validation/RESOURCE_CURATION_PILOT_V3.md`：当前资源采编专项测试方案
- `docs/validation/SOURCE_COVERAGE_FINDING_01.md`：中国实践来源覆盖问题的证据记录
- `docs/validation/SOURCE_ADAPTER_PILOT_V3.md`：来源 Skill/MCP 的本地资格审查、只读验证与增量测试方案
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
- 多 Agent 编排；
- 固定平台覆盖配额；
- 默认安装/调用所有平台适配器。

任何机制进入主线前都必须回答：

> **它是否能让泛 ERP 用户更快选到更合适的 AI 工作方式或真正值得学习/使用的资源？**
