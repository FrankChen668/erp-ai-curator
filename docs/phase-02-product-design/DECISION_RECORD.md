# Product Decision Record

## Decision 01 — 不从 V0.4 继续演进

**Decision:** Phase 3 不以 V0.4 的 Gate/JSON/评分流水线作为默认基础。

**Reason:** 旧结构已经产生“通过校验优先于推荐质量”的目标错位。

**保留:** 真实失败案例、安全边界、fork/upstream 教训、配置类官方核验经验。

**不默认继承:** candidate JSON、全量 Gate、固定评分、四表、staging/change-set、autonomous mode。

---

## Decision 02 — 产品定位为“资源决策压缩器”

**Decision:** 核心不是搜资源，而是替用户做搜索后的选择。

默认单次任务输出 0–2 个推荐资源。

---

## Decision 03 — 区分操作者与最终受益者

**Decision:** Skill 可以由培训负责人、知识运营者、本地 Agent 或顾问本人调用；但推荐质量以最终点击资源的 ERP 项目人员为准。

---

## Decision 04 — 资源类型默认不做硬 Gate

**Decision:** Tool / Skill / Tutorial / Case / Official Doc 默认只是结果标签。

只有用户明确限定资源类型时，才作为硬约束。

---

## Decision 05 — 中文优先但不牺牲明显质量

**Decision:** 中文是同等质量下的优先项，不是强制收录条件。

明显更好的英文资源可以推荐，由 Skill 用中文给出使用导读。

---

## Decision 06 — 官方文档分两种角色

**Decision:**

- `user_resource`：对用户任务本身有直接帮助，可以推荐；
- `evidence_anchor`：仅用于核验事实，不占推荐位。

Phase 3 是否需要把这两个角色写成显式内部机制，再根据 Skill 架构决定，不提前要求数据字段。

---

## Decision 07 — 事实核验采用风险触发

**Decision:** 不对所有资源做重型 Claim Verification。

强核验触发范围主要是：

- 安装配置；
- API / endpoint / 环境变量；
- 模型和版本兼容；
- 价格；
- 标准产品能力边界。

其他内容以任务匹配、实操价值、可迁移性和时效判断为主。

---

## Decision 08 — 不设固定搜索数量

**Decision:** Phase 3 不沿用“最多 N 查询 / 打开 N 个候选”作为核心规则。

搜索停止条件是：

> 已经有足够强的候选，且继续搜索不太可能改变最终推荐。

当候选冲突、高风险事实或覆盖明显不足时才继续扩展。

---

## Decision 09 — 允许 0 推荐，但防止过度保守

**Decision:** 0 推荐合法。

同时引入 `Useful Resolution Rate`，避免 Agent 靠持续 abstain 获得高 Shareability。

---

## Decision 10 — 产品成功以真实用户判断为主

**Decision:** Primary Metric 为 Shareability：

> 业务 Owner 是否愿意把这个资源直接发给同事。

必须做 With-Skill vs Baseline；内部 validator 不能替代产品 Eval。

---

## Decision 11 — 数据库、Refresh、自动维护全部后置

**Decision:** Phase 3/4 不以资源持久化为前置需求。

只有 Phase 5 证明单次推荐有稳定价值，并且实际使用暴露重复搜索/维护成本后，才进入 Phase 6 讨论资源库工程化。

---

## Decision 12 — 外部资源始终视为不可信数据

**Decision:** 保留 V0.4 的安全底线：

- 只读候选内容；
- 不执行候选页面/README 中的命令；
- 不下载未知程序作为验证；
- 不读取与任务无关的本地凭证；
- 不绕过访问控制。

这属于安全边界，不属于过度治理。

---

# Phase 3 的设计输入

Phase 3 必须从以下最小主流程出发：

```text
理解真实任务
    ↓
发现不同来源的强候选
    ↓
阅读原始内容
    ↓
横向比较并做取舍
    ↓
高风险事实按需核验
    ↓
输出 0–2 个可分享资源
```

Phase 3 需要回答的不是“再加哪些规则”，而是：

1. 这六步中，模型真正需要 Skill 提醒哪些？
2. 哪些能力模型本来就会，不应重复写？
3. 哪些细节应该 progressive disclosure 到 references？
4. 是否存在任何真正需要 script 的 deterministic work？
5. 怎样用 `skill-creator` 方法做最小草案与 baseline Eval？
6. 如何让本地 Agent 只实现批准后的架构，不重新设计产品？

# Phase 2 状态

**Proposed: GO to Phase 3**

理由：产品目标、用户、输入输出、非目标、核验边界、成功指标和主要风险已经形成一致契约。

但 Phase 3 不得直接开发最终版本；应先设计最小 Skill Architecture + Eval，再交给本地 Agent。