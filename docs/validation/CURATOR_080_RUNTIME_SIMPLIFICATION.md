# Curator 0.8.0 — Runtime Simplification

Date: 2026-08-30
Status: **SIMPLIFICATION IMPLEMENTED / CLOUD BOUNDED REGRESSION PASS / ORIGINAL-HOST BEHAVIOR STILL REAL-USE EVIDENCE**

## 1. Trigger

After fixing the real flowchart-practice discovery defect in 0.7.1, the Owner challenged a higher-level risk:

> Has the Skill itself become too complex relative to the product goal?

Answer after first-principles and adversarial review: **yes**.

The problem was not file-count compliance. It was cognitive complexity: repeated local defects had accumulated A/B/C, intent separation, adoption consistency, decision-boundary examples, evidence hierarchy, practitioner discovery, safety, multiple output templates and final checks.

Each rule was individually defensible, but together they created patch-on-patch behavior.

## 2. Product goal re-derived from first principles

ERP AI Curator exists to do this:

```text
understand a real ERP / ToB work task
→ find existing practices/resources when that is what the user needs
→ filter noise
→ verify serious candidates/current facts
→ recommend a small number of high-fit practices/resources
→ tell the user when their current toolchain is already enough
```

The user should experience **better search/filter/selection**, not the internal method taxonomy.

Therefore A/B/C can remain useful historical analysis labels in project evidence, but they do not need to be runtime steps.

## 3. External Skill-design principles rechecked

### OpenAI Skill Creator

Current official Skill Creator emphasizes:

- default assumption: Codex is already very smart;
- only add context Codex does not already have;
- challenge whether each paragraph justifies token cost;
- high-variability judgment tasks should have high degrees of freedom;
- keep the core workflow in `SKILL.md` and detailed material in references;
- avoid duplication between `SKILL.md` and references.

Source:

- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md

### Anthropic Skill Creator

Current official Skill Creator emphasizes:

- description is the primary trigger mechanism;
- progressive disclosure;
- prefer imperative but general instructions;
- explain why rather than stacking heavy-handed MUSTs;
- use a few realistic prompts to iterate, with objective evals only where they make sense.

Source:

- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

### Agent Skills / Harness implication

For this high-judgment Curator, the correct direction is not a deterministic decision engine. The repository can retain rich research/evidence; the runtime Skill should be a small behavioral map.

## 4. Proposed simplification before implementation

Initial design target:

- remove mandatory A/B/C from runtime;
- remove adoption-consistency reference;
- remove decision-boundaries reference;
- retain only practitioner discovery and evidence/safety as conditional references;
- collapse runtime into `understand → discover → verify → select/stop`, while preserving the separate question “do you actually need a new capability?”;
- keep user-facing output natural, not category-labelled.

## 5. Adversarial review of the proposal

### Attack A — Are we simply replacing A/B/C with another taxonomy?

Correction: do **not** introduce replacement labels such as Explore/Adopt/Hold. Use natural language only.

### Attack B — Will removing A/B/C reintroduce over-tooling?

Keep one invariant in the core Skill:

> Recommend a new capability only when it solves a concrete gap in the user's current toolchain and the benefit justifies setup/learning/permission/maintenance cost.

No category is needed to express this.

### Attack C — Will practitioner-first now force social-platform search for every task?

No. Practitioner discovery is required when the user explicitly asks for practices/tutorials/resources or when real-use evidence materially affects an adoption decision. It is not a platform quota.

### Attack D — Are we deleting useful evidence discipline?

No. Evidence role and executable-resource safety remain in a single conditional reference because these are easy-to-miss, materially important behaviors.

### Attack E — Will project documents re-inject the old framework?

Correction: `PROJECT_MAP` explicitly marks `AI_LEVERAGE_MODEL_V3.md` as historical/analysis-layer detail, not the 0.8.0 runtime contract. Historical case A/B labels remain evidence records only.

### Attack F — Does simplification make the Skill too vague?

Countermeasure: retain concrete output behavior for the product's most differentiating request—explicit best-practice/tutorial curation must lead with 1–3 selected practitioner resources, priority and boundaries rather than a model-authored tutorial.

## 6. Implemented runtime

`skills/curating-erp-ai-resources/SKILL.md` version `0.8.0` now centers on five steps:

1. understand the real task;
2. identify whether the user wants practice discovery, adoption advice, or both;
3. discover practitioner practice when material;
4. verify serious candidates/current facts;
5. select/compress/stop.

Deleted runtime references:

- `references/adoption-consistency.md`
- `references/decision-boundaries.md`

Retained and simplified:

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

Project Contract adds a runtime `SKILL.md <= 140 lines` simplification guardrail and explicitly checks that removed references do not reappear. This is a size/architecture invariant only; it does not score recommendation quality.

## 7. Bounded Cloud regression

This is a manual Cloud replay of existing real-origin/real-use prompts, not an independent original-host runtime test.

### R1 — Flowchart best-practice request

Intent: `给我找下做流程图的最佳实践`.

Expected critical behavior:

- practitioner discovery occurs even if no new Tool is strictly necessary;
- output can prioritize real Chinese product/ToB-adjacent resources;
- official standards do not replace curation.

Observed Cloud replay:

- found a Bilibili AI product-manager/Skill series with `一句话生成专业流程图/架构图，能用 drawio 二次编辑` and image→editable draw.io content;
- found Agents365 drawio-skill author practice with concrete Flowchart/BPMN/editable capabilities and strong engagement;
- current implementation remains traceable to the Agents365 GitHub repo.

Result: **PASS — practitioner-first behavior survived simplification.**

### R2 — Oracle EBS AI development practice

Expected critical behavior:

- do not hunt for a magical EBS-specific model;
- direct EBS practitioner practice should remain discoverable;
- current implementation/official facts are verification, not the whole answer.

Observed Cloud replay:

- JMJ Cloud `Make Claude Code Your Most Productive Oracle EBS Developer` remains a direct author self-practice candidate describing monorepo + structured EBS context;
- its evidence role remains `author self-practice`, not independent superiority proof.

Result: **PASS — key curation insight survives without A/B/C runtime classification.**

### R3 — Weekly report/PPT consolidation

Existing real-origin problem: multiple consultant reports must be consolidated and key numbers checked.

Critical anti-overtooling behavior under 0.8.0:

- compare against existing AI + Excel/PPT workflow;
- if the real bottleneck is source-of-truth/data consistency rather than missing AI capability, do not recommend another Skill/MCP;
- only upgrade when system/data movement itself becomes the concrete recurring gap.

Manual replay conclusion: **PASS — no new classification is needed to reach the no-new-tool recommendation.**

### R4 — SAP bug / system evidence access

Existing real-origin problem: a non-ABAP consultant wants AI help locating a program bug.

Critical boundary under 0.8.0:

- when complete dump/log/code is already available, use grounded read-only analysis first;
- only recommend SAP-native/system access when the missing root-cause evidence actually lives in ST22/where-used/runtime metadata or other unavailable system facts;
- do not recommend MCP merely because it exists.

Manual replay conclusion: **PASS — system-access boundary survives simplification.**

## 8. What this regression proves / does not prove

Supports:

- the removed runtime taxonomy/references are not necessary to express the four key observed behaviors in the Cloud path;
- simplification preserves practitioner discovery and anti-overtooling boundaries at the instruction level;
- project authority can retain historical evidence without making runtime execute the historical framework.

Does not prove:

- the exact original Agent host will always execute 0.8.0 correctly;
- 0.8.0 is superior to 0.7.1 in real-user outcomes;
- product value over ordinary AI/self-search is validated.

Those remain controlled REAL_USER_USE questions.

## 9. Final adversarial calibration

### Did we simplify only cosmetically?

No. Two runtime references were deleted, mandatory A/B/C classification was removed, multiple output variants/self-checks were collapsed, and `AI_LEVERAGE_MODEL_V3` was demoted from runtime guidance to analysis/history.

### Did we remove too much?

Current bounded replay did not lose the four most important behaviors: practitioner discovery, direct-practice curation, anti-overtooling and conditional system access.

### Are we adding a new framework to police simplicity?

No semantic framework was added. The only mechanical guardrail is line/reference structure because those facts are deterministic.

## 10. Verdict

> **ACCEPT 0.8.0 SIMPLIFIED RUNTIME FOR CONTROLLED USER TRIAL.**

Next product step remains real-user use, not further internal Skill polishing.

Future runtime additions require a stronger burden of proof:

> **If this instruction is removed, does repeated real-user evidence show that user outcomes materially degrade?**

If not, keep it out of the Skill.
