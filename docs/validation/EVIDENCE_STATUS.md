# Current Evidence Status

Date: 2026-08-30

> Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`.

## 1. Demand evidence

The 2026-08 survey remains the primary REAL_USER demand source.

Supported conclusions:

- implementation consultants and project managers are the main audience;
- many respondents already use AI;
- the main gap is practical delivery quality, not AI introduction;
- users repeatedly want real methods/cases for requirements, PRD, prototypes, diagrams, PPT, Excel/data, testing, project management and Agent usage;
- typical inputs are actual project artifacts rather than abstract prompts.

Authority:

- `SURVEY_DERIVED_PROBLEM_CARDS_01.md`

The survey validates demand, not solution outcome.

## 2. Current source-strategy position

Supported direction:

> **For practical delivery questions, practitioner guides/reviews/cases should normally be the first discovery lane; original Tool/Skill and official docs are supporting verification layers.**

This is practical-value-first, not independent-third-party-at-all-costs.

An author/maintainer/original repository can still be the best primary learning resource when it contains the strongest workflow, examples and failure guidance, but its evidence role must be labeled honestly.

Authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

## 3. Current web/platform evidence

Observed in current cloud research:

- ordinary public Web can surface useful Chinese and international practitioner material without treating any platform as a quota;
- direct Bilibili page/transcript acquisition can still intermittently hit anti-bot limits, so discovery and full-content access must be distinguished;
- WeChat Search → Reader remains a qualified path when a concrete article needs full text;
- Xiaohongshu remains an acquisition/indexing coverage gap; do not infer content scarcity from access difficulty.

Adapter failure/status must not be used as a proxy for platform value.

## 4. Existing upstream ecosystems discovered

Current evidence shows that ERP AI Curator can reuse existing ecosystems rather than rebuild them, including:

- Chinese AI Product Manager Skill libraries;
- broader PM Agent Skill libraries;
- WorkBuddy community practical bluebooks;
- practitioner creator series;
- task-specific GitHub Skills and workflow repositories.

These are feeder pools, not final recommendations by themselves.

## 5. P01

Status: **KEEP FOR PRACTICAL PILOT**

Main retained resource:

- `Convert Notes to Requirements Working Skill`

Classification:

> high task fit / low independent validation

Useful practical method; not an independently validated industry standard.

## 6. P04 technical/implementation evidence

Retained implementation anchors remain:

- `Castaldo-Solutions/process-builder` — strong enterprise-process method/implementation; author self-practice;
- official `jgraph/drawio-mcp` — implementation/current-fact anchor;
- Anttu draw.io MCP article — optional independent technical operation/troubleshooting companion.

The previously prepared `P04B` runtime pilot remains:

> **DEFERRED / escalation only**

Do not rerun technical/static/runtime work unless a later real adoption decision exposes a new material unresolved risk.

## 7. P04 practitioner delta — CLOSED

Status: **CLOSE P04 — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `P04_PRACTITIONER_CURATION_RESULT_02.md`

Retained practitioner evidence includes:

- `冰冰酱 — 从一张白纸到交付PRD：我的全自动 AI 产品工作流` — independent practitioner workflow/judgement evidence with real semantic correction and rework;
- `健彬的产品Live / 北沐而川 — 3分钟绘制流程图！这个AI+绘图工具的神仙组合` — independent practitioner-style operational guide for text → XML → Draw.io → manual adjustment.

Remaining Bilibili full-content gaps are explicit but no longer decision-blocking.

P04 demonstrated the desired stopping behavior: targeted delta, evidence-role discipline, explicit coverage gap, then stop once recommendation is stable.

## 8. P06 data reconciliation — ACTIVE

Status: **CLOUD CURATION DONE / ONE BOUNDED LOCAL RUNTIME DELTA JUSTIFIED**

Authority / task envelope:

- `DELIVERY_P06_DATA_RECONCILIATION.md`

Current cloud evidence:

- independent practitioner experience shows recurring multi-file reconciliation becomes unreliable when treated as free-form chat; stable procedure, deterministic execution, explicit validation and human-review routing materially improve repeatability;
- current spreadsheet-native AI can now inspect/update workbooks directly and is a legitimate low-friction option, so P06 must not assume dedicated Skills are always necessary;
- `alchaincyf/huashu-excel` is the strongest currently discovered packaged audit-oriented spreadsheet method, inspected at commit `9348581a87cc03ed8d0b30706631088e922c6027`;
- its strongest current evidence is author-created method + implementation + author-run pressure testing, not independent ERP field validation.

Current decision gap:

> **Does Huashu-Excel materially improve ERP-style multi-file reconciliation over a competent plain code-first local Agent enough to justify the adoption overhead?**

Only this runtime comparison is currently justified. Local broad Web discovery, benchmark-framework construction and global Skill installation are out of scope.

## 9. Runtime-testing policy

Do not use a technical test ladder as a mandatory pipeline for every resource.

Local runtime test is justified only when it can plausibly change an adoption decision, for example:

- credible practical evidence remains insufficient or contradictory;
- install/permission/privacy risk matters and static review cannot resolve it;
- exact reproducibility is essential;
- a candidate may become a repeated internal standard.

P06 meets this threshold narrowly because a new self-authored Skill is competing with an already-capable plain code-first workflow on a correctness-sensitive task.

## 10. Main remaining uncertainties

Immediate:

- P06: whether Huashu-Excel produces a material accuracy/auditability/rework advantage over plain code-first Agent execution on the same ERP-like reconciliation fixture.

Product-level:

- whether practitioner-first curation remains stable across additional heterogeneous Problem Cards;
- whether curated packages are genuinely useful to colleagues on real material;
- which feeder ecosystems deserve recurring discovery prior;
- whether a minimal production Curator Skill is eventually worth packaging.

## 11. Main risk now

The dominant risk is not insufficient technical validation.

It is:

> **doing extra research/tests that do not change the colleague's adoption decision, or recommending a specialized Skill when plain deterministic Agent work is already enough.**

P06 should therefore stop immediately once the bounded local comparison stabilizes that decision.
