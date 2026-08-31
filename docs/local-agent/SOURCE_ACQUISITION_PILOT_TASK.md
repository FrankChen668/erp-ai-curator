# Local Agent Task — Source Acquisition Pilot

Use this task only after syncing the repository branch/main that contains `docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`.

## Objective

Determine whether the repeated absence of Xiaohongshu / WeChat / Bilibili / Zhihu practitioner evidence is primarily:

- normal Web recall/indexing weakness;
- original-content acquisition weakness;
- or a gap that a small read-only source adapter can materially solve.

Do not modify Runtime Skills during this task.

## Hard boundaries

- Do not edit either Runtime `SKILL.md`.
- Do not create a new router/orchestrator.
- Do not install all adapters up front.
- Do not use project historical P04/validation URLs as the candidate source for the test.
- Do not paste cookies, tokens, passwords, QR payloads or browser-profile data into chat, files or Git.
- Do not use publish/comment/like/favorite/follow/message/upload capabilities.
- Do not claim an adapter is useful merely because it returns more links.
- Preserve exact search/tool/open facts; do not reconstruct missing logs from memory.

## Working branch

Create a local validation branch, for example:

`validation/source-acquisition-pilot-local`

Commit only pilot result Markdown and non-sensitive diagnostic summaries. Never commit credentials, cookies, browser profiles, downloaded third-party corpora or adapter binaries.

## P0 — targeted normal-Web baseline

Fresh Agent context. Confirm Runtime 0.9.1 is loaded, but do not use repository validation/history as source evidence.

Use the natural task:

> 使用 curating-erp-ai-resources skill 给我找下做流程图的最佳实践

Run the normal broad discovery first.

If the result pool misses obvious Chinese practitioner ecosystems, exercise targeted normal-Web recall. Use source-qualified query forms appropriate to the host, including a small subset such as:

```text
site:bilibili.com AI draw.io 流程图 产品经理 ERP
site:zhihu.com AI draw.io 流程图 产品经理 ERP
site:mp.weixin.qq.com AI draw.io 流程图 产品经理 ERP
site:xiaohongshu.com AI draw.io 流程图 产品经理 ERP
```

Do not force a query that the host/search backend does not support. Record that limitation instead.

For each source class record:

- actual query;
- top relevant candidate titles/URLs;
- whether original content could be opened/read;
- publication/update date if visible;
- whether the candidate is serious enough to inspect further;
- access/indexing limitation.

Do not produce the final Curator recommendation yet.

Write:

`docs/validation/source-acquisition-pilot/P0_TARGETED_WEB_RESULT.md`

### P0 decision facts

Classify each source only by observable acquisition state:

- `WEB_DISCOVER_AND_READ`
- `WEB_DISCOVER_ONLY`
- `WEB_NO_USEFUL_RECALL`
- `HOST_TOOL_UNSUPPORTED`

Do not infer content absence from poor Web recall.

## P1 — WeChat lightweight qualification

Proceed after P0 if WeChat is `WEB_DISCOVER_ONLY` or `WEB_NO_USEFUL_RECALL` and WeChat evidence could plausibly affect the recommendation.

Candidate:

`zjp1997720/wechat-article-search`

Pilot pin reviewed by Cloud:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Before installation:

1. inspect `SKILL.md`, package manifest/lock, install instructions and `scripts/search_wechat.js` at the pinned commit;
2. list network targets, dependencies and file writes;
3. confirm the intended operations are search/metadata/URL-resolution only;
4. record any security concern that would make installation disproportionate.

If acceptable, install/execute the pinned source in the local pilot environment. Do not silently switch to `latest`.

Run 2–4 task-relevant keyword searches, not a broad crawl.

Measure:

- does it return relevant WeChat practitioner candidates P0 did not expose?;
- can serious candidates be resolved/opened sufficiently for judgement?;
- does it add a candidate or evidence that could materially change the final recommendation?

Write:

`docs/validation/source-acquisition-pilot/P1_WECHAT_RESULT.md`

## P2 — Bilibili qualification

Proceed after P0 if Bilibili is not reliably readable through normal Web and video practitioner evidence remains material.

Candidate:

`XZXZZX-Ai/bilibili-mcp`

Pilot pin reviewed by Cloud:

`b25b394bce0d05973a8afd7029651509bf407567`

Before installation/configuration:

1. inspect package/install/client setup and tool reference at the pinned commit;
2. identify credential storage and all exposed write/social capabilities;
3. plan a read-only subset: search, metadata, transcript; comments only if specifically useful as counter-evidence;
4. do not install optional ASR for the first smoke test.

If local credential setup or client restart is unavoidable, stop only at that exact point and give the Owner the minimum local action. Never request or display credential values.

After reconnect, verify the adapter's own login/credential status through its non-secret status tool before claiming success.

Run task-relevant Bilibili search, select one or a few serious candidates, and read transcript/metadata only for those candidates.

Measure whether transcript-level evidence changes judgement versus P0 title/snippet evidence.

Write:

`docs/validation/source-acquisition-pilot/P2_BILIBILI_RESULT.md`

## P3 — Xiaohongshu isolated read-only qualification

Do not start P3 merely because Xiaohongshu was absent from P0. Start it when:

- normal Web coverage is weak;
- Xiaohongshu practitioner evidence is plausibly decision-changing for the task;
- P0–P2 have not already made the source-acquisition decision stable.

Candidate:

`xpzouying/xiaohongshu-mcp`

Current Cloud-observed main on 2026-08-31:

`332d196854a9eac0d2b8c2c0e3d0cc43139d724c`

The immediately preceding functional pin already recorded by the project is:

`6fb866a7db4e3dcce8dc00a0dde07370f3b12946`

The newer commit is documentation-only. For controlled qualification, inspect the diff and choose one explicit pinned commit; do not use floating latest.

Before install/configuration:

1. inspect manifests, entry points, binaries/releases, browser automation and credential storage;
2. enumerate all tools and identify the minimum read-only subset;
3. confirm the adapter exposes publish/comment/like/favorite/follow or other social actions and ensure they will not be invoked;
4. prefer a low-risk/test account where practical;
5. if the host cannot technically restrict the tool subset, record this as a material risk.

Login/QR/manual authentication is an Owner-local action. Stop at that exact point when needed; do not request secrets in chat.

Smoke test only:

- login/status;
- keyword search;
- post detail/read for a few serious candidates.

Do not publish, interact, upload files or mutate the account.

Write:

`docs/validation/source-acquisition-pilot/P3_XIAOHONGSHU_RESULT.md`

## Final pilot comparison

After the completed stages, write:

`docs/validation/source-acquisition-pilot/FINAL_SOURCE_ACQUISITION_COMPARISON.md`

For each path compare:

| Path | Unique serious candidates | Original content readable | Changed ranking/judgement? | Security/maintenance cost | Proposed status |
|---|---:|---|---|---|---|
| targeted normal Web | | | | | |
| WeChat adapter | | | | | |
| Bilibili adapter | | | | | |
| Xiaohongshu adapter | | | | | |

Proposed status must be one of:

- `APPROVED`
- `CONDITIONAL`
- `PILOT`
- `REMOVED`

Do not make the final product-architecture decision. Provide evidence and a proposed status for Cloud/Owner review.

## Stop rule

Continue independently through all steps that do not require secrets/manual account authentication/client restart.

Stop only when:

- Owner-local login/QR/credential action is genuinely required;
- a security/supply-chain concern makes installation unsafe to continue;
- the host cannot expose the required capability;
- or the pilot decision is already stable and later stages would not be decision-changing.

When stopping, report:

1. completed stage;
2. exact blocker/decision point;
3. exact next actor action;
4. files/commit produced;
5. what Cloud should review next.
