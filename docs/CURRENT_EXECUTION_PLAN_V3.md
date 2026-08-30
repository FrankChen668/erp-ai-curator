# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. The context-drift correction remains recorded in `docs/REBASE_AUDIT_20260830.md`. P03 and P07 have since been rerun from scratch with auditable evidence trails.

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

- 83-response 2026-08 training survey;
- normalized semantics in `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

The survey validates demand, not recommendation outcome.

### P01 — retained, low maturity

> **KEEP FOR PRACTICAL PILOT — HIGH TASK FIT / LOW INDEPENDENT VALIDATION**

### P04 — accepted closed card

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority: `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`.

### P06 — accepted closed card

> **CLOSED — PLAIN CODE-FIRST DEFAULT WITH EXPLICIT RECONCILIATION CONTROLS; HUASHU OPTIONAL**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

### P03 — accepted closed card after clean rerun

> **CLOSED — SPEC-FIRST CODE PROTOTYPE DEFAULT; FIGMA MAKE CONDITIONAL UPGRADE**

Authority: `docs/validation/P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — accepted closed engineering card after clean rerun

> **CLOSED — TRACEABLE READ-ONLY REPO EXPLORATION DEFAULT; CONDITIONAL LSP/SEMANTIC OR ERP-NATIVE MCP UPGRADE**

Authority: `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

Reason accepted:

- rerun began from survey semantics rather than the invalid prior verdict;
- professional comprehension research, practitioner success/failure evidence and Chinese practical workflow were actually read;
- current large-repository Agent guidance and serious semantic/graph implementations were inspected;
- SAP system-native MCP capability and security/write-risk boundaries were separately verified;
- the result distinguishes implemented code facts from inferred business intent;
- no synthetic runtime test was manufactured when no representative real legacy/system-native repository was available.

## 3. Invalidated sprint conclusions remain invalid

The following files remain **not accepted product evidence**:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md`.

Only Result 02 files are authoritative for P03/P07.

The old claims “validation complete / Minimal Curator V0.1 validated / REAL USER PILOT already started” do not become true merely because the replacement cards are now closed. They require a fresh cross-card reassessment.

## 4. Correct current checkpoint

> **P03 and P07 are now trustworthy closed cards. The next task is cross-card method reassessment, not another default validation card.**

The corrected evidence discipline has now been exercised across materially different work:

- requirement/workshop packaging (P01, lower maturity);
- business-process diagramming (P04);
- ERP-like data reconciliation with bounded runtime evidence (P06);
- requirements/rules → clickable prototype (P03);
- engineering/codebase understanding (P07).

This is sufficient to ask the next product question, but not to prejudge its answer.

## 5. Immediate next action — cross-card reassessment

Reassess whether the candidate Curator method is stable enough for a minimal real-user pilot.

Required sequence:

```text
trustworthy P01/P04/P06/P03/P07 evidence
→ candidate Skill current text
→ extract recurring rules only
→ test for contradictions / overfitting / framework creep
→ identify any narrowly necessary Skill correction
→ decide:
    stable enough → package minimal user-facing Curator + bounded REAL_USER pilot
    material contradiction → correct only that contradiction, then reassess
```

Questions to answer:

1. Do the cards repeatedly support “ordinary AI first, specialized capability only for a concrete gap”?
2. Is practitioner-first discovery consistently useful when external resources are actually needed?
3. Does runtime testing add value only when a material adoption decision remains unresolved?
4. Does the current Skill preserve source/evidence discipline without becoming a rigid framework?
5. Are there any card-specific rules that were accidentally generalized?
6. Is the next uncertainty now **real-user adoption/outcome**, rather than more synthetic method validation?

Do not add P10 or another card by default before answering these questions.

## 6. Candidate Skill status

Current candidate:

- `skills/curating-erp-ai-resources/SKILL.md`

Status:

> **experimental candidate — cross-card reassessment pending**

Repeated evidence supports its leverage-first direction, but validation status must come from the reassessment, not from naming/versioning.

If changes are needed, keep them minimal and derived from repeated evidence. Do not encode P03/P07-specific implementation details into the permanent method.

## 7. Cloud / local split

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

## 8. Task preflight

Before any non-trivial task, confirm:

1. current milestone;
2. concrete evidence the task will create;
3. why the evidence can change a product/adoption decision;
4. why the task is preferable to directly executing the current milestone.

Goal hierarchy:

```text
North Star
→ current trustworthy checkpoint
→ decision-changing evidence
→ task
→ artifact / test / commit / Agent
```

## 9. Anti-drift

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

## 10. Current milestone

> **Determine whether the recurring Curator method is now stable enough to become a minimal user-facing Curator and enter a bounded real-user adoption pilot. Make that decision from the trustworthy cross-card evidence before doing more card validation.**
