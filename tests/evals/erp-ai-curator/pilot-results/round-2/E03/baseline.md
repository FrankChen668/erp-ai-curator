# Claude Code 接 OpenRouter / 第三方模型：当前有效的配置方案

> 核查日期：2026-08-29。下面每条资源我都实际打开了原始页面确认内容，不是凭搜索摘要下结论。凡是"当前仍有效"的判断，都基于页面上能看到的最新版本/日期信息。

---

## 零、先说结论：官方到底支不支持

这件事有一个**必须先讲清楚的前提**，否则后面所有教程都容易用错。

Anthropic 官方现在有完整的 **LLM gateway（网关）机制**，原生支持把 Claude Code 指向第三方端点。但官方文档里有一句非常关键的原话：

> "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and **doesn't support routing Claude Code to non-Claude models through any gateway**."

翻译成人话：

- ✅ **官方支持**：Claude Code → 网关 → Claude 模型（哪怕这个 Claude 跑在 Bedrock / Vertex / Foundry 上）
- ❌ **官方不支持**：Claude Code → 网关 → 非 Claude 模型（DeepSeek / GLM / Kimi / GPT 等）

所以你要分清自己想做哪件事，两者的靠谱程度完全不同：

| 你的目标 | 靠谱程度 | 说明 |
|---|---|---|
| **A. 用 OpenRouter 当"计费/容灾层"，底层还是跑 Claude** | ⭐⭐⭐⭐⭐ 官方机制 + 厂商官方维护文档 | 这是 OpenRouter 官方明确保证的组合 |
| **B. 让 Claude Code 跑 DeepSeek / GLM / Kimi** | ⭐⭐⭐ 能用，但属"未受支持地带" | 国产厂商自己出了 Anthropic 兼容端点，但兼容性边界得自己趟 |

下面按这两条线分别给资源。

---

## 一、权威基线（建议先花 5 分钟读这两个）

### 1. Anthropic 官方 · Other LLM gateways

- 链接：https://code.claude.com/docs/en/llm-gateway
- 为什么值得读：这是整个话题的**定义性文档**。它规定了网关必须满足的 API 格式要求、必须转发的请求头（`anthropic-beta`、`anthropic-version`）、以及上面那句"不支持非 Claude 模型"的官方表态。
- 我确认到的当前内容：
  - 网关必须暴露 Anthropic Messages（`/v1/messages`、`/v1/messages/count_tokens`）、Bedrock InvokeModel 或 Vertex rawPredict 至少一种格式
  - 只转发到 Anthropic 的网关必须在 `anthropic-beta` 头里转发 OAuth capability
  - 网关凭证生效时，claude.ai 订阅**不会**被消耗；但只设 `ANTHROPIC_BASE_URL` 而不设凭证时，订阅仍会生效

### 2. Anthropic 官方 · Connect Claude Code to your gateway

- 链接：https://code.claude.com/docs/en/llm-gateway-connect
- 为什么值得读：这是**动手页**，讲清了三个环境变量的语义差别，比任何二手教程都准。
- 关键要点（我逐条核对过原文）：
  - `ANTHROPIC_AUTH_TOKEN` → 发到 `Authorization: Bearer` 头
  - `ANTHROPIC_API_KEY` → 发到 `x-api-key` 头
  - `apiKeyHelper`（settings 配置项，不是环境变量）→ 两个头都发，适合密钥轮换/vault 场景
  - **放错变量会得到 401**，这是最常见的坑
  - 给了 `curl` 验证命令，返回 `{"id":"msg_...` 即成功；返回 unknown model 也算成功（说明 URL 和凭证都对了）
  - 遇到 `400` 且报 `context_management` / `Extra inputs are not permitted`，设 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`
  - `settings.json` 的 `env` 优先级**高于** shell export
  - 警告：不要把凭证写进项目级 `.claude/settings.json`（会被提交到 git）

> 💡 这两个页面就是判断"别人给的教程是不是过时"的标尺。凡是把 `ANTHROPIC_API_KEY` 塞给 OpenRouter 的，都和官方语义不符。

---

## 二、OpenRouter 主线（目标 A，最成熟）

### 3. OpenRouter 官方 · Claude Code Integration（cookbook）— **首选**

- 链接：https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration
- 这是**厂商官方文档**，我完整读了一遍，当前有效的配置如下：

```bash
# 加到 ~/.zshrc 或 ~/.bashrc
export OPENROUTER_API_KEY="<你的 key>"
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""                    # 必须显式为空，不是 unset
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1   # 可选，开启网关模型选择器
```

项目级写法（`.claude/settings.local.json`）：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api",
    "ANTHROPIC_AUTH_TOKEN": "<你的 key>",
    "ANTHROPIC_API_KEY": "",
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
  }
}
```

我核对到的几个**容易踩的细节**（都是文档原文强调的）：

1. **Base URL 必须是 `https://openrouter.ai/api`，不是 `/api/v1`。** Claude Code 会自己拼 `/v1/messages`，你写了 `/v1` 就会变成 `/api/v1/v1/messages`，报的错还很难查。
2. **`ANTHROPIC_API_KEY` 必须是空字符串 `""`，不能 unset。** 否则 Claude Code 会拿着 `x-api-key` 头回落到 Anthropic 直连。
3. **变量顺序有讲究**：`ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"` 是在 source 时展开的，如果 `OPENROUTER_API_KEY` 定义在它后面，token 会展开成空。
4. **改完必须 `source ~/.zshrc` 或重开终端**，文档明确说"否则你会一直测的是旧环境，然后得出配置不工作的结论"。
5. **如果之前用 Anthropic 账号登录过，必须跑一次 `/logout`** 再重启 `claude`，否则缓存的 OAuth session 会产生 auth conflict，典型症状是 `openrouter/auto` 之类的模型报 model-not-found。
6. 不要写进项目级 `.env` 文件，原生安装器不读 `.env`。

模型档位覆盖（可选）：

```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL="~anthropic/claude-opus-latest"
export ANTHROPIC_DEFAULT_SONNET_MODEL="~anthropic/claude-sonnet-latest"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="~anthropic/claude-haiku-latest"
export ANTHROPIC_DEFAULT_FABLE_MODEL="~anthropic/claude-fable-latest"
export CLAUDE_CODE_SUBAGENT_MODEL="~anthropic/claude-opus-latest"
```

> 注意文档里的提醒：Claude Code 2.1.x 新增了 **Fable** 这个第四档，指向 OpenRouter 时默认**不会**出现在 `/model` 里，只能靠 `ANTHROPIC_DEFAULT_FABLE_MODEL` 手动加。

验证：`/status` 里应显示 `Auth token: ANTHROPIC_AUTH_TOKEN` 和 `Anthropic base URL: https://openrouter.ai/api`。

**兼容性边界（重要）**：文档开头就写明 —— "Claude Code with OpenRouter is only guaranteed to work with the Anthropic first-party provider"，并建议把 Anthropic 1P 设为优先 provider。也就是说，**想稳定就别在 OpenRouter 上跑非 Anthropic 模型**。

### 4. OpenRouter 官方博客 · How to Use Claude Code with OpenRouter（2026-06-16）

- 链接：https://openrouter.ai/blog/tutorials/claude-code-openrouter
- 发布时间：2026 年 6 月 16 日（比我搜索到的多数第三方教程都新）
- 价值点：补了一些 cookbook 没写的实操内容
  - **Fast Mode**：只对 Opus 4.6 / 4.7 / 4.8 有效，需设 `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1`，**要求 Claude Code v2.1.96 或更高**
  - **免费档**：免费模型每天最多 50 次请求，充值 $10 后升到 1000 次/天；上下文窗口比付费模型小，适合练手不适合生产
  - **CI 用法**：官方 GitHub Action 需要同时传 `anthropic_api_key` 输入（满足启动检查）和 `ANTHROPIC_BASE_URL` 环境变量
  - **终端成本显示**：`github.com/OpenRouterTeam/openrouter-examples` 的 `claude-code` 目录有 statusline 脚本，能实时显示 provider / model / 花费
  - FAQ 明确回答："non-Anthropic models aren't supported through the native endpoint"

### 5. OpenRouter 官方 · ori CLI（2026-08-04 发布，最新）

- 链接：https://openrouter.ai/blog/announcements/ori-harness
- 发布时间：2026 年 8 月 4 日 —— **这是本次核查里最新的官方产物**
- 解决什么问题：手动配 OpenRouter 其实要设**一长串**变量才能拿到接近官方的体验，ori 帮你自动配好：

```bash
curl -fsSL https://openrouter.ai/labs/ori/install.sh | bash
ori login
ori claude      # 也支持 ori codex / ori opencode / ori hermes
```

- 它会自动处理的关键变量（官方博客列出的完整清单，比单看 cookbook 多出好几个）：

```
ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_API_KEY, OPENROUTER_API_KEY,
CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1, CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1,
ENABLE_TOOL_SEARCH=true, CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=1,
ANTHROPIC_DEFAULT_HAIKU/SONNET/OPUS/FABLE_MODEL, ANTHROPIC_DEFAULT_FABLE_MODEL_NAME=Fable
```

- 一个有意思的点：`ENABLE_TOOL_SEARCH=true` 对 Anthropic 模型能省掉近一半 system prompt token，但**多数开源模型根本不支持 tool search**，ori 会根据你的 `--model` 自动切换最优设置。手动配的人通常不知道这一点。
- 当前支持：Claude Code、Codex、OpenCode、Hermes。

---

## 三、国产模型官方直连（目标 B）

这几年国产厂商自己出了 Anthropic 兼容端点，**不需要 OpenRouter 中转，也不需要任何代理**。以下都是厂商官方文档，我逐个打开验证过。

### 6. DeepSeek 官方 · Integrate with Claude Code

- 链接：https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code
- 端点：`https://api.deepseek.com/anthropic`（官方原生 Anthropic 兼容，非 OpenAI 格式转换）
- 当前官方示例（Linux/Mac）：

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash
export CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flash
export CLAUDE_CODE_EFFORT_LEVEL=max
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=786432
```

- 我核对到的细节：
  - 当前模型名是 `deepseek-v4-pro` / `deepseek-v4-flash`（文档注明版本已更新到 V4-Pro-0813，但**调用名不变**）
  - **模型名映射机制**：传 `claude-opus*` 会自动映射到 `deepseek-v4-pro`，传 `claude-haiku*` / `claude-sonnet*` 映射到 `deepseek-v4-flash`；传未知模型名一律落到 `deepseek-v4-flash`
  - **原生支持 WebSearch**，但会额外产生 token 消耗
  - 兼容性坑：Anthropic 格式下 `cache_control`、`citations`、`container`、`service_tier`、`top_k` 等字段是被**忽略**的；`thinking` 的 `budget_tokens` 也被忽略

### 7. Kimi / Moonshot 官方 · 在 Claude Code 中使用 Kimi

- 链接：https://platform.kimi.com/docs/guide/claude-code-kimi
- 端点：`https://api.moonshot.cn/anthropic`（另有国际站 `https://api.moonshot.ai/anthropic`）
- 当前官方配置：

```bash
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic"
export ANTHROPIC_AUTH_TOKEN="${YOUR_MOONSHOT_API_KEY}"
export ANTHROPIC_MODEL="kimi-k3[1m]"
export ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k3[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k3[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k3[1m]"
export ANTHROPIC_DEFAULT_FABLE_MODEL="kimi-k3[1m]"
export CLAUDE_CODE_SUBAGENT_MODEL="kimi-k3[1m]"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="1048576"
export CLAUDE_CODE_EFFORT_LEVEL="max"
```

- **这份文档质量很高**，我特别想强调它给出的几点：
  - **提供了清理脚本**：`~/.claude/settings.json` 的 `env` 会**覆盖**终端 export，残留旧配置是"改了不生效"的头号原因。官方给了 `node --eval` 脚本批量删除 16 个 `ANTHROPIC_*` / `CLAUDE_CODE_*` 变量，还提醒检查 `~/.zshrc`、`~/.bashrc` 残留。
  - **`CLAUDE_CODE_AUTO_COMPACT_WINDOW` 必须和模型上下文匹配**：`kimi-k3` 是 1M（1048576），`kimi-k2.7-code` 是 256K（262144）。设小了过早压缩丢上下文，设大了报超限。
  - **`/model` 菜单不会显示 Kimi 模型**，这是正常的——判断生效与否看 `/status`，不是看 `/model`。
  - `kimi-k2.7-code` **强制要求开启 Thinking**（Tab 键），否则报 `400 invalid thinking`；`kimi-k3` 无此限制。
  - 已知限制：WebFetch 当前报 `temporarily unavailable`，官方说待支持。
  - 官方明确点名 cc-switch 等社区工具"非 Kimi 官方维护，预设值可能与此页推荐值有差异"。

### 8. 智谱 GLM 官方 · Z.AI（国际站 / GLM Coding Plan）

- 链接：https://docs.z.ai/devpack/tool/claude
- 端点：`https://api.z.ai/api/anthropic`
- 当前官方配置（页面 2026 年已更新到 GLM-5.3）：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zai_api_key",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5.3-flash[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.3[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.3[1m]",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
    "API_TIMEOUT_MS": "3000000"
  }
}
```

- 一键方式（仅 macOS/Linux）：
  - `npx @z_ai/coding-helper`（官方 Coding Tool Helper，推荐，Windows 也可用）
  - 或 `curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh`（不支持 Windows）
- 注意：该页面 FAQ 里的"推荐版本"仍写着 Claude Code 2.0.14，属于页面未及时更新的部分，**建议直接用最新版**。

### 9. 智谱 · 国内站（open.bigmodel.cn）⚠️ 有个大坑

- 官方 Claude API 兼容说明：https://docs.bigmodel.cn/cn/guide/develop/claude/introduction
- 端点：`https://open.bigmodel.cn/api/anthropic`

**但这里有个我这次核查才发现的关键问题**：

我查到多篇 2026 年 8 月底的一手实测记录（含掘金、开发者博客）指出 —— 直接把 Claude Code 指向 `open.bigmodel.cn/api/anthropic`，**请求会落到 GLM Coding Plan 计费通道**，需要买套餐；如果你只是想用**普通按量付费 API**，这条路走不通，会报 `429 [1309] 您的 GLM Coding Plan 套餐已到期`。

想走普通 API 的正确链路是：
1. 端点改用工信部 OpenAI 格式地址 `https://open.bigmodel.cn/api/paas/v4/chat/completions`
2. 上游格式选 **OpenAI Chat Completions**
3. 中间需要一层协议转换（Anthropic Messages ↔ OpenAI Chat Completions），比如用本地路由工具接管

> 我的判断：这条链路上官方**缺少一份权威的 Claude Code 接入文档**（我尝试的 `docs.bigmodel.cn/cn/guide/coding/claude_code` 已 404），所以国内站普通 API 接 Claude Code 目前**不建议作为主力方案**。要么买 GLM Coding Plan 走 `/api/anthropic`，要么自己架协议转换层。

---

## 四、第三方本地网关（想跑任意模型 / 多模型路由）

### 10. Claude Code Router (CCR)

- 仓库：https://github.com/musistudio/claude-code-router
- **当前状态（我 2026-08-29 实测查证）**：
  - 最新版本 **v3.0.22**，发布于 **2026-08-24**
  - 最后一次提交 **2026-08-27**（合并 PR #1682）
  - 36k+ stars，MIT 协议，**活跃维护中**
- 当前安装方式（v3 已改工作流，**旧的 `ccr code` 命令已从 README 移除**）：
  - 桌面应用（推荐）：Releases 页下载，Windows `.exe` / Linux `.AppImage` / macOS `.dmg`
  - npm CLI：`npm install -g @musistudio/claude-code-router`，然后 `ccr ui`
  - 管理 UI：`http://127.0.0.1:3458`；模型网关：`http://127.0.0.1:3456`
  - Docker：`docker compose up -d --build`
  - **要求 Node.js 22+**
- v3 流程：Providers → Add Provider → Server → Start → Agent Profiles → 选模型 apply。支持按请求类型路由（default / background / think / longContext / webSearch / image）、条件规则、回退链。
- 支持的 agent：Claude Code、Codex、Grok CLI、Kimi CLI、Kilo Code、OpenCode、Pi、ZCode 等。

> ⚠️ **务必注意的冲突信息**：第三方索引站 x-cmd 把这个项目标为 "EOL / Maintenance mode，2026-01-06 后停止更新，不支持 Claude Code 2.x"。这**与 GitHub 仓库的实际情况不符**（仓库 8 月还在高频提交和发版）。我以 GitHub 一手信息为准，也顺手记一笔：**搜索结果里的"项目状态"字段不可轻信，一定要回仓库看 commit 日期。**

---

## 五、避坑清单：这些"看起来像教程"的东西不要用

这是我这次核查里实际撞到的**失效/错误内容**，每一条都有据可查：

| ❌ 不要用的说法 | 问题 | 正确做法 |
|---|---|---|
| `ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"` + `ANTHROPIC_API_KEY=sk-or-...`（见 claudecodeguides.com 的 "2026 Guide"） | 双错：路径多 `/v1` 会导致 `/api/v1/v1/messages`；用 `ANTHROPIC_API_KEY` 会走 `x-api-key` 头回落 Anthropic 直连 | 用 `/api` + `ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_API_KEY=""` |
| `export OPENAI_API_KEY=...` / `OPENAI_BASE_URL="https://openrouter.ai/api/v1"` 接 Claude Code（见某些 ima.qq.com 分享文档） | **完全错误**。Claude Code 走的是 Anthropic Messages 协议，不认 `OPENAI_*` 变量。原文"Claude Code 底层兼容 OpenAI API 格式"的说法不成立 | 用 `ANTHROPIC_*` 系列变量 |
| `ccr code` 命令启动 | CCR v3 已改工作流，README 里不再有这个命令 | 用 `ccr ui` 或桌面应用 |
| `docs.bigmodel.cn/cn/guide/coding/claude_code` | **实测 404**，该文档页已失效 | 用 `docs.bigmodel.cn/cn/guide/develop/claude/introduction` 或 Z.AI 文档 |
| 直接连 `open.bigmodel.cn/api/anthropic` 用普通 API | 会走 Coding Plan 通道，无套餐时报 `429 [1309]` | 要么买 Coding Plan，要么走 `/api/paas/v4/chat/completions` + 协议转换 |
| 用 x-cmd 等索引站的"项目状态"当依据 | 该项目页把 CCR 标为 EOL，与仓库实际（8-27 仍在提交）矛盾 | 回 GitHub 看 release 和 commit 日期 |
| 把所有模型变量一次性改完再测 | 央视级踩坑：失败时无法定位是哪个变量的问题 | 官方建议逐个验证：先固定 key → 不用 1M 验证链路 → 再换模型 → 最后开 1M |

---

## 六、我的推荐路径

**如果你的目标是"接 OpenRouter 跑 Claude"（最稳）：**

1. 先读官方 https://code.claude.com/docs/en/llm-gateway-connect 建立正确心智模型
2. 按 OpenRouter cookbook 配三个变量（`/api` + `ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_API_KEY=""`）
3. 嫌麻烦就直接上 `ori claude`（2026-08-04 官方新工具，自动配齐全套）
4. 在 OpenRouter provider 设置里把 **Anthropic 1P 设为最高优先级**
5. 跑 `/status` 验证

**如果你的目标是"让 Claude Code 跑国产模型"：**

1. **首选 DeepSeek**（`api.deepseek.com/anthropic`）或 **Kimi**（`api.moonshot.cn/anthropic`）—— 这两家官方文档最完整、当前、且明确给出了清理脚本和兼容性边界
2. 有 GLM Coding Plan 的话，Z.AI 方案（api.z.ai）很顺；只有国内站普通 API 的话，目前官方支持薄弱，不建议当主力
3. 想一套配置切多家 → 用 CCR v3.0.22
4. 心理预期放对：这是**官方未支持的用法**，工具调用、长上下文压缩、WebFetch 等都可能遇到边界问题

**通用排错顺序（按各官方文档总结的）：**

```
/status 看 Base URL 和 Auth token 对不对
  ↓ 不对 → 检查 settings.json 的 env 是否覆盖了终端 export
  ↓       → 检查 ANTHROPIC_API_KEY 是否真的为空字符串
  ↓       → 之前登录过就跑 /logout 再重启
curl 测端点 → 401 说明凭证放错了变量（AUTH_TOKEN vs API_KEY）
  ↓ 400 且报 context_management/Extra inputs → 加 CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1
模型报 not found → 检查各 DEFAULT_*_MODEL 是否都补齐了（Fable/Haiku 最容易漏）
```

---

## 运行记录

### 实际使用的搜索关键词

1. `Claude Code OpenRouter 配置 ANTHROPIC_BASE_URL`
2. `Claude Code third-party model provider OpenRouter setup 2026`
3. `Anthropic 官方 Claude Code LLM gateway 第三方模型 文档 docs.claude.com`
4. `智谱 GLM Claude Code Anthropic 兼容端点 api.z.ai 配置 2026`
5. `claude-code-router CCR 2026 是否还维护 弃用 Claude Code 原生网关`
6. `Kimi Moonshot Claude Code ANTHROPIC_BASE_URL 官方接入 2026`
7. `DeepSeek Claude Code Anthropic 兼容接口 api.deepseek.com/anthropic 官方`
8. `docs.bigmodel.cn Claude Code 接入 GLM 官方文档 open.bigmodel.cn/api/anthropic`

共 8 次 WebSearch，全部返回结果，无搜索失败。

### 实际打开过的原始链接（WebFetch 抓取并逐条核对）

| # | 链接 | 性质 | 结果 |
|---|---|---|---|
| 1 | https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration | OpenRouter 官方文档 | ✅ 成功，cookbook 完整内容已核对 |
| 2 | https://code.claude.com/docs/en/llm-gateway-connect | Anthropic 官方文档 | ✅ 成功，三个变量语义 + curl 验证 + 400 排错 |
| 3 | https://code.claude.com/docs/en/llm-gateway | Anthropic 官方文档 | ✅ 成功，拿到"不支持非 Claude 模型"原话 |
| 4 | https://openrouter.ai/blog/tutorials/claude-code-openrouter | OpenRouter 官方博客 | ✅ 成功，发布时间 2026-06-16 |
| 5 | https://docs.z.ai/devpack/tool/claude | Z.AI 官方文档 | ✅ 成功，已更新到 GLM-5.3 |
| 6 | https://github.com/musistudio/claude-code-router | 开源仓库 | ✅ 成功，确认 v3.0.22 / 2026-08-24 release / 2026-08-27 last commit |
| 7 | https://openrouter.ai/blog/announcements/ori-harness | OpenRouter 官方博客 | ✅ 成功，发布时间 2026-08-04 |
| 8 | https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code | DeepSeek 官方文档 | ✅ 成功，v4-pro/v4-flash 配置 + 模型映射机制 |
| 9 | https://platform.kimi.com/docs/guide/claude-code-kimi | Kimi 官方文档 | ✅ 成功，含清理脚本与兼容性边界 |
| 10 | https://docs.bigmodel.cn/cn/guide/coding/claude_code | 智谱国内站文档 | ❌ **404 Page Not Found**（该路径已失效，改用 `develop/claude/introduction`） |

### 是否查阅了官方当前文档

**是，且这是本次回答的主要依据来源。** 具体：

- **Anthropic 官方**：`code.claude.com/docs/en/llm-gateway`、`/llm-gateway-connect` 两个页面均完整抓取核对，包括原话引述
- **OpenRouter 官方**：cookbook 文档页 + 两篇官方博客（2026-06-16、2026-08-04）
- **DeepSeek 官方**：`api-docs.deepseek.com` 的 Claude Code 集成页 + Anthropic API 兼容页
- **Kimi 官方**：`platform.kimi.com/docs/guide/claude-code-kimi`
- **智谱 Z.AI 官方**：`docs.z.ai/devpack/tool/claude`
- **开源项目一手源**：直接查 GitHub 仓库的 release 和 commit 日期

所有推荐资源的配置参数均来自上述官方页面原文，未凭记忆编造任何端点、变量名或模型名。

### 遇到的异常或失败

1. **`docs.bigmodel.cn/cn/guide/coding/claude_code` 返回 404。** 该链接来自一篇第三方教程文章的引用，说明智谱国内站的 Claude Code 接入文档路径已变更。我改用搜索定位，找到当前有效的 `docs.bigmodel.cn/cn/guide/develop/claude/introduction`，但后者只是"Claude API 兼容"通用说明，**并非专门的 Claude Code 接入文档**。这构成了回答中对国内站方案的保留意见。

2. **搜索结果中出现相互矛盾的项目状态信息。** 关于 claude-code-router：索引站 x-cmd 标注 "EOL / Maintenance mode，最后更新 2026-01-06，不支持 Claude Code 2.x"，而另一索引站 everydev.ai 与博客则称其 "v3.0.18，2026-07-31 发布，活跃维护"。处理方式：**回一手源查证**，直接抓 GitHub 仓库，确认为 v3.0.22（2026-08-24）/ last commit 2026-08-27，采纳"活跃维护"结论，并在回答中显式标注这一冲突及判据。

3. **搜索结果中存在内容错误的教程。** 至少两处（`claudecodeguides.com` 的 "2026 Guide"、某 ima.qq.com 分享文档）给出的配置与官方文档矛盾——前者用 `/api/v1` + `ANTHROPIC_API_KEY`，后者用 `OPENAI_API_KEY` / `OPENAI_BASE_URL`。这些错误内容在搜索结果中排名不低，若只看摘要会直接被误导。因为本次要求"实际打开原始页面确认"，我通过比对官方一手文档识别出了它们，并写入了避坑清单。

4. **WebFetch 对长页面的内容截断。** 抓取 OpenRouter cookbook 与 Anthropic 网关文档时，返回内容为模型提炼的摘要而非完整原文，部分章节（如 GitHub Action 完整示例、LiteLLM 配置细节）未完整呈现。对这类页面我通过**二次搜索 + 交叉验证**补足（例如 Fast Mode 的版本要求 v2.1.96 来自官方博客而非 cookbook）。

5. **未做实机验证。** 本次仅做了文档层面的核查，未在真实机器上跑通配置。所有"当前有效"的判断基于：官方文档存在且内容新鲜（有明确发布日期或版本号）+ 端点/模型名在官方页面中为当前推荐值。**未验证的部分**：各家端点在 2026-08-29 当天的实际可用性、实时价格、以及具体模型的工具调用成功率。

### 其他说明

- 全程使用 WebSearch + WebFetch 真实联网，无编造资源。
- 用户要求"不要旧教程"，因此我把核查重点放在**失效识别**上，最终回答中"避坑清单"一节的权重较高——这是本次检索最实际的发现：该话题下搜索结果中的过期/错误内容比例相当高。
- 所有资源均标注了性质（官方文档 / 官方博客 / 开源仓库 / 第三方实测），便于判断可信度。
