# ERP AI Curator — Current Execution Plan

Date: 2026-08-31
Status: **CURRENT — SOURCE ACQUISITION PILOT / CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / ToB / 企业信息化工作任务，帮用户找到真正值得学习的现成 AI 实践；当用户明确做能力选型时，再判断当前工具链是否够用、是否值得新增能力。**

Product remains one Curator. Runtime 0.9.1 uses two single-responsibility Skills:

```text
Practice intent
→ curating-erp-ai-resources
→ fresh practitioner discovery / inspection / selection

Capability intent
→ advising-erp-ai-capabilities
→ current baseline / concrete gap / minimum useful upgrade or no-upgrade
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. Current Runtime — 0.9.1 FROZEN DURING PILOT

### Practice Curator

`skills/curating-erp-ai-resources/SKILL.md`

负责：最佳实践、教程、真实 workflow/case、值得先学的 practitioner 资源。

当前关键边界：

- 本次外部策展先做 fresh discovery；
- 项目 validation/history/prior packs 只能作为线索，不能决定当前候选排序；
- 最终外部资源本次重新打开核验；
- AI 工作流快速变化时检查近期候选/发布日期/当前适用性；
- 宽搜漏掉明显用户生态时做定向 recall correction，不做平台配额；
- 普通用户答案不展示内部 validation 作为外部依据。

Reference：`references/practitioner-discovery.md`。

### Capability Advisor

`skills/advising-erp-ai-capabilities/SKILL.md`

负责：当前工具链是否够、是否存在具体能力缺口、是否值得新增 Tool/Skill/MCP/plugin/Agent/workflow、最小升级是什么。

默认不做：泛最佳实践/教程资源策展。

Reference：`references/evidence-and-safety.md`。

Release class: **CONTROLLED USER TRIAL**  
Product value: **UNVALIDATED**

Authorities：

- `docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`
- `docs/validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md`

## 3. New cross-host evidence — source acquisition is now the dominant bottleneck

After 0.9.1, the remaining issue is no longer well explained by one host or one Skill wording failure.

Observed across more than one Agent host:

- broad Web queries repeatedly return official docs, GitHub, CSDN/general blogs and a limited subset of practitioner pages;
- Xiaohongshu / WeChat public-account / Bilibili / Zhihu practitioner pools are often absent unless specifically targeted or already known;
- one fresh 0.9.0 log contained no targeted Bilibili/WeChat/Xiaohongshu/Zhihu discovery;
- a separate Agent run on 2026-08-31 showed the same broad-search pattern and similarly did not surface Xiaohongshu/WeChat/Zhihu material.

This repeated behavior is sufficient to activate the previously conditional Source Adapter hypothesis.

Important boundary:

> This does **not** prove every platform needs an adapter, or that social-platform content is better. It proves ordinary broad Web discovery may have a repeated material recall/acquisition gap for the practitioner ecosystems this product depends on.

Authority: `docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`.

## 4. Current milestone — staged Source Acquisition Pilot

Do not patch Runtime 0.9.1 during this pilot.

Pilot order:

```text
P0 targeted normal-Web baseline
→ P1 WeChat lightweight discovery qualification
→ P2 Bilibili search/transcript qualification
→ P3 Xiaohongshu isolated read-only qualification
```

### P0 — targeted Web baseline

First determine whether explicit source-qualified queries can recover useful candidates without any new dependency.

This distinguishes search-intent failure from index/acquisition failure.

### P1 — WeChat

Pilot candidate: `zjp1997720/wechat-article-search`.

Reason to start early: narrow search-only purpose, MIT, no API key, relatively low operational cost.

### P2 — Bilibili

Pilot candidate: `XZXZZX-Ai/bilibili-mcp`.

Scope: search / metadata / transcript only. Credentials remain local. Optional ASR is not required for first qualification.

### P3 — Xiaohongshu

Pilot candidate: `xpzouying/xiaohongshu-mcp`.

This addresses the hardest current discovery gap but has the highest login/browser/permission maintenance cost, so it is isolated after P0–P2. Use search/read only and a low-risk/test account where practical.

Zhihu remains normal-Web-first; no adapter is justified yet.

## 5. Pilot success condition

An adapter is only justified if it does more than increase link count.

It must:

1. acquire practitioner evidence normal Web could not reliably acquire;
2. expose enough original content/provenance for Curator judgement;
3. materially change candidate pool, ranking, rejection reason, confidence, or an explicit coverage boundary;
4. keep security/credential/maintenance cost proportionate.

If it only produces more low-quality links, do not promote it.

## 6. Source adapter architecture boundary

Existing design remains the basis:

- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

Curator owns task/evidence judgement. Adapters only own source-specific discovery/read acquisition.

Runtime use is separate from adapter maintenance:

- normal curation may use an already-qualified installed adapter when it fills a concrete evidence gap;
- normal curation does not silently install/update third-party executable dependencies;
- credentials/cookies stay local and never enter prompts or Git history;
- read-only research operations are the default.

## 7. Adversarial constraints

Current pilot explicitly does **not** add:

- newest-wins；
- platform quotas；
- “B站 + 小红书 + 公众号 + 知乎” mandatory coverage；
- resource DB / auto-refresh；
- crawler pipeline；
- creator ranking；
- third Router Skill；
- A/B/C runtime taxonomy；
- custom adapter framework before simple composition is tested；
- auto-install/update inside normal curation tasks。

## 8. Curation Pack / historical evidence boundary

Historical Curation Pack, P04 and validation documents remain project research evidence.

They may provide a lead or known-risk hint, but they do not define the current candidate pool, current ranking or current source availability.

## 9. Cloud / Local Agent boundary

Cloud owns：

- current architecture/adversarial review；
- candidate repo/current-state/security surface review；
- GitHub authority/Harness maintenance；
- final judgement on whether pilot evidence justifies promotion。

Local Agent owns only the environment-dependent qualification work：

- P0 actual target-host search behavior；
- installing/qualifying approved pilot adapters；
- client/MCP configuration；
- read-only smoke tests；
- exact search/open/tool logs。

Owner/manual action should occur only for unavoidable local credential/QR login/client restart steps. The Agent must never ask the Owner to audit package files manually.

## 10. Release boundary

### GO

- controlled user trial；
- staged local source-acquisition pilot。

### HOLD

- organization-wide mandatory standard；
- “product value validated” claim；
- all-host compatibility claim；
- permanent source-adapter architecture；
- public/open-source release completion without an explicit repository license decision。

## 11. Next

Highest-value next action is the local Source Acquisition Pilot in:

`docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`

Do **not** rerun the same prompt repeatedly without collecting source-acquisition evidence.

The next decision is not “does the answer mention Xiaohongshu?” It is:

> **Can targeted normal Web or a minimal read-only source adapter obtain serious practitioner evidence that ordinary broad Web misses, and does that evidence materially improve the Curator recommendation?**

Only after that result should Runtime, adapter routing, or product architecture change again.
