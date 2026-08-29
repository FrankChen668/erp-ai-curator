# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Use this document to decide what happens next, who does it, and when to stop. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Current product direction

ERP AI Curator is not a resource database and not a general-purpose plugin manager.

Its job is:

> **Given a real ERP / enterprise-information-system work problem, help the user choose the most useful AI working approach; when external resources are actually needed, find and curate a small number of resources worth learning, trying or sharing.**

The current product shape is a **bounded Curator / Orchestrator Skill hypothesis**:

```text
real work problem
→ understand outcome + constraints
→ AI leverage diagnosis
→ Mode A / B / C
→ if external discovery is needed:
     normal Web + GitHub
     + optional approved source adapters when coverage is weak
→ compare evidence
→ return a small actionable recommendation package
```

Source adapters are replaceable acquisition capabilities. They do not own ERP judgement or final recommendations.

## 2. What has been learned so far

### Product-model findings

- Resource-first Phase 2/3 was too narrow.
- Heavy Gate / scoring / candidate JSON governance can be internally consistent while still making poor product decisions.
- Current-stack sufficiency must be tested before recommending another Tool / Skill.
- Official sources are valuable factual anchors but should not automatically occupy recommendation slots.

### Resource-curation findings from T01/T02

- Selection quality improved when official facts and practitioner evidence were separated.
- T01 showed a real **discovery recall risk**: the first pass could favor mature SaaS/official results and miss relevant GitHub/local-Agent methods.
- T02 showed a separate **fit vs maturity risk**: a method can fit ERP work very well while still being weakly proven as a maintained/mature dependency.
- Chinese practitioner evidence is underrepresented in the default search path, but `not found` must not be interpreted as `does not exist`.

### Source-adapter finding

A bounded composition model is worth testing:

```text
Curator judgement
→ identify missing evidence capability
→ invoke an already-installed approved read-only source adapter
→ acquire original content
→ return to Curator judgement
```

This architecture is **not proven yet**. The next local phase exists to falsify it.

## 3. Current architecture boundary

### Layer A — Curator judgement

Owns:

- task interpretation;
- current-stack comparison;
- evidence need;
- candidate comparison;
- task fit / practical value / trust / limitation judgement;
- final recommendation;
- stopping research.

### Layer B — normal discovery

Use Web / GitHub first when they already provide sufficient coverage.

Do not invoke every platform because an adapter exists.

### Layer C — optional source adapters

Use only when a concrete source-access gap matters to the recommendation.

Current pilot capabilities:

- WeChat article discovery;
- WeChat public article reading;
- Bilibili search/transcript;
- Xiaohongshu public-note search/read.

Runtime use is read-only. Installation/update is a separate maintenance action.

### Layer D — local runtime

Local Codex is responsible for facts that cannot be proven in cloud review:

- Windows compatibility;
- actual Skill/MCP installation;
- dependency/runtime behavior;
- credential/login boundaries;
- read-only smoke tests;
- real multi-Skill/MCP routing;
- same-task baseline/uplift execution.

## 4. Current phase map

### Phase 0 — V3 product reset

Status: **DONE**

Output:

- North Star;
- AI Leverage Model V3;
- V3 Skill blueprint;
- trigger boundary;
- adversarial review.

### Phase 1 — resource curation behaviour

Status: **DONE ENOUGH TO MOVE ON**

Evidence:

- T01 interactive prototype;
- T01 recall challenge;
- T02 requirements / Fit-Gap / Solution Design.

Do not keep re-searching these topics. Repeated searching would contaminate later tests without resolving the next unknown.

### Phase 2 — source-adapter qualification

Status: **NEXT / LOCAL**

Goal:

> Prove which candidate source adapters can be safely installed and can actually acquire original public evidence in the target Windows Codex environment.

Candidate pilot set:

- WeChat discovery: `zjp1997720/wechat-article-search`
- WeChat reader: `Githun1314/agent-wechat-reader`
- Bilibili: `XZXZZX-Ai/bilibili-mcp`
- Xiaohongshu: `xpzouying/xiaohongshu-mcp`

Required result per adapter:

`KEEP FOR PILOT / CONDITIONAL / REMOVE`

No production endorsement is implied.

### Phase 3 — orchestration/routing test

Status: **BLOCKED BY PHASE 2**

Goal:

> Verify that Codex can use Curator intent plus multiple installed Skills/MCPs in one task without turning the workflow into a platform checklist.

Must prove:

- correct adapter selected;
- unrelated adapters skipped;
- evidence returned to Curator judgement;
- read-only boundary preserved;
- adapter failure degrades gracefully.

### Phase 4 — curation uplift A/B test

Status: **BLOCKED BY PHASE 3**

Use a fresh real topic not already contaminated by T01/T02.

First recommended task:

> Help an ERP / enterprise-system practitioner quickly understand an unfamiliar ERP module or custom enterprise system: process, objects/data, configuration/logic, integrations, exceptions and how to verify understanding.

Run:

- A: normal discovery path;
- B: same task with qualified adapters available and conditional routing.

Compare only material user value:

- serious candidates gained;
- original content gained;
- recommendation changed/strengthened;
- learning/adoption cost reduced;
- research overhead added.

Do not judge by number of links or calls.

### Phase 5 — repeat on 2–3 fresh tasks

Status: **FUTURE**

Only if Phase 4 shows material uplift.

Use genuinely different work problems, for example:

- code/project architecture understanding;
- current model-routing / low-cost coding Agent configuration;
- another real survey/user problem when available.

Purpose: determine whether adapter value and Curator judgement generalize or were topic-specific.

### Phase 6 — packaging decision

Status: **FUTURE**

Only after repeated evidence.

Choose one:

1. **Build minimal Curator Skill** — if stable instructions materially improve ordinary Codex behaviour.
2. **Keep as working method/docs** — if a strong model already performs equally well without Skill packaging.
3. **Keep selective adapters only** — if source acquisition helps but Curator Skill packaging adds little.
4. **Drop adapter layer** — if acquisition overhead does not improve final recommendations.

Do not implement a production Skill merely because a blueprint exists.

## 5. Cloud vs local responsibilities

### Cloud / ChatGPT owns

- product direction and first-principles review;
- adversarial review;
- upstream candidate research;
- GitHub/static source review where possible;
- architecture/docs/authority synchronization;
- evidence interpretation;
- deciding KEEP / CONDITIONAL / REMOVE after local evidence;
- deciding whether repeated failures justify a rule/design change;
- GitHub PR/merge/cleanup.

Cloud should continue these autonomously without asking the Owner for routine approval.

### Local Codex owns

Only work requiring the local runtime or local environment:

- sync repo;
- inspect local installed Skills/MCP configuration;
- security/mechanical qualification of exact pinned dependencies;
- install/configure approved pilot candidates;
- run read-only smoke tests;
- handle local process/restart/tool registration;
- run routing tests and A/B executions;
- report artifacts and observed behaviour.

Local Codex does **not** own:

- redefining V3;
- adding Gates/scorecards;
- deciding product PASS;
- installing arbitrary new adapters outside the assigned candidate set;
- changing pins because `latest` looks newer;
- editing ERP AI Curator product rules during a pilot.

### Product Owner owns

Only decisions that cannot be delegated safely:

- unavoidable local authentication / QR scan;
- enterprise/account/privacy approval when needed;
- final human usefulness judgement such as “would I actually send/use this with colleagues?”;
- genuinely ambiguous business semantics.

Do not make the Owner manually inspect package code or relay routine cloud work.

## 6. Collaboration contract

Each local task should have one narrow objective and one stop point.

Flow:

```text
Cloud defines current task + pins + boundaries
→ Local Codex executes and reports observed evidence
→ Cloud independently reviews evidence
→ Cloud updates architecture/docs only if repeated evidence justifies it
→ next task
```

A local report is evidence, not a product decision.

If local Codex discovers an unexpected issue, it should report it. It should not invent a new architecture to fix it unless explicitly assigned.

## 7. Dependency lifecycle

For third-party source Skills/MCPs:

```text
qualification
→ controlled install at pinned commit/release
→ smoke test
→ pilot use
→ later explicit update review if needed
```

During normal curation:

- use only already-installed qualified adapters;
- do not install arbitrary dependencies mid-task;
- do not auto-update;
- do not enable write/social actions;
- fallback to normal Web/GitHub when possible;
- report coverage gaps honestly.

Details are authoritative in `SOURCE_ADAPTER_LIFECYCLE_V3.md`.

## 8. Immediate action sequence

### Cloud — completed in this calibration

- consolidate current direction into this execution plan;
- sync evidence status with T01/T02 and adapter findings;
- sync the source-adapter pilot with the separate WeChat discovery + reader chain;
- keep the production Skill unimplemented.

### Local — next command

Execute **Phase 2 source-adapter qualification only**.

Do not run the final curation task yet.

Stop after producing:

- qualification table;
- actual install status;
- read-only smoke result;
- multi-skill readiness notes;
- unavoidable human action, if any.

Then cloud reviews the result before Phase 3.

## 9. Definition of done for the next phase

Phase 2 is complete when we can answer, from actual local evidence:

1. Which adapters are safe enough for this pilot?
2. Which actually work on this Windows Codex environment?
3. Which can be constrained to research/read behaviour?
4. Which require login/manual action?
5. Which should be removed before any curation uplift test?

Until those answers exist, do not claim the meta-Skill/source-adapter architecture works.

## 10. Anti-drift checks

Stop and re-evaluate if any of these appear:

- building a resource database;
- adding platform quotas;
- building an adapter package manager;
- automatic adapter updates;
- installing every available social-media Skill;
- using search volume as quality evidence;
- letting a source adapter make final recommendations;
- turning every ERP problem into external-resource discovery;
- treating local test PASS as independent user validation.

The project advances only when the next action reduces a real uncertainty about user value or runtime feasibility.
