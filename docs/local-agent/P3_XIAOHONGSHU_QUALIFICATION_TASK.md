# Local Agent Task — P3 Xiaohongshu Read-Only Qualification

Date: 2026-08-31
Status: **NEXT SOURCE-ACQUISITION PILOT STEP**

## Objective

Qualify whether Xiaohongshu can materially improve practitioner evidence acquisition for ERP/ToB AI practice curation when normal Web search returns no useful Xiaohongshu recall.

This is a source-acquisition test, not a product-feature rollout.

Runtime Skills remain **0.9.1 frozen**. Do not edit them.

## Starting point

Sync latest `main` and read:

- `docs/validation/source-acquisition-pilot/CLOUD_ADVERSARIAL_REVIEW_20260831.md`
- `docs/validation/source-acquisition-pilot/P0_TARGETED_WEB_RESULT.md`
- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

Create a new local branch such as:

`validation/source-acquisition-pilot-p3-xiaohongshu`

Do not reuse the prior multi-Agent evidence branch.

## Candidate

Repository:

`xpzouying/xiaohongshu-mcp`

Cloud-observed current main on 2026-08-31:

`332d196854a9eac0d2b8c2c0e3d0cc43139d724c`

The immediately preceding functional commit recorded by the project:

`6fb866a7db4e3dcce8dc00a0dde07370f3b12946`

The newer commit is documentation-only relative to the preceding functional commit. For controlled qualification, inspect the exact diff and choose one explicit pinned commit. Do not use floating `latest`.

## Hard boundaries

- Do not modify either Runtime `SKILL.md`.
- Do not build a router/orchestrator.
- Do not install or enable unrelated social-platform tools.
- This task is governed by this Runbook. Do not invoke unrelated project Skills such as `graph-engineering`, generic coding-guideline Skills, or other orchestration Skills merely because the task has multiple steps or contains source/build inspection. If the host auto-loads one, record it as a host Skill-collision fact and do not let it broaden the task.
- Do not publish, comment, reply, like, favorite, follow, message, upload, delete, edit or mutate account content.
- Do not paste cookies, tokens, QR payloads, browser profile files or passwords into chat, Markdown or Git.
- Do not use customer/project files as test content.
- Use only public content and a low-risk/test account where practical.
- Do not claim Xiaohongshu is useful merely because search returns more results.
- Do not install system-wide language runtimes, SDKs, package managers or build toolchains for this pilot. Do not use `winget`, Chocolatey, Scoop, MSI installers or equivalent to add Go or mutate machine-wide/user-wide `PATH`, registry or developer configuration.

## Phase A — pre-login supply-chain / capability inspection

Before installation or login:

1. inspect the pinned repository source, manifests, build/install instructions and executable entry points;
2. enumerate all MCP tools/capabilities;
3. explicitly identify the minimum read-only subset needed for this pilot:
   - login/status check;
   - keyword search;
   - post/detail read;
   - metadata needed for provenance (author/date/URL/engagement where available);
4. identify all write/social/account capabilities and confirm they will not be invoked;
5. identify browser automation, local file writes, credential/cookie storage and network targets;
6. identify whether the host can technically restrict the exposed tool subset. If not, record that as a material risk;
7. inspect whether binaries are downloaded/prebuilt or built locally;
8. record exact pinned commit selected and why.

If inspection reveals a material security/supply-chain concern that makes read-only qualification disproportionate, stop and report it before login.

## Phase B — install/configure up to Owner-local authentication boundary

Install/configure only the pinned candidate in a temporary or isolated local pilot environment.

Proceed autonomously through all steps that do not require account authentication **and do not mutate the host development environment**.

### Build/runtime dependency boundary

If the pinned candidate requires a build/runtime tool that is not already available locally (for example Go):

1. do **not** install it system-wide or through a system package manager merely to complete the pilot;
2. first determine whether a prebuilt artifact has provenance that matches the exact reviewed source/tag/commit. A release binary from a different tag or commit is not an automatic substitute for the pinned candidate;
3. if source build remains necessary, an official portable toolchain may be extracted entirely under a temporary pilot directory only when its provenance/checksum is verifiable, it requires no admin rights and no persistent PATH/registry/profile changes, and the extra setup remains proportionate to this qualification;
4. keep all toolchain caches/build outputs under temporary or disposable locations where practical;
5. if an exact-provenance artifact or proportionate isolated toolchain path is not available, stop and record this as an operational/supply-chain qualification cost. Do not silently widen the machine setup.

The existence of an upstream prebuilt release does not by itself prove it corresponds to the pinned commit under review.

At the exact point where Xiaohongshu QR/login/manual authentication is required:

**STOP.**

Do not attempt to bypass login, reuse browser cookies automatically, scrape local browser profiles, or request credential values.

Tell the Owner only:

1. what command/window is waiting for login;
2. the minimum action required (for example, scan the displayed QR in the local window);
3. whether client restart/reconnect is required after login;
4. what non-secret status check will confirm login succeeded.

Do not continue until the Owner completes that local action.

## Phase C — read-only smoke test after Owner login

After login/reconnect, first verify login status using the adapter's own non-secret status capability.

Only if login is confirmed, run a small task-relevant search set. Use the same task family as P0 so acquisition delta is comparable, for example:

- `AI draw.io 流程图`
- `AI 业务流程图 产品经理`
- `AI 流程图 ERP ToB`

Do not mass crawl.

For the returned candidates:

1. identify 3–8 serious candidates using task/role/artifact fit, not raw popularity;
2. open/read detail for only the strongest 2–4;
3. record:
   - title;
   - author/account;
   - publication date if available;
   - original URL/note identifier;
   - engagement metadata only as discovery context;
   - actual practitioner steps/input/output/failure notes;
   - whether the post is author self-practice, promotional, reposted or unclear;
   - whether the content materially adds evidence beyond P0/P1/P2.

Do not like/favorite/comment/follow/message anything.

## Phase D — decision comparison

Write:

`docs/validation/source-acquisition-pilot/P3_XIAOHONGSHU_RESULT.md`

Compare Xiaohongshu with current evidence, especially:

- normal Web: zero useful Xiaohongshu recall;
- WeChat: strong positive acquisition but still Cloud status PILOT;
- Bilibili: CONDITIONAL, normal Web discovery + anonymous metadata/comments, credential needed for search/transcript.

The key question is:

> Did Xiaohongshu obtain serious practitioner evidence that normal Web and the already-tested sources did not provide, and did that evidence materially change candidate pool, ranking, rejection reason, confidence, or an explicit coverage boundary?

Propose exactly one status:

- `APPROVED`
- `CONDITIONAL`
- `PILOT`
- `REMOVED`

This proposed status is evidence input only. Cloud makes the architecture/promotion decision.

## Required evidence boundary

If search works but detail reading fails, record acquisition as partial; do not infer post quality from title/snippet/engagement alone.

If no serious candidate is found, distinguish:

- platform search returned no relevant candidate;
- search/access failed;
- candidates existed but were low-fit;
- original content was inaccessible.

Do not collapse these into “小红书没有好内容”.

## Commit boundary

Commit only:

- `P3_XIAOHONGSHU_RESULT.md`;
- optional small non-sensitive diagnostic summary needed to support it.

Never commit:

- cookies/tokens;
- QR images/payloads;
- browser profiles;
- account identifiers not already public and necessary for evidence;
- downloaded corpora;
- adapter binaries;
- screenshots containing account/session secrets.

Push to a new remote review branch; do not force-push over another Agent's branch.

## Stop rule

Stop only when:

- Owner-local QR/login/restart action is required;
- security/supply-chain inspection blocks continuation;
- the adapter cannot expose the needed read path;
- a missing dependency cannot be satisfied through a proportionate isolated path without host mutation;
- or P3 evidence is complete.

When stopping for Owner login, do not summarize the whole project. Give only the exact local action needed and wait.
