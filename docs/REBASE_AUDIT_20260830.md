# REBASE AUDIT — 2026-08-30

Purpose: establish a clean project baseline after context-length drift and unsupported sprint conclusions.

## Accepted evidence baseline

### Demand

Accepted:
- 83-response training survey as REAL_USER demand evidence;
- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md` as normalized demand map, with its stated caveat that free text may be platform-polished and is semantic rather than guaranteed verbatim evidence.

### P01

Accepted only as:
> high task fit / low independent validation

It remains suitable for practical pilot/learning, not proof of a general method.

### P04

Accepted:
> CLOSED — recommendation stable with explicit coverage gaps

Reason: retained result records concrete source URLs, evidence roles, limitations and coverage gaps.

Authority:
- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

### P06

Accepted:
> CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional

Reason: bounded runtime evidence, pinned candidate commit, hidden truth, isolated baseline/with-Skill runs and retained result artifacts exist.

Authorities:
- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`
- `docs/validation/evidence/p06/`

## Invalidated recent conclusions

### P03 sprint close

`docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` is **INVALIDATED AS PRODUCT EVIDENCE**.

Why:
- it contains named practitioner/source assertions without retained URLs/citations proving the material was actually acquired and read;
- current tool capability claims are written without traceable current-fact sources;
- the sprint was produced during a context-overload phase and closed without a trustworthy evidence audit.

The ideas inside may later be rediscovered and supported, but none of its verdicts should be treated as established.

### P07 sprint close

`docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` is **INVALIDATED AS PRODUCT EVIDENCE**.

Why:
- it contains broad claims about Claude Code, Codex, practitioner workflows and legacy-system practice without concrete retained source links/citations;
- there is no auditable acquisition trail sufficient to distinguish researched evidence from model synthesis;
- therefore its `CLOSED` verdict is unsupported.

### Validation-complete / REAL USER PILOT claim

The conclusion that P01/P04/P06/P03/P07 provided sufficient heterogeneous evidence to declare Curator-method validation complete is **withdrawn**.

Consequences:
- do not treat the project as having completed validation;
- do not treat P03/P07 as accepted cards;
- do not use the invalid sprint artifacts as evidence for product-stage decisions;
- REAL USER input remains important, but it is not a substitute for completing the currently planned trustworthy heterogeneous validation sequence.

### Minimal Curator V0.1 status

The simplified `skills/curating-erp-ai-resources/SKILL.md` may remain as an **experimental candidate implementation**, because much of its structure follows the valid North Star principles. However it is **not yet validated as Minimal Curator V0.1**.

Its P03/P07-specific "validated behavior" claims must not be retained as established facts.

## Correct current position

Last trustworthy controlled checkpoint:

> **P06 closed. P03 is the next controlled heterogeneous card.**

Execution order:

1. rerun P03 cloud curation from scratch, with concrete practitioner URLs/content evidence + implementation/current-fact verification + limitations;
2. only run local/runtime delta if a material adoption decision remains unresolved;
3. after P03, choose one engineering-type card such as P07 and execute it with the same evidence discipline;
4. only then reassess whether the Curator method is stable enough for a minimum user-facing pilot.

## Evidence acceptance rule going forward

A card cannot be marked `CLOSED` merely because the conclusion sounds plausible.

For external-research cards, the retained authority must make it possible to audit at least:
- what concrete source was used;
- whether it was actually read or only discovered;
- what evidence role it plays;
- what material claim it supports;
- what limitations/counter-evidence remain;
- why further search/test would not change the adoption decision.

A source-less synthesis can be useful reasoning, but it is not accepted product evidence.
