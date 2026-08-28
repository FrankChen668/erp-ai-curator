# 候选资源硬门槛（V0.4）

## 原则

Gate 是淘汰机制，不是评分维度。

- 任一必需 Gate 失败，候选不得进入 recommended。
- 不允许用高 Star、高点赞、高分或中文优先覆盖 Gate 失败。
- `unclear` 只有在不影响核心可用性时可继续；影响核心判断时转 `human_review`。

## G0 可核验性

### PASS
- canonical：能确认原始/官方身份和当前有效性；
- practical：至少读取到主要正文、README、可用字幕或关键步骤。

### REJECT / REVIEW
- 只有搜索摘要、标题、二手截图：不得 practical；
- 正文受限：candidate + human_review；
- 页面已失效且无可靠镜像/原始来源：reject。

## G1 语义契约适配

G1 不只问“相关不相关”，而是同时检查 **任务、产出、资源类型**。

搜索前必须已有：
- `user_role`
- `user_action`
- `expected_output`
- `requested_resource_types`

候选必须记录：
- `resource_type`
- `fit_sentence`
- `reroute_topic`（如错类型/错主题但资源有价值）

`resource_type` 建议枚举：
- `tool`：完整产品/应用/CLI/桌面工具；
- `skill`：可安装/加载到 Agent 的 Skill；
- `tutorial`：操作教程/视频/图文；
- `official_doc`：官方文档/官方指南；
- `case`：真实案例/厂商案例；
- `collection`：资源合集/Prompt/Skill 集合；
- `prompt_framework`：可复用 Prompt 方法框架，而非单条普通 Prompt；
- `other`。

`fit_sentence` 模板：

> 该资源是【resource_type】，帮助【角色】完成【动作】，得到【可用结果】。

### PASS
必须同时满足：
1. **task_fit**：资源主要内容直接支撑目标动作；
2. **output_fit**：资源实际交付/学习结果与 expected_output 一致；
3. **resource_type_fit**：资源客观类型属于 requested_resource_types。

### FAIL
出现以下任一情况：
- 只能说“相关、值得了解、可参考”；
- 资源解决相邻但不同的问题；
- 工具/桌面应用被误标成 Skill；
- BPM/工作流系统配置教程被当成“画业务流程图”的教程；
- 开发者扩展文档被当成顾问学习/使用教程；
- 需要 Agent 自己补出大量步骤才能映射到本主题。

失败码：
- `REJECT_TOPIC_MISMATCH`：任务或输出错配；
- `REJECT_RESOURCE_TYPE_MISMATCH`：资源类型不属于本次请求。

错配资源如果本身有价值，可以记录 `reroute_topic`，但**不能通过修改当前 topic_intent 来把它留下**。

## G2 来源与上游

### GitHub
必须记录：
- repo_full_name
- fork: true/false
- parent/source（若有）
- stars
- pushed_at / recent release（可获得时）

若 `fork=true`：
1. 必须解析 parent/source；
2. 必须比较 upstream；
3. 默认优先 upstream；
4. fork 只有在存在明确、可证据化、与本主题有关的实质优势时才可胜出，例如：新增当前需要的 provider、修复上游未合并 bug、中文本地化且持续维护。

未完成上游判断：`REVIEW_UPSTREAM_UNRESOLVED`，不得推荐。

### 文章/视频
尽量确认：
- 原作者；
- 是否转载；
- 是否存在更早的原始页面/官方说明。

洗稿/来源不明：`REJECT_PROVENANCE`。

## G3 关键事实交叉核验

只核验“会影响用户是否能用、是否该相信”的重要声明。

见 `claim-verification.md`。

### PASS
所有 critical claims 均为 `supported`；non-critical 可有少量 `unclear`，但必须不影响核心价值。

### FAIL
任一 critical claim 与当前官方/原始信息冲突：

`REJECT_FACT_CONFLICT`

不得因为教程其它部分很好而保留为 practical。

## G4 实操价值

practical 至少证明三项：
- 明确步骤/操作序列；
- 前置条件；
- 可观察结果；

最好还包含：失败处理、版本说明、截图/代码、限制。

只有成品展示、营销介绍、理念文章：不得 practical。

## G5 时效与可用性

### volatile
必须核对当前官方状态、版本或配置。

### evolving
至少检查最近维护/Release/主要兼容性声明。

### stable
时效权重较低，但失效链接、废弃项目仍需处理。

## Gate 结果结构

每个候选至少记录：

```json
{
  "candidate_url": "...",
  "resource_type": "tool|skill|tutorial|official_doc|case|collection|prompt_framework|other",
  "requested_resource_types": ["skill", "tutorial"],
  "gate_topic_fit": "pass|fail",
  "gate_output_fit": "pass|fail",
  "gate_resource_type_fit": "pass|fail",
  "gate_provenance": "pass|review|fail",
  "gate_claims": "pass|review|fail|not_applicable",
  "gate_practicality": "pass|fail|not_applicable",
  "gate_freshness": "pass|review|fail",
  "gate_result": "pass|review|reject",
  "rejection_code": "",
  "evidence": ["short fact 1", "short fact 2"]
}
```

`gate_result != pass` 的候选不得进入推荐评分。
