# Source Adapter Routing Result 01 — WeChat

Date: 2026-08-29

## Test objective

Verify whether Curator-style evidence need can cause local Codex to compose two already-installed source capabilities in one task:

`wechat-article-search → wechat-article-reader`

without manual URL relay, unrelated adapter use, or search-snippet substitution.

## Result

**PASS**

Actual chain observed:

```text
Curator evidence need: Chinese practitioner evidence for process interviews / As-Is / To-Be
→ normal Web judged insufficient for practitioner detail
→ wechat-article-search
→ 5 real public-account candidates + direct mp.weixin.qq.com links
→ wechat-article-reader on one candidate in the same task
→ original article body + metadata obtained
→ Curator judged practical value
→ stopped
```

Unrelated Bilibili/Xiaohongshu adapters were not invoked.

## Original-content evidence

Article:

`AI大模型，是流程建设的“神助攻”吗？`

Account / author:

`流程进修`

Date:

`2026-03-02`

Reader observation:

- HTTP 200;
- `ok=true`;
- approximately 3,244 characters;
- `verification_page=false`;
- actual body content was distinguished from search summary.

Practical evidence obtained from the article included:

- interview recording → text → key-step extraction;
- business description → draft process diagram;
- FAQ / SOP wording support;
- explicit cautions on private deployment/input boundaries, prompt quality and expert review.

The article did not provide complete enterprise project data or a reusable As-Is/To-Be template.

## What this proves

Supported:

- local Codex can compose the two installed WeChat Skills in one task;
- Curator-style evidence need can trigger source-specific acquisition conditionally;
- the workflow can preserve provenance and distinguish discovery snippets from original evidence;
- unrelated adapters can remain unused;
- the chain can stop once the evidence need is satisfied.

Not proven:

- arbitrary Skill-to-Skill orchestration;
- Bilibili/Xiaohongshu routing;
- that adapter evidence improves final curation enough to justify permanent architecture;
- that a production Curator Skill is needed;
- independent-user value.

## Product implication

The bounded Curator / Orchestrator hypothesis is **supported for the WeChat discovery → original-reader chain**.

The next uncertainty is no longer routing feasibility. It is **incremental user value**:

> Does adding this qualified source capability materially improve the final resource recommendation compared with normal Web/GitHub discovery alone?

That question is tested in Phase 4 with a fresh paired A/B curation task.
