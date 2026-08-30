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

## 7. Current retained / active evidence

### P01 — workshop/minutes → requirement package

Retained:

- `Convert Notes to Requirements Working Skill`

Current classification:

> **high task fit / low independent validation**

It is a useful working method, not an independently proven industry standard and not REAL_USER outcome validation.

### P04 — business description/requirements → editable process diagram

Current verdict:

> **CLOSED — RECOMMENDATION STABLE WITH EXPLICIT COVERAGE GAPS**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

Retained package:

- `冰冰酱 — 从一张白纸到交付PRD：我的全自动 AI 产品工作流` — independent practitioner workflow/judgement evidence;
- `健彬的产品Live / 北沐而川 — 3分钟绘制流程图！这个AI+绘图工具的神仙组合` — independent practitioner-style low-friction walkthrough;
- `Castaldo-Solutions/process-builder` — strongest enterprise-process-specific method/implementation retained; author self-practice;
- official `jgraph/drawio-mcp` — implementation/current-fact anchor;
- Anttu draw.io MCP article — optional technical operation/troubleshooting companion.

Do not reopen P04 unless a later real adoption decision exposes a new material risk.

### P06 — Excel / CSV / system export → reconcile and validate

Current status:

> **ACTIVE — cloud practitioner/fact research done; one bounded local runtime delta justified**

Authority / task envelope:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`

Current cloud judgement:

- direct conversational reconciliation can be useful for one-off low-risk work, but independent practice shows recurring reconciliation needs a frozen procedure, deterministic execution, explicit checks and exception routing;
- current spreadsheet-native AI is materially stronger than older chat-only workflows, so P06 must not assume `Python + Skill` is always required;
- `alchaincyf/huashu-excel` is the strongest currently discovered packaged audit-oriented method, but it is recent and primarily author self-practice;
- the only local test currently justified is whether Huashu-Excel materially improves ERP-style multi-file reconciliation over a competent plain code-first Agent.

Do not run broad local Web discovery or build a benchmark framework.

## 8. Immediate next action — finish P06 with cloud/local split

Cloud has already done the discovery/fact layer for the current P06 delta.

Local Agent should execute only the bounded comparison defined in:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`

Local freedom:

- fixture details, code, output format and internal iteration are flexible;
- use fresh isolated contexts for baseline vs with-Skill;
- temporary candidate checkout is allowed;
- do not globally install or modify project governance.

After local evidence returns, cloud will:

1. inspect the compact evidence package and key artifacts;
2. compare it with current practitioner evidence;
3. decide whether the final recommendation is spreadsheet-native AI, plain code-first Agent, Huashu-Excel, or a differentiated boundary between them;
4. stop P06 when the user decision is stable.

Do not start P03/P07/P10 in parallel.

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

Loop readiness is behavior-based, not card-count-based. Broader controlled batching becomes reasonable only when heterogeneous real jobs repeatedly show that the process can:

- avoid early stopping;
- distinguish practical usefulness, evidence independence, implementation evidence and official facts correctly;
- use delta search/tests only when they can plausibly change the decision;
- stop based on decision quality;
- avoid framework/governance expansion;
- preserve the real Problem Card rather than drifting into tool-centric research.

Even then, use small bounded batches with review checkpoints when judgement is uncertain.

Loop must not autonomously change project principles, install Skills/MCPs/adapters, trigger runtime tests without material reason, declare product PASS, maximize source/platform counts or process cards indefinitely.

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

For bounded local tasks, fix the objective, hard boundaries, escalation conditions and evidence return; leave search/execution details flexible unless a specific control is needed to preserve evidence validity.

## 12. Anti-drift

Stop and correct if work becomes:

- a new validation protocol per Tool;
- official-document gravity;
- independent-third-party evidence treated as a mandatory gate even when the best practical resource is first-party;
- one failed platform URL treated as platform absence;
- platform quotas or influencer popularity substituted for content evidence;
- duplicate social reposts counted as corroboration;
- stale setup presented as current truth;
- executable resources recommended with no proportional safety inspection;
- retained historical assets treated as permanent approvals;
- Curator synthesis presented as external experience;
- technical completeness mistaken for user usefulness;
- Loop Engine optimizing activity rather than decision quality;
- new frameworks added to solve one-off failures.

The project advances by accumulating **high-value practical resources for real work**, not tests, rules, links or loop iterations.
