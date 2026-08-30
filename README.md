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

状态：

> **high task fit / low independent validation**

保留用于实践，不作为强验证证据。

### P04 — 业务逻辑 → 可编辑流程图

状态：

> **CLOSED — recommendation stable with explicit coverage gaps**

Authority:

- `docs/validation/P04_PRACTITIONER_CURATION_RESULT_02.md`

### P06 — Excel/CSV → 对账与验证

状态：

> **CLOSED — plain code-first default with explicit reconciliation controls; Huashu optional**

Authorities:

- `docs/validation/DELIVERY_P06_DATA_RECONCILIATION.md`
- `docs/validation/P06_LOCAL_RUNTIME_RESULT_01.md`

## 2026-08-30 纠错：P03 / P07 结论已撤回

最近一次长上下文冲刺中，P03 和 P07 被过早写成 `CLOSED`，随后又据此宣告“验证完成 / Minimal Curator V0.1 / REAL USER PILOT”。

重新审计后发现，两份结果没有保留足够可信的来源 URL / 引用 / acquisition trail，无法区分真实研究证据与模型综合。

因此：

- `docs/validation/P03_PROTOTYPE_CURATION_RESULT_01.md` — **INVALIDATED**
- `docs/validation/P07_CODEBASE_UNDERSTANDING_RESULT_01.md` — **INVALIDATED**
- “验证阶段已经完成” — **撤回**
- “Minimal Curator V0.1 已验证” — **撤回**
- “当前已经正式进入 REAL USER PILOT” — **撤回**

完整纠错记录：

- `docs/REBASE_AUDIT_20260830.md`

## 当前 Skill 状态

主候选：

- `skills/curating-erp-ai-resources/SKILL.md`
- metadata version: `0.5.1`

它保留了“真实任务 → AI 杠杆判断 → 必要时才找专门资源”的简化方向，但当前只是：

> **experimental candidate — validation incomplete**

不是已经验证完成的产品。

## 当前阶段

最后一个可信受控检查点是：

> **P06 已关闭，下一步重新执行 P03。**

P03 必须从头重新做，保留：

- 具体 practitioner URL；
- 实际读到的内容与 discovery-only 的区别；
- Tool / Skill / implementation 证据；
- 必要的当前事实核验；
- 限制 / 反证；
- 为什么可以停止。

只有存在真正会改变采用判断的材料缺口时，才做 local/runtime delta。

P03 可信关闭后，再做一个工程型异构卡（例如 P07 或 P10），之后才重新判断是否进入最小真实用户 Pilot。

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
- `docs/REBASE_AUDIT_20260830.md` — 本次上下文漂移纠错
- `docs/SESSION_HANDOFF_CURRENT.md` — 新会话交接
- `skills/curating-erp-ai-resources/SKILL.md` — 实验性候选 Skill

## 当前成功标准

当前不是证明“用户已经喜欢产品”。当前先完成可信的异构验证：

> **P03 用可审计证据得出稳定采用建议，再完成一个工程型异构卡；然后重新裁决是否进入 Minimal Curator 的真实用户 Pilot。**
