# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator exists for **real ERP / enterprise-information-system delivery work**.

Its basic unit is:

```text
real project situation
+ actual input artifacts
+ concrete action
+ expected reviewable deliverable
+ time / privacy / environment constraints
→ decide how AI should help
→ discover external Skill / Tool / method / tutorial / case only when it adds material value
→ read original evidence
→ separate task fit, maturity, runtime proof and adoption cost
→ return a small practical package
```

Curator synthesis must be labelled as synthesis, not presented as external capability.

## 2. Demand source

The primary demand source is the 83-response training survey and its normalized Problem Cards.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

The survey supports a practical-delivery focus: users already use AI, but need repeatable ways to turn real Word/PDF/PPT/Excel/minutes/screenshots/code/logs into reviewable deliverables with less rework.

## 3. First-wave Problem Cards

- P01 — workshop/minutes → requirement package
- P02 — requirements → PRD / FS / functional design
- P03 — requirements/rules → clickable prototype
- P04 — business logic → editable process / architecture diagram
- P05 — source materials → customer-ready PPT
- P06 — Excel/CSV → clean / reconcile / validate
- P07 — codebase → logic / FS / debug
- P10 — requirement → test scenarios / cases

This is a provisional queue, not a permanent taxonomy.

## 4. Source / creator strategy

Authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

Rules:

- original/current evidence before recommendation;
- official/original is a fact anchor, not an automatic winner;
- practitioner content matters when it adds operating steps, prompts, templates, examples, failure modes or adoption lessons;
- Creator Prior changes discovery order only;
- popularity is a weak discovery signal;
- open discovery remains available so niche creators can win;
- task fit and source maturity are separate.

For a generalized ERP audience, also guard against **execution-environment bias**:

> Before concluding that a Codex/Agent-native solution is the only useful boundary, inspect at least one materially different lower-friction path when one plausibly exists (for example browser/SaaS collaborative workflow).

This is a comparison discipline, not a quota. The alternative may still lose.

## 5. Source-adapter state

```text
WeChat discovery → CONDITIONAL
WeChat reader → KEEP FOR PILOT
Bilibili first provider → CONDITIONAL / credential blocked
Bilibili alternative → deferred
Xiaohongshu first provider → REMOVED
Xiaohongshu replacement → none approved
```

Do not expand adapters merely for platform coverage.

## 6. Completed — P01

Status: **CURATION COMPLETE / KEEP FOR PRACTICAL PILOT**

Authority:

- `docs/validation/P01_CURATION_RESULT_01.md`

Main retained resource:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

P01 proved useful discovery behavior, not real-user outcome improvement.

## 7. Completed — P04A curation

Status: **PROMISING DISCOVERY / RUNTIME UNPROVEN**

Authority:

- `docs/validation/P04A_CURATION_RESULT_01.md`

Strong retained candidate:

- official `jgraph/drawio-mcp` Codex draw.io Skill
- cloud review pin: `14b318b19cc37b159f841227b9d11fbd18ce18ea`

Documentary evidence strongly supports native `.drawio` generation and editing paths.

But P04A intentionally prohibited installation, so it did **not** prove:

- local installation/runtime;
- non-trivial swimlane/branch/exception output quality;
- edit-and-correct workflow;
- lower rework than manual drawing;
- semantic fidelity on ERP process prose.

Therefore documentary curation alone must not be reported as `Tomorrow usefulness = Yes` for an executable candidate.

Use:

> **plausible / promising from source evidence**

until runtime evidence exists.

### P04A adversarial corrections

1. `.drawio` editability is not ERP semantic correctness.
2. draw.io XML with BPMN-like shapes is not automatically BPMN 2.0 semantic XML.
3. the anti-hallucination prompt in the local result is `Curator synthesis`.
4. `Optional second solution: none` was not established strongly enough; current browser/collaborative alternatives exist with materially different adoption boundaries.
5. the official Codex Skill fetches shared GitHub references at runtime, creating network/reproducibility considerations for enterprise adoption.
6. `Agents365-ai/drawio-skill` is a useful second Skill candidate but does not replace independent practitioner/case evidence.

## 8. Immediate next test — P04B pinned runtime pilot

Status: **NEXT / LOCAL**

Protocol:

- `docs/validation/DELIVERY_P04B_DRAWIO_RUNTIME_PILOT.md`

Unique purpose:

> Test whether the pinned official draw.io Codex Skill actually works in the current Windows/Codex environment on a representative ERP process, produces a valid editable `.drawio`, survives one controlled revision, and cleans up without disturbing unrelated Codex plugin state.

This is not a new search.

Do not search for more diagram tools during P04B.

Do not move to another Problem Card before cloud review of P04B.

## 9. Evidence ladder for executable resources

For executable Skills/Tools, keep these levels distinct:

```text
Discovery evidence
→ Original documentation inspected
→ Static dependency/permission review
→ Pinned local runtime proof
→ Representative work artifact proof
→ Real-user project outcome evidence
```

Do not jump from documentation directly to `validated practical workflow`.

For non-executable methods/tutorials, runtime installation is not required; use an equivalent artifact/application check instead.

## 10. Cloud / local / Owner split

### Cloud / ChatGPT

Owns product direction, adversarial review, survey interpretation, source/provider/creator research, maturity/evidence interpretation, GitHub maintenance and final KEEP/CONDITIONAL/REMOVE decisions.

### Local Codex

Owns fresh curation runs, observable source evidence and explicitly assigned local runtime/install tests. It does not redefine V3 or install arbitrary dependencies.

### Product Owner

Only unavoidable login/privacy/business-semantics decisions and final human usefulness judgement.

## 11. Anti-drift

Stop if work turns into:

- broad consulting labels detached from actual artifacts;
- AI/tool feature catalogs;
- mandatory platform coverage;
- influencer rankings;
- link-count scoring;
- Codex-native answers chosen merely because the test Agent is Codex;
- documentation claims treated as runtime proof;
- editable file format treated as semantic correctness;
- Curator synthesis presented as discovered capability;
- local success treated as real-user outcome validation;
- more framework without better practical evidence.

The project advances only when the next action helps a real ERP colleague solve a real delivery problem better.
