# Success Metrics

## 1. 为什么不能再用“0 ERROR”作为成功标准

结构校验只能证明：

- 文件格式合法；
- 字段存在；
- 脚本规则被满足。

它不能证明：

- 推荐真的好；
- 用户愿意点击；
- 比普通搜索更省时间；
- Agent 没有通过改标签迎合校验器。

因此工程指标只能作为辅助证据，不能成为产品主验收。

## 2. Primary Metric — Shareability

每个真实任务默认最多输出 2 个资源，由业务 Owner 对每条资源标记：

- **值得分享**：我愿意直接转发给同事；
- **一般**：有一定价值，但不会主动推荐；
- **不值得分享**：错配、太泛、过时、营销、事实问题或不够实操。

### 目标

首轮产品验收目标：

> 推荐资源中，`值得分享` 占比达到 **80% 或以上**。

这是一个阶段目标，不是永久 SLA；Phase 5 可根据样本结果校准。

## 3. Guardrail — Useful Resolution Rate

只看 Shareability 会鼓励 Agent “什么都不推荐”。因此必须同时衡量任务是否被有效解决。

一个任务记为 `resolved`，满足任一条件：

1. 至少有 1 个资源被业务 Owner 标记为“值得分享”；
2. Skill 返回 0 推荐，且业务 Owner 同意“这轮确实没有够格资源，保持空缺是正确决定”。

首轮目标：

> 10 个真实任务中至少 **7 个 resolved**。

这样既允许合理 abstain，又不能靠持续留空获得高质量分。

## 4. Baseline Uplift — Skill 必须证明自己有必要存在

同一批任务必须做两组：

### Baseline

同一个 Agent，不加载 ERP AI Curator Skill，只给普通自然语言任务。

### With Skill

同一个 Agent、同等可用工具，加载 ERP AI Curator Skill。

比较：

- Shareability；
- Useful Resolution Rate；
- 用户纠正次数；
- 结果冗余程度；
- 明显错配/过时/事实冲突数量。

### Go 条件

Skill 至少应满足：

- Shareability 明显高于 baseline；
- 且 Useful Resolution Rate 不低于 baseline；
- 且严重错配/事实冲突不高于 baseline。

如果结果接近，应优先简化 Skill，而不是通过增加规则制造“看起来有差异”。

## 5. Secondary Metrics

### Task Fit

业务 Owner 判断：

- 直接解决；
- 部分相关；
- 错题。

### Actionability

资源是否让用户知道下一步能做什么：

- 可直接操作；
- 可作为有效参考；
- 只有概念/宣传。

### Discovery Value

Skill 是否找到用户自己普通搜索不容易发现、但确实有价值的内容。

注意：冷门不等于有价值。

### Trust

是否存在：

- 链接/标题错误；
- 类型冒充；
- 当前配置冲突；
- 厂商自述被写成客观事实；
- 官方锚点被包装成实操推荐。

### Correction Count

业务 Owner 为得到可用结果，需要纠正 Agent 几次：

- 0 次；
- 1 次；
- 2 次及以上。

### Concision

默认是否把结果控制在真正值得看的 0–2 个，而不是把候选列表转嫁给用户。

## 6. 初始 Eval Set 设计

Phase 3 先建立 10 个真实任务，至少覆盖：

1. 业务流程图 Skill；
2. 原型设计实操教程；
3. Claude Code 第三方模型配置；
4. Codex / 本地 Agent 实用配置；
5. SAP 需求调研 / Fit-to-Standard；
6. Oracle 需求/方案工作；
7. SAP 陌生模块快速学习；
8. Oracle 陌生模块快速学习；
9. 一个明确限定资源类型的任务；
10. 一个故意资源稀缺、正确结果可能为 0 的任务。

不要只复用 V0.4 已经针对性修过的 5 道题，否则会过拟合历史失败。

## 7. 失败分类

产品 Eval 失败后先分类，再决定是否改 Skill：

- `TASK_UNDERSTANDING`：理解错用户真正任务；
- `SEARCH_COVERAGE`：没有找到强候选；
- `WEAK_SELECTION`：找到但选错；
- `TYPE_CONFUSION`：资源类型判断错误；
- `FRESHNESS`：过时；
- `FACT_CONFLICT`：关键事实错误；
- `OVER_RECOMMEND`：凑数/输出过多；
- `OVER_ABSTAIN`：过度保守；
- `LANGUAGE_BIAS`：为了中文牺牲明显质量；
- `PROCESS_OVERHEAD`：为了简单推荐付出过重流程成本。

只有反复出现的失败模式才值得固化成 Skill 机制。

## 8. 工程检查的位置

以下检查仍然有价值，但属于 Phase 4/5 的工程护栏：

- SKILL.md frontmatter 合法；
- references 链接有效；
- scripts 可运行；
- 输出格式可解析；
- deterministic helper 测试通过。

它们回答“实现有没有坏”，不回答“产品有没有价值”。