# Phase 1 Design Synthesis — 对 ERP AI Curator 的设计启示

> 本文是研究结论，不是 Phase 2 最终产品方案。目的：明确下一阶段需要重新证明什么，避免直接从 V0.4 继续增加规则。

## 1. 第一性重新定义

从用户价值出发，ERP AI Curator 的本质更可能是：

> **面向 SAP / Oracle / ERP 顾问真实工作任务的资源决策压缩器：替用户完成搜索、阅读、比较和取舍，只留下极少量值得继续投入时间的原始资源。**

它不应默认被定义为资源数据库、搜索引擎、事实审计平台、AI 工具百科或自动采编后台。这个定义仍需在 Phase 2 用真实任务验证。

## 2. V0.2–V0.4 偏航的根因

资源采编的核心判断包括：资源是否真正解决当前任务、是否比其他候选更值得看、语言与质量冲突时如何取舍、热度与专业性冲突时如何判断、什么时候宁可留空。

这些属于 `judgment + context-dependent decision`。

V0.x 逐渐把这些判断转成 `fields + gates + validator + PASS`，导致 Agent 的优化目标从“找到值得分享的资源”滑向“构造能通过校验的 candidate”。这是结构性问题，不是再补一个 Gate 能解决的问题。

## 3. 从 21 个 Skill 提炼出的候选产品原则

### P1 — 强匹配优先于覆盖率

来自 `academy-guide`：强匹配才推荐，最多 1–2 个，弱匹配宁可沉默。

> 一个主题 0 推荐应该是正常结果，而不是失败状态。

### P2 — 搜索必须为比较服务

来自 `deep-research`：多角度搜索、主动寻找反例、追溯原始来源、解释冲突，最后替用户做选择。

“搜到 N 条”本身不是成功指标。

### P3 — 时效事实只在必要时升级核验

不是每篇资源都需要 claim audit。只有 API、安装配置、模型兼容、价格、版本、产品能力等会直接影响用户是否能照做成功的内容，才需要更强事实核验。

普通方法论、案例、设计思路主要判断 task fit、practical value、differentiation、transferability。

### P4 — 主 Skill 应像导航器，不像法规汇编

候选方向：

```text
SKILL.md
├── 理解用户任务
├── 搜索与比较主流程
├── 推荐输出原则
└── 按需路由到 references
    ├── source-strategy.md
    ├── recommendation-heuristics.md
    └── volatile-fact-check.md
```

是否采用，Phase 3 再决定。

### P5 — Script 只处理 deterministic work

可能适合 script：URL normalize、exact duplicate、数据格式转换、固定 schema 校验。

不适合 script：是否值得推荐、哪个候选更有顾问价值、案例能否迁移、是否应该留空。

### P6 — 不把资源库当成前置条件

Phase 2 应优先验证：

> 即使没有数据库，只用运行时搜索和轻量历史信息，这个 Skill 能否创造明显价值？

如果能，数据库是后续优化；如果不能，数据库也不会解决核心问题。

## 4. Phase 2 必须回答的关键问题

1. 用户为什么不用普通搜索或通用 AI 搜索，而需要这个 Skill？
2. 核心任务究竟是“找资源”还是“做选择”？
3. Tool / Skill / Tutorial / Case 是否需要固定分类？
4. 什么时候必须给官方文档，什么时候实践资源更重要？
5. “中文优先”究竟意味着什么？
6. 热度、权威、实操、ERP 相关性冲突时如何取舍？
7. 用户怎样判断一次结果成功？
8. 0 推荐什么情况下是合理结果？
9. 是否需要长期保存资源，保存的目的是什么？
10. Refresh 是产品核心，还是后续维护能力？

## 5. Phase 2 反证审查清单

产品方案出来后，至少做以下压力测试：

- **普通 Prompt 替代**：如果一条短 Prompt 已能达到大部分效果，为什么需要 Skill？
- **搜索工具替代**：如果通用搜索已经能给答案，Skill 的独特增益是什么？
- **过度治理**：某个机制是在提高推荐质量，还是只让过程更复杂？
- **历史过拟合**：换掉 V0.2–V0.4 的旧测试题后，设计是否仍成立？
- **验收迎合**：Agent 是否能靠改变字段、措辞或分类让自己看起来通过？
- **信息时效**：60 天后哪些机制仍有效，哪些会变成维护负担？
- **用户时间**：为了推荐 2 个链接，流程成本是否超过用户自己搜索？
- **空结果**：连续几个主题没有好资源时，产品是否仍然有价值？

## 6. 初步 Eval 方向

不要先测试 Skill 文件是否合法，优先测试产品结果。

### Primary：Shareability

给 10 个真实 ERP 顾问任务，每题最多推荐 2 个资源，由业务 Owner 标记：

- 值得分享；
- 一般；
- 不值得分享。

### Secondary

- Task fit
- Discovery value
- Actionability
- Trust
- Correction count
- Time-to-useful-result

### Baseline

必须和“没有 Skill、同一个 Agent 只接收普通任务 Prompt”的结果比较，否则不能证明 Skill 本身创造了增益。

## 7. 对当前 V0.4 资产的态度

### 保留作为历史资产

- V0.2–V0.4 audit；
- 回归样本；
- source/freshness 等经验；
- fork/upstream、官方冲突等真实教训。

### 不默认继承

- 四 CSV 表；
- staging/change-set 主流程；
- 全候选 Gate；
- candidate JSON；
- universal validator；
- 固定评分体系；
- autonomous mode。

这些都必须重新证明必要性。

## 8. 当前结论

> **下一步不是把 Skill 写得更严谨，而是把产品问题问得更准确。**

优秀 Skill 的共同特征是：只在模型真正需要帮助的地方提供知识；不重复模型本来就会的事情；不让脚本替代判断；按需加载上下文；通过真实任务观察行为；用用户结果决定下一轮迭代。

因此 Phase 2 应先完成产品设计与反证审查，再允许任何 Skill 重构。
