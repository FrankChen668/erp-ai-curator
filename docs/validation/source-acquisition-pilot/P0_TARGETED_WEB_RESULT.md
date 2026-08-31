# P0 — Targeted Normal-Web Baseline Result

**Date:** 2026-08-31
**Runtime:** curating-erp-ai-resources 0.9.1 (frozen)
**Branch:** validation/source-acquisition-pilot-local
**Agent host:** TRAE (local Agent, Windows)

## 0. Context

Fresh Agent context. Runtime 0.9.1 confirmed loaded from `skills/curating-erp-ai-resources/SKILL.md`.

Natural task used:

> 使用 curating-erp-ai-resources skill 给我找下做流程图的最佳实践

No repository validation/history URLs were used as candidate sources.

## 1. Normal broad discovery (baseline)

Before running site-qualified queries, the Agent executed broad discovery in a prior turn of the same natural task. The following source classes appeared:

### Queries executed

| # | Query | 
|---|-------|
| B1 | `用 AI 画流程图 实践 教程 ChatGPT Claude 工作流 2026` |
| B2 | `AI generate flowchart best practices practitioner workflow Mermaid draw.io 2026` |
| B3 | `AI 流程图 生成 实战案例 掘金 CSDN 知乎 从业者` |

### Broad discovery result pool

| Source class | Candidates found | Opened/read? | Serious? |
|---|---|---|---|
| juejin.cn (掘金) | 3 | Yes — full article text readable via WebFetch | Yes |
| blog.csdn.net (CSDN) | 4+ | Yes — full article text readable via WebFetch | Yes (mixed quality) |
| 51cto.com | 1 | Not opened (snippet sufficient for classification) | Borderline |
| toutiao.com | 1 | Not opened (snippet sufficient for classification) | Borderline |
| bilibili.com | 0 | — | — |
| zhihu.com | 0 | — | — |
| mp.weixin.qq.com | 0 | — | — |
| xiaohongshu.com | 0 | — | — |

**Observation:** Broad discovery found juejin and CSDN but did not surface Bilibili, Zhihu, WeChat public-account, or Xiaohongshu practitioner content.

## 2. Targeted normal-Web recall (site-qualified queries)

The task requires exercising targeted recall when Chinese practitioner ecosystems are absent from the broad pool.

### Queries executed

| # | Query | Results returned |
|---|-------|----------------|
| T1 | `site:bilibili.com AI draw.io 流程图 产品经理 ERP` | 1 |
| T2 | `site:zhihu.com AI draw.io 流程图 产品经理 ERP` | 0 |
| T3 | `site:mp.weixin.qq.com AI draw.io 流程图 产品经理 ERP` | 0 |
| T4 | `site:xiaohongshu.com AI draw.io 流程图 产品经理 ERP` | 0 |
| T5 | `site:zhihu.com AI 流程图 工具 最佳实践` | 0 |
| T6 | `site:mp.weixin.qq.com AI 流程图 生成 工具` | 0 |
| T7 | `site:xiaohongshu.com AI 流程图 工具` | 0 |

### Per-source-class detail

#### Bilibili

- **Actual query:** `site:bilibili.com AI draw.io 流程图 产品经理 ERP`
- **Top candidate:**
  - Title: 【🚀AI画图新革命！Gemini 3 + Draw.io 联动，一键生成可编辑流程图】
  - URL: https://www.bilibili.com/video/BV1bDywBAEp2/
  - Author: acmakb (space.bilibili.com/501866357)
  - Publication date: 2025-11-20
  - Views: 4037; Likes: 47; Coins: 8; Favorites: 158
- **Original content opened?** Yes — WebFetch successfully retrieved the video page. The page returned video title, description, tags, author info, and a recommendation list of 18 related videos.
- **What was readable:** Video description (workflow: Gemini 3 → Mermaid code → Draw.io import → edit), tool links, applicable scenarios (毕业设计, 工作汇报, 项目开发, 业务流程). Tags: AI, 科技前沿, 科研必备, 谷歌AI, 流程图, 办公技巧, Gemini3.
- **What was NOT readable:** Video transcript/subtitles are not available via normal Web fetch. Only metadata and description.
- **Serious enough to inspect further?** Borderline — the description shows a concrete workflow (Gemini 3 → Mermaid → Draw.io), but the video format means the actual practice detail is in the video content, not the page text. Without transcript, judgement relies on title/snippet only.
- **Related videos discovered via recommendation list (not from search, but from page fetch):**
  - BV1PM5JzSEQx — "AI+drawio+提示词一键生成高质量图" (2.9万 views)
  - BV1SZ421n7Cm — "用Kimi+drawio，10秒生成流程图，支持再编辑" (8.0万 views)
  - BV1cEj3zZEuy — "DeepSeek + mermaid 轻松搞定各种流程图" (1.1万 views)
  - BV1xyNfe1EKP — "deepseek+draw.io绘制流程图" (7.8万 views, 28 coins)
  - BV1jmLfzJEft — "原来Claude+Visio才是终极画图王炸！" (1.0万 views)
  - BV1ysL1zoEGH — "mermaid加Claude一键生成美观高级的流程图" (7126 views)
- **Access/indexing limitation:** Bilibili video pages are fetchable (metadata + description), but transcript/subtitle content is not accessible via normal Web. The recommendation list is a bonus discovery channel but is not search-indexed.
- **Acquisition state:** `WEB_DISCOVER_AND_READ` (metadata/description readable; transcript not accessible via normal Web)

#### Zhihu

- **Actual queries:**
  - `site:zhihu.com AI draw.io 流程图 产品经理 ERP` → 0 results
  - `site:zhihu.com AI 流程图 工具 最佳实践` → 0 results
- **Top relevant candidates:** None returned.
- **Original content opened?** N/A — no candidates returned.
- **Publication/update date:** N/A.
- **Serious enough to inspect further?** N/A.
- **Access/indexing limitation:** The WebSearch backend returned zero results for both site:zhihu.com query forms. This may indicate either (a) the search engine does not sufficiently index zhihu.com content for these query terms, or (b) no matching content exists on Zhihu for this specific topic. Cannot distinguish between these two causes from search alone.
- **Acquisition state:** `WEB_NO_USEFUL_RECALL`

#### WeChat public-account (mp.weixin.qq.com)

- **Actual queries:**
  - `site:mp.weixin.qq.com AI draw.io 流程图 产品经理 ERP` → 0 results
  - `site:mp.weixin.qq.com AI 流程图 生成 工具` → 0 results
- **Top relevant candidates:** None returned.
- **Original content opened?** N/A — no candidates returned.
- **Publication/update date:** N/A.
- **Serious enough to inspect further?** N/A.
- **Access/indexing limitation:** The WebSearch backend returned zero results for both site:mp.weixin.qq.com query forms. WeChat articles are hosted on a semi-closed ecosystem; search engines are known to have limited indexing of mp.weixin.qq.com content. Sogou WeChat Search is the primary external discovery path for WeChat articles, but it is not available through the normal WebSearch tool.
- **Acquisition state:** `WEB_NO_USEFUL_RECALL`

#### Xiaohongshu

- **Actual queries:**
  - `site:xiaohongshu.com AI draw.io 流程图 产品经理 ERP` → 0 results
  - `site:xiaohongshu.com AI 流程图 工具` → 0 results
- **Top relevant candidates:** None returned.
- **Original content opened?** N/A — no candidates returned.
- **Publication/update date:** N/A.
- **Serious enough to inspect further?** N/A.
- **Access/indexing limitation:** The WebSearch backend returned zero results for both site:xiaohongshu.com query forms. Xiaohongshu is a closed ecosystem with limited search-engine indexing. Content discovery typically requires the platform's own search or an API/adapter.
- **Acquisition state:** `WEB_NO_USEFUL_RECALL`

## 3. P0 decision facts

| Source class | Acquisition state | Rationale |
|---|---|---|
| Bilibili | `WEB_DISCOVER_AND_READ` | Site: query returned 1 candidate; WebFetch read page metadata, description, tags, and recommendation list. Transcript not accessible via normal Web. |
| Zhihu | `WEB_NO_USEFUL_RECALL` | Two site: query forms returned zero results. |
| WeChat (mp.weixin.qq.com) | `WEB_NO_USEFUL_RECALL` | Two site: query forms returned zero results. Semi-closed ecosystem; limited search-engine indexing. |
| Xiaohongshu | `WEB_NO_USEFUL_RECALL` | Two site: query forms returned zero results. Closed ecosystem; limited search-engine indexing. |

## 4. Summary

- Normal broad discovery reliably finds juejin and CSDN practitioner content.
- Bilibili is discoverable via site: queries and page metadata is readable via WebFetch, but video transcripts are not accessible through normal Web — this limits judgement to title/description level.
- Zhihu, WeChat, and Xiaohongshu return zero results from site-qualified normal-Web queries, indicating a real acquisition gap for these ecosystems.
- The gap is most severe for WeChat and Xiaohongshu (closed ecosystems with limited search-engine indexing), and less clear for Zhihu (may be a query-term mismatch rather than a total indexing gap).

## 5. P0 → P1/P2/P3 gate

- **WeChat:** `WEB_NO_USEFUL_RECALL` → P1 qualification is warranted if WeChat evidence could plausibly affect the recommendation.
- **Bilibili:** `WEB_DISCOVER_AND_READ` (metadata only, no transcript) → P2 qualification is warranted to test whether transcript-level evidence changes judgement versus title/snippet-only.
- **Xiaohongshu:** `WEB_NO_USEFUL_RECALL` → P3 deferred until P0–P2 decision stability is assessed.
- **Zhihu:** No dedicated adapter in the first pilot. Monitor in final comparison.

No final Curator recommendation is produced at this stage, per Runbook.
