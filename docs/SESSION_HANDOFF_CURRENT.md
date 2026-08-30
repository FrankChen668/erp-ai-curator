# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> **Fresh-session authority after context reset.** Always inspect current `main` first. Do not rely on prior chat summaries when they conflict with repository evidence.

## 0. Owner execution rule — mandatory

Authority: `docs/OWNER_EXECUTION_RULES.md`.

Hard rule:

> **If Cloud/ChatGPT can complete the next useful project step with cloud capabilities, continue executing it directly. Do not stop merely to describe the next step or leave the next actor ambiguous.**

Cloud stops only for:

1. a genuine Owner decision;
2. a genuine Local Agent handoff because local files/repository/runtime/enterprise environment are required;
3. an external evidence barrier such as real-user action, protected access or permission.

When stopping, explicitly state who acts next, what they must execute/return, and what Cloud will do after the result returns.

## 1. Repository / authority

- GitHub: `FrankChen668/erp-ai-curator`
- Owner execution rules: `docs/OWNER_EXECUTION_RULES.md`
- North Star: `docs/PROJECT_NORTH_STAR.md`
- Current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`
- Pilot contract: `docs/REAL_USER_PILOT_V1.md`
- Active Pilot Case 001: `docs/pilot/PILOT_CASE_001_ERP_OPERATING_MANUAL.md`
- 0.6.2 Harness patch: `docs/validation/CURATOR_062_HARNESS_PATCH.md`
- 0.6.3 best-practice boundary patch: `docs/validation/CURATOR_063_BEST_PRACTICE_BOUNDARY_PATCH.md`
- Pilot Skill: `skills/curating-erp-ai-resources/SKILL.md`

## 2. Product objective — do not drift

ERP AI Curator is fundamentally a **best-practice / existing-resource curator for real ERP work**.

Core question:

> **面对真实工作问题，普通 AI 是否够用？如果不够，互联网上已经存在的实操经验、Tool / Skill / MCP / 方法 / 教程中，什么最值得学习和采用？**

Main chain:

```text
real problem
→ AI leverage judgement
→ practitioner practice / review / failure evidence
→ original implementation verification
→ decision-changing official facts
→ small curated recommendation
```

The default deliverable is **not** a complete execution SOP, user training plan, or tool-test protocol.

Real-user adoption/modification/rejection is product-validation evidence after the recommendation is delivered; it is not the Curator output itself.

## 3. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md`:

- version: `0.6.3`
- status: **Minimal Curator V0.1 — real-user pilot candidate**

0.6.3 keeps the 0.6.2 adoption-consistency check and adds one scope guardrail:

> **Do not silently turn best-practice curation into execution coaching/testing unless the user's task explicitly asks for execution/test design.**

## 4. Why 0.6.3 exists

Pilot Case 001 initially drifted into:

```text
choose tool
→ ask colleague to run a bounded trial
→ compare UI-change maintenance
```

That was a validation workflow, not the product's primary output.

The Owner corrected the boundary, and this matches the existing North Star. The durable correction is recorded in `CURATOR_063_BEST_PRACTICE_BOUNDARY_PATCH.md`.

## 5. Active Pilot Case 001 — corrected

Authority:

- `docs/pilot/PILOT_CASE_001_ERP_OPERATING_MANUAL.md`

Status:

> **BEST-PRACTICE CURATION READY — AWAITING REAL USER FEEDBACK / ADOPTION**

The curated result is now:

- task/role-based modular operating documentation;
- capture-assisted screenshot/annotation work;
- stable text for business purpose, roles, permissions, exceptions and notes;
- selective screenshots instead of screenshot-per-step by default;
- change-oriented maintenance;
- cloud/local choice based on enterprise data boundary.

Practitioner evidence comes first. Guidde / Folge are only implementation examples for different boundaries.

Do not tell the user they must run a tool experiment just to validate the Curator.

## 6. Current checkpoint

> **REAL_USER best-practice curation / adoption is the governing phase.**

For a genuine colleague problem:

1. curate the best existing practice/resource;
2. give a compact evidence-backed recommendation;
3. stop when the user knows what is worth learning/adopting;
4. if the user later adopts/modifies/rejects it, capture that as validation evidence.

## 7. Cloud / local boundary

Cloud should continue automatically on cloud-executable best-practice research, curation, evidence review and GitHub maintenance.

Use a Local Agent only when a curation decision genuinely needs local files/repository/runtime or an enterprise environment.

Do not dispatch local work merely because an Agent is available.

## 8. Anti-drift

Do not default to:

- user test protocols;
- synthetic benchmark loops;
- large tool/resource directories;
- fixed scenario taxonomies;
- scoring/Gate systems;
- mandatory runtime tests;
- card-specific rules in the permanent Skill.

## 9. New-session start instruction

When a fresh cloud conversation starts:

1. inspect current `main`;
2. read Owner Execution Rules + North Star + Current Plan + this Handoff + Evidence Status;
3. use `0.6.3` as the current distributable Skill;
4. remember: **Curator first = find and compress best existing practices; execution coaching only when explicitly requested**;
5. continue cloud-executable work automatically;
6. stop only for a genuine Owner decision, Local Agent handoff or external evidence barrier, and make the next actor explicit.
