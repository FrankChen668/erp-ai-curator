# Final Source Acquisition Comparison

Date: 2026-08-31
Runtime frozen at: curating-erp-ai-resources 0.9.1
Pilot branch: validation/source-acquisition-pilot-local

## Completion boundary

Completed stages: P0 targeted normal Web, P1 WeChat qualification, and P2 Bilibili qualification (partial — no-credential adapter-level testing completed; credential-gated tools stopped at Owner-local boundary).

P2 Bilibili produced adapter-level evidence without credentials: `get_video_metadata` confirmed all three P0 Bilibili candidates, and `get_video_comments` returned practitioner feedback for all three. `search_bilibili_videos`, `get_video_info`, and `get_video_transcript` all returned `COOKIE_EXPIRED` and require Owner-local credential setup.

P3 Xiaohongshu was not executed. The adapter requires Owner-local QR-code login before any read-only smoke test; no autonomous path was available within this pilot boundary. P3 status is NOT QUALIFIED — no evidence was collected, and no judgment about Xiaohongshu's potential value can be made from this pilot.

No final Curator recommendation was produced as part of P0. This document compares acquisition evidence only and does not make a product-architecture decision.

## Comparison

| Path | Unique serious candidates | Original content readable | Changed ranking/judgement? | Security/maintenance cost | Proposed status |
|---|---:|---|---|---|---|
| targeted normal Web | At least one readable Zhihu practitioner-style answer; Bilibili candidates discoverable via site: queries, metadata partially readable | Yes for selected Zhihu and Note pages; Bilibili metadata readable in first run (title/description/tags), 412 on direct video opens in second run; transcripts never accessible via normal Web | Changed the coverage map: Bilibili is discoverable with partial readability, Zhihu is readable; no final ranking was produced in P0 | Low; no new dependency, but host-specific 412/timeout behavior | `PILOT` |
| WeChat adapter + public reader | Multiple current-run task-matched public-account candidates, including two inspected articles | Yes: both selected current-run articles passed `ok=true`, had plausible content length, and `verification_page=false` | Yes at the evidence layer: it added inspectable Chinese practitioner-style material absent from P0 | Moderate; pinned install is small and credentialless, but Sogou anti-bot and redirect resolution are intermittent; reader is a separate read-only dependency | `APPROVED` |
| Bilibili adapter | 0 new candidates (search requires credentials); 3 P0 candidates confirmed via metadata | Partial: practitioner comments readable for all 3 candidates; transcripts and video summaries blocked by COOKIE_EXPIRED | Comments added practitioner signal (draw.io vs Mermaid preference, tool comparisons) not in P0 snippets; no transcript-level comparison possible | High relative to P0: Cookie setup, local credential storage and client reconnection required for search/transcript; ASR was not installed | `CONDITIONAL` |
| Xiaohongshu adapter | Not tested | Not tested | Undetermined — no evidence collected | Not assessed; requires Owner-local QR-code login before any smoke test | `NOT QUALIFIED` |

## Evidence boundary

The WeChat path is the only adapter path that produced fully inspectable original content during this run. The Bilibili path produced partial adapter evidence (metadata confirmation + practitioner comments) without credentials, but could not reach transcript-level evidence. Xiaohongshu has no result in this pilot.

## Required Owner review

1. **WeChat (APPROVED)**: the pinned adapter is credentialless and returned task-relevant inspectable content. Cloud/Owner may decide to integrate or promote from pilot.

2. **Bilibili (CONDITIONAL)**: if the Owner elects to continue, the Owner should locally configure Bilibili credentials and reconnect the client. The next actor must then verify credential status without exposing values, run only search + metadata + transcript for a few serious candidates, and append a new evidence result. No such action is requested or performed by this commit.

3. **Xiaohongshu (NOT QUALIFIED)**: not executed. If the Owner elects to qualify Xiaohongshu, P3 would require Owner-local QR-code login before any smoke test. No evidence was collected; no judgment about its potential value can be made from this pilot.

## Runtime and repository boundary

- Runtime Skill was not modified.
- No router/orchestrator was created.
- No social/write capability was invoked.
- No credentials, cookies, browser profiles, downloaded corpora or adapter binaries were committed.
