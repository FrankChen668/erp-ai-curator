# ERP AI Curator — Source Strategy V3

> Draft for testing. The goal is not to maximize source diversity; it is to combine **trustworthy capability facts** with **practical, reproducible usage evidence** for generalized ERP / enterprise-information-system practitioners.

## 1. Core principle

A good recommendation should answer two different questions:

1. **Can this capability actually be used now?**
2. **How does a practitioner use it well in real work?**

These questions often require different sources.

- Official / original sources are usually strongest for product facts, installation, versions, compatibility, APIs, supported capability and security/privacy statements.
- Practitioner / community sources are often stronger for workflow, prompts, examples, failure modes, adoption friction, comparison and real usage experience.

Therefore:

> **Official sources establish truth; practitioner sources establish practical value. Neither source class automatically owns the recommendation slot.**

## 2. Source classes

### A. Original / official

Examples:

- official product documentation;
- official repository / README;
- vendor release notes;
- original author documentation;
- official learning material.

Best for:

- current capability;
- installation / configuration;
- version / compatibility;
- API / endpoint / environment variables;
- pricing / license;
- native vs extension boundary;
- data / privacy statements.

### B. Practitioner / community

Examples:

- GitHub projects / Skills / MCPs maintained by practitioners;
- WeChat public-account articles;
- Xiaohongshu practical posts;
- Bilibili / YouTube tutorials;
- Zhihu / Juejin / CSDN / personal blogs;
- implementation notes, comparative reviews and field reports.

Best for:

- real operating steps;
- prompts / templates;
- concrete examples and outputs;
- common mistakes and workarounds;
- comparison between alternatives;
- learning curve and adoption cost;
- transfer into ERP / enterprise project work.

## 3. Search behavior

When Mode B requires resource discovery:

1. define the capability gap first;
2. search original/official sources for what the capability is and whether it is current;
3. deliberately search practitioner/community sources for how it is actually used;
4. for GitHub-like resources, open README plus task-relevant examples / docs / issues when needed;
5. for articles/videos/posts, require enough concrete evidence to judge whether the author actually used the method;
6. compare candidates by practical task fit, not by source prestige;
7. stop when additional searching is unlikely to change the decision.

Do not require every final recommendation to contain both source classes. Some topics genuinely have only one strong source class.

## 4. Preferred recommendation shape

When evidence supports it, prefer a layered recommendation rather than a flat link list:

### Main recommendation
The Tool / Skill / method actually worth adopting.

### Truth anchor
An official/original link used to confirm current capability, setup, compatibility or limits.

### Practical companion
One strong practitioner/community resource that helps the user use the recommendation well.

### Advanced option
Only when a second solution has a genuinely different use case or capability boundary.

The truth anchor and practical companion do **not** automatically consume separate recommendation slots. They can support one main recommendation.

## 5. Practitioner-source admission test

A community source should normally show at least two of the following:

- real operating steps;
- screenshots / demo / code / prompt / output;
- clear input and result;
- specific failure modes or limitations;
- comparison with another method;
- reproducible setup or example;
- evidence of actual project use.

Signals that reduce confidence:

- pure repost / aggregation;
- title-only or generic AI summary;
- obvious promotional copy without real operation;
- no original output or evidence;
- outdated setup without date/version context;
- copied screenshots with no process explanation.

Popularity, likes, followers, stars and repost count are weak signals only.

## 6. Chinese-source policy

Chinese practitioner content can be especially valuable because it reduces adoption cost for internal ERP users.

When quality is comparable, prefer Chinese practical content.

But Chinese-language convenience cannot override:

- factual errors;
- outdated setup;
- weak evidence;
- obvious marketing;
- mismatch with the task.

If the best original source is English and the best practical explanation is Chinese, that is often an ideal combination.

## 7. Platform-specific caution

WeChat, Xiaohongshu, Bilibili and similar platforms can contain excellent practical content, but discovery ranking and engagement are not quality proof.

Treat them as practitioner evidence, not as authoritative capability evidence.

For volatile or product-native claims mentioned in community content, verify against a current original/official source before presenting them as fact.

## 8. Output discipline

The user should not receive a source dump.

Default output for a resource-discovery task:

- 1 main recommendation;
- optional second recommendation only for a meaningfully different use case;
- official/original truth anchor when needed;
- up to 1–2 practical companion resources when they materially improve adoption;
- a short list of important rejected candidates if useful for explaining the choice.

A practitioner companion may be more valuable to the user than the official manual, but the official manual may still be kept as a fact anchor.

## 9. Success test

The source strategy is working when the final package answers:

> **What should I use? Why is it trustworthy? How do I actually get value from it? What are the real limitations?**

Not merely:

> Here are two authoritative links.
