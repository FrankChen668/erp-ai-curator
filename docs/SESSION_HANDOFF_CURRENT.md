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

### P06

Status:

> **CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

### P03 — newly rerun and accepted

Status:

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_02.md`

Why trusted:

- rerun began from survey semantics rather than the invalid prior verdict;
- concrete URLs and source roles are retained;
- actually-read evidence is separated from discovery-only coverage gaps;
- Chinese practical workflow, independent practitioner counter-evidence, current platform facts and original Skill implementations are represented;
- limitations and the reason not to run synthetic runtime A/B are explicit.

Bounded recommendation:

- clarify roles/permissions/fields/validation/states/transitions/exceptions first;
- use a code-capable Agent for a small interactive review artifact by default;
- use Figma Make when Figma/design-system/collaboration context materially changes the workflow;
- use hosted builders such as Lovable conditionally when app-like hosted behavior is worth the cloud/data boundary;
- install specialized prototype Skills only for a concrete adjacent missing capability.

## 5. Critical correction — invalid sprint files remain invalid

The earlier long-context sprint artifacts remain invalid:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` = **INVALIDATED / NOT PRODUCT EVIDENCE**.

P03 Result 02 does **not** rehabilitate Result 01.

Still withdrawn:

- “P07 closed”;
- “five heterogeneous cards prove validation complete”;
- “Minimal Curator V0.1 is validated”;
- “current authoritative phase is REAL USER PILOT”.

Do not use prior P07 claims such as “repo-aware Agent default / specialist code-understanding Skill unnecessary” as established facts. They must be independently rediscovered and supported if they are to return.

## 6. Candidate Skill status

`skills/curating-erp-ai-resources/SKILL.md` remains:

> **experimental candidate — validation incomplete**

P03 supports its leverage-first direction but does not justify prototype-specific permanent rules or a validated-product claim.

## 7. Correct current checkpoint

> **P03 is closed. P07 is next.**

Current milestone:

> **Complete P07 with a trustworthy, auditable evidence chain and stable colleague recommendation. Then reassess whether heterogeneous evidence is sufficient for a minimal real-user pilot.**

P07 is preferred over P10 because it is a materially different engineering task and its prior close was invalidated, making it the cleanest test of the corrected evidence discipline.

## 8. Immediate next cloud action — start P07 from scratch

P07 real job from survey semantics:

> A consultant/developer inherits an SAP/Oracle/custom-system codebase or enhancement and needs to understand structure, business logic, call chains, potential changes/defects/performance issues and sometimes reverse-generate functional logic/specification.

Do not reuse the invalid P07 result as an answer or search prior.

Cloud should:

1. search practitioner-first for current real codebase-understanding workflows/cases;
2. retain concrete URLs and distinguish discovery-only vs actually-read sources;
3. inspect serious code-Agent / Skill / MCP / architecture-understanding candidates;
4. verify only current facts that affect adoption (repository context, indexing/context behavior, local/cloud boundary, privacy/security, installation/cost where material);
5. look for failure, context-loss, hallucination, unsafe-change and correctness counter-evidence;
6. decide whether a plain repo-aware Agent is enough or a specialized capability materially improves the job;
7. use local/runtime testing only if a material unresolved adoption decision could change because of it;
8. write one concise P07 authority and stop.

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
3. do not reopen settled P03/P04/P06;
4. immediately begin a trustworthy P07 cloud curation cycle;
5. stop only for a genuine Owner decision or evidence barrier.
