---
name: advising-erp-ai-capabilities
description: Decide whether an SAP, Oracle, ERP, ToB, product, project, or enterprise-system practitioner should add, install, choose, or compare an AI capability such as a Tool, Skill, MCP, plugin, Agent, model, integration, or new workflow. Use when the user explicitly asks whether their current toolchain is enough, whether a new capability is worth adopting, which capability to choose, or what the smallest useful upgrade is. Do not use for generic best-practice/tutorial/resource curation; use curating-erp-ai-resources for that. Do not use merely because a practitioner resource mentions a Tool/Skill.
compatibility: External adoption advice benefits from Web/search/fetch. Local repositories, runtimes, or enterprise systems are only needed when the decision materially depends on evidence unavailable otherwise. Never bypass access controls.
metadata:
  version: "0.9.2"
  product_stage: "Controlled user trial — split runtime / capability advisor"
  language: "zh-CN"
---

# ERP AI Capability Advisor

## Goal

For a real ERP / ToB task, decide whether the user's **current AI/toolchain is already enough** and, only if not, what **smallest additional capability** is worth adopting.

Do not become a Tool/Skill catalogue. A stronger or newer capability is not automatically worth adding.

## Workflow

### 1. Establish the real baseline

Use only facts that can change the adoption decision:

- concrete task and expected artifact;
- current AI / Agent / tools already available;
- actual bottleneck or repeated failure;
- hard constraints such as editable format, local/cloud, privacy, system access, permissions, version, cost, or repeated scale.

Do not compare against a bare model if the user already has a working toolchain.

### 2. Name the concrete capability gap

Ask:

> What can the current workflow not do reliably enough that matters to this task?

If there is no concrete gap, say plainly that the current toolchain is enough and stop. Do not invent a Tool/Skill recommendation to make the answer feel more useful.

Missing information is not automatically a capability gap. If one unknown fact decides the recommendation, state the condition instead of guessing.

### 3. Discover only capabilities that solve that gap

Search narrowly for capabilities that directly address the identified gap.

Useful evidence can include:

- original Tool / Skill / MCP / repo implementation;
- independent practitioner adoption or failure experience when setup/maintenance/permission cost matters;
- current official facts that change compatibility, privacy, permissions, price, or licensing.

Do not let discovery expand into a broad marketplace scan.

### 4. Verify serious candidates

Read [evidence and safety](references/evidence-and-safety.md) when recommending executable resources, system access, or volatile/high-risk claims.

Verify only decision-changing facts such as:

- required input/output and artifact format;
- install/runtime dependencies;
- account, credentials, permissions, write actions, or data egress;
- maintenance/current compatibility;
- price/license where material.

A candidate whose output does not match the user's required artifact is not a valid substitute unless a credible bridge is verified and explained.

### 5. Recommend the minimum useful change

Default outcomes are natural-language decisions, not A/B/C labels:

- **现有工具已够** — do not add another capability;
- **值得补能力** — name the concrete gap and the smallest capability that solves it;
- **条件式升级** — state the one condition that would make an upgrade worthwhile.

Normally keep **0–1** main capability. Add a second only when it represents a materially different adoption boundary.

Explain:

- what gap it solves;
- why the current workflow cannot solve that gap cheaply enough;
- what setup/learning/permission/maintenance cost it adds;
- what important boundary could make the recommendation wrong.

Only provide installation commands or perform installation when the user explicitly asks for installation/setup.

## Practice-curation boundary

This Skill does **not** curate generic “best practices / tutorials / how others do it” requests.

If the user primarily wants practitioner workflows or learning resources, use `curating-erp-ai-resources`. A Tool/Skill appearing inside a good tutorial is not evidence that the user should adopt it.

## Guardrails

- Never recommend a new capability without naming the concrete gap it solves.
- Never treat more features, installs, stars, popularity, or novelty as sufficient adoption evidence.
- Never recommend a capability whose output/artifact does not match the actual need without explaining the bridge.
- Never grant write/system permissions merely because a Tool/MCP supports them; use minimum necessary access.
- Never treat author self-practice as independent validation.
- Never turn a capability decision into a large comparison table unless the user explicitly asks for broad comparison.
