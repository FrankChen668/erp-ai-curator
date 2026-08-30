# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> **Fresh-session authority after context reset.** Always inspect current `main` first. Do not rely on prior chat summaries when they conflict with repository evidence.

## 1. Repository / authority

- GitHub: `FrankChen668/erp-ai-curator`
- North Star: `docs/PROJECT_NORTH_STAR.md`
- Current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`
- Cross-card reassessment: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`
- Pilot contract: `docs/REAL_USER_PILOT_V1.md`
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
- P03 — **CLOSED** via clean `P03_PROTOTYPE_CURATION_RESULT_02.md`;
- P07 — **CLOSED** via clean `P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Invalid old sprint artifacts remain invalid:

- `P03_PROTOTYPE_CURATION_RESULT_01.md`;
- `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`.

Do not use them as product evidence.

## 4. Cross-card reassessment — completed

Authority:

- `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`

Verdict:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The recurring method is now stable enough to expose to real colleagues:

- real-task-first;
- ordinary AI/existing Agent as baseline;
- specialized capability only for a concrete bottleneck;
- practitioner evidence first when the question is real adoption/workflow;
- implementation/current official facts used for the claims they actually support;
- important outputs grounded in project/source/system evidence;
- unknowns exposed rather than guessed;
- runtime/local tests only when decision-changing;
- stop when the colleague's next action is stable.

No material contradiction was found across the trusted cards.

## 5. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md`:

- version: `0.6.1`
- status: **Minimal Curator V0.1 — real-user pilot candidate**

`0.6.1` is a bounded runtime hardening release. It does not add a new product claim or change the validated recurring method. The runtime Skill is now decoupled from project-governance documents, uses four compressed core principles, includes a few decision-boundary examples, and keeps only two active on-demand references.

Legacy V0.4 Gate/scoring/taxonomy/validator/eval assets are archived under `archive/curator-v0.4-runtime-assets/` and are not current runtime authority.

This still means method readiness, not validated user value.

## 6. Correct current checkpoint

> **The project has moved from internal method validation to a bounded real-user adoption pilot.**

This is a newly earned transition based on the corrected P03/P07 reruns plus the fresh cross-card reassessment. It is not the unsupported old sprint claim.

Do not default back to P10 or more internal validation cards.

## 7. Immediate next action — real colleague task

Pilot authority:

- `docs/REAL_USER_PILOT_V1.md`

The next decision-changing evidence requires a real colleague with a real task.

For each case, capture:

1. task in the colleague's own words;
2. real materials/constraints that affect the choice;
3. Curator recommendation actually given;
4. what the colleague actually tried, changed or rejected;
5. usable artifact/result or concrete failure reason;
6. saved/added search, setup or rework;
7. missed environment/privacy/permission/capability constraints;
8. whether they would use this type of recommendation again.

Do not require Problem Card classification and do not manufacture tasks to cover categories.

## 8. What cloud should do now

When a real pilot task arrives:

1. run Minimal Curator V0.1 against the actual task;
2. use current Web/GitHub research only if the task genuinely needs external resource discovery;
3. keep the recommendation compact and actionable;
4. capture post-action evidence when available;
5. fix only concrete method defects exposed by real use;
6. maintain repository authorities.

If no real pilot task is available, do not invent internal work to keep the project busy.

## 9. Local Agent boundary

Use a local Agent only when the real pilot task materially needs:

- local project files;
- repository/runtime access;
- inaccessible-source acquisition;
- environment-specific reproducibility evidence.

Do not dispatch local tasks merely because an Agent is available.

## 10. Anti-drift

During Pilot, avoid:

- returning to validation-card accumulation without a real blocker;
- synthetic benchmarks presented as product evidence;
- new taxonomy/Gate/scoring frameworks;
- resource database construction;
- mandatory runtime tests;
- card-specific rules added to the permanent Skill;
- claiming product success before real colleague action exists.

## 11. New-session start instruction

When a fresh cloud conversation starts:

1. inspect current `main`;
2. read this handoff + Current Plan + Evidence Status + Cross-Card Reassessment + Pilot contract;
3. do not reopen settled P03/P04/P06/P07 without a new material reason;
4. treat **REAL_USER pilot** as the current phase;
5. execute real submitted tasks directly and capture adoption/outcome evidence;
6. stop only for a genuine Owner decision or external evidence barrier.
