# ERP AI Curator

面向 **泛 ERP / 企业信息化从业者** 的 AI 工作方式与高质量资源 Curator。

目标用户包括：

- SAP / Oracle 标准实施、二开与集成；
- Java / .NET 等技术栈建设的定制供应链、财务、采购、制造等企业系统；
- 实施 / 业务顾问、项目经理、产品经理、解决方案人员、开发人员。

## 当前产品目标

面对一个真实项目工作任务，帮助用户判断：

> **AI 应该怎样介入？现有 AI / 工具链是否已经够用？如果需要外部能力或学习资源，哪些现成 Skill / Tool / 方法 / 教程 / 实战经验最值得采用？**

当前基本单元不是“需求分析 / PPT / 原型 / 数据处理”这种宽标签，而是：

```text
真实项目情境
+ 手头已有材料
+ 当前必须完成的动作
+ 下一份明确交付物
+ 时间 / 评审 / 数据边界
```

例如：

> 客户 Workshop 已结束，手里有会议纪要、现状流程、RFP、Excel/Word 附件；第二天上午需要形成第一版可评审需求包。

## 默认资源采编顺序

对“怎么做 / 值不值得学 / 有什么坑”这类采用问题，当前原则是：

```text
第三方实操 / 测评 / 攻略 / 案例
→ 对应原始 Skill / Tool / 方法 / 仓库
→ 必要的官方当前事实核验
```

第三方内容优先回答：

- 别人怎么用；
- 输入、Prompt、步骤、Workflow；
- 实际输出；
- 返工、失败点和适用边界；
- 是否真的值得顾问投入时间学习。

官方/原始事实重点核验：

- 版本；
- 当前安装方式；
- 兼容；
- 价格；
- 隐私 / 安全政策；
- 许可证；
- 当前原生能力。

官方不是默认主推荐，但第三方作者、粉丝、收藏、点赞、播放、Stars 也不是质量结论。

## 第三方来源

可作为高价值实操来源的包括：

- Bilibili / YouTube；
- 微信公众号；
- 小红书；
- 知乎、掘金、CSDN、人人都是产品经理等社区；
- AI 产品经理 / 企业咨询 / Agent 实践作者；
- GitHub PM / BA / Agent / Skill 库；
- WorkBuddy / Codex / Claude Code 等现成教程、社区手册、蓝皮书。

原则：

> **Creator reputation may decide what to inspect first; only the specific content decides what to recommend.**

如果普通 Web 能发现内容但拿不到完整正文/字幕，才考虑已批准的来源 Adapter；仍无法读取则记录 Coverage Gap。

不能因为当前 Agent 读不到某个平台，就推断该平台没有优质内容。

## 不重复造轮子

已经存在的：

- PM / BA Skill 库；
- Agent / Codex / WorkBuddy 实战教程；
- PRD / 原型 / 流程图 / PPT / 数据处理工作流；
- 社区蓝皮书、作者专题和教程系列；

都优先作为 **feeder ecosystem**。

ERP AI Curator 的价值不是复制它们，而是：

> **把已有互联网生态映射到真实 ERP 工作问题，并只留下少量真正值得用的内容。**

只有现成资源明确不足时，才补 `Curator synthesis`，并且必须显式标注。

## 本地实测不是默认流水线

不再默认对每个候选执行：

`静态审查 → 安装 → runtime → artifact → cleanup`

只有以下情况才做最小实测：

- 高质量第三方证据不足；
- 不同测评结论冲突；
- 安装 / 权限 / 隐私 / 安全风险高；
- 准备作为公司内部长期标准推荐；
- 关键能力仅靠文档无法确认。

否则，**第三方实操 + 原始实现 + 必要官方事实**已经足够做资源推荐。

## 当前真实需求来源

2026-08 培训问卷提供了 83 份目标用户反馈。

当前主要对象是实施顾问和项目经理；大量用户已经经常使用 AI，真正反复出现的问题是：

> **怎样把手头真实项目材料稳定变成可以评审、编辑、交付的成果，并减少返工。**

当前优先 Problem Cards 包括：

- Workshop / 纪要 → 需求包；
- 需求 → PRD / FS；
- 需求 / 规则 → 可点击原型；
- 业务逻辑 → 可编辑流程图；
- 项目材料 → 客户汇报 PPT；
- Excel / CSV → 清洗、核对、异常；
- 代码库 → 功能逻辑 / FS / Debug；
- 需求 → 测试场景 / 测试用例；
- Codex / WorkBuddy 等工具如何服务以上真实任务。

这些只是当前需求队列，不是永久 taxonomy。

## 当前状态

**V3 实际资源采编阶段。新的正式 Curator Skill 尚未实现。**

已经确认：

- 旧 V0.2–V0.4 的重 Gate / 评分 / validator 路线不回归；
- Survey-derived Problem Cards 已成为真实需求源；
- P01 已找到可实践的会议纪要 → 需求提炼资源，但成熟度仍需谨慎表述；
- P04A 找到强 draw.io 候选，同时暴露了官网重力、Codex 环境偏置、实测过度等问题；
- 来源策略已改为 **practitioner-first**；
- 微信 Search → Reader 已证明可受控组合，但 Adapter 只是按需获取能力；
- B站等平台的普通 Web discovery 与完整正文/字幕 acquisition 必须分开判断；
- P04B 这类 runtime pilot 不再自动成为下一步，只在真正存在材料不确定性时恢复。

当前重点不是继续扩测试框架，而是围绕真实 Problem Cards **持续采集和筛选高质量实操资源**。

## 当前权威文档

- `docs/PROJECT_NORTH_STAR.md`：长期产品边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md`：当前执行主线
- `docs/SOURCE_STRATEGY_V3.md`：practitioner-first 来源策略
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`：优质作者 discovery prior 边界
- `docs/ADVERSARIAL_REVIEW_V3.md`：长期反偏航检查
- `docs/SKILL_BLUEPRINT_V3.md`：未来 Curator Skill 设计，尚未实现
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`：真实问卷问题卡
- `docs/validation/EVIDENCE_STATUS.md`：已证明 / 未证明内容
- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`：来源 Adapter 架构边界
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`：来源 Adapter 安装/更新/调用规则
- `docs/history/`：历史设计与失败经验

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
- 影响者排行榜；
- 每个候选强制 runtime / artifact test；
- 自建另一个 PM Skills / WorkBuddy / Codex 教程库；
- 因 acquisition 工具受限而降低 B站 / 微信 / 小红书等平台价值；
- 把 Curator synthesis 包装成第三方最佳实践。

最终检查始终是：

> **如果今晚把这个资源发给一个泛 ERP 同事，他明天能不能拿自己的真实项目材料开始用？**
