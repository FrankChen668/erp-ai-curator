# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> **Fresh-session authority after context reset.** Always inspect current `main` first. Do not rely on prior chat summaries when they conflict with repository evidence.

## 0. Owner execution rule — mandatory

Authority:

- `docs/OWNER_EXECUTION_RULES.md`

Hard rule:

> **If Cloud/ChatGPT can complete the next useful project step with cloud capabilities, continue executing it directly. Do not stop merely to describe the next step or leave the next actor ambiguous.**

Cloud stops only for:

1. a genuine Owner decision;
2. a genuine Local Agent handoff because local files/repository/runtime/enterprise environment are required;
3. an external evidence barrier such as real-user action, protected access or permission.

When stopping, explicitly state who acts next, what they must execute/return, and what Cloud will do after the result returns.

This rule does not justify busywork. Continue the highest-value current milestone only.

## 1. Repository / authority

- GitHub: `FrankChen668/erp-ai-curator`
- Owner execution rules: `docs/OWNER_EXECUTION_RULES.md`
- North Star: `docs/PROJECT_NORTH_STAR.md`
- Current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`
- Cross-card reassessment: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`
- Pilot contract: `docs/REAL_USER_PILOT_V1.md`
- Active bounded regression: `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`
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

The recurring method is stable enough to expose to real colleagues: real-task-first; ordinary AI/existing Agent as baseline; specialized capability only for a concrete bottleneck; evidence grounded; runtime/local tests only when decision-changing; stop when the colleague's next action is stable.

## 5. Minimal Curator status

`skills/curating-erp-ai-resources/SKILL.md`:

- version: `0.6.1`
- status: **Minimal Curator V0.1 — real-user pilot candidate**

`0.6.1` is a bounded runtime hardening release. Legacy V0.4 Gate/scoring/taxonomy/validator/eval assets are archived and are not current runtime authority.

This still means method readiness, not validated user value.

## 6. Current checkpoint — REAL_USER pilot remains the milestone

> **The project remains in a bounded real-user adoption pilot. Do not default back to P10 or broad internal validation.**

However, the first survey-based local exercise exposed a bounded defect candidate worth checking before using `0.6.1` broadly:

- Curator correctly avoided unnecessary tools;
- but it may be **under-tooling** — overusing A/C and failing to recognize specialized capability when it is genuinely useful;
- `C` may also be getting misused as “information is missing”.

This is not real-user adoption evidence and does not reopen the validation-card program.

## 7. Active bounded regression — 0.6.1 boundary discrimination

Authority:

- `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`

Cases are derived from real survey responses: 65, 8, 5, 75, 38.

Test design:

```text
same raw real-user problem
→ fresh Baseline context without Curator
vs
→ separate fresh Curator 0.6.1 context
→ freeze both answers
→ fresh independent evaluator
→ compare adoption judgement, not prose quality
```

Key question:

> **Can 0.6.1 avoid over-tooling without becoming under-tooling?**

The regression must not be presented as REAL_USER adoption evidence.

## 8. Immediate next actor

The cloud-side design and repository preparation for this regression is complete.

The next step requires a **Local Agent** only because the experiment needs isolated fresh contexts/runs outside the current cloud conversation.

Local Agent must execute `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_PLAN.md` exactly and return:

1. five frozen Baseline answers;
2. five frozen Curator 0.6.1 answers;
3. the fresh evaluator's cross-case comparison;
4. no repository/Skill modifications.

After those results return, Cloud/ChatGPT resumes immediately: adversarially reviews the evidence, determines whether the issue is Skill-level or execution/eval-level, and if justified makes one narrow patch through GitHub.

## 9. REAL_USER pilot evidence rule

Actual pilot evidence still requires a real colleague to act on a recommendation. Capture:

- task in the colleague's own words;
- recommendation actually given;
- what they actually tried/changed/rejected;
- artifact/result or rejection reason;
- saved/added search/setup/rework;
- missed capability/privacy/permission/environment constraints;
- whether they would bring another task.

Do not manufacture tasks to claim adoption evidence.

## 10. Local Agent boundary

Use a Local Agent only when it materially adds access/execution unavailable to Cloud: local project files, repository/runtime, enterprise environment, isolated experimental contexts, or environment-specific reproducibility.

Do not dispatch local work merely because an Agent is available.

## 11. Anti-drift

During Pilot, avoid:

- returning to validation-card accumulation without a real blocker;
- synthetic benchmarks presented as product evidence;
- new taxonomy/Gate/scoring frameworks;
- resource database construction;
- mandatory runtime tests;
- card-specific rules added to the permanent Skill;
- claiming product success before real colleague action exists.

## 12. New-session start instruction

When a fresh cloud conversation starts:

1. inspect current `main`;
2. read Owner Execution Rules + this handoff + Current Plan + Evidence Status + Pilot contract;
3. continue cloud-executable work automatically;
4. do not reopen settled P03/P04/P06/P07 without a new material reason;
5. treat REAL_USER pilot as the governing phase;
6. if the 0.6.1 boundary regression is not yet resolved, use its plan as the active bounded exception;
7. stop only for a genuine Owner decision, Local Agent handoff or external evidence barrier, and always make the next actor explicit.
