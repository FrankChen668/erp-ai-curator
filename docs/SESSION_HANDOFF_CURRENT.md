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

Current main before this P06 branch started: `32ce5c82e4d9963c4188bd463f1fbbd39bc2bb7d`.

Current P06 task envelope:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`

Current `main` always wins if newer.

## 2. Product intent

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners: implementation consultants, PMs, product managers, developers and solution roles.

It is not a generic AI tool directory, tutorial encyclopedia, Prompt library or tool-certification lab.

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

## 3. Source / evidence boundary

For adoption questions, use:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ official/current fact check where needed
→ limitations / counter-evidence
```

Practical-value-first does not mean independent-third-party-at-all-costs. Author/maintainer tutorials may be primary when genuinely strongest, but label evidence roles correctly.

Official/current sources mainly verify volatile facts such as version, install, compatibility, privacy/data flow and native output format.

Survey evidence validates demand, not solution quality or outcome.

## 4. Safety / testing / platform boundary

- Runtime testing is exceptional, not default.
- Executable resources require proportional lightweight static inspection before install/run recommendations.
- One failed platform route does not prove content absence.
- No platform quotas, source-count targets or influencer ranking.
- Historical retained resources are search priors, not permanent approvals.

## 5. P01 / P04 retained state

### P01

Retained:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

### P04

Verdict:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Do not reopen P04 unless later real adoption exposes a new material risk.

## 6. P06 — current active card

Problem:

> **Several legacy / target / mapping Excel or CSV files must be reconciled into a reviewable, reproducible ERP migration/data-validation result. Which AI working method is actually worth adopting?**

Authority / local task envelope:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`

### Cloud work already completed

Cloud practitioner/current-fact research has established:

- direct conversational reconciliation can work for one-off low-risk jobs, but recurring/high-consequence reconciliation needs a fixed procedure, deterministic execution, explicit checks and exception routing;
- current spreadsheet-native AI is materially stronger than older chat-only workflows, so `Python + Skill` must not be assumed as the only valid answer;
- `alchaincyf/huashu-excel` is the strongest discovered packaged audit-oriented method so far, but it is recent and its strongest evidence is author self-practice / author-run pressure testing;
- candidate was inspected at commit `9348581a87cc03ed8d0b30706631088e922c6027`.

### Why one local runtime delta is justified

The remaining decision is narrow:

> **Does Huashu-Excel materially improve ERP-style multi-file reconciliation over a competent plain code-first local Agent, enough to justify adoption overhead?**

This can change the recommendation and cannot be settled confidently from author evidence alone.

### Local Agent should do only this

Use the Task Envelope in `DELIVERY_P06_DATA_RECONCILIATION.md`.

Core comparison:

- fresh baseline context: plain local Agent + code execution, no Huashu knowledge;
- fresh with-Skill context: same task/data, allowed to read/use pinned Huashu repository in a temporary isolated checkout;
- hidden ground truth kept out of both execution contexts;
- synthetic ERP-like data only;
- stop when the comparison changes or stabilizes the adoption decision.

Do not broadly search the Web, globally install the Skill, modify project principles, build a benchmark framework or start another Problem Card.

## 7. Cloud/local collaboration rule

For local Task Envelopes:

- **fixed:** real job, decision question, hard boundaries, escalation conditions, evidence return;
- **flexible:** exact fixture, tools, scripts, output format, search/execution details and internal iteration unless evidence validity requires otherwise.

Local Agent escalates only when the task would change project direction, require credentials/risky installation, or cross a hard boundary. Minor execution choices should be made locally.

Cloud does not rerun completed local work by default; it inspects key evidence, does the adversarial decision check, and owns the current stop/final recommendation judgement.

## 8. Immediate next action

Wait only for the bounded P06 local evidence package if the local Agent is being used.

After it returns, cloud should:

1. inspect the evidence and key artifacts;
2. compare against existing practitioner/current-fact evidence;
3. decide the P06 recommendation boundary: spreadsheet-native AI vs plain code-first Agent vs Huashu-Excel (or a clearly differentiated combination);
4. close P06 when further work is unlikely to change what an ERP colleague should do.

Do not start P03/P07/P10 in parallel.

## 9. Loop Engine position

Current decision:

> **Use controlled single-card Loop thinking; do not authorize unattended self-governing multi-card loops.**

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

## 10. Anti-drift

- do not add scoring/Gates/databases/taxonomies for one-off failures;
- do not mistake technical completeness for colleague usefulness;
- do not require independent evidence when it adds no decision value;
- do not let author self-tests masquerade as independent field evidence;
- do not turn runtime testing into the default;
- do not maximize sources/tests/iterations;
- do not autonomously modify project principles.

Success test:

> **Would we directly send this small package to a colleague because it saves search/learning time and helps them act on real project material?**
