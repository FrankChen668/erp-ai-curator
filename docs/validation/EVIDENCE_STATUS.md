# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.

## 1. REAL_USER demand evidence

The 2026-08 survey provides current demand evidence from 83 target users.

Supported conclusions:

- implementation consultants and project managers are the main audience;
- many respondents already use AI frequently;
- the dominant need is practical project-delivery use rather than AI introduction;
- unstable output quality, lack of real project cases/methods and enterprise data constraints are recurring frictions;
- repeated free-text semantics support Problem Cards such as workshop → requirement package, requirements → prototype, business logic → editable process diagram, materials → PPT, Excel → reconciliation, codebase → logic/debug and requirements → test cases.

Authority:

- `SURVEY_DERIVED_PROBLEM_CARDS_01.md`

The survey is demand validation, not outcome validation.

## 2. Curation behavior supported so far

- original/current evidence before recommendation;
- official/original sources are fact anchors, not automatic winners;
- practical/community content matters when it adds a reproducible workflow/example/failure/adoption lesson;
- Curator synthesis must be separated from external resources;
- creator reputation/popularity affects discovery order only;
- task fit, maturity, runtime proof and adoption cost must be separated;
- installed adapters should not be called mechanically;
- execution-environment bias is real: a Codex-based researcher may over-prefer Codex-native solutions unless a materially different lower-friction path is considered.

## 3. Adapter lifecycle / routing

- WeChat discovery: `CONDITIONAL`;
- WeChat reader: `KEEP FOR PILOT`;
- Bilibili first provider: `CONDITIONAL / credential blocked`;
- Xiaohongshu first provider: `REMOVE`.

WeChat Search → Reader bounded multi-Skill routing: **PASS**.

This proves acquisition composition feasibility, not user-value uplift.

## 4. P01 result

Status: **KEEP FOR PRACTICAL PILOT**

Authority:

- `P01_CURATION_RESULT_01.md`

Main resource:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

P01 supports practical discovery behavior but does not yet prove reduced rework on real project material.

## 5. P04A result

Status: **PROMISING DISCOVERY / RUNTIME UNPROVEN**

Authority:

- `P04A_CURATION_RESULT_01.md`

Main retained candidate:

- official `jgraph/drawio-mcp` Codex draw.io Skill
- cloud review pin: `14b318b19cc37b159f841227b9d11fbd18ce18ea`

Supported by original documentation:

- native `.drawio` output;
- Mermaid → `.drawio` path;
- direct draw.io XML authoring;
- optional layout/export paths;
- continued editability.

Not yet supported by runtime evidence:

- install succeeds in current Windows/Codex environment;
- a representative ERP process diagram opens and edits correctly;
- controlled revision preserves unrelated semantics;
- actual rework is lower than manual drawing;
- offline/runtime-reference behavior is acceptable.

### P04A adversarial findings

- the protocol prohibited installation but still asked for `Tomorrow usefulness = Yes/Maybe/No`; therefore `Yes` could only be inferred, not proven;
- file-format/editability capability was partially conflated with business semantic fidelity;
- draw.io XML is not automatically BPMN 2.0 semantic XML;
- the anti-hallucination generation constraints in the local result are Curator synthesis;
- `Optional second solution: none` was not sufficiently established because materially different browser/collaborative paths currently exist;
- the official Skill fetches shared GitHub references at runtime, which matters for reproducibility/network policy;
- the practical companion was another Skill, not strong independent practitioner/case evidence.

Current candidate classification:

> **KEEP FOR PINNED RUNTIME PILOT**

## 6. Evidence ladder for executable resources

Do not collapse these levels:

```text
Discovery evidence
→ original docs inspected
→ static dependency/permission review
→ pinned local runtime proof
→ representative work artifact proof
→ real-user project outcome evidence
```

P04A reached the first two levels for the main candidate, not the later levels.

## 7. Evidence asset state

| Asset | Evidence type | Current status |
|---|---|---|
| Survey export 2026-08 | REAL_USER demand evidence | strong/current |
| Survey-derived Problem Cards 01 | normalized demand evidence | current |
| Creator Prior Strategy V3 | discovery design | current; uplift unproven |
| Source Adapter Qualification 01 | local runtime evidence | provider decisions proven |
| Source Adapter Routing Result 01 | local runtime evidence | WeChat bounded composition PASS |
| Curation Uplift A/B Test 01 | paired value test | no material uplift for mixed task |
| P01 Curation Result 01 | practical curation evidence | KEEP FOR PRACTICAL PILOT |
| P04A Curation Result 01 | executable candidate discovery | PROMISING / runtime unproven |
| Independent REAL_USER outcome/use results | primary solution validation | still insufficient |

## 8. Next validation

Next: **P04B — pinned official draw.io Codex Skill runtime pilot**.

Protocol:

- `DELIVERY_P04B_DRAWIO_RUNTIME_PILOT.md`

P04B does not search for more tools. It tests the exact strong candidate on one representative ERP process, one revision, runtime dependencies and cleanup.

Run P04B once, then stop for cloud review.

## 9. Main remaining uncertainties

- whether selected executable Skills/Tools actually survive pinned local runtime qualification;
- whether recommended resources reduce real-user rework on actual project materials;
- whether Curator consistently finds share-worthy resources across distinct artifact types;
- whether Creator Prior improves recall without popularity bias;
- whether Chinese practitioner evidence materially improves a real package;
- whether V3 should eventually become a production Skill.

## 10. Main risks

- documentation claims mistaken for runtime proof;
- editable output mistaken for business-semantic correctness;
- Codex-native solution bias because Codex is the research environment;
- personal frameworks polished into “best practice” without independent evidence;
- adapter/platform checklist drift;
- creator popularity echo chamber;
- Curator synthesis mistaken for discovered capability;
- local technical success mistaken for real-user outcome validation;
- building more validation machinery instead of accumulating useful resources.
