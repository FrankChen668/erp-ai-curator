# ERP AI Curator — Current Execution Plan

Date: 2026-08-30
Status: **CURRENT — CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

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

## 2. Current Skill — 0.8.2

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

0.8.0 完成 runtime simplification：移出 A/B/C 强制分类、adoption-consistency、decision-boundaries、多套固定输出和重复自检。

0.8.1 不恢复这些框架，只增加两条实际日志支持的执行要求：

1. **query intent preservation**：如果用户在问“用 AI/Agent/Tool 改善某工作”，practitioner discovery 至少保留一条 `AI/tool × role/industry/artifact` 高信号 query；
2. **candidate investigation**：明确找最佳实践/教程时，返回前实际打开至少一个 practitioner/creator 候选；若宿主策略/coverage/access 阻止，则明确 `coverage/policy gap`。

0.8.2 再增加三条由新鲜 0.8.1 结果直接支持的 candidate-selection 边界：

3. **audience/ecosystem fit**：用户语言、地区、职业生态明确时，同质量优先该生态 practitioner；跨语言资源只有明显更强或本地存在真实 coverage gap 时再上位；
4. **artifact fit**：候选必须真实支持用户所需交付物，不能把 SVG-only 当成 editable draw.io 等价能力；
5. **no incidental install**：用户只是找最佳实践/教程时，不因为搜索中出现 Tool/Skill 就顺手推荐安装；只有它直接解决当前工作流的具体缺口时才推荐。

Runtime references 仍只有：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

Authority：`docs/validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md`。

## 3. Why 0.8.2

新鲜 0.8.1 结果已经能找到 practitioner 内容，但最终优先推荐了日文 Qiita 实践，并附带 `html-svg-diagrams` Skill 安装建议。

这证明 discovery 有改善，但 candidate selection 仍有三个问题：

- 用户/项目明确面向中文泛 ERP / ToB / 产品经理生态，却没有优先筛同生态内容；
- 前面总结的是 editable draw.io XML，后面推荐的 Skill 核心输出是 SVG，交付物能力不一致；
- 用户没有要求新增 Tool/Skill，却出现安装命令，属于 over-tooling 风险。

这次不把“禁止日本/海外来源”写进 Skill，也不增加评分表、语言配额或新 reference。

## 4. Host/Harness risks kept outside the Skill

此前日志暴露的三类宿主风险仍保持在 Skill 外：

- Codex Web policy 可能存在 `technical questions → primary sources only` 冲突；
- Graph Engineering Skill 被“多步骤任务”错误触发，属于 Skill collision / over-triggering；
- Browser/Chrome 能力存在但是否需要 source-acquisition fallback 未验证。

不要用 Curator 规则掩盖宿主问题。

## 5. Curation Pack 01 — closed

Authority: `docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Pack：

- Case 001 — ERP 操作手册：历史 B；
- Case 002 — Oracle EBS AI 开发：历史 B；
- Case 003 — 多顾问周报/PPT 汇总：历史 A；
- Case 004 — SAP Bug 诊断/系统 evidence access：历史 A → conditional B。

旧标签保留为历史分析证据，不定义 0.8.2 runtime。

## 6. 当前里程碑 — Controlled REAL_USER_USE

受控试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

允许：

- 少量真实 ERP/企业信息化用户；
- 用户用自己的自然问题；
- 已知/批准的 Agent Skills 宿主；
- 自然接受、修改、拒绝或忽略建议；
- 记录真正会改变产品判断的反馈。

不要求：

- 固定 benchmark；
- 用户跑工具测试协议；
- 长问卷或评分；
- 为了覆盖类别继续制造 Case。

## 7. 当前最重要的未验证目标

> **Curator 是否能持续给出比普通 AI/用户自己搜索更高信任、更低噪声、更值得点击的采用/学习建议，并且这个差异足以让真实用户再次使用？**

需要 REAL_USER_USE 回答：

- 是否真正发现用户自己不容易筛到的高价值实践；
- 是否减少搜索/选型成本；
- 是否减少错装/错选工具；
- 是否漏掉企业环境/版本/权限；
- 是否降低后续返工；
- 用户是否愿意再次使用。

## 8. Cloud / Local Agent 边界

Cloud owns：

- 对自然真实反馈做证据审查；
- 当前 Web/GitHub practitioner discovery 与事实核验；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 只在真实决策依赖以下内容时接力：

- 本地项目文件/repo/runtime；
- 企业 ERP 环境；
- 当前系统元数据/日志/权限；
- Cloud 无法获得且会改变结论的受保护 evidence；
- 需要在某个具体宿主中验证 Skill/reference/Web 行为。

Agent 可用性本身不是派活理由。

## 9. Release boundary

### GO

- controlled user trial。

### HOLD

- organization-wide mandatory standard；
- “产品价值已验证”声明；
- 全宿主兼容声明；
- public/open-source release completion。

公开/open-source 发布还需要 Owner 明确 repository license；Agent 不擅自选择。

## 10. Anti-drift

真实用户未暴露必要性前，不新增：

- synthetic validation loop；
- fixed scenario taxonomy；
- scoring/Gate；
- resource database/refresh；
- mandatory runtime benchmark；
- multi-Agent orchestration；
- creator ranking；
- source-adapter framework as default architecture；
- card-specific permanent rules；
- user test protocol as Curator default output。

尤其不要把 0.8.2 扩成“中文优先评分模型”或语言/平台配额。

## 11. 下一步

0.8.2 合并后继续自然 controlled use。下一次相似资源请求重点观察：

- 是否优先出现用户职业/语言生态匹配的 practitioner；
- 海外资源是否有明确的“为什么值得越过本地候选”；
- 推荐的工具/Skill 是否真的匹配目标 artifact；
- 未要求新增能力时是否仍出现无必要安装建议。

只有重复真实缺陷再做窄修正。
