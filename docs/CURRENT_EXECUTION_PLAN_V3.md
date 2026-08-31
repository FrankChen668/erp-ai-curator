# ERP AI Curator — Current Execution Plan

Date: 2026-08-31
Status: **CURRENT — SOURCE ACQUISITION P0–P3 CLOSED / CONTROLLED REAL-USER USE**

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

## 2. Current Runtime — 0.9.1 FROZEN

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

## 3. Cross-host finding — source acquisition is a real bottleneck

After 0.9.1, repeated host evidence shows the remaining issue is not well explained by one host or one Skill wording failure.

Observed across more than one Agent host:

- broad Web repeatedly favors official docs, GitHub, CSDN/general blogs and only a subset of practitioner pages;
- Bilibili / WeChat / Xiaohongshu / Zhihu practitioner pools are often absent unless specifically targeted or otherwise known;
- targeted `site:` queries recover some Bilibili/Zhihu content but normal Web still has weak/zero recall for WeChat and Xiaohongshu;
- source-specific acquisition can materially improve evidence, but provider cost varies sharply.

Important boundary:

> This does **not** prove every platform needs an adapter, or that social-platform content is better. It proves ordinary broad Web can have a repeated material recall/acquisition gap for practitioner ecosystems this product depends on.

Authorities:

- `docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`
- `docs/validation/source-acquisition-pilot/CLOUD_ADVERSARIAL_REVIEW_20260831.md`

## 4. P0–P3 Source Acquisition Pilot — CLOSED

Runtime 0.9.1 was not patched during qualification.

### P0 — targeted normal Web

Status: **KEEP AS BASELINE / LOWEST-COST FALLBACK**

Result:

- useful recall correction;
- Bilibili/Zhihu can sometimes be discovered/read;
- insufficient for WeChat/Xiaohongshu coverage.

### P1 — WeChat

Provider: `zjp1997720/wechat-article-search`.

Cloud status: **PILOT — STRONG POSITIVE**

Result:

- credentialless discovery;
- new current-run practitioner candidates absent from P0;
- original public-account content was readable through the tested read path;
- materially improved candidate/evidence pool for the flowchart task.

Not yet `APPROVED` because repeatability across a second materially different ERP/ToB task and dependency/security closure are still missing.

### P2 — Bilibili

Provider: `XZXZZX-Ai/bilibili-mcp`.

Cloud status: **CONDITIONAL**

Result:

- known-BVID metadata/comments/chapters work without credentials;
- search/transcript require Owner-local credentials;
- targeted Web already discovers some Bilibili candidates;
- do not configure credentials merely to complete the matrix.

### P3 — Xiaohongshu

Provider tested: `xpzouying/xiaohongshu-mcp`.

Provider status: **REMOVED**

Reason:

- broad read/write MCP surface with no demonstrated practical read-only allowlist;
- exact-pin qualification required temporary Go build tooling on a host without Go;
- first-run additionally required a large custom browser runtime;
- browser acquisition timed out before QR/login/search/detail;
- operational/supply-chain/permission cost is disproportionate for the current Curator architecture.

Critical boundary:

> Provider `REMOVED` does **not** mean Xiaohongshu lacks useful content. Platform status remains **coverage gap / unqualified**.

Do not seek a replacement Xiaohongshu provider merely to complete platform coverage. Revisit only if a live task makes the missing source materially decision-changing and a substantially simpler enforceably read-only provider exists.

Zhihu remains normal-Web-first; no adapter is justified yet.

## 5. Adapter promotion success condition

An adapter is only justified if it does more than increase link count.

It must:

1. acquire practitioner evidence normal Web could not reliably acquire;
2. expose enough original content/provenance for Curator judgement;
3. materially change candidate pool, ranking, rejection reason, confidence, or an explicit coverage boundary;
4. keep security/credential/maintenance cost proportionate;
5. show repeatable value beyond a single favorable task before permanent promotion.

If it only produces more low-quality links or creates disproportionate operating complexity, do not promote it.

## 6. Source adapter architecture boundary

Existing design remains the basis:

- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

Curator owns task/evidence judgement. Adapters only own source-specific discovery/read acquisition.

Current evidence supports an asymmetric strategy:

```text
normal broad Web
→ targeted normal-Web recall when an obvious ecosystem is missing
→ qualified low-cost read-only source capability only when it can change the decision
→ Curator independently evaluates acquired evidence
```

Current provider posture:

```text
WeChat        → PILOT / strong positive
Bilibili      → CONDITIONAL / anonymous enrichment by default
Xiaohongshu   → tested provider REMOVED; platform coverage gap remains
Zhihu         → normal-Web-first
```

Runtime use remains separate from adapter maintenance:

- normal curation does not silently install/update third-party executable dependencies;
- credentials/cookies stay local and never enter prompts or Git history;
- read-only research operations are the default;
- provider qualification may reject a provider even when platform coverage would be useful.

## 7. Adversarial constraints

Current work explicitly does **not** add:

- newest-wins；
- platform quotas；
- “B站 + 小红书 + 公众号 + 知乎” mandatory coverage；
- resource DB / auto-refresh；
- crawler pipeline；
- creator ranking；
- third Router Skill；
- A/B/C runtime taxonomy；
- permanent multi-adapter framework before repeatability is proven；
- auto-install/update inside normal curation tasks；
- replacement-provider hunting merely to fill an empty platform slot。

## 8. Curation Pack / historical evidence boundary

Historical Curation Pack, P04 and validation documents remain project research evidence.

They may provide a lead or known-risk hint, but they do not define the current candidate pool, current ranking or current source availability.

## 9. Cloud / Local Agent boundary

Cloud owns：

- current architecture/adversarial review；
- candidate repo/current-state/security surface review；
- GitHub authority/Harness maintenance；
- final judgement on adapter promotion/removal。

Local Agent owns environment-dependent qualification work only when Cloud has already selected a bounded test：

- target-host search behavior；
- installing/qualifying an explicitly approved pilot adapter；
- client/MCP configuration；
- bounded read-only smoke tests；
- exact search/open/tool logs。

Owner/manual action should occur only for unavoidable local credential/QR login/client restart steps. Local qualification must not mutate the host development environment merely to make a provider test pass.

## 10. Release boundary

### GO

- controlled user trial；
- bounded source-acquisition qualification when decision-changing。

### HOLD

- organization-wide mandatory standard；
- “product value validated” claim；
- all-host compatibility claim；
- permanent source-adapter architecture；
- public/open-source release completion without an explicit repository license decision。

## 11. Next

Highest-value next evidence is **not another platform qualification**.

Next step:

> Run the WeChat PILOT on one materially different real ERP/ToB task and compare it against normal/targeted Web.

Required decision question:

> **Does WeChat acquisition again add serious, inspectable practitioner evidence that materially changes the candidate pool, ranking, rejection reason or confidence?**

Also close the reported dependency vulnerability enough to judge practical pilot safety.

Do not:

- rerun the same flowchart task merely to collect more links;
- configure Bilibili credentials without a live decision-changing need;
- search for another Xiaohongshu provider merely to complete coverage;
- patch Runtime 0.9.1 before the second-task source-acquisition evidence exists.

Only after the second-task WeChat result should Cloud decide whether a compact `source-adapter-routing` reference is justified.
