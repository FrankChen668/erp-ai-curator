# ERP AI Curator — Source Strategy V3

> Current source strategy for ERP / enterprise-delivery curation.

## 1. First principle

The user normally asks two different questions:

1. **别人到底怎么用，值不值得学，踩过什么坑？**
2. **这个功能现在是否真的存在，当前怎么安装，边界是什么？**

For training / practical curation, the first question usually determines usefulness; the second protects factual accuracy.

Therefore the default order is:

```text
real Problem Card
→ practitioner / review / tutorial discovery first
→ inspect the actual Skill / Tool / method referenced
→ official / original fact check for volatile claims
→ one falsification pass
→ small recommendation package
```

Do not default to official documentation and then look for practice only if something is missing.

Official documentation is usually a **fact anchor**, not the main learning resource.

## 2. Default evidence roles

### A. Practitioner guide / review / field note — default discovery lane

Use first when the question is about how to perform real work.

Good sources include:

- Bilibili / YouTube practical walkthroughs;
- WeChat public-account articles;
- Xiaohongshu practical notes;
- 人人都是产品经理 / 知乎 / 掘金 / CSDN / personal blogs;
- practitioner-created Skill / workflow collections;
- real project retrospectives, comparisons and failure reports.

Strong content shows some combination of:

- actual input;
- actual steps;
- prompt / command / configuration;
- screenshots / video / generated artifact;
- before / after;
- failures and correction;
- reusable Skill / template / repository;
- comments that reveal adoption friction.

### B. Original implementation artifact

Open the actual Skill / Tool / MCP / repository referenced by the practitioner content.

Use it to confirm what is really implemented and to avoid recommending recycled or misrepresented content.

### C. Official / current fact anchor

Use official docs / release notes / original vendor pages primarily to verify volatile claims:

- current feature availability;
- install command;
- version / compatibility;
- pricing / licensing;
- privacy / data flow;
- platform support;
- native output format.

### D. Independent counter-evidence

For non-trivial adoption, look once for:

- failures;
- unresolved issues;
- stale setup;
- compatibility problems;
- hidden paid requirements;
- correction cost;
- evidence that a simpler existing workflow is already enough.

## 3. Search order for practical Problem Cards

For most survey-derived practical jobs, use:

1. search the real task in natural practitioner language;
2. search Bilibili / WeChat / Xiaohongshu / PM-consulting communities / blogs for walkthroughs and reviews;
3. check known high-signal creators and existing curated resource libraries;
4. open the original Skill / Tool / repo behind serious candidates;
5. verify only the current facts that matter against official/original sources;
6. stop when additional searching is unlikely to change the recommendation.

This is **practitioner-first**, not **platform-quota**.

If a platform cannot be fully read because of login, anti-bot, dynamic rendering or tooling limits:

- use public search/discovery evidence only for discovery;
- invoke an already-approved read adapter when available and justified;
- otherwise record a coverage gap;
- never invent unseen content.

## 4. Existing resource ecosystems are feeder sources, not competitors

Do not rebuild resources that already exist.

Existing PM/Agent Skill libraries, practical bluebooks, creator series and tutorial collections should be treated as **feeder ecosystems**.

Curator value is not to duplicate them. Curator adds:

```text
ERP / enterprise delivery Problem Card
→ find the few relevant items across existing ecosystems
→ remove hype / stale / mismatched content
→ pair practical experience with current fact checks
→ explain exactly when a consultant should use it
```

Do not create another generic Prompt library, Skill directory, creator leaderboard or tutorial encyclopedia.

## 5. Creator prior

Creator Prior affects where to inspect first.

For practical AI delivery work, useful creator topics include:

- AI 产品经理 / PM;
- AI 企业咨询 / 数字化顾问;
- requirements / PRD / prototype;
- process diagram / draw.io / BPMN;
- PPT / documentation;
- Excel / data processing;
- Codex / Claude Code / WorkBuddy / Agent workflows;
- reusable Skills / prompts / workflows.

Popularity is only a discovery hint.

Rough hints when available:

- Xiaohongshu: 收藏/收藏率、有效评论 > 点赞/粉丝;
- Bilibili: 收藏、投币、有效评论 > 单纯播放/点赞/粉丝;
- WeChat: sustained original practical output > account prestige;
- GitHub: capability/examples/maintenance/issues > stars/forks.

Adversarial test:

> If author name and engagement metrics were hidden, would this specific content still be worth sending to a colleague?

## 6. Original-content rule

Do not recommend a practical resource based only on:

- search snippet;
- AI summary;
- repost title;
- engagement count;
- creator reputation;
- screenshots without context.

Read the original article / video page or transcript / repository / sufficiently complete primary material whenever technically possible.

## 7. Independence and incentive rule

`Third-party` does not automatically mean `independent`.

For any serious practical guide/review, identify when reasonably observable whether the creator is:

- the Tool / Skill author or maintainer;
- an employee / official evangelist / partner;
- an affiliate, paid promoter or course seller;
- an independent practitioner;
- unknown.

Author-created tutorials are still valuable for operation steps, but they are **first-party practice evidence**, not independent validation.

Commercial relationships do not automatically disqualify content. They lower confidence in comparative claims such as `best`, `better`, `saves X%`, or `no downside` unless supported elsewhere.

Do not require formal disclosure research for every post; record only material, observable incentives that could change interpretation.

## 8. Content-lineage / echo rule

Ten posts repeating one original demo are not ten independent pieces of evidence.

When several practical sources:

- use the same screenshots/demo;
- repeat the same prompt almost verbatim;
- point to the same upstream tutorial/repo;
- repeat identical claims without new failure/adoption evidence;

collapse them mentally to one evidence family.

Prefer sources that add **independent operating experience**, different constraints, failure modes, before/after artifacts or a materially different workflow.

Do not confuse social repetition with corroboration.

## 9. Freshness and version coupling

A practical tutorial can be useful even when old, but the Curator must separate:

- **stable practice insight** — workflow, prompt structure, review habit, failure lesson;
- **version-coupled instruction** — UI path, install command, model name, API, plugin syntax, feature availability, pricing.

When a practical resource depends materially on a version/tool state, record the publication/update date when available and recheck the version-coupled claims against current original/official evidence.

Do not reject an old article merely for age if the stable insight still transfers. Do not present stale setup steps as current truth.

## 10. Minimum safety review for executable resources

Practitioner-first does **not** mean `install first`.

Before recommending that a colleague install/run a third-party Skill / MCP / plugin / script, do a lightweight static safety check proportional to risk. At minimum inspect, when available:

- repository/source ownership and current state;
- installation commands and package dependencies;
- requested credentials / API keys;
- filesystem, shell, browser, network or account access;
- whether it exposes mutating actions;
- obvious data egress / telemetry paths;
- license and maintenance signals when relevant.

This is not a mandatory runtime certification.

If the practical value can be learned without installation, prefer `learn/read first` and separate that from `safe to install`.

High-risk or unclear executable candidates should be marked conditional or escalated to a focused runtime/security check rather than casually recommended for enterprise material.

## 11. Lightweight retained-resource memory

Do not build a large resource database, but do not lose the evidence boundary either.

When a resource is actually retained as an asset, keep only lightweight provenance needed for safe reuse, such as:

- Problem Card / job it solved;
- resource title + original URL;
- creator / source role;
- practical evidence actually observed;
- important limitations / incentive caveat;
- tool/repo/version/commit when materially relevant;
- last checked date;
- current state such as `retain`, `conditional`, `stale/recheck`.

Historical retention is a **search prior**, not permanent approval. Reused volatile claims must be rechecked when they matter.

## 12. Local runtime testing — exception, not default

ERP AI Curator is not a tool-testing laboratory.

Do **not** install and smoke-test every promising Skill or Tool.

Run a local test only when at least one of these is true:

1. third-party practical evidence is missing or contradictory;
2. installation / permission / data-safety risk is material;
3. the exact training recommendation depends on reproducible local steps;
4. a candidate is likely to become a repeated internal standard and the cost of being wrong is high.

When good practitioner evidence + original implementation + current fact checks already answer the user's decision, stop.

## 13. Recommendation package

Default package should reflect the user journey:

### Practical recommendation — first

The tutorial / workflow / Skill / method most useful to learn and apply.

Explain:

- what real job it solves;
- input;
- actual steps;
- expected output;
- why practitioners found it useful;
- limitations / correction cost;
- whether the practical source is independent, first-party or commercially interested when that materially changes interpretation.

### Tool / Skill — when applicable

Link the actual implementation or product used by the practical guide.

If installation is recommended, distinguish `practical usefulness` from `installation/safety confidence`.

### Official fact anchor — supporting

Attach only the official/current facts needed to prevent stale or inaccurate adoption.

### Alternative — only if materially different

For example no-install/browser vs local Agent/Skill.

Avoid flat link lists.

## 14. Success test

The source strategy works when an ERP colleague can answer:

> **别人实际怎么做？我今晚应该先看哪个？明天怎么在自己的项目材料上试？这个方法有哪些坑？这是不是作者自己在推产品？当前版本还成立吗？如果要安装，企业环境是否值得冒这个成本？**

That is more important than proving the Curator searched every platform or technically validated every candidate itself.
