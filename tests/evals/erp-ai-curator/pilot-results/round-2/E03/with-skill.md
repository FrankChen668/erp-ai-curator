# E03 eval 结果 — Claude Code 接 OpenRouter / 其他第三方模型的当前有效配置方法

> 任务原文：Claude Code 接 OpenRouter 或其他第三方模型，现在有没有靠谱的配置方法？给我当前还有效的资源，不要旧教程。
> 执行日期：2026-08-29

---

## 第一部分：面向用户的最终回答

**结论：有，且官方路径是主流。推荐 2 个资源。** 配置 Claude Code 走第三方模型的原理是三个环境变量（`ANTHROPIC_BASE_URL` 指向网关、`ANTHROPIC_AUTH_TOKEN` 放密钥、`ANTHROPIC_API_KEY` 必须显式留空），这是 Anthropic 官方为"LLM 网关"定义的语义，OpenRouter 是当前最成熟、文档最完整的落地渠道。

| 资源 | 类型 | 为什么值得看 | 能得到什么 | 重要限制 |
|---|---|---|---|---|
| [Claude Code Integration — OpenRouter 官方文档](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration) | 官方文档 | 这是 OpenRouter 官方维护的 Claude Code 集成指南，是"接 OpenRouter"当前最权威的配置源，所有旧教程（本地代理、`ANTHROPIC_SMALL_FAST_MODEL` 等）都可对照它淘汰 | 完整的当前有效配置：`ANTHROPIC_BASE_URL=https://openrouter.ai/api`、`ANTHROPIC_AUTH_TOKEN=<sk-or-...>`、`ANTHROPIC_API_KEY=""`（必须显式空，否则会回退到 Anthropic 官方认证）；按任务分模型的变量表（`ANTHROPIC_DEFAULT_OPUS/SONNET/HAIKU/FABLE_MODEL`、`CLAUDE_CODE_SUBAGENT_MODEL`）；`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` 打开 /model 网关模型选择器；Fast Mode（`CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1`，需 v2.1.96+）；GitHub Action / Agent SDK 接入；以及 /logout、/status 等排错步骤 | 官方明确：本集成只保证 Anthropic 第一方 provider 的模型；非 Anthropic 模型走原生 endpoint 不保证兼容。已登录过 Anthropic 账号的必须先 `/logout` 再重开 |
| [claude-code-router — 官方 GitHub 仓库](https://github.com/musistudio/claude-code-router) | Tool（开源项目） | 如果你要的是"其他第三方模型"（DeepSeek / GPT / Gemini / 本地 Ollama 等），OpenRouter 原生路径并不保证，这是当前仍在活跃维护（v3.0.22，2026-08-24 发布）的本地网关方案，把 Claude Code 的请求路由到任意提供商 | 一个本地网关（`127.0.0.1:3456`）接管 Claude Code，支持 OpenAI / Anthropic / Gemini / DeepSeek / SiliconFlow / Moonshot / Kimi / Mistral / Z.AI / 百炼等，按任务类型（default/background/think/longContext/webSearch）路由到不同模型，含重试、凭据池、回退模型与本地请求日志 | 现在的官方推荐是桌面应用 / `ccr ui` 界面配置（npm CLI 需 Node.js 22+），README 已不再强调手写 config.json；网上流传的 `api_base`/`api_base_url` 字段写法教程彼此不一致，请以官方 README 为准。它是 Claude Code 之上的额外一层，只想接 OpenRouter 时不需要它 |

### 为什么没有推荐更多

- **Anthropic 官方《Connect Claude Code to an LLM Gateway》**（code.claude.com/docs/en/llm-gateway-connect）是上述配置的权威语义来源（`ANTHROPIC_AUTH_TOKEN` 走 `Authorization: Bearer`、`ANTHROPIC_API_KEY` 走 `x-api-key`、settings 文件优先级），质量很高，但内容已被推荐 #1 完整引用并覆盖——它适合排错时查，不需要单独占一个推荐位。
- **中文侧候选全部被排除**：搜到的中文教程（七牛云、腾讯云、ima 知识库文章）要么仍推荐已被官方废弃的 `ANTHROPIC_SMALL_FAST_MODEL`，要么声称"Claude Code 底层兼容 OpenAI 格式、用 `OPENAI_BASE_URL` 配置"——这与 Anthropic / OpenRouter 官方文档相悖（Claude Code 走 Anthropic Messages API，配置变量是 `ANTHROPIC_*`），属于会误导人的旧信息，不推荐。
- **OpenRouter 自家新出的 ori CLI** 本质是把上述环境变量自动化的一键工具，不增加新的知识量，未占推荐位。

### 一次配置到底怎么做（摘要，来自推荐 #1）

```bash
# 写入 ~/.zshrc 或 ~/.bashrc
export OPENROUTER_API_KEY="sk-or-v1-..."
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"   # 不要带 /v1，Claude Code 会自己拼 /v1/messages
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""                             # 必须显式为空
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1     # 可选：/model 选择器
```

若之前用 Anthropic 账号登录过：在 claude 里 `/logout` 后重开。用 `/status` 确认 base URL 为 `https://openrouter.ai/api` 即成功。

---

## 第二部分：运行记录

### 1. 任务理解

- 角色：Claude Code 用户（开发者），此前可能已有 Anthropic 账号或想避开它。
- 动作：把 Claude Code 的模型请求路由到 OpenRouter 或其他第三方模型。
- 最终想要：一套**当前仍有效**的配置方法（环境变量 / endpoint / 兼容范围），明确排除旧教程。
- 高风险事实核验判定：涉及安装与配置、endpoint、环境变量、模型兼容 → 命中 volatile-fact-check 路径，执行强核验。

### 2. 实际使用的搜索关键词

| 序号 | 语言 | 关键词 | 用途 |
|---|---|---|---|
| 1 | 英文 | `Claude Code OpenRouter third-party model configuration official docs` | 找 OpenRouter 官方配置文档 |
| 2 | 中文 | `Claude Code 接入 OpenRouter 第三方模型 配置方法 环境变量` | 找中文侧候选与社区做法 |
| 3 | 英文 | `Anthropic Claude Code docs third-party LLM gateway ANTHROPIC_BASE_URL configuration` | 核对 Claude Code 官方 LLM 网关文档 |
| 4 | 英文 | `claude-code-router 2026 current setup non-Anthropic models maintainer` | 核验社区"接非 Anthropic 模型"方案的当前状态 |

### 3. 实际打开过的原始链接清单

| # | 链接 | 性质 | 读到什么 / 结论 |
|---|---|---|---|
| 1 | https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration | OpenRouter 官方文档 | 完整配置变量、模型路由表（含新增 Fable 类）、gateway model discovery、Fast Mode（v2.1.96+）、GitHub Action / Agent SDK / statusline、Troubleshooting（/logout、ANTHROPIC_API_KEY 必须显式空、/status 验证）。确认 base URL 为 `https://openrouter.ai/api`。明确"仅保证 Anthropic 第一方 provider；非 Anthropic 模型原生 endpoint 不保证"。→ **核心推荐 #1** |
| 2 | https://openrouter.ai/blog/tutorials/claude-code-openrouter | OpenRouter 官方博客 | 发布时间 2026-06-16。三变量配置、settings.local.json 用法、不要用 .env、/logout 提示、免费模型层说明。FAQ 明确回答"非 Anthropic 模型通过原生 endpoint 不受支持"。与 #1 同源，作佐证 |
| 3 | https://code.claude.com/docs/en/llm-gateway-connect | Anthropic 官方文档 | 官方定义 `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN`（Bearer）/ `ANTHROPIC_API_KEY`（x-api-key）语义、配置位置（shell、settings.json env 块、settings.local.json）与优先级、curl 验证、apiKeyHelper；文档覆盖至 v2.1.246，持续维护。→ **证据锚点**，交叉核验 #1 的变量语义成立 |
| 4 | https://github.com/musistudio/claude-code-router | claude-code-router 官方仓库 | 最近提交 2026-08-27、Release v3.0.22（2026-08-24），活跃维护。支持 OpenAI/Anthropic/Gemini/DeepSeek/SiliconFlow/Moonshot/Kimi/Mistral/Z.AI/百炼等。当前推荐桌面应用 / `ccr ui` 配置，本地网关 `127.0.0.1:3456`，npm CLI 需 Node.js 22+。README 不再以手写 config.json 为主。→ **核心推荐 #2** |
| 5 | https://www.zyte.com/blog/how-to-run-any-model-inside-claude-code/ | 第三方博客 | 佐证 base URL 不要带 /v1（Claude Code 会拼 /v1/messages）；提到 `ANTHROPIC_SMALL_FAST_MODEL` 已废弃、由 HAIKU 变量取代。第三方来源，仅作旁证，不推荐 |
| 6 | https://news.qiniu.com/archives/1781748097958 | 第三方中文文章 | 仍使用已被废弃的 `ANTHROPIC_SMALL_FAST_MODEL`，且夹带自家 API 推广 → **排除** |
| 7 | https://ima.qq.com/wiki/?shareId=...（两条） | 第三方中文知识库 | 其中一条声称"Claude Code 底层兼容 OpenAI API 格式，用 OPENAI_BASE_URL"，与官方相悖 → **排除** |

> 搜索摘要中出现的 agent.csdn.net、morphllm.com、getaiperks.com、llmgateway.io、merge.dev、docs.anthropic.com 等页面未逐页打开，仅作为线索判断方向；凡进入最终推荐的资源均已在原始页面打开核验。

### 4. 实际读取的 references 及读取环节（顺序）

| 顺序 | 文件 | 读取环节 |
|---|---|---|
| 1 | `references/source-strategy.md` | 任务理解完成、**开始联网搜索前**（环节：确定搜索关键词与来源优先级） |
| 2 | `references/volatile-fact-check.md` | **第一轮搜索拿到配置类候选后**（环节：判定命中高风险事实核验——安装/配置、endpoint、环境变量、模型兼容） |
| 3 | `references/selection-heuristics.md` | **交叉核验完成、进入最终候选横向取舍时**（环节：决定第二个推荐位取 Anthropic 官方文档还是 claude-code-router） |

### 5. 高风险事实核验结果

- **官方 vs 第三方冲突**：
  - 冲突 A：第三方文章使用 `ANTHROPIC_SMALL_FAST_MODEL`。核验：OpenRouter 官方 cookbook 与 Anthropic 官方当前均用 `ANTHROPIC_DEFAULT_HAIKU_MODEL`，第三方 Zyte 文亦标注前者 deprecated。→ 含旧变量的教程（七牛云文）**已排除**。
  - 冲突 B：ima.qq.com 声称用 `OPENAI_BASE_URL`/OpenAI 格式。核验：Anthropic 官方 llm-gateway-connect 与 OpenRouter cookbook 均明确 Claude Code 走 Anthropic Messages API、配置变量为 `ANTHROPIC_*`。→ **已排除**。
- **endpoint 核验**：OpenRouter 官方确认 base URL 是 `https://openrouter.ai/api`（非 `/api/v1`；Claude Code 自行追加 `/v1/messages`）。多来源（官方 cookbook、官方博客、Zyte 旁证）一致。→ 通过。
- **兼容范围核验**：OpenRouter 官方明确原生 endpoint 仅保证 Anthropic 模型，非 Anthropic 模型不保证；claude-code-router 官方仓库确认支持 DeepSeek/GPT/Gemini 等非 Anthropic 模型。→ 推荐按此区分，未把"通过 OpenRouter 用非 Claude 模型"包装成官方保证。
- **未把"曾经有效"当"现在有效"**：所有最终推荐均来自 2026-06 之后仍在更新的官方/原始来源（OpenRouter cookbook 含 v2.1.x 新特性、claude-code-router v3.0.22 于 2026-08-24 发布、Anthropic 文档覆盖至 v2.1.246）；含过时变量的旧教程已全部排除。

### 6. 遇到的异常或失败

- 无 WebFetch 失败。claude-code-router 的 README 未给出 config.json 的字段级结构（`api_base` vs `api_base_url`），因此不对其字段名做断言，并在推荐中提示"以官方 README 为准"——这正是"无法确认当前有效时不包装成当前可用"的处理。
- 搜索摘要里的多个聚合站/第三方教程（morphllm、getaiperks 等）配置字段互相矛盾，判定为不可靠线索，未进入推荐。

### 7. 中文 tie-breaker 的处理

- 质量相同时优先中文：但本次中文侧候选（七牛云、腾讯云、ima 知识库）全部含过时或与官方相悖的配置，**质量明显低于**英文官方/原始来源，按"质量差距明显时不因中文优先保留较差资源"规则，放弃中文候选，推荐两个英文原始来源，并用中文说明重点与限制。

### 8. 为什么没有推荐更多

- Anthropic 官方 llm-gateway-connect：内容与推荐 #1 高度重合（#1 已引用其权威语义），作为证据锚点而非占位推荐。
- OpenRouter ori CLI、官方博客教程：与 #1 同源或仅为 #1 的自动化，不构成独立增量。
- 各种第三方中文/英文教程：含废弃变量或与官方相悖，或未被当前官方佐证。
