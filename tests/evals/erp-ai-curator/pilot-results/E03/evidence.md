# E03 Evidence

## 使用的 prompt（原样，未改写）

> Claude Code 接 OpenRouter 或其他第三方模型，现在有没有靠谱的配置方法？给我当前还有效的资源，不要旧教程。

## 是否独立上下文

是。baseline 与 with-skill 各由一个全新启动的独立子代理执行，互不共享上下文：

- baseline 代理未读取任何 Skill 文件；
- with-skill 代理先读取 `skills/erp-ai-curator/SKILL.md` 及 3 个 references 后再执行。

## 是否有 Web 能力

两组均具备并真实使用了 WebSearch + WebFetch，结果文件均含实际打开过的原始链接清单与失败记录。

## 推荐数量

| 组 | 最终推荐数 | 是否违反 0–2 契约 |
|---|---|---|
| baseline | 6（Anthropic 官方网关文档、OpenRouter 官方集成页、DeepSeek、智谱 GLM、Kimi、claude-code-router） | 不适用（baseline 无此契约） |
| with-skill | 2 | 否 |

## 原始链接

**baseline**

- https://code.claude.com/docs/en/llm-gateway-connect
- https://code.claude.com/docs/en/llm-gateway
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/model-config
- https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration
- https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code
- https://docs.bigmodel.cn/cn/guide/develop/claude
- https://platform.kimi.com/docs/guide/claude-code-kimi
- https://github.com/musistudio/claude-code-router

**with-skill**

- https://code.claude.com/docs/en/llm-gateway-connect
- https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration

（智谱 GLM 与 DeepSeek 官方接入页经核验有效，但按"同一套机制、只换 base URL"的去重原则未占推荐位，仅在正文中作为补充原始出处给出。）

## 高风险题是否查当前官方

本题是 EVAL_PLAN 指定的强事实核验路径，两组均查阅了当前官方文档。

- **baseline**：查阅了 Anthropic 官方 4 个页面，并交叉核对各厂商官方接入文档；实测发现两个广泛流传的文档链接已 404（OpenRouter `/docs/community/use-with-claude-code`、智谱 `/cn/guide/coding/claude_code`）。
- **with-skill**：明确触发 `volatile-fact-check.md`，命中"安装与配置 / API endpoint 环境变量 / 模型与版本兼容"三项，逐条回到官方原始页面对照。判定中文教程普遍使用的 `ANTHROPIC_SMALL_FAST_MODEL` 已被官方标注 `[DEPRECATED]`（现行写法 `ANTHROPIC_DEFAULT_HAIKU_MODEL`），据此排除全部旧教程。

## 明显异常

1. **两组都识别了同一个关键过时信号**（`ANTHROPIC_SMALL_FAST_MODEL` 已废弃），说明该题的事实核验难度对 baseline 并不构成壁垒 —— 这是判断 Skill 增益的重要对照点，供业务 Owner 评估。
2. **主要差异在收敛度而非事实准确性**：baseline 给出 6 个（覆盖三家厂商端点 + 社区路由工具），with-skill 收敛到 2 个，把厂商端点按"同一机制"去重后移出推荐位。
3. **baseline 抓取失败 4 次**：`docs.claude.com` fetch failed（后改用 `code.claude.com` 成功）、两个官方旧路径 404、GitHub HTML 页降级为 raw README。
4. **with-skill 抓取截断 1 次**：官方 env-vars 页面约 10 万字符，返回值在变量表 B/C 段之后被截断；所需变量均在已取得的 A 段内，核验目的达成，但 `CLAUDE_CODE_*` 系列变量未完整读取。
5. **with-skill 记录了一处"无法确认"**：`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` 的版本门槛（第三方称 v2.1.129+）未能在官方页面核实，已如实标注为未核实、未当作官方事实引用。
6. **官方页面普遍无"最后更新日期"字段**：with-skill 因此将"当前有效"的判定依据记为"官方站点内容自洽 + 与厂商官方文档交叉一致"，而非页面时间戳。
