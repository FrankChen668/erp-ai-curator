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

2026-08 培训问卷提供了 83 份目标用户反馈，需求基线见：

- `docs/validation/SURVEY_DERIVED_PROBLEM_CARDS_01.md`

问卷证明需求存在，但不证明某个 Tool / Skill / 工作流就是正确答案。

## Curator 的核心判断

### A — 普通 AI / 现有 Agent 已经够用

不搜索、不凑 Skill，直接给最小可行工作方式。

### B — 专门能力有明显增益

只有当 Tool / Skill / 方法解决了一个具体能力缺口，例如可编辑格式、可验证性、专业交互、本地/隐私、系统访问或深度集成时，才定向发现和比较。

### C — 暂不值得引入复杂方案

给低成本试验路径，并说明什么条件出现后再升级。

## 外部资源发现原则

真正需要外部资源时，默认顺序：

```text
真实 practitioner 实操 / 复盘 / 失败案例
→ 对应 Tool / Skill / repo / 方法原始实现
→ 只核验会改变采用判断的当前官方事实
→ 限制 / 反证
```

搜索摘要只能用于发现，不能冒充已读原文。

## 当前可信证据

已完成一组异构真实任务/代表性任务验证：

- **P01 会议/Workshop → 需求包**：高任务匹配 / 低独立验证；
- **P04 业务逻辑 → 可编辑流程图**：CLOSED；
- **P06 Excel/CSV → 对账与验证**：CLOSED，包含受控 runtime delta；
- **P03 需求/规则 → 可点击原型**：CLOSED，clean Result 02；
- **P07 代码库/程序 → 理解逻辑、反推 FS、缺陷假设**：CLOSED，clean Result 02。

当前证据状态：

- `docs/validation/EVIDENCE_STATUS.md`

P03/P07 的旧 Result 01 仍然 **INVALIDATED**，不得作为产品证据。

## 跨卡片结论

Authority:

- `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md`

当前结论：

> **METHOD READY FOR REAL-USER PILOT — PRODUCT OUTCOME NOT YET VALIDATED**

不同任务反复支持同一最小方法：

1. 从真实任务、材料、交付物和约束出发；
2. 普通 AI / 现有 Agent 是基线，不是退而求其次；
3. 专门方案必须对应具体瓶颈；
4. 重要产物必须回到项目/source/system 证据；
5. 事实、推断和未知不要混写；
6. runtime/local test 只在可能改变采用判断时做；
7. 同事下一步行动稳定后停止，不继续堆资源。

因此当前不再默认继续做 P10 等内部验证卡片。

## Minimal Curator V0.1

当前 Skill：

- `skills/curating-erp-ai-resources/SKILL.md`
- version: `0.6.0`
- status: **Minimal Curator V0.1 — real-user pilot candidate**

这表示**方法已经足够稳定进入 Pilot**，不表示真实用户价值已经被证明。

Skill 保留跨任务稳定原则，不把 P03/P04/P06/P07 的具体答案积累成永久场景规则。

## 当前阶段 — REAL_USER Pilot

Pilot 说明：

- `docs/REAL_USER_PILOT_V1.md`

当前最重要的未知已经从：

> “这套方法能不能在不同任务上成立？”

转为：

> **“真实 ERP/企业信息化同事会不会采用这个建议，它是否真的减少选错工具、搜索/配置成本或后续返工？”**

下一份有效证据应该来自真实同事的真实任务：

```text
真实任务
→ Curator 推荐
→ 同事实际尝试 / 修改 / 拒绝
→ 可用结果或失败原因
→ 检查节省/新增的搜索、配置、返工成本
→ 必要时窄修正方法
```

不要求用户先选择 Problem Card，也不为了覆盖类别制造测试题。

## 当前不做

在真实使用证明必要性之前，不建设：

- 大型资源数据库；
- 固定 taxonomy；
- 自动 Refresh；
- 统一评分 / Gate；
- 每个候选强制 runtime test；
- unattended multi-card Loop；
- UP主/作者排行榜；
- 多 Agent 编排；
- 为了保持 Agent 忙碌而制造任务；
- 没有真实用户阻塞却重新回到内部验证卡片积累。

## 当前权威文档

- `docs/PROJECT_NORTH_STAR.md` — 长期产品边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前执行主线
- `docs/validation/EVIDENCE_STATUS.md` — 当前证据状态
- `docs/validation/CROSS_CARD_METHOD_REASSESSMENT_20260830.md` — Pilot readiness 裁决
- `docs/REAL_USER_PILOT_V1.md` — 当前真实用户 Pilot 合同
- `docs/SESSION_HANDOFF_CURRENT.md` — 新会话交接
- `docs/REBASE_AUDIT_20260830.md` — 历史上下文漂移纠错
- `skills/curating-erp-ai-resources/SKILL.md` — Minimal Curator V0.1 Pilot Candidate

## 当前成功标准

> **让真实同事把 Minimal Curator V0.1 用在真实工作任务上，取得第一批 adoption/outcome 证据；不要再用更多内部自测替代真实使用。**
