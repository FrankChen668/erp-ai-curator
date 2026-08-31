# Local Agent Task — WeChat Cross-Task Qualification

Date: 2026-08-31
Status: **NEXT SOURCE-ACQUISITION EVIDENCE STEP**

## Objective

Test whether the currently strong-positive WeChat acquisition path produces **repeatable material value on a second, materially different ERP/ToB task**, rather than only on the prior AI-flowchart task.

This is a source-acquisition repeatability test, not a Runtime Skill rewrite and not a product-value validation.

Runtime Skills remain **0.9.1 frozen**. Do not edit them.

## Task under test

Use this natural task family:

> 我是一名 ERP/ToB 项目经理/实施顾问，经常需要把需求访谈、会议纪要和零散业务讨论整理成结构化需求、PRD/FS 或需求包。帮我找现在用 AI 提升这类工作的最佳实践和真实实操经验。

This task is intentionally different from the previous flowchart/draw.io task:

- primary artifact: structured requirements / PRD / FS / requirement package;
- primary work: requirement elicitation, meeting/minutes synthesis, ambiguity/gap handling, validation/review;
- target users: ERP/ToB project managers and implementation/business consultants;
- do not turn the task into flowchart generation or generic AI meeting-summary advice.

## Authorities to read first

Read only the project authorities needed for this test:

- `docs/CURRENT_EXECUTION_PLAN_V3.md`
- `docs/validation/source-acquisition-pilot/CLOUD_ADVERSARIAL_REVIEW_20260831.md`
- `docs/validation/source-acquisition-pilot/P1_WECHAT_RESULT.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

Do not load unrelated engineering/orchestration Skills merely because this task has multiple steps. The Runbook is the task authority.

## Candidate and pin

WeChat discovery provider:

`zjp1997720/wechat-article-search`

Pinned commit:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Do not update to floating `latest`, run `npm audit fix`, or modify dependency versions during this qualification.

## Known dependency/security fact to verify, not hide

The pinned lockfile currently resolves `cheerio 1.2.0`, which brings `undici 7.x` transitively. A prior `npm audit` reported a High finding.

For this run:

1. install only in a temporary/isolated directory;
2. run `npm audit --omit=dev --json` and save a **small non-sensitive summary** of the exact advisory/package/version result;
3. do not run `npm audit fix`;
4. inspect/confirm the actual adapter script network path still uses Node built-in `https` and `cheerio` for parsing rather than explicitly using undici network/WebSocket/cache/proxy APIs;
5. record that package-level vulnerability presence and practical reachability are separate questions;
6. do not promote to `APPROVED` merely because the vulnerable code path appears unused.

If the audit result is materially worse than the prior P1 evidence or a new reachable risk is found in the actual execution path, stop and report before executing the adapter.

## Hard boundaries

- Do not modify Runtime `SKILL.md` files.
- Do not use project validation/history URLs as current external candidates.
- Do not use P1's old article URLs as the current candidate pool.
- Do not install unrelated MCPs/Skills.
- Do not install system-wide runtimes/SDKs/package managers.
- Do not use customer or confidential meeting notes as test input.
- Do not create synthetic customer data files.
- Do not publish/comment/like/favorite/follow/message anything.
- Do not claim WeChat is better merely because it returns more links.
- Do not force platform diversity in the final result.

## Phase A — fresh normal/targeted Web baseline

Run the natural task in a fresh context or otherwise ensure no historical P1/P04 candidate list is reused.

Build a current baseline with ordinary Web only.

Use a small serious query set that preserves role + task + AI context, for example:

- `AI 需求访谈 会议纪要 需求分析 产品经理 实施顾问`
- `AI PRD FS 需求文档 ERP 项目 实战`
- `AI requirements elicitation meeting notes PRD ERP consultant workflow`

If obvious Chinese practitioner ecosystems are absent, add only the most relevant targeted Web correction(s), including `site:mp.weixin.qq.com` if useful.

Record:

- exact queries;
- serious candidates;
- which originals were actually opened/read;
- role/task/artifact fit;
- publication/update date where available;
- what practical input → operation → output evidence exists;
- limitations/rejection reasons.

Do **not** produce a final user recommendation yet.

## Phase B — pinned WeChat discovery

Use the exact pinned WeChat adapter in an isolated temp directory.

Run a small query set that targets the same task family. Suggested starting terms:

- `AI 需求访谈 会议纪要`
- `AI 需求分析 PRD 产品经理`
- `AI ERP 实施顾问 需求分析`
- `AI 需求文档 FS`

You may adjust wording once if a query is clearly too narrow, but do not mass-search.

Measure:

1. how many task-relevant candidates are returned that Phase A did not expose;
2. which 3–8 candidates are serious enough for inspection;
3. whether direct `mp.weixin.qq.com` URLs can be resolved;
4. whether the strongest 2–4 originals can actually be read through the available read-only path;
5. whether the content contains concrete practitioner workflow, examples, failure modes, templates/checklists, or review/validation discipline rather than generic AI promotion.

Do not infer article quality from title/summary alone.

## Phase C — evidence comparison

Compare Phase A and Phase B without using platform quotas or a numeric scoring model.

For each strong candidate, judge at least:

- ERP/ToB role/task fit;
- concrete workflow depth;
- target artifact fit (requirements / PRD / FS / requirement package);
- evidence/current applicability;
- author self-practice vs vendor/promotion/repost/unclear;
- whether it adds decision information not already present in normal Web candidates.

Answer the key question:

> Did the WeChat path again acquire serious, inspectable practitioner evidence that ordinary/targeted Web did not provide, and did that evidence materially change candidate pool, ranking, rejection reason, confidence, or an explicit coverage boundary?

A result is **not material** if WeChat only adds more versions of the same generic advice.

## Phase D — bounded candidate package

Produce two internal comparison packages, not two polished user tutorials:

### Package A — Web-only

- strongest 1–3 current candidates;
- why they survived;
- important gaps.

### Package B — Web + WeChat

- strongest 1–3 current candidates after adding inspected WeChat evidence;
- whether any ranking/selection changed;
- why.

The objective is to observe acquisition delta, not to force WeChat into Package B.

## Required result

Write:

`docs/validation/source-acquisition-pilot/P4_WECHAT_CROSS_TASK_RESULT.md`

Include:

1. task and host/runtime;
2. fresh Web queries/results/opened originals;
3. WeChat queries/results/opened originals;
4. Package A vs Package B;
5. exact acquisition delta;
6. dependency/audit summary;
7. operational cost/failures;
8. evidence boundary;
9. one proposed provider status: `APPROVED`, `CONDITIONAL`, `PILOT`, or `REMOVED`.

The proposed status is Local Agent evidence input only. Cloud makes the final promotion decision.

## Promotion interpretation

A second positive task can support promotion only if:

- WeChat again changes the serious evidence/recommendation package materially;
- original-content reading remains sufficiently reliable;
- the operational cost remains low;
- the dependency/security issue is either fixed or acceptably bounded for the intended read-only use.

A second weak/no-delta task should keep the provider at `PILOT` or downgrade it; do not rationalize around the result.

## Commit boundary

Commit only:

- `P4_WECHAT_CROSS_TASK_RESULT.md`;
- optional small non-sensitive audit/diagnostic summary if needed.

Do not commit:

- node_modules;
- temp downloads;
- cookies/session material;
- downloaded article corpora;
- customer/project data;
- adapter binaries.

Push to a new remote review branch. Do not force-push over other Agent branches.

## Stop rule

Stop only if:

- the pinned adapter can no longer be installed/executed proportionately in isolation;
- dependency/security inspection finds a materially reachable risk that makes execution disproportionate;
- source access repeatedly fails such that original-content inspection is impossible;
- or P4 evidence is complete.

No Owner login or account action should be required for this WeChat pilot.
