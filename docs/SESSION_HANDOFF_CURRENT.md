# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> Purpose: start a fresh cloud/ChatGPT session without replaying the full conversation. Always inspect current `main` before making project claims.

## 1. Repository and authority

- GitHub: `FrankChen668/erp-ai-curator`
- Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Product contract: `docs/PROJECT_NORTH_STAR.md`
- Source strategy: `docs/SOURCE_STRATEGY_V3.md`
- Creator prior: `docs/CREATOR_PRIOR_STRATEGY_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`

Current `main` always wins over this handoff.

## 2. Product intent

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners.

Core user question:

> **我现在碰到这个具体工作问题，别人已经有哪些值得学习和采用的 AI Skill / Tool / 方法 / 教程 / 经验？**

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work problem/action
+ expected deliverable
+ material constraints
→ practical resource curation
```

It is not a generic AI tool directory, Prompt library, tutorial encyclopedia or tool-certification lab.

## 3. Evidence / source position

Default evidence flow:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ official/current fact check where needed
→ limitations / counter-evidence
```

Practical-value-first does not mean independent-third-party-only. Evidence roles must be labeled honestly.

Survey evidence validates REAL_USER demand, not solution outcome.

Discovery is problem-driven, not platform-quota-driven.

## 4. Safety / testing position

- Runtime testing is exceptional, not default.
- Executable third-party resources require proportional lightweight static inspection when relevant.
- Do not create a validation framework/Gate/benchmark for each candidate.
- Use local Agent only when local files, runtime, environment or inaccessible-source evidence materially adds value.

For local Task Envelopes:

- fixed: real job, decision question, hard boundaries, escalation conditions, evidence return;
- flexible: exact fixture, tools, scripts, output format and internal iteration unless evidence validity requires otherwise.

Repository evidence is not considered delivered until the remote GitHub branch/commit is readable.

## 5. Current retained state

### P01

Retained:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

### P04

Status:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Do not reopen unless later real adoption reveals a new material risk.

### P06

Status:

> **CLOSED — PLAIN CODE-FIRST DEFAULT, HUASHU OPTIONAL**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

Final cloud judgement:

- competent plain code-first Agent is the default for ordinary ERP multi-file reconciliation;
- required method discipline includes replayable deterministic execution, row/amount checks, source control-total/subtotal back-checks when available, conservative normalization/mapping, no guessing on ambiguous matches, human-review routing and traceability;
- spreadsheet-native AI remains valid for one-off lower-risk workbook tasks;
- `alchaincyf/huashu-excel` is useful as an optional audit/checklist method for recurring/high-consequence work but is not required by current evidence.

Runtime evidence:

- baseline and with-Skill matched all 9 expected record-level outcomes and produced the same reconciliation CSV;
- Huashu additionally surfaced a legacy `TOTAL` difference of 10;
- the pinned Huashu scripts first misclassified three subtotal rows and needed manual correction, plus Windows UTF-8 adjustment;
- therefore the portable value is mainly the audit/control discipline rather than a demonstrated mandatory Skill advantage.

Do not expand P06 into a benchmark suite or rerun unless real-user adoption exposes a materially different risk.

## 6. Immediate next action

P06 is at the controlled single-card review checkpoint.

Next planned heterogeneous card:

> **P03 — requirements / rules → clickable prototype / UI demo**

P03 should test whether Curator generalizes to interactive/editable artifact generation, where fidelity, iteration and handoff cost differ materially from P01/P04/P06.

Use the same controlled pattern:

```text
Problem Card
→ practitioner discovery
→ serious Tool/Skill/method inspection
→ fact/safety check only where needed
→ targeted delta only for material gaps
→ recommendation package
→ adversarial stop check
→ review checkpoint
```

Do not start unattended multi-card loops.

After P03, select one engineering-type card such as P07 code understanding or P10 testing. Then reassess whether enough heterogeneous evidence exists to move from validation-heavy work toward a minimal user-facing Curator.

## 7. Cloud / local collaboration

Cloud owns product judgement, Web/GitHub research, source prioritization, current fact checks, adversarial review, GitHub maintenance and final stop/recommendation judgement.

Local Agent should be used only for evidence the cloud cannot obtain efficiently or credibly, especially local files/runtime/environment-specific tests.

Cloud should not rerun completed local work by default; inspect key evidence and attack the conclusion instead.

## 8. Anti-drift

- do not add scoring/Gates/databases/taxonomies for one-off failures;
- do not turn source/platform access issues into quotas;
- do not present author self-tests as independent field evidence;
- do not turn runtime testing into default work;
- do not recommend specialized Skills when plain deterministic Agent work is enough;
- do not maximize sources/tests/iterations;
- do not autonomously modify project principles;
- do not keep accumulating validation artifacts after the adoption decision is stable.

Success test:

> **Would we directly send this small package to a colleague because it saves search/learning time and helps them act on real project material?**
