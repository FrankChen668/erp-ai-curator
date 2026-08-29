# ERP AI Curator — Source Adapter Architecture V3

> Status: pilot architecture. This does **not** mean all source adapters should be installed by default, and it does not yet change the Curator into a multi-agent crawler.

## 1. Product correction

The Chinese-source coverage tests exposed a real capability gap:

> The Curator can often judge source quality, but the default Web/Codex path cannot reliably discover or read every practitioner platform.

The correct response is **not** to move curation into WorkBuddy or another separate system by default.

A better architecture is:

```text
ERP AI Curator
  ├─ task / evidence judgement
  ├─ normal Web + GitHub discovery
  └─ optional source adapters
       ├─ WeChat discovery / reading
       ├─ Xiaohongshu discovery / reading
       └─ Bilibili discovery / transcript
```

The Curator remains the judgement layer. Source adapters only add acquisition capability.

## 2. What “Skill calls Skill” means in Codex

Do not assume a nested Skill works like a hard-coded function call.

Codex can use multiple installed Skills and tools in one task. The Curator Skill should therefore contain routing instructions such as:

> If practitioner evidence from a platform is materially useful and the normal Web path cannot reliably acquire it, use the installed matching source-adapter Skill/MCP. Return the acquired evidence to the Curator workflow for evaluation.

So the runtime model is:

```text
Curator instructions
      ↓
Codex runtime chooses / invokes matching installed Skill or MCP
      ↓
source evidence returned
      ↓
Curator evaluates task fit, trust, practical value and limitations
```

The first local pilot must verify that this multi-Skill routing is reliable in the actual Codex environment. Do not treat it as proven merely because the Skill files exist.

## 3. Responsibility boundary

### Curator owns

- understand the real ERP / enterprise-information-system job;
- decide what evidence is missing;
- decide whether a source adapter is worth invoking;
- define search intent and useful evidence;
- compare candidates across source classes;
- verify volatile/native claims;
- decide what is worth recommending;
- stop research when the decision is stable.

### Source adapter owns

- access one source that the normal path handles poorly;
- search or open source-native content;
- obtain enough original content to judge it;
- return source metadata and access limitations.

### Source adapter must not own

- final recommendation;
- “best resource” judgement;
- ERP task interpretation;
- automatic platform quotas;
- permanent resource database maintenance.

## 4. Adapter trigger

Use an adapter only when all of these are true:

1. the task is in external resource discovery / evidence gathering;
2. the source class could materially change the recommendation or reduce adoption cost;
3. the normal Web/GitHub path has weak discovery or reading coverage for that source;
4. an installed adapter can fill that concrete gap with acceptable cost and risk.

Do **not** invoke all installed adapters for every topic.

Examples of valid triggers:

- We found a promising WeChat result but cannot resolve/read the original article.
- The topic is strongly practitioner-driven and Xiaohongshu contains potentially useful field practice that ordinary Web search does not expose well.
- Bilibili search finds relevant videos but the normal browser cannot get full subtitles/transcript.

Invalid trigger:

> “We installed three adapters, so every curation task must query all three.”

## 5. Read-only principle

The Curator is a research product, not a social-media operations bot.

For source-adapter use, default capabilities are:

```text
ALLOW
- search
- read detail
- read transcript / article body
- read author / date / original URL
- read public comments only when needed as counter-evidence

DENY BY DEFAULT
- publish
- edit
- delete
- like
- favorite
- follow
- comment / reply
- send message
- account management
```

If a third-party Skill bundles write actions, the local setup should expose only the minimum tools needed for research whenever technically possible.

## 6. Minimal evidence handoff

Adapters should return enough evidence for evaluation, not a huge archive.

```text
platform
query / discovery path
source title
source author/account (if available)
publish date (if available)
original URL
content type
original-content status: full / sufficient / partial / inaccessible
practical evidence: steps / prompt / demo / output / failure notes (if present)
access limitation
```

Do not commit full third-party article/video contents into the ERP AI Curator repository.

The repository should store our judgement, links, small evidence summaries and coverage findings—not copied source corpora.

## 7. Candidate adapter shortlist for Windows Codex pilot

These are **pilot candidates**, not endorsed permanent dependencies.

### A. WeChat discovery — `zjp1997720/wechat-article-search`

Role:

- Codex/Agent Skill for keyword discovery of WeChat public-account articles via Sogou WeChat Search;
- returns title, summary, account, time and link;
- optional resolution to direct `mp.weixin.qq.com` URL.

Why it is interesting:

- narrow read/discovery purpose;
- MIT;
- no API key required for the Sogou path;
- directly packaged as an Agent/Codex Skill.

Pilot pin observed 2026-08-29:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Known limitation:

- Sogou anti-bot can return empty results or fail URL resolution;
- it is stronger for **discovery** than guaranteed full-text reading.

Therefore the Curator must still open the original article when it becomes a serious candidate.

### B. Xiaohongshu search/read — `xpzouying/xiaohongshu-mcp`

Role:

- local MCP for Xiaohongshu login, search, feed detail and other operations;
- current releases include Windows x64 binaries;
- an external Skill wrapper can route search/detail operations.

Why it is interesting:

- mature user base relative to other candidates;
- active current maintenance;
- Windows support;
- can fill the exact Xiaohongshu discovery/read gap observed in T01/T02.

Pilot pin observed 2026-08-29:

`6fb866a7db4e3dcce8dc00a0dde07370f3b12946`

Important counter-evidence:

- project has many open issues;
- historical reports include search failures under Xiaohongshu anti-bot/risk controls and browser-process problems;
- login/cookie/browser automation introduces more local security and maintenance cost than a simple search Skill.

Pilot policy:

- use only search + detail capabilities;
- do not enable publishing/interactions for Curator testing;
- actual stability must be proven locally before it becomes a supported adapter.

### C. Bilibili search/transcript — `XZXZZX-Ai/bilibili-mcp`

Role:

- topic search → video candidate → transcript/context/evidence-link workflow;
- can retrieve transcript, metadata, chapters and selected comments;
- current project includes handling for some HTTP 412 subtitle failures.

Why it is interesting:

- directly addresses the failure observed when ordinary browser access could discover videos but could not reliably read them;
- active current maintenance;
- Apache-2.0 on current main.

Pilot pin observed 2026-08-29:

`b25b394bce0d05973a8afd7029651509bf407567`

Pilot policy:

- use search/transcript only;
- do not treat video popularity as quality evidence;
- transcript still needs Curator evaluation for task fit and practical value.

## 8. Candidates not selected as first pilot defaults

### WeChat Official Studio MCP

Useful for the owner's own public-account operations and reading known public article URLs, but it bundles write/upload/draft capabilities and does not solve arbitrary cross-account discovery as cleanly as the narrower WeChat search Skill.

Not first pilot default.

### Full historical WeChat crawlers / RSS sync

Potentially useful for deep research on known accounts, but they introduce persistent local storage and long-running sync behavior.

Too heavy for the first Curator adapter test.

### Xiaohongshu all-in-one publishing/analytics Skills

Many include publishing, commenting, likes, account operations or platform-specific binaries.

The first Curator pilot needs search/read only. Do not install extra social-operation capability merely because it is available.

## 9. Supply-chain and security rules

Third-party Skills are executable workflow dependencies, not harmless Markdown links.

Before local installation:

1. pin repository + commit SHA;
2. inspect `SKILL.md`, install scripts, package manifests and executable entry points;
3. identify network targets and credential/cookie locations;
4. identify write/destructive capabilities;
5. check whether binaries are downloaded or committed prebuilt;
6. prefer source-built / verifiable components where practical;
7. never commit cookies, tokens, local browser profiles or credentials;
8. use a test account where account login is required whenever practical;
9. do not silently auto-update adapters during a controlled pilot.

The installation review is mechanical/security work and may be performed by the local Codex Agent. The Product Owner should not be asked to audit package files manually.

## 10. Main architectural risks

### Risk 1 — adapter sprawl

If each failed source adds another permanent Skill, Curator becomes a tool zoo.

Mitigation:

- add adapters only for repeated material acquisition gaps;
- first pilot only WeChat / Xiaohongshu / Bilibili.

### Risk 2 — platform checklist drift

Installed adapters may tempt the Agent to query all platforms every time.

Mitigation:

- adapter trigger is evidence need, not availability.

### Risk 3 — source adapter becomes recommender

A platform-specific Skill may return rankings or summaries that bias the final answer.

Mitigation:

- treat adapter results as candidates/evidence only;
- Curator independently evaluates them.

### Risk 4 — login state mistaken for evidence quality

Successful scraping does not prove the content is useful.

Mitigation:

- acquisition success and curation quality remain separate.

### Risk 5 — hidden write capability

Social MCPs often bundle publish/interact actions.

Mitigation:

- read-only tool subset for Curator pilot;
- no write actions without explicit separate user intent.

### Risk 6 — nested Skill orchestration is unreliable

The design assumes Codex can consistently combine Curator instructions with source-specific Skills/tools.

Mitigation:

- test orchestration explicitly before implementing the final Curator Skill.

## 11. First implementation hypothesis

Do not build a custom adapter framework yet.

First test the simplest composition:

```text
Codex local environment
├─ ERP AI Curator working instructions (current docs / later Skill)
├─ WeChat search Skill
├─ Xiaohongshu search/read Skill + MCP
└─ Bilibili search/transcript Skill/MCP
```

The Curator only needs a small routing rule:

> Use an installed source adapter when its source can materially resolve a missing evidence need and normal Web access is insufficient. Use read-only acquisition. Return to Curator judgement after acquisition.

If this works reliably, no new orchestration software is needed.

If it fails repeatedly, then consider a more explicit adapter contract or orchestrator.

## 12. What must be proven before this becomes product architecture

The pilot must show all three:

1. source adapters materially improve discovery/read coverage;
2. the added evidence materially improves the final recommendation package;
3. multi-Skill routing remains simple enough that Curator does not become a complicated pipeline.

If adapters only produce more links, the architecture is not justified.
