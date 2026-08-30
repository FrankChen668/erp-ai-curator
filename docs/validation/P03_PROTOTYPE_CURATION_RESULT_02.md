# P03 Prototype Curation Result 02

Date: 2026-08-30

> Fresh rerun from the survey-derived P03 job. `P03_PROTOTYPE_CURATION_RESULT_01.md` remains invalidated and was not used as evidence or as a search prior.

## Verdict

> **CLOSE P03 — SPEC-FIRST CODE PROTOTYPE IS THE DEFAULT; FIGMA MAKE IS A COLLABORATION/DESIGN-SYSTEM UPGRADE, NOT A REQUIREMENT**

For an ERP / enterprise-information-system consultant or PM who has requirements, fields, roles, states and exceptions and needs a clickable artifact for requirement clarification or solution review:

- do **not** start by selecting an AI UI generator;
- first turn the source material into a bounded interaction contract;
- use a competent code-capable Agent to generate a small interactive HTML/React prototype;
- verify the important business rules and exception paths by clicking the result;
- introduce Figma Make only when its Figma-native design-system/context/collaboration advantages materially matter;
- use Lovable or similar hosted app builders only when hosted web-app behavior / backend-like state / easy cloud sharing materially outweigh enterprise-data and platform constraints.

A specialized prototype Skill is not mandatory for this P03 job.

## Real job and acceptance boundary

Demand authority: `SURVEY_DERIVED_PROBLEM_CARDS_01.md`.

P03 is not “make a pretty mockup”. The artifact must help people review and iterate:

```text
requirements / source material
→ roles + permissions
→ fields + validation
→ states + transitions
→ normal flow + exception flow
→ clickable review artifact
→ human correction / decision
```

The prototype is a clarification artifact, not the authoritative requirement source and not automatically production-ready UI/code.

## Evidence retained

### 1. Chinese practitioner/training workflow — actually read

**MSUP — AI Native 项目实战训练营**  
https://www.msup.com.cn/course/19270

Evidence role: **Chinese practitioner/training workflow evidence**.

Material observations:

- teaches Claude Code directly from a PRD to a clickable HTML prototype and browser visual confirmation;
- then structures executable specification as domain terms → preconditions → main flow → exception handling → acceptance criteria;
- requires human confirmation of acceptance criteria;
- teaches small-step verification, Git control and HITL rather than one-shot generation;
- treats the prototype as a review/development basis, with screenshots/design-system constraints carried into later specification.

Why it matters:

> A general code Agent already has a plausible low-friction path from requirement material to an interactive review artifact. The decision-changing discipline is structured rules + verification, not a mandatory specialist prototype product.

Limitation:

- this is a commercial training provider/course outline, not an independent controlled outcome study;
- its examples are software-product oriented, so ERP business semantics still have to come from the user's own project sources.

### 2. Independent practitioner counter-evidence — actually read

**r/UXDesign — “Prototyping in the good ‘old’ Figma way”**  
https://www.reddit.com/r/UXDesign/comments/1o0ra0o/

Evidence role: **community workflow / failure evidence**.

Retained signal:

- practitioners report AI prototyping can be useful for stakeholder demos, usability testing and interactions that are expensive to fake manually;
- the same discussion reports that complex behavior, edge cases and production-quality refinement can become slower than manual work.

Limitation: community anecdotes, not controlled evidence.

**r/UXDesign — “Prototyping in Figma is dead. The future is AI prototyping.”**  
https://www.reddit.com/r/UXDesign/comments/1ncq0ka/

Evidence role: **counter-evidence against one-shot / tool-first adoption**.

Retained signal: a highly upvoted practitioner report describes spending more time correcting an AI-generated complex seat-selection prototype than rebuilding it manually in Figma.

Limitation: one self-reported case.

**r/FigmaDesign — existing 18-screen design → Figma Make**  
https://www.reddit.com/r/FigmaDesign/comments/1mq0cqj/

Evidence role: **existing-design drift / correction-cost evidence**.

Retained signal: the author reports about five hours removing invented elements and fixing UX deviations before abandoning the attempt.

Limitation:

- the report is from 2025;
- Figma added Make kits, attachments and stronger editing/context controls in 2026, so it is evidence of a failure mode, not a claim that current Figma Make always behaves this way.

### 3. Figma Make — current product facts, actually read

**Figma Help — Explore Figma Make**  
https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make

Evidence role: **current capability / adoption-fact anchor**.

Verified current facts:

- prompt-to-app for functional prototypes, web apps and interactive UI;
- can attach existing Figma designs/components and other context;
- iterative prompting, point/edit, annotations and generated-code editing;
- team collaboration and shareable previews;
- Full seats on paid plans have full access; other seats/plans can try it.

**Figma — Build with more context and more control in Figma Make**  
https://www.figma.com/blog/introducing-make-kits-and-make-attachments/

Evidence role: **current implementation evolution + vendor-stated failure boundary**.

Material observation: Figma explicitly frames the first-draft problem as wrong components/copy and missing edge cases, and introduced Make kits/attachments so real components, data, PDFs, markdown, CSV/JSON, screenshots and constraints can ground generation.

This supports using Figma Make when a team already has useful Figma/design-system context; it does not remove the need to check business rules.

### 4. Figma controlled productivity evidence — actually read

**Figma — Measuring time savings from Figma Make**  
https://www.figma.com/blog/measuring-time-savings-from-figma-make/

Evidence role: **vendor-run randomized controlled study**.

The study reports 100 participants (50 PMs, 50 product designers). Across its three standardized design tasks, PMs using Make were cumulatively 23% faster, but PMs did **not** show a statistically significant time improvement on the most challenging / extensive task.

Practical implication:

> Figma Make has credible productivity value for bounded PM design contributions, but the evidence itself argues against assuming the gain scales automatically to complex ERP interaction logic.

Limitations:

- Figma designed and published the study;
- tasks were standardized social-media UI tasks, not ERP requirements with roles, validation and exception chains;
- it measured time/ease, not business-rule correctness.

### 5. Lovable — current facts, actually read

**Lovable Docs — Connect your project to GitHub**  
https://docs.lovable.dev/integrations/github

Evidence role: **current implementation / portability fact anchor**.

Verified current facts:

- generated projects can be connected to GitHub;
- default-branch edits sync both ways;
- developers can work locally and deploy elsewhere;
- Lovable cannot import an arbitrary existing GitHub repository as the starting project.

**Lovable Docs — Manage training data and privacy**  
https://docs.lovable.dev/features/business/data-opt-out

Evidence role: **enterprise-adoption constraint**.

Current documentation says customer data may be used for model training/business purposes unless the customer opts out; the opt-out mechanism differs by plan. Therefore restricted ERP project material must not be uploaded by default without checking organization policy and workspace settings.

### 6. Relevant Skills — original implementations actually read

**SpaceZephyr/pm-skills @ tree `4c486c7a532de8890e88036533e0a48d578087ed`**  
https://github.com/SpaceZephyr/pm-skills

Evidence role: **PM Skill ecosystem / implementation inspection**.

The repository is useful, but its prototype Skills do not directly solve the core P03 mapping:

- `pm-image2proto`: screenshot/mockup → faithful single-file HTML prototype;
- `pm-url2proto`: existing URL → local project.

`pm-image2proto` adds useful design-system memory, iterative screenshot reproduction and interaction checks, but it assumes an image/UI reference. It is therefore a **conditional companion** when a consultant already has prior-system screenshots or a UI style to reuse, not the default requirements/rules → prototype method.

**alima-max/prototype-to-figma-skill @ `6e2e1befaa6f6df34a046956127b1d4f54bcb158`**  
https://github.com/alima-max/prototype-to-figma-skill

Evidence role: **downstream review/handoff implementation**.

It converts an already-working code prototype into a structured Figma file with separate interaction states, design-system component mapping, annotations and flow arrows. This can improve asynchronous review after a code prototype exists, but it requires Figma MCP/tooling and is downstream of P03's main generation problem. Do not make it a prerequisite.

## Recommended colleague workflow

### Default — ordinary code-capable Agent is enough

Use this when the goal is requirement clarification / solution review and the team does not already depend on a Figma design system.

1. Feed the real requirement sources to the Agent; do not rely on model memory for ERP rules.
2. Produce a **prototype contract** before UI generation:
   - roles / permissions;
   - entities and key fields;
   - validation rules;
   - states and transitions;
   - one or two primary flows;
   - important exception paths;
   - unresolved questions.
3. Limit v1 to the minimum reviewable slice. Do not generate the whole system.
4. Generate a local single-file HTML or small React prototype with representative fake data.
5. Click through every retained normal and exception path and reconcile the behavior back to the prototype contract.
6. Record open decisions beside the prototype. Correct the contract first when the business rule changes, then update the UI.
7. Treat the result as a review artifact; do not silently promote generated UI/code into approved specification or production implementation.

### Upgrade to Figma Make when

- the team already works in Figma;
- existing Figma components/design libraries are important inputs;
- PM/design/engineering need shared review in the same environment;
- a shareable interactive preview and visual iteration are worth the paid/cloud workflow;
- enterprise data policy permits the material.

Use attachments/design-system context and plan/review steps; do not rely on a single text prompt.

### Consider Lovable when

- the prototype needs more app-like hosted behavior, backend/state or easy external sharing;
- code export/GitHub ownership is useful;
- the project is safe for the cloud workspace and its data/training controls have been checked.

It is not the default for restricted ERP project material.

### Add a specialized Skill only for a concrete missing capability

Examples:

- prior UI screenshot must be reproduced consistently → `pm-image2proto` may help;
- working code prototype must become a structured Figma review artifact → `prototype-to-figma-skill` may help.

Do not install either merely because the task contains the word “prototype”.

## Adversarial checks

### Rejected: “AI prototype tool = better prototype”

The evidence does not support this. The dominant failure mode is correction cost when behavior, design context or edge cases are underspecified.

### Rejected: “Figma Make should always be the default”

Current Figma capability is strong, but its own RCT shows the PM productivity gain is not statistically significant on the hardest tested task. ERP role/state/exception logic is not simpler than that by assumption.

### Rejected: “plain Agent is enough, so no controls are needed”

The practitioner evidence says the opposite: executable structure, small steps, acceptance criteria and human verification are the reason a code-first path is trustworthy enough to recommend.

### Rejected: “existing prototype Skills prove specialized Skill advantage”

The inspected PM Skills solve adjacent transformations (image→prototype, URL→prototype), not P03's source problem. The downstream Figma Skill solves review packaging after a working prototype exists.

## Coverage gaps

- Bilibili discovery surfaced relevant AI-prototyping/product-manager material, but direct full-page access was intermittent; titles/snippets were not used to support material claims.
- no independent ERP-specific controlled benchmark comparing code Agent vs Figma Make vs Lovable was found;
- no evidence proves the generated prototype itself is business-correct without human review.

These gaps are explicit but not decision-blocking because the adoption boundary is already stable.

## Runtime decision

> **No local/runtime A/B required for P03 now.**

A synthetic bake-off would mainly compare models/prompts on an invented UI and would not resolve the key adoption decision. Current evidence already establishes:

- code-capable Agents can produce interactive HTML from structured requirements;
- specialist platforms add real collaboration/design-system/hosting advantages;
- complexity and underspecified edge cases create correction cost;
- human rule/exception verification remains necessary.

A future runtime test is justified only if a real colleague supplies project artifacts and the choice between two concrete workflows remains unresolved.

## Stop decision

P03 is closed because the recommendation is decision-complete:

- real task and output boundary: covered;
- Chinese practical workflow: covered;
- independent success/failure signals: covered;
- current Figma/Lovable facts: covered;
- serious Skill implementations: inspected;
- correction and edge-case risk: explicit;
- enterprise-data boundary: explicit;
- reason not to run synthetic runtime testing: explicit.

Further search may add more tools or tutorials, but is unlikely to change what an ERP colleague should do first.

## Next project action

Execute one engineering-type heterogeneous card, preferably **P07 codebase understanding** or **P10 requirements → tests**, with the same acquisition/citation discipline. Only after that should the project reassess readiness for a minimal real-user pilot.
