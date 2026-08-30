# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. Context-drift correction remains recorded in `docs/REBASE_AUDIT_20260830.md`. P03/P07 were rerun from scratch, and the subsequent cross-card reassessment is now complete.

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

Demand authority:

- 83-response 2026-08 training survey;
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

Accepted heterogeneous task evidence:

- P01 — workshop/minutes → requirement package: **high task fit / low independent validation**;
- P04 — business logic → editable process diagram: **CLOSED**;
- P06 — ERP-style reconciliation: **CLOSED**, with bounded runtime evidence;
- P03 — requirements/rules → clickable prototype: **CLOSED** via clean Result 02;
- P07 — codebase/program → logic/FS/defect hypotheses: **CLOSED** via clean Result 02.

Current evidence authority:

- `docs/validation/EVIDENCE_STATUS.md`

Invalidated files remain invalid:

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md`;
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md`.

Only Result 02 is authoritative for P03/P07.

## 3. Cross-card method decision

Authority:

- `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`

Verdict:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The recurring method survived materially different tasks without requiring contradictory permanent rules:

1. start from the real job, actual artifacts, deliverable and material constraints;
2. ordinary AI / existing Agent is the baseline;
3. specialized capability is introduced only for a concrete bottleneck;
4. when external adoption evidence matters, prefer practitioner workflow/failure evidence → original implementation → decision-changing current official facts;
5. important outputs remain source/project/system grounded and unknowns are explicit;
6. local/runtime testing is used only when the result can change the adoption recommendation;
7. stop when the colleague's next action is stable.

This is sufficient method readiness for a pilot. It is not evidence that real users already gain time, quality or adoption value.

## 4. Minimal Curator V0.1 status

Current Skill:

- `skills/curating-erp-ai-resources/SKILL.md`
- version `0.6.0`

Status:

> **Minimal Curator V0.1 — real-user pilot candidate**

The Skill intentionally contains recurring method principles rather than accumulating P03/P04/P06/P07 scenario answers.

Do not describe it as a validated product yet.

## 5. Correct current checkpoint

> **Internal heterogeneous method validation is sufficient for pilot readiness. The dominant uncertainty is now real-user adoption/outcome.**

Do not add P10 or another validation card by default.

The next decision-changing evidence must come from a real colleague using the Curator on a real work task.

## 6. Immediate next action — bounded REAL_USER pilot

Pilot authority:

- `docs/REAL_USER_PILOT_V1.md`

For each real task:

```text
real colleague task/materials/constraints
→ Minimal Curator V0.1 recommendation
→ colleague actually tries / modifies / rejects it
→ capture usable result or concrete failure
→ inspect saved search/setup/rework or missed constraint
→ narrow method correction only if evidence requires it
```

Capture only decision-changing evidence:

- task in the colleague's own words;
- recommendation actually given;
- what they actually did;
- artifact/result or rejection reason;
- where the recommendation saved or added effort;
- missed capability, privacy, permission or environment constraints;
- whether they would bring another real task.

Do not require users to classify their task into Problem Cards.

## 7. Pilot success/failure interpretation

Positive direction:

- next action becomes clearer;
- colleagues can start from real project materials;
- unnecessary Tool/Skill installation is avoided;
- specialized capability is recommended for an observable reason;
- important limitations appear before they create rework;
- colleagues would reuse the Curator on another real task.

Important negative signals:

- recommendations are reasonable but users do not act;
- Curator searches/tools when ordinary AI was already enough;
- setup/search cost exceeds the value created;
- material project/privacy/permission constraints are missed;
- generated recommendations are too generic to improve on the user's existing AI workflow.

No arbitrary numeric PASS threshold is required in advance.

## 8. Cloud / local split

Cloud/ChatGPT owns:

- running Curator recommendations for submitted real tasks;
- current Web/GitHub research when external resources are actually needed;
- product/adoption judgement;
- evidence review and narrow method corrections;
- GitHub authority maintenance.

Use a local Agent only when a real pilot task materially requires local files/repository/runtime evidence.

Agent availability is not a reason to create work.

## 9. Anti-drift during pilot

Do not return to internal validation work merely because it is easier to execute.

Do not add without real-user evidence of need:

- new validation cards by default;
- fixed scenario taxonomy;
- scoring/Gate systems;
- mandatory runtime benchmarks;
- resource databases or automatic refresh;
- multi-Agent orchestration;
- source/influencer rankings;
- card-specific rules in the permanent Skill.

Synthetic/internal testing is justified only to fix a defect exposed by real use or remove a concrete pilot blocker.

## 10. Current milestone

> **Run Minimal Curator V0.1 on genuine colleague tasks and obtain the first real adoption/outcome evidence. Do not substitute more internal proof for this milestone.**
