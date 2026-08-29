# Validation Protocol V3 — AI Leverage First

> Current validation protocol. Supersedes V2 for new evidence. V2 remains historical evidence of the resource-first phase.

## 1. 验证什么

V3 不再验证：

> “能不能给真实任务找到 0–2 个资源？”

而验证：

> **面对真实泛 ERP / 企业信息化任务，是否能更快判断出合适的 AI 工作方式，并减少不必要的工具试错、搜索、重复建设和学习成本？**

资源推荐只是可能结果之一。

## 2. 输入必须是真实任务

每条任务标明来源：

- `REAL_USER`：真实从业者原始问题；
- `OWNER_REAL`：项目负责人真实遇到的问题；
- `REPRESENTATIVE`：边界测试；
- `SYNTHETIC`：纯测试。

产品结论主要依据 `REAL_USER + OWNER_REAL`。

不把后两类包装成真实需求。

## 3. 不做人为角色配额

泛 ERP 用户可以来自：

- 实施 / 业务顾问；
- 项目经理；
- 产品 / 解决方案人员；
- 开发人员；
- 其他企业信息化角色。

验证时记录真实角色分布，但不为了“矩阵完整”人为补题。

如果真实问题长期集中在某几类角色，产品边界应跟着证据收缩或扩展。

## 4. 每题最小记录

```text
Task ID
Source
Role（已知才填）
Original problem（保留原文）
Desired outcome / hard constraints（能直接从原问题得到才填）
Current baseline（用户现有 AI / Agent / toolchain，已知才填）
AI leverage diagnosis
Mode: A / B / C
Recommendation / working approach
Why
Critical limitation（有则填）
Owner judgement: worth using / maybe / not useful
Observed use（有则记录）
Failure reason（失败才填）
```

不引入统一数字评分、candidate JSON 或 Gate。

## 5. 先判断用户是在“执行任务”还是“选择 AI 工作方式”

### 直接执行

例如：

- “帮我分析这段代码。”
- “帮我写周报。”
- “解释这个业务流程。”

Curator 不抢占。

### AI 工作方式探索

例如：

- “这个需求分析怎么用 AI 做得更好？”
- “我想快速理解这个陌生系统，有没有合适的 AI 做法？”
- “这个事情值得装 Skill 吗？”

进入 V3。

### 明确资源发现

例如：

- “帮我找一个 editable draw.io Skill。”

可以走 fast path，但仍需判断该外部方案相比用户当前工具链是否有真实增量价值。

“用户明确说要 Skill”不是自动 Mode B。

判断边界不是关键词，而是用户意图。

## 6. 三种 Mode

### Mode A — 当前工具链足够

判断新增专门 Tool / Skill 不会显著改善结果。

成功表现：

- 不为了展示能力而搜索；
- 优先复用用户现有 AI / Agent / 内部工具；
- 给出一个简洁可执行的现有工具使用方式；
- 专业 ERP / 代码 / 配置知识尽量 source-grounded；
- 能解释为什么不值得增加工具复杂度。

### Mode B — 专门方案有明显增益

先定义当前 baseline 缺失的能力，再定向搜索。

成功表现：

- 搜索围绕一个明确能力缺口；
- 候选来自适合问题的来源，不固定“官网优先”；
- 正式推荐默认 1 个主方案，确有差异时最多再给 1 个；
- 明确相比现有工具链的增量价值；
- 给出怎么开始和关键限制；
- 数据、源码、账号、权限、本地/云端等企业约束不冲突。

### Mode C — 暂不值得复杂化

证据不足以支持专门方案，但存在值得试验的方向。

成功表现：

- 优先用现有 Agent / 工具做低成本试验；
- 明确什么信号出现后再升级；
- 不把“可能有用”包装成成熟推荐。

Mode C 必须同时包含一个最小试验和一个 upgrade signal。

## 7. Mode B 的发现协议

只有 Mode B 需要发现外部方案时：

1. 明确当前 baseline 与能力缺口；
2. 搜索不同来源中真正可能解决它的候选；
3. 最终候选必须打开原始内容；
4. 对 Tool / Skill 读取与任务相关的 linked / bundled materials；
5. 比较完整 task fit、实际产出、相对现有栈的增量价值、启动成本、差异化、限制；
6. 检查数据 / 源码 / 本地云端 / 权限等硬约束；
7. 安装 / 配置 / API / Endpoint / 环境变量 / 价格 / 版本 / 模型兼容 / 原生能力等高波动事实回当前官方或原始来源核验；
8. 准备给 0 正式推荐时，换一种来源类型或搜索表达做一次反证式搜索，防止过早放弃；
9. 结论稳定后停止，不设固定查询次数。

## 8. 过去发现的资源怎么用

历史 Starter Pack / 已知项目只能作为搜索先验：

> “这个方向可能值得先看。”

不能直接作为答案。

尤其是配置、模型、API、版本类资源必须运行时重新确认。

如果用户当前已有同等或更合适的内部/已批准工具，历史外部资源不应因为“仓库里已经收录”就进入推荐位。

## 9. 成功证据

### L1 — Usefulness

Owner 判断：

- `worth using`：愿意直接采用 / 分享这种工作方式；
- `maybe`：有启发但还不足以实际采用；
- `not useful`：没有减少决策或试错成本。

### L2 — Behavior

有真实反馈时记录：

- 直接尝试；
- 安装 / 配置；
- 收藏；
- 转发；
- 在项目中重复使用；
- 复用现有工具而避免新增依赖；
- 明确放弃某个不必要工具。

“被劝退一个不必要的复杂方案”同样是有效行为结果。

### L3 — Skill uplift

只有 V3 工作模型被真实任务证明有价值后，才验证是否值得封装成 Skill。

A/B 比较的是：

- ordinary AI conversation；
- with Skill working model。

A/B 只回答“Skill 封装有没有额外增益”，不能反过来证明产品问题存在。

## 10. 失败类型只做诊断，不做 Gate

出现失败时标一个最接近的原因即可：

- TASK_MISREAD：没理解用户真正工作结果；
- BASELINE_MISREAD：没识别用户已有工具/能力；
- OVER_TOOLING：现有工具链已经够，却强推新工具；
- UNDER_DISCOVERY：确实存在高价值专门方案但没发现；
- WEAK_FIT：推荐只相关、不解决完整任务；
- STALE_FACT：关键动态事实过时；
- OVER_RESEARCH：为了回答简单问题做无止境搜索；
- PREMATURE_ABSTAIN：过早说没有；
- CONSTRAINT_MISS：忽略数据、源码、权限或环境限制；
- COMPLEXITY_DRIFT：为了一个问题引入不必要流程/规则。

重复出现的失败才有资格改变 Skill 设计。

## 11. 何时允许重新实现 Skill

不设机械的 `8/10`、`9 个样本` 等门槛。

只有出现以下证据组合时才值得封装：

- 多个真实任务中，AI 杠杆诊断本身反复有价值；
- 能正确比较“用户当前栈”与“新增专门方案”；
- Mode A/B/C 的判断能明显减少错误工具选择；
- Mode B 的推荐能让用户更快开始工作；
- 普通 AI 对话经常遗漏这些判断，而稳定工作模型能改善；
- 没有依赖大量场景硬编码和资源预置。

如果普通 AI 已经自然做得一样好，不为了“项目完整”强行做 Skill。

## 12. 云端与本地职责

云端直接完成能完成的：研究、判断、Web/GitHub 检索、文档、设计、验证。

本地 Agent 只有在必须访问本地环境、运行具体工具或做机械验证时才参与；不承担产品判断和是否 PASS 的决定。
