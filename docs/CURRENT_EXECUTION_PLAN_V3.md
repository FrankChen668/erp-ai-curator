# ERP AI Curator — Current Execution Plan V3

> Current execution authority. Keep this document short and current; historical detail belongs in validation records.

## 1. Product objective

ERP AI Curator helps SAP / Oracle / ERP / enterprise-information-system practitioners solve **real delivery problems** using existing AI practice and resources.

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work action/problem
+ expected deliverable
+ material constraints
→ practical resource curation
```

The product is **not** an AI tool directory, generic tutorial library, Prompt library, influencer ranking, or tool-certification lab.

Core user question:

> **我现在碰到这个具体工作问题，别人已经有哪些值得学习和采用的 AI Skill / Tool / 方法 / 教程 / 经验？**

## 2. Demand evidence and its boundary

Primary demand source:

- the 83-response 2026-08 training survey;
- normalized Problem Cards derived from it.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

Evidence discipline:

- closed-choice aggregates are direct survey evidence;
- free-text answers are useful mainly for repeated semantic patterns because the survey platform may have performed second-level summarization/polish;
- do not quote or interpret polished free text as guaranteed verbatim user language;
- the survey validates **REAL_USER demand**, not recommendation quality or user outcome.

Current recurring jobs include requirements, PRD/FS, prototypes, editable diagrams, PPT, Excel/data, code/debug, testing, project coordination, manuals/training and Agent/Skill adoption tied to real work.

## 3. Source principle — practitioner value first, not website type first

For adoption/learning questions, default evidence flow is:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ current official/original fact check where needed
→ limitations / counter-evidence
```

This means **practical usefulness is the first user-value question**.

It does **not** mean an independent third party must always occupy the first recommendation slot.

A tool author, maintainer, official team or original repository may be the best practical learning resource if it contains the strongest real workflow, examples, failures and artifacts. When that happens:

- it may be the primary recommendation;
- clearly label its evidence role and incentives;
- do not describe author/vendor self-practice as independent validation;
- use independent practitioner evidence as a confidence/counter-evidence layer when it materially improves the decision.

Official/current sources remain preferred for volatile facts such as version, install command, compatibility, price/license, privacy/data flow and native output format.

Authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

## 4. Discovery and platform discipline

Useful discovery pools include Bilibili, WeChat, Xiaohongshu, YouTube, PM/BA/consulting communities, blogs, GitHub Skill collections and existing Agent/PM resource ecosystems.

But this is **not a platform quota**.

Rules:

- one failed page/adapter does not prove a platform lacks useful content;
- ordinary public Web discovery comes before special adapters;
- WeChat Search → Reader may be used when a concrete high-value public article needs full text;
- Xiaohongshu access/index limitations are a Coverage Gap, not evidence of content scarcity;
- creator popularity/likes/saves/views/stars affect discovery order only;
- multiple derivative posts of the same demo are one evidence family, not independent corroboration;
- stop only when additional discovery is unlikely to change the user decision, not because one technically complete candidate was found.

## 5. Reuse existing ecosystems; Curator before Builder

Existing PM/BA Skill libraries, Agent tutorials, WorkBuddy guides/bluebooks, creator series and tool-specific practical collections are feeder ecosystems.

ERP AI Curator should:

```text
real ERP/enterprise Problem Card
→ search existing ecosystems
→ remove hype / stale / mismatch
→ connect practice to the actual Tool/Skill
→ verify only facts that matter
→ retain a small recommendation package
```

Do not rebuild a generic PM Skill library, WorkBuddy manual, Codex handbook or tutorial encyclopedia when strong upstream material already exists.

Curator-created methods are allowed only when a real gap remains and must be labeled `Curator synthesis`.

## 6. Safety and testing boundary

Repeated runtime testing is not the default.

For executable third-party Skill/MCP/plugin/script, do a lightweight static review before recommending installation when relevant:

- install/dependencies;
- credentials;
- filesystem/shell/browser/network/account access;
- mutating actions;
- obvious data egress;
- license/maintenance.

Runtime/artifact testing is justified only when a material decision cannot be resolved otherwise, for example:

- practical evidence is absent or contradictory after reasonable discovery;
- installation/permission/privacy risk remains material;
- exact local reproducibility is essential;
- a candidate may become a repeated internal standard and the cost of being wrong is high.

`runtime test not required` does not mean `executable safety can be ignored`.

## 7. Current retained evidence

### P01 — workshop/minutes → requirement package

Retained:

- `Convert Notes to Requirements Working Skill`

Current classification:

> **high task fit / low independent validation**

It is a useful working method, not an independently proven industry standard and not REAL_USER outcome validation.

### P04 — business description/requirements → editable process diagram

Current verdict:

> **USEFUL WITH GAPS / GOAL NOT YET COMPLETE**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_01.md`

Retained so far:

- `Castaldo-Solutions/process-builder` — strong task-fit method/implementation; author self-practice, not independent validation;
- official `jgraph/drawio-mcp` — implementation/current-fact anchor;
- Anttu draw.io MCP article — useful independent technical operation/troubleshooting companion, but not sufficient by itself as ERP/business-process practice evidence.

Observed failure:

> Discovery Recall stopped too early after a technically complete solution was found; later ordinary Web search surfaced additional relevant practitioner content.

Do not rerun the technical/static/runtime part of P04.

## 8. Immediate next action — narrow P04 practitioner delta

Purpose:

> **challenge or complete the current P04 package with better practitioner evidence, then close P04.**

Do a small, targeted practitioner search across the most promising available sources. Start with the already-observed Chinese/Bilibili recall gap, but do not treat Chinese sources, Bilibili, or any fixed source count as a requirement.

Prioritize content that adds at least one material signal:

- real business/process input;
- actual steps / prompt / workflow;
- editable artifact;
- correction/iteration process;
- failure or rework evidence;
- adoption friction;
- materially different user boundary.

Prefer independent practitioner evidence when it adds information, but **do not require an independent third party as a gate to close P04**. If the strongest resource remains an author/original tutorial after reasonable challenge, retain it with the correct evidence label.

Compare new evidence against the retained Castaldo + Anttu + draw.io package.

Close P04 when either:

- a stable recommendation package exists and additional search is unlikely to change the user decision; or
- the remaining practitioner coverage gap is explicit and further search has low expected value.

Do not repeat:

- draw.io official capability research already completed;
- static inspection already completed;
- runtime certification / P04B;
- new validation-framework design.

After P04, choose the next real Problem Card from demand evidence; likely candidates include P03 prototype, P02 PRD/FS, P05 PPT, data/Excel, testing, or a Codex/WorkBuddy workflow tied to a concrete job. Do not treat this list as a mandatory sequence.

## 9. Loop Engine — controlled execution pattern only

Current decision:

> **Use Loop Engine thinking; do not authorize unattended self-governing multi-card loops yet.**

Safe single-card pattern:

```text
Problem Card
→ practitioner discovery
→ inspect serious Tool/Skill/method
→ fact/safety check only where needed
→ material evidence gap?
    yes → targeted delta discovery
    no  → recommendation package
→ adversarial stop check
→ stop / review checkpoint
```

The loop optimizes **decision completeness**, not number of iterations, sources or platforms.

### Loop readiness is behavior-based, not card-count-based

Do not enable broader batching merely because `1–2 more cards` were completed.

Broader controlled batching becomes reasonable only when several heterogeneous real jobs demonstrate that the process can repeatedly:

- avoid early stopping after the first technically complete candidate;
- distinguish practical usefulness, independence, implementation evidence and official fact anchors correctly;
- use targeted delta search only when it can plausibly change the decision;
- stop with an explicit decision-quality rationale rather than a source-count threshold;
- avoid framework/governance expansion during execution;
- preserve the real Problem Card rather than drifting into tool-centric research.

Even then, use small bounded batches with a review checkpoint between cards/batches when judgement is uncertain.

### Loop must not autonomously

- change project principles/governance;
- install new Skills/MCPs/adapters;
- trigger runtime tests without an explicit material reason;
- declare the product PASS;
- process cards indefinitely;
- maximize source/platform/iteration counts;
- convert historical retained resources into permanent recommendations.

## 10. What good looks like

A strong output lets an ERP colleague answer:

- who has actually done something relevant;
- what to read/watch first;
- what input/steps/output are involved;
- which Tool/Skill is behind it;
- what rework/failure/adoption costs exist;
- whether claims are first-party, independent or promotional;
- what current official facts matter;
- whether they can try it tomorrow on real project material.

Final owner test:

> **Would we directly send this small package to a colleague because it saves search/learning time and helps them act?**

## 11. Cloud / local split

Cloud/ChatGPT should directly perform work it can do well: product judgement, Web/GitHub research, source/creator prioritization, fact checks, adversarial review, lightweight static inspection, GitHub maintenance and final curation decisions.

Use local Agent only when local capability materially adds evidence, such as local-only adapters, inaccessible source acquisition, justified runtime checks or evidence requiring the user's environment.

This is a capability/cost boundary, not an ideological cloud-vs-local rule.

## 12. Anti-drift

Stop and correct if work becomes:

- a new validation protocol per Tool;
- official-document gravity;
- independent-third-party evidence treated as a mandatory gate even when the best practical resource is first-party;
- one failed platform URL treated as platform absence;
- Bilibili/WeChat/Xiaohongshu treated as quotas;
- influencer popularity substituted for content evidence;
- duplicate social reposts counted as corroboration;
- stale setup presented as current truth;
- executable resources recommended with no proportional safety inspection;
- retained historical assets treated as permanent approvals;
- Curator synthesis presented as external experience;
- technical completeness mistaken for user usefulness;
- Loop Engine optimizing activity rather than decision quality;
- new frameworks added to solve one-off failures.

The project advances by accumulating **high-value practical resources for real work**, not tests, rules, links or loop iterations.
