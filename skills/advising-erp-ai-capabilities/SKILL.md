---
name: advising-erp-ai-capabilities
description: Decide whether an SAP, Oracle, ERP, ToB, product, project, or enterprise-system practitioner should add, install, choose, or compare an AI capability such as a Tool, Skill, MCP, plugin, Agent, model, integration, or new workflow. Use when the user explicitly asks whether their current toolchain is enough, whether a new capability is worth adopting, which capability to choose, or what the smallest useful upgrade is. Do not use for generic best-practice/tutorial/resource curation; use curating-erp-ai-resources for that. Do not use merely because a practitioner resource mentions a Tool/Skill.
compatibility: External adoption advice benefits from Web/search/fetch. Local repositories, runtimes, or enterprise systems are only needed when the decision materially depends on evidence unavailable otherwise. Never bypass access controls.
metadata:
  version: "0.9.1"
  product_stage: "Controlled user trial — split runtime / capability advisor"
  language: "zh-CN"
---

# ERP AI Capability Advisor

## Responsibility

For a real ERP / ToB task, decide whether the user's **current AI/toolchain is already enough** and, only if not, what **smallest additional capability** is worth adopting.

This Skill makes adoption decisions. It does not curate generic “best practices / tutorials / how others do it” requests.

## Operating contract

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

If there is no concrete gap, say plainly that the current toolchain is enough and stop. Missing information is not automatically a capability gap; if one unknown decides the answer, make the recommendation conditional instead of guessing.

### 3. Discover only gap-solving capabilities

Search narrowly for capabilities that directly solve the identified gap. Prefer original implementations, then independent adoption/failure evidence when setup or maintenance cost matters, plus current official facts only where they change the decision.

Do not expand into a broad Tool/Skill/MCP marketplace scan.

### 4. Verify decision-changing facts

Verify only what could change adoption: required input/output and artifact format, dependencies, accounts/credentials, permissions/data egress, maintenance/current compatibility, and price/license when material.

A candidate whose output does not match the required artifact is not a valid substitute unless a credible bridge is verified and explained.

Read [evidence and safety](references/evidence-and-safety.md) when the recommendation involves executable third-party resources, system access, volatile product claims, or meaningful permission/privacy risk.

### 5. Recommend the minimum useful change

Use natural-language outcomes:

- **现有工具已够** — no additional capability;
- **值得补能力** — name the concrete gap and smallest capability that solves it;
- **条件式升级** — state the one condition that would make the upgrade worthwhile.

Normally keep **0–1** main capability. Add a second only when it represents a materially different adoption boundary.

Explain the gap solved, why the current workflow cannot solve it cheaply/reliably enough, the setup/learning/permission/maintenance cost added, and the boundary that could make the recommendation wrong.

Only provide installation commands or perform setup when the user explicitly asks for installation/setup.

## Prohibited drift

- Do not recommend a new capability without a concrete gap.
- Do not treat features, installs, stars, popularity, or novelty as sufficient adoption evidence.
- Do not recommend an artifact-mismatched capability without a verified bridge.
- Do not grant write/system permissions beyond the minimum necessary.
- Do not turn the answer into a large comparison table unless the user explicitly asks for broad comparison.
