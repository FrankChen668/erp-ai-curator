# ERP AI Curator — Current Execution Plan

Date: 2026-08-31
Status: **CURRENT — CONTROLLED REAL-USER USE**

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

## 2. Current Runtime — 0.9.1

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

## 3. Why 0.9.1

0.9.0 成功改善了最严重的职责串台：新的流程图最佳实践回答不再直接变成 Skill 安装建议。

但本地执行日志证明新的答案并不是一次充分独立的 fresh curation：

- 本次只有一批 4 个宽泛 Web query；
- 没有针对 Bilibili/公众号/小红书/知乎做定向发现；
- 最终两篇人人都是产品经理文章来自本地 `rg` 找到的历史 `P04_PRACTITIONER_CURATION_RESULT_02.md`，不是本次 Web Search；
- `Castaldo-Solutions/process-builder` 同样来自历史 P04，并且本次没有重新打开；
- 最终答案还把内部 P04 validation 文件直接展示给用户；
- 当前运行没有实际 Web 访问失败可以解释这些缺口。

这暴露的核心问题是：**历史证据污染当前策展 + freshness 缺失 + 宽搜 recall 偏差**，而不是“必须补齐某几个平台”。

Cloud 在 2026-08-31 做定向 sanity search 时，立即发现本地当前候选池没有包含的近期内容，包括 2026-07 Bilibili drawio-skill 更新实战、2026-06 供应链/WMS 产品经理 CodeX→Draw.io 泳道图实战。这不证明它们一定更优，但证明 fresh discovery 可能改变 serious candidate pool，不能由旧 P04 直接继承“recommendation stable”。

## 4. Adversarial constraints

0.9.1 明确不做：

- newest-wins；
- B站/公众号/小红书/知乎固定配额；
- 大型资源数据库或自动 Refresh；
- 第三个 Router Skill；
- A/B/C runtime taxonomy；
- scoring/Gate/creator ranking；
- Browser/Graph Engineering/host-policy workaround；
- 每次把所有平台都搜一遍。

Best ≠ newest。旧资源可以继续排第一，但必须经本次 fresh evidence 与当前候选重新成立。

## 5. Host/Harness risks remain separate

此前真实日志仍暴露：

- Codex Web policy 可能存在 `technical questions → primary sources only` 冲突；
- Graph Engineering Skill collision / over-triggering；
- Browser/Chrome 是否需要 source-acquisition fallback 未验证。

这些没有足够证据成为 Curator Runtime 规则。

## 6. Curation Pack 01 / P04 historical evidence

历史 Curation Pack 与 P04 研究仍保留用于产品研究、回归和方法分析。

重要新边界：

> **历史项目证据不能成为普通用户当次外部策展的默认候选源或当前排名依据。**

若历史文件提供一个有用 URL/作者名，只能作为 lead；正常用户请求仍需当前外部重新发现/打开/核验。

## 7. Current milestone — Controlled REAL_USER_USE

受控试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

允许真实 ERP/企业信息化用户用自然问题使用；不要求固定 benchmark、工具测试协议、长问卷或为了覆盖类别继续制造 Case。

当前最重要的未验证目标：

> **Curator 是否能持续比普通 AI/自搜索更高信任、更低噪声地找到当前仍适用、真正值得学的实践，并在能力选型时减少错装/错选，且这个差异足以让真实用户再次使用？**

## 8. Cloud / Local Agent boundary

Cloud owns：

- 自然真实反馈的证据审查；
- 当前 Web/GitHub practitioner discovery 与事实核验；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 只在真实决策依赖本地 repo/runtime、企业 ERP 环境、受保护 evidence，或必须验证具体宿主 Skill trigger/reference/Web 行为时接力。

Agent 可用性本身不是派活理由。

## 9. Release boundary

### GO

- controlled user trial。

### HOLD

- organization-wide mandatory standard；
- “产品价值已验证”声明；
- 全宿主兼容声明；
- public/open-source release completion。

公开/open-source 发布仍需要 Owner 明确 repository license。

## 10. Anti-drift

真实用户未暴露必要性前，不新增：

- synthetic validation loop；
- fixed scenario taxonomy；
- scoring/Gate；
- resource database/auto refresh；
- mandatory runtime benchmark；
- 第三个 Router Skill；
- multi-Agent orchestration；
- creator ranking；
- source-adapter framework as default architecture；
- card-specific permanent rules；
- user test protocol as default output。

## 11. Next

0.9.1 合并后继续自然 controlled use。

最高价值仍是同一个原始 practice-only 请求：

> “使用这个 skill 给我找下做流程图的最佳实践”

观察：

- 是否先做本次 fresh external discovery，而不是从 P04/history 继承候选；
- 宽搜漏掉中文 practitioner 生态时是否出现有选择的 targeted recall；
- 最终每个外部资源是否都在本次重新打开；
- 是否考虑近期/当前适用性，而不是默认沿用历史排序；
- 最终用户回答是否不再出现内部 validation 链接。

如果仍失败，优先取实际 search/open/source 日志，再决定下一步；不根据最终答案继续盲加规则。
