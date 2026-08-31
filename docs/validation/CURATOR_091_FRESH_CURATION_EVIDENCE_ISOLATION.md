# Curator 0.9.1 — Fresh Curation / Evidence Isolation

Date: 2026-08-31
Status: **REAL CONTROLLED-USE DEFECT — PATCH IMPLEMENTED / HOST RE-RUN REQUIRED**

## 1. Trigger

After Runtime 0.9.0 split practice curation from capability adoption, the same natural flowchart request improved materially: it stopped recommending a Skill installation and returned practitioner-style resources.

However, the Local Agent execution log showed that the apparent improvement was partly produced by **reusing this repository's historical P04 validation result**, not by completing a fresh independent curation run.

Observed user-facing answer retained:

- two `woshipm.com` articles;
- `Castaldo-Solutions/process-builder`;
- an internal link to `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`.

## 2. What the execution log directly proves

The run executed one Web Search call containing four broad queries:

1. `AI draw.io 可编辑 流程图 实战 顾问 产品经理 工作流`
2. `Claude Code draw.io editable flowchart practitioner workflow tutorial`
3. `AI generated flowchart import draw.io editable workflow review iteration`
4. `ERP consultant AI editable business process diagram draw.io BPMN workflow`

The merged Web results contained official draw.io material, GitHub implementations, Note/independent blogs, DevelopersIO, Reddit, papers and other candidates.

But:

- no targeted Bilibili, WeChat, Xiaohongshu or Zhihu discovery was executed;
- the two final `woshipm.com` resources were not discovered by the current Web Search;
- those two URLs were found by local repository `rg` from historical validation material, then opened directly;
- `Castaldo-Solutions/process-builder` was also taken from the historical P04 validation record and was **not reopened in this run**;
- the final answer exposed the internal P04 validation file to the user;
- there was no current Web access failure, login failure, anti-bot error or host-policy error explaining the lack of targeted Chinese practitioner discovery.

## 3. First-principles diagnosis

The defect is not primarily "missing Xiaohongshu".

It has three more general causes.

### 3.1 Historical evidence contamination

A normal user curation run allowed this repository's prior validation result to seed the candidate pool and ranking.

That creates a self-confirming loop:

```text
previous project recommendation
→ local repo search finds the old recommendation
→ current run reuses the same URLs/order
→ current answer appears to confirm the previous recommendation
```

Historical project evidence is useful for engineering diagnosis and regression, but it is not independent current practitioner evidence.

### 3.2 Freshness was not an explicit selection dimension

AI work practices, Agent/Skill ecosystems and tool capabilities change quickly. The current Runtime checked fit and practitioner evidence but did not force a fresh look at recent/current alternatives.

A previous recommendation can remain correct, but that must be re-established against current candidates rather than inherited.

### 3.3 Broad-search recall bias

The broad query batch did not surface the user's obvious Chinese practitioner ecosystems. Because no targeted follow-up was required, the run stopped before correcting search-engine/indexing bias.

This is different from requiring every platform in every answer.

## 4. Cloud adversarial sanity check

A fresh targeted Web check on 2026-08-31 immediately surfaced recent candidates that were absent from the Local Agent's current candidate pool, including:

- Bilibili, 2026-07-18: `〖5.9K Star 神器 drawio-skill〗版本大升级 更专业 更全面 更优秀`;
- 人人都是产品经理, 2026-06-23: `我是怎么使用 CodeX 把“仓库盘点脑图”，一步步做成可导入飞书的流程图的？` — explicitly framed around supply-chain/WMS product work and Draw.io XML/swimlane output;
- Bilibili, 2026-04-23: `这个 AI 画图技能，居然能从一张图学会你的审美？ drawio-skill重磅更新`.

This does **not** prove these candidates should replace the retained P04 recommendations. It proves that fresh discovery can materially change the serious candidate pool and therefore cannot be skipped.

## 5. 0.9.1 correction

Practice Curator now requires:

1. **fresh external discovery** for normal external curation requests;
2. project validation/history/prior packs are leads only and cannot determine the current ranking;
3. every final external recommendation is freshly opened/read in the current run unless the user explicitly asks to reuse prior curation;
4. fast-changing AI workflows include freshness-aware discovery and currentness checks;
5. broad Web search that misses the user's obvious practitioner ecosystem triggers a targeted recall pass on the one/few pools most likely to change the answer;
6. internal validation/history is not surfaced as user-facing external evidence unless the user explicitly asks about project evidence/history.

## 6. Adversarial review

### Not a platform quota

0.9.1 does not require Bilibili + WeChat + Xiaohongshu + Zhihu in every run. Targeted platform search only compensates when broad discovery clearly misses the user's likely ecosystem.

### Not newest-wins

Newer content is not automatically better. Older high-quality practitioner evidence may remain first when it is more direct, reproducible and task-matched.

### Not a resource database/refresh system

0.9.1 does not build a crawler, cache, scheduled refresh pipeline or permanent ranking database. Freshness is evaluated inside the user's actual current request.

### Not a ban on historical project evidence

Historical evidence remains valuable for product research, regression and engineering decisions. It is simply separated from current external recommendation evidence.

## 7. Evidence boundary

The Local Agent log supports the defect diagnosis and the need for evidence isolation/fresh discovery.

The Cloud targeted search supports only this narrower conclusion:

> the current candidate pool had omitted materially recent candidates, so historical recommendation stability could not be assumed.

Neither proves 0.9.1 works in the Local Agent host or that ERP AI Curator has validated product value.

## 8. Next evidence

After syncing 0.9.1, run the same natural practice request in a fresh host context.

Observe only normal behavior:

- does current external discovery happen before historical project evidence can influence ranking?;
- when broad search misses obvious Chinese practitioner pools, does targeted recall occur?;
- are all final external recommendations freshly opened?;
- are publication/update/currentness signals considered where material?;
- does the final user answer avoid internal validation files unless explicitly requested?

If this still fails, collect actual search/open/source logs before changing Runtime again.
