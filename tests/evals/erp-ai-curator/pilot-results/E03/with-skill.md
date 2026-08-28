# Claude Code 接 OpenRouter / 第三方模型：当前还有效的配置资源

先说结论：**有，而且机制已经是官方支持的（LLM gateway 通道），但 Anthropic 明确不为"接非 Claude 模型"背书。** 下面两个是我核验到今天仍然有效的原始出处。

| 资源 | 类型 | 为什么值得看 | 能得到什么 | 重要限制 |
|---|---|---|---|---|
| **Connect Claude Code to an LLM gateway**（Anthropic 官方文档）<br>https://code.claude.com/docs/en/llm-gateway-connect | 官方文档 | 所有第三方接入（OpenRouter / DeepSeek / GLM / Kimi / 自建网关）走的是同一套机制，这一页是唯一权威口径；还给了不启动 Claude Code 就能验证的 curl 测法，和一张覆盖第三方常见报错（400 adaptive thinking、WAF 403、上下文被网关改写）的排查表 | 两个必设变量的准确写法、settings.json 与 shell 的优先级、`/status` 怎么看、以及"要不要用 `ANTHROPIC_AUTH_TOKEN` 还是 `ANTHROPIC_API_KEY`"的判断依据 | 页面定位是"企业自建网关"，不教你挑模型；且官方在 https://code.claude.com/docs/en/llm-gateway 明确写：*Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway.* |
| **Claude Code Integration**（OpenRouter 官方 Cookbook）<br>https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration | 官方文档（厂商） | 你点名要 OpenRouter，这一页是 OR 自己维护的当前值：base URL 精确到 `https://openrouter.ai/api`（多写 `/v1` 会拼成 `/api/v1/v1/messages`）、`ANTHROPIC_API_KEY` 必须显式置空、必须 `/logout` 清缓存登录，以及 Fable 不会自动出现在 `/model` 里 | 可直接复制的 shell profile 段和 `.claude/settings.local.json` 段、各档模型 pin 法、`/status` 该显示成什么样 | 属于厂商自述，不是中立评测；页面自己声明 *Claude Code with OpenRouter is only guaranteed to work with the Anthropic first-party provider*，建议把 Anthropic 1P 设为首选 provider |

## 为什么没有推荐更多

我只给了 2 个。搜到的大量中文教程（腾讯云开发者社区、CSDN、各类转载）里还在用 `ANTHROPIC_SMALL_FAST_MODEL`，而这个变量在官方 env-vars 页已标注 **[DEPRECATED]**，现行写法是 `ANTHROPIC_DEFAULT_HAIKU_MODEL`——这类正是你说的"旧教程"，直接排除。另外像 Morph 那篇"2026 Guide"是卖自家 gateway 的营销页，配置示例里把 `claude-sonnet-4-5` 映射到本地 Ollama 模型，属于厂商自述，不做推荐。

智谱 GLM 和 DeepSeek 的官方接入页我也逐字打开核验过，当前有效、且用的是现行变量，但它们和上面第 1 个资源是**同一套机制，只是换 base URL 和模型名**，按去重原则不占推荐位。你要接国产模型，直接看这两个原始出处（比我更不容易过期）：

- 智谱 GLM：https://docs.bigmodel.cn/cn/guide/develop/claude —— 当前给出 `ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic` + `ANTHROPIC_AUTH_TOKEN`，并 pin `ANTHROPIC_DEFAULT_SONNET_MODEL=glm-5.2[1m]`；官方称在 Claude Code 2.1.140 验证通过
- DeepSeek：https://api-docs.deepseek.com/zh-cn/guides/anthropic_api —— `ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic`，官方文档示例用的是 `ANTHROPIC_API_KEY`（注意：与 GLM/OpenRouter 用的 token 变量不同）；不支持的模型名会被自动映射到 `deepseek-v4-flash`

## 几个必须先知道的判断（都来自上面的官方原文）

1. **`ANTHROPIC_BASE_URL` 只改请求发往哪里，不改哪个模型回答。** 这是官方 model-config 页的原话。所以"能不能跑"取决于对端是否说 Anthropic Messages 协议，以及模型名对不对。
2. **为什么第三方模型事实上能跑、但官方不背书**：官方 model-config 页写明，在 LLM gateway 或自定义 `ANTHROPIC_BASE_URL` 之后，模型名由网关定义，Claude Code **不做校验、任何字符串直接透传**（直连 `api.anthropic.com` 时才会校验）。这是社区方案能work的原因，也是它不受支持的原因。
3. **鉴权变量按对端要求二选一**：`ANTHROPIC_AUTH_TOKEN` → `Authorization: Bearer`；`ANTHROPIC_API_KEY` → `x-api-key`。官方给的判断法是：没被告知就用 token，curl 验证返回 401 就换另一个。OpenRouter / GLM 用 token，DeepSeek 官方示例用 api key。
4. **别写进项目 `.env`**，Claude Code 原生安装不读 `.env`；写 `~/.claude/settings.json` 或 shell profile。凭据不要放进项目的 `.claude/settings.json`（会被提交）。
5. **指向非第一方 host 的副作用**（官方 env-vars 页）：MCP tool search 默认关闭（需 `ENABLE_TOOL_SEARCH=true`）；v2.1.196 起 Remote Control 被禁用；后台 agent 不保证继承 shell 里的 export，要写进 settings 文件。
6. **想在 `/model` 里看到网关自己的模型**：设 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`（官方 llm-gateway-connect 页有写）。官方页面**未标注版本门槛**；有第三方博客称需 v2.1.129+，我没能在官方页面核实到这个数字，不要当官方事实。

---

## 运行记录

**任务理解**（Skill 流程第 1 步）
- 谁要用：正在用 Claude Code 的开发者（本任务为通用可迁移场景，非 ERP 专属）
- 要完成什么动作：把 Claude Code 的推理请求改道到 OpenRouter 或其他第三方模型供应商
- 期望结果：一份当前仍生效、可直接照做的配置，明确排除已过时的旧教程

**已加载的 references**
- `references/source-strategy.md`（进入联网搜索时加载）
- `references/selection-heuristics.md`（多候选取舍时加载）
- `references/volatile-fact-check.md`（命中高风险核验时加载）

**实际使用的搜索关键词（WebSearch，共 4 组）**
1. `Claude Code OpenRouter 配置 ANTHROPIC_BASE_URL 第三方模型`
2. `Claude Code third party model provider ANTHROPIC_BASE_URL ANTHROPIC_AUTH_TOKEN official docs`
3. `Claude Code 接入 第三方模型 DeepSeek GLM Kimi 配置 2026 可行吗 官方不支持`

**实际打开并阅读正文的原始链接（WebFetch，共 6 个）**
1. https://code.claude.com/docs/en/env-vars （官方环境变量参考）
2. https://code.claude.com/docs/en/llm-gateway （官方：第三方网关声明与边界）
3. https://code.claude.com/docs/en/llm-gateway-connect （官方：连接步骤 + 排查表）→ 推荐位 1
4. https://code.claude.com/docs/en/model-config （官方：模型配置、第三方 provider pin 模型、弃用说明）
5. https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration （OpenRouter 官方 Cookbook）→ 推荐位 2
6. https://api-docs.deepseek.com/zh-cn/guides/anthropic_api （DeepSeek 官方，核验端点与鉴权变量）
7. https://docs.bigmodel.cn/cn/guide/develop/claude （智谱 GLM 官方，核验端点与现行变量）

**搜索命中但未采信为推荐对象的链接**（作为线索，未被当作可推荐来源）
- https://claude-wiki.com/environment-variables.html —— 第三方镜像站（虽标注 origin 为官方 docs），只作线索，未采信
- https://fazm.ai/t/claude-code-llm-gateway-anthropic-base-url-official-docs —— 二手复述，其"v2.1.129+"版本门槛未能核实
- https://www.morphllm.com/use-different-llm-claude-code —— 厂商营销页，含厂商自述数字
- https://www.zyte.com/blog/how-to-run-any-model-inside-claude-code/ 、https://mykolaaleksandrov.dev/posts/2026/05/using-openrouter-with-claude-code —— 个人博客，作为交叉对照（base URL 拼法一致）
- 腾讯云开发者社区 2 篇、CSDN 1 篇、devpress.csdn.net 1 篇 —— 二手转载/聚合站，且含已弃用变量

**是否触发高风险事实核验：是**

命中 `volatile-fact-check.md` 的触发项：**安装与配置**、**API / endpoint / 环境变量**、**模型与版本兼容**。因此所有涉及变量取值、base URL、模型名的内容均回到官方/厂商原始页面逐条对照，未使用训练记忆。

**核验结论**
- ✅ **通过（推荐位 1）**：`code.claude.com/docs/en/llm-gateway-connect` 与 `env-vars`、`model-config` 三页互相一致；curl 验证法、凭据变量到 header 的映射、排查表均为官方原文。
- ✅ **通过（推荐位 2）**：OpenRouter Cookbook 的 `https://openrouter.ai/api`、显式置空 `ANTHROPIC_API_KEY`、`/logout` 步骤，与官方 env-vars 页对 `ANTHROPIC_AUTH_TOKEN` / `ANTHROPIC_API_KEY` 的定义一致，无冲突。
- ✅ **通过（不占推荐位，仅作补充）**：智谱 GLM 官方页使用现行变量 `ANTHROPIC_DEFAULT_HAIKU_MODEL`；DeepSeek 官方页 base URL 与"模型名映射"规则明确。两者均与官方机制一致。
- ❌ **核验不通过 / 判定为过时**：多篇中文教程使用 `ANTHROPIC_SMALL_FAST_MODEL`，官方 env-vars 页已标注 `[DEPRECATED]`，model-config 页明确"deprecated in favor of `ANTHROPIC_DEFAULT_HAIKU_MODEL`"。按"官方已变更的旧变量教程不得推荐"处理，全部排除。
- ⚠️ **边界已记录并写入回答**：官方明言不支持通过网关路由到非 Claude 模型、不审计第三方网关。因此回答中把"能跑"与"官方支持"分开陈述，未把社区方案包装成官方能力。
- ⚠️ **无法确认项已如实标注**：`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` 的版本门槛（第三方称 v2.1.129+）未能在官方页面核实；OpenRouter 所列 `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK` 需 v2.1.96+ 为厂商文档说法，未作官方事实引用。

**遇到的异常或失败**
- `code.claude.com/docs/en/env-vars` 页面极长（约 10 万字符），返回内容在变量表 B/C 段之后被截断，仅完整取得 A 段及之前全部内容。所需变量（`ANTHROPIC_BASE_URL`、`ANTHROPIC_AUTH_TOKEN`、`ANTHROPIC_API_KEY`、`ANTHROPIC_MODEL`、`ANTHROPIC_DEFAULT_*_MODEL`、`ANTHROPIC_SMALL_FAST_MODEL`、`ANTHROPIC_CUSTOM_HEADERS`）均在 A 段内，核验目的已达成；但 C 段之后的 `CLAUDE_CODE_*` 系列变量未在本次完整读取。
- 官方页面均未显示"最后更新日期"字段，因此"当前有效"的判定依据是：官方站点内容自洽 + 与厂商官方文档交叉一致，而非页面上的时间戳。
- 联网能力正常，全程真实使用 WebSearch + WebFetch，无降级，无凭记忆编造取值。

**降级情况**：无。
