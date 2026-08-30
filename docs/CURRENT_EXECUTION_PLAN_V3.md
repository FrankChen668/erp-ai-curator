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

## 2. Current Skill — 0.8.1

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- product value: **UNVALIDATED**

0.8.0 完成 runtime simplification：移出 A/B/C 强制分类、adoption-consistency、decision-boundaries、多套固定输出和重复自检。

0.8.1 不恢复这些框架，只增加两条实际日志支持的执行要求：

1. **query intent preservation**：如果用户在问“用 AI/Agent/Tool 改善某工作”，practitioner discovery 至少保留一条 `AI/tool × role/industry/artifact` 高信号 query；
2. **candidate investigation**：明确找最佳实践/教程时，返回前实际打开至少一个 practitioner/creator 候选；若宿主策略/coverage/access 阻止，则明确 `coverage/policy gap`。

Runtime references 仍只有：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

## 3. Why 0.8.1

Codex Desktop 的实际执行日志显示：

- 本次整段运行不是干净的 0.8.0 测试：前半段先用了 0.6.1/拟议 0.6.2 并做过官方导向搜索，之后才同步 `main@d6165fa` 到 0.8.0；
- 但同步后的 0.8.0 SKILL 和两个 references 确实被读取；
- 第二批 query 仍把“AI + 产品/ToB/ERP 工作方式”退化成纯“流程图/泳道/BPMN 最佳实践”；
- 中文 practitioner discovery pools 没有被实际定向展开；
- 搜索结果已经出现中文 practitioner/creator 候选，却基本没有打开；
- 最终答案再次由 official/standard/implementation 主导。

Authority：`docs/validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`。

## 4. Host/Harness risks kept outside the Skill

当前日志还暴露三类宿主风险，但证据不足以写进 Curator runtime：

- Codex Web policy 可能存在 `technical questions → primary sources only` 冲突；
- Graph Engineering Skill 被“多步骤任务”错误触发，属于 Skill collision / over-triggering；
- Browser/Chrome 能力存在但本次未使用，是否需要 source-acquisition fallback 未验证。

不要用 Curator 规则掩盖宿主问题。

## 5. Curation Pack 01 — closed

Authority: `docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

Pack：

- Case 001 — ERP 操作手册：历史 B；
- Case 002 — Oracle EBS AI 开发：历史 B；
- Case 003 — 多顾问周报/PPT 汇总：历史 A；
- Case 004 — SAP Bug 诊断/系统 evidence access：历史 A → conditional B。

旧标签保留为历史分析证据，不定义 0.8.1 runtime。

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

尤其不要因为本次日志暴露 host policy / Skill collision / Browser fallback 风险，就把这些全部写成 Curator runtime 规则。

## 11. 下一步

0.8.1 合并后，在**全新 Codex Desktop 上下文**同步最新 `main`，再用同一句自然问题重跑：

> “使用这个 skill 给我找下做流程图的最佳实践”

约束：

- 不修改 Skill；
- 不复用旧搜索上下文；
- 不人为要求必须搜某个平台；
- 只记录实际 query、reference、打开候选、最终来源角色和明确的 host policy/coverage failure。

若仍失败，再按证据区分：Curator instruction execution、host source policy、search coverage、Skill collision 或 source acquisition。不要继续凭最终答案猜根因。
