# Current Evidence Status

Date: 2026-08-29

## 1. What we know with relatively high confidence

### Product problem exists

ERP project staff do face high-noise resource discovery problems around Agent Skills, AI tools, current configuration guides, practical tutorials and learning methods.

Phase 1 research and the exploratory batches show that useful resources are fragmented across official docs, GitHub, community projects and tutorials, and that recency/task-fit judgement matters.

### The decision layer matters more than raw search

Observed failures repeatedly came from:

- recommending something merely related rather than matching the full task;
- treating official material as automatically user-facing;
- using adjacent tools to fill an empty recommendation slot;
- missing linked/bundled material and incorrectly claiming a resource lacked a capability;
- using outdated configuration facts.

So the useful core is not search recall. It is task understanding + comparison + abstention + targeted verification.

### Heavy governance is the wrong default

V0.2–V0.4 showed that universal gates, scoring, candidate JSON and validators can be gamed while producing poor recommendations.

## 2. What is only partially supported

### 0–2 recommendations

This is a strong default for ordinary use, but not a permanent hard rule. Broad research requests may legitimately need a larger candidate set after Top Picks.

### Runtime search first

It is reasonable before a database is justified. But repeated real use may later show that retaining validated resources meaningfully reduces search cost; if so, a lightweight curated memory/index may become useful.

### The current role scope

Implementation/consulting use cases are better represented than PM and developer use cases. We do not yet have enough independent evidence to claim equal value across all three roles.

## 3. What is NOT proven

- The proposed Skill itself adds value over a good ordinary prompt.
- The product has been validated by enough independent real users.
- Batch 01's 7 strong / 3 abstain result predicts real adoption.
- `>=8/10` is the correct product threshold.
- A persistent resource database is needed.
- Automation/refresh is needed.

## 4. Evidence classification of current assets

| Asset | Evidence type | Status |
|---|---|---|
| Phase 1 — 21 Skill study | design research | keep |
| Phase 2 — product vision | product hypothesis | keep, now bounded by North Star |
| Phase 3 — minimal architecture | implementation hypothesis | keep, do not execute yet |
| V0.4 / historical gates | failure evidence | archive only |
| PR #4 Phase 4 pilot | execution + failure evidence | closed, do not merge |
| PR #6 Batch 01 | exploratory discovery | useful, not validation |
| Real-user task results | product validation | insufficient today |

## 5. Current project state

**Status: product discovery / evidence gathering. Not Skill implementation.**

The next useful evidence is not another synthetic Eval round. It is real task intake from the target population, processed with Protocol V2.

Until that arrives, cloud work should focus on:

1. preserving and verifying the strongest discovered resources as a starter pack;
2. preparing role-balanced task intake and review cards;
3. improving only repeated failure patterns, not individual test-case quirks;
4. keeping all implementation choices reversible and lightweight.

## 6. Anti-drift stop conditions

Stop and reassess if any of these occurs:

- more time is spent maintaining Eval mechanics than reviewing real resources;
- new rules are added because of a single example;
- synthetic tasks outnumber real-origin tasks but are used to claim success;
- the project starts building a database before repeated search cost is demonstrated;
- the Curator begins directly performing every ERP task and loses its resource-decision boundary;
- local Agent execution becomes a dependency for product decisions.
