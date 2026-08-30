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

- Bilibili public Web search can surface practical tutorials, descriptions and engagement metadata for WorkBuddy, Codex, draw.io Skills and AI PM workflows;
- direct Bilibili page opening/transcript acquisition can still intermittently hit 412/anti-bot, so discovery availability and full-content availability must be distinguished;
- one failed Bilibili URL path is not enough to conclude that practitioner evidence is unavailable;
- WeChat Search → Reader remains a qualified path for original public-article evidence;
- Xiaohongshu remains an acquisition/indexing coverage gap; do not infer content scarcity from access difficulty.

Therefore adapter failure/status must not be used as a proxy for platform value.

## 4. Existing upstream ecosystems discovered

Current evidence shows that ERP AI Curator can reuse existing ecosystems rather than rebuild them, including:

- Chinese AI Product Manager Skill libraries covering PRD, PRD review, UI/prototype, Draw.io and solution challenge;
- broader PM Agent Skill libraries with dozens of reusable workflows;
- WorkBuddy community practical bluebooks organized around real tasks;
- Bilibili creator series covering Draw.io Skills, Codex, PM Skills and WorkBuddy practical operation;
- practitioner articles describing end-to-end AI PM workflows.

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

New retained practitioner evidence:

- `冰冰酱 — 从一张白纸到交付PRD：我的全自动 AI 产品工作流`
  - role: independent practitioner workflow/judgement evidence;
  - material evidence: real product context, multi-round correction, rework after semantic/model errors, Draw.io in the actual toolchain, explicit remaining layout defects;
  - value: establishes the correct quality boundary — clarify semantics first, then generate/review/iterate.

- `健彬的产品Live / 北沐而川 — 3分钟绘制流程图！这个AI+绘图工具的神仙组合`
  - role: independent practitioner-style operational guide;
  - material evidence: CRM/product text → AI-generated XML → Draw.io import → manual adjustment → editable artifact;
  - caveat: shallow demo; “3 minutes”/“standard” claims are not treated as validated outcomes; DeepSeek UI/setup details are version-coupled.

Bilibili delta:

- `AI辅导员小宇` Cursor + draw.io walkthrough is useful but does not materially improve the selected package;
- `产品老兵杰哥` exposes several highly relevant PM/ERP-adjacent Draw.io Skill videos through public search, but full original content remains intermittently inaccessible; record as a coverage gap rather than absence evidence.

Adversarial rejection:

- a detailed 2026 CSDN `DeepSeek + Draw.io` article was not retained because unsupported quantitative claims, inconsistent setup statements and incomplete runnable code reduce evidence reliability.

Why P04 can close:

- real business/product input: covered;
- actual workflow: covered;
- editable output: covered;
- correction/rework and failure boundary: covered;
- low-cost first trial: covered;
- deeper enterprise process mapping method: covered;
- current implementation/fact anchor: covered;
- remaining platform acquisition gap: explicit;
- additional search is unlikely to change what a colleague should learn/use first.

## 8. Runtime-testing policy

Do not use a technical test ladder as a mandatory pipeline for every resource.

Local runtime test is justified only when:

- credible practical evidence is absent/contradictory after reasonable practitioner discovery;
- install/permission/privacy risk matters and static review cannot resolve it;
- exact local reproducibility is essential to training;
- the candidate may become a repeated internal standard.

Otherwise curation should stop earlier.

## 9. Main remaining uncertainties

- can practitioner-first discovery consistently find share-worthy material across other real Problem Cards without stopping early;
- which practitioner sources/creators consistently produce the best resources for ERP delivery jobs;
- whether curated packages are genuinely useful to colleagues on real material;
- which existing PM/Agent/WorkBuddy resource ecosystems deserve recurring feeder status;
- whether platform-specific acquisition gaps materially harm recall;
- whether a minimal production Curator Skill is eventually worth packaging.

## 10. Main risk now

The dominant risk is not insufficient technical validation.

It is:

> **premature search stopping or source-role confusion causing the Curator to return a technically strong candidate before it has found enough practical evidence to support the user's adoption decision.**

P04 now demonstrates the desired stopping behavior: do a targeted evidence delta, reject dense-but-unreliable material, make the remaining coverage gap explicit, and stop once the recommendation is stable.
