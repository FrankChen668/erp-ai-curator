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

## 2. Current Skill — 0.8.1

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

0.8.0 完成 runtime simplification；0.8.1 是一条真实宿主执行缺陷的窄修正，不重新引入分类框架。

### 0.8.1 修什么

Codex Desktop 的一次真实运行日志证明：

1. `0.8.0` 与 `practitioner-discovery.md` 已实际加载；
2. 但搜索 query 把原本的“AI + 产品/ToB/ERP 工作方式”退化成纯“流程图/泳道/BPMN 最佳实践”；
3. Bilibili、公众号、小红书、知乎、人人都是产品经理、掘金/CSDN 均未被实际定向搜索；
4. 搜索结果中已出现中文 practitioner/creator 候选，但基本没有打开；
5. 最终答案再次由 official/standard/implementation 来源主导。

因此 0.8.1 只增加两个可观察执行要求：

- **query intent preservation**：AI/Agent/Tool 工作方式请求至少保留一条 `AI/tool × role/industry/artifact` 高信号 query；
- **candidate investigation**：明确找最佳实践/教程时，返回前实际打开至少一个 practitioner/creator 候选；若宿主策略/coverage/access 阻止，则明确 `coverage/policy gap`。

Authority：`docs/validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`。

## 3. What remains intentionally simple

Runtime 不恢复：

- A/B/C 强制分类；
- adoption-consistency reference；
- decision-boundaries reference；
- 平台配额；
- creator scoring；
- 固定 benchmark；
- 多套固定输出结构。

Runtime references 仍只有：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

## 4. Host/Harness issues kept outside the Skill

当前日志还暴露三类宿主风险，但没有足够证据把它们写进 Curator runtime：

- Codex Web policy 中存在 `technical questions → primary sources only`，可能与 practitioner-first 存在策略冲突；
- Graph Engineering Skill 被“多步骤任务”错误触发，属于 Skill collision / over-triggering；
- Browser/Chrome 能力存在但本次未使用，是否需要作为 source-acquisition fallback 仍未验证。

这些先记录为 host compatibility risks，不通过增加 Curator 规则解决。

## 5. Historical evidence remains bounded

Curation Pack 01 已关闭；历史 A/B 标签保留为当时分析记录，不定义 0.8.1 runtime。

当前发布边界仍是：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

## 6. Current milestone — clean host verification + continued real use

0.8.1 合并后，下一条最有价值的 evidence 是在**全新 Codex Desktop 上下文**用同一句自然问题重跑：

> “使用这个 skill 给我找下做流程图的最佳实践”

要求仅验证真实宿主行为：

- 先同步 `main` 后再启动任务；
- 不修改 Skill；
- 不复用旧搜索上下文；
- 不人为要求它必须搜某个平台；
- 记录实际 query、reference、打开候选和最终来源角色。

这不是让用户跑工具实验，而是验证本次宿主执行修正是否真正生效。

## 7. Anti-drift

新的 runtime 规则只有在真实日志能证明重复缺陷时才进入 Skill。

任何候选修正先问：

> **这是 Curator runtime 的缺陷，还是宿主 policy / search coverage / Skill collision / access 的问题？**

不能区分就先取证，不加规则。
