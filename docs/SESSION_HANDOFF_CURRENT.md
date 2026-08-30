# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> Purpose: start a fresh cloud/ChatGPT session without replaying the full conversation. Always inspect current `main` before making project claims.

## 1. Repository and authority

- GitHub: `FrankChen668/erp-ai-curator`
- Current execution authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Product contract: `docs/PROJECT_NORTH_STAR.md`
- Source strategy: `docs/SOURCE_STRATEGY_V3.md`
- Creator prior: `docs/CREATOR_PRIOR_STRATEGY_V3.md`
- Adversarial review: `docs/ADVERSARIAL_REVIEW_V3.md`
- Current evidence: `docs/validation/EVIDENCE_STATUS.md`

Do not rely on this handoff if the repository has changed; current `main` wins.

## 2. Product intent

ERP AI Curator serves SAP / Oracle / ERP / enterprise-information-system practitioners: implementation consultants, PMs, product managers, developers and solution roles.

It is not a generic AI tool directory, tutorial encyclopedia, Prompt library or tool-certification lab.

Core user question:

> **我现在碰到这个具体工作问题，别人已经有哪些值得学习和采用的 AI Skill / Tool / 方法 / 教程 / 经验？**

Atomic unit:

```text
real project situation
+ actual input artifacts
+ concrete work problem/action
+ expected deliverable
+ material constraints
→ practical resource curation
```

## 3. Demand evidence boundary

The 83-response 2026-08 training survey is the primary REAL_USER demand source.

Important boundary:

- closed-choice aggregates are direct evidence;
- free-text responses are mainly semantic/pattern evidence because the survey platform may have performed second-level summarization or polishing;
- do not treat polished free text as guaranteed verbatim user wording;
- the survey validates **demand**, not solution outcome or recommendation quality.

Problem Cards are normalized search/judgement units, not a permanent scenario taxonomy.

## 4. Source principle

For adoption/learning questions, default evidence flow is:

```text
practical guide / review / case / field experience
→ actual Skill / Tool / repo / method
→ official/current fact check where needed
→ limitations / counter-evidence
```

Interpret this as **practical-value-first**, not `independent-third-party-at-all-costs`.

An author, maintainer, official team or original repository may be the best practical resource if it contains the strongest workflow, examples, artifacts and failure guidance. If so, it can be the primary recommendation, but label its evidence role honestly.

Independent practitioner evidence is valuable when it changes confidence, comparative judgement, failure understanding or adoption cost. It is not a mandatory gate.

Official/current sources mainly verify volatile facts such as version, install, compatibility, price/license, privacy/data flow and native output format.

## 5. Discovery/platform boundary

Relevant discovery pools may include Bilibili, WeChat, Xiaohongshu, YouTube, PM/BA/consulting communities, blogs, GitHub Skill collections and existing Agent/PM ecosystems.

Rules:

- one failed page/adapter does not mean a platform lacks useful content;
- ordinary Web discovery before special adapters;
- WeChat Search → Reader only when a concrete high-value public article needs full text;
- Xiaohongshu access limitations are a Coverage Gap, not content-scarcity evidence;
- no platform quota;
- popularity metrics are discovery hints only;
- derivative reposts of one demo are one evidence family;
- do not stop merely because one technically complete candidate has been found.

## 6. Curator before Builder

Existing PM/BA Skill libraries, Agent tutorials, WorkBuddy guides/bluebooks, creator series and tool-specific practical collections are feeder ecosystems.

Curator value is:

> real ERP/enterprise Problem Card → find the relevant few → remove hype/stale/mismatch → connect practice to Tool/Skill → verify necessary current facts → recommend a small actionable package.

Do not rebuild generic PM Skill libraries, WorkBuddy manuals, Codex handbooks or tutorial encyclopedias when strong upstream material exists.

Curator-created methods must be labeled `Curator synthesis`.

## 7. Safety/testing boundary

Runtime/artifact testing is exceptional, not default.

For executable third-party Skill/MCP/plugin/script, use proportional lightweight static inspection before recommending installation when relevant: install/dependencies, credentials, filesystem/network/browser/shell access, writes, data egress, license/maintenance.

Runtime testing is justified only when a material decision cannot be resolved through practitioner evidence + original implementation + current facts.

## 8. Current evidence

### P01 — workshop/minutes → requirement package

Retained:

- `Convert Notes to Requirements Working Skill`

Classification:

> **high task fit / low independent validation**

Useful working method; not an independently proven industry standard and not REAL_USER outcome validation.

### P04 — business description/requirements → editable process diagram

Current verdict:

> **USEFUL WITH GAPS / GOAL NOT YET COMPLETE**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_01.md`

Retained:

- `Castaldo-Solutions/process-builder` — strong task-fit method/implementation; author self-practice;
- official `jgraph/drawio-mcp` — implementation/current-fact anchor;
- Anttu draw.io MCP article — useful independent technical operation/troubleshooting companion, but not enough by itself as ERP/business-process practice evidence.

Observed failure:

> Discovery Recall stopped too early after a technically complete candidate; later ordinary Web search surfaced additional relevant practitioner material.

Do not rerun P04 technical/static/runtime research already completed.

## 9. Immediate next action

Do one narrow **P04 practitioner-evidence delta** to challenge/complete the current package, then close P04.

Start with the known Chinese/Bilibili recall gap because it has already produced relevant candidates, but do not treat Bilibili, Chinese content, or any fixed candidate count as a requirement.

Look for practitioner content that adds material evidence such as:

- real business/process input;
- actual operation/prompt/workflow;
- editable output;
- correction/iteration;
- failure/rework;
- adoption friction;
- a materially different user boundary.

Independent evidence is preferred when informative, but not required as a closure gate.

Compare new evidence with the retained Castaldo + Anttu + draw.io package.

Close P04 when additional search is unlikely to change the user decision or when the remaining coverage gap is explicit and further search has low expected value.

Do not repeat:

- draw.io official capability research already completed;
- static review already completed;
- runtime certification / P04B;
- validation-framework design.

After P04, choose the next real Problem Card from demand evidence. P03 prototype, P02 PRD/FS, P05 PPT, data/Excel, testing, or a concrete Codex/WorkBuddy workflow are candidates, not a mandatory sequence.

## 10. Loop Engine position

Current decision:

> **Use Loop Engine thinking as a controlled single-card pattern; do not authorize unattended self-governing multi-card loops yet.**

Safe pattern:

```text
Problem Card
→ practitioner discovery
→ inspect serious Tool/Skill/method
→ fact/safety check only where needed
→ material evidence gap?
    yes → targeted delta discovery
    no  → recommendation package
→ adversarial stop check
→ review checkpoint / stop
```

Loop readiness is **behavior-based**, not `after 1–2 more cards`.

Broader controlled batching only becomes reasonable when heterogeneous real jobs repeatedly show that the process can:

- avoid early stopping;
- classify evidence roles correctly;
- use delta search only when it can change the decision;
- stop based on decision quality, not source count;
- avoid tool-centric drift and governance expansion.

Even then, batches stay small and bounded, with review checkpoints when judgement is uncertain.

Loop must not autonomously change project principles, install Skills/MCPs/adapters, trigger runtime tests without material reason, declare product PASS, maximize source/platform counts or process cards indefinitely.

## 11. Cloud/local split

Cloud/ChatGPT should directly do what it can do well: product judgement, Web/GitHub practitioner research, source prioritization, current fact checks, adversarial review, lightweight static inspection, GitHub maintenance and final curation decisions.

Use local Agent only when local capability materially adds evidence: local-only adapters, inaccessible source acquisition, justified runtime checks or evidence requiring the user's environment.

This is a capability/cost boundary, not a rigid ideology.

## 12. Working style / anti-drift

- Chinese; concise, practical.
- First principles + adversarial review for solution changes.
- Inspect actual repo/docs before project claims.
- Do not proliferate frameworks, scores, gates, databases or taxonomies.
- Do not fabricate REAL_USER evidence.
- Do not turn `practitioner-first` into `independent-third-party-only`.
- Do not turn a known Bilibili recall gap into a new Bilibili quota.
- Do not turn Loop into an activity-maximizing automation.
- The success test remains:

> **Would we directly send this small package to a colleague because it saves search/learning time and helps them act on real project material?**
