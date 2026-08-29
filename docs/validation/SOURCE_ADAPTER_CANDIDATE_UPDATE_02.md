# Source Adapter Candidate Update 02 — Bilibili Alternative Review

Date: 2026-08-29

## 1. Why this review exists

The first local Bilibili provider (`XZXZZX-Ai/bilibili-mcp`) built and started correctly but its real search path returned `COOKIE_EXPIRED`. Before asking the Owner to configure Bilibili credentials, cloud review looked for a lower-friction provider that can produce useful public evidence anonymously.

## 2. Candidate

Repository:

`https://github.com/sandraschi/bilibili-mcp`

Cloud-review pin:

`74401935c121b644999208f1ce18c6967b7f2b10`

License: MIT.

Runtime: Python 3.11+, FastMCP/FastAPI/httpx/pydantic; source install is available.

## 3. Capability fit

The candidate separates an anonymous tier from an optional account tier.

Documented anonymous capabilities include:

- trending/rank/hot-search discovery;
- video/user search, although anonymous search may still hit Bilibili risk control;
- video metadata/comments/pages;
- transcript retrieval when a subtitle track is publicly available.

The account tier adds following/favorites and can help search risk control, but is not required by design for the core read path.

This is materially different from the first provider's tested behaviour because it creates a plausible path to video/transcript evidence without making Cookie configuration the first step.

## 4. Static security / scope review

### Positive findings

- no social publish/comment/like/follow mutation tools were found in the MCP tool set;
- account tools are reads (`status`, `following`, `favorites`);
- Cookie configuration is optional and documented via local `.env`/environment variable;
- default API base is `https://api.bilibili.com`;
- stdio mode is available and should be preferred for the Curator pilot;
- transcript failure is intended to return an explicit unavailable/login-gated result rather than fabricate content.

### Important caveats

This is not a minimal transcript-only adapter.

It also exposes/supports:

- local LLM discovery/chat/translate/summarize surfaces;
- local web/FastAPI surfaces;
- a server shutdown tool;
- Prefab status/cache tools.

One specific implementation issue matters to our read-only discipline:

`show_bilibili_cache_card` is annotated as `READ_ONLY` but actually clears the local response cache.

That is a local side effect, not a social-platform write, but it proves tool annotations alone are not sufficient evidence for Curator permission decisions.

The HTTP mode also supports broad local/LAN/Tailscale CORS patterns. The Curator pilot does not need that surface.

## 5. Pilot boundary if locally tested

Use only source-built pinned code and **stdio mode**.

Allowed tool subset for the Curator qualification:

```text
bilibili_explore
bilibili_search
bilibili_video (info/pages/comments only as needed)
bilibili_transcript
bilibili_help (optional)
bilibili_account(status only, if needed for diagnosis)
```

Do not invoke:

```text
bilibili_shutdown
show_bilibili_cache_card
local LLM chat/translate/summarize surfaces
following/favorites
HTTP/webapp mode
```

No Cookie should be configured for the first test. The whole purpose is to see whether the anonymous path reduces adoption friction.

## 6. Local test required

Cloud review cannot prove:

- anonymous Bilibili search works from the Owner's current network;
- a real candidate video can yield transcript text;
- risk-control behaviour is better than the first provider;
- Windows/stdin integration remains stable.

Therefore status is:

> **CONDITIONAL CANDIDATE — SAFE ENOUGH FOR A NARROW LOCAL QUALIFICATION, NOT APPROVED FOR CURATION YET.**

Recommended local smoke test later:

```text
anonymous startup
→ bilibili_search("AI 原型")
→ choose real BVID
→ bilibili_video(info)
→ bilibili_transcript
```

If search is risk-controlled anonymously, test whether known-BVID transcript still works. This distinguishes `search coverage` from `content-reading coverage`.

## 7. Xiaohongshu parallel finding

Cloud search found a read-oriented crawler/MCP candidate (`yangsijie666/xiaohongshu-crawler`) whose exposed tools are search/detail/comment collection rather than social write actions.

However it uses:

- Playwright browser automation;
- stealth/fingerprint anti-detection;
- persistent QR-login state;
- optional bulk collection/storage.

This solves the original write-surface problem but introduces a different maintenance/platform-risk profile. It is **not approved for local installation** at this stage.

Current Xiaohongshu state remains:

> coverage gap; do not weaken the Curator permission boundary merely to fill it.

## 8. Decision

- `sandraschi/bilibili-mcp`: **CONDITIONAL CANDIDATE FOR LATER LOCAL QUALIFICATION**.
- `XZXZZX-Ai/bilibili-mcp`: remains **CONDITIONAL**; do not require Owner Cookie setup yet.
- Xiaohongshu: no replacement provider approved.
- None of this blocks Phase 3A WeChat multi-Skill routing.
