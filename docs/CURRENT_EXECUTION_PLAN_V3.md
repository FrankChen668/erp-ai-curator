# ERP AI Curator — Current Execution Plan V3

> Status: current execution authority. Product principles remain defined by `PROJECT_NORTH_STAR.md` and `AI_LEVERAGE_MODEL_V3.md`.

## 1. Product direction

ERP AI Curator is a **bounded Curator / Orchestrator hypothesis** for泛 ERP / 企业信息化工作。

Its job is:

> **Given a real work problem, help the user choose the most useful AI working approach; when external resources are needed, find and curate a small number of external resources worth learning, trying or sharing.**

Current flow:

```text
real work problem
→ understand outcome + constraints
→ compare current AI/tool baseline
→ decide whether external discovery is needed
→ normal Web/GitHub first
→ approved read-only source adapters only when a material coverage gap exists
→ compare evidence
→ small actionable recommendation package
```

Curator owns judgement. Source adapters only acquire evidence.

Important curation boundary:

> Curator-created usage guidance must be labelled as synthesis. Do not present newly invented guidance as a discovered external resource.

## 2. What is already supported

### Curation behaviour

- official/original sources are fact anchors, not automatic recommendation winners;
- T01 exposed discovery-recall risk;
- T02 exposed task-fit vs dependency-maturity risk;
- practical companion content must add real workflow/example/failure/adoption evidence;
- Chinese practitioner coverage mixes access gap, index bias and true quality/scarcity.

### Source-adapter lifecycle

Local qualification produced real provider decisions:

- WeChat discovery: **CONDITIONAL**;
- WeChat public article reader: **KEEP FOR PILOT**;
- first Bilibili provider: **CONDITIONAL / credential blocked**;
- first Xiaohongshu provider: **REMOVE**.

### Bounded composition

WeChat multi-Skill routing: **PASS** for this chain only.

```text
Curator evidence need
→ WeChat Search
→ mp.weixin.qq.com candidate
→ WeChat Reader
→ original body + metadata
→ Curator judgement
→ stop
```

This proves bounded composition, not arbitrary Skill orchestration.

## 3. Phase 4 result

`CURATION_UPLIFT_AB_TEST_01` is complete.

Verdict for the exact mixed task:

> **NO MATERIAL UPLIFT**

Reason:

- Run A used normal Web/GitHub only;
- Run B had WeChat available but did **not** invoke it;
- therefore differences between A and B cannot be attributed to adapter evidence.

Positive signal:

- Run B did not call WeChat merely because it was installed;
- conditional routing discipline held.

See `docs/validation/CURATION_UPLIFT_AB_RESULT_01.md`.

## 4. Test-design correction

The Phase 4 raw task mixed two different jobs:

1. learn an unfamiliar **standard ERP module**;
2. reverse-engineer a **custom enterprise system/codebase**.

Both runs gravitated toward codebase/process-mining evidence. That can hide weakness on the standard-ERP-learning job.

Do not repeat this mixed task.

Future validation separates the jobs by work outcome, not by role.

## 5. Current provider state

```text
wechat_discover_public_articles
  zjp1997720/wechat-article-search → CONDITIONAL

wechat_read_public_article
  Githun1314/agent-wechat-reader → KEEP FOR PILOT

bilibili
  XZXZZX-Ai/bilibili-mcp → CONDITIONAL / credential blocked
  sandraschi/bilibili-mcp → cloud-reviewed alternative; local test deferred

xiaohongshu
  xpzouying/xiaohongshu-mcp → REMOVED
  replacement → none approved
```

Do not expand adapter footprint until a task demonstrates material value.

## 6. Next phase — Standard ERP Module Diagnostic

Status: **NEXT / LOCAL**

Question:

> Can ERP AI Curator find a genuinely useful external learning package for an unfamiliar standard ERP module, and does optional WeChat practitioner evidence add material value beyond authoritative Web/GitHub sources?

This is a diagnostic follow-up because the previous mixed task did not isolate this job.

It is **not** a search for a positive adapter result.

### Test design

Use one specific unfamiliar standard ERP module/business area.

Recommended neutral task:

> A consultant who has not worked with SAP EWM must quickly understand inbound receiving and putaway: end-to-end process, roles, main business objects/documents, core configuration boundaries, key integrations, common exceptions, and how to verify understanding. Find only a small number of strong AI-enabled methods/Skills/Tools/tutorials/practitioner resources worth learning or sharing.

Why a specific module:

- prevents the Agent from escaping into generic codebase archaeology;
- exposes whether official documentation alone is enough;
- gives practitioner-source adapters a fair but non-forced opportunity to add implementation detail.

### Incremental design

Do **not** use another fully independent A/B pair as the primary causal test.

Instead:

1. **Baseline** — normal Web/GitHub discovery only; freeze candidate package.
2. **Adapter delta** — start from the frozen baseline package; allow only the qualified WeChat Search → Reader chain as new acquisition capability.
3. Ask whether newly acquired evidence changes/adds/removes any recommendation or materially strengthens practical guidance.

This isolates adapter contribution from ordinary search/model variance.

If WeChat is not useful, valid result is `NO MATERIAL DELTA`.

## 7. Next local stop point

Local Codex only executes the Standard ERP Module Diagnostic.

It must stop after producing:

- frozen baseline package;
- any WeChat evidence actually acquired;
- revised package only if evidence justifies a change;
- explicit delta trace.

Local Codex does not decide product architecture.

## 8. Cloud / local / Owner split

### Cloud / ChatGPT

Owns product direction, adversarial review, source/provider research, evidence interpretation, GitHub docs/PRs and final KEEP/REMOVE/package decisions.

### Local Codex

Owns local runtime execution, installed Skill/MCP use, isolated/frozen test artifacts and observable evidence.

### Product Owner

Only unavoidable login/privacy/business-semantics decisions and final human usefulness judgement.

## 9. Non-blocking tracks

Bilibili replacement and Xiaohongshu provider research are deferred.

Do not install more source adapters until current evidence shows a real acquisition-value gap.

## 10. Anti-drift checks

Stop if work turns into:

- resource database construction;
- platform quotas;
- adapter package manager;
- automatic updates;
- every-platform search;
- link-count scoring;
- source adapter making final recommendations;
- Curator synthesis presented as discovered external resource;
- local PASS treated as independent-user validation.

The project advances only when the next action reduces uncertainty about real user value or runtime feasibility.
