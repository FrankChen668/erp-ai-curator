# P01 Test Readiness Note

Date: 2026-08-30

## Decision

**READY TO TEST.**

The project has enough design certainty to stop adding validation frameworks and run the first survey-driven practical curation test.

This note is intentionally short. It does not introduce a new framework.

## What is frozen for the pilot

1. **Demand source** — the 83-response survey is the primary REAL_USER demand source. Free text is used as repeated semantic evidence, not assumed verbatim.
2. **Product unit** — use a concrete Problem Card: real situation + actual inputs + work action + expected deliverable + acceptance/constraints.
3. **Practicality standard** — a resource must help a practitioner act on real project material with lower rework; `can generate X` is not enough.
4. **Source strategy** — official/original evidence anchors facts; practitioner content should add real steps/examples/failures/adoption evidence.
5. **Creator prior** — high-signal creators affect discovery order only. Specific original content still decides recommendation quality.
6. **Adapter boundary** — only already-qualified source adapters may be used conditionally; no platform quota and no runtime installation.
7. **Output boundary** — external resources and Curator synthesis remain separate.
8. **Validation boundary** — local Agent gathers evidence and produces the package; cloud reviews product value. A local PASS is not outcome validation.

## Adversarial checks passed sufficiently for testing

- **Popularity trap:** creator metrics cannot determine recommendation.
- **Official-only trap:** practical evidence is deliberately sought when adoption/workflow matters.
- **Chinese-content halo:** Chinese content can reduce adoption cost but must still pass content/evidence checks.
- **Problem abstraction drift:** the pilot uses a specific survey-derived work unit rather than a broad `requirements analysis` label.
- **Adapter sprawl:** no new Bilibili/Xiaohongshu installation is required for P01.
- **Framework growth:** no scoring, taxonomy engine, influencer database, search quota or new Gate is needed before the pilot.

## First pilot

Run `P01 / J02 — Post-Workshop Requirements Package`.

After the result returns, do not automatically run P02/P03/etc. First ask:

> **Would an ERP/enterprise-system colleague actually open one of these resources tonight and be able to use it on tomorrow's real project material?**

If `Yes`, preserve the useful resources and learn from the discovery path.

If `No`, fix discovery/selection/output behavior before adding more project machinery.
