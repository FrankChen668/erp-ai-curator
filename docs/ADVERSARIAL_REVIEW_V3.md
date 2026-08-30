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

---

## A3 — Over-discovery: Mode B 又变成无止境搜索

### Attack

只要进入 Mode B，Agent 会不会再次花大量时间翻官网、GitHub、文章、视频？

### Finding

Real risk, historically observed.

### Correction

搜索必须绑定一个明确 capability gap；结论稳定即停止。

“搜索来源数量”不是质量指标。

---

## A4 — Memory gravity: Starter Pack 变成隐藏答案库

### Attack

仓库已经知道 drawio、baoyu、OpenRouter 等资源。Agent 会不会每次都把新问题导向旧资源？

### Finding

Real risk.

### Correction

历史资源只能做 search prior，不占默认推荐位。

先做 leverage diagnosis，再看历史候选是否仍符合当前能力缺口。

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

---

## A6 — Domain risk: 通用 AI 能做，但可能胡说业务知识

### Attack

“陌生模块学习 → Mode A”可能低估 ERP 领域幻觉风险。

### Finding

Real risk.

### Correction

Mode A 不等于“凭模型记忆回答”。

对于专业业务 / 系统知识，通用 AI 的正确工作方式应优先是 **source-grounded analysis**：用户材料、官方/项目文档、代码、配置或可信知识源。

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

---

## A8 — Hidden setup cost

### Attack

一个专门 Skill 明显更强，但安装、账号、权限、迁移、学习成本可能超过收益。

### Finding

Important.

### Correction

Mode B comparison 必须把 **adoption cost** 当成增量价值的一部分。

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

只有真实任务反复证明普通对话会持续偏航，才值得封装。

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

---

## A18 — Validation-lab drift: 每个候选都要自己测

### Attack

为了避免误推荐，会不会形成：发现一个 Skill → 静态审查 → 安装 → runtime → artifact → 再测一轮，最终 Curator 变成工具实验室？

### Finding

Already happened.

### Correction

本地实测是**例外**，不是默认流水线。

仅当高价值第三方证据缺失/冲突、风险高、准备长期标准化或关键能力仅靠文档无法确认时做最小实测。

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

---

## A20 — Research-environment bias

### Attack

本地研究 Agent 是 Codex，会不会自然更容易发现和推荐 Codex Plugin / GitHub Skill，而忽略普通顾问更低摩擦的浏览器、SaaS、视频教程和社区工作流？

### Finding

Observed in P04A.

### Correction

当一个任务存在明显不同的采用边界时，至少审视一个**非当前研究环境原生**的可行路径。

---

## A21 — Platform checklist drift

### Attack

既然强调 B站、微信、小红书，会不会又变成“每题必须三平台都搜一遍”？

### Finding

Possible.

### Correction

第三方实操优先是**证据角色原则**，不是平台配额。

来源数量和平台覆盖率都不是 KPI。

---

## A22 — False independence: 作者自测被当成第三方测评

### Attack

一篇看起来很像“实测”的文章/视频，其实就是 Skill 作者、厂商员工、合作伙伴或带货账号自己做的。Curator 会不会把它当独立经验？

### Finding

High risk under practitioner-first strategy.

### Correction

当关系公开可观察且会影响判断时，区分：

- independent practitioner;
- author/maintainer;
- vendor/employee/partner;
- affiliate/sponsored/course seller;
- unknown.

作者教程可以证明“怎么操作”，但不能自动证明“独立用户觉得值得用”。

利益关系不自动淘汰内容，但会降低对比较性/夸张性结论的信任。

---

## A23 — Social echo: 多个平台其实都在复读同一个 Demo

### Attack

B站、小红书、公众号出现十篇相似内容，是否会被误判成“很多人都验证过”？

### Finding

Very plausible in fast-moving AI topics.

### Correction

识别内容血缘：相同截图、Prompt、Demo、上游仓库、相同数字结论通常属于同一 evidence family。

只有新增不同输入、失败案例、返工过程、长期使用、企业限制等才算真正增量证据。

**Social repetition ≠ independent corroboration.**

---

## A24 — Tutorial staleness: 方法没过时，操作步骤已经过时

### Attack

高质量实操文章可能半年后仍有方法价值，但 UI、安装命令、模型名、插件能力已经变化。Curator 会不会整篇判“可用”或整篇判“过期”？

### Finding

Real risk.

### Correction

强制分开：

- stable practice insight;
- version-coupled instruction.

稳定经验可保留；版本耦合事实必须按当前原始/官方来源复核。

资源被留存时尽量记录 last checked 与关键版本/commit（仅在相关时）。

---

## A25 — Safety pendulum: 为了不重测试，直接推荐安装第三方 Skill

### Attack

“runtime test 是例外”会不会被 Agent 错解成“无需安全检查”？

### Finding

High-impact for enterprise users.

### Correction

必须区分：

```text
lightweight static safety review = installable recommendation minimum
runtime/artifact certification = exception
```

若建议同事安装第三方 Skill/MCP/plugin/script，最低限度检查可见的安装命令、依赖、凭据、文件/网络/浏览器/账号权限、写操作、明显数据外发、许可证/维护状态。

这不是实验室认证；只是避免把未知可执行代码轻率推荐进企业环境。

如果只推荐“阅读/学习这篇教程”，不需要把学习价值和安装安全捆绑。

---

## A26 — Stale asset memory: 今天精选，半年后变成隐藏旧答案

### Attack

一旦资源进入项目资产，后续 Agent 会不会把它当永久批准答案，重新产生 Starter Pack gravity？

### Finding

Real risk.

### Correction

保留资源时只记录轻量 provenance：解决什么 Problem Card、原始 URL、证据类型、重要限制、必要版本/commit、last checked、`retain/conditional/stale-recheck`。

历史资产只能做 search prior；高波动事实复用时仍要检查当前状态。

不因此建设大型数据库或自动 Refresh 系统。

---

## A27 — Proxy-goal substitution: 用工程完成感替代产品进展

### Attack

当当前目标已经变成“真实用户实际采用”后，Agent 会不会因为 smoke test、readiness、Quickstart、PR、PASS 更容易完成，而把这些代理指标当成下一步？

### Finding

**Observed. High risk.**

### Correction

所有任务必须先映射当前里程碑，并通过反事实检查：

> **如果任务完美完成，但真实用户没有因此更快做选择/开始工作/减少返工，也没有解除真实 Pilot 的明确阻塞，项目是否更接近目标？**

若否，不执行。

文档、测试、Commit、PASS 都是手段，不能单独成为产品进度。

---

## A28 — Agent-utilization bias: 因为有本地 Agent 就制造任务

### Attack

Owner 问“本地 Agent 做什么”时，Cloud 会不会默认必须给它安排任务，从而制造原本不存在的工作？

### Finding

**Observed.**

### Correction

本地 Agent 是能力，不是待填满的产能。

> **“Agent 现在没有里程碑相关任务”是合法且可能最优的结论。**

任何本地 Task Envelope 都必须明确：

- `milestone_link`；
- `user_evidence_created`。

任一为空，不下发。

---

## A29 — Phase regression: 已进入真实用户阶段又退回自我验证

### Attack

项目在某阶段已经完成方法验证后，会不会因为新的不确定感，再回到 synthetic card、smoke、benchmark、readiness 流水线？

### Finding

**Observed immediately after V0.1.**

### Correction

阶段升级后默认单向推进。

回退到验证阶段只允许两种理由：

1. 真实用户使用暴露了一个会改变核心产品假设的 material failure；
2. 一个真实 Pilot 被具体技术/安全问题阻断，且必须用最小验证解除。

“想再确认一下”不够。

---

## A30 — Self-test mutation: 自己出的测试又驱动自己改产品

### Attack

Cloud/Local 自己设计测试、自己判失败、再据此修改 Skill，会不会形成自洽但脱离用户的闭环？

### Finding

High risk; closely related to A14 but stronger after productization.

### Correction

Synthetic/smoke/regression 主要用于：

- 实现回归；
- design falsification；
- 修复真实使用已暴露的问题。

它们不能单独触发新的产品方向、功能体系或治理机制。

真实用户阶段的产品变化，优先由**真实使用摩擦**触发。

---

# Final adversarial conclusion

V3 只有在以下边界同时成立时才不会再次偏航：

1. **真实工作问题驱动，而不是工具/场景目录驱动；**
2. **用户采用问题优先看第三方实操/测评，官方主要负责易变化事实核验；**
3. **第三方内容必须区分独立经验、作者自述和商业利益，并防止社交复读被当成多重验证；**
4. **平台获取能力与平台内容价值严格分开；**
5. **现有 PM/Agent/WorkBuddy/Skill 生态优先复用，Curator before Builder；**
6. **runtime / artifact test 是必要时的最小补证，但可执行资源在推荐安装前仍需最低限度静态安全审查；**
7. **教程的稳定经验和版本耦合操作必须分开；**
8. **已留存资源是 search prior，不是永久批准；**
9. **研究环境、作者名气、互动量都不能替代任务匹配和具体内容证据；**
10. **任何任务先证明它推进当前里程碑，禁止用工程产物、PASS 或 Agent 利用率替代产品进展；**
11. **阶段升级后不因“再确认一下”退回自我验证，真实用户摩擦才是产品化后的主要学习源。**

当前最大的执行风险不再是“能不能搜到资源”，而是：

> **是否会在已经进入真实用户阶段后，又因为 AI Agent 擅长生成测试、文档和工程任务，而重新优化那些容易完成、但不改变真实用户结果的代理目标。**

对此的主防线不是更多测试，而是固定目标层级：

```text
North Star → current milestone → real user outcome/evidence → task → artifact/test/Agent
```
