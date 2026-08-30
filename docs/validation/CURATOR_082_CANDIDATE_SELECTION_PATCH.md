# Curator 0.8.2 — Candidate Selection Patch

Date: 2026-08-30
Status: **PATCH IMPLEMENTED — CONTROLLED USE CONTINUES**

## 1. Trigger

A fresh 0.8.1 result for:

> “使用这个 skill 给我找下做流程图的最佳实践”

no longer collapsed into official-only sources. It found practitioner material, but selected:

- a Japanese Qiita article as the main resource;
- an `html-svg-diagrams` Skill as a companion capability;
- an installation command although the user had not asked to add a Tool/Skill.

The answer's own preferred workflow emphasized editable draw.io XML, while the recommended Skill emphasized SVG output.

## 2. First-principles diagnosis

The Curator's job is not to find the most globally polished resource. It is to reduce the user's selection cost under the user's actual context.

A serious candidate therefore needs to fit at least the dimensions that materially change adoption:

```text
user/role/ecosystem
+ real task
+ required artifact
+ current toolchain / constraints
```

The 0.8.1 run improved discovery but still lost three dimensions at selection time.

### D1 — Audience/ecosystem fit

The project and user context are Chinese ERP / ToB / product-manager oriented. A foreign-language resource may still be best, but it should lead because it is materially stronger or because local evidence is weak—not merely because it was found first or looks authoritative.

### D2 — Artifact fit

Editable draw.io and SVG are not equivalent deliverables. Adjacent formats can be useful, but the Curator must not silently treat them as interchangeable.

### D3 — Adoption restraint

An explicit best-practice/tutorial request does not itself imply a need for a new installable Skill. A new capability should only appear when it directly solves a concrete gap in the user's current workflow.

## 3. 0.8.2 runtime changes

### Change A — audience/ecosystem fit

When the user's language, region or professional ecosystem is clear:

- prefer practitioner evidence from that ecosystem when quality is comparable;
- allow cross-language resources to lead when they are materially stronger or local coverage is genuinely weak;
- do not infer that foreign-language novelty equals superiority.

### Change B — artifact fit

A candidate must actually support the required deliverable. Examples:

- editable draw.io ≠ SVG-only;
- PPTX ≠ image-only slides;
- Word/Markdown editable source ≠ PDF-only output;
- BPMN model ≠ generic flowchart image.

If a bridge exists, verify and explain it.

### Change C — no incidental install

A best-practice/tutorial request alone does not justify a Tool/Skill recommendation. Only introduce an installable capability when it is integral to the selected practice and directly solves a concrete gap.

## 4. Adversarial review

### Attack A — Does this become “Chinese sources only”?

No. Cross-language resources remain valid and can be primary when they are materially stronger or local coverage is weak.

### Attack B — Does this create a scoring framework?

No. No score, weight, ranking table or Gate is introduced. The Skill receives one natural-language priority: audience/work-context fit and artifact fit outrank generic polish/popularity.

### Attack C — Does this ban SVG resources for draw.io work?

No. SVG may be useful, but it cannot be presented as equivalent to editable draw.io unless the workflow genuinely preserves editability or provides a credible bridge.

### Attack D — Does this remove useful Tool/Skill recommendations?

No. It only removes incidental installation. If a concrete capability gap exists, the Curator can still recommend the smallest suitable Tool/Skill.

### Attack E — Are we patching host-specific issues again?

No. Codex source policy, Graph Engineering collision and Browser fallback remain outside the Curator Skill until separate evidence establishes a necessary host-level correction.

## 5. Acceptance boundary

0.8.2 is acceptable for controlled use if:

- Project Contract passes;
- runtime references remain only `practitioner-discovery.md` and `evidence-and-safety.md`;
- no A/B/C, Gate, scoring, platform quota or new source-adapter framework is introduced;
- Current docs identify 0.8.2 consistently;
- the patch is represented as candidate-selection correction, not product-value validation.

## 6. Next evidence

Continue natural controlled use. On similar practice/resource requests, inspect whether:

- selected practitioner resources match the user's language/professional ecosystem when comparable local evidence exists;
- any cross-language recommendation has a real reason to outrank local candidates;
- resource/tool output matches the user's required artifact;
- installable capabilities appear only for demonstrated gaps.

Do not create a fixed benchmark or platform quota to force these outcomes.
