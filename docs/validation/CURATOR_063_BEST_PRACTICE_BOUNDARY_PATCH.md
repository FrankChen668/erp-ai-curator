# Minimal Curator V0.1 / Skill 0.6.3 — Best-Practice Curator Boundary Patch

Date: 2026-08-30
Status: **ACCEPTED OWNER / NORTH-STAR CORRECTION**

## Trigger

Pilot Case 001 drifted from Curator work into execution coaching: after finding candidate tools, Cloud designed a detailed real-user tool-test protocol and treated that protocol as the next product step.

The Owner corrected the product boundary:

> **The product's essence is to help users find the best existing practices, not to primarily instruct users how to execute or test a tool.**

This matches `docs/PROJECT_NORTH_STAR.md`, whose main chain is:

```text
真实任务
→ AI 杠杆判断
→ 第三方实操/经验发现
→ 原始 Skill/Tool 核验
→ 必要官方事实兜底
→ 少量可执行建议
```

## Root cause

The North Star was correct, but the runtime Skill's wording around “next action / immediate trial” allowed an Agent to cross the boundary from **Curator** into **Workflow Coach / Test Coordinator**.

This is a Harness legibility problem, not an ERP scenario-knowledge problem.

## 0.6.3 correction

The runtime Skill now makes explicit that:

- the default product output is a curated best-practice / existing-resource adoption recommendation;
- practitioner workflows, reviews and failure experience come before vendor feature lists when external evidence matters;
- the user should not be turned into a tool tester by default;
- detailed execution SOPs or test protocols are only produced when the user's task explicitly asks for them;
- real-user adoption/modification/rejection remains product-validation evidence, but is not the Curator output itself.

No SAP/Oracle/ERP scenario answer is added.

## Case 001 correction

`docs/pilot/PILOT_CASE_001_ERP_OPERATING_MANUAL.md` is rewritten as a Best-Practice Curation result:

- practitioner evidence first;
- tool capabilities second;
- Curator synthesis clearly labeled;
- no mandatory user test protocol.

## Guardrail

Before finalizing a Curator response, ask:

> **Am I helping the user discover and select an existing best practice, or have I silently become an execution coach/test coordinator?**

If the latter and the user did not ask for execution/test design, return to Curator mode.

## Evidence boundary

This is a product-scope / Harness correction grounded in the existing North Star and explicit Owner instruction. It is not REAL_USER adoption evidence and does not prove product value over ordinary search or ordinary AI.
