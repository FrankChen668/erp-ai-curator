# ERP AI Curator — Source Strategy V3

> Current discovery-source strategy for testing. The goal is not to maximize source diversity; it is to combine **current factual anchors** with **practical, reproducible usage evidence** for generalized ERP / enterprise-information-system practitioners.

## 1. Core principle

A useful recommendation usually needs to answer two different questions:

1. **Can this capability actually be used now, under the user's constraints?**
2. **How does a practitioner use it well in real work?**

Different sources may answer different parts.

- Official/original material is normally the preferred fact anchor for native capability, current setup, versions, compatibility, APIs, pricing/license and policy/security claims.
- Practitioner/community material is often stronger for workflows, prompts, examples, failure modes, adoption friction, comparison and real usage experience.

But there is no universal source hierarchy.

> **Judge each source by the evidence role it plays and the value it adds to the user's decision. Official does not mean automatically useful; community does not mean automatically practical.**

## 2. Classify by evidence role, not website

A source may play one or more roles:

### Fact anchor
Used to verify volatile/native claims such as capability, installation, version, compatibility, API, pricing, license, privacy or standard-product boundary.

Typical sources: official docs, release notes, original repo/docs.

### Original implementation artifact
The actual Tool / Skill / MCP / repository / demo being evaluated.

Typical sources: official or personal GitHub repositories, product demos, author documentation.

### Practitioner guide / field note
Shows how somebody actually used the method.

Typical sources: WeChat public-account articles, Xiaohongshu posts, Bilibili/YouTube videos, Zhihu, Juejin, CSDN, personal blogs, implementation notes.

### Independent comparison / counter-evidence
Helps expose trade-offs, failures, maintenance problems or compatibility limits.

Typical sources: comparative reviews, GitHub issues/discussions, negative field reports, independent benchmarks.

### Secondary / aggregation
Useful for discovery only unless the original source cannot be found and the content itself is sufficiently complete and attributable.

Examples: reposts, link collections, AI summaries, aggregation pages.

Do not equate platform with evidence role. A GitHub repo may be official, original implementation and practitioner evidence at the same time.

## 3. Search behavior

When Mode B requires external discovery:

1. define the capability gap first;
2. find enough original/current evidence to understand what the candidate actually does;
3. when practical adoption matters, deliberately look for practitioner evidence showing how it behaves in real use;
4. for non-trivial adoption decisions, make one falsification pass for limitations, issues, failed attempts, maintenance or compatibility caveats;
5. compare candidates by complete task fit, evidence and adoption value, not by source prestige;
6. stop when another search is unlikely to change the recommendation or materially help the user act.

This is **not** a platform-coverage checklist.

Do not search WeChat, Xiaohongshu, Bilibili, GitHub and official sites merely to prove diversity. Search a source class because it can resolve a real uncertainty.

## 4. Original-content rule

A source cannot become a recommended practical companion based only on:

- search snippet;
- AI-generated summary;
- repost title;
- engagement count;
- screenshot seen out of context.

The Agent must actually open/read the original post, article, transcript, repository, video transcript/notes, or sufficiently complete primary material.

If a platform is inaccessible because of login, dynamic rendering or tool limitations:

> **report the coverage gap; do not invent or infer the unseen content.**

## 5. Practitioner evidence heuristics

There is no numeric Gate.

A practitioner/community source becomes interesting when it gives enough concrete evidence that another practitioner can **learn, reproduce or judge** the method.

Strong signals include:

- real operating steps;
- screenshots / demo / code / prompt / output;
- clear input and result;
- specific failure modes or limitations;
- comparison with another method;
- reproducible setup or example;
- evidence of actual project use;
- useful follow-up discussion or maintenance history.

Confidence drops when the content is mainly:

- repost / aggregation;
- generic AI summary;
- promotional copy without real operation;
- polished outcome with no process evidence;
- stale configuration with no date/version context;
- copied screenshots without explanation.

Popularity, likes, followers, stars and repost count are weak discovery signals only.

## 6. Chinese-source policy

Chinese practitioner content can be especially valuable because it reduces adoption cost for internal ERP users.

When practical quality is comparable, prefer Chinese content.

But language convenience cannot override:

- factual errors;
- outdated setup;
- weak evidence;
- obvious marketing;
- mismatch with the task.

A strong package may therefore be:

> **English original implementation / official fact anchor + Chinese practitioner guide.**

## 7. Stable insight vs volatile fact

A practical article may be old but still contain a useful workflow pattern.

Separate:

- **stable insight**: workflow, prompt structure, adoption lesson, failure pattern;
- **volatile fact**: version, endpoint, model support, installation command, pricing, current native capability.

Stable insight can remain useful if transferable.

Volatile facts must be rechecked against a current original/official source before being presented as current truth.

## 8. Preferred recommendation package

Avoid a flat link list.

Default package:

### Main recommendation
The Tool / Skill / method actually worth adopting.

### Fact anchor — only when useful
A current official/original source confirming the facts that matter.

### Practical companion — default 0–1
One practitioner resource that materially helps the user get value from the main recommendation.

### Second solution — only when meaningfully different
Use only when it solves a different capability boundary or user condition.

The fact anchor and practical companion support the main recommendation; they do not automatically consume separate recommendation slots.

More links require explicit user request or clear incremental value.

## 9. Falsification habit

Before confidently recommending a non-trivial Tool / Skill / workflow, deliberately look once for evidence that could change the decision:

- known limitations;
- unresolved issues;
- failed attempts;
- maintenance inactivity;
- privacy/security concern;
- compatibility caveat;
- evidence that the existing toolchain already does the same job.

This is a judgment habit, not a fixed query count or Gate.

## 10. Success test

The source strategy is working when the final package answers:

> **What should I use? Why should I trust this decision? How do I actually get value from it? What are the real limitations?**

And the practical Owner test remains:

> **Would I directly send this package to a colleague because it saves them search/learning time and helps them act?**

Source diversity, official citations and link count do not rescue a package that fails that test.
