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

## 6. Cloud / local split

Cloud/ChatGPT owns product judgement, current Web/GitHub research, evidence-role judgement, fact checks, proportional static inspection, GitHub maintenance and final recommendation/stop decisions.

Use local Agent only when local capability materially adds evidence: local repository/runtime, inaccessible source acquisition, local files/environment, or a justified reproducibility check.

For bounded local tasks:

- fixed: objective, hard boundaries, escalation conditions, evidence return;
- flexible: execution path, tools, scripts and internal iteration unless evidence validity requires otherwise.

Remote GitHub branch + readable remote commit is the completion boundary for local repository evidence.

## 7. What not to build yet

Until real-user usage proves need, do not add:

- more Problem Card validation for its own sake;
- unattended multi-card Loop;
- large resource database;
- fixed taxonomy;
- universal scores / Gates;
- mandatory runtime benchmarks;
- automated refresh infrastructure;
- influencer/source rankings;
- new governance for one-off failures.

## 8. Success criterion now

The next milestone is no longer “another card passes”.

It is:

> **A real ERP colleague brings a real task, receives a Curator recommendation, actually uses it, and reports that it reduced search/learning/rework enough that they would use Curator again.**
