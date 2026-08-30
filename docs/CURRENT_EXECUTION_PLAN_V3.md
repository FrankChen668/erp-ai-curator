# ERP AI Curator — Current Execution Plan V3

> Current execution authority. Historical validation detail belongs in `docs/validation/`.

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

## 2. Validation phase — COMPLETE FOR V0.1

Do not continue through remaining Problem Cards merely for coverage.

Current heterogeneous evidence:

- **P01** — workshop/minutes → requirement package;
- **P04** — business logic → editable process diagram;
- **P06** — Excel/CSV/system export → deterministic reconciliation;
- **P03** — requirements/rules → clickable B-end prototype;
- **P07** — codebase/program → understand logic / support FS / locate defects.

These cover materially different artifact classes: text, structured visual, data/computation, interactive UI and code/repository reasoning.

Observed stable behavior across cards:

- starts from the real job rather than a preferred Tool;
- can correctly conclude “plain AI / existing Agent is enough”;
- introduces specialist capability only when adoption benefit is material;
- separates practical evidence, implementation evidence and current facts;
- uses runtime testing only when it can change the decision;
- stops when colleague advice is stable rather than maximizing research activity.

Therefore Curator-method validation is sufficient for Minimal Curator V0.1.

## 3. Current product — Minimal Curator V0.1

Primary implementation:

- `skills/curating-erp-ai-resources/SKILL.md`
- metadata version `0.5.0`

The Skill has been simplified from the earlier Gate/scoring-oriented curation workflow into a user-facing decision flow:

```text
understand real task
→ AI leverage judgement
→ general AI enough?
    yes → give minimum viable workflow and stop
    no  → targeted practical discovery
→ necessary fact/safety check
→ 0–1 main recommendation by default
→ concrete “try now” guidance
→ stop
```

Default user-facing output:

1. conclusion;
2. why;
3. recommended workflow (`input → operation → output → review`);
4. 0–1 main practical resource, second only for a materially different boundary;
5. main failure/adoption risks;
6. what to try now.

Internal evidence machinery should remain mostly invisible to normal users.

## 4. Current retained lessons

These are method evidence, not permanent tool whitelists.

- **P01:** specialized working method can improve structure/traceability, but evidence role must be honest.
- **P04:** clarify semantics before generating; editable diagram is a review artifact, not business truth.
- **P06:** plain code-first Agent can be enough if deterministic replay, row/amount/control-total checks and no-guess review routing are present.
- **P03:** coded prototype is the generic B-end default; prefer Figma Make when an existing Figma/design-system workflow is already the organizational source.
- **P07:** repo-aware code Agent is the generic default; reliability comes from source/test/log grounding and verification, not an extra architecture Skill.

## 5. Immediate next phase — REAL USER PILOT

The next product-learning loop is not another synthetic/representative card.

Use real ERP / enterprise colleagues and real work tasks.

For each pilot, capture only evidence that improves the product:

- what real task/material the user brought;
- what Curator recommended;
- whether they actually tried it;
- whether it reduced search/learning time or rework;
- what recommendation was wrong/useless;
- what risk was missed;
- whether they would use Curator again.

Do not build a heavy feedback database before real usage volume justifies it.

### Valid work in this phase

A task is valid only if it does at least one of the following:

1. **serves an actual real-user / owner-real work task now** and produces a recommendation the person can actually use;
2. **fixes a material defect exposed by real use**;
3. **removes a concrete blocker preventing a real pilot from happening**.

The following do **not** count as product progress by themselves:

- synthetic/smoke/readiness tests;
- generic Quickstart or documentation polish;
- creating work merely because a local/cloud Agent is available;
- more validation cards for coverage;
- internal PASS/score/readiness labels;
- implementation cleanup that no real pilot currently depends on.

Engineering smoke/regression checks are allowed after a justified product change, but they are implementation verification — **not product evidence and not a milestone substitute**.

## 6. Mandatory task preflight — milestone first

Before cloud or local Agent starts any non-trivial task, answer these four questions privately and concretely:

1. **What is the current milestone?**
2. **What observable evidence will this task create for that milestone?**
3. **If the task succeeds perfectly but no real user behavior/decision changes, are we actually closer to the milestone?**
4. **Why must this task happen now instead of directly serving the next real user problem?**

If question 2 has no concrete answer, or question 3 is “no” without a real blocker being removed, **do not execute the task**.

Goal hierarchy is fixed:

```text
North Star
→ current milestone
→ real user outcome/evidence
→ task
→ artifact / test / commit / Agent
```

Never reverse it.

In particular:

> **“We have a local Agent, what should it do?” is not a product reason to create work.**

Agent capacity is a means. It can be idle when no milestone-relevant local work exists.

## 7. Cloud / local split

Cloud/ChatGPT owns product judgement, current Web/GitHub research, evidence-role judgement, fact checks, proportional static inspection, GitHub maintenance and final recommendation/stop decisions.

Use local Agent only when local capability materially adds evidence or execution needed by a valid current-phase task: local repository/runtime, inaccessible source acquisition, local files/environment, or a justified reproducibility check.

For bounded local tasks:

- fixed: objective, hard boundaries, escalation conditions, evidence return;
- flexible: execution path, tools, scripts and internal iteration unless evidence validity requires otherwise.

Every delegated local task must be traceable to:

- `milestone_link`: which current milestone it advances;
- `user_evidence_created`: what real-user evidence or concrete blocker removal it produces.

If either is empty, do not delegate.

Remote GitHub branch + readable remote commit is the completion boundary for local repository evidence; it is not itself evidence of product value.

## 8. What not to build yet

Until real-user usage proves need, do not add:

- more Problem Card validation for its own sake;
- unattended multi-card Loop;
- large resource database;
- fixed taxonomy;
- universal scores / Gates;
- mandatory runtime benchmarks;
- automated refresh infrastructure;
- influencer/source rankings;
- new governance for one-off failures;
- pilot-readiness machinery whose only purpose is to prove the product is ready.

## 9. Success criterion now

The next milestone is no longer “another card passes”, “Skill loads”, “smoke tests pass” or “local Agent completed a task”.

It is:

> **A real ERP colleague brings a real task, receives a Curator recommendation, actually uses it, and reports that it reduced search/learning/rework enough that they would use Curator again.**

Until that happens, prefer serving the next real task over polishing the system that serves it.
