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

1. credible third-party practical evidence is absent or contradictory after reasonable practitioner discovery;
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

The previously prepared `P04B` runtime pilot remains:

> **DEFERRED / escalation only**

### P04 practitioner-first wave

Verdict:

> **USEFUL WITH GAPS / GOAL NOT YET COMPLETE**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_01.md`

Retained:

- `Castaldo-Solutions/process-builder` — strong task-fit implementation/method candidate, but author self-practice rather than independent validation;
- official `jgraph/drawio-mcp` — implementation/current-fact anchor;
- Anttu draw.io MCP article — useful technical operation/troubleshooting companion, but not enough as the primary business-process/ERP practice guide.

The run did not complete the practitioner-first objective because it stopped discovery too early. A later cloud falsification search immediately surfaced relevant Bilibili PM/draw.io practical content through ordinary public Web.

Do not rerun the technical part of P04.

## 9. Immediate next work

Do **one narrow P04 practitioner-evidence delta**, not another full validation round.

Goal:

> fill the missing independent-practice layer for `业务描述/需求 → 可编辑流程图`.

Only do:

1. inspect 2–4 high-signal Bilibili / Chinese practitioner candidates already discoverable through ordinary Web;
2. prioritize PM / consultant / enterprise-workflow walkthroughs over tool-author self-demos;
3. use WeChat Search → Reader only if a concrete high-value article needs full-text acquisition;
4. compare those practical resources against the already-retained Castaldo + Anttu package;
5. retain at most one primary practical guide and one materially different companion.

Do **not** repeat:

- draw.io official capability research;
- static inspection already completed for retained candidates;
- runtime certification;
- P04B;
- new validation framework design.

When the practitioner layer is either filled or clearly remains a coverage gap, close P04 and move on to:

1. P03 — 需求 / PRD → 可点击原型;
2. P02 — 零散需求 → PRD / FS;
3. P05 — 项目材料 → 客户汇报 PPT;
4. Codex / WorkBuddy usage only when bound to one of these real jobs.

For each problem, aim to retain only:

- 1 strong practical guide / review / creator resource;
- the actual Skill / Tool / repository if applicable;
- 0–1 official/current fact anchor;
- 0–1 materially different alternative.

Do not run a technical certification sequence for each item.

## 10. Loop Engine position — use the thinking, not an autonomous infinite loop

Loop Engine is useful **as a bounded curation execution pattern**, not as a self-governing research engine.

Why it helps:

- Problem Cards repeat the same broad sequence;
- discovery may need more than one pass when the first result set is biased or shallow;
- a loop can explicitly ask whether a new search pass would materially change the recommendation;
- it can reduce manual re-prompting once the curation pattern is stable.

Why full autonomy is premature now:

- P04 exposed that Discovery Recall is still unstable;
- the Agent can stop early after finding one technically complete candidate;
- source-quality judgement remains high-judgement work;
- an automated loop would amplify official/GitHub/Codex bias or shallow social repetition if the stopping logic is wrong.

### Allowed bounded loop

Within **one Problem Card**:

```text
Problem Card
→ practitioner discovery pass
→ inspect serious original Tool/Skill/method
→ fact/safety check only where needed
→ ask: is a material practitioner/source gap still unresolved?
    → yes: one targeted delta discovery pass
    → no: package recommendation
→ adversarial stop check
→ stop and return for cloud/Owner review
```

The loop should optimize **decision completeness**, not number of sources.

### Stop conditions

Stop when either:

- there is a strong practical resource + linked implementation when applicable + necessary current facts + known limitations, and additional search is unlikely to change the user decision; or
- a material coverage gap remains after reasonable targeted discovery and is explicitly recorded.

### Forbidden autonomous behavior

Loop Engine must not, by itself:

- process many Problem Cards indefinitely;
- modify project principles or write new governance rules;
- declare the overall product PASS;
- install new Skills/MCPs/adapters;
- trigger runtime tests without an explicit escalation reason;
- turn platform coverage or source count into a target;
- convert retained historical resources into permanent recommendations;
- keep looping merely because more links can be found.

### Adoption sequence

Current recommendation:

1. finish the P04 practitioner-evidence delta manually/supervised;
2. run 1–2 additional Problem Cards with the same curation discipline;
3. if the stop logic and source judgement stay stable, then use Loop Engine to batch **bounded single-card curation loops**, with cloud/Owner review between cards or small batches.

So the current decision is:

> **YES to Loop Engine thinking; NOT YET to unattended multi-card Loop Engine execution.**

## 11. What “good” now means

A strong package lets an ERP colleague answer:

- 谁已经这样做过？是独立使用者还是作者/厂商自己？
- 我先看哪一个攻略/视频/文章？
- 具体输入什么、怎么操作、产出什么？
- 用的是哪个 Tool / Skill？
- 有什么坑、返工点、隐私/安装成本？
- 当前官方事实有没有变化？
- 如果要安装，最低限度的企业安全边界是否看清？
- 我明天能不能拿自己的材料试？

## 12. Cloud / local split

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

## 13. Anti-drift

Stop if work turns into:

- one validation protocol per Tool;
- repeated runtime tests with no user decision value;
- official docs dominating practical recommendations;
- influencer popularity substituting for specific-content evidence;
- author/vendor self-demo being silently described as independent review;
- multiple derivative posts being counted as multiple independent validations;
- stale setup steps presented as current truth;
- recommending executable third-party code with no basic permission/data-flow inspection;
- one failed URL/platform path being treated as evidence that practitioner content is unavailable;
- ignoring Bilibili/WeChat/Xiaohongshu merely because an adapter is inconvenient;
- rebuilding existing PM/Agent resource catalogs;
- creator popularity ranking;
- link-count accumulation;
- retained historical assets becoming permanent answers without recheck;
- Curator synthesis presented as external experience;
- technical proof mistaken for actual colleague usefulness;
- Loop Engine optimizing iteration count/source count instead of user decision quality;
- unattended loops changing product rules or expanding scope.

The project advances by accumulating **good practical resources for real work**, not by accumulating tests or loop iterations.
