# ERP AI Curator — Current Execution Plan

Date: 2026-08-31
Status: **CURRENT — REUSE-BEFORE-BUILD / SOURCE COMPOSITION EFFECTIVENESS INCONCLUSIVE / CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / ToB / 企业信息化工作任务，帮用户找到真正值得学习的现成 AI 实践；当用户明确做能力选型时，再判断当前工具链是否够用、是否值得新增能力。**

Product remains one Curator with two Runtime responsibilities:

```text
Practice intent
→ curating-erp-ai-resources
→ fresh practitioner discovery / inspection / selection

Capability intent
→ advising-erp-ai-capabilities
→ current baseline / concrete gap / minimum useful upgrade or no-upgrade
```

Curator is not a crawler, source database, tool marketplace or adapter framework.

## 2. Runtime — 0.9.1 FROZEN

Practice Curator continues to require:

- fresh external discovery;
- history/validation as lead-only evidence;
- fresh inspection of final external recommendations;
- current-applicability/freshness checks when material;
- selective targeted recall correction when broad Web misses the user's obvious ecosystem;
- no platform quota;
- no default Tool/Skill/MCP adoption decision.

Capability Advisor remains:

> current baseline → concrete gap → minimum useful capability or explicit no-upgrade.

Authorities:

- `docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`
- `docs/validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md`

Release class: **CONTROLLED USER TRIAL**  
Product value: **UNVALIDATED**

## 3. Source-acquisition evidence — P0–P4 CLOSED

The investigation proved a real recall/acquisition problem, but not a need to own platform implementations.

### P0 — normal / targeted Web

Keep as default baseline.

Supported:

- broad Web can miss Chinese practitioner ecosystems;
- targeted `site:` search improves some Bilibili/Zhihu recall;
- WeChat/Xiaohongshu can remain weak or zero-recall.

### P1/P4 — WeChat provider

Provider: `zjp1997720/wechat-article-search`.

Evidence is mixed:

- P1: strong positive on the flowchart task, including new candidates and readable original content;
- P4: second ERP/ToB requirements task returned useful metadata leads, but 0 current original WeChat articles were resolved/read due Sogou anti-spider behavior; final Top 3 did not change;
- production dependency audit still reported a High transitive `undici` vulnerability, although the inspected script's active network path used Node built-in `https`.

Decision:

> **PILOT / UNSTABLE — NOT APPROVED.**

Do not make it a permanent Runtime dependency.

### P2 — Bilibili provider

Status: **CONDITIONAL**.

- normal targeted Web already finds candidates;
- anonymous metadata/comments can enrich known BVIDs;
- search/transcript credentials are not justified merely to complete a matrix.

### P3 — Xiaohongshu provider

Provider `xpzouying/xiaohongshu-mcp`: **REMOVED**.

Reason:

- broad read/write tool surface;
- no demonstrated enforceable read-only subset in target host;
- exact-pin qualification required temporary build tooling;
- first-run required a large custom browser runtime;
- setup timed out before QR/search/detail;
- operating/supply-chain cost was disproportionate.

Boundary:

> Provider removal does not mean Xiaohongshu lacks useful practitioner content. Platform coverage remains unresolved.

Authorities:

- `docs/validation/source-acquisition-pilot/P3_XIAOHONGSHU_RESULT.md`
- `docs/validation/source-acquisition-pilot/P4_WECHAT_CROSS_TASK_RESULT.md`
- `docs/validation/source-acquisition-pilot/CLOUD_ADVERSARIAL_REVIEW_20260831.md`

## 4. Architecture direction — REUSE BEFORE BUILD

The previous per-platform Adapter direction was becoming an engineering trap.

The Curator's job is not to maintain WeChat/Bilibili/Xiaohongshu acquisition implementations.

Working architecture hypothesis:

```text
Curator
→ normal Web / GitHub
→ mature external Chinese-platform research Skill when recall is materially weak
→ mature browser-access Skill only when a serious candidate requires dynamic/login-state original reading
→ Curator independently evaluates the evidence
```

Authority:

- `docs/validation/REUSE_BEFORE_BUILD_SOURCE_COMPOSITION_20260831.md`
- `docs/validation/SOURCE_COMPOSITION_UNCERTAINTY_20260831.md`

## 5. Mature Skill candidates under qualification

### Cross-platform discovery

Candidate: `Jesseovo/last30days-skill-cn`

Role:

- expand current Chinese-platform candidate recall;
- cover multiple ecosystems through one maintained external Skill;
- return leads/provenance, not final Curator judgement.

Its relevance/recency/engagement ranking is discovery-only and must not determine the final recommendation.

### Dynamic/original-page reading fallback

Candidate: `eze-is/web-access`

Role:

- use the Owner's existing Chrome/Edge through CDP when a serious dynamic/login-state page cannot otherwise be inspected;
- avoid platform-specific custom browser runtimes.

Boundary:

- host-native Browser remains preferred when sufficient;
- `web-access` is fallback, not global network owner;
- Curator usage is read-only: no publish/upload/comment/like/favorite/follow/message/account mutation.

## 6. P5 interpretation — INCONCLUSIVE / OWNER-DISPUTED

Owner-reported P5 summary says:

- Candidate A added five Bilibili candidates but did not convert them into inspectable original evidence;
- Xiaohongshu / Zhihu / WeChat showed no effective gain in that run;
- Candidate B was blocked because Chrome CDP was not enabled and therefore was not exercised;
- Local Agent proposed `CONDITIONAL`, discovery-only use.

This evidence does **not** currently justify either extreme conclusion:

- mature-Skill composition is proven sufficient; or
- mature-Skill composition is proven insufficient and Source Acquisition should be closed.

The earlier informal Cloud inference leaning toward the second conclusion is withdrawn as a project conclusion after Owner challenge.

Current status:

> **MATURE-SKILL COMPOSITION EFFECTIVENESS — OPEN / INCONCLUSIVE.**

Reason:

> the intended chain `discovery → original-page reading → Curator judgement` was not completed end to end because the reading fallback was not actually tested.

Authority: `docs/validation/SOURCE_COMPOSITION_UNCERTAINTY_20260831.md`.

## 7. Explicit boundaries while unresolved

Do not:

- build an ERP-owned social-platform crawler;
- fork platform adapters merely to make qualification pass;
- create a platform-complete adapter matrix;
- install one MCP per platform by default;
- create a custom adapter package manager/framework;
- let external Skill ranking replace Curator judgement;
- let a browser Skill replace host-native Web/Browser by default;
- patch Runtime 0.9.1 based on the reported P5 result;
- declare Source Acquisition solved or abandoned from P5 alone;
- run more synthetic platform tests simply to fill evidence slots.

Further source-composition evidence should be collected only when it can materially resolve the open question, preferably in a real ERP/ToB task where both discovery and original inspection can affect the final recommendation.

## 8. Real-user value remains the real milestone

Lane B remains the product-value authority.

The core unresolved question is still:

> **Does Curator consistently give real ERP/ToB users a more useful, current, trustworthy and lower-noise answer than ordinary AI/self-search, enough that they act on it or return?**

Source composition is enabling infrastructure. Its current effectiveness is unresolved and it is not product-value validation.

Authority: `docs/REAL_USER_PILOT_V1.md`.

## 9. Release boundary

### GO

- controlled user trial;
- bounded source-composition evidence when decision-changing.

### HOLD

- organization-wide mandatory standard;
- product-value-validated claim;
- permanent source adapter/framework claim;
- mature-Skill composition solved/failed claim;
- all-host compatibility claim;
- public/open-source release completion without explicit repository license decision.
