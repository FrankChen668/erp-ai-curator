# Validation Protocol V2 — Real-task first

## 1. 为什么重写验证协议

之前两种验证都不够可靠：

- Phase 4：过早验证 Skill + 本地 Agent A/B，执行噪声淹没产品问题；
- Cloud Batch 01：任务主要由我们自己挑选，同一 Agent 出题、搜索、筛选、总结，存在自证循环。

V2 只验证一件事：

> **面对真实 ERP 工作问题，资源决策方法是否稳定减少用户搜索和判断成本。**

## 2. Task provenance 是第一字段

每个任务必须标明来源：

- `REAL_USER`：来自真实顾问 / PM / 开发人员的原始问题
- `OWNER_REAL`：项目负责人真实遇到的问题
- `REPRESENTATIVE`：为角色覆盖或边界测试设计
- `SYNTHETIC`：纯测试构造

产品 Go / No-Go 主要看 `REAL_USER + OWNER_REAL`。

不得把 REPRESENTATIVE / SYNTHETIC 的表现包装成真实用户验证。

## 3. Role coverage

在宣布“产品方法验证通过”前，至少需要来自三类角色的真实问题：

- 实施 / 业务顾问
- 项目经理
- 开发人员

建议首个有效样本集：每类至少 3 个真实问题，总数至少 9 个。

如果某角色确实没有需求，可以根据真实数据收缩范围，而不是人为补题。

## 4. 每题只做最小记录

```text
Task ID
Source: REAL_USER / OWNER_REAL / REPRESENTATIVE / SYNTHETIC
Role
Original problem
Need external resource? yes/no
Final recommendation: 0–2
Why these
Critical limitation
Owner judgement: worth sharing / maybe / not worth sharing
Observed use (if available): clicked / tried / shared / ignored
Failure reason (only if failed)
```

不引入统一评分、候选 JSON 或 Gate。

## 5. 一个重要前置判断：是否需要 Curator

不是所有真实问题都应该进入资源搜索。

先判断：

> 当前用户需要的是“直接答案/直接执行”，还是“找外部资源来完成任务”？

如果前者，Curator 应退出。

这项判断本身也是未来 Skill trigger 的关键验证内容。

## 6. 资源选择协议

当任务确实需要外部资源：

1. 理解完整任务意图，不能只匹配关键词或资源类型；
2. 多源搜索；
3. 最终候选必须打开原始内容；
4. 对 Skill / Tool 要读与当前任务相关的 linked / bundled materials；
5. 比较完整 task fit、实际产出、差异化、关键限制；
6. 配置/API/版本/价格/能力边界等高风险事实回当前官方或原始来源核验；
7. 默认输出 0–2 个；相邻资源不占正式推荐位。

## 7. 成功证据分三层

### L1 — Shareability

业务 Owner 是否愿意直接把该结果发给同事：

- 值得分享
- 一般
- 不值得分享

### L2 — Behavior

有条件时记录真实行为：

- 点击
- 收藏
- 实际尝试
- 转发给同事
- 后续继续询问

行为证据比“我们觉得不错”更强。

### L3 — Skill uplift

只有 L1/L2 证明产品方法有价值后，才重新实现 Skill，并用 fresh tasks 比较：

- ordinary prompt
- with Skill

A/B 只回答“Skill 是否值得存在”，不回答“产品需求是否存在”。

## 8. Go / No-Go 不再用单一 8/10 阈值

`8/10` 可以作为观察值，但不能单独触发开发。

进入 Skill 固化至少需要同时满足：

1. 有真实来源任务，而非主要靠自造题；
2. 三类目标角色至少已有初步证据，或数据明确支持缩窄角色范围；
3. 多数真实任务的推荐被认为值得分享，且没有反复出现严重错配；
4. 0 推荐不是主要逃避策略；
5. 产品 Owner 能指出至少若干“如果没有 Curator，我本来会花更多时间搜索/判断”的具体案例。

## 9. 当前 Batch 01 的位置

`validation/cloud-batch-01` 重新定义为 **Exploratory Discovery Batch**：

- 可以沉淀候选资源；
- 可以暴露选择启发式；
- 可以做未来真实任务的参考；
- 不能作为产品验证通过证据；
- 不能直接授权 Skill 实现。

## 10. 云端与本地职责

云端负责：研究、搜索、判断、文档、GitHub、后续 Skill 设计与实现（能直接完成的部分）。

本地低能力 Agent 不再承担：

- 产品判断
- Eval 设计
- 证据解释
- 是否 PASS 的决定

只有未来确实需要本地运行、环境测试或机械批处理时才使用，并且不能成为关键决策链路。
