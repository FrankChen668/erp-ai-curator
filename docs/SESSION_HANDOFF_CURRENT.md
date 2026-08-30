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
- Cross-card reassessment: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`
- Pilot contract: `docs/REAL_USER_PILOT_V1.md`
- Closed 0.6.1 regression result: `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`
- Context-drift correction: `docs/REBASE_AUDIT_20260830.md`
- Pilot Skill: `skills/curating-erp-ai-resources/SKILL.md`

## 2. Product objective

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners.

Core question:

> **面对一个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
→ practical AI working-method recommendation
```

The product is not a generic AI tool directory, Prompt library, tutorial encyclopedia or tool-certification lab.

## 3. Trusted evidence checkpoint

Demand:

- 83-response 2026-08 training survey;
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Trusted heterogeneous task evidence:

- P01 — **high task fit / low independent validation**;
- P04 — **CLOSED**;
- P06 — **CLOSED**, with bounded runtime delta;
- P03 — **CLOSED** via clean Result 02;
- P07 — **CLOSED** via clean Result 02.

Invalid P03/P07 Result 01 files remain invalid and must not be used as product evidence.

## 4. Cross-card reassessment — completed

Authority: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Verdict:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

## 5. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md`:

- version: `0.6.1`
- status: **Minimal Curator V0.1 — real-user pilot candidate**

This still means method readiness, not validated user value.

## 6. 0.6.1 boundary regression — closed

Authority:

- `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

Verdict:

> **CLOSED — KEEP 0.6.1 UNCHANGED; RETURN TO REAL_USER PILOT**

The paired regression used 11 isolated Codex contexts: five Baselines, five Curator runs and one evaluator.

Bounded result:

- no over-tooling signal;
- under-tooling appeared in Case 5/38 and lightly in Case 8;
- C-as-missing-information was not confirmed;
- recurring decomposition defect was not confirmed;
- no clear repeatable Curator adoption advantage over ordinary Agent was demonstrated;
- the strongest under-tooling misses are already covered by current Skill/reference rules, so no permanent Skill-text defect was established.

Decision: **do not patch 0.6.1 from this regression and do not run another internal boundary test by default.**

This is internal bounded regression evidence only, not REAL_USER adoption evidence.

## 7. Correct current checkpoint

> **The project is back to the REAL_USER adoption pilot with no active internal regression.**

Do not reopen P10 or more internal validation unless a genuine real-use blocker/defect appears.

## 8. Immediate next action

Pilot authority: `docs/REAL_USER_PILOT_V1.md`.

The next decision-changing evidence requires a **real colleague using a real work task**.

For each genuine use, capture:

1. task in the colleague's own words;
2. real materials/constraints that affect the choice;
3. Curator recommendation actually given;
4. what the colleague actually tried, changed or rejected;
5. usable artifact/result or concrete failure reason;
6. saved/added search, setup or rework;
7. missed environment/privacy/permission/capability constraints;
8. whether they would use this type of recommendation again.

## 9. Cloud / local boundary

Cloud should continue automatically on any cloud-executable real task, research, review or GitHub maintenance.

Use a Local Agent only when a real task materially requires local files/repository/runtime, enterprise environment or environment-specific reproducibility.

Do not dispatch local work merely because an Agent is available.

## 10. Anti-drift

During Pilot, avoid:

- returning to validation-card accumulation without a real blocker;
- new boundary regressions without a real-use defect;
- synthetic benchmarks presented as product evidence;
- new taxonomy/Gate/scoring frameworks;
- resource database construction;
- mandatory runtime tests;
- card-specific rules added to the permanent Skill;
- claiming product success before real colleague action exists.

## 11. New-session start instruction

When a fresh cloud conversation starts:

1. inspect current `main`;
2. read Owner Execution Rules + this handoff + Current Plan + Evidence Status + Pilot contract;
3. continue cloud-executable work automatically;
4. do not reopen settled P03/P04/P06/P07 or the closed 0.6.1 boundary regression without a new material reason;
5. treat REAL_USER pilot as the governing phase;
6. stop only for a genuine Owner decision, Local Agent handoff or external evidence barrier, and always make the next actor explicit.
