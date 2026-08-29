# ERP AI Curator

面向 **泛 ERP / 企业信息化从业者** 的 AI 工作方式与高质量资源 Curator。

目标用户包括：

- SAP / Oracle 标准实施、二开与集成；
- Java / .NET 等技术栈建设的定制供应链、财务、采购、制造等企业系统；
- 实施 / 业务顾问、项目经理、产品经理、解决方案人员、开发人员。

## 当前产品目标

面对一个真实项目工作任务，帮助用户判断：

> **AI 应该怎样介入？现有 AI / 工具链是否已经够用？如果需要外部能力或学习资源，哪些 Skill / Tool / 方法 / 教程真正值得采用？**

当前主链路：

`真实交付任务 → 明确输出与约束 → 判断 AI 工作方式 → 必要时定向发现资源 → 比较与核验 → 少量可执行推荐`

因此项目不是 AI 工具大全，也不是“搜索几个链接”的资源搜索器。

当用户明确要求寻找外部资源时，**资源采编本身是核心能力之一**：不仅要找到当前可信的官方/原始来源，也要尽量找到真正有实操价值的 GitHub 项目、教程、公众号/视频/社区经验与最佳实践，并替用户做取舍。

## 当前验证重点

**项目交付场景优先。**

当前主要验证两类任务：

### 1. 交付产物型

- 需求分析；
- 方案设计；
- 数据处理 / 核对；
- PPT / 项目汇报；
- 交互原型；
- 其他有真实证据的测试 / 问题分析场景。

### 2. 工具上手型

- Codex；
- WorkBuddy；
- 其他能明显改善项目交付的 AI / Agent 工具。

目标不是整理“功能大全”，而是找到从“知道这个工具”到“能在 ERP / 企业信息化项目里真正用起来”的最短可靠路径。

当前场景计划见：

`docs/validation/DELIVERY_SCENARIO_VALIDATION_V3.md`

## 当前状态

**V3 product validation + delivery-scenario curation validation。尚未发布新的正式 Skill。**

已经确认：

- V0.2–V0.4 的重 Gate / 评分 / candidate JSON / validator 路线不作为下一版默认架构；
- 旧 Phase 2/3 把产品逐渐收窄成“资源搜索 + 0–2 推荐”，这一假设已被 V3 工作模型修正；
- 对明确的资源发现任务，不再把“官方资料”当天然主推荐：官方/原始资料主要承担当前事实锚点，GitHub、社区实战、中文教程、视频和独立测评可以承担实践价值；
- T01/T02 暴露出 Discovery Recall、方案适配度与成熟度区分、中国实践平台获取覆盖等问题；
- 当前验证一种受控的 **Curator / Orchestrator** 形态：Curator 负责判断，Codex 仅在证据需要时调用已安装、已审查、只读的来源 Skill/MCP；
- 微信 Search → Reader 的受控组合已在本地真实 PASS，但这只证明该链路可组合，不证明来源 Adapter 一定提升最终推荐；
- 第一次 Adapter uplift 测试在一个混合任务上没有产生可归因增量，同时暴露了测试题偏离项目交付主线的问题；
- Adapter 的运行时调用与安装/更新维护已经分离，禁止正常采编过程中自动安装或追 `latest`；
- 企业数据、源码、本地/云端、权限和合规限制属于真实可用性约束；
- 云端负责产品判断、研究、文档和 GitHub；本地 Agent 仅在必须访问本地环境、安装/运行具体工具或执行受控采编测试时参与，不承担最终产品判断。

当前下一步不是开发正式 Skill，也不是继续扩来源 Adapter，而是验证 **需求分析、数据处理、Codex/WorkBuddy 上手、方案/PPT/原型等项目交付场景的资源采编质量**。

## 当前权威文档

- `docs/CURRENT_EXECUTION_PLAN_V3.md`：**当前执行主线、阶段、云端/本地职责与停止条件**
- `docs/AI_LEVERAGE_MODEL_V3.md`：当前产品工作模型
- `docs/PROJECT_NORTH_STAR.md`：当前项目 North Star
- `docs/SKILL_BLUEPRINT_V3.md`：未来 Skill 的最小设计蓝图，**尚未实现**
- `docs/SOURCE_STRATEGY_V3.md`：当前资源发现与来源组合策略
- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`：来源能力的条件式组合 Pilot 架构
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`：来源 Skill/MCP 的安装、更新、调用、降级和移除契约
- `docs/validation/DELIVERY_SCENARIO_VALIDATION_V3.md`：**当前项目交付场景验证计划**
- `docs/validation/DELIVERY_D01_REQUIREMENTS_ANALYSIS.md`：下一项需求分析采编测试协议
- `docs/validation/RESOURCE_CURATION_PILOT_V3.md`：资源采编专项测试历史主协议
- `docs/validation/SOURCE_ADAPTER_PILOT_V3.md`：来源 Skill/MCP 本地资格审查与增量测试方案
- `docs/validation/SOURCE_ADAPTER_ROUTING_RESULT_01.md`：微信 Search → Reader 路由实测结果
- `docs/validation/CURATION_UPLIFT_AB_RESULT_01.md`：第一次来源增量测试解释
- `docs/validation/REAL_TASK_INTAKE.md`：真实问题进入项目的方法
- `docs/validation/REAL_TASK_BANK_V0.md`：真实来源任务与证据缺口
- `docs/validation/EVIDENCE_STATUS.md`：当前已证明 / 未证明内容
- `docs/history/`：V0.2–V0.4 历史设计与审查记录
- `archive/`：冻结的早期设计资产

## 关于现有 Skill

`skills/curating-erp-ai-resources/` 是历史 V0.x 实现，冻结，仅作为历史资产和失败样本。

新的正式 Skill 尚未实现。

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
- 默认安装/调用所有平台适配器；
- Adapter package manager / 自动 updater。

场景列表只是当前验证样本，不是永久分类体系。

任何机制进入主线前都必须回答：

> **它是否能让泛 ERP / 企业信息化人员更快完成真实项目交付，或更快找到真正值得学习/使用的 AI 资源？**
