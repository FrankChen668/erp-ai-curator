# ERP AI Curator — Current Execution Plan

Date: 2026-08-30
Status: **CURRENT — CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 1. Product objective

> **面对真实 ERP / ToB / 企业信息化工作任务，帮用户找到最值得学习/采用的现成 AI 实践与资源，并判断是否真的需要新增能力。**

Runtime main chain:

```text
real task / role / artifact / current toolchain / hard constraints
→ understand whether the user wants practices, adoption advice, or both
→ practitioner-first discovery when practices are requested/material
→ verify serious candidates and decision-changing current facts
→ select a small number of high-fit recommendations
→ stop
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. Current Skill — 0.8.0

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

0.8.0 是 runtime simplification，不是新方法扩张。

已移出 runtime 主流程：

- A/B/C 强制分类；
- adoption-consistency reference；
- decision-boundaries reference；
- 多套固定输出结构和重复自检。

仍保留的核心行为：

1. 从用户真实任务、当前工具和关键约束出发；
2. 用户明确找最佳实践/教程时，真正完成 practitioner/resource curation；
3. 新 Tool/Skill 只有在当前工具存在重要能力缺口且值得采用成本时才推荐；
4. practitioner/author/implementation/official/synthesis 证据角色不混淆；
5. 只核验 serious candidates 和会改变选择的当前事实；
6. 强匹配优先，少推荐，结论稳定即停。

Runtime references 只保留：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

## 3. 为什么做 0.8.0

0.7.0/0.7.1 的真实使用暴露了一个更高层问题：每次失败后加规则虽然局部正确，但逐渐形成 patch-on-patch 的认知复杂度。

对照 OpenAI / Anthropic Skill Creator 和 Agent Skills progressive-disclosure 范式，本轮校准结论是：

> **项目仓库可以复杂；runtime Skill 必须只保留模型真正需要的核心程序性知识。**

0.8.0 不用另一套新 taxonomy 替换旧 taxonomy，而是恢复高自由度 judgment skill 应有的少量启发式。

Authority：`docs/validation/CURATOR_080_RUNTIME_SIMPLIFICATION.md`。

## 4. Historical evidence remains valid but not runtime logic

Curation Pack 01 已关闭：

- Case 001 — ERP 操作手册：历史 B；
- Case 002 — Oracle EBS AI 开发：历史 B；
- Case 003 — 多顾问周报/PPT 汇总：历史 A；
- Case 004 — SAP Bug/system evidence access：历史 A → conditional B。

这些标签保留为当时的分析记录，不再要求 0.8.0 runtime 先产生 A/B/C。

## 5. Current milestone — Controlled REAL_USER_USE

真实用户直接用自然问题。

重点观察：

- 是否真正找到用户想看的 practitioner 实践；
- 是否减少搜索和筛选成本；
- 是否过度推荐新工具；
- 是否漏掉版本/权限/数据边界；
- 用户是否愿意再次使用。

不要求用户跑固定 benchmark、工具测试协议或复杂评分。

## 6. Cloud / Local boundary

Cloud 自动处理：

- Web/GitHub discovery 与事实核验；
- 真实反馈的证据审查；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 仅在推荐真正依赖本地 repo/runtime、企业 ERP 环境、受保护 evidence，或必须验证某具体宿主的 Skill/reference 路由时接力。

## 7. Anti-drift

真实使用未证明必要前，不新增：

- 新分类框架 / Gate / scoring；
- synthetic benchmark loop；
- resource database / auto refresh；
- creator ranking；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- card-specific permanent rules。

任何新 runtime 规则进入 Skill 前先问：

> **删掉它，真实用户结果会明显变差吗？**

不能明确回答“会”，默认不加。

## 8. Next

1. 完成 0.8.0 simplification PR + Project Contract；
2. 用既有真实问题做 bounded regression，验证“删规则但不丢关键行为”；
3. 合并后继续 controlled real-user use；
4. 只有新的真实使用缺陷才触发下一版。
