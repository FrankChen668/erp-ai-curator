# ERP AI Curator — Creator Prior Strategy V3

Date: 2026-08-30

## 1. Purpose

This strategy improves discovery recall for practitioner content.

It does **not** define a popularity ranking and does **not** make creators recommendation authorities.

The question is:

> When looking for practical AI resources for ERP / enterprise delivery work, which creators are worth checking early because they repeatedly publish concrete, reusable material?

A creator prior affects **search order**, not the final recommendation decision.

## 2. First-principles model

Use three separate layers:

```text
Creator prior
→ helps decide where to look first

Content evidence
→ decides whether this specific article/video/post is useful

Current fact verification
→ verifies volatile capability/setup claims against original/official sources when needed
```

Never collapse these into one popularity score.

## 3. What creates a strong creator prior

A creator becomes a useful discovery seed when their history repeatedly shows several of the following:

- focuses on AI product management, enterprise consulting, Agent workflows, practical AI adoption or adjacent delivery work;
- publishes concrete operating steps rather than only concept commentary;
- shows inputs, prompts, screenshots, demos, outputs or before/after artifacts;
- explains failure modes, limitations or correction loops;
- provides reusable templates / Skills / workflows / repositories / examples;
- connects AI usage to real work such as requirements, PRD, prototypes, process diagrams, PPT, data processing, testing or project management;
- updates content when tools change;
- has multiple useful posts over time rather than one viral hit;
- receives substantive comments/questions from practitioners that expose real adoption experience.

Creator prior should be reduced when the account is mainly:

- generic AI news reposting;
- motivational/productivity content with little operational detail;
- prompt-list aggregation without examples;
- affiliate/vendor promotion with weak counter-evidence;
- highly polished demos without reproducible steps;
- stale tutorials for volatile tools.

## 4. Engagement signals — discovery hints only

No single metric is a quality label.

### Xiaohongshu

When available, a rough discovery preference is:

`收藏/收藏率 > 高质量评论 > 点赞 > 粉丝数`

Reason:

- saves often signal future-use intent;
- comments can reveal whether users actually tried the workflow;
- likes are lower-cost reactions;
- follower count mostly measures account reach, not task fit.

Do not treat this as a numeric scoring formula.

### Bilibili

When available, useful hints include:

`收藏/投币 + 评论质量 + 完播/长期搜索可见性 > 点赞/播放量 > 粉丝数`

Practical tutorials with modest views can be more valuable than viral concept videos.

### WeChat public accounts

Public comparable engagement is often incomplete.

Prefer creator history signals:

- repeated original practical articles;
- recognizable specialization;
- concrete screenshots/templates/cases;
- consistent update quality;
- useful cross-reference/citation by practitioners.

Do not infer quality from account prestige alone.

### GitHub

For Tools / Skills / workflows:

`actual capability + README/example quality + maintenance/issues > stars/forks`

Stars/forks mainly help discovery and maturity estimation.

## 5. Creator-first discovery lane

When a delivery Problem Card would benefit from practitioner evidence, Curator may use a creator-first lane:

1. search normally for the real problem;
2. check known high-signal creators whose historical topic matches the job;
3. search within or around those creators for the current specific problem;
4. open/read the original content;
5. compare against strong content from outside the creator seed set;
6. falsify important claims;
7. stop when the package is stable.

The creator lane supplements open discovery. It must not become a closed whitelist.

## 6. Seed-set lifecycle

A small creator seed set may be maintained as discovery memory.

A creator enters the seed set only after Curator has independently observed repeated useful content, or strong external evidence indicates consistent practical value.

Record only lightweight fields such as:

- creator/account name;
- platform;
- stable profile/original URL when available;
- recurring topics;
- observed strengths;
- known weaknesses / promotional bias / access limits;
- last checked date;
- examples of content that actually passed curation.

Do **not** store passwords, cookies, private follower data or scrape-derived personal data.

Do not build a large influencer database.

## 7. Recommendation boundary

A high-prior creator can still produce a bad post.

A low-follower niche creator can still produce the best resource.

Therefore:

> **Creator reputation may decide what to inspect first; only the specific content and evidence decide what to recommend.**

The final package must still answer:

- does this solve the user's concrete delivery job?
- can another practitioner reproduce/use it?
- was the original content actually read?
- are volatile claims current?
- are marketing/source limitations explicit?

## 8. Adversarial checks

Before relying heavily on creator priors, ask:

1. Are we creating a popularity echo chamber?
2. Are several creators copying the same original source?
3. Are engagement metrics inflated by broad-interest AI content rather than project-delivery relevance?
4. Are we missing niche ERP/BA/PM practitioners with smaller audiences?
5. Is a creator's old reputation being used to excuse weak current content?
6. Does the creator have a commercial incentive that should be disclosed?
7. Would the resource still be recommended if the author name and metrics were hidden?

If the last answer is no, the evidence is too reputation-dependent.

## 9. Product implication

Creator priors are a discovery optimization, not a new Gate or recommendation score.

They are especially useful for:

- AI enterprise consulting;
- AI product management;
- Agent/Codex/WorkBuddy usage;
- requirements / PRD / prototypes;
- process diagrams;
- PPT / documentation;
- spreadsheet/data workflows;
- high-quality prompt/workflow examples.

Real survey Problem Cards remain the driver. Creator seeds only improve how Curator searches for answers to those problems.
