# ERP AI Curator — Source Acquisition Pilot 2026-08-31

Status: **ACTIVE PILOT — RUNTIME 0.9.1 FROZEN**

## 1. Trigger

Repeated real executions across more than one Agent host show the same pattern:

- broad Web search can find official docs, GitHub, CSDN, general blogs and some practitioner pages;
- it often does not surface Xiaohongshu / WeChat public-account / Bilibili practitioner content unless the source is already known or a platform-specific path is used;
- the 0.9.0 diagnostic run executed no targeted WeChat/Xiaohongshu/Zhihu/Bilibili discovery;
- a separate Agent run on 2026-08-31 again used broad queries and similarly failed to surface Xiaohongshu / WeChat / Zhihu content.

This cross-host repetition raises the root cause from a single Skill-execution defect to a likely **source-acquisition / search-index coverage gap**.

Runtime 0.9.1 already contains targeted-recall instructions. Do not keep adding more search wording until acquisition paths are tested.

## 2. First-principles hypothesis

The product value chain is:

```text
real user task
→ discover serious practitioner candidates
→ acquire enough original content
→ compare / verify / select
→ return 1–3 high-value resources
```

If the discovery/acquisition layer cannot see important Chinese practitioner ecosystems, better ranking logic cannot recover missing evidence.

Therefore the next question is not:

> Can we add another rule telling the Agent to search Xiaohongshu?

It is:

> Which minimum acquisition capability materially improves the serious candidate pool and final recommendation, at acceptable security and maintenance cost?

## 3. Existing architecture reused

Authorities:

- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

The Curator remains the judgement layer. Source adapters are read-only evidence-acquisition dependencies, not recommenders and not mandatory platform quotas.

## 4. Staged pilot

### P0 — targeted Web baseline, no new dependency

Use a fresh local Agent context and the same natural task:

> 使用 curating-erp-ai-resources skill 给我找下做流程图的最佳实践

After the normal broad search, if Chinese practitioner ecosystems are absent, explicitly exercise normal-search targeted recall with a small set of source-qualified queries. Example forms:

```text
site:bilibili.com AI draw.io 流程图 产品经理 ERP
site:zhihu.com AI draw.io 流程图 产品经理 ERP
site:mp.weixin.qq.com AI draw.io 流程图 产品经理 ERP
site:xiaohongshu.com AI draw.io 流程图 产品经理 ERP
```

Do not force all four if the host/search tool makes some obviously unproductive. The purpose is to distinguish:

- Agent failed to issue targeted queries;
- search engine does not index/return the platform sufficiently;
- candidate is discoverable but original content cannot be read.

Record only search/open facts; do not modify Runtime 0.9.1 during P0.

### P1 — WeChat lightweight discovery qualification

Candidate: `zjp1997720/wechat-article-search`.

Current observed facts on 2026-08-31:

- public MIT repository;
- keyword search through Sogou WeChat Search;
- no API key;
- Node.js 18+;
- discovery-oriented; direct URL resolution may fail under Sogou anti-bot.

Qualification scope:

- inspect the pinned source before install;
- install in the local pilot environment only;
- allow keyword search / metadata / URL resolution only;
- do not mass crawl;
- use the same flowchart task to see whether it yields serious practitioner candidates unavailable in P0.

### P2 — Bilibili search/transcript qualification

Candidate: `XZXZZX-Ai/bilibili-mcp`.

Current observed facts on 2026-08-31:

- active Apache-2.0 repository;
- supports topic search, video metadata, subtitles/transcripts and selected comments;
- local MCP; some functions require local credentials/login;
- optional local ASR is not required for the first pilot.

Qualification scope:

- search + metadata + transcript only;
- no social interaction actions;
- credentials/cookies remain local and must never be pasted into Agent chat or committed;
- Owner/manual action is allowed only when credential setup or client restart genuinely requires it;
- compare whether full transcript evidence changes the candidate judgement versus title/snippet-only Web results.

### P3 — Xiaohongshu isolated read-only qualification

Candidate: `xpzouying/xiaohongshu-mcp`.

Current observed facts on 2026-08-31:

- active Apache-2.0 repository, large active user base;
- search and post-detail capabilities exist;
- login is required for meaningful detail access;
- the project also exposes publishing/comment/social actions, so it has materially higher permission and maintenance risk.

P3 is intentionally after P0–P2.

Qualification scope:

- use a low-risk/test account where practical;
- expose/use only login-status, search and post-detail/read operations;
- do not publish, comment, like, favorite, follow, message or upload project/customer content;
- if the host cannot technically restrict the tool subset, record that as a risk and keep the adapter CONDITIONAL;
- measure whether Xiaohongshu adds serious practitioner evidence that changes the recommendation, not merely more links.

### Zhihu

No dedicated adapter in the first pilot. Test targeted normal Web discovery first. Add a source-specific dependency only if repeated evidence shows a material acquisition gap that normal Web cannot solve.

## 5. Success criteria

An adapter is useful only if all are true:

1. it acquires practitioner evidence normal Web could not reliably acquire;
2. original-content provenance is sufficient to inspect the practice, not just a title/snippet;
3. the acquired evidence changes at least one material decision: serious candidate pool, ranking, rejection reason, confidence, or explicit coverage boundary;
4. acquisition cost/security/maintenance remains proportionate.

If an adapter only returns more low-quality links, do not promote it.

## 6. Promotion decision

After P0–P3, each source capability gets one status:

- `APPROVED` — repeated material value, acceptable operational cost;
- `CONDITIONAL` — useful but login/anti-bot/maintenance risk is significant;
- `PILOT` — evidence still insufficient;
- `REMOVED` — no material recommendation improvement or unacceptable risk.

Only then consider adding a compact `source-adapter-routing` reference to the Runtime Skill.

Do **not** build a custom adapter framework unless simple Skill/MCP composition repeatedly fails.

## 7. Adversarial boundaries

This pilot is not:

- a requirement to search every platform every time;
- a crawler/resource database;
- an automated refresh service;
- a creator-ranking system;
- proof that Xiaohongshu/Bilibili/WeChat content is inherently better;
- permission to install arbitrary third-party executable Skills during a normal user request.

The goal is narrower:

> prove whether missing-source acquisition is a real product bottleneck and whether a small read-only adapter layer materially improves Curator output.

## 8. Runtime freeze

Keep Runtime Skills at **0.9.1** during this pilot.

Do not create 0.9.2 merely because a platform is absent from a result. Change Runtime only after the pilot produces a repeatable routing requirement that cannot be handled by existing 0.9.1 behavior plus approved acquisition tools.
