# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. This file was rebased after a context-length audit. `docs/REBASE_AUDIT_20260830.md` records the correction.

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

Reason: concrete source URLs, evidence roles, limitations and coverage gaps are retained and auditable.

### P06 — accepted closed card

Status:

> **CLOSED — PLAIN CODE-FIRST DEFAULT WITH EXPLICIT RECONCILIATION CONTROLS; HUASHU OPTIONAL**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

Reason: bounded runtime evidence exists with a pinned candidate commit, isolated baseline/with-Skill runs, hidden truth and retained artifacts.

## 3. Invalidated sprint conclusions

The following recent sprint conclusions are **not accepted product evidence**:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

Why:

- the retained files do not provide a trustworthy source-acquisition/citation trail for the external claims they use;
- some conclusions were produced during an overloaded long-context sprint and cannot be distinguished reliably from model synthesis;
- therefore their `CLOSED` verdicts were unsupported.

Consequently, these statements are withdrawn:

- “P03 is closed”;
- “P07 is closed”;
- “five heterogeneous cards prove Curator-method validation complete”;
- “Minimal Curator V0.1 is validated”;
- “the project has already entered REAL USER PILOT as the current authoritative phase”.

The simplified Skill produced in that sprint remains only an **experimental candidate implementation**, not validated product evidence.

## 4. Correct current checkpoint

The last trustworthy controlled checkpoint is:

> **P06 closed. P03 is the next controlled heterogeneous validation card.**

This is the same checkpoint that existed before the invalid sprint close.

Do not restart P04 or P06 without a new material reason.

## 5. Immediate next action — rerun P03 correctly

P03:

> **requirements / rules → clickable prototype / UI demo**

Run it from scratch. Do not use the invalid P03 verdict as a search prior or answer.

Required evidence flow:

```text
survey-derived real job
→ practitioner discovery with concrete source URLs
→ actually read serious sources
→ inspect relevant Tool / Skill / implementation
→ verify only current facts that affect adoption
→ record limitations / counter-evidence
→ material evidence gap?
    yes → targeted delta
    no  → recommendation package
→ adversarial stop check
```

For every retained external source, preserve enough information to audit:

- concrete URL/source identity;
- whether content was actually read or only discovered;
- evidence role;
- material claim supported;
- important limitation/counter-evidence.

A plausible synthesis without traceable sources is not accepted evidence.

Runtime/local A/B is **not default**. Use it only if a concrete unresolved adoption decision could change because of the result.

## 6. After P03

After a trustworthy P03 close, select one engineering-type card such as P07 code understanding or P10 testing and execute it with the same evidence discipline.

Only then reassess whether heterogeneous evidence is sufficient to package a minimal user-facing Curator and move into real-user adoption validation.

Do not predeclare that transition now.

## 7. Candidate Skill status

Current candidate:

- `skills/curating-erp-ai-resources/SKILL.md`

Its simplified leverage-first direction is broadly aligned with the North Star, but it is **experimental** until the validation sequence is trustworthy again.

Do not describe it as proven Minimal Curator V0.1.

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

Current milestone is **not** “real users love the product” yet.

It is:

> **Complete P03 with a trustworthy, auditable evidence chain and a stable colleague recommendation; then test one engineering-type heterogeneous card before deciding whether the method is ready for a minimal real-user pilot.**
