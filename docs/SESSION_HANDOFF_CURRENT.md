# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> Always inspect current `main` first. Current repository authority wins over this handoff.

## 1. Repository / authority

- GitHub: `FrankChen668/erp-ai-curator`
- North Star: `docs/PROJECT_NORTH_STAR.md`
- Current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`
- User-facing Skill: `skills/curating-erp-ai-resources/SKILL.md`

## 2. Product position

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners.

Core question:

> **面对一个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

It is not a generic tool directory, Prompt library, tutorial encyclopedia or tool-certification lab.

## 3. Validation status

Curator-method validation is **sufficient for Minimal Curator V0.1**.

Heterogeneous retained cards:

- P01 — workshop/minutes → requirement package;
- P04 — business logic → editable process diagram;
- P06 — Excel/CSV → reconciliation and validation;
- P03 — requirements/rules → clickable prototype/UI demo;
- P07 — codebase → understand logic / support FS / locate defects.

Authorities for newer cards:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

Do not continue additional Problem Cards merely for coverage.

## 4. Cross-card lessons

Stable behavior now observed:

- start from the real job, not a preferred Tool;
- “plain AI / existing Agent is enough” is a valid final answer;
- introduce specialist capability only for material adoption benefit;
- practitioner evidence is usually the first adoption-learning lane;
- author/implementation/official evidence roles stay explicit;
- runtime testing is exceptional and only used when it can change the recommendation;
- stop when colleague advice is stable.

Important card boundaries:

- P04: clarify semantics before diagram generation; generated diagrams remain review artifacts.
- P06: plain code-first is enough only with deterministic replay, row/amount/control-total checks and no-guess exception routing.
- P03: generic B-end default is coded prototype; Figma Make is preferable when mature Figma/design-system collaboration already exists.
- P07: repo-aware code Agent is the default; source/test/log grounding matters more than a separate architecture Skill.

## 5. Minimal Curator V0.1

Current Skill metadata version: `0.5.0`.

The previous V0.4 Gate/scoring/staging-heavy workflow has been simplified.

Current flow:

```text
understand real task
→ AI leverage judgement
→ general AI enough?
    yes → minimum viable workflow and stop
    no  → targeted practical discovery
→ necessary current fact / safety check
→ 0–1 main recommendation by default
→ concrete try-now guidance
→ stop
```

Normal user output should be compact:

1. conclusion;
2. why;
3. recommended workflow (`input → operation → output → review`);
4. 0–1 main resource, second only for a materially different boundary;
5. main risks;
6. what to try now.

Old `references/`, `evals/`, scripts and historical validation files remain regression/history assets. Do not automatically load them for a normal user consultation.

## 6. Immediate next phase — REAL USER PILOT

Do not start another synthetic/representative validation card.

Use real colleagues and real work tasks.

Capture only high-value feedback:

- real task/material;
- Curator recommendation;
- whether user actually tried it;
- whether search/learning/rework time decreased;
- what advice was wrong/useless;
- what risk was missed;
- whether user would use it again.

The next milestone is:

> **A real ERP colleague uses Curator advice on a real task and says it saved enough search/learning/rework time that they would return.**

### Mandatory preflight before doing or delegating work

Before any non-trivial cloud/local task, check:

1. current milestone;
2. concrete milestone evidence the task will create;
3. whether success still matters if no document/test/commit is counted;
4. why direct service of the next real user problem is not the better action.

If the task creates no real-user evidence and removes no concrete pilot blocker, do not do it.

In this phase, **smoke/readiness/synthetic tests, Quickstart polish, internal PASS labels and “give the local Agent something to do” are not valid substitutes for a real pilot.**

Engineering regression checks may follow a justified product change, but do not count them as product progress.

## 7. Cloud / local collaboration

Cloud owns product judgement, Web/GitHub research, evidence-role judgement, current fact checks, adversarial review, GitHub maintenance and stop/recommendation decisions.

Use local Agent only when a valid current-phase task actually needs local-only evidence or execution: repo/runtime, local files/environment, inaccessible-source acquisition or justified reproducibility checks.

**Agent availability is not a reason to create a task. Local Agent may correctly have nothing to do.**

Every local Task Envelope must state:

- `milestone_link` — which current milestone it advances;
- `user_evidence_created` — what real-user evidence or concrete blocker removal it produces.

If either is empty, do not delegate.

Remote GitHub branch + readable commit is the delivery boundary for repository evidence, not product-value evidence.

## 8. Anti-drift

Do not add without real-user evidence:

- more validation cards for their own sake;
- universal scores/Gates;
- large resource database/taxonomy;
- automatic refresh system;
- mandatory runtime benchmarks;
- unattended multi-card Loop;
- source/influencer rankings;
- pilot-readiness machinery whose primary purpose is proving the product is ready.

Goal hierarchy:

```text
North Star → current milestone → real user outcome/evidence → task → artifact/test/Agent
```

Never reverse it.
