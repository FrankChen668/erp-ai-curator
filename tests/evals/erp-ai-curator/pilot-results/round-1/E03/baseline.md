# Claude Code 接第三方模型：当前仍然有效的配置资源

> 核查时间：2026-08-28。下面每一条资源我都实际打开了原始页面确认内容，不是凭搜索摘要下结论。凡是页面打不开或已失效的，我在"运行记录"里如实标注了。

---

## 先说结论

"靠谱的配置方法"现在确实存在，但它分成了**两类完全不同的路子**，混着看会晕：

| 路子 | 适用场景 | 官方支持程度 |
| --- | --- | --- |
| **A. 厂商官方 Anthropic 兼容端点** | 想用 DeepSeek / GLM / Kimi 等非 Claude 模型 | 模型厂商自己维护，Anthropic 不背书 |
| **B. 网关聚合（OpenRouter 等）** | 想用一把钥匙管多个模型、做 failover 和预算控制 | 网关方维护；OpenRouter 官方明说"只保证 Anthropic 一供" |
| **C. 本地路由工具（claude-code-router）** | 想给只有 OpenAI 格式的厂商做协议转换，或按任务分流模型 | 社区开源项目 |

**一句话建议**：如果你只是想省钱换模型，走 A（DeepSeek / GLM / Kimi 官方端点），配置最短、坑最少。如果你要的是"多个模型随时切"，走 C。走 B 的话，请接受"只能用 Claude 系模型才稳"这个前提。

---

## 一个必须先讲清楚的官方立场

这条是我在 Anthropic 官方文档里翻到的，很多教程都不会告诉你：

> "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and **doesn't support routing Claude Code to non-Claude models through any gateway**."
> —— 官方 LLM gateway 文档

也就是说：技术上 `ANTHROPIC_BASE_URL` 指向谁都行，但**接了非 Claude 模型出问题，Anthropic 不负责**。这不是吓唬人，后面你会看到它带来几个具体的功能折损。

---

## 资源清单

### 1. Anthropic 官方：Claude Code 连 LLM 网关（必读，权威基线）

**链接**：
- <https://code.claude.com/docs/en/llm-gateway-connect>（连接步骤 + 排错表）
- <https://code.claude.com/docs/en/llm-gateway>（概述 + 官方立场）
- <https://code.claude.com/docs/en/env-vars>（环境变量全表）
- <https://code.claude.com/docs/en/model-config>（模型槽位映射）

**推荐理由**：这是唯一一份**你自己就能验证、且不会过期**的基线。不管你最后接哪家，配置文件里写的都是这几个变量，以官方为准就不会被旧教程带偏。

核心就两个变量：

```bash
export ANTHROPIC_BASE_URL=https://你的端点
export ANTHROPIC_AUTH_TOKEN=你的密钥
```

官方文档里特别好用的三块内容：

**（a）先 curl 验一遍，别上来就开 Claude Code**（避免"到底是我配错了还是网关挂了"这种无谓排查）：

```bash
curl -X POST "$ANTHROPIC_BASE_URL/v1/messages" \
  -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-sonnet-4-6","max_tokens":1,"messages":[{"role":"user","content":"."}]}'
```

返回以 `{"id":"msg_` 开头且有 `content:[...]` 就是通的。**哪怕是"模型不存在"的报错也算通**——说明网关已经认证了你的请求才去拒绝模型名。返回 401 才是密钥不对，或者你选错了变量（bearer 用 `ANTHROPIC_AUTH_TOKEN`，x-api-key 用 `ANTHROPIC_API_KEY`）。

**（b）模型槽位要配全，否则后台任务静默失败**。这是最常见的坑：Claude Code 不只用主模型，后台摘要、子 agent、Plan 模式各走不同槽位。官方文档给的槽位变量是：

| 变量 | 作用 |
| --- | --- |
| `ANTHROPIC_MODEL` | 主对话 |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Opus 档（复杂推理 / Plan 模式） |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Sonnet 档（日常编码） |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Haiku 档（后台任务、摘要） |
| `ANTHROPIC_DEFAULT_FABLE_MODEL` | Fable 档（Claude Code 2.1.x 新增的第四档） |
| `CLAUDE_CODE_SUBAGENT_MODEL` | 子 agent |

**（c）功能折损清单**（官方排错表里写的，接第三方前建议先看）：

- `ANTHROPIC_BASE_URL` 指向非第一方主机时，**MCP tool search 默认关闭**；代理若转发 `tool_reference` 块，用 `ENABLE_TOOL_SEARCH=true` 打开
- 自 v2.1.196 起，指向非 `api.anthropic.com` 时 **Remote Control 被禁用**
- `ANTHROPIC_AUTH_TOKEN` / `ANTHROPIC_API_KEY` / `apiKeyHelper` 任一生效时，**voice dictation 不可用**
- 网关若不转发 Claude Code 新版本加的字段，对应功能会坏——官方原话是"a gateway that doesn't forward them breaks the corresponding features"，所以网关产品得跟着 Claude Code 一起更新

---

### 2. OpenRouter 官方：Claude Code 集成页

**链接**：<https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration>

**推荐理由**：OpenRouter 自己维护的官方文档，实测可访问，内容详细到把"为什么"都写清楚了。

**但开头第一句就是一盆冷水**，我照抄：

> "Claude Code with OpenRouter is **only guaranteed to work with the Anthropic first-party provider**. For maximum compatibility, we recommend setting Anthropic 1P as top priority provider when using Claude Code."

以及后半页再次强调：

> "Claude Code is optimized for Anthropic models and **may not work correctly with other providers**."

所以 OpenRouter 这条路的价值不在"接别的模型"，而在**统一计费 + 供应商 failover + 团队预算控制**。冲着"用 OpenRouter 跑 GLM/DeepSeek"去的，劝你直接看下面第 3~5 条，走厂商官方端点更省事。

官方给出的配置（我逐字核对过）：

```bash
export OPENROUTER_API_KEY="<你的 key>"
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""          # 必须是空字符串，不是"不设置"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1   # 可选，让 /model 列出网关模型
```

四个容易翻车的点，全在它文档里：

1. **Base URL 是 `https://openrouter.ai/api`，不带 `/v1`**。Claude Code 会自己拼 `/v1/messages`，你写了 `/v1` 就变成 `/api/v1/v1/messages`。
2. **`ANTHROPIC_API_KEY=""` 必须显式留空**。官方解释：这个变量走 `x-api-key` 头、被当成"直连 Anthropic"的凭据，留着真 key 会导致 Claude Code 绕开网关直接打 Anthropic。
3. **之前 `/login` 登录过 Claude 账号的，要先跑一次 `/logout`**，否则缓存的登录态和网关凭据冲突，症状是 `openrouter/auto`、`openrouter/pareto-code` 这类模型报 model-not-found。
4. **改完 shell profile 要 `source`**，否则你一直在用旧环境测试，然后得出"配置不work"的错误结论。

验证方式是进会话敲 `/status`，应该看到：

```
Auth token: ANTHROPIC_AUTH_TOKEN
Anthropic base URL: https://openrouter.ai/api
```

模型槽位它推荐用 `~` 前缀别名（`~anthropic/claude-sonnet-latest`），这样永远解析到该系列最新版，不会过时。它文档里还提到：Claude Code 2.1.x 加了 Fable 档后，指向 OpenRouter 时 Fable **默认不出现在 `/model` 里**，只能靠显式设 `ANTHROPIC_DEFAULT_FABLE_MODEL` 才能选。

---

### 3. DeepSeek 官方：接入 Claude Code

**链接**：<https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code>

**推荐理由**：官方页面实测可访问，配置示例完整，且明确写了模型映射规则。这是我心里"最省事"的一条路。

官方原文配置（Linux/Mac）：

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

Windows PowerShell 版它文档里也给了，变量名一样，把 `export X=Y` 换成 `$env:X="Y"` 即可。

两个值得注意的细节：

- **它把所有槽位都配齐了**，包括最容易被漏掉的 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 和 `CLAUDE_CODE_SUBAGENT_MODEL`——上面 OpenRouter 那条坑在这里被官方提前填了。
- **官方会做模型名映射**：传 `claude-opus` 开头的映射到 deepseek-v4-pro，`claude-haiku`/`claude-sonnet` 开头的映射到 deepseek-v4-flash。好处是你在新版 Claude Desktop 开发者模式里只改 base_url 和 key 就能用，绕过 App 对模型名的限制。
- 文档中提到 DeepSeek API 原生支持 Claude Code 的 Web Search 功能（模型自行判断触发），但会产生额外的 token 费用。

---

### 4. 智谱 GLM 官方：Claude Code 接入

**链接**：<https://docs.bigmodel.cn/cn/guide/develop/claude>

**推荐理由**：官方页面实测可访问，而且它的"常见问题"章节质量很高，把 `/status` 验证、模型切换、effort 映射都写清楚了。

⚠️ **注意：网上流传的 `https://docs.bigmodel.cn/cn/guide/coding/claude_code` 已经 404 了**（我实测过）。现在有效的地址是上面这个 `/guide/develop/claude`。这正好是你要的"不要旧教程"的典型例子——很多聚合文章还在引用那个死链。

官方手动配置示例（`~/.claude/settings.json`，Windows 为 `用户目录/.claude/settings.json`）：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.7",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
    "API_TIMEOUT_MS": "3000000"
  }
}
```

它另外提供两种省事的方式：

```bash
npx @z_ai/coding-helper        # 交互式助手，自动装工具+配套餐+管 MCP
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh   # 仅 macOS/Linux
```

几个官方明确写了的点：

- **默认走服务端模型映射**：界面上看到的是 Claude 模型名，实际是 GLM。默认三档全是 `GLM-4.7`；要用最新的 GLM-5.2 得显式改配置。
- **1M 上下文要加 `[1m]` 后缀**（`glm-5.2[1m]`），同时必须把 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 设成 `"1000000"`。官方还补了一句：如果加了 `[1m]` 后 Claude Code 报模型不存在，先升级 Claude Code 到最新版。
- **effort 映射**：`low/medium/high` → 实际 `high`；`xhigh/max/ultracode` → 实际 `max`。官方建议 coding 任务切到 `max`。
- 官方验证过的 Claude Code 版本是 **2.1.140**（页面原文写"我们在 Claude Code 2.1.140 等版本验证 OK"）。
- 注意 Coding Plan 的 **团队套餐 Key 与平台其他 API Key 不通用**，别拿错。

---

### 5. Kimi（Moonshot）官方：在 Claude Code 中使用 Kimi

**链接**：<https://platform.kimi.com/docs/guide/claude-code-kimi>

**推荐理由**：我这次核查里**文档写得最严谨的一篇**——它连"旧配置残留会覆盖新配置"这种坑都给了清理脚本，还专门提示了社区工具 cc-switch 的预设可能和官方推荐值不一致。

配置（官方原文，`~/.claude/settings.json` 的 `env` 字段）：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_MOONSHOT_API_KEY",
    "ANTHROPIC_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "kimi-k3[1m]",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "kimi-k3[1m]",
    "CLAUDE_CODE_SUBAGENT_MODEL": "kimi-k3[1m]",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1048576",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

它文档里有三处我觉得必须转述给你：

1. **`settings.json` 的 `env` 会覆盖终端里 export 的同名变量**。如果你之前用第三方工具改过 `~/.claude/settings.json`，残留的旧 `env` 会静默覆盖你新 export 的值，导致"配了但没生效"。官方文档直接给了一段 node 清理脚本，把 `ANTHROPIC_*`、`CLAUDE_CODE_SUBAGENT_MODEL`、`ENABLE_TOOL_SEARCH` 等 17 个 key 从 `env` 里删掉。同时提醒检查 `~/.zshrc`、`~/.bashrc`、Windows 用户环境变量里有没有残留 export。

2. **`/model` 菜单不会显示 Kimi 模型**——那是 Claude Code 内置的固定别名列表。判断配置是否生效**以 `/status` 为准**，看 Base URL 和 Model 两行，不要去 `/model` 里找。这条能省掉大量"我是不是配错了"的自我怀疑。

3. **不同模型的 thinking 行为不一样**（官方实测结论）：
   - `kimi-k3`：默认开启思考，开箱即用
   - `kimi-k2.7-code`：**必须显式开启思考**（Claude Code 里按 `Tab` 打开 Thinking on），否则请求被拒，报 `400 invalid thinking: only type=enabled is allowed for this model`，WebSearch 也跟着挂
   - `kimi-k2.6`：思考可选，延迟敏感的简单任务可用

   另外 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 要跟模型上下文对齐：`kimi-k3` 是 1M（`1048576`），`kimi-k2.7-code` 是 256K（`262144`）。

它还坦白了一个当前限制：**该端点暂不支持 WebFetch 抓取**（报 `temporarily unavailable`），官方说是待平台支持，临时方案是把网页内容粘给模型或用 MCP 抓取工具。这种"官方自己承认的限制"反而是我判断一篇文档可信的信号。

---

### 6. claude-code-router（CCR）：本地路由工具（需要协议转换时用）

**链接**：<https://github.com/musistudio/claude-code-router>
**文档**：<https://ccrdesk.top/>

**推荐理由**：我拉了它的 README 原文确认，**项目活跃，当前版本 v3.0.22**，不是废弃项目。

**什么时候才需要它**：上面 2~5 条都是厂商自带 Anthropic 兼容端点，不需要它。只有两种情况值得上：

1. 你的目标厂商**只提供 OpenAI 格式**（官方 quickstart 里明说 Kimi API "兼容 OpenAI API 格式"；阿里云百炼也是 OpenAI 兼容），需要一个本地层做协议转换
2. 你想**按任务分流**——主对话用一个模型、后台摘要用便宜的、长上下文用另一个

用法（README 原文）：

```bash
npm install -g @musistudio/claude-code-router   # 需要 Node.js 22+
ccr ui
```

然后浏览器开 `http://127.0.0.1:3458`，走 Providers → Server → Agent Config 三步；网关本体在 `http://127.0.0.1:3456`。它也提供桌面版（Win/Linux/macOS）和 Docker Compose 部署。支持的客户端除了 Claude Code 还有 Codex、Kimi CLI、OpenCode 等。

**一个提醒**：Kimi 官方文档明确说了 cc-switch 这类社区工具"并非 Kimi 官方维护，其预设配置可能与本页推荐值存在差异"，用了要逐项核对并用 `/status` 确认。同样的谨慎适用于任何第三方路由工具。

---

## 我建议你按这个顺序走

1. **先花 5 分钟看官方 env-vars 和 llm-gateway-connect 两页**（资源 1）。这是地基，看完你就有了判断力，以后再看到任何教程你都能自己判断它对不对。
2. **想省钱换模型 → 走资源 3 / 4 / 5**（DeepSeek / GLM / Kimi 官方端点）。三家配置结构完全一样，只是 URL 和模型名不同，随便挑一家，10 分钟内能跑通。我个人的排序是：Kimi 文档最严谨（排错最全）、DeepSeek 配置最完整（槽位全配齐）、GLM 选择最多（有官方脚本和 Coding Plan 套餐）。
3. **只是想要 OpenRouter 的统一计费和 failover → 走资源 2**，但请把模型保持在 Claude 系，并且务必做 `ANTHROPIC_API_KEY=""` 和 `/logout` 两步。
4. **目标厂商只有 OpenAI 格式，或要按任务分流模型 → 走资源 6**。

---

## 怎么一眼看出是"旧教程"

这次核查里我实际撞到的失效/过时特征，列出来给你当检查清单：

| 特征 | 说明 |
| --- | --- |
| 用 `ANTHROPIC_SMALL_FAST_MODEL` | **已废弃**。官方 model-config 页原文：`ANTHROPIC_SMALL_FAST_MODEL` is deprecated in favor of `ANTHROPIC_DEFAULT_HAIKU_MODEL` |
| OpenRouter base URL 写成 `https://openrouter.ai/api/v1` | 错。Claude Code 会自己拼 `/v1/messages`，应该是 `/api` |
| 智谱文档链到 `docs.bigmodel.cn/cn/guide/coding/claude_code` | **已 404**。现在是 `/cn/guide/develop/claude` |
| 只配 `ANTHROPIC_BASE_URL` + `ANTHROPIC_MODEL` 两个变量 | 不完整。至少要把 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 和 `CLAUDE_CODE_SUBAGENT_MODEL` 配上，否则后台任务和子 agent 会静默失败 |
| 教你用 `y-router` / 自建 Docker 代理来接 OpenRouter | 过时。OpenRouter 现在有原生 Anthropic Skin，不需要本地代理，它官方原文说 "No local proxy server is required" |
| 只给配置不告诉怎么验证 | 不可信。靠谱的文档都会让你 `/status` 或先 curl 验一遍 |

**最后一句提醒**：这个领域变化极快，模型名（GLM-4.7 / glm-5.2、kimi-k3、deepseek-v4-pro 这些）几乎肯定会在几个月内变。配置骨架（`ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN` + 各槽位变量）是稳定的，但**具体模型名请一定去对应厂商的官方页面现查**，别信二手文章里抄的名字。

---

## 运行记录

### 实际使用的搜索关键词

1. `Claude Code OpenRouter 配置 第三方模型`（freshness: m3）
2. `Claude Code ANTHROPIC_BASE_URL third party model setup`（freshness: m3）
3. `Claude Code docs environment variables ANTHROPIC_BASE_URL docs.claude.com`
4. `OpenRouter docs Claude Code integration anthropic compatible endpoint`
5. `DeepSeek 智谱 GLM Kimi 官方 Anthropic 兼容端点 Claude Code 接入文档`（freshness: m3）
6. `docs.bigmodel.cn GLM Claude Code 接入 open.bigmodel.cn/api/anthropic`

### 实际打开过的原始链接（WebFetch）

**成功获取内容：**

| # | 链接 | 结果 |
| --- | --- | --- |
| 1 | <https://code.claude.com/docs/en/env-vars> | 成功。Anthropic 官方环境变量全表，逐字核对了 `ANTHROPIC_BASE_URL`、`ANTHROPIC_AUTH_TOKEN`、`ANTHROPIC_API_KEY`、`ANTHROPIC_MODEL`、`ANTHROPIC_DEFAULT_*_MODEL` 系列、`ANTHROPIC_CUSTOM_MODEL_OPTION`、`ANTHROPIC_SMALL_FAST_MODEL`（标注 DEPRECATED） |
| 2 | <https://code.claude.com/docs/en/llm-gateway> | 成功。拿到官方立场原文 "doesn't support routing Claude Code to non-Claude models through any gateway" |
| 3 | <https://code.claude.com/docs/en/llm-gateway-connect> | 成功。完整的连接步骤、curl 验证命令、凭据变量对照表、各 surface 配置、排错表 |
| 4 | <https://code.claude.com/docs/en/model-config> | 成功。模型槽位变量表、deprecation 说明、gateway 下的模型名透传规则 |
| 5 | <https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration> | 成功。OpenRouter 官方配置原文、"only guaranteed with Anthropic 1P" 声明、三条翻车提示、`/status` 验证、Fable 档说明 |
| 6 | <https://openrouter.ai/docs/quickstart> | 成功。确认 OpenRouter 的 OpenAI 格式端点是 `/api/v1`，与 Claude Code 用的 `/api` 区分开 |
| 7 | <https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/claude_code> | 成功。DeepSeek 官方配置原文（含 Linux/Mac 与 Windows 两版）、模型映射规则、Web Search 说明 |
| 8 | <https://docs.bigmodel.cn/cn/guide/develop/claude> | 成功。智谱官方配置原文、模型切换说明、effort 映射表、验证版本 2.1.140 |
| 9 | <https://platform.kimi.com/docs/guide/claude-code-kimi> | 成功。Kimi 官方配置原文、旧配置清理脚本、`/status` 而非 `/model` 的判断依据、thinking 行为差异表、WebFetch 限制 |
| 10 | <https://raw.githubusercontent.com/musistudio/claude-code-router/main/README.md> | 成功。确认项目活跃、版本 v3.0.22、安装与启动方式、支持的客户端列表 |
| 11 | <https://platform.moonshot.cn/docs/guide/agent-support> | **发生了跳转**，实际落在 <https://platform.kimi.com/docs/overview>（Kimi 快速开始页）。该页确认 Kimi API 兼容 OpenAI 格式，并给出了 `claude-code-kimi` 官方接入文档的正确链接，因此发现了资源 5 |

**失败 / 失效（如实记录）：**

| # | 链接 | 失败情况 |
| --- | --- | --- |
| 1 | <https://docs.claude.com/en/docs/claude-code/settings> | `fetch failed`，网络层失败。后改用搜索找到官方域名 `code.claude.com` 才成功 |
| 2 | <https://openrouter.ai/docs/community/use-with-claude-code> | **404 Page Not Found**。这是网上常见的引用路径，已失效。正确路径是 `/docs/cookbook/coding-agents/claude-code-integration` |
| 3 | <https://docs.bigmodel.cn/cn/guide/coding/claude_code> | **404 Page Not Found**。这是被大量聚合文章引用的智谱旧文档路径，已失效。正确路径是 `/cn/guide/develop/claude` |
| 4 | <https://github.com/musistudio/claude-code-router>（HTML 页） | 只返回了页面标题，未拿到正文。改用 `raw.githubusercontent.com` 拉 README 原文后成功 |

### 是否查阅了官方当前文档

**是，且这是本次核查的主体。** 6 份推荐资源中有 5 份是厂商/项目官方一手文档，逐字核对了配置示例原文，而非依赖搜索摘要：

- Anthropic 官方 4 个页面（env-vars / llm-gateway / llm-gateway-connect / model-config）
- OpenRouter 官方 2 个页面（cookbook 集成页 / quickstart）
- DeepSeek 官方接入文档
- 智谱官方 Claude Code 文档
- Kimi 官方 Claude Code 文档
- claude-code-router 官方 README（raw 原文）

### 遇到的异常或失败

1. **官方域名不是我以为的那个**：`docs.claude.com` 抓取直接 `fetch failed`，而有效的官方域名是 `code.claude.com`。如果没做这一步，可能会误判"官方文档抓不到"而退回二手资料。
2. **两个广泛流传的文档链接已 404**：OpenRouter 的 `/docs/community/use-with-claude-code` 和智谱的 `/cn/guide/coding/claude_code`。这两条恰好是本题"不要旧教程"的核心证据。
3. **GitHub HTML 页面抓取降级**：直接抓 repo 页面只返回标题，改拉 raw README 才拿到完整内容。
4. **搜索结果存在大量低质量/疑似 SEO 内容农场**，例如 claudecodeguides.com 给出的 OpenRouter base URL 是 `https://openrouter.ai/api/v1`（错误，应为 `/api`）、atlascloud.ai 与 llmgateway.io 等聚合站混着真实变量和可疑模型名。我**没有**把这些作为推荐来源，只用官方页面交叉验证过的变量值。
5. **模型名时效性风险**：搜索结果里出现了大量我无法独立验证的模型名（GLM-5.2、GPT-5.5、DeepSeek V4 Pro 等）。我的处理方式是——**只引用厂商官方文档页面上当前写着的模型名**（如 `glm-5.2[1m]`、`kimi-k3[1m]`、`deepseek-v4-pro[1m]`），并在正文末尾明确提醒读者模型名会变、需现查。
6. **未做实机验证**：本次只做了文档层面的核查与交叉验证，没有实际安装 Claude Code 并跑通某一家端点。因此"能配通"是基于官方文档的推断，不是我亲测的结论。
