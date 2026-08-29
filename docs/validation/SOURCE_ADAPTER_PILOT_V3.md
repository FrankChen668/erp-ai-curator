# Source Adapter Pilot V3 — Local Qualification + Curation Uplift

> Purpose: test whether installed source-specific Skills/MCPs can safely and reliably improve ERP AI Curator's evidence acquisition and final recommendation quality.

This is not a production install guide and not a permanent adapter catalog.

## 1. Pilot questions

The pilot must answer four questions:

1. Can the local Codex environment safely install and invoke the candidate adapters?
2. Can each adapter actually acquire original/sufficient content from its target platform?
3. Can Curator route to an adapter only when needed, rather than query everything?
4. Does adapter evidence materially improve the final share-worthy recommendation package?

## 2. Candidate set

### WeChat discovery

Candidate:

`zjp1997720/wechat-article-search`

Pinned pilot commit:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Purpose:

- keyword discovery of public-account articles via Sogou WeChat Search;
- return title/account/time/summary/link;
- resolve direct `mp.weixin.qq.com` URL when possible.

This is a **discovery** capability, not sufficient proof that the original article body was read.

### WeChat public-article reader

Candidate:

`Githun1314/agent-wechat-reader`

Pinned pilot commit:

`0d5b167239f135934dced0411b0fb887d35bf9be`

Skill:

`skills/wechat-article-reader`

Purpose:

- read public exact-host `https://mp.weixin.qq.com/...` article URLs;
- extract clean article content + metadata + trace;
- no Cookie, credentials, browser control or third-party mirror service.

Cloud static review found the implementation intentionally narrow: HTTPS exact host, GET-only, bounded redirects/size, verification-page detection, and stop-on-verification behaviour. Local smoke test is still required.

### Xiaohongshu

Candidate MCP:

`xpzouying/xiaohongshu-mcp`

Pinned pilot commit:

`6fb866a7db4e3dcce8dc00a0dde07370f3b12946`

Purpose:

- keyword search;
- feed/detail reading;
- Windows-capable release exists.

Use only read/search capabilities during this pilot.

This candidate is higher-risk because login/browser automation and write/social actions exist in the wider MCP. The local pilot must verify whether research use can remain read-only in practice.

### Bilibili

Candidate:

`XZXZZX-Ai/bilibili-mcp`

Pinned pilot commit:

`b25b394bce0d05973a8afd7029651509bf407567`

Purpose:

- topic search;
- transcript/context retrieval;
- evidence links.

Use only read/search/transcript capabilities.

Current upstream includes fallback handling for some Bilibili HTTP 412 subtitle failures, but local reliability must be proven rather than inferred from documentation.

## 3. Phase A — Qualification before installation

Local Codex performs a static review for each candidate.

Minimum checks:

```text
repository + commit
license
install method
dependencies
install scripts
prebuilt binaries
network targets
credential/cookie locations
filesystem writes
browser extension / browser automation
available read actions
available write actions
whether read-only restriction is technically possible
Windows compatibility
known open issues relevant to search/read
```

Do not install a candidate if the Agent finds an unexplained high-risk action in the install/runtime path.

Do not ask Product Owner to manually inspect source files. Report only decisions and material risks.

## 4. Phase B — Controlled installation

Rules:

- clone/download from the pinned commit, not floating latest;
- record installed path;
- record exact commit/hash;
- do not auto-update during pilot;
- do not modify ERP AI Curator product code/docs;
- do not commit credentials/cookies;
- do not enable publishing/interactions for research use.

For dependencies that require login, pause only when a human authentication action is genuinely unavoidable (for example QR scan).

Do not use a login-requiring Adapter as the sole route to a useful Curator answer.

## 5. Phase C — Read-only smoke tests

Use harmless generic topics such as:

`AI 原型` or `AI 需求分析`

Do not use customer confidential data.

### WeChat end-to-end smoke test

This must test **two capabilities in one chain**:

```text
keyword
→ wechat-article-search
→ real candidate metadata
→ direct mp.weixin.qq.com URL
→ wechat-article-reader
→ original article body + metadata
```

Expected evidence:

- discovery returns real public-account candidates;
- at least one direct original article URL is obtained when available;
- reader actually extracts meaningful body text and metadata;
- search summary and original body can be distinguished;
- no login/write/account mutation occurs.

If discovery cannot resolve a direct URL, report that limitation; do not pretend the summary is full-text evidence.

### Xiaohongshu smoke test

Expected evidence:

- search returns real notes;
- at least one result can be opened/read with title, author and meaningful body/detail;
- no like/favorite/comment/follow/publish action occurs.

If login is required, stop at the unavoidable human authentication step and report it rather than requesting Cookie/password values in chat.

### Bilibili smoke test

Expected evidence:

- topic search returns real videos;
- at least one candidate yields transcript or sufficiently complete text context;
- source URL/video ID remains traceable;
- actual fallback behaviour is recorded if a 412/risk-control path appears.

Record failure as capability evidence. Do not hide anti-bot/login failures.

## 6. Phase D — Explicit multi-Skill/MCP routing test

After healthy adapters exist, use a fresh Codex session.

Give a practitioner-evidence task where normal Web coverage is known to be incomplete, but do not instruct the Agent to query every adapter.

Check:

- did Codex select the capability that matches the evidence gap?
- did it avoid unrelated adapters?
- for WeChat, can it move discovery → original article reader without manual copy/paste masquerading as orchestration?
- did it return acquired evidence to Curator judgement?
- did it preserve read-only boundaries?
- did it stop after enough evidence was obtained?

Record:

`Multi-skill routing: PASS / PARTIAL / FAIL`

Do not treat installed files alone as orchestration proof.

## 7. Phase E — Fresh curation uplift test

Only after qualification/smoke/routing tests.

Use a new topic, not T01/T02 answers.

Recommended first topic:

> Find strong AI methods / Skills / practical guides that help an ERP consultant quickly understand an unfamiliar ERP module or custom enterprise system: business process, key objects/data, configuration/logic chain, integrations, common issues and how to verify understanding.

### Run A — normal path

Fresh session with current Curator authority docs. Adapter acquisition is unavailable/disabled for the comparison.

Freeze the final package.

### Run B — qualified adapters available

Fresh session, same task and current authority docs, with only qualified adapters available and conditional routing rules enabled.

The Agent decides whether any adapter is actually needed.

Compare:

- new serious candidates;
- original/full practitioner content gained;
- practical Chinese evidence gained;
- recommendation changed or materially strengthened;
- confidence improved because evidence is better;
- user adoption/learning cost reduced;
- research/setup overhead added.

The question is not `did we get more links?` but `did the final package become more worth sharing?`.

## 8. Success evidence

Useful adapter uplift:

- finds a strong practitioner guide absent from normal search;
- obtains original/full content that normal search only exposed as a snippet;
- exposes failure/limitations absent from official/GitHub evidence;
- discovers a local Chinese Tool/Skill/workflow that materially changes candidate comparison;
- makes the final package more share-worthy for ERP colleagues.

Not useful:

- more links but same decision;
- generic AI content;
- promotional content;
- platform popularity metrics only;
- scraped content the Curator cannot trust or act on;
- large setup burden for negligible curation improvement.

## 9. Evidence reporting

During qualification, prefer reporting in chat first so installation problems do not create noisy project commits.

Required fields:

```text
Adapter / capability
Pinned commit
Qualification: OK / RISK / REJECT
Installed: yes/no
Installed/configured path
Read-only enforceable: yes/no/partial
Smoke test: PASS / PARTIAL / FAIL
Evidence actually acquired
Known limitation
Human action required
Recommendation: KEEP FOR PILOT / CONDITIONAL / REMOVE
```

No numeric score.

## 10. Stop conditions

Stop and report rather than improvising when:

- install script requests unexplained privileged access;
- executable origin/hash cannot be established;
- credential handling is unclear;
- adapter requires write permissions to perform read-only research;
- platform blocks access persistently;
- source project's documented behavior materially differs from inspected code/runtime.

Do not install a replacement candidate during this same task unless cloud review explicitly assigns it.

## 11. Pilot decisions

After Phase E choose one:

### KEEP NATIVE COMPOSITION

Installed source Skills/MCPs materially improve Curator and routing remains simple.

### KEEP SELECTIVELY

Only one or two adapters provide useful uplift; retain only those.

### USE EXTERNAL ACQUISITION BACKEND

Native Codex adapters are unreliable/unsafe, but a separate acquisition tool proves stronger.

### DROP EXTRA ACQUISITION

Additional adapters do not materially improve final curation.

No permanent architecture is declared before this evidence exists.
