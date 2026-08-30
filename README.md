# ERP AI Curator

面向 **SAP / Oracle / ERP / 企业信息化从业者** 的 AI 工作方式导航器。

目标不是做 AI 工具大全，而是帮助实施顾问、项目经理、产品经理、解决方案人员和开发人员回答：

> **面对这个真实工作任务，普通 AI 是否已经够用？如果不够，什么现成 Tool / Skill / 方法 / 教程最值得采用？**

## 真实任务优先

基本输入不是“需求分析 / PPT / 原型 / 数据处理”这种宽标签，而是：

```text
真实项目情境
+ 手头已有材料
+ 当前必须完成的动作
+ 下一份明确交付物
+ 真正影响方案的约束
```

## 当前真实需求来源

2026-08 培训问卷提供了 83 份目标用户反馈。

当前需求基线见：

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

问卷证明需求存在，但不证明某个 Tool / Skill / 工作流就是正确答案。

## Curator 的核心判断

### A — 普通 AI / 现有 Agent 已经够用

不搜索、不凑 Skill，直接给最小可行工作方式。

### B — 专门能力有明显增益

只有当 Tool / Skill / 方法能明显改善交付格式、准确性、重复劳动、专业交互、本地/隐私适配或现有系统连接时，才定向发现和比较。

### C — 暂不值得引入复杂方案

给低成本试验路径，并说明什么时候再升级。

## 外部资源发现原则

需要外部资源时，默认顺序：

```text
真实 practitioner 实操 / 复盘 / 案例
→ 对应 Tool / Skill / repo / 方法原始来源
→ 必要的当前官方事实核验
→ 限制 / 反证
```

关键结论必须能够回到具体来源。搜索摘要只能用于发现，不能冒充已读原文。

## 当前可信证据

### P01 — 会议/Workshop → 需求包

> **high task fit / low independent validation**

保留用于实践，不作为强验证证据。

### P04 — 业务逻辑 → 可编辑流程图

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority: `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`.

### P06 — Excel/CSV → 对账与验证

> **CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`

### P03 — 需求/规则 → 可点击原型

> **CLOSED — spec-first code prototype default; Figma Make conditional upgrade**

Authority: `docs/validation/P03_PROTOTYPE_CURATION_RESULT_02.md`.

### P07 — 代码库/程序 → 理解逻辑、反推 FS、缺陷假设

> **CLOSED — traceable read-only repo exploration default; conditional LSP/semantic or ERP-native MCP upgrade**

Authority: `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_02.md`.

当前可信结论：普通本地 Git 仓库先用 repo-aware Agent 做范围明确、只读、可追溯的分层理解；只有文本搜索/跨符号关系成为真实瓶颈时才升级 LSP/语义导航。若权威代码、where-used、ATC、测试等信息位于系统侧，ERP-native MCP 才形成实质能力增益，SAP ABAP 是当前明确例子。代码解释不等于业务意图，反推 FS 必须区分事实、推断和待业务确认项。

## 2026-08-30 纠错仍然有效

以下旧长上下文产物仍然无效：

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED**
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED**

只有 Result 02 是当前权威。

原来的“验证完成 / Minimal Curator V0.1 已验证 / 已进入 REAL USER PILOT”不会因为新 Result 02 出现而自动恢复；现在需要重新做一次跨卡片审查。

## 当前 Skill 状态

主候选：

- `skills/curating-erp-ai-resources/SKILL.md`
- metadata version: `0.5.1`

当前状态：

> **experimental candidate — cross-card reassessment pending**

多张可信卡片已经反复支持“真实任务优先、普通 AI 够用时不强推 Skill、只有真实能力缺口才升级”的方向，但还要检查候选 Skill 是否存在卡片过拟合、矛盾或框架膨胀。

## 当前阶段

当前可信受控检查点：

> **P03、P07 均已可信关闭；下一步不是默认继续做 P10，而是重新审查整个 Curator 方法是否已经足够稳定进入最小真实用户 Pilot。**

立即要回答：

- 不同任务是否反复支持相同的最小判断逻辑？
- 候选 Skill 是否忠实表达这个逻辑，而没有夹带 P03/P06/P07 的专用规则？
- 当前主要未知是否已经从“方法是否成立”转为“真实同事是否愿意采用、是否真的改善交付”？

如果答案成立，就应该进入小范围真实用户验证，而不是继续为了“更有把握”而机械增加验证卡片。

## 当前不做

没有证据证明必要性之前，不建设：

- 大型资源数据库；
- 固定 taxonomy；
- 自动 Refresh；
- 统一评分 / Gate；
- 每个候选强制 runtime test；
- unattended multi-card Loop；
- UP主/作者排行榜；
- 为了让本地 Agent 有事做而制造任务；
- 没有来源证据链却写完整 `CLOSED` 报告。

## 当前权威文档

- `docs/PROJECT_NORTH_STAR.md` — 长期产品边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前执行主线
- `docs/validation/EVIDENCE_STATUS.md` — 当前证据状态
- `docs/REBASE_AUDIT_20260830.md` — 上下文漂移纠错记录
- `docs/SESSION_HANDOFF_CURRENT.md` — 新会话交接
- `skills/curating-erp-ai-resources/SKILL.md` — 实验性候选 Skill

## 当前成功标准

> **完成跨卡片方法审查：若候选 Curator 已足够稳定/最小，则正式进入一个有边界的 REAL_USER adoption pilot；若存在实质矛盾，只做必要的窄修正后再决定。**
