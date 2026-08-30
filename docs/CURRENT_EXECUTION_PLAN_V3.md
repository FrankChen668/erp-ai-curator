# ERP AI Curator — Current Execution Plan V3

Date: 2026-08-30

> Current execution authority. Context-drift correction remains recorded in `docs/REBASE_AUDIT_20260830.md`. Minimal Curator V0.1 remains in a bounded real-user pilot.

## 0. Owner execution continuity rule

Authority: `docs/OWNER_EXECUTION_RULES.md`.

> **Cloud/ChatGPT must continue any useful next step it can execute itself. It stops only for a genuine Owner decision, a genuine Local Agent handoff, or an external evidence barrier. When it stops, the next actor/task/result must be explicit.**

This does not authorize busywork; continue the highest-value current milestone.

## 1. Product objective

ERP AI Curator helps SAP / Oracle / ERP / enterprise-information-system practitioners find the **best existing AI working method for a real delivery task**.

Core question:

> **面对这个真实工作任务，普通 AI 是否已经够用？如果不够，互联网上已经存在的实操经验、Tool / Skill / MCP / 方法 / 教程中，什么最值得学习和采用？**

Main chain:

```text
real task
→ AI leverage judgement
→ practitioner workflow / review / failure evidence
→ original Tool / Skill / repo verification
→ decision-changing official facts
→ small curated best-practice recommendation
```

The default product output is **best-practice / existing-resource curation**, not a full execution SOP and not a user tool-testing program.

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

Current evidence authority: `docs/validation/EVIDENCE_STATUS.md`.

Invalidated P03/P07 Result 01 files remain invalid. Only Result 02 is authoritative.

## 3. Cross-card method decision

Authority: `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`.

Verdict:

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

The recurring method remains:

1. start from the real job, actual artifacts, deliverable and material constraints;
2. ordinary AI / existing Agent is the baseline;
3. specialized capability is introduced only for a concrete bottleneck;
4. when external evidence matters, practitioner workflow/failure evidence comes before vendor feature lists;
5. verify original Tool / Skill / repo and only decision-changing current facts;
6. local/runtime testing is used only when the result can change the recommendation;
7. stop when the user has a stable small set of best practices/resources worth learning or adopting.

## 4. Minimal Curator V0.1 status

Current Skill:

- `skills/curating-erp-ai-resources/SKILL.md`
- version `0.6.3`

Status:

> **Minimal Curator V0.1 — real-user pilot candidate**

0.6.2 added the adoption-consistency Harness check. 0.6.3 adds a product-boundary Harness correction after Pilot Case 001 drifted from Curator work into execution/test coaching.

Authorities:

- `docs/validation/CURATOR_062_HARNESS_PATCH.md`
- `docs/validation/CURATOR_063_BEST_PRACTICE_BOUNDARY_PATCH.md`

Do not describe it as a validated product yet.

## 5. Correct current checkpoint

> **REAL_USER best-practice curation / adoption remains the active product milestone.**

The product must first give a real colleague a high-value curated answer to a real task. User adoption/modification/rejection is then captured as validation evidence.

Do not invert this order by making the user perform a test protocol as the Curator's main output.

## 6. Active Pilot Case 001 — ERP operating manual

Authority:

- `docs/pilot/PILOT_CASE_001_ERP_OPERATING_MANUAL.md`

Current status:

> **BEST-PRACTICE CURATION READY — AWAITING REAL USER FEEDBACK / ADOPTION**

Case 001 now curates the reusable practice rather than prescribing a test:

- task/role-based modular documentation;
- capture-assisted screenshot/annotation work;
- stable text for business context, permissions, exceptions and notes;
- selective screenshots instead of image-per-step by default;
- change-oriented maintenance;
- cloud/local choice driven by enterprise data boundaries.

Guidde / Folge are implementation candidates for different boundaries, not the product itself.

## 7. Immediate next action — real-user curation loop

For each genuine case:

```text
real colleague task/materials/constraints
→ Minimal Curator 0.6.3 finds and compresses best practices
→ user receives 0–1 primary resource / method by default
→ user may learn / adopt / modify / reject naturally
→ capture concrete feedback if available
→ narrow method/harness correction only if evidence requires it
```

Capture only decision-changing validation evidence:

- which recommendation/resource the user actually found useful or useless;
- whether it reduced search/selection effort;
- whether an important capability/privacy/permission/environment constraint was missed;
- whether they adopted, modified or rejected it and why;
- whether they would bring another real problem to Curator.

## 8. Cloud / local split

Cloud/ChatGPT owns:

- continued execution whenever cloud capabilities are sufficient;
- current Web/GitHub best-practice/resource research;
- practitioner/original/official evidence separation;
- product/adoption judgement;
- evidence review and narrow method/harness corrections;
- GitHub authority maintenance.

Use a Local Agent only when a real curation decision materially depends on local files/repository/runtime, enterprise environment or environment-specific reproducibility.

Agent availability is not a reason to create work.

## 9. Anti-drift during pilot

Do not add without real-user evidence of need:

- new validation cards by default;
- new synthetic boundary regressions by default;
- fixed scenario taxonomy;
- scoring/Gate systems;
- mandatory runtime benchmarks;
- resource databases or automatic refresh;
- multi-Agent orchestration;
- source/influencer rankings;
- card-specific rules in the permanent Skill;
- user test protocols as the default Curator deliverable.

## 10. Current milestone

> **Use Minimal Curator 0.6.3 to turn genuine colleague problems into small, evidence-backed best-practice recommendations, then observe whether colleagues actually find them worth learning/adopting.**
