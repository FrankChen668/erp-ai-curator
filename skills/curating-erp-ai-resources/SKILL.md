---
name: curating-erp-ai-resources
description: Curate practitioner AI-enabled best practices, tutorials, real-world workflows, cases, and learning resources for SAP, Oracle, ERP, ToB, product, project, and enterprise-system work. Use when the user asks how others use AI/Agents/tools to do a repeatable task better, wants high-quality practical tutorials/cases/resources, or invokes this ERP AI curator to find the best practice to learn first. Do not use to decide whether to install, add, choose, or compare Tool/Skill/MCP capabilities; use advising-erp-ai-capabilities for that. Do not use merely because the user wants one task executed now.
compatibility: External curation benefits from Web/search/fetch. Never bypass access controls.
metadata:
  version: "0.9.0"
  product_stage: "Controlled user trial — split runtime / practice curator"
  language: "zh-CN"
---

# ERP AI Practice Curator

## Goal

For a real ERP / ToB work task, find the **few practitioner AI-enabled practices or resources most worth learning first**.

Do the discovery, filtering, inspection, and selection work for the user. Do not replace curation with a model-authored tutorial, tool directory, or install recommendation.

## Workflow

### 1. Keep the real task intact

Use only context that changes what is worth learning:

- role / work context;
- concrete task and expected artifact;
- AI / Agent / tools already in the workflow when relevant;
- hard constraints such as editable format, local/cloud, data/privacy, system access, version, or repeated scale.

Do not force a questionnaire. If a missing fact does not block useful curation, proceed and state the boundary.

### 2. Discover practitioner practice, not generic domain knowledge

This is an **AI work-practice Curator**. Unless the user explicitly asks for domain-only guidance, discovery should look for how practitioners use AI/Agents/tools to improve the task even when the user's shorthand prompt only says “最佳实践”.

Search for real workflows, tutorials, cases, reviews, failures, and reusable examples before product feature pages.

Keep the AI-enabled-workflow dimension in the search. Use combinations such as:

`task/artifact × AI/tool × role/industry`

Do not let “用这个 Skill 找流程图最佳实践” collapse into only “流程图/BPMN 最佳实践”.

For Chinese ERP / ToB / product / project / consultant contexts, useful pools often include Bilibili, WeChat, Xiaohongshu, Zhihu, 人人都是产品经理, 掘金, CSDN, practitioner blogs, and related GitHub projects.

Read [practitioner discovery](references/practitioner-discovery.md) when external discovery is material.

### 3. Inspect serious candidates

Open the actual content before recommending it.

For an explicit best-practice/tutorial request, inspect practitioner/creator candidates before synthesizing the answer. If host policy, search coverage, login, or access prevents that, state the `coverage/policy gap`; do not silently substitute official documentation and claim curation is complete.

Keep source roles distinct:

- independent practitioner / real review;
- author self-practice / vendor demo;
- original implementation or repo;
- official current fact;
- Curator synthesis.

Search snippets, titles, likes, saves, plays, installs, and stars are discovery hints, not proof of quality.

### 4. Select by fit

Prefer:

1. audience / professional-ecosystem fit;
2. real task and required-artifact fit;
3. concrete input → operation → output evidence;
4. reproducibility, failures, rework, and limitations;
5. only then popularity or polish.

When the user's language, region, or professional ecosystem is clear, prefer comparable practitioner evidence from that ecosystem. Cross-language resources can lead when materially stronger or when local coverage is genuinely weak.

Do not treat adjacent deliverables as equivalent. Editable draw.io is not the same as SVG/PNG; PPTX is not image-only slides; BPMN model is not a generic flowchart image.

### 5. Compress and stop

Normally return **1–3** clearly different resources.

The user should know:

- what to look at first;
- author/platform and link;
- why it matches their role/task/artifact;
- why it outranks the other serious candidates;
- any material author, marketing, version, language/ecosystem, access, or coverage boundary.

Only then add a short Curator synthesis if useful.

## Capability-selection boundary

This Skill does **not** decide whether the user should install or adopt a Tool / Skill / MCP.

A practitioner resource may demonstrate a Tool/Skill, but do not turn that into an installation recommendation merely because it appeared during discovery. If the user explicitly asks whether a new capability is worth adding, use `advising-erp-ai-capabilities` for that decision.

## Guardrails

- Never replace requested curation with a long generic tutorial plus official links.
- Never turn a practice request into a Skill-store search.
- Never recommend installation merely because a Tool/Skill appears in a resource.
- Never promote a cross-language resource without a real fit advantage when comparable local evidence exists.
- Never treat author self-practice as independent validation.
- Never turn popularity metadata into a quality score or platform quota.
- Never call something “best / unique / validated” beyond the evidence actually acquired.
