# Adversarial Review — Source Strategy V3

Date: 2026-08-29

Purpose: attack the first draft of `docs/SOURCE_STRATEGY_V3.md` before using it in local-Agent tests.

## 1. Attack: “official = truth” is too absolute

Risk:

- official pages can be marketing-heavy, incomplete or silent about practical failure modes;
- an original GitHub repository may be more useful than a vendor product page;
- a practitioner may reveal a limitation that official material does not emphasize.

Correction:

> Official/original sources are the preferred **fact anchor for native capability, version, setup, compatibility, pricing and policy claims**, not a universal truth hierarchy.

Recommendation quality must still come from task fit and evidence.

## 2. Attack: forcing source diversity can become a new coverage KPI

Risk:

The Agent may search WeChat, Xiaohongshu, Bilibili, GitHub and official sites for every task merely to prove “diversity”, recreating over-research.

Correction:

- search source classes to resolve an information gap, not to tick boxes;
- practitioner search is strongly preferred when it can materially improve adoption guidance;
- stop when another source is unlikely to change the recommendation or help the user act.

## 3. Attack: community access can be partial or indirect

Risk:

Some platforms are login-gated, dynamically rendered or poorly indexed. Search snippets can look convincing while the original post was never actually read.

Correction:

> Never promote a community item to a recommended practical companion unless the original content, transcript, repository or sufficiently complete primary material was actually opened/read.

If access is unavailable, report the coverage gap. Do not infer the content from a search snippet.

## 4. Attack: “two evidence signals” can become another Gate

Risk:

The project previously drifted into checklist optimization. A rigid admission count encourages superficial box-ticking.

Correction:

Convert the list into heuristics. The real question is:

> Does this source provide enough concrete evidence that a practitioner can learn, reproduce or judge the method?

No numeric threshold.

## 5. Attack: practical companions can become a new link dump

Risk:

“1–2 practical companions + official anchor + second solution + rejected list” can quietly expand into 5–8 links.

Correction:

Default package:

- 1 main solution;
- 0–1 practical companion;
- fact anchor only when useful;
- second solution only for a different capability boundary.

More links require explicit user request or clear incremental value.

## 6. Attack: community popularity can masquerade as experience quality

Risk:

Likes, stars, followers, reposts, polished screenshots and enthusiastic language are easy to game.

Correction:

Prefer evidence of actual use:

- real inputs/outputs;
- steps;
- constraints;
- failures;
- comparison;
- updates / maintenance;
- reproducibility.

Engagement remains a weak discovery signal only.

## 7. Attack: platform taxonomy is misleading

Risk:

“GitHub = community” is not always true: an official vendor repo is original/official. A personal repo may be both primary implementation and practitioner evidence.

Correction:

Classify sources by **evidence role**, not by website:

- fact anchor;
- implementation/original artifact;
- practitioner guide/review;
- independent comparison;
- secondary/aggregation.

A source may play more than one role.

## 8. Attack: positive best-practice bias

Risk:

Only searching “教程 / 最佳实践 / 推荐” can produce promotional success stories and miss real failure modes.

Correction:

For non-trivial adoption decisions, deliberately look once for counter-evidence such as:

- limitations;
- issues;
- failed attempts;
- negative reviews;
- maintenance problems;
- compatibility caveats.

This is not a fixed query count; it is a falsification habit before a confident recommendation.

## 9. Attack: practitioner content can become stale faster than official docs

Risk:

A detailed 2024 tutorial may be highly practical but unusable in 2026.

Correction:

Separate:

- stable workflow insight;
- volatile setup fact.

Keep the workflow insight if still transferable, but re-check volatile setup against current original sources.

## 10. Attack: source strategy can overshadow the original product goal

Risk:

The Agent may spend more time proving source quality than finding something genuinely worth sending to an ERP colleague.

Correction:

Final test remains:

> **Would I directly send this package to a colleague because it saves them search/learning time and helps them act?**

If not, source diversity and citation completeness do not rescue the result.

## Decision

Keep the mixed-source direction, but revise the draft before use:

1. evidence-role classification, not site hierarchy;
2. no mandatory platform coverage;
3. original content must be actually readable before recommendation;
4. no numeric community-source gate;
5. default 0–1 practical companion;
6. one falsification/counter-evidence habit for meaningful adoption decisions;
7. shareability/actionability remains the final criterion.
