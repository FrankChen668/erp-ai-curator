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

## 2. Major source-strategy correction

New supported direction:

> **For practical delivery questions, third-party practitioner guides/reviews/cases should normally be the first discovery lane; original Tool/Skill and official docs are supporting verification layers.**

Reason:

- the user primarily needs “how people actually use it, what works, what fails”;
- official docs are stronger for current capability/setup/privacy/version facts;
- existing communities already contain substantial practical material and Skill libraries;
- rebuilding independent tests for every tool creates low-value duplication.

Authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

## 3. Current web/platform evidence

Observed in current cloud research:

- Bilibili public Web search can surface current practical tutorials, descriptions and engagement metadata for WorkBuddy, Codex, draw.io Skills and AI PM workflows;
- direct Bilibili page opening/transcript acquisition can still intermittently hit 412/anti-bot, so discovery availability and full-content availability must be distinguished;
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

## 6. P04A

Status: **STRONG IMPLEMENTATION CANDIDATE / PRACTITIONER EVIDENCE UNDER-SAMPLED**

Retained implementation:

- official `jgraph/drawio-mcp` draw.io Skill

P04A confirmed strong documentary evidence for native editable `.drawio` output, but the run underweighted third-party guides/reviews and over-weighted implementation docs.

The local result also could not prove runtime usability because candidate installation was prohibited.

The previously prepared `P04B` runtime pilot is now:

> **DEFERRED / escalation only**

It should run only if practitioner evidence + original implementation + current fact checks leave a material unresolved risk.

## 7. Runtime-testing policy

Do not use this ladder as a mandatory pipeline for every resource.

Local runtime test is justified only when:

- credible practical evidence is absent/contradictory;
- install/permission/privacy risk matters;
- exact local reproducibility is essential to training;
- the candidate may become a repeated internal standard.

Otherwise curation should stop earlier.

## 8. Main remaining uncertainties

- which practitioner sources/creators consistently produce the best resources for ERP delivery jobs;
- whether the curated package is genuinely useful to colleagues on real material;
- which existing PM/Agent/WorkBuddy resource ecosystems deserve recurring feeder status;
- whether platform-specific acquisition gaps materially harm recall;
- whether a minimal production Curator Skill is eventually worth packaging.

## 9. Main risk now

The dominant risk is no longer “insufficient validation”.

It is:

> **over-validation and framework-building causing the project to miss the actual value: finding and curating existing practical experience faster than colleagues can find it themselves.**
