# ERP AI Curator — Creator Prior Strategy V3

Date: 2026-08-30

## 1. Purpose

For practical ERP / enterprise-delivery questions, creator and practitioner content is often the fastest way to discover **how people actually use AI at work**.

Creator Prior therefore exists to improve discovery recall and reduce blind search cost.

It is not an influencer ranking.

## 2. Default position

For Problem Cards that ask “怎么做 / 有什么技巧 / 哪个 Skill 值得用 / 实际踩坑是什么”, practitioner discovery is the default first lane.

Use:

```text
real work problem
→ open practitioner / review / tutorial discovery
→ check known high-signal creators / collections
→ inspect specific content
→ trace back to actual Tool / Skill / repo
→ current official fact check when needed
```

Do not start from official docs by default for this kind of question.

## 3. What makes a useful creator seed

A creator is worth checking early when repeated history shows:

- real operating steps rather than AI news commentary;
- actual prompts / commands / screenshots / videos / files;
- before/after artifacts;
- failure modes and correction;
- reusable Skills / workflows / templates / repos;
- project-delivery topics such as requirements, PRD, prototypes, diagrams, PPT, spreadsheets, testing or project management;
- current Agent practice such as Codex / Claude Code / WorkBuddy;
- multiple useful posts over time, not one viral hit.

Reduce prior for:

- generic AI news/reposts;
- motivational productivity content;
- prompt-list aggregation with no examples;
- affiliate/vendor promotion with no counter-evidence;
- polished demo with no reproducible steps;
- stale tutorials for volatile tools.

## 4. Engagement signals — hints only

No numeric score.

### Xiaohongshu

When available:

`收藏/收藏率 + 有效评论 > 点赞 > 粉丝数`

### Bilibili

When available:

`收藏 + 投币 + 有效评论 > 播放/点赞 > 粉丝数`

### WeChat

Public metrics are incomplete. Prefer:

- sustained original practical articles;
- topic consistency;
- concrete screenshots/templates/cases;
- practitioner cross-reference.

### GitHub

Prefer:

`actual capability + examples + maintenance + issues > stars/forks`

## 5. Independence / commercial-interest discipline

Creator Prior must not silently treat all creator content as independent review.

When materially observable, distinguish:

- independent practitioner;
- Tool / Skill author or maintainer;
- vendor employee / evangelist / partner;
- affiliate / sponsored promoter / course seller;
- unknown.

A creator can still be a strong discovery seed even when commercially connected. The implication is narrower:

- trust concrete operation/demo evidence for what it visibly proves;
- lower confidence in comparative or superlative claims;
- seek independent counter-evidence before repeating `best`, `better`, `huge efficiency gain` or similar claims.

Do not require invasive background research. Only record incentive information that is public and materially relevant.

## 6. Content-lineage discipline

Many AI creators repackage the same upstream demo, Skill or prompt.

Do not count multiple derivative posts as independent confirmation merely because they come from different accounts.

When several posts share the same source/demo/prompt, ask:

> **What new evidence does this creator add?**

Useful incremental evidence includes:

- different real input;
- a failure case;
- correction/rework process;
- enterprise/privacy constraint;
- a different tool boundary;
- long-term usage experience;
- a genuinely clearer reproducible tutorial.

If there is no incremental evidence, treat them as one evidence family.

## 7. Existing creator/resource ecosystems

Do not recreate what existing communities already curate.

Useful feeder ecosystems may include:

- AI 产品经理 / Agent creator series on Bilibili;
- WeChat public-account practical articles;
- Xiaohongshu PM / consultant / AI-office notes;
- 人人都是产品经理 / 知乎 / 掘金 / CSDN / personal blogs;
- existing PM Agent Skill libraries;
- tool-specific practical bluebooks / case libraries.

Curator should use these as upstream discovery pools, then apply the ERP Problem Card and evidence rules.

## 8. Seed-set lifecycle

A small seed set is allowed.

Add a creator only after at least one strong item has passed curation and there is evidence of repeated topic-quality, or strong external evidence of sustained practical output.

Record only lightweight fields:

- creator/account;
- platform;
- stable profile URL when available;
- recurring topics;
- observed strengths;
- known weaknesses / promotional bias / access limits;
- observable relationship to promoted tools when material;
- examples that actually passed curation;
- last checked date.

No passwords, cookies or private data.

No large influencer database.

## 9. Recommendation boundary

Creator prior affects **what to inspect first**.

Specific content decides **what to recommend**.

Adversarial tests:

> If the author name, follower count, likes, saves and views were hidden, would this specific resource still deserve recommendation?

> If five other creators disappeared because they all copied the same upstream source, would the remaining evidence still support the claim?

If not, do not treat popularity or repetition as evidence quality.

## 10. Platform access discipline

Do not assume a platform is unusable merely because one adapter failed.

Separate:

- discovery via normal Web/index;
- original page accessibility;
- transcript/full-text accessibility;
- login/cookie requirement;
- adapter availability.

Examples:

- a Bilibili video may be discoverable through public Web even when direct page/transcript retrieval later hits anti-bot;
- WeChat keyword discovery may require the approved Search → Reader chain to reach original article text;
- Xiaohongshu may have stronger indexing/login/dynamic-rendering gaps.

Use the least costly available path first; report coverage gaps rather than equating access difficulty with content scarcity.

## 11. Product implication

The resource library should feel like:

> **有人已经实战过，我帮你找到最值得看的那一两个，分清是独立经验还是作者自述，再把当前官方边界核对清楚。**

It should not feel like:

> **我重新为每个 Tool 做一遍实验室认证。**
