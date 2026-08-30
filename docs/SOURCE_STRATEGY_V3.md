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

## 7. Local runtime testing — exception, not default

ERP AI Curator is not a tool-testing laboratory.

Do **not** install and smoke-test every promising Skill or Tool.

Run a local test only when at least one of these is true:

1. third-party practical evidence is missing or contradictory;
2. installation / permission / data-safety risk is material;
3. the exact training recommendation depends on reproducible local steps;
4. a candidate is likely to become a repeated internal standard and the cost of being wrong is high.

When good practitioner evidence + original implementation + current fact checks already answer the user's decision, stop.

## 8. Recommendation package

Default package should reflect the user journey:

### Practical recommendation — first

The tutorial / workflow / Skill / method most useful to learn and apply.

Explain:

- what real job it solves;
- input;
- actual steps;
- expected output;
- why practitioners found it useful;
- limitations / correction cost.

### Tool / Skill — when applicable

Link the actual implementation or product used by the practical guide.

### Official fact anchor — supporting

Attach only the official/current facts needed to prevent stale or inaccurate adoption.

### Alternative — only if materially different

For example no-install/browser vs local Agent/Skill.

Avoid flat link lists.

## 9. Success test

The source strategy works when an ERP colleague can answer:

> **别人实际怎么做？我今晚应该先看哪个？明天怎么在自己的项目材料上试？这个方法有哪些坑？官方当前边界是什么？**

That is more important than proving the Curator searched every platform or technically validated every candidate itself.
