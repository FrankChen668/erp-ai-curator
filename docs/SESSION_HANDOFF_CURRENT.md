# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> **Fresh-session authority after context reset.** Always inspect current `main` first. Do not rely on prior chat summaries when they conflict with repository evidence.

## 1. Repository / authority

- GitHub: `FrankChen668/erp-ai-curator`
- North Star: `docs/PROJECT_NORTH_STAR.md`
- Current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`
- Context-drift correction: `docs/REBASE_AUDIT_20260830.md`
- Candidate Skill: `skills/curating-erp-ai-resources/SKILL.md`

## 2. Product objective

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners.

Core question:

> **面对一个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
→ practical AI working-method recommendation
```

The product is not a generic AI tool directory, Prompt library, tutorial encyclopedia or tool-certification lab.

## 3. Demand baseline — trusted

Primary REAL_USER demand source:

- 83-response 2026-08 training survey;
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Survey demand does not prove recommendation outcomes.

## 4. Trusted card evidence

### P01

> **KEEP FOR PRACTICAL PILOT — high task fit / low independent validation**

### P04

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority: `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`.

### P06

> **CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

### P03

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority: `docs/validation/P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — newly rerun and accepted

> **CLOSED — traceable read-only repo exploration default; conditional LSP/semantic or ERP-native MCP upgrade**

Authority: `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Bounded recommendation:

- start from a concrete question, not “understand the whole codebase”;
- keep first-pass exploration read-only and evidence-linked;
- move global → relevant flow/modules → detailed source/test/log verification;
- distinguish observed behavior, inference and business-confirmation-required unknowns;
- ordinary local Git repo: repo-aware Agent first;
- noisy cross-symbol/cross-module retrieval: native LSP/semantic navigation, then dedicated tool only if the bottleneck persists;
- code/system truth outside local files: system-native connector/MCP can materially help; SAP ABAP is a clear current example;
- live SAP write/activation capabilities increase the need for least privilege;
- no synthetic runtime A/B without a representative real repository.

## 5. Critical correction remains in force

The earlier long-context sprint artifacts remain invalid:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**.

Only Result 02 files are authoritative.

Do not restore the old claims “validation complete / Minimal Curator V0.1 validated / REAL USER PILOT started” by historical inheritance. They require a fresh cross-card reassessment now that the evidence gap has actually been repaired.

## 6. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` remains:

> **experimental candidate — cross-card reassessment pending**

Repeated trustworthy evidence supports its leverage-first direction, but it must now be checked for contradiction, overfitting and framework creep before being called a minimal validated Curator.

## 7. Correct current checkpoint

> **P03 and P07 are trustworthy closed cards. The next action is cross-card method reassessment.**

Do not default to P10 or another card before this product decision.

Current milestone:

> **Determine whether the recurring Curator method is stable/minimal enough for a bounded real-user adoption pilot.**

## 8. Immediate next cloud action — reassess, do not accumulate more cards

Cloud should:

1. reread the candidate Skill plus trustworthy P01/P04/P06/P03/P07 evidence;
2. extract only recurring decision rules across heterogeneous cards;
3. check whether “ordinary AI first / specialized capability only for a concrete gap” survives all cards;
4. check practitioner-first discovery, source-role separation and stop decisions for repeated support;
5. check whether any P03/P07/P06-specific detail was accidentally generalized into the Skill;
6. adversarially inspect complexity: remove rules that exist only to make the method look complete;
7. decide whether the remaining uncertainty is now real-user adoption/outcome;
8. if stable, package the smallest usable Curator and define a bounded pilot; if not, make only the narrow correction and reassess.

No new runtime benchmark, taxonomy or resource database is implied by this step.

## 9. Evidence acceptance discipline

For every retained external source, preserve enough to answer:

- exact source/URL;
- was it actually read or only discovered?;
- evidence role;
- material claim supported;
- limitation/counter-evidence.

Source-less synthesis may be useful reasoning but is not product evidence.

## 10. Cloud / local split

Cloud owns product judgement, Web/GitHub research, source prioritization, current fact checks, adversarial review, static inspection and final stop/recommendation decisions.

Use local Agent only when local capability materially adds evidence: local files/repo/runtime, inaccessible-source acquisition, environment-specific evidence or justified reproducibility.

Do not create tasks merely to keep a local Agent busy.

## 11. Anti-drift

Avoid:

- new Gate/benchmark/framework per candidate;
- official-document gravity;
- platform/source quotas;
- author self-tests presented as independent proof;
- runtime testing by default;
- specialized Skill recommendations when plain AI is sufficient;
- synthetic/readiness work presented as product evidence;
- undocumented external claims;
- long-context synthesis silently promoted to evidence.

## 12. New-session start instruction

When a fresh cloud conversation starts:

1. inspect current `main`;
2. read this handoff + Current Plan + Evidence Status + Rebase Audit;
3. do not reopen settled P03/P04/P06/P07 without a new material reason;
4. immediately perform the cross-card candidate-Skill reassessment;
5. stop only for a genuine Owner decision or evidence barrier.
