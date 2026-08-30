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

Important boundary:

- aggregate closed-choice data is direct evidence;
- free-text is semantic evidence and may contain platform-side wording cleanup;
- survey demand does not prove recommendation outcomes.

Problem Cards P01–P14 are normalized demand units, not permanent taxonomy.

## 4. Trusted card evidence

### P01

Status:

> **KEEP FOR PRACTICAL PILOT — high task fit / low independent validation**

Do not overstate maturity.

### P04

Status:

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Why trusted: concrete URLs, evidence roles, limitations and coverage gaps are retained.

### P06

Status:

> **CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

Why trusted: pinned candidate commit, isolated baseline/with-Skill runs, hidden truth and retained runtime artifacts.

## 5. Critical correction — DO NOT REUSE INVALID SPRINT CONCLUSIONS

During the previous long-context sprint, cloud rapidly produced P03/P07 close reports and then inferred that validation was complete.

Re-audit found the evidence trail was insufficient.

Therefore:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**;
- “P03 closed” = withdrawn;
- “P07 closed” = withdrawn;
- “five heterogeneous cards prove validation complete” = withdrawn;
- “Minimal Curator V0.1 is validated” = withdrawn;
- “current authoritative phase is REAL USER PILOT” = withdrawn.

Do not use prior P03 claims such as “coded prototype default / Figma Make boundary” as established facts.

Do not use prior P07 claims such as “repo-aware Agent default / specialist code-understanding Skill unnecessary” as established facts.

They must be independently rediscovered and supported if they are to return.

## 6. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` is version `0.5.1`.

Status:

> **experimental candidate — validation incomplete**

Its leverage-first structure is directionally consistent with the North Star, but it is not accepted proof of product readiness.

The Skill must not carry P03/P07 sprint-specific conclusions as validated behavior.

## 7. Correct current checkpoint

> **P06 is closed. P03 is next.**

This is the last trustworthy controlled checkpoint before the invalid sprint.

Current milestone:

> **Complete P03 with a trustworthy, auditable evidence chain and stable colleague recommendation. Then execute one engineering-type heterogeneous card such as P07 or P10 before deciding whether to enter a minimal real-user pilot.**

## 8. Immediate next cloud action — start P03 from scratch

P03 real job from survey semantics:

> A consultant/PM has requirements, fields, roles, states and exceptions and needs a clickable prototype for requirement clarification or solution review. They need a reviewable and iteratable artifact, not merely a pretty mockup.

Do not reuse the invalid P03 result as an answer or search prior.

Cloud should:

1. search practitioner-first for current real workflows/cases;
2. retain concrete URLs and distinguish discovery-only vs actually-read sources;
3. inspect serious Tool / Skill / implementation candidates;
4. verify only current facts that affect adoption (input/output, editability, collaboration, pricing/availability/privacy where material);
5. look for failure/rework/counter-evidence;
6. decide whether the adoption boundary is stable;
7. use local/runtime testing only if a material unresolved decision could change because of it;
8. write one concise P03 authority with auditable evidence and stop.

## 9. Evidence acceptance discipline

For every retained external source, preserve enough to answer:

- exact source/URL;
- was it actually read or only discovered?;
- evidence role;
- material claim supported;
- limitation/counter-evidence.

Source-less synthesis may be useful reasoning but is not product evidence.

A card cannot be `CLOSED` because the conclusion sounds plausible.

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
3. do not reopen settled P04/P06;
4. immediately begin a trustworthy P03 cloud curation cycle;
5. stop only for a genuine Owner decision or evidence barrier.
