# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Current product direction

ERP AI Curator is a **bounded Curator / Orchestrator hypothesis** for泛 ERP / 企业信息化工作。

Its job is:

> **Given a real work problem, help the user choose the most useful AI working approach; when external resources are actually needed, find and curate a small number of resources worth learning, trying or sharing.**

Current flow:

```text
real work problem
→ understand outcome + constraints
→ compare current AI/tool baseline
→ Mode A / B / C
→ if external discovery is needed:
     normal Web + GitHub first
     + approved read-only source adapters only when a material coverage gap exists
→ compare evidence
→ small actionable recommendation package
```

Curator owns judgement. Source adapters only acquire evidence.

## 2. What is already supported

### Product / curation

- Resource-first Phase 2/3 was too narrow.
- Heavy Gate / scoring / candidate JSON governance is a demonstrated failure mode.
- Official sources are fact anchors, not automatic recommendation winners.
- T01 exposed discovery-recall risk.
- T02 exposed task-fit vs maturity risk.
- Chinese practitioner-content gaps mix access, indexing and true quality/scarcity; `not found` does not mean `does not exist`.

### Source adapter qualification

First Windows + Codex qualification:

- WeChat discovery: **CONDITIONAL**.
- WeChat public article reader: **KEEP FOR PILOT**.
- `XZXZZX-Ai/bilibili-mcp`: **CONDITIONAL**, real search blocked by `COOKIE_EXPIRED`.
- `xpzouying/xiaohongshu-mcp`: **REMOVE**, broad write/account surface failed the research-only boundary.

### Multi-Skill routing

Phase 3A result: **PASS** for the WeChat chain.

Observed in one task:

```text
Curator evidence need
→ wechat-article-search
→ direct mp.weixin.qq.com candidate
→ wechat-article-reader
→ original article body + metadata
→ Curator judgement
→ stop
```

Bilibili/Xiaohongshu were not called. Search snippet was not substituted for original content.

This proves bounded composition for this chain only. It does **not** prove arbitrary Skill orchestration or user-value uplift.

See:

- `docs/validation/SOURCE_ADAPTER_QUALIFICATION_RESULT_01.md`
- `docs/validation/SOURCE_ADAPTER_ROUTING_RESULT_01.md`

## 3. Current provider state

```text
wechat_discover_public_articles
  zjp1997720/wechat-article-search → CONDITIONAL

wechat_read_public_article
  Githun1314/agent-wechat-reader → KEEP FOR PILOT

bilibili_search_public_videos / bilibili_read_transcript
  XZXZZX-Ai/bilibili-mcp → CONDITIONAL / credential blocked
  sandraschi/bilibili-mcp → cloud-reviewed alternative; separate local qualification later

xiaohongshu_search_public_notes / xiaohongshu_read_public_note
  xpzouying/xiaohongshu-mcp → REMOVED
  replacement → none approved
```

Do not weaken permission boundaries to regain platform coverage.

## 4. Phase map

### Phase 0 — V3 product reset

**DONE**

### Phase 1 — resource-curation behaviour (T01/T02)

**DONE ENOUGH TO MOVE ON**

Do not keep re-searching those topics.

### Phase 2 — source-adapter qualification

**FIRST RUN DONE**

Enough evidence exists to test value with the WeChat chain.

### Phase 3A — WeChat multi-Skill routing

**DONE / PASS**

Routing feasibility is no longer the next uncertainty.

### Phase 3B — Bilibili alternative

**NON-BLOCKING / LATER**

Cloud static review of `sandraschi/bilibili-mcp` found an anonymous read path worth a separate local qualification, but it also exposes broader local-LLM/web/shutdown/cache surfaces. Do not install it as part of Phase 4.

### Xiaohongshu

**COVERAGE GAP / RESEARCH ONLY**

No approved replacement. Do not install a high-risk crawler merely to fill coverage.

### Phase 4 — curation uplift paired A/B

**NEXT / LOCAL**

Question:

> Does the qualified WeChat adapter chain materially improve the final ERP resource-curation package over normal Web/GitHub discovery alone?

Protocol:

`docs/validation/CURATION_UPLIFT_AB_TEST_01.md`

Fresh task:

> 请为泛 ERP / 企业信息化从业者寻找：能够帮助实施顾问、产品经理或开发人员借助 AI 快速理解一个陌生 ERP 模块或定制企业系统的优秀 Skill、Tool、方法和实战资源。目标包括快速建立端到端业务流程、角色/单据/主数据、配置或代码逻辑、接口上下游、异常场景的认识，并能验证自己的理解，而不是让 AI 凭记忆解释。最终只保留真正值得采用、学习或分享给同事的少量资源。

Run A:

- fresh isolated session;
- normal Web/GitHub only;
- source adapters unavailable;
- freeze output before Run B.

Run B:

- separate fresh isolated session;
- same raw task/model/config/repo commit;
- normal Web/GitHub + qualified WeChat chain available;
- do not force WeChat use;
- do not read Run A output.

Local Agent produces both frozen outputs and observable acquisition traces. It does **not** judge which run wins.

Cloud then adversarially compares:

- serious candidates gained;
- original practitioner evidence gained;
- recommendation/confidence/limitations materially changed;
- share-worthiness improved;
- maintenance/research overhead justified.

Valid cloud verdicts:

- `MATERIAL UPLIFT`
- `LIMITED UPLIFT`
- `NO MATERIAL UPLIFT`
- `INVALID TEST`

### Phase 5 — repeat fresh tasks

**FUTURE / ONLY IF PHASE 4 SHOWS MATERIAL VALUE**

Repeat on 1–2 genuinely different real tasks before generalizing.

### Phase 6 — packaging decision

**FUTURE**

Only after repeated evidence choose:

1. build minimal Curator Skill;
2. keep as working method/docs;
3. keep selective adapters only;
4. drop adapter layer.

Do not implement a production Skill merely because routing works.

## 5. Responsibility split

### Cloud / ChatGPT

Owns:

- product direction;
- first-principles/adversarial review;
- upstream candidate/static research;
- evidence interpretation;
- KEEP / CONDITIONAL / REMOVE decisions;
- A/B comparison;
- GitHub docs/PR/merge.

Continue autonomously unless a real Owner decision is required.

### Local Codex

Owns only local-runtime facts/actions:

- sync exact repo state;
- installed Skill/MCP runtime;
- read-only smoke/routing/A-B execution;
- isolated sessions;
- observable evidence/artifacts.

Does not redefine V3, install unassigned adapters, change pins, or declare product PASS.

### Product Owner

Only:

- unavoidable QR/login/account approval;
- privacy/enterprise approval;
- final human usefulness judgement when genuinely needed;
- ambiguous business semantics.

## 6. Dependency/runtime rules

During normal curation:

- use only already-qualified installed adapters;
- do not install/update dependencies mid-task;
- no auto-update;
- no social/write actions;
- Web/GitHub remains default when sufficient;
- adapter failure degrades honestly to normal sources / Coverage Gap.

Installation/update remains a separate maintenance activity under `SOURCE_ADAPTER_LIFECYCLE_V3.md`.

## 7. Immediate action

### Cloud — done

- recorded Phase 3A PASS with narrow evidence boundary;
- designed the Phase 4 paired A/B protocol;
- kept Bilibili replacement and Xiaohongshu research off the critical path.

### Local — next

Execute `CURATION_UPLIFT_AB_TEST_01.md` exactly.

Stop after Run A and Run B outputs are frozen and reported.

Do not:

- compare/judge A vs B locally;
- run Phase 5;
- install Bilibili/Xiaohongshu replacements;
- modify product rules.

## 8. Anti-drift checks

Stop if the work turns into:

- resource database construction;
- platform quotas;
- adapter package manager;
- automatic adapter updates;
- every-platform search;
- link-count scoring;
- source adapter making final recommendations;
- local PASS treated as independent-user validation.

The project advances only when the next action reduces uncertainty about real user value or runtime feasibility.
