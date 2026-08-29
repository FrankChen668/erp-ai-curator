# OWNER_REAL Trigger Negatives 01

Date: 2026-08-29

Purpose: validate when ERP AI Curator should **not** enter the conversation.

These are real owner-origin work patterns from the project context. Their value is not resource recommendation quality; their value is preventing the Curator from becoming a universal Agent.

## TN01 — “Graph Engineering 是什么？简单讲下”

**Source:** OWNER_REAL  
**Need external resource?** no, unless the user later asks for a concrete Skill/tool to try.

Correct behavior:

- directly explain the concept;
- distinguish architecture/workflow graph from runtime observability and static diagrams;
- use web/current sources if the term is recent or ambiguous;
- do **not** start by recommending 0–2 resources.

Why Curator exits:

The user needs understanding, not a resource decision.

---

## TN02 — “这个 Graph Engineering Skill 是侵入性的，还是进去纯绘制 graph？”

**Source:** OWNER_REAL  
**Need external resource?** usually no.

Correct behavior:

- inspect the specific referenced Skill/repository;
- answer what it changes and what it does not change;
- if the user asks “有没有更适合我、只读可视化的工具”，then Curator enters.

Why Curator exits initially:

This is a specific-resource due-diligence question, not a discovery request.

---

## TN03 — “帮我看这个 SPEC / 项目代码有没有问题”

**Source:** OWNER_REAL  
**Need external resource?** no.

Correct behavior:

- inspect the provided repo/file;
- review against project boundaries and requirements;
- only search outside resources when a factual standard or comparison is genuinely required.

Why Curator exits:

The job is code/spec review, not selecting a resource.

---

## TN04 — “把这页内容整理成 PPT / 给我一个 AI PPT 提示词”

**Source:** OWNER_REAL  
**Need external resource?** no.

Correct behavior:

- directly draft the slide structure / prompt / artifact;
- do not recommend presentation tools unless the user explicitly asks which tool to use.

---

## TN05 — “双反和合规追溯有什么区别？追溯系统能不能出证明材料？”

**Source:** OWNER_REAL  
**Need external resource?** no, unless the user asks for a reusable external research/tool/resource.

Correct behavior:

- direct domain research and explanation;
- current laws/policies should be verified on the web;
- do not route through Curator just because external sources are needed.

Important distinction:

> **Using sources to answer a question is not the same as helping the user choose an external resource.**

This is a critical trigger boundary.

---

# Trigger principle derived

Curator should trigger only when the user's decision is substantially:

> “What external Skill / Tool / tutorial / method should I use or spend time on?”

It should not trigger merely because:

- web search is needed;
- GitHub is involved;
- the question mentions a Skill;
- an external source is cited;
- AI tooling is the topic.

This boundary is more important than maximizing trigger recall. A Curator that activates on every ERP/AI question becomes a generic assistant with extra search steps.
