# Source Adapter Qualification Result 01

Date: 2026-08-29

> Evidence source: first controlled local Windows + Codex qualification run against the pinned candidates defined by `SOURCE_ADAPTER_PILOT_V3.md`.

This is runtime qualification evidence, not a production endorsement.

## 1. Decision summary

| Capability | Candidate / pin | Local result | Current decision |
|---|---|---|---|
| WeChat discovery | `zjp1997720/wechat-article-search` @ `7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6` | Installed; real keyword search worked; 5/5 test results resolved to `mp.weixin.qq.com`; dependency/security caveats remain | **CONDITIONAL** |
| WeChat original-article read | `Githun1314/agent-wechat-reader` @ `0d5b167239f135934dced0411b0fb887d35bf9be` | Installed; self-test passed; public article body and metadata were actually read; exact-host GET-only/no-cookie boundary held | **KEEP FOR PILOT** |
| Bilibili search/transcript | `XZXZZX-Ai/bilibili-mcp` @ `b25b394bce0d05973a8afd7029651509bf407567` | Source build/stdio startup succeeded; real search failed with `COOKIE_EXPIRED`; no transcript evidence obtained | **CONDITIONAL** |
| Xiaohongshu search/detail | `xpzouying/xiaohongshu-mcp` @ `6fb866a7db4e3dcce8dc00a0dde07370f3b12946` | Rejected before installation because the fixed MCP exposes broad social write/account actions and no practical read-only tool surface was demonstrated | **REMOVE** |

## 2. What is now proven

### WeChat acquisition chain is real

The local environment demonstrated:

```text
keyword
→ WeChat discovery Skill
→ real article candidates
→ direct mp.weixin.qq.com URL
→ separate public-article reader Skill
→ original body + metadata
```

The test also demonstrated an important evidence distinction:

> Search snippets are discovery evidence; the original article reader is what upgrades a serious candidate to original-content evidence.

The reader obtained a meaningful article body (4,542 characters in the test) together with title/author/date/original URL evidence.

This is enough to proceed to a focused multi-Skill routing test for the WeChat chain.

### Bilibili candidate is not yet qualified for the desired zero-friction path

The installed pinned candidate reached real MCP invocation, but `search_bilibili_videos("AI 原型")` failed with `COOKIE_EXPIRED`.

Therefore the following are **not yet proven** for this provider in the owner's environment:

- anonymous search reliability;
- search → transcript;
- 412 fallback behaviour.

This is an authentication/setup blockage, not proof that Bilibili content is unavailable.

### Current Xiaohongshu provider failed the permission-boundary test

The first Xiaohongshu candidate was correctly rejected before installation.

Reason:

- the default MCP registers broad write/social/account operations;
- the pilot could not show a practical way to expose only the research/read subset;
- browser automation + persistent login state would add further operational risk.

The capability `xiaohongshu_search_public_notes / xiaohongshu_read_public_note` remains useful in principle. Only this **provider** is removed.

## 3. Adversarial interpretation

### Do not wait for every platform before testing orchestration

The first local report concluded that incomplete Bilibili/Xiaohongshu qualification blocks Phase 3.

That conclusion is too strong.

Phase 3 asks whether Curator intent can route to available qualified capabilities without becoming a platform checklist. One qualified two-step chain is sufficient to falsify or support that hypothesis.

Therefore:

> **WeChat discovery → reader is enough to start a narrow Phase 3 routing test.**

Bilibili and Xiaohongshu can continue on separate provider-qualification tracks.

### Do not relax read-only boundaries merely to gain source coverage

The Xiaohongshu rejection is positive evidence that the lifecycle contract is working. The correct response is not to enable broad write capabilities and promise not to call them.

Prefer:

1. a provider whose exposed tool surface is naturally read-oriented;
2. a technically enforceable read-only subset;
3. otherwise leave a documented coverage gap.

### Installation success is not user-value evidence

The WeChat chain has passed acquisition qualification, but it has **not** yet proven that:

- Codex will invoke it only when useful;
- it improves the final ERP resource recommendation;
- the setup cost is justified across topics.

Those questions belong to Phase 3 and Phase 4.

## 4. Cloud follow-up candidate research

### Bilibili alternative under review

A second current candidate was found:

`https://github.com/sandraschi/bilibili-mcp`

Cloud-observed candidate pin:

`74401935c121b644999208f1ce18c6967b7f2b10`

Its current documentation claims:

- anonymous explore/video-info/transcript capability;
- search may still hit anonymous risk control;
- account-only operations are separated;
- transcript returns an honest unavailable/login-gated result rather than fabricating content.

This directly addresses the first provider's hard Cookie dependency for the tested search path, but the project is broader than a minimal transcript tool and still requires local static/runtime qualification before use.

Status: **CANDIDATE — NOT INSTALLED / NOT APPROVED YET**.

### Xiaohongshu alternative research

A read-oriented crawler/MCP candidate was found:

`https://github.com/yangsijie666/xiaohongshu-crawler`

It exposes search/detail/comment collection rather than social write actions, but uses Playwright plus stealth/fingerprint anti-detection and persistent login state.

That reduces the write-surface problem but introduces a different platform-risk/maintenance problem.

Status: **RESEARCH ONLY — DO NOT INSTALL YET**.

No replacement Xiaohongshu provider is approved at this point.

## 5. Current adapter registry state

```text
wechat_discover_public_articles
  provider: zjp1997720/wechat-article-search
  status: CONDITIONAL

wechat_read_public_article
  provider: Githun1314/agent-wechat-reader
  status: KEEP FOR PILOT

bilibili_search_public_videos / bilibili_read_transcript
  provider A: XZXZZX-Ai/bilibili-mcp
  status: CONDITIONAL — credential blocked
  provider B: sandraschi/bilibili-mcp
  status: CANDIDATE — qualification pending

xiaohongshu_search_public_notes / xiaohongshu_read_public_note
  provider A: xpzouying/xiaohongshu-mcp
  status: REMOVED
  replacement: none approved
```

## 6. Next evidence-producing actions

Do these in parallel conceptually, but keep each local task narrow:

1. **Phase 3A — WeChat routing test**
   - fresh Codex session;
   - Curator-style research task;
   - verify search Skill → reader Skill composition in one task;
   - verify unrelated adapters are not invoked;
   - no T03 curation uplift yet.

2. **Bilibili provider replacement qualification**
   - cloud completes static review first;
   - only then assign exact pinned candidate to local Codex;
   - test anonymous search/video/transcript before asking the Owner to configure credentials.

3. **Xiaohongshu remains a coverage gap**
   - do not weaken read-only policy;
   - continue provider research only if later tasks show the missing source materially matters.

## 7. Product implication

The source-adapter idea has survived its first falsification step only partially:

- **supported:** narrow, replaceable, read-oriented source adapters can extend Codex acquisition;
- **supported:** provider qualification and pinning prevent unsafe/broad candidates from silently entering the workflow;
- **not yet supported:** all desired Chinese platforms can be covered safely;
- **not yet supported:** source adapters materially improve final ERP curation;
- **not yet supported:** full Curator Skill packaging is justified.

The project remains in runtime/product validation, not production Skill implementation.
