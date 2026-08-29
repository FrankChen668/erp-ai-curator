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

### WeChat

Candidate:

`zjp1997720/wechat-article-search`

Pinned pilot commit:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Purpose:

- keyword discovery of public-account articles;
- return metadata and links;
- not assumed to guarantee full article reading.

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

If a Skill wrapper is used, it must be reviewed separately and pinned too.

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
- do not modify ERP AI Curator project code;
- do not commit credentials/cookies;
- do not enable publishing/interactions for research use.

For dependencies that require login, pause only when a human authentication action is genuinely unavoidable (for example QR scan). That is a legitimate Product Owner/local-user action.

## 5. Phase C — Read-only smoke tests

Use a harmless generic topic such as:

`AI 原型` or `AI 需求分析`

Do not use customer confidential data.

### WeChat smoke test

Expected evidence:

- keyword search returns real public-account candidate metadata;
- original URL can be resolved for at least some results or unresolved status is explicit;
- no write/account mutation occurs.

### Xiaohongshu smoke test

Expected evidence:

- search returns real notes;
- at least one result can be opened/read with title, author and meaningful body/detail;
- no like/favorite/comment/follow/publish action occurs.

### Bilibili smoke test

Expected evidence:

- topic search returns real videos;
- at least one candidate yields transcript or sufficiently complete text context;
- source URL/video ID remains traceable.

Record failure as capability evidence. Do not hide anti-bot/login failures.

## 6. Phase D — Explicit multi-Skill routing test

After the adapters are healthy, use a fresh Codex session.

Give Codex this intent:

> Find practitioner evidence about a topic. Normal Web search has weak coverage for a specific platform. Use the installed source-specific capability to obtain original evidence, then return to Curator-style evaluation.

Check:

- did Codex select the correct adapter?
- did it avoid unrelated adapters?
- did it return evidence rather than platform-specific recommendations?
- did it stop after obtaining enough evidence?

This verifies the practical meaning of Curator → adapter orchestration.

## 7. Phase E — Fresh curation uplift test

Only after qualification/smoke tests.

Use a new topic, not T01/T02 answers.

Recommended first topic:

> Find strong AI methods / Skills / practical guides that help an ERP consultant quickly understand an unfamiliar ERP module or custom enterprise system: business process, key objects/data, configuration/logic chain, integrations, common issues and how to verify understanding.

### Run 1 — normal path

Fresh session with current Curator authority docs, but do not explicitly request platform adapters.

Record the final recommendation package.

### Run 2 — adapters available

Fresh session, same task and same current authority docs, with installed adapters available and the routing rule from `SOURCE_ADAPTER_ARCHITECTURE_V3.md`.

The Agent decides whether adapters are needed.

Compare:

- new serious candidates;
- practical Chinese evidence gained;
- recommendation changed or strengthened;
- confidence improved;
- user adoption cost reduced;
- research overhead added.

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

## 9. Evidence file

Local Agent may create one local pilot report in ERP AI Curator only if explicitly instructed after the run.

During qualification, prefer reporting in chat first so installation problems do not create noisy project commits.

Suggested report fields:

```text
Adapter
Pinned commit
Qualification: OK / RISK / REJECT
Installed: yes/no
Read-only enforceable: yes/no/partial
Smoke test: PASS / PARTIAL / FAIL
Evidence acquired
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

## 11. Pilot decisions

After Phase E choose one:

### KEEP NATIVE COMPOSITION

Installed source Skills/MCPs materially improve Curator and routing remains simple.

### KEEP SELECTIVELY

Only one or two adapters provide useful uplift; retain only those.

### USE EXTERNAL ACQUISITION BACKEND

Native Codex adapters are unreliable/unsafe, but a separate tool such as WorkBuddy proves stronger for acquisition.

### DROP EXTRA ACQUISITION

Additional adapters do not materially improve final curation.

No permanent architecture is declared before this evidence exists.
