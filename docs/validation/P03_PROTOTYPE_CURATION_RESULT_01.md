# P03 — Requirements / Rules → Clickable Prototype / UI Demo

Date: 2026-08-30

## Verdict

> **CLOSED — CODED PROTOTYPE DEFAULT; FIGMA MAKE WHEN THE TEAM IS FIGMA / DESIGN-SYSTEM FIRST**

For ERP / enterprise-information-system practitioners, the default recommendation is **not** “find the strongest one-click prototype generator” and not “install a dedicated prototype Skill”.

The durable pattern is:

```text
confirmed business rules / user stories / flow / states
→ AI-generated coded prototype
→ review business semantics and edge cases
→ iterate in code / visual editor
→ hand off or keep as demo artifact
```

For a consultant / PM who needs a reviewable B-end demo quickly and does not already live inside a mature Figma design-system workflow, a **coded prototype path** (for example v0 or an AI IDE / coding Agent) is the default low-friction recommendation.

When the team already has a mature Figma library / design system and designers are part of the downstream workflow, **Figma Make** becomes the stronger path because it can use existing Figma designs/libraries as context and keep design collaboration close to the source environment.

A dedicated prototype Skill is not justified by current evidence as a default dependency.

## Why this closes P03

### 1. Practitioner evidence establishes the real quality boundary

Recent Chinese PM / design-practice material repeatedly converges on the same point:

- AI can accelerate requirement → front-end demo;
- the hard part is not generating pixels;
- complex business logic, multi-state behavior, branches, exceptions and handoff remain the review burden;
- controllability, reuse, code/design-system grounding and iteration matter more than first-shot visual quality.

Retained practical evidence:

1. **PM维他命 — 产品经理 AI 工作流 / AI IDE 项目结构**
   - 2026 practitioner material;
   - explicitly targets PM daily work, requirement analysis, PRD and demo-level front-end prototypes;
   - uses AI IDEs such as Cursor / Antigravity and emphasizes reusable project structure rather than one-shot prompting;
   - useful because it treats prototype generation as part of a maintainable PM workflow.

2. **AI产品经理养成记 — AI 做产品原型完整流程**
   - 2026 practitioner walkthrough;
   - covers research / user story / structure before prototype, then two modes: precise control vs exploratory co-creation;
   - continues into code management, deployment, review annotation, PRD back-propagation and engineering follow-up;
   - explicitly frames the problem as making AI prototypes controllable, reusable and shippable/reviewable rather than merely attractive.

3. **互联网产品小龙虾 — AI 工具原型实操 / 原型背后的业务逻辑**
   - 7-year product practitioner;
   - explicitly calls out AI weaknesses on complex business scenes, multiple states and branching;
   - stresses that prototypes exist to make business flow, functional structure, field rules, page states and exception cases clear.

4. **范米花儿 — 从 PRD 到前端页面：B 端 AI 工作流**
   - B-end / design-system-adjacent practitioner evidence;
   - uses code-side design system + Skill / component maintenance to accelerate B-end delivery;
   - supports the conclusion that enterprise prototype quality improves when AI is grounded in reusable components/design language rather than free-form generation.

5. **Maple Feather — 2026 PM AI product-design workflow**
   - author reports multi-stage real PM usage;
   - recommends separating requirement clarification, user stories, flow/IA, PRD, wireframe and clickable prototype instead of forcing one model/tool through the entire chain;
   - explicitly notes that prototype work exposes missing flows and sends the PM back to earlier stages.

## Current tool / implementation facts

### v0

Current v0 supports:

- natural-language / screenshot / mockup / Figma input;
- real code and interactive previews;
- direct code editing and visual Design Mode;
- design-system context through registries;
- GitHub branching / commits / PR workflow;
- export/deployment beyond a disposable image mockup.

This makes it a strong low-friction coded-prototype option for dashboards, internal tools and B-end demos.

### Figma Make

Current Figma Make supports:

- functional prototypes / web apps / interactive UI;
- attaching existing Figma designs and design libraries;
- plan-before-code mode;
- iterative prompting plus direct preview/code editing;
- GitHub and design-system-oriented workflows.

Its strongest boundary is when the organization already treats Figma/design libraries as the collaboration source.

Community feedback also shows an important limitation: generated output may still require significant correction for exact interactions, design-system fidelity, Auto Layout/components and handoff precision. Therefore it should not be treated as automatic design truth.

### Lovable

Lovable remains a legitimate alternative when the objective is rapidly turning PRDs/docs/tickets into a working prototype and testing flows before engineering.

However current practitioner/community evidence does not show a decisive advantage over coded-prototype alternatives for the generic ERP/B-end P03 job, and some users report edit/control friction. Keep it as an optional alternative rather than the default recommendation.

## ERP colleague recommendation

### Default path — coded prototype

Use when:

- the goal is a clickable B-end demo for workshop / requirement review;
- there is no strict requirement to stay in Figma;
- business logic, fields, states and exceptions matter more than polished visual design;
- the artifact may later be handed to development or kept under version control.

Suggested sequence:

1. clarify roles, user stories, main flow, key fields, states and exceptions;
2. freeze a small first-demo scope;
3. feed those materials to v0 / AI IDE / coding Agent;
4. generate the first clickable version;
5. review every action for destination/state/error/permission behavior;
6. iterate only the incorrect parts;
7. preserve code / version history and update the PRD when the prototype reveals requirement gaps.

### Figma-first path

Use Figma Make when:

- the organization already has a Figma design system/library;
- designer collaboration and downstream Figma workflow matter;
- matching existing tokens/components is more important than generic code ownership.

## What must still be human-reviewed

- business meaning and scope;
- role / permission differences;
- state transitions;
- exception and cancellation paths;
- field rules and validations;
- whether the prototype accidentally invents behavior;
- whether a polished visual hides an incorrect workflow.

## Why no local runtime test

A local A/B would mostly compare transient model/tool output quality on one synthetic UI.

Current adoption decision is already stable from:

- multiple practitioner workflows;
- B-end-specific evidence;
- current implementation capabilities;
- community counter-evidence about control/handoff limits.

A runtime test would not plausibly change the default recommendation unless a real colleague later has a specific design-system, permission, deployment or local-environment constraint.

## Stop rationale

P03 now answers the colleague decision:

- **Do I need a special Skill?** Usually no.
- **What should I use by default?** A coded prototype workflow grounded in clarified business semantics.
- **When should I prefer Figma Make?** When Figma/design-system collaboration is already the organizational source of truth.
- **What is the main failure mode?** A visually plausible prototype that silently gets business states/branches/permissions wrong.

Further generic tool comparison is unlikely to change this decision.
