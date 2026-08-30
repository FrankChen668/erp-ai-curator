# ERP AI Curator — Current Execution Plan V3

> Current execution authority. Keep this document short and current; historical detail belongs in validation records.

## 1. Product objective

ERP AI Curator helps SAP / Oracle / ERP / enterprise-information-system practitioners solve **real delivery problems** using existing AI practice and resources.

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
→ practical resource curation
```

The product is **not** an AI tool directory, generic tutorial library, Prompt library, influencer ranking, or tool-certification lab.

Core user question:

> **我现在碰到这个具体工作问题，别人已经有哪些值得学习和采用的 AI Skill / Tool / 方法 / 教程 / 经验？**

## 2. Demand and source discipline

Primary REAL_USER demand source:

- 83-response 2026-08 training survey;
- normalized Problem Cards in `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

The survey validates demand, not recommendation outcome.

Default evidence flow:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ current official/original fact check where needed
→ limitations / counter-evidence
```

Practical-value-first does not mean independent-third-party-at-all-costs. Author/maintainer material may be primary when genuinely strongest, but evidence roles must be labeled honestly.

Discovery is problem-driven, not platform-quota-driven. One failed platform route does not prove content absence.

## 3. Curator before Builder

Reuse existing PM/BA Skill libraries, Agent tutorials, WorkBuddy guides, creator series and task-specific repositories when they already solve the job well.

Curator value is:

```text
real ERP Problem Card
→ find the relevant few
→ remove hype / stale / mismatch
→ connect practice to Tool/Skill
→ verify only facts that matter
→ retain a small actionable package
```

Curator-created methods are allowed only when a real gap remains and must be labeled `Curator synthesis`.

## 4. Safety and testing boundary

Runtime testing is exceptional, not default.

For executable third-party Skill/MCP/plugin/script, use proportional lightweight static inspection before recommending installation when relevant.

Runtime is justified only when it can plausibly change an adoption decision, exact reproducibility matters, or material safety/privacy uncertainty remains.

Do not create new validation frameworks, Gates or benchmark systems for one-off candidates.

## 5. Current retained evidence

### P01 — workshop/minutes → requirement package

Retained:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

Useful working method; not independently proven industry standard or REAL_USER outcome validation.

### P04 — business logic → editable process diagram

Status:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Retained package combines practitioner workflow evidence, a low-friction text → Draw.io path, `Castaldo-Solutions/process-builder`, official `jgraph/drawio-mcp`, and optional technical troubleshooting material.

Do not reopen P04 unless a later real adoption decision exposes a new material risk.

### P06 — Excel / CSV / system export → reconcile and validate

Status:

> **CLOSED — PLAIN CODE-FIRST DEFAULT, WITH EXPLICIT RECONCILIATION CONTROLS**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`

Final cloud judgement:

- for ordinary ERP multi-file reconciliation, a competent local code-first Agent is sufficient as the default path;
- this does **not** mean free-form code with no controls is enough;
- the default method must include deterministic/replayable execution, explicit row/amount checks, source control-total/subtotal back-checks when available, no-guess handling for ambiguous matches, and human-review routing for unresolved cases;
- current spreadsheet-native AI remains a valid low-friction option for one-off lower-risk workbook work;
- `alchaincyf/huashu-excel` is useful as an optional audit/checklist method for recurring or high-consequence jobs, but the bounded P06 test does not justify mandatory Skill adoption.

Local runtime evidence:

- baseline and with-Skill produced identical record-level reconciliation outcomes across all 9 expected keys;
- Huashu uniquely surfaced a legacy `TOTAL` difference of 10;
- the pinned Huashu scripts first misclassified three subtotal rows and required manual repair, plus Windows UTF-8 output adjustment;
- therefore the durable value is primarily the **control-check discipline**, which can be carried into plain code-first execution without requiring the Skill itself.

Do not rerun P06 unless later real-user adoption reveals a materially different risk or workload boundary.

## 6. Immediate next action

P06 has reached the controlled single-card review checkpoint.

Next planned heterogeneous validation card:

> **P03 — requirements / rules → clickable prototype / UI demo**

Why P03 next:

- it tests a materially different resource/tool ecosystem from P01/P04/P06;
- acceptance depends on interaction fidelity, editability and iteration cost rather than only text or data correctness;
- it helps test whether Curator logic generalizes across another delivery-artifact class.

Do **not** start unattended multi-card execution. Start P03 as a new controlled card in the next execution cycle.

After P03, select one engineering-type card such as P07 code understanding or P10 testing before deciding whether the Curator is stable enough to move toward a minimal user-facing product.

## 7. Loop Engine position

Current decision:

> **Use controlled single-card Loop thinking; do not authorize unattended self-governing multi-card loops yet.**

```text
Problem Card
→ practitioner discovery
→ inspect serious Tool/Skill/method
→ fact/safety check only where needed
→ material evidence gap?
    yes → targeted delta
    no  → recommendation package
→ adversarial stop check
→ review checkpoint / stop
```

Loop readiness is behavior-based, not card-count-based.

Broader bounded batching only becomes reasonable when heterogeneous jobs repeatedly show that the process can:

- avoid early stopping;
- classify evidence roles correctly;
- use delta search/tests only when they can change the decision;
- stop based on decision quality;
- avoid framework/governance expansion and tool-centric drift.

## 8. Cloud / local split

Cloud/ChatGPT owns product judgement, Web/GitHub research, source prioritization, current fact checks, adversarial review, proportional static inspection, GitHub maintenance and final stop/recommendation decisions.

Use local Agent only when local capability materially adds evidence: local-only source acquisition, justified runtime checks, local files/environment, or reproducibility evidence.

For bounded local tasks:

- **fixed:** real job, decision question, hard boundaries, escalation conditions, evidence return;
- **flexible:** exact fixture, tools, scripts, output format and internal iteration unless evidence validity requires otherwise.

Remote GitHub branch + readable remote commit is the completion boundary for local work intended as repository evidence.

## 9. Anti-drift

Stop and correct if work becomes:

- a new framework/Gate per Tool;
- official-document gravity;
- independent evidence treated as a mandatory gate;
- platform/source-count optimization;
- author self-tests presented as independent field evidence;
- runtime testing used by default;
- specialized Skills recommended when plain deterministic Agent work is already enough;
- technical completeness mistaken for colleague usefulness;
- unattended Loop activity replacing judgement.

The success test remains:

> **Would we directly send this small package to a colleague because it saves search/learning time and helps them act on real project material?**
