# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. This file was rebased after a context-length audit. `docs/REBASE_AUDIT_20260830.md` records the correction. P03 was subsequently rerun from scratch with a trustworthy evidence trail.

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

### Demand — accepted

Primary REAL_USER demand source:

- 83-response 2026-08 training survey;
- normalized semantics in `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

The survey validates demand, not recommendation outcome. Free-text is semantic evidence and may contain platform-side wording cleanup.

### P01 — retained, low maturity

Status:

> **KEEP FOR PRACTICAL PILOT — HIGH TASK FIT / LOW INDEPENDENT VALIDATION**

Do not treat P01 as independent proof of a general method.

### P04 — accepted closed card

Status:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

### P06 — accepted closed card

Status:

> **CLOSED — PLAIN CODE-FIRST DEFAULT WITH EXPLICIT RECONCILIATION CONTROLS; HUASHU OPTIONAL**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

### P03 — accepted closed card after clean rerun

Status:

> **CLOSED — SPEC-FIRST CODE PROTOTYPE DEFAULT; FIGMA MAKE CONDITIONAL UPGRADE**

Authority:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_02.md`

Reason accepted:

- the rerun starts from the survey-derived task, not the invalid prior conclusion;
- retained external sources have concrete URLs and evidence roles;
- Chinese practical workflow, independent practitioner failure evidence, current platform facts and original Skill implementations are separated;
- limitations and enterprise-data boundaries are explicit;
- the stop decision explains why synthetic runtime A/B would not change the adoption decision.

Do not use `P03_PROTOTYPE_CURATION_RESULT_01.md` as supporting evidence.

## 3. Invalidated sprint conclusions remain invalid

The following files remain **not accepted product evidence**:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md`.

P03 Result 02 does not rehabilitate Result 01.

The earlier claims remain withdrawn:

- “P07 is closed”;
- “five heterogeneous cards prove Curator-method validation complete”;
- “Minimal Curator V0.1 is validated”;
- “the project has already entered REAL USER PILOT as the current authoritative phase”.

The simplified Skill remains an **experimental candidate implementation**.

## 4. Correct current checkpoint

> **P03 is now closed with trustworthy evidence. P07 is the next controlled engineering-type validation card.**

Do not restart P04, P06 or P03 without a new material reason.

P07 is preferred over P10 because:

- it is materially different from prototype/diagram/data artifact work;
- repository context, code correctness and technical evidence dominate;
- the previous P07 close was invalid, so a clean rerun directly tests whether the corrected evidence discipline survives an engineering task.

## 5. Immediate next action — rerun P07 correctly

P07 real job from survey semantics:

> A consultant/developer inherits an SAP/Oracle/custom-system codebase or enhancement and must understand structure, business logic, call chains, potential changes/defects/performance issues and sometimes reverse-generate functional logic/specification.

Run P07 from scratch. Do not use the invalid P07 verdict as a search prior or answer.

Required evidence flow:

```text
survey-derived real job
→ practitioner-first discovery with concrete URLs
→ actually read serious workflows/cases
→ inspect relevant code-Agent / Skill / MCP implementations
→ verify only current facts that affect adoption
→ retain failure / context / safety / correctness counter-evidence
→ decide whether plain repo-aware Agent is enough or specialist capability materially helps
→ material unresolved evidence gap?
    yes → targeted static/runtime/local delta
    no  → recommendation package
→ adversarial stop check
```

For every retained external source, preserve:

- concrete URL/source identity;
- actually read vs discovery-only;
- evidence role;
- material claim supported;
- limitation/counter-evidence.

Runtime/local testing is **not default**. Use it only if a concrete unresolved adoption decision can change because of the result.

## 6. After P07

After a trustworthy P07 close, reassess heterogeneous evidence as a whole.

Only then decide whether the method is stable enough to package a minimal user-facing Curator and enter real-user adoption validation.

Do not predeclare that transition now.

## 7. Candidate Skill status

Current candidate:

- `skills/curating-erp-ai-resources/SKILL.md`

Status:

> **experimental candidate — not validated Minimal Curator V0.1**

P03 supports the leverage-first direction but does not justify adding prototype-specific rules or claiming general validation.

Future changes must be driven by repeated trustworthy evidence, not by completing a framework.

## 8. Cloud / local split

Cloud/ChatGPT owns:

- product judgement;
- Web/GitHub research;
- source prioritization;
- evidence-role judgement;
- current fact checks;
- adversarial review;
- proportional static inspection;
- GitHub maintenance;
- final recommendation/stop decisions.

Use local Agent only when local capability materially adds evidence: local repository/runtime, inaccessible-source acquisition, local files/environment or justified reproducibility evidence.

Agent availability is not a reason to create work.

## 9. Task preflight

Before any non-trivial task, confirm:

1. current milestone;
2. concrete evidence the task will create;
3. why the evidence can change a product/adoption decision;
4. why the task is preferable to directly executing the current card.

Goal hierarchy:

```text
North Star
→ current trustworthy checkpoint
→ decision-changing evidence
→ task
→ artifact / test / commit / Agent
```

Do not reverse it.

## 10. Anti-drift

Do not add without evidence of need:

- new framework/Gate per Tool;
- large resource database or taxonomy;
- fixed source/platform quotas;
- mandatory runtime benchmarks;
- unattended multi-card Loop;
- automatic refresh infrastructure;
- source/influencer rankings;
- synthetic/smoke/readiness work presented as product evidence;
- conclusions that cannot be traced back to actually acquired evidence.

## 11. Current milestone

> **Complete P07 with a trustworthy, auditable evidence chain and a stable colleague recommendation. Then reassess whether the heterogeneous evidence base is sufficient for a minimal real-user pilot.**
