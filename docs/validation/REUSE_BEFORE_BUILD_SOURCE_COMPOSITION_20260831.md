# Reuse-Before-Build Source Composition Decision

Date: 2026-08-31
Status: **CURRENT ARCHITECTURE CORRECTION — MATURE SKILL COMPOSITION FIRST**

## 1. Trigger

The P0–P4 source-acquisition work proved a real Chinese-platform coverage gap, but it also exposed an engineering trap:

- qualifying one provider per platform created installation, build, browser, credential and supply-chain work that is outside the Curator's product value;
- Xiaohongshu provider qualification consumed substantial setup effort without reaching content evidence;
- WeChat showed one positive task and one metadata-only / anti-spider task;
- Bilibili already had useful normal-Web discovery plus partial anonymous enrichment.

The product does not need to own platform acquisition implementations.

## 2. First-principles correction

ERP AI Curator is a judgement/orchestration Skill.

It should ask:

> What evidence is missing, and is there already a mature installed Skill that can acquire it?

The default order becomes:

```text
Curator
  → normal Web / GitHub
  → mature external research Skill when Chinese-platform recall is materially weak
  → mature browser-access Skill only when a serious candidate requires dynamic/login-state reading
  → Curator independently evaluates the returned evidence
```

**Reuse before build.** Do not build, fork, package-manage or maintain one provider per platform unless repeated live evidence proves no mature composition can solve the gap.

## 3. Primary mature composition candidates

### A. Cross-platform discovery — `Jesseovo/last30days-skill-cn`

Observed 2026-08-31:

- Agent Skill, MIT;
- current reviewed main: `1a8a04c3c347defbcdbb8da26d7cf1a531426b1f`;
- covers Weibo, Xiaohongshu, Bilibili, Zhihu, Douyin, WeChat, Baidu and Toutiao;
- supports source selection, recency windows, compact/JSON/Markdown output and diagnostics;
- has public project evidence of a substantial user/community footprint and automated tests;
- most sources have fallback paths; optional credentials/crawler modes improve coverage.

Role in Curator:

> **candidate discovery / recall expansion only.**

Its engagement/recency/relevance scoring is a discovery hint. Curator must not inherit its ranking as the final "best practice" decision.

### B. Dynamic/original-page reading fallback — `eze-is/web-access`

Observed 2026-08-31:

- MIT;
- current reviewed main: `33eef84a55b1919396a80e7a55650a07bb83f590`;
- large active community;
- supports normal search/fetch plus CDP access to the user's existing Chrome/Edge browser;
- explicitly targets dynamic/login-state sites including Xiaohongshu and WeChat;
- avoids requiring a separate platform-specific browser runtime.

Role in Curator:

> **read a serious candidate when static Web cannot inspect the original page.**

It is a fallback, not the global networking owner. On hosts with native browser capability, use native browser first when it already satisfies the need.

Read-only Curator use means no publish, upload, comment, like, favorite, follow, message or other account mutation.

## 4. What not to do now

Do not:

- create an ERP-owned Xiaohongshu/WeChat/Bilibili crawler;
- fork a third-party source project merely to make the pilot pass;
- build a permanent source-adapter registry/framework;
- install three platform MCPs because three platforms exist;
- make platform coverage a quota;
- let an external research Skill's popularity/engagement score decide the final recommendation;
- let `web-access` replace host-native Web/Browser by default;
- modify Runtime 0.9.1 before composition behavior is proven in the actual host.

## 5. Relationship to P0–P4 evidence

P0–P4 remain valid evidence. Their architectural meaning changes:

- P0 proves normal broad Web can miss Chinese practitioner ecosystems;
- P1/P4 prove a source can improve recall while original-content reliability varies;
- P2 proves some platform evidence can be obtained cheaply without full credential setup;
- P3 proves provider setup cost itself can outweigh potential source value.

Those findings argue for **composition and substitution**, not ERP-owned adapter engineering.

## 6. Qualification strategy from here

The next test is black-box Skill composition, not provider implementation qualification.

### Stage 1 — `last30days-cn`

Use the current flowchart or requirements task as a normal Curator request and invoke the mature Skill only to expand Chinese-platform candidate recall.

Success means it supplies serious new candidates/provenance with low setup cost.

### Stage 2 — `web-access` only if needed

If one of the strongest candidates cannot be read through normal host Web/Browser, use `web-access` against the user's existing browser in read-only mode.

Success means it reads enough original content for Curator judgement without platform-specific runtime engineering.

Stop if Stage 1 already provides enough evidence.

## 7. Promotion condition

Only after composition works in the target host should Runtime gain a small routing rule such as:

> When normal Web materially misses Chinese practitioner evidence, use an already-installed mature Chinese-platform research Skill for candidate discovery. For a serious dynamic/login-state source that cannot otherwise be inspected, use an already-installed browser-access Skill read-only. Return all evidence to Curator judgement; do not install or update Skills during a normal curation request.

Do not hard-code repository names into the core product logic unless host routing requires a maintained reference.

## 8. Current decision

> **STOP SOURCE-ADAPTER ENGINEERING. TEST MATURE SKILL COMPOSITION.**

Runtime 0.9.1 remains frozen during this test.
