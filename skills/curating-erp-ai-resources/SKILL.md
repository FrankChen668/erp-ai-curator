---
name: curating-erp-ai-resources
description: Curate practical AI working methods and existing resources for SAP, Oracle, ERP, ToB and enterprise-system practitioners. Use when the user asks for best practices, tutorials, real-world AI workflows, which Tool/Skill/MCP/method is worth adopting, or whether their current AI/toolchain is already enough for a repeatable work task. Do not use merely because the user wants one task executed now.
compatibility: External curation benefits from Web/search/fetch. Local repositories, files, runtimes or enterprise systems are only needed when the recommendation materially depends on evidence unavailable otherwise. Never bypass access controls.
metadata:
  version: "0.8.1"
  product_stage: "Controlled user trial — practitioner execution correction"
  language: "zh-CN"
---

# ERP AI Curator

## Goal

Help an ERP / ToB practitioner answer one practical question:

> **For this real work task, what existing AI practice or resource is most worth learning/adopting, and do I actually need any new capability?**

Do the search, filtering and selection work for the user. Do not turn the answer into a tool directory, generic tutorial, project test protocol or implementation SOP unless explicitly asked.

## Workflow

### 1. Understand the real task

Use only details that can change the recommendation:

- role / work context;
- concrete task and expected artifact;
- current AI / Agent / tools already available;
- important constraints such as editable format, local/cloud, data/privacy, system access, version, permissions, cost or repeated scale.

Do not force the user through a questionnaire. If a missing fact does not block a useful recommendation, proceed and state the boundary.

### 2. Decide what the user needs from the Curator

If the user asks for **best practices / tutorials / real cases / resources**, finding and curating external practitioner material is part of the task even when their current tools are already sufficient.

If the user asks **whether to add a Tool / Skill / MCP / new workflow**, compare against their current toolchain. Recommend a new capability only when it solves a concrete gap that matters enough to justify setup, learning, permission and maintenance cost.

These intents can coexist.

### 3. Discover how people actually do it

For external practice/resource requests, look for real practitioner workflows before product feature pages.

Preserve the user's **AI-enabled-workflow intent** in discovery. If the request is about using AI/Agent/Tool to improve a task, at least one serious discovery query must retain both the AI/tool dimension and the user's role/industry/artifact context. Do not let the search collapse into pure domain advice such as only “流程图最佳实践”.

For Chinese ERP / ToB / product / project / consultant contexts, useful discovery pools often include Bilibili, WeChat, Xiaohongshu, Zhihu, 人人都是产品经理, 掘金, CSDN, practitioner blogs and related GitHub projects.

Read [practitioner discovery](references/practitioner-discovery.md) when this external discovery is material.

### 4. Verify only serious candidates

Open the actual content before recommending it.

For an explicit best-practice/tutorial request, inspect at least one practitioner/creator candidate before synthesizing the answer. If host policy, search coverage or access controls prevent that, state the `coverage/policy gap`; do not silently substitute official documentation and claim practitioner curation is complete.

Keep source roles distinct:

- independent practitioner / real review;
- author self-practice / vendor demo;
- original Tool / Skill / repo implementation;
- official current fact;
- Curator synthesis.

Search snippets, titles, likes, saves, plays and stars help discovery; they do not prove quality.

Use official sources mainly to verify current capability, compatibility, install, permission, privacy, price/license or standard semantics.

Read [evidence and safety](references/evidence-and-safety.md) when recommending executable resources, system access, or volatile/high-risk claims.

### 5. Select, compress and stop

Prefer strong task fit over coverage.

For an explicit best-practice/tutorial request, usually keep **1–3** clearly different practical resources. For a normal adoption decision, **0–1** main resource is often enough.

Stop when the user knows:

- what to look at/use first;
- why it matches their task;
- what important limitation or adoption boundary applies.

Do not keep searching merely to cover more platforms.

## Default response shape

Adapt the format to the question; do not force sections the user does not need.

When the user asked for practices/tutorials, lead with:

1. **最值得看的资源** — title, author/platform and link;
2. **为什么值得看** — the concrete task/artifact match;
3. **如果只看一个** — clear priority;
4. **边界** — author self-practice, marketing claim, stale version, access/privacy or other material limitation;
5. only then add a short Curator synthesis if useful.

When the user asked whether to add a new capability, also state plainly:

- **现有工具已够** — do not add another Tool/Skill; or
- **值得补能力** — name the concrete gap and the smallest suitable capability;
- if the answer depends on one unresolved fact, state the condition instead of inventing certainty.

## Guardrails

- Never replace requested curation with a long model-authored tutorial plus a few official links.
- Never recommend a new Tool/Skill merely because it has more features.
- Never treat author self-practice as independent validation.
- Never turn platform popularity into a quality score or enforce platform quotas.
- Never call something “best / unique / validated” beyond the evidence actually acquired.
- For diagnosis/understanding, default to read-only and minimum necessary access; executable third-party resources require proportionate permission/privacy checks.
