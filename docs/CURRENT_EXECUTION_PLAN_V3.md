# ERP AI Curator — Current Execution Plan V3

> Current execution authority.

## 1. Product direction

ERP AI Curator exists to help ERP / enterprise-information-system practitioners solve real delivery problems with **existing practical AI resources**.

Basic unit:

```text
real project situation
+ actual input artifacts
+ concrete task
+ expected deliverable
→ find how practitioners already solve it
→ identify the useful Tool / Skill / workflow behind that practice
→ verify only the current facts that matter
→ return a small package worth learning and trying
```

The project is a **curator**, not a generic Skill directory and not a tool certification lab.

## 2. Demand source

Primary demand source:

- 83-response training survey;
- normalized survey Problem Cards.

Authority:

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

First-wave practical problems include:

- workshop/minutes → requirement package;
- requirements → PRD / FS;
- requirements/rules → clickable prototype;
- business logic → editable process diagram;
- source materials → customer-ready PPT;
- Excel/CSV → clean / reconcile / validate;
- codebase → logic / FS / debug;
- requirement → test scenarios/cases.

## 3. Source order — practitioner first

Authority:

- `docs/SOURCE_STRATEGY_V3.md`
- `docs/CREATOR_PRIOR_STRATEGY_V3.md`

For practical questions, default search order is now:

```text
第三方攻略 / 测评 / 实战 / creator content
→ actual Tool / Skill / repository
→ official/current fact anchor
→ limitations / counter-evidence
```

This is a deliberate correction from the earlier official/original-first tendency.

The expected main learning resource is often a practitioner guide, video, case or field note. Official docs normally support current facts rather than occupy the first recommendation slot.

## 4. Platforms / access

Do not equate adapter status with platform usefulness.

Current reality:

- Bilibili practical videos can often be discovered through ordinary public Web/indexing; direct full-page/transcript access may still hit anti-bot/412 depending on the path.
- WeChat Search → Reader is qualified for original article acquisition when ordinary discovery is insufficient.
- Xiaohongshu remains an acquisition coverage gap; login/dynamic-rendering/indexing limits are not evidence that useful content does not exist.

Use the least costly path first.

Do not require every platform in every run.

## 5. Existing ecosystems — reuse, do not rebuild

There are already substantial upstream ecosystems:

- PM / AI Product Manager Skill libraries;
- Agent Skill repositories;
- Bilibili practitioner series;
- WeChat / Xiaohongshu practical creators;
- WorkBuddy practical guides / bluebooks;
- tool-specific community tutorials and reviews.

ERP AI Curator should treat them as feeder pools.

Our value is the ERP / enterprise-delivery filter:

> which one actually helps this consultant solve this specific project problem tomorrow?

Do not create another generic Prompt library, tutorial encyclopedia, influencer ranking or PM Skill catalog.

## 6. Practitioner-evidence safeguards

Practitioner-first must not become influencer-first.

For serious retained resources:

- distinguish independent practitioner evidence from author/vendor/affiliate self-promotion when materially observable;
- do not count multiple reposts/derivative demos as independent validation;
- separate stable workflow insight from version-coupled setup/UI claims;
- for installable third-party Skill/MCP/plugin/script, do a lightweight static safety review before recommending installation;
- retain only lightweight provenance such as original URL, evidence role, limitations, materially relevant version/commit and last checked date.

Important distinctions:

```text
practical usefulness ≠ independent validation
social repetition ≠ corroboration
old article ≠ useless insight
runtime test not required ≠ executable safety can be ignored
retained asset ≠ permanent approval
```

Do not add numeric scoring or a large database for these safeguards.

## 7. Testing policy — major simplification

Repeated local runtime testing is **not** the default.

Do not test every recommended Skill/Tool merely to prove the Curator designed the recommendation correctly.

Local runtime proof is justified only when:

1. credible third-party practical evidence is absent or contradictory;
2. installation / permission / privacy risk is material and static evidence cannot resolve it;
3. the training recommendation depends on exact reproducible local steps;
4. the resource is likely to become a repeated internal standard and being wrong is costly.

Otherwise:

> strong practitioner evidence + actual implementation + current fact check + limitations

is sufficient for curation.

This corrects the previous over-validation drift.

## 8. Existing pilot conclusions

### P01 — workshop → requirement package

Retained resource:

- `Convert Notes to Requirements Working Skill`

Classification:

> high task fit / low independent validation

Useful as a practical method; not an industry-standard best practice.

### P04A — business description → editable process diagram

Strong implementation candidate:

- official `jgraph/drawio-mcp` / draw.io Skill

But P04A underweighted practitioner evidence and over-weighted implementation documentation.

The missing layer is not another technical test first. The missing layer is:

> **第三方实操：别人到底怎么用 draw.io + Agent/Codex/Skill，效果如何，哪里需要修改，适不适合普通顾问。**

The previously prepared `P04B` local runtime pilot is therefore **DEFERRED / NOT NEXT**. Keep it only as an escalation path if practitioner evidence cannot resolve a material uncertainty.

## 9. Immediate next work

Stop designing more validation protocols.

Run a **practitioner-first resource curation wave** across a few survey-derived concrete problems.

Recommended next practical set:

1. P04 — 业务描述 → 可编辑流程图;
2. P03 — 需求 / PRD → 可点击原型;
3. P02 — 零散需求 → PRD / FS;
4. P05 — 项目材料 → 客户汇报 PPT;
5. Codex / WorkBuddy usage only when bound to one of these real jobs.

For each problem, aim to retain only:

- 1 strong practical guide / review / creator resource;
- the actual Skill / Tool / repository if applicable;
- 0–1 official/current fact anchor;
- 0–1 materially different alternative.

Do not run a technical certification sequence for each item.

## 10. What “good” now means

A strong package lets an ERP colleague answer:

- 谁已经这样做过？是独立使用者还是作者/厂商自己？
- 我先看哪一个攻略/视频/文章？
- 具体输入什么、怎么操作、产出什么？
- 用的是哪个 Tool / Skill？
- 有什么坑、返工点、隐私/安装成本？
- 当前官方事实有没有变化？
- 如果要安装，最低限度的企业安全边界是否看清？
- 我明天能不能拿自己的材料试？

## 11. Cloud / local split

### Cloud / ChatGPT

Owns:

- product direction;
- web / GitHub practitioner-source research;
- adversarial review;
- creator/source prioritization;
- current fact verification;
- lightweight static review for installable resources;
- GitHub maintenance;
- final curation decisions.

### Local Codex

Use only when needed for:

- local-only source adapters;
- inaccessible WeChat/Bilibili content acquisition;
- explicitly justified runtime checks;
- evidence that genuinely requires the user's environment.

Local Agent is no longer the default engine for every curation task when cloud Web can already research the sources.

## 12. Anti-drift

Stop if work turns into:

- one validation protocol per Tool;
- repeated runtime tests with no user decision value;
- official docs dominating practical recommendations;
- influencer popularity substituting for specific-content evidence;
- author/vendor self-demo being silently described as independent review;
- multiple derivative posts being counted as multiple independent validations;
- stale setup steps presented as current truth;
- recommending executable third-party code with no basic permission/data-flow inspection;
- ignoring Bilibili/WeChat/Xiaohongshu merely because an adapter is inconvenient;
- rebuilding existing PM/Agent resource catalogs;
- creator popularity ranking;
- link-count accumulation;
- retained historical assets becoming permanent answers without recheck;
- Curator synthesis presented as external experience;
- technical proof mistaken for actual colleague usefulness.

The project advances by accumulating **good practical resources for real work**, not by accumulating tests.
