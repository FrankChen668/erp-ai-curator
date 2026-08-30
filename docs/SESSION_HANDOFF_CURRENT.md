# ERP AI Curator — Current Session Handoff

Date: 2026-08-30

> Purpose: start a fresh ChatGPT/cloud session without replaying the full historical conversation. Always inspect current `main` before making project claims.

## 1. Repository

- GitHub: `FrankChen668/erp-ai-curator`
- Current authority: `docs/CURRENT_EXECUTION_PLAN_V3.md`
- Product north star: `docs/PROJECT_NORTH_STAR.md`
- Source strategy: `docs/SOURCE_STRATEGY_V3.md`
- Creator prior: `docs/CREATOR_PRIOR_STRATEGY_V3.md`
- Adversarial review: `docs/ADVERSARIAL_REVIEW_V3.md`
- Evidence status: `docs/validation/EVIDENCE_STATUS.md`

## 2. Product intent

ERP AI Curator is for SAP / Oracle / ERP / enterprise-information-system practitioners: implementation consultants, PMs, product managers, developers, solution roles.

Its value is not to build another AI tool directory or generic knowledge base.

Basic user question:

> **我现在碰到这个具体工作问题，有没有别人已经实践过的 Skill / Tool / 方法 / Prompt / 教程 / 经验，值得我马上学、马上用？**

Atomic unit:

```text
real project situation
+ real input artifacts
+ concrete work action/problem
+ expected deliverable
→ practical resource curation
```

Examples: meeting notes → requirements; requirements → PRD; requirements → prototype; business logic → editable process diagram; project materials → PPT; multiple Excel files → reconciliation; requirements → tests.

The 83-response training survey is the primary REAL_USER demand source. It validates demand, not solution quality.

## 3. Permanent source boundary

For practical adoption/learning questions, default evidence order is:

```text
第三方实操 / 攻略 / 测评 / 案例
→ actual Skill / Tool / repo / method
→ official/current fact anchor
→ limitations / counter-evidence
```

Official documentation normally verifies volatile facts: current feature, install, version, compatibility, price/license, privacy/data flow, output format.

Do not let official docs become the default learning recommendation.

### Platform rules

- Bilibili/WeChat/Xiaohongshu are valuable discovery pools when relevant.
- One failed page/adapter does not mean a platform lacks useful content.
- Ordinary public Web discovery should be tried before special adapters.
- WeChat Search → Reader is approved when a concrete high-value public article needs full text.
- Xiaohongshu remains an acquisition gap; report the gap instead of inferring scarcity.
- Do not force every platform into every run.

### Creator rules

Creator Prior affects where to inspect first, not what wins.

Followers/likes/views/stars are only discovery hints. Distinguish independent practitioner evidence from author/vendor/affiliate self-promotion. Derivative reposts of the same demo are one evidence family, not multiple independent validations.

## 4. Reuse existing ecosystems

Do not rebuild PM Skill libraries, Agent tutorials, WorkBuddy guides, prompt libraries, creator rankings or generic tutorial encyclopedias.

Existing PM/BA/Agent Skill libraries, community bluebooks, creator series and practical tutorials are feeder ecosystems.

Curator adds:

> ERP/enterprise Problem Card → find the relevant few → remove hype/stale/mismatch → pair practice with current fact checks → tell the colleague what is actually worth using.

Curator before Builder.

## 5. Validation/testing boundary

The project previously drifted into heavy validation: static review → install → runtime → artifact → repeated tests. That is no longer the default.

Runtime testing is exceptional, justified only when practitioner evidence is absent/contradictory, material safety/permission uncertainty remains, exact reproducibility is essential, or a resource may become a repeated internal standard.

For executable third-party Skill/MCP/plugin/script, lightweight static safety review is still required before recommending installation: install command, dependencies, credentials, filesystem/network/browser access, write operations, data egress, license/maintenance.

Do not create a new protocol for every tool.

## 6. Current evidence

### P01 — workshop/minutes → requirement package

Retained: `Convert Notes to Requirements Working Skill`.

Classification: **high task fit / low independent validation**. Useful working method, not an independently proven industry standard.

### P04 — business description/requirements → editable process diagram

Historical technical discovery found strong candidates, especially official `jgraph/drawio-mcp`.

Latest practitioner-first wave verdict:

> **USEFUL WITH GAPS / GOAL NOT YET COMPLETE**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_01.md`

Retained:

- `Castaldo-Solutions/process-builder`: strong ERP/task fit, but author self-practice rather than independent validation;
- `jgraph/drawio-mcp`: implementation/current-fact anchor;
- Anttu draw.io MCP article: useful operation/troubleshooting companion, not enough as primary ERP/business-process practice evidence.

Key failure: Discovery Recall. The local run stopped too early and said Bilibili evidence was insufficient, but a later simple cloud Web search immediately surfaced relevant PM/draw.io Bilibili content.

Therefore do not rerun technical/static/runtime work for P04.

## 7. Immediate next action

Do one narrow **P04 practitioner-evidence delta**:

1. inspect 2–4 high-signal Bilibili/Chinese practitioner candidates already discoverable through ordinary Web;
2. prioritize PM / consultant / enterprise workflow practitioners over tool-author self-demos;
3. use WeChat Reader only if one concrete high-value article needs it;
4. compare new practitioner evidence with retained Castaldo + Anttu package;
5. retain at most one primary practical guide and one materially different companion;
6. close P04 when extra search is unlikely to change the user decision or when the remaining coverage gap is explicit.

Do not repeat draw.io official research, static inspection, runtime certification or P04B.

After P04, likely next cards:

- P03: requirements/PRD → clickable prototype;
- P02: fragmented requirements → PRD/FS;
- P05: project materials → customer-ready PPT;
- Codex/WorkBuddy only when tied to a concrete work problem.

## 8. Loop Engine decision

Use **Loop Engine thinking**, but do not yet run an unattended multi-card loop.

Current safe pattern within one Problem Card:

```text
Problem Card
→ practitioner discovery
→ inspect serious Tool/Skill/method
→ fact/safety check only when needed
→ material evidence gap?
    yes → targeted delta discovery
    no  → recommendation package
→ adversarial stop check
→ stop for cloud/Owner review
```

Reason: repeated structure makes loop thinking useful, but P04 proves Discovery Recall and stop judgement are not stable enough for autonomous batching.

Forbidden for an unattended loop:

- changing project principles/governance;
- installing new Skills/MCPs/adapters;
- triggering runtime tests without explicit escalation;
- declaring product PASS;
- maximizing source/platform counts;
- processing Problem Cards indefinitely.

Recommended adoption:

1. finish P04 delta with supervision;
2. run 1–2 more Problem Cards;
3. if judgement and stop logic remain stable, use Loop Engine for bounded single-card/batch curation, with cloud/Owner review between cards or small batches.

Decision:

> **YES to Loop Engine thinking; NOT YET to unattended multi-card Loop Engine execution.**

## 9. Cloud/local responsibilities

Cloud ChatGPT owns:

- product judgement;
- Web/GitHub practitioner research;
- adversarial review;
- source/creator prioritization;
- current fact checks;
- lightweight static review;
- GitHub updates;
- final curation decision.

Local Codex/Agent is only needed for:

- local-only adapters/acquisition;
- content cloud paths cannot read;
- explicitly justified runtime checks;
- evidence requiring the local environment.

If cloud can do it, do not push work to local Agent.

## 10. Working style / anti-drift

- Chinese; concise and practical.
- First principles + adversarial review for solution changes.
- Inspect actual repo/docs before project claims.
- Do not proliferate frameworks, scores, gates, databases or taxonomies.
- Do not fabricate REAL_USER evidence.
- Curator synthesis must be labeled as synthesis.
- The real success test is: **would we directly send this resource package to a colleague because it saves search/learning time and helps them act tomorrow?**
