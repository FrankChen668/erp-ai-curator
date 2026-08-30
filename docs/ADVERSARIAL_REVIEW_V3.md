# Adversarial Review V3 — AI Leverage Model

Date: 2026-08-30

Question: if `AI_LEVERAGE_MODEL_V3` is wrong, how will it fail?

## A1 — Scope inflation: 变成万能 AI 顾问

### Attack

从“资源推荐器”扩展成“AI 工作方式导航器”后，是否会开始回答所有 AI 问题，最终变成没有边界的通用 Agent？

### Finding

Real risk.

### Boundary

Skill 只处理 **工作方式选择**：

- 通用 AI 是否够；
- 是否值得引入专门能力；
- 该选哪类 / 哪个现成方案。

它不抢占用户要求的直接执行任务。

**Keep.**

---

## A2 — Under-discovery: 太容易说“通用 AI 就够”

### Attack

Mode A 会不会成为新的 lazy answer，导致真正高价值 Tool / Skill 被漏掉？

### Finding

Real risk.

### Correction

Mode A 不能基于“LLM 理论上能做”就结束。

至少要问：

> 是否存在通用模型本身无法提供的能力缺口，例如真实系统访问、特殊可编辑格式、专有知识、runtime evidence、重复自动化或高波动兼容性？

如果存在，必须进入 B/C 判断。

**Already covered by the Leverage Test. No new Gate needed.**

---

## A3 — Over-discovery: Mode B 又变成无止境搜索

### Attack

只要进入 Mode B，Agent 会不会再次花大量时间翻官网、GitHub、文章、视频？

### Finding

Real risk, historically observed.

### Correction

搜索必须绑定一个明确 capability gap；结论稳定即停止。

“搜索来源数量”不是质量指标。

**Keep current design.**

---

## A4 — Memory gravity: Starter Pack 变成隐藏答案库

### Attack

仓库已经知道 drawio、baoyu、OpenRouter 等资源。Agent 会不会每次都把新问题导向旧资源？

### Finding

Real risk.

### Correction

历史资源只能做 search prior，不占默认推荐位。

先做 leverage diagnosis，再看历史候选是否仍符合当前能力缺口。

**Keep.**

---

## A5 — Generalized ERP becomes too generic

### Attack

把范围扩大到 SAP / Oracle / Java 定制系统以后，会不会失去 ERP 特性，最终变成通用知识工作者 Skill？

### Finding

Moderate risk.

### Boundary

用户工作必须属于企业信息化 / 企业系统交付语境，例如：

- 业务流程与需求；
- 企业应用设计；
- 实施、配置、二开、集成；
- 项目交付；
- 企业系统开发、测试、运维；
- 企业软件学习与分析。

普通个人效率、消费应用、纯创意娱乐不属于产品主范围。

不需要产品厂商 taxonomy，但需要 **enterprise-system work context**。

---

## A6 — Domain risk: 通用 AI 能做，但可能胡说业务知识

### Attack

“陌生模块学习 → Mode A”可能低估 ERP 领域幻觉风险。

### Finding

Real risk.

### Correction

Mode A 不等于“凭模型记忆回答”。

对于专业业务 / 系统知识，通用 AI 的正确工作方式应优先是 **source-grounded analysis**：用户材料、官方/项目文档、代码、配置或可信知识源。

这仍然不等于必须安装专门 Skill。

**Add as a general principle, not a scenario rule.**

---

## A7 — Mode C becomes procrastination

### Attack

Agent 不敢做判断时会不会都说“先试一下”？

### Finding

Real risk.

### Correction

Mode C 只能在“专门方案增量价值不确定且引入成本不可忽略”时使用。

必须给：

- 一个具体最小试验；
- 一个明确 upgrade signal。

没有这两项就不是合法 Mode C。

---

## A8 — Hidden setup cost

### Attack

一个专门 Skill 明显更强，但安装、账号、权限、迁移、学习成本可能超过收益。

### Finding

Important.

### Correction

Mode B comparison 必须把 **adoption cost** 当成增量价值的一部分。

不是“能力更强”就自动值得推荐。

---

## A9 — Confidentiality / enterprise data

### Attack

泛 ERP 工作经常包含客户数据、源代码、业务流程、合同或配置。推荐第三方 AI 工具可能引入数据泄露风险。

### Finding

High-impact.

### Correction

Task understanding must capture material data constraints when relevant:

- local / cloud restriction;
- whether source code / customer data can leave environment;
- enterprise approval / account constraints.

这不是 universal security audit，而是**可用性硬约束**。

---

## A10 — Explicit resource request can still be misguided

### Attack

用户说“find me a Skill”，但正确答案可能是“不需要装”。

### Finding

Yes.

### Correction

Explicit request creates a fast path, not automatic Mode B acceptance.

---

## A11 — “Official isn't priority” may overcorrect

### Attack

避免官网重力以后，会不会反过来低估官方事实？

### Finding

Possible.

### Correction

分开两个问题：

1. **Best user working resource** — 官方没有默认优先权；
2. **Truth of volatile/native capability claims** — 官方 / 当前原始来源优先。

---

## A12 — Skill vs ordinary prompt redundancy

### Attack

强模型本身可能已经能完成这些判断，Skill 是否多余？

### Finding

Still a major unresolved risk.

### Decision

不要因为 blueprint 看起来完整就实现 Skill。

只有真实任务反复证明普通对话会：

- over-tool；
- search too early；
- miss capability gaps；
- 推荐资源但说不清增量价值；
- 在来源与证据选择上反复偏航；

才值得封装。

---

## A13 — Scenario creep through examples

### Attack

示例会不会慢慢变成事实上的 hard-coded scenario？

### Finding

Real long-term risk.

### Correction

只固化**通用能力原则**，不固化“某类任务必用某工具”。

---

## A14 — Evaluation can again become self-proof

### Attack

Owner-generated tasks + cloud reasoning 会不会继续证明自己的模型？

### Finding

Yes.

### Decision

OWNER_REAL replay 只用于 design falsification。

Primary product validation 仍来自真实用户问题、真实资源使用和实际 judgement。

---

## A15 — Official gravity: 把官网当用户答案

### Attack

Agent 为了“可信”会不会优先返回厂商文档，而用户真正需要的是别人怎么用、有哪些坑、值不值得学？

### Finding

Historically observed.

### Correction

对采用/学习型问题，默认顺序应是：

```text
第三方实操 / 测评 / 案例
→ 原始 Skill / Tool / 仓库
→ 官方当前事实兜底
```

官方可以证明“功能存在”，不能自动证明“这是最值得用户学习的资源”。

**Permanent boundary.**

---

## A16 — Practitioner-first overcorrection: 把网红经验当事实

### Attack

第三方优先后，会不会被高赞视频、公众号、UP主测评带偏？

### Finding

Real risk.

### Correction

第三方实操优先解决“怎么用 / 有什么坑”，但：

- 必须实际读取具体内容；
- engagement 只影响 discovery order；
- 版本、安装、兼容、价格、隐私、许可证等事实必须回原始/官方核验；
- 如果隐藏作者名和互动数据后内容不值得推荐，则淘汰。

**Practitioner-first ≠ practitioner-authority.**

---

## A17 — Access failure ≠ content absence

### Attack

当前 Agent 读不到 B站字幕、小红书正文或某公众号时，会不会得出“这个平台没好内容”或干脆不搜？

### Finding

Historically observed.

### Correction

必须分开：

```text
Discovery available?
Full-content acquisition available?
Content quality if acquired?
```

普通 Web 能发现就先发现；完整内容拿不到时再按需使用已批准 Adapter；仍拿不到则记录 Coverage gap。

**任何 acquisition failure 都不能直接转化成平台价值判断。**

---

## A18 — Validation-lab drift: 每个候选都要自己测

### Attack

为了避免误推荐，会不会形成：发现一个 Skill → 静态审查 → 安装 → runtime → artifact → 再测一轮，最终 Curator 变成工具实验室？

### Finding

Already happened.

### Correction

本地实测是**例外**，不是默认流水线。

仅当：

- 高价值第三方证据缺失；
- 第三方结论冲突；
- 安装/权限/安全风险高；
- 准备作为内部长期标准；
- 关键能力仅靠文档无法确认；

才做最小实测。

否则 `第三方实操 + 原始实现 + 必要官方事实` 足以进入推荐。

**Do not prove every recommendation from scratch.**

---

## A19 — Ecosystem reinvention: 重复建设别人已有的知识库

### Attack

项目会不会开始自己整理 PM Skills、WorkBuddy 教程、Codex 手册、PRD/原型/流程图方法论，最后变成另一个内容库？

### Finding

High risk.

### Correction

现有 PM/BA Skill 库、Agent 教程、社区蓝皮书、作者专题、实战系列首先作为 **feeder ecosystem**。

Curator 的价值是：

> **把已有生态映射到真实 ERP 工作问题，并筛到少量最值得用的内容。**

只有现有生态有明确缺口时才补 Curator synthesis，而且必须标注。

**Curator before Builder.**

---

## A20 — Research-environment bias

### Attack

本地研究 Agent 是 Codex，会不会自然更容易发现和推荐 Codex Plugin / GitHub Skill，而忽略普通顾问更低摩擦的浏览器、SaaS、视频教程和社区工作流？

### Finding

Observed in P04A.

### Correction

当一个任务存在明显不同的采用边界时，至少审视一个**非当前研究环境原生**的可行路径。

不是为了凑方案，而是为了防止“我用什么研究，就推荐什么”。

---

## A21 — Platform checklist drift

### Attack

既然强调 B站、微信、小红书，会不会又变成“每题必须三平台都搜一遍”？

### Finding

Possible.

### Correction

第三方实操优先是**证据角色原则**，不是平台配额。

如果一个高质量 B站教程已经给出完整实操，不需要为了形式再搜小红书；反之亦然。

来源数量和平台覆盖率都不是 KPI。

---

# Final adversarial conclusion

V3 只有在以下边界同时成立时才不会再次偏航：

1. **真实工作问题驱动，而不是工具/场景目录驱动；**
2. **用户采用问题优先看第三方实操/测评，官方主要负责易变化事实核验；**
3. **平台获取能力与平台内容价值严格分开；**
4. **现有 PM/Agent/WorkBuddy/Skill 生态优先复用，Curator before Builder；**
5. **runtime / artifact test 是必要时的最小补证，不是默认流水线；**
6. **研究环境、作者名气、互动量都不能替代任务匹配和具体内容证据。**

最大的产品风险已经从“能不能搜到资源”转成：

> **能否稳定从大量现成互联网经验中，挑出真正能解决当前 ERP 项目问题的少量内容，而不重新造轮子。**

下一阶段应该用持续真实采编来回答，而不是继续增加验证架构。
