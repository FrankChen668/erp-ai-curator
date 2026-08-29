# Adversarial Review V3 — AI Leverage Model

Date: 2026-08-29

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

**Already in blueprint.**

---

## A8 — Hidden setup cost

### Attack

一个专门 Skill 明显更强，但安装、账号、权限、迁移、学习成本可能超过收益。

### Finding

Important and currently under-emphasized.

### Correction

Mode B comparison 必须把 **adoption cost** 当成增量价值的一部分。

不是“能力更强”就自动值得推荐。

Current blueprint already asks whether startup cost is worth it; retain prominently.

---

## A9 — Confidentiality / enterprise data

### Attack

泛 ERP 工作经常包含客户数据、源代码、业务流程、合同或配置。推荐第三方 AI 工具可能引入数据泄露风险。

### Finding

High-impact omission.

### Correction

Task understanding must capture material data constraints when relevant:

- local / cloud restriction;
- whether source code / customer data can leave environment;
- enterprise approval / account constraints.

This is not a universal security audit. It is a **hard usability constraint**: a solution that cannot legally/operationally receive the user's data is not a solution.

**Add to V3 blueprint and North Star as a key constraint example.**

---

## A10 — Explicit resource request can still be misguided

### Attack

User says “find me a Skill”, but the right answer may be “you don't need one”. Should explicit resource requests always force Mode B?

### Finding

No.

### Correction

Explicit request creates a fast path, but the Skill should still detect obvious over-tooling.

Example:

> “Find me a Skill to summarize this one paragraph.”

Correct answer can remain Mode A.

Fast path means less ceremony, not automatic acceptance of the user's solution hypothesis.

**Blueprint needs a small wording correction.**

---

## A11 — “Official isn't priority” may overcorrect

### Attack

After avoiding official-document gravity, could the system underweight official sources for product capabilities?

### Finding

Possible.

### Correction

Separate two questions:

1. **Best user working resource** — official has no automatic priority;
2. **Truth of volatile/native capability claims** — official/current original source has high priority.

Current V3 preserves this distinction.

---

## A12 — Skill vs ordinary prompt redundancy

### Attack

A strong model may already reason exactly this way if asked once. Is the Skill unnecessary?

### Finding

Still the largest unresolved product risk.

### Decision

Do not implement merely because the blueprint looks good.

The future Skill is justified only if fresh real tasks show ordinary conversations repeatedly:

- over-tool;
- search too early;
- miss capability gaps;
- fail to distinguish A/B/C;
- recommend resources with unclear incremental value.

If not, keep the model as a training method / prompt framework rather than a Skill.

---

## A13 — Scenario creep through examples

### Attack

Even without a taxonomy, repeated examples may slowly become de facto hard-coded scenarios.

### Finding

Real long-term risk.

### Correction

Only codify a lesson if it can be stated as a **general capability principle**.

Good:

> editable output format can justify specialization.

Bad:

> draw.io tasks always use jgraph.

---

## A14 — Evaluation can again become self-proof

### Attack

Owner-generated tasks + cloud reasoning can still prove its own model.

### Finding

Yes.

### Decision

OWNER_REAL replay is design falsification only.

Primary product validation remains independent REAL_USER behavior / judgement when available.

Do not invent user quotas or synthetic coverage to compensate for missing data.

---

# Final adversarial conclusion

V3 is materially better aligned with the original product intent than the resource-first Phase 2/3 model, but only if three boundaries remain explicit:

1. **Work-method navigation, not universal task execution**;
2. **General AI sufficiency must still consider true capability gaps and source grounding**;
3. **Specialized capability must justify its adoption/privacy cost, not merely be more feature-rich.**

The biggest unresolved question remains:

> **Does this need to be a Skill at all, or is it already a good reusable working method for a strong model?**

Do not resolve that question by adding more architecture. Resolve it later with fresh real tasks.
