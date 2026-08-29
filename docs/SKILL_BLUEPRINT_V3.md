# ERP AI Curator — Skill Blueprint V3

> Design only. Do not implement until the working model has enough real-task support.

## 1. Skill 的真正职责

Skill 不负责“维护一个 ERP AI 资源库”。

Skill 负责稳定执行一个判断：

> **面对当前泛 ERP / 企业信息化任务，最合适的 AI 工作方式是什么？是否真的需要引入专门能力？**

随着来源采编测试推进，它还出现了一个有限的第二职责：

> **当外部资源发现确实需要某个平台专门读取能力时，判断是否应调用已经安装且已批准的来源 Skill / MCP，并把获取到的证据重新交回 Curator 判断。**

因此它更接近一个 **bounded orchestration / curator Skill**，而不是任意发现、安装和执行第三方 Skill 的“万能元 Skill”。

## 2. Trigger

### Trigger when

用户正在选择 / 探索 AI 工作方式，例如：

- “这个工作怎么用 AI 做得更好？”
- “有没有更合适的 AI 方法？”
- “值得装一个 Skill 吗？”
- “什么 Tool 能做到这个？”
- “帮我找一个现成方案。”

### Do not hijack

用户只是要求直接完成一次任务：

- explain / write / code / summarize / draw / analyze / generate artifact。

如果用户的目标是“把事情做完”，优先直接做；如果目标是“选一种以后反复使用的 AI 做法”，再进入 Skill。

## 3. Main flow

主 Skill 只需要这条链：

```text
1. Understand the real work outcome and hard constraints
2. Run the AI leverage test against the user's current stack
3. Choose Mode A / B / C
4. If Mode B needs discovery, search narrowly
5. If normal Web/GitHub cannot acquire needed evidence, route to an approved installed source adapter when useful
6. Compare only serious candidates
7. Verify volatile facts only when needed
8. Return an actionable working recommendation
```

第 1 步的 hard constraints 只抓真正会决定方案可用性的条件，例如：

- 数据 / 源码能否离开当前环境；
- 必须本地还是允许云端；
- 是否需要特定可编辑格式、系统集成或权限；
- 版本、成本、企业账号等明显边界。

不要把搜索放到第 1 步。

## 4. AI Leverage Test — 核心判断

专门 Tool / Skill / Method 是否值得引入，主要看有没有一个**用户当前工具链无法很好提供的能力缺口**。

这里的 baseline 不是“裸模型”，而是用户已经拥有并可以使用的：

- 通用 AI / coding Agent；
- 企业已批准工具；
- 内部 exporter / pipeline；
- 现有知识库、IDE、ALM、测试或自动化能力。

新方案必须相对这个真实 baseline 有足够增量价值。

### Signal 1 — Special output / protocol constraint

例如：

- 必须生成原生 editable `.drawio`；
- 必须写入特定 ALM / issue tracker；
- 必须产生可机器执行的固定协议 / schema；
- 必须连接真实 IDE / repo / database / system。

这类通常支持 Mode B。

### Signal 2 — Unique data / knowledge access

例如：

- 专有产品知识库；
- 企业内部知识源；
- 当前系统真实数据；
- 通用 Web 模型拿不到的权限内容；
- 普通 Web 路径难以稳定读取的平台原文或字幕。

如果这种访问直接决定质量，专门方案可能有明显价值。

反过来，如果候选方案不能满足客户数据、源码或企业合规边界，它即使能力很强也不是可用方案。

### Signal 3 — Runtime observation / action

例如：

- tracing；
- browser / system interaction；
- test execution；
- deployment state；
- codebase scanning；
- API calling。

通用聊天模型无法仅靠 Prompt 获得这些真实能力。

### Signal 4 — Repeated deterministic or structured work

如果同一类工作会高频重复，并且存在稳定步骤：

- extraction；
- conversion；
- validation；
- synchronization；
- generation with strict format。

专门 workflow / Skill 才可能抵消安装和学习成本。

一次性任务通常先 Mode A/C。

### Signal 5 — High-volatility setup / compatibility

例如：

- model routing；
- API / endpoint；
- environment variables；
- plugin / version compatibility；
- pricing / provider support。

这类通常需要当前专门资料和事实核验。

## 5. Current-stack Sufficiency Test

以下特征越多，越应该优先 Mode A：

- 一次性任务；
- 输入材料已经齐全；
- 主要是理解、分析、改写、总结、规划或生成草稿；
- 用户现有 Agent / 工具已经可以完成；
- 没有真实系统操作；
- 没有特殊可编辑 / 协议格式；
- 输出可以由用户快速人工判断；
- 新 Tool 只是“可能更方便”，没有明显质量 / 时间增益。

但 Mode A 不等于“凭模型记忆直接回答”。

对于 ERP 业务、配置、代码、接口等专业内容，优先采用 **source-grounded working method**：围绕用户材料、项目文档、代码、配置或可信知识源分析，并让关键结论可回溯。

不要因为发现了一个相关 Skill 就倒推它有必要。

## 6. Mode C — 防止过度自信

当以下情况出现时，不要强行 A 或 B：

- 不知道这是一次性还是高频工作；
- 不知道用户当前 Agent / 工具已经能做到什么水平；
- 专门方案需要较高安装 / 配置 / 迁移成本；
- 理论上有优势，但缺少真实使用证据。

此时给最小试验：

> “先用现有 Agent / 工具完成一个真实样本。如果出现 X 问题，再升级到 Y 类专门能力。”

Mode C 必须包含：

- 一个具体最小试验；
- 一个明确 upgrade signal。

没有这两项，就只是犹豫，不是合法 Mode C。

## 7. Discovery fast path

如果用户已经明确提出专门能力约束，例如：

> “我需要一个能直接输出 editable draw.io 的 Agent Skill。”

不需要重新长篇论证“AI 能不能帮忙”。

可以直接：

`确认约束 → 定向发现 → 阅读原始材料 → 比较 → 推荐`

但“用户说要 Skill”仍然只是一个 solution hypothesis，不是强制 Mode B。

如果需求明显是一次性简单任务、专门 Skill 没有可解释的增量价值，仍可以回答：

> “这个任务不值得额外装 Skill，现有工具链已经够。”

Fast path 的意思是减少流程，不是无条件接受用户预设解法。

## 8. Search strategy

只有 Mode B 需要外部发现时：

- 搜索问题写成“能力缺口”，不是宽泛场景；
- 优先找能直接证明产出的原始 repo / demo / tutorial；
- GitHub / community / practitioner / official 都可竞争；
- 官方不是默认 Top 1；
- high-volatility claim 才重点回官方核验；
- 历史 Starter Pack 只作为先验，不作为答案；
- 结论稳定就停。

当普通 Web/GitHub 已足够时，不因为已经安装了平台适配器就额外调用它们。

## 9. Source-adapter orchestration

### 9.1 Runtime principle

未来 Curator Skill 可以调用**已经安装、已经资格审查、与当前证据缺口匹配**的来源 Skill / MCP。

主 Skill 只需要知道能力，例如：

- `wechat_discover_public_articles`
- `wechat_read_public_article`
- `bilibili_search_public_videos`
- `bilibili_read_transcript`
- `xiaohongshu_search_public_notes`
- `xiaohongshu_read_public_note`

不要把产品逻辑绑定到具体仓库名。

### 9.2 Runtime 不安装、不更新

普通资源采编任务中：

- 可以检测已安装能力；
- 可以按需调用；
- 缺失时优先降级到普通 Web/GitHub；
- 仍然缺证据时明确 Coverage gap。

默认禁止：

- 在用户当前采编任务中临时发现并安装任意第三方 Skill；
- 运行中自动升级到 `latest`；
- 因为第三方 MCP 暴露了写操作就启用发布、点赞、评论等能力。

安装和更新是单独的维护任务。

### 9.3 安装 / 更新 / 调用契约

详细规则放在：

- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

未来正式 Skill 采用 progressive disclosure，把这些内容压缩为 `references/source-adapter-routing.md`。

其中需要说明：

- capability → provider 映射；
- 固定 commit/release；
- 安装前资格检查；
- read-only 权限；
- credential 本地边界；
- 显式更新流程；
- invocation 条件；
- failure / fallback；
- remove / deprecate。

## 10. Candidate comparison

不做分数表。

只问：

1. 能否解决完整任务？
2. 用户实际会得到什么？
3. 相比用户**当前 AI + 当前工具链**，它的增量价值是什么？
4. 启动 / 安装 / 迁移 / 学习成本是否值得？
5. 是否符合数据、源码、企业环境和权限边界？
6. 当前是否可用？
7. 什么情况下不要用它？

如果第 3 条说不清，默认不推荐专门方案。

## 11. Output contract

### Mode A

```text
判断：不需要新增专门 Tool / Skill
原因：...
建议用现有方式这样做：...
```

### Mode B

```text
判断：值得引入专门能力
主推荐：...
为什么：...
能得到什么：...
怎么开始：...
重要限制：...
原始链接：...
```

只有存在明显不同的适用条件时才给第二推荐。

### Mode C

```text
判断：先不要增加复杂度
最小试验：...
升级条件：如果出现 X，再考虑 Y 类方案
```

## 12. Proposed skill structure

如果未来实现，第一版建议仍然很小：

```text
skills/erp-ai-curator/
├── SKILL.md
└── references/
    ├── leverage-diagnosis.md
    ├── discovery-and-selection.md
    ├── source-adapter-routing.md
    └── volatile-fact-check.md
```

### SKILL.md

只包含：

- trigger / non-trigger；
- 主流程；
- A/B/C；
- 何时读取 references；
- 来源适配器的最小调用原则；
- 输出契约。

### leverage-diagnosis.md

只放通用能力缺口判断，不放 SAP / Oracle / 财务 / 供应链场景清单。

### discovery-and-selection.md

只在 Mode B 需要搜索时加载。

### source-adapter-routing.md

只在普通 Web/GitHub 无法稳定取得所需来源证据时加载。

负责：

- 支持的来源能力；
- 已批准/试点 provider 与 pin；
- 安装与更新维护说明；
- read-only 边界；
- 调用示例；
- fallback / removal。

不要把所有第三方 Skill 的完整 README 复制进来。

### volatile-fact-check.md

只在高波动事实出现时加载。

第一版仍默认 **0 custom scripts**。

只有当真实 Pilot 反复证明“检查已安装 adapter / pin / 可用状态”容易出错时，才考虑一个 deterministic `adapter-doctor`。不要提前造 package manager 或 updater。

## 13. Explicit non-goals

第一版不要：

- 场景百科；
- “SAP 资源区 / Oracle 资源区 / Java ERP 资源区”；
- 资源数据库；
- 固定检索站点清单；
- 星标阈值；
- 100 分评分；
- candidate JSON；
- automated Gate；
- multi-agent pipeline；
- automatic refresh crawler；
- 自动 Skill 商店；
- 运行时自动安装第三方依赖；
- 自动跟随第三方 `latest`。

## 14. Skill 是否值得存在仍需证伪

V3 只是一个更合理的工作模型，不代表一定要封装成 Skill。

现在还多了一项需要验证的价值假设：

> **普通 AI 是否能稳定判断何时需要来源适配器、正确组合多个已安装 Skill/MCP，并在调用后回到统一的 Curator 证据判断，而不是平台各自为政？**

如果普通模型自然就能稳定完成，或者来源适配器只是增加链接数量而不提升推荐质量，不继续为了形式增加架构。
