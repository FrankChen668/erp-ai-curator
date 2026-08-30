# Minimal Curator V0.1 / Skill 0.6.2 — Harness Consistency Patch

Date: 2026-08-30
Status: **ACCEPTED NARROW HARNESS PATCH — REAL_USER PILOT REMAINS ACTIVE**

## 1. Trigger

Authority:

- `docs/validation/CURATOR_061_BOUNDARY_REGRESSION_RESULT_01.md`

The isolated 0.6.1 regression found:

- no over-tooling signal;
- under-tooling in Case 5 / 38, lightly in Case 8;
- no proven permanent domain-rule defect;
- no clear repeatable adoption advantage over ordinary Agent.

The initial response was to keep 0.6.1 unchanged because the relevant rules already existed.

## 2. Harness-engineering reinterpretation

The observed failure is better framed as:

> **The rule exists, but its execution is not sufficiently legible/enforceable at the decision boundary.**

This does not justify adding Oracle/SAP cases or another general rule. It justifies a narrow execution invariant.

The patch follows the Harness Engineering principle: when an Agent struggles, identify the missing capability/guardrail/legibility and encode the smallest reusable feedback mechanism rather than asking the model to “try harder”.

## 3. 0.6.2 change

`skills/curating-erp-ai-resources/SKILL.md` remains method-equivalent to 0.6.1, but adds one final adoption-consistency checkpoint.

New on-demand reference:

- `skills/curating-erp-ai-resources/references/adoption-consistency.md`

It is loaded only when all of the following are true:

1. the run has already identified a concrete capability gap;
2. the run is still preparing to output no specialized resource / ordinary-AI-only / low-cost-trial-first;
3. the justification for not crossing the adoption threshold is not already clear.

The check asks whether:

- the gap is observable and material;
- a specialized capability directly solves it;
- expected benefit exceeds adoption/setup/security/maintenance cost.

If the answer supports specialization, the run must reconsider B or conditional B. If not, A/C remains valid with an explicit reason.

## 4. What this does not add

Do not add from this patch:

- Oracle EBS scenario rules;
- SAP/ABAP scenario rules;
- fixed Tool/MCP recommendations;
- mandatory external search;
- mandatory resource recommendation;
- scoring/Gate systems;
- another synthetic regression round.

## 5. Why no new internal test

The previous paired regression already identified the failure mode. A new synthetic retest would mostly measure another stochastic sample and would not answer the dominant product question.

The next useful feedback loop is real-user use:

```text
real task
→ 0.6.2 recommendation
→ colleague acts / modifies / rejects
→ inspect whether the consistency check avoided both over-tooling and under-tooling
→ narrow correction only if real evidence requires it
```

## 6. Evidence boundary

0.6.2 is a Harness consistency improvement, not evidence that the product is validated or that Curator outperforms ordinary Agent.

The dominant uncertainty remains real-user adoption/outcome.
