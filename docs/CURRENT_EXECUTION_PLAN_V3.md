# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. Context-drift correction remains recorded in `docs/REBASE_AUDIT_20260830.md`. P03/P07 were rerun from scratch, the cross-card reassessment is complete, and Minimal Curator V0.1 is in a bounded real-user pilot.

## 0. Owner execution continuity rule

Authority: `docs/OWNER_EXECUTION_RULES.md`.

> **Cloud/ChatGPT must continue any useful next step it can execute itself. It stops only for a genuine Owner decision, a genuine Local Agent handoff, or an external evidence barrier. When it stops, the next actor/task/result must be explicit.**

This does not authorize busywork; always continue the highest-value current milestone.

## 1. Product objective

ERP AI Curator helps SAP / Oracle / ERP / enterprise-information-system practitioners choose the **right AI working method for a real delivery task**.

Core question:

> **面对这个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

Atomic input:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
```

The product is not a generic AI tool directory, Prompt library, tutorial encyclopedia or tool-certification lab.

## 2. Trustworthy evidence baseline

Demand authority:

- 83-response 2026-08 training survey;
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Accepted heterogeneous task evidence:

- P01 — workshop/minutes → requirement package: **high task fit / low independent validation**;
- P04 — business logic → editable process diagram: **CLOSED**;
- P06 — ERP-style reconciliation: **CLOSED**, with bounded runtime evidence;
- P03 — requirements/rules → clickable prototype: **CLOSED** via clean Result 02;
- P07 — codebase/program → logic/FS/defect hypotheses: **CLOSED** via clean Result 02.

Current evidence authority: `docs/validation/EVIDENCE_STATUS.md`.

Invalidated P03/P07 Result 01 files remain invalid. Only Result 02 is authoritative.

## 3. Cross-card method decision

Authority: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Verdict:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The recurring method survived materially different tasks without contradictory permanent rules:

1. start from the real job, actual artifacts, deliverable and material constraints;
2. ordinary AI / existing Agent is the baseline;
3. specialized capability is introduced only for a concrete bottleneck;
4. when external adoption evidence matters, prefer practitioner workflow/failure evidence → original implementation → decision-changing current official facts;
5. important outputs remain source/project/system grounded and unknowns are explicit;
6. local/runtime testing is used only when the result can change the adoption recommendation;
7. stop when the colleague's next action is stable.

This is method readiness, not evidence that real users already gain time, quality or adoption value.

## 4. Minimal Curator V0.1 status

Current Skill:

- `skills/curating-erp-ai-resources/SKILL.md`
- version `0.6.1`

Status:

> **Minimal Curator V0.1 — real-user pilot candidate**

`0.6.1` is a bounded runtime hardening release. It removes project-governance/runtime coupling, compresses duplicated principles, adds a few decision-boundary examples and moves V0.4 Gate/scoring/taxonomy/runtime assets out of the distributable Skill.

Do not describe it as a validated product yet.

## 5. Correct current checkpoint

> **REAL_USER adoption/outcome remains the dominant uncertainty. Do not add P10 or broad internal validation by default.**

A bounded exception is currently active because the first survey-based local exercise exposed a concrete defect candidate:

- good resistance to over-tooling;
- possible **under-tooling** — failing to recognize a specialized capability when it is materially useful;
- possible misuse of `C` as a proxy for missing information.

This is sufficiently specific to justify one narrow regression. It does not reopen the internal validation program.

## 6. Active bounded regression — Curator 0.6.1 boundary discrimination

Authority:

- `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_PLAN.md`

Question:

> **Can 0.6.1 avoid over-tooling without becoming under-tooling?**

Cases: survey responses 65, 8, 5, 75, 38.

Method:

```text
same raw case
→ isolated ordinary-Agent Baseline
vs
→ isolated Curator 0.6.1 run
→ freeze answers
→ independent evaluator
→ compare adoption judgement, decomposition, critical unknowns, safety proportionality and actionability
```

Do not pre-seed expected A/B/C answers.

Important semantic check:

- A/B/C is an adoption decision;
- missing decision-changing information should be exposed explicitly;
- do not automatically convert “missing information” into `C`.

The regression is **not REAL_USER adoption evidence**.

## 7. Immediate next action / actor

Cloud preparation is complete for the regression: raw cases, isolation rules and evaluator contract are versioned in GitHub.

The next execution step requires a **Local Agent** because the paired experiment needs independent fresh contexts outside the current cloud conversation.

Local Agent returns:

1. five frozen Baseline answers;
2. five frozen Curator 0.6.1 answers;
3. one fresh evaluator comparison;
4. no repository or Skill changes.

Then Cloud/ChatGPT resumes automatically to:

- adversarially review whether the observed difference is real;
- distinguish Skill defect from Agent/eval execution error;
- if justified, make only one narrow Skill/reference correction;
- otherwise leave `0.6.1` unchanged;
- return to REAL_USER pilot rather than continue internal testing.

## 8. REAL_USER pilot

Pilot authority: `docs/REAL_USER_PILOT_V1.md`.

For genuine real-user use:

```text
real colleague task/materials/constraints
→ Minimal Curator recommendation
→ colleague actually tries / modifies / rejects it
→ capture usable result or concrete failure
→ inspect saved search/setup/rework or missed constraint
→ narrow method correction only if evidence requires it
```

Actual adoption evidence must come from real colleague action, not this regression.

## 9. Cloud / local split

Cloud/ChatGPT owns:

- continued execution whenever cloud capabilities are sufficient;
- running Curator recommendations for submitted real tasks;
- current Web/GitHub research when external resources are actually needed;
- product/adoption judgement;
- evidence review and narrow method corrections;
- GitHub authority maintenance.

Use a Local Agent only when it materially adds access/execution unavailable to Cloud, including local files/repository/runtime, enterprise environment, isolated experimental contexts or environment-specific reproducibility.

Agent availability is not a reason to create work.

## 10. Anti-drift during pilot

Do not return to internal validation work merely because it is easier to execute.

Do not add without real-user evidence of need:

- new validation cards by default;
- fixed scenario taxonomy;
- scoring/Gate systems;
- mandatory runtime benchmarks;
- resource databases or automatic refresh;
- multi-Agent orchestration;
- source/influencer rankings;
- card-specific rules in the permanent Skill.

Synthetic/internal testing is justified only to fix a concrete defect exposed by use or remove a concrete pilot blocker. The current 0.6.1 regression is such a bounded defect check and must stop after its decision is made.

## 11. Current milestone

> **Resolve the bounded 0.6.1 under-tooling/C-boundary defect candidate, then continue Minimal Curator V0.1 on genuine colleague tasks to obtain real adoption/outcome evidence.**
