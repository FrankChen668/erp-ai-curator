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
- T02 showed a separate **fit vs maturity risk**: a method can fit ERP work very well while still be weakly proven as a maintained/mature dependency.
- Chinese practitioner evidence is underrepresented in the default search path, but `not found` must not be interpreted as `does not exist`.

### Source-adapter qualification findings

The first local Windows + Codex qualification run produced real provider-level decisions:

- WeChat discovery: **CONDITIONAL** — actual search worked and direct `mp.weixin.qq.com` URLs were resolved, but dependency/Sogou anti-bot/cookie-path caveats remain.
- WeChat public article reader: **KEEP FOR PILOT** — public exact-host article reading worked with meaningful body + metadata and the intended GET-only/no-cookie boundary.
- Bilibili provider `XZXZZX-Ai/bilibili-mcp`: **CONDITIONAL** — local build/stdio worked, but real search was blocked by `COOKIE_EXPIRED`; search→transcript is not proven.
- Xiaohongshu provider `xpzouying/xiaohongshu-mcp`: **REMOVE** — rejected before install because a practical research-only tool surface was not demonstrated and broad social write/account actions are registered.

The WeChat two-step chain is enough to proceed to a narrow orchestration test. We do **not** need every desired platform to qualify before testing the core routing hypothesis.

See `docs/validation/SOURCE_ADAPTER_QUALIFICATION_RESULT_01.md`.

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

Current provider state:

```text
wechat_discover_public_articles
  zjp1997720/wechat-article-search → CONDITIONAL

wechat_read_public_article
  Githun1314/agent-wechat-reader → KEEP FOR PILOT

bilibili_search_public_videos / bilibili_read_transcript
  XZXZZX-Ai/bilibili-mcp → CONDITIONAL (credential blocked)
  sandraschi/bilibili-mcp → cloud-review candidate, not approved yet

xiaohongshu_search_public_notes / xiaohongshu_read_public_note
  xpzouying/xiaohongshu-mcp → REMOVED
  replacement → none approved
```

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

Status: **FIRST RUN DONE**

Result:

- one usable two-step WeChat chain exists;
- one Bilibili provider is credential-blocked;
- the first Xiaohongshu provider was correctly rejected;
- provider qualification/pinning boundaries are functioning as intended.

Phase 2 does **not** need to reach full platform coverage before Phase 3.

Separate provider-replacement research can continue without blocking the core routing test.

### Phase 3A — focused orchestration/routing test

Status: **NEXT / LOCAL**

Goal:

> Verify that Codex can use Curator intent plus the two installed WeChat Skills in one task, moving discovery → original article read without manual copy/paste, while avoiding unrelated adapters and preserving the read-only boundary.

This phase intentionally uses only the qualified/conditional WeChat chain.

Must prove:

- Curator-style evidence need triggers WeChat discovery only when material;
- search result is handed to the original-article reader in the same task;
- search snippet is not mistaken for original evidence;
- unrelated adapters are skipped;
- evidence returns to Curator judgement;
- workflow stops when enough evidence exists;
- failure degrades honestly.

Result:

`Multi-skill routing: PASS / PARTIAL / FAIL`

### Phase 3B — Bilibili replacement qualification

Status: **CLOUD REVIEW ACTIVE / LOCAL LATER**

Current first provider remains CONDITIONAL because of the local credential failure.

Cloud has identified `sandraschi/bilibili-mcp` as a possible anonymous-tier alternative. It must complete static review before a pinned local qualification command is issued.

Do not ask the Owner to configure a Bilibili Cookie until the lower-friction alternative has been tested or rejected.

### Xiaohongshu provider track

Status: **COVERAGE GAP / RESEARCH ONLY**

The first provider is REMOVED.

Do not weaken read-only requirements to regain Xiaohongshu coverage.

A replacement should only be assigned when cloud review finds a provider whose acquisition value and permission/maintenance profile are acceptable. A read-oriented crawler using stealth/fingerprint evasion is currently research-only, not approved for local installation.

### Phase 4 — curation uplift A/B test

Status: **BLOCKED BY PHASE 3A**

Use a fresh real topic not already contaminated by T01/T02.

First recommended task:

> Help an ERP / enterprise-system practitioner quickly understand an unfamiliar ERP module or custom enterprise system: process, objects/data, configuration/logic, integrations, exceptions and how to verify understanding.

Run:

- A: normal discovery path;
- B: same task with qualified adapters available and conditional routing.

At first, B may use only the WeChat chain if that is the only qualified practitioner-source adapter. This is sufficient to measure whether the adapter adds material value.

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
→ Cloud updates architecture/docs only if evidence justifies it
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

### Cloud — current work

- record Phase 2 qualification evidence;
- advance the core route to Phase 3A using the WeChat chain;
- review lower-friction Bilibili provider candidates;
- keep Xiaohongshu as an explicit coverage gap rather than lowering permission standards.

### Local — next command

Execute **Phase 3A WeChat multi-Skill routing test only**.

Do not run T03/Phase 4 curation uplift yet.

Stop after producing:

- whether discovery → reader happened in one task;
- which tools/Skills were actually used;
- whether unrelated adapters were skipped;
- whether original article evidence was distinguished from search snippets;
- routing result `PASS / PARTIAL / FAIL`;
- any observed failure/fallback.

Then cloud reviews the result before Phase 4.

## 9. Definition of done for the next phase

Phase 3A is complete when we can answer, from actual local evidence:

1. Can Curator-style intent cause Codex to select WeChat discovery when it is useful?
2. Can Codex then pass a discovered original URL to the separate reader in the same task?
3. Does it avoid manually pretending that two unrelated runs are orchestration?
4. Does it avoid invoking Bilibili/Xiaohongshu just because they exist?
5. Does it preserve source provenance and distinguish snippet vs original content?
6. Does it stop after the evidence need is satisfied?

Until those answers exist, do not claim the bounded meta-Skill composition works.

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
