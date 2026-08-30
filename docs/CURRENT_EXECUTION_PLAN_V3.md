# ERP AI Curator — Current Execution Plan V3

> Current execution authority. Historical detail belongs in validation records.

## 1. Product objective

ERP AI Curator helps SAP / Oracle / ERP / enterprise-information-system practitioners choose the **right AI working method for a real delivery task**.

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
→ AI leverage judgement + practical curation
```

Core user question:

> **面对这个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

The product is not a generic AI tool directory, tutorial encyclopedia, Prompt library or tool-certification lab.

## 2. Evidence / discovery discipline

Primary REAL_USER demand source remains the 83-response 2026-08 training survey and its normalized Problem Cards.

Default evidence flow:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ current official/original fact check where needed
→ limitations / counter-evidence
```

Practical-value-first does not mean independent-third-party-at-all-costs. Do not use platform quotas, popularity, source counts or author self-tests as substitutes for evidence quality.

Curator before Builder: reuse strong existing PM/BA/Agent/WorkBuddy/tutorial ecosystems instead of rebuilding them.

Runtime testing remains exceptional and is used only when it can plausibly change an adoption decision.

## 3. Retained heterogeneous evidence

### P01 — workshop/minutes → requirement package

Status: **KEEP FOR PRACTICAL PILOT**

Retained: `Convert Notes to Requirements Working Skill`

Classification: **high task fit / low independent validation**.

### P04 — business logic → editable process diagram

Status: **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority: `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Key lesson: clarify business semantics first; AI diagram is a reviewable/editable artifact, not truth.

### P06 — Excel / CSV / system export → reconcile and validate

Status: **CLOSED — PLAIN CODE-FIRST DEFAULT, WITH EXPLICIT RECONCILIATION CONTROLS**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`

Key lesson: do not install a specialized Skill when deterministic plain Agent execution is enough; retain row/amount/control-total checks, conservative matching and human-review routing.

### P03 — requirements / rules → clickable prototype / UI demo

Status: **CLOSED — CODED PROTOTYPE DEFAULT; FIGMA MAKE FOR FIGMA/DESIGN-SYSTEM-FIRST TEAMS**

Authority:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`

Final judgement:

- generic ERP/B-end prototype work should default to clarified business semantics → coded clickable prototype → review/iterate;
- v0 / AI IDE / coding Agent are valid low-friction coded-prototype paths;
- Figma Make is preferred when existing Figma libraries/design-system collaboration are already the organizational source;
- no dedicated prototype Skill is justified as a default dependency;
- main failure mode is visually plausible UI with wrong states, branches, permissions or field rules.

No P03 local runtime test is justified unless later real use exposes a specific environment/design-system decision gap.

## 4. Sprint mode — final validation card only

Current mode:

> **SPRINT: one engineering-type card, then stop validating Curator itself.**

Next and final planned heterogeneous validation card:

> **P07 — codebase / program → understand business logic, explain behavior, locate defects and support FS/solution work**

P07 exists to test a materially different source-grounded engineering task: repository context, code navigation, implementation evidence, defect reasoning and business/technical translation.

Use the same controlled single-card pattern, but keep it lightweight. Do not build a new framework or mandatory runtime benchmark.

## 5. Exit criterion from research/validation

After P07, do **not** continue through the remaining Problem Cards merely for coverage.

If P07 demonstrates the same behaviors already shown across P01/P04/P06/P03:

- starts from real work rather than tools;
- can conclude generic AI / plain Agent is enough;
- finds specialist capability only when it materially helps;
- separates practitioner / implementation / official evidence correctly;
- uses targeted delta only when it can change the decision;
- stops when colleague advice is stable;

then Curator-method validation is considered sufficient for V0.1.

## 6. Immediate productization after P07

Next phase is **Minimal Curator V0.1**, not more research.

Minimum user-facing output:

1. what the user is actually trying to deliver;
2. recommended AI intervention;
3. whether a specialized Tool/Skill is needed;
4. one main practical resource/method when external learning is useful;
5. concrete starting workflow;
6. major failure/rework risks;
7. enterprise data/environment cautions;
8. what to try now.

Internal evidence machinery should remain mostly hidden from normal users.

## 7. Real-user phase

After V0.1, use real ERP colleagues and real project tasks to test:

- did they understand and try the recommendation;
- did it reduce search/learning time;
- what advice was wrong or useless;
- what failure/risk was missed;
- would they return for another task.

Real usage, not additional synthetic cards, becomes the primary product-learning loop.

## 8. Cloud / local split

Cloud/ChatGPT owns product judgement, Web/GitHub research, source prioritization, fact checks, adversarial review, proportional static inspection, GitHub maintenance and final stop/recommendation decisions.

Use local Agent only when local-only capability materially adds evidence: repository/runtime access, inaccessible source acquisition, local files/environment or a justified reproducibility check.

For bounded local tasks:

- fixed: real job, decision question, hard boundaries, escalation conditions, evidence return;
- flexible: exact tools/scripts/output/internal iteration unless evidence validity requires otherwise.

Remote GitHub branch + readable remote commit is the completion boundary for local repository evidence.

## 9. Anti-drift

Stop and correct if work becomes:

- another framework/Gate/benchmark per tool;
- platform/source-count optimization;
- runtime testing by default;
- specialized Skill promotion when plain Agent work is enough;
- endless Problem Card validation;
- technical completeness mistaken for colleague usefulness;
- unattended Loop activity replacing judgement.

Success test:

> **Would we directly send this advice/resource package to a colleague because it saves search/learning time and helps them act on real project material?**
