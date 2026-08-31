# Reuse-Before-Build Source Composition Decision

Date: 2026-08-31
Status: **CURRENT ARCHITECTURE HYPOTHESIS — MATURE SKILL COMPOSITION FIRST / EFFECTIVENESS UNRESOLVED**

## 1. Trigger

The P0–P4 source-acquisition work proved a real Chinese-platform coverage gap, but it also exposed an engineering trap:

- qualifying one provider per platform created installation, build, browser, credential and supply-chain work that is outside the Curator's product value;
- Xiaohongshu provider qualification consumed substantial setup effort without reaching content evidence;
- WeChat showed one positive task and one metadata-only / anti-spider task;
- Bilibili already had useful normal-Web discovery plus partial anonymous enrichment.

The product should not default to owning platform acquisition implementations.

## 2. First-principles correction

ERP AI Curator is a judgement/orchestration Skill.

It should ask:

> What evidence is missing, and is there already a mature installed Skill that can acquire it?

The working order is:

```text
Curator
  → normal Web / GitHub
  → mature external research Skill when Chinese-platform recall is materially weak
  → mature browser-access Skill only when a serious candidate requires dynamic/login-state reading
  → Curator independently evaluates the returned evidence
```

**Reuse before build.** Do not build, fork, package-manage or maintain one provider per platform unless repeated live evidence proves no mature composition can solve the gap and the product value justifies the ownership cost.

## 3. Primary mature composition candidates

### A. Cross-platform discovery — `Jesseovo/last30days-skill-cn`

Observed 2026-08-31:

- Agent Skill, MIT;
- reviewed main: `1a8a04c3c347defbcdbb8da26d7cf1a531426b1f`;
- covers Weibo, Xiaohongshu, Bilibili, Zhihu, Douyin, WeChat, Baidu and Toutiao;
- supports source selection, recency windows, compact/JSON/Markdown output and diagnostics;
- most sources have fallback paths; optional credentials/crawler modes improve coverage.

Role in Curator:

> **candidate discovery / recall expansion only.**

Its engagement/recency/relevance scoring is a discovery hint. Curator must not inherit its ranking as the final "best practice" decision.

### B. Dynamic/original-page reading fallback — `eze-is/web-access`

Observed 2026-08-31:

- MIT;
- reviewed main: `33eef84a55b1919396a80e7a55650a07bb83f590`;
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
- fork a third-party source project merely to make a pilot pass;
- build a permanent source-adapter registry/framework;
- install three platform MCPs because three platforms exist;
- make platform coverage a quota;
- let an external research Skill's popularity/engagement score decide the final recommendation;
- let `web-access` replace host-native Web/Browser by default;
- modify Runtime 0.9.1 before composition behavior is proven in the actual host.

## 5. Relationship to P0–P4 evidence

P0–P4 remain valid evidence:

- P0 proves normal broad Web can miss Chinese practitioner ecosystems;
- P1/P4 prove a source can improve recall while original-content reliability varies;
- P2 proves some platform evidence can be obtained cheaply without full credential setup;
- P3 proves provider setup cost itself can outweigh potential source value.

These findings support **reuse-before-build and asymmetric acquisition**, but they do not prove the current mature-Skill combination is sufficient.

## 6. P5 interpretation — OPEN / INCONCLUSIVE

Owner-reported P5 summary indicates:

- `last30days-cn` added five Bilibili candidates;
- those candidates did not become inspectable original evidence in that run;
- Xiaohongshu / Zhihu / WeChat showed no effective gain;
- `web-access` was blocked because Chrome CDP was not enabled and therefore was not actually exercised;
- Local Agent proposed `CONDITIONAL`, discovery-only use.

This is partial evidence only.

It does not prove composition succeeds, because the run did not demonstrate a recommendation-changing inspected evidence delta.

It also does not prove composition fails, because the intended two-layer path was incomplete:

```text
discovery candidate
→ original-page reading fallback
→ Curator judgement
```

The original-page reading fallback was not exercised.

Owner explicitly challenged the stronger interpretation that P5 justifies closing or abandoning the Source Acquisition problem. That stronger interpretation is withdrawn as a project conclusion.

Current status:

> **MATURE-SKILL COMPOSITION EFFECTIVENESS — INCONCLUSIVE / OPEN.**

Authority: `docs/validation/SOURCE_COMPOSITION_UNCERTAINTY_20260831.md`.

## 7. Promotion / rejection condition

Do not promote the mature composition into Runtime until it demonstrates, in a material task:

- serious new practitioner candidates normal Web missed;
- sufficient original content for Curator judgement;
- a meaningful change in candidate pool, ranking, rejection reason, confidence or coverage understanding;
- proportionate setup/security/maintenance cost.

Do not reject the composition strategy from a run where the reading layer was not exercised.

Do not hard-code repository names into core product logic unless host routing eventually requires a maintained reference.

## 8. Current decision

> **REUSE BEFORE BUILD REMAINS THE WORKING ARCHITECTURE PRINCIPLE. THE EFFECTIVENESS OF THE CURRENT MATURE-SKILL COMBINATION REMAINS UNRESOLVED.**

Therefore:

- do not resume platform-by-platform engineering by default;
- do not claim mature Skill composition has solved source acquisition;
- do not claim mature Skill composition has failed or that source acquisition should be abandoned;
- keep Runtime 0.9.1 frozen until evidence materially resolves the question.
