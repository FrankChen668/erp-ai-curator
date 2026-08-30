# P04A Curation Result 01 — Editable Process Diagram

Date: 2026-08-30

## 1. Classification

**PROMISING DISCOVERY / RUNTIME UNPROVEN**

P04A found a strong candidate, but the curation run did not prove that an ERP consultant can install it, generate a non-trivial business process diagram, open the artifact, edit it, and correct it with acceptable effort.

Do not convert this result into `Tomorrow usefulness = Yes` or `validated practical workflow` yet.

## 2. Strong candidate retained

Main candidate:

- `jgraph/drawio-mcp` — official draw.io Codex plugin / drawio Skill
- cloud review pin: `14b318b19cc37b159f841227b9d11fbd18ce18ea`
- source: https://github.com/jgraph/drawio-mcp/tree/main/plugins/codex/drawio

Original evidence supports:

- native `.drawio` output;
- Mermaid → `.drawio` conversion when draw.io Desktop is available;
- direct draw.io XML authoring;
- optional ELK layout;
- PNG/SVG/PDF export with embedded XML;
- browser URL mode;
- Codex plugin installation path.

This is materially stronger than image-only diagram generation for P04.

## 3. What P04A did not prove

### 3.1 Runtime usability

The P04A protocol explicitly prohibited candidate installation.

Therefore the local run did **not** prove:

- Codex plugin installation works in the actual Windows/local environment;
- a representative swimlane/process diagram is generated successfully;
- `.drawio` opens without XML/import problems;
- edit → regenerate / correct workflow is smooth;
- layout remains reviewable on a non-trivial ERP process;
- actual correction cost is lower than manual drawing.

This is a protocol boundary, not a local-agent execution failure.

### 3.2 Semantic fidelity

The official draw.io Skill strongly proves **diagram artifact generation**.

It does not itself prove that AI will correctly infer ERP business semantics from incomplete prose.

The local run's anti-hallucination instructions — e.g. `不得新增步骤`, `待确认`, explicit gateway conditions, exception closure — are useful, but they are **Curator synthesis**, not a proven capability of the official Skill.

Therefore keep separate:

> file/editability capability

from

> business-process semantic correctness.

### 3.3 draw.io XML is not BPMN semantic validation

A `.drawio` diagram can visually represent BPMN-like pools, lanes, gateways and flows.

That does **not** mean the result is BPMN 2.0 semantic XML, executable BPMN, or BPMN-conformance-validated.

For customer workshop / blueprint review this may be sufficient, but the distinction must be explicit.

## 4. Discovery bias found

The local run was executed inside Codex and selected a Codex-native solution.

That is a plausible winner, but P04A did not seriously compare one low-code/no-install collaborative path before concluding `Optional second solution: none`.

Cloud counter-check found current official alternatives with a materially different adoption boundary:

- draw.io online Generate: prompt → standard mxGraph XML → editable draw.io diagram;
- Miro AI diagrams: text → editable board diagram, with collaborative review/editing;
- Lucidchart AI flowchart: text/file → editable flowchart canvas.

References:

- https://www.drawio.com/docs/manual/generate/
- https://www.drawio.com/docs/manual/generate/ai-models/
- https://help.miro.com/hc/en-us/articles/28782102127890-Miro-AI-with-Diagrams-and-mindmaps
- https://lucid.co/diagram/flowchart/ai-flowchart-generator

This does not mean those alternatives win. It means `no materially different second boundary exists` was not sufficiently established.

For generalized ERP consultants, a browser/collaboration workflow may have lower adoption cost than installing a Codex plugin.

## 5. Practical-companion weakness

`Agents365-ai/drawio-skill` is a useful second Skill candidate and contains concrete structural/visual checking guidance.

But it is still another tool/Skill instruction source.

P04A did **not** find a strong independent practitioner tutorial/case showing a real business description → generated editable swimlane diagram → human correction workflow.

Therefore practical-evidence coverage remains incomplete.

## 6. Enterprise adoption caveat

The official Codex plugin README says the Skill fetches shared XML/Mermaid references from GitHub at runtime.

The recommended marketplace installation also follows the repository integration rather than a project-owned immutable dependency by default.

For enterprise use this creates:

- network dependency;
- reproducibility/version-drift risk;
- need for pinned-source qualification if adopted as a standard team Skill.

This is not a reason to reject the candidate, but it must be included in adoption judgement.

## 7. Correct current status

Retain:

> **jgraph/drawio-mcp Codex Skill — KEEP FOR PINNED RUNTIME PILOT**

Do not yet label:

- proven ERP workflow;
- lowest-friction solution for all consultants;
- semantic process validator;
- independent best practice.

## 8. Next action

Do not move immediately to another Problem Card.

Run **P04B pinned runtime pilot** first.

The goal is to test the strong candidate on a representative ERP process artifact and measure:

- installability;
- `.drawio` validity/editability;
- swimlane/branch/exception/handoff representation;
- correction workflow;
- rework burden;
- dependency/network behavior.

Authority:

- `docs/validation/DELIVERY_P04B_DRAWIO_RUNTIME_PILOT.md`
