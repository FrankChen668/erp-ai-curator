# Curation Uplift A/B Result 01

Date: 2026-08-29

## Verdict

**NO MATERIAL UPLIFT — for this exact mixed task.**

This verdict is narrow. It does not mean the WeChat adapter is useless in general.

## What actually happened

Run A and Run B used the same raw task, model/config and isolated sessions.

Run A used normal Web/GitHub only and recommended a package centered on:

- GitHub Copilot codebase exploration;
- source-grounded repository investigation;
- NotebookLM/Gemini Notebook for source-grounded document Q&A;
- PM4Py for event-log-based process verification.

Run B had the qualified WeChat adapter available but **did not invoke it**. It recommended a package centered on:

- Codebase Memory MCP;
- Microsoft Power Automate Process Mining tutorial;
- SAP Signavio Process Intelligence.

Therefore the recommendation differences between A and B are attributable to normal search/model variance, not to WeChat evidence.

## First-principles interpretation

The test question was:

> Does adapter-acquired practitioner evidence materially improve the final curation package?

The treatment did not occur in Run B. No WeChat evidence entered the recommendation.

Therefore this test provides **no positive evidence of adapter uplift** for this task.

The correct result is not `MATERIAL UPLIFT` and not `LIMITED UPLIFT`.

For the exact task, the observed result is `NO MATERIAL UPLIFT`.

## Important positive evidence

The absence of adapter use is itself useful evidence:

- the Curator did not mechanically call WeChat because it was installed;
- the platform-checklist failure mode did not appear;
- normal Web/GitHub was judged sufficient for the technical path selected by Run B.

This supports conditional routing discipline, not adapter user-value uplift.

## Test-design issue exposed

The raw task combined two materially different jobs:

1. understanding an unfamiliar **standard ERP module**;
2. understanding a **custom enterprise system / codebase**.

Both runs naturally concentrated on the second because repository/code/process evidence is easier to make falsifiable.

This creates a test-design blind spot: a strong answer for custom-system archaeology can mask weak curation for standard SAP/Oracle module learning.

Future validation should separate these jobs rather than ask one recommendation package to cover both.

## Curation-quality issues exposed

### 1. Synthesized-method drift

Run A's main recommendation combined an external resource (GitHub Copilot) with a newly synthesized `ERP 取证提示规范`.

That guidance may be useful, but ERP AI Curator's original curation principle is to find and curate external reusable resources rather than quietly manufacture a new method and present the bundle as one resource.

Future outputs must distinguish:

- external resource;
- Curator usage guidance / synthesis.

Do not present Curator-created guidance as if it were a discovered external resource.

### 2. Practitioner-evidence gap remains

Neither A nor B found a strong practitioner/community companion.

Run A used official GitHub/Google/PM4Py material.
Run B used GitHub/author-associated research/Microsoft/SAP material.

This is not a failure by itself, but it means the earlier question about practical Chinese ERP learning evidence remains unresolved for a **standard ERP module** task.

### 3. Pairwise baseline variance

The same task/config produced different main recommendations even without adapter contribution.

Therefore future adapter-value tests must not infer causality merely because Run B's final package differs from Run A.

Any claimed uplift must be traceable to evidence acquired through the adapter.

## Product implication

Current evidence supports:

- bounded WeChat Search → Reader composition works;
- Curator can abstain from using the adapter when normal sources appear sufficient;
- adapter value is task-dependent.

Current evidence does **not** support:

- permanent promotion of the WeChat adapter as generally value-adding;
- broader adapter expansion;
- production Curator Skill implementation.

## Next uncertainty

Run one diagnostic test on the part the mixed task failed to isolate:

> **How should a consultant use AI and external learning resources to rapidly understand an unfamiliar standard ERP module while verifying process, objects, configuration boundaries and exceptions against authoritative evidence?**

This follow-up is not a search for a positive adapter result. WeChat remains optional and must not be forced.

The purpose is to determine whether practitioner-source acquisition has incremental value when the task is genuinely about standard ERP learning rather than codebase archaeology.
