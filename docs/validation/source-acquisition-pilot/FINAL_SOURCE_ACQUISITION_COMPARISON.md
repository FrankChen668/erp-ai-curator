# Final Source Acquisition Comparison

Date: 2026-08-31
Runtime frozen at: curating-erp-ai-resources 0.9.1
Pilot branch: validation/source-acquisition-pilot-local

## Completion boundary

Completed stages: P0 targeted normal Web and P1 WeChat qualification.

P2 Bilibili reached the exact Owner-local credential/reconnection boundary and was stopped. P3 Xiaohongshu was not started because the Runbook stop rule was reached before Bilibili could be evaluated and before a P3 decision could be shown to change the acquisition decision.

No final Curator recommendation was produced as part of P0. This document compares acquisition evidence only and does not make a product-architecture decision.

## Comparison

| Path | Unique serious candidates | Original content readable | Changed ranking/judgement? | Security/maintenance cost | Proposed status |
|---|---:|---|---|---|---|
| targeted normal Web | At least one readable Zhihu practitioner-style answer; Bilibili candidates were discoverable but not readable through host Web | Yes for selected Zhihu and Note pages; Bilibili direct pages returned 412 | Changed the coverage map: Bilibili is discoverable-only, Zhihu is readable; no final ranking was produced in P0 | Low; no new dependency, but host-specific 412/timeout behavior | `PILOT` |
| WeChat adapter + public reader | Multiple current-run task-matched public-account candidates, including two inspected articles | Yes: both selected current-run articles passed `ok=true`, had plausible content length, and `verification_page=false` | Yes at the evidence layer: it added inspectable Chinese practitioner-style material absent from P0 | Moderate; pinned install is small and credentialless, but Sogou anti-bot and redirect resolution are intermittent; reader is a separate read-only dependency | `PILOT` |
| Bilibili adapter | No adapter-acquired candidate in this run; normal Web supplied title/snippet candidates only | Not tested at adapter level; credential setup was required before search/transcript | Undetermined; no transcript-level comparison possible | High relative to P0: Cookie setup, local credential storage and client reconnection required; ASR was not installed | `CONDITIONAL` |
| Xiaohongshu adapter | Not tested | Not tested | Undetermined | Not assessed because P2 Owner-local blocker stopped the staged pilot | `PILOT` |

## Evidence boundary

The WeChat path is the only adapter path that produced inspectable original content during this run. The Bilibili path remains a conditional candidate, not a demonstrated improvement, because the required local credential action was not available within the autonomous boundary. Xiaohongshu has no result in this pilot.

## Required Owner review

Only if the Owner elects to continue P2 should the Owner locally configure Bilibili credentials and reconnect the client. The next actor must then verify credential status without exposing values, run only search + metadata + transcript for a few serious candidates, and append a new evidence result. No such action is requested or performed by this commit.

## Runtime and repository boundary

- Runtime Skill was not modified.
- No router/orchestrator was created.
- No social/write capability was invoked.
- No credentials, cookies, browser profiles, downloaded corpora or adapter binaries were committed.
