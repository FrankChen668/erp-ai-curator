# 执行契约

## 默认输入

### discover

必需：一个明确主题，例如“Claude Code 第三方模型配置”或“ERP 顾问业务流程图 Skill”。

默认：
- autonomy=`review-first`
- max_queries=8
- max_fetches=12
- preferred_language=`zh-CN`
- allow_english_fallback=true

执行前必须先形成：
- `topic_intent`
- `out_of_scope`

### refresh

需要已有 `resources/topics/recommendations` 数据，以及一个 topic_id、主题名或“全部 volatile 主题”。

### audit

只需已有数据文件，不要求联网；如果有联网能力，可同时做失效/时效检查。

### bootstrap

需要一组主题或项目阶段范围。每个主题仍独立执行 discover；不得一次搜索后批量粗分所有主题。

## 默认输出

不要输出长报告。输出：

1. 本主题候选数 / Gate 淘汰数；
2. 0–2 个拟推荐资源；
3. 每条原始链接 + 证据化短理由；
4. 必要的 `human_review` 项；
5. `proposed_changes`；
6. 一条 run 记录。

逐候选 claim table / Gate 细节默认保存在 staging 审计记录中，不需要全部展示给最终用户。

## 候选状态机

固定为：

`discovered → content_checked → gate_passed → scored → compared → recommended`

失败分支：

`discovered/content_checked → rejected`

不确定分支：

`discovered/content_checked → human_review`

禁止跳过 `gate_passed` 直接进入 `scored/recommended`。

## 自治级别

### review-first（默认）

- 可自动搜索、核验、淘汰、评分、排序、生成变更集；
- 不直接覆盖正式推荐表；
- 适合新 Skill、新模型、新运行时。

### autonomous

仅在用户明确允许，且目标 Agent 已跑过关键 eval 后启用。

自动提交必须满足：
- 记录结构有效；
- 推荐资源所有 Gate PASS；
- 推荐资源核验等级合格；
- 无 critical claim conflict；
- GitHub fork 已完成 upstream 判断；
- 无 `human_review=true`；
- 无访问/来源争议；
- 更新前已备份；
- 更新后校验通过。

## 幂等性

- resource_id 必须由规范化 URL 稳定生成；同 URL 多次运行不能生成新资源。
- topic_id 必须由规范化 topic_key 稳定生成。
- recommendation 必须按 `topic_id + resource_id + slot` 去重。
- refresh 不能因为一次重跑制造新的重复记录。

## 成本与停止

默认单主题最多 8 个搜索查询、12 个正文抓取。

满足覆盖目标后，如果连续两类新查询都没有出现能进入同槽前二的 Gate-PASS 候选，停止扩展。

用户要求深度研究时才扩大预算。

## 禁止的“完成偏差”

以下行为视为执行失败：

- 为了完成 N 个主题而降低 Gate；
- 为了输出两条推荐而保留次品；
- 先写推荐理由，再反向寻找证据；
- 把“没有好资源”当作失败；
- 把系统适配/加脚本/写数据库计划当作实际采编产出。
