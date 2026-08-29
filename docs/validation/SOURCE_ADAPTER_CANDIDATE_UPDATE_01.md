# Source Adapter Candidate Update 01 — WeChat discovery + reader

> Status: current pilot evidence. This note refines the WeChat part of `SOURCE_ADAPTER_ARCHITECTURE_V3.md` and `SOURCE_ADAPTER_PILOT_V3.md` without changing the overall architecture.

## 1. Why the WeChat adapter should be split

A single WeChat tool does not need to own discovery, reading and account operations.

For ERP AI Curator the cleaner pilot chain is:

```text
keyword / topic
    ↓
wechat-article-search
    ↓
public mp.weixin.qq.com candidate URL
    ↓
wechat-article-reader
    ↓
original article evidence
    ↓
Curator judgement
```

This keeps each capability narrow and read-only.

## 2. Discovery Skill

Repository:

`zjp1997720/wechat-article-search`

Pinned pilot commit:

`7e1be9a0d5b5a9e6835c83cddb2d79bb9c9fe6b6`

Role:

- keyword discovery through Sogou WeChat Search;
- return title, summary, publish time, source account and link;
- attempt to resolve direct WeChat article links when possible.

Remote static check:

- MIT;
- package dependency at the pinned commit is `cheerio`;
- no package install script was present in the inspected package manifest;
- network path is HTTPS-based Sogou/WeChat discovery;
- anti-bot/rate-limit behavior remains a known reliability risk.

This Skill is **discovery evidence**, not proof that the article body has been read.

## 3. Reader Skill

Repository:

`Githun1314/agent-wechat-reader`

Pinned pilot commit:

`0d5b167239f135934dced0411b0fb887d35bf9be`

Skill path:

`skills/wechat-article-reader/`

Role:

- read public exact-host `https://mp.weixin.qq.com/...` article URLs;
- extract article metadata and clean Markdown;
- expose verification/failure status;
- provide traceable local artifacts for the current session.

Remote static check:

- MIT;
- exact host restriction to `mp.weixin.qq.com`;
- HTTPS only;
- GET only;
- bounded redirects, timeout and maximum response size;
- no cookies;
- no credentials;
- no browser/CDP control;
- no third-party mirror/reader fallback;
- verification/login/paywall response causes a stop rather than bypass attempts;
- temporary local outputs are Markdown, metadata JSON, raw HTML and trace JSON.

This is a good fit for the Curator read-only acquisition principle.

Maturity caveat:

- repository is very small/new and has little external adoption evidence;
- therefore it is a **pilot candidate**, not a trusted permanent dependency yet.

## 4. Pilot order

For WeChat qualification:

1. install the pinned discovery Skill;
2. run a harmless keyword search such as `AI 需求分析`;
3. select one public article candidate;
4. install/use the pinned reader Skill;
5. read the resolved `mp.weixin.qq.com` article;
6. confirm title / author / body are actually available;
7. compare search snippet vs full article evidence;
8. confirm neither Skill performs account writes or requires a WeChat account login.

If the discovery Skill cannot resolve a direct article URL but exposes a valid candidate link, record the failure explicitly rather than treating the article as read.

## 5. Curator routing rule

The Curator should not invoke both WeChat Skills for every task.

Use them when:

- Chinese practitioner evidence from WeChat could materially help the decision; and
- normal Web discovery/read coverage is insufficient.

Then:

- discovery Skill finds candidates;
- reader Skill reads only serious candidates;
- Curator independently decides whether the content is useful, trustworthy and worth sharing.

## 6. Why this is preferable to a large WeChat MCP for the first pilot

The Curator currently needs:

- search;
- original article reading.

It does not need:

- official-account backend login;
- draft creation;
- publishing;
- material upload;
- account analytics;
- account mutation.

The two narrow Skills therefore create a smaller permission and maintenance surface for the first experiment.

## 7. What remains local-only to prove

Cloud static review cannot prove:

- actual Windows/Codex installation behavior;
- live Sogou/WeChat accessibility from the user's network;
- Codex automatic/explicit multi-Skill routing;
- output quality on current real articles.

These belong to the next local qualification/smoke-test step.
