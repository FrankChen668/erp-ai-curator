# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Demand evidence

The 83-response 2026-08 training survey remains the primary REAL_USER demand source.

Supported conclusions:

- implementation consultants and project managers are the main audience;
- users already use AI heavily;
- the major gap is practical delivery quality, not AI introduction;
- recurring jobs include requirements, prototypes, diagrams, PPT, Excel/data, testing, code understanding/debugging, project management and Agent usage;
- typical inputs are real project artifacts rather than abstract prompts.

The survey validates demand, not recommendation outcome.

## 2. Curator-method validation — sufficient for V0.1

Current heterogeneous evidence spans five materially different task classes.

### P01 — workshop/minutes → requirement package

Status: **KEEP FOR PRACTICAL PILOT**

Retained: `Convert Notes to Requirements Working Skill`

Classification: **high task fit / low independent validation**.

### P04 — business logic → editable process diagram

Status: **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority: `P04_PRACTITIONER_CURATION_RESULT_02.md`

Lesson: semantic clarification precedes diagram generation; AI output remains a review artifact.

### P06 — Excel/CSV/system export → reconcile and validate

Status: **CLOSED — PLAIN CODE-FIRST DEFAULT / HUASHU OPTIONAL**

Authorities:

- `DELIVERY_P06_DATA_RECONCILIATION.md`
- `P06_LOCAL_RUNTIME_RESULT_01.md`
- `evidence/p06/`

Lesson: a specialized Skill is not required when a plain code Agent can provide deterministic execution plus row/amount/control-total checks, conservative matching and review routing.

### P03 — requirements/rules → clickable prototype/UI demo

Status: **CLOSED — CODED PROTOTYPE DEFAULT; FIGMA MAKE FOR FIGMA/DESIGN-SYSTEM-FIRST TEAMS**

Authority: `P03_PROTOTYPE_CURATION_RESULT_01.md`

Supported judgement:

- generic ERP/B-end prototype work should use clarified business rules/states/flows → coded clickable prototype → human review/iteration;
- v0 / AI IDE / coding Agent are valid low-friction coded-prototype paths;
- Figma Make becomes preferable when existing Figma libraries/design-system collaboration are already central;
- no dedicated prototype Skill is justified as a default dependency;
- main failure mode is a plausible-looking UI that gets business states, branches, permissions or field rules wrong.

No generic P03 runtime comparison is justified because it would benchmark transient model output rather than resolve an adoption gap.

### P07 — codebase/program → understand logic / support FS / locate defects

Status: **CLOSED — REPO-AWARE CODE AGENT DEFAULT**

Authority: `P07_CODEBASE_UNDERSTANDING_RESULT_01.md`

Supported judgement:

- capable repo-aware code Agents already cover unfamiliar-code exploration, feature tracing, debugging, tests and documentation;
- business/FS explanations should be recovered from code/data/integration evidence with source pointers and explicit uncertainty;
- critical conclusions/fixes require tests/logs/runtime evidence and independent review where consequence warrants it;
- a specialist graph/architecture/code-understanding layer is justified only when normal repo navigation is materially inadequate.

No generic runtime A/B is justified because the adoption boundary is already stable.

## 3. Cross-card conclusion

Across text, diagrams, data, interactive prototypes and code, the Curator repeatedly demonstrates the intended behavior:

- real task before Tool;
- plain AI/Agent is a valid final recommendation;
- specialist capability is introduced only when it adds material value;
- practitioner evidence is prioritized for adoption questions;
- author/official evidence roles remain explicit;
- runtime testing is targeted rather than default;
- work stops when the colleague decision stabilizes.

This is enough to exit Curator-method validation for Minimal Curator V0.1.

## 4. Minimal Curator V0.1

Primary artifact:

- `skills/curating-erp-ai-resources/SKILL.md`
- Skill version `0.5.0`

The Skill now emphasizes user-facing decision quality instead of the earlier Gate/scoring/staging machinery.

Default decision sequence:

```text
real work task
→ AI leverage judgement
→ general AI enough?
→ targeted discovery only when needed
→ necessary fact/safety checks
→ small actionable recommendation
→ stop
```

## 5. Evidence boundary

None of the current cards prove universal performance.

Do not interpret them as:

- permanent Tool whitelists;
- “plain AI always works”;
- “specialized Skills are unnecessary”;
- independent production validation for every retained resource.

They validate the Curator's **decision behavior strongly enough to start real-user piloting**.

## 6. Main uncertainty now

The dominant uncertainty has changed from method design to product usefulness:

> **Will real ERP colleagues actually use the recommendation, save search/learning/rework time, and come back for another task?**

That can only be answered by real-user pilot evidence.

## 7. Current stop rule

Do not continue synthetic/representative Problem Cards merely to increase coverage.

Reopen validation only if real-user usage reveals a concrete failure pattern that could materially change Curator decision logic.
