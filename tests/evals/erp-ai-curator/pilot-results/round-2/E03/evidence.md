# E03 Evidence — Round 2

## 使用的 prompt（原样，未改写）

> Claude Code 接 OpenRouter 或其他第三方模型，现在有没有靠谱的配置方法？给我当前还有效的资源，不要旧教程。

## Artifact 验证（执行 correction D）

| 文件 | 存在 | 非空 | 含最终用户回答 |
|---|---|---|---|
| `round-2/E03/baseline.md` | ✅ | ✅（25,561 B） | ✅ |
| `round-2/E03/with-skill.md` | ✅ | ✅（11,884 B） | ✅ |

两个文件均由独立子代理会话生成后，用 Read 工具逐一复核通过，未出现"调用成功但文件缺失"的情况。

## Session 独立性

- **baseline**：全新启动的独立子代理，只接收原始 prompt，未接触任何 Skill 文件。
- **with-skill**：另一个全新启动的独立子代理，预加载内容仅为 `SKILL.md` 全文；references 按 SKILL.md 加载条件由代理自行打开。两个会话互不共享上下文，未复用 Round-1 输出。

## with-skill 实际 reference 读取顺序（agent 自报 + 产物核对）

1. `references/source-strategy.md` — 任务理解完成、开始联网搜索前（确定关键词与来源优先级）
2. `references/volatile-fact-check.md` — 第一轮搜索拿到配置类候选后（命中高风险事实核验：安装/配置、endpoint、环境变量、模型兼容）
3. `references/selection-heuristics.md` — 交叉核验完成、进入最终候选横向取舍时

与 SKILL.md 加载条件一致，未提前批量读取。

## 最终推荐数量

| 组 | 最终推荐数 | 说明 |
|---|---|---|
| baseline | 多条（按"权威基线 + OpenRouter 主线 + 第三方模型线"分层，含官方文档、官方博客、开源网关等） | 分组呈现 |
| with-skill | 2 | OpenRouter 官方 cookbook + claude-code-router 官方仓库 |

## 实质性事实 / 选择差异（同一 Round 内对比）

1. **高风险事实核验的显式化**：with-skill 明确命中 `volatile-fact-check.md` 并完成 6 项核验；两组都正确排除了废弃变量 `ANTHROPIC_SMALL_FAST_MODEL` 与"用 `OPENAI_BASE_URL` 配置"的相悖说法，这一点行为一致。
2. **推荐位纪律**：with-skill 将 Anthropic 官方《llm-gateway-connect》判为"证据锚点而非占位推荐"（内容已被推荐 #1 引用覆盖），保持 2 个推荐位；baseline 将两份 Anthropic 官方文档都列为独立"权威基线"条目，未做同一证据去重。
3. **兼容范围边界**：两组都区分了"OpenRouter 官方仅保证 Anthropic 模型"与"非 Anthropic 模型需第三方网关"，未把 OpenRouter 原生路径包装成通用保证；with-skill 以 claude-code-router 官方仓库（v3.0.22, 2026-08-24）作为活跃维护证据，baseline 对第三方网关的当前维护状态表述较弱。
4. **endpoint 细节**：两组一致确认 base URL 为 `https://openrouter.ai/api`（不带 `/v1`）；with-skill 额外提示"Claude Code 自行追加 `/v1/messages`"，且明确 `ANTHROPIC_API_KEY=""` 必须显式留空，避免回退官方认证。

## 跨 Round 比较声明

本 evidence 的所有产品结论均只基于 Round 2 内 baseline vs with-skill 配对，未使用 Round-1 数据做任何结论支撑。
