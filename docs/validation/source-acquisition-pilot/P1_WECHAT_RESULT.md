# P1 — WeChat Lightweight Qualification Result

**Date:** 2026-08-31
**Runtime:** curating-erp-ai-resources 0.9.1 (frozen)
**Branch:** validation/source-acquisition-pilot-local
**Adapter:** zjp1997720/wechat-article-search
**Pinned commit:** 7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6
**Agent host:** TRAE (local Agent, Windows, Node.js v22.16.0)

## 1. Pre-installation inspection

### 1.1 SKILL.md

- **Name:** wechat-article-search
- **Version:** 0.1.0
- **Allowed tools:** Bash, Read
- **Description:** Search WeChat public-account articles by keyword via Sogou WeChat Search. Returns title, URL, summary, publish datetime, source account name.
- **Operations:** Search, metadata extraction, optional URL resolution, optional file output.
- **No publish/comment/like/favorite/follow/message/upload capabilities.**

### 1.2 package.json

```json
{
  "name": "wechat-article-search",
  "version": "0.1.0",
  "private": true,
  "description": "搜索微信公众号文章（搜狗微信搜索），deepsight_vault skill 内嵌依赖",
  "dependencies": {
    "cheerio": "^1.0.0"
  }
}
```

- Single npm dependency: `cheerio` (HTML parser).
- No other runtime dependencies.
- `npm install` reported 1 high severity vulnerability (cheerio transitive dependency); non-blocking for a read-only pilot in a temp directory.

### 1.3 scripts/search_wechat.js — full inspection (463 lines)

**Network targets:**
| Target | Purpose |
|---|---|
| `weixin.sogou.com` | Primary search endpoint (Sogou WeChat Search) |
| `v.sogou.com` | Cookie acquisition (anti-bot session initialization) |
| `mp.weixin.qq.com` | URL resolution target (only with `-r` flag, via redirect following) |

**Dependencies:**
- Node.js built-in: `https`, `zlib`
- npm: `cheerio`

**File writes:**
- Only when `-o` flag is used: writes JSON to a user-specified file path.
- Default: stdout only. No other file system writes.

**Capabilities confirmed:**
- Keyword search: YES
- Metadata extraction: YES (title, URL, summary, publish datetime, source account)
- URL resolution: YES (optional `-r` flag, converts Sogou redirect to mp.weixin.qq.com direct link)
- Publish/comment/like/favorite/follow/message/upload: NO — none of these exist in the script
- The script makes only HTTP GET requests. No POST/PUT/DELETE.

**Security assessment:**
- No API keys, no user credentials, no login required.
- The script uses a pool of 20 User-Agent strings rotated per request — standard anti-bot evasion, not a user security risk.
- It extracts cookies from Sogou responses and reuses them for session continuity — standard web scraping practice, no credential storage.
- A hardcoded base cookie string (`ABTEST=...; IPLOC=CN5101; ...`) is used for URL resolution — this is a Sogou search session cookie, not a user credential.
- No data exfiltration: the script only connects to Sogou and mp.weixin.qq.com.
- The `-r` URL resolution has built-in rate limiting (500ms + random 1000ms delay between requests).

**Conclusion:** Safe to install and execute. Operations are search/metadata/URL-resolution only. No write/social capabilities. No credential handling. Installation is proportionate to the pilot scope.

### 1.4 Installation

- Downloaded GitHub archive zip of pinned commit `7e1be9a0` to `%TEMP%\wechat-article-search-pilot`.
- Extracted and ran `npm install` in the skill directory.
- Dependency `cheerio` installed successfully (23 packages).
- No adapter binaries or credentials committed to the project repository.

## 2. Search execution

### Search 1: "AI 流程图" (-n 10)

- **Results:** 10 articles returned.
- **Key candidates (not in P0 pool):**

| # | Title | Source | Date | Serious? |
|---|---|---|---|---|
| 1 | 终于有人,把 AI 画的流程图救回来了 | AI 趋势老王 | 2026-08-19 | Yes — direct AI flowchart practice |
| 2 | AI做流程图 3分钟画出专业流程图 | 普通人的AI应用笔记 | 2026-08-23 | Yes — tutorial with methods |
| 3 | AI时代,流程管理从业者的挑战与机遇 | 案头随笔 | 2026-08-30 | Yes — process management + AI, ERP-adjacent |
| 4 | 流程图AI生成常见问题解答+7款工具推荐 | 嗨少大呲花 | 2026-03-02 | Yes — tool comparison |
| 5 | 2026升职快人一步:3类人用AI流程图甩开PPT内卷 | 贝尔康智能生活馆 | 2026-02-19 | Borderline — workplace angle |

### Search 2: "AI draw.io 流程图" (-n 10)

- **Results:** 10 articles returned.
- **Key candidates (not in P0 pool):**

| # | Title | Source | Date | Serious? |
|---|---|---|---|---|
| 1 | 告别手动画流程图!AI 一句话生成,直接拿到 draw.io 源文件 | 图叙AI | 2026-08-18 | Yes — detailed tool review with deployment options |
| 2 | 我做了一个 draw.io AI 侧边栏:边聊边画流程图 | 过拟合人 | 2026-08-20 | Yes — practitioner building a Chrome extension |
| 3 | 用AI画业务流程图draw.io | 产品经理一二AI学习 | 2026-08-28 | Yes — product manager perspective, business flowchart |
| 4 | 为什么AI画图不该只给你一张图片 | AC技术与生活 | 2026-08-31 | Yes — argues for editable XML over static images |
| 5 | 实用工具系列:AI生成draw.io流程图完全教程 | 孤海游人 | 2026-02-27 | Yes — complete tutorial |
| 6 | 狂揽24k Star \| AI生成可编辑Draw.io技术路线图 | 植物功能生态 | 2026-03-23 | Yes — covers open-source project with 24k stars |

### Search 3: "AI 画流程图 工具 最佳实践" (-n 10)

- **Results:** 10 articles returned.
- **Key candidates (not in P0 pool):**

| # | Title | Source | Date | Serious? |
|---|---|---|---|---|
| 1 | 流程再造(BPR)与最佳实践在银行业AI创新中的"地基"作用 | 中长期项目专家咨询 | 2026-08-25 | Yes — BPR + AI in banking, ERP-adjacent |
| 2 | 怎么用Mermaid代码生成流程图?AI在线绘图实战指南 | AIPPT工具箱 | 2026-02-04 | Yes — Mermaid practice guide |
| 3 | AI工具在研发流程中的最佳实践 | 微盟技术中心 | 2023-10-31 | Borderline — older, but enterprise perspective |
| 4 | 国内首个全流程体系生产工具:企业流程架构智能生成系统 | AI流程布道师 | 2026-03-28 | Borderline — vendor/promotional |

### URL resolution test (-r flag, 5 articles)

- **Resolution success rate:** 5/5 (100%)
- All Sogou redirect URLs successfully resolved to real `mp.weixin.qq.com` direct links.

## 3. Original content readability test

Two resolved URLs were fetched via WebFetch to test whether original article content is readable:

### Article 1: "我做了一个 draw.io AI 侧边栏:边聊边画流程图" (过拟合人, 2026-08-20)

- **URL:** `https://mp.weixin.qq.com/s?src=11&timestamp=...`
- **Readable?** YES — full article text returned.
- **Content quality:** High. Practitioner describes building a Chrome extension (Draw.io AI Sidebar) that integrates AI into draw.io. Covers: motivation (XML copy-paste friction), implementation (natural language → XML → canvas injection → screenshot feedback → version control), installation steps, model configuration, and honest limitations ("AI is auxiliary, judgement remains in your hands").
- **Relevance to task:** Directly demonstrates a concrete AI + draw.io workflow with input → operation → output evidence.

### Article 2: "告别手动画流程图!AI 一句话生成,直接拿到 draw.io 源文件" (图叙AI, 2026-08-18)

- **URL:** `https://mp.weixin.qq.com/s?src=11&timestamp=...`
- **Readable?** YES — full article text returned.
- **Content quality:** High. Covers Next AI Draw.io open-source project (GitHub: DayuanJiang/next-ai-draw-io). Details: 6 core features (natural language generation, image-to-diagram, PDF-to-diagram, version history, cloud architecture support, animation connectors), 4 deployment modes (online demo, desktop app, Docker, cloud), MCP Server integration for Claude/Cursor/VS Code, model support (14+ providers), and 3 prompt templates.
- **Relevance to task:** Comprehensive practitioner review of an AI flowchart tool with reproducible deployment instructions and prompt templates.

## 4. Measurement

### 4.1 Does the adapter return relevant WeChat practitioner candidates P0 did not expose?

**YES.** The adapter returned 30 unique WeChat articles across 3 searches. P0's `site:mp.weixin.qq.com` queries returned zero results. All 30 candidates are completely new to the pool. At least 10 are serious practitioner candidates with direct relevance to the "AI flowchart best practices" task, including perspectives from product managers, process management consultants, and tool builders.

### 4.2 Can serious candidates be resolved/opened sufficiently for judgement?

**YES.** URL resolution succeeded for 5/5 tested articles (100%). WebFetch successfully read full article content for 2/2 tested resolved URLs. The articles returned complete, structured text with concrete workflow details, tool recommendations, and prompt templates — sufficient for Curator-level judgement.

### 4.3 Does the adapter add a candidate or evidence that could materially change the final recommendation?

**YES.** The adapter exposed evidence that materially changes the candidate pool:

1. **Practitioner tool-building perspective** (过拟合人 — Chrome extension integrating AI into draw.io) — not found in P0's juejin/CSDN pool.
2. **Product manager business-flowchart perspective** (产品经理一二AI学习 — using AI for business process flowcharts with desensitized real project examples) — ERP/ToB relevant.
3. **Process management + AI perspective** (案头随笔 — AI era challenges for process management practitioners; 中长期项目专家咨询 — BPR + AI in banking) — directly ERP-adjacent.
4. **Open-source project with MCP Server integration** (Next AI Draw.io — 24k stars, Claude/Cursor integration) — a deployment path not surfaced in P0.
5. **Very fresh content** (multiple articles from 2026-08-18 to 2026-08-31, including one published 4 hours before the search) — recency that broad Web search did not expose.

This evidence would add at least 2-3 new serious candidates to the final Curator recommendation and could change the ranking by introducing the product-manager and process-management perspectives that were absent from the P0 pool.

## 5. Security and maintenance cost

- **Security risk:** Low. No credentials, no API keys, no login. Read-only HTTP GET to Sogou and mp.weixin.qq.com. No social/write capabilities.
- **Maintenance cost:** Low. Single npm dependency (cheerio). No ongoing credential management. Anti-bot rate limiting is handled by the script (UA rotation, cookie extraction, rate-limited URL resolution).
- **Known limitations:**
  - Sogou anti-bot may intermittently return empty results — retry with different keywords or wait.
  - URL resolution (`-r`) may fail under aggressive anti-spider policy — in this test it succeeded 5/5, but this is not guaranteed.
  - The adapter searches via Sogou WeChat Search, not the WeChat API — coverage depends on Sogou's indexing of WeChat articles.

## 6. Proposed status

**APPROVED**

Rationale: The adapter meets all four success criteria:
1. It acquires practitioner evidence normal Web could not reliably acquire (30 articles vs 0 from site: queries).
2. Original-content provenance is sufficient to inspect the practice (full article text readable via WebFetch after URL resolution).
3. The acquired evidence changes material decisions: new candidate pool, new perspectives (product manager, process management, tool builder), fresh content.
4. Acquisition cost/security/maintenance remains proportionate (no credentials, low maintenance, single dependency).
