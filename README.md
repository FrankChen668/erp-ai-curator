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

例如：

> 客户 Workshop 已结束，手里有会议纪要、现状流程和附件；第二天上午要形成第一版可评审需求包。

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

Bilibili、微信公众号、小红书、YouTube、社区、博客、GitHub 等都是发现池，不设平台配额。

搜索摘要只能用于发现，不能冒充已读原文；读不到的平台记录 `Coverage gap`，不能推断平台没有好内容。

## 当前产品：Minimal Curator V0.1

主 Skill：

- `skills/curating-erp-ai-resources/SKILL.md`
- metadata version: `0.5.0`

当前用户路径已经从旧版的 Gate / 评分 / staging 采编系统，收敛成：

```text
理解真实任务
→ 判断 AI 杠杆
→ 普通 AI 是否够用？
    是 → 给最小工作方式并停止
    否 → 定向寻找实操/Tool/Skill
→ 只核验必要事实和风险
→ 默认 0–1 个主推荐
→ 给今天/明天就能执行的路径
→ 停止
```

旧 `references/`、`evals/` 和脚本保留作为历史验证/回归资产，正常用户咨询不应默认全部加载。

## 已完成的异构验证

目前方法已覆盖五种明显不同的任务：

- **P01**：Workshop / 会议纪要 → 需求包
- **P04**：业务逻辑 → 可编辑流程图
- **P06**：Excel / CSV → 对账与验证
- **P03**：需求 / 规则 → 可点击 B 端原型
- **P07**：代码库 → 业务逻辑理解 / FS / 缺陷定位

跨卡片得到的核心结论不是某个 Tool 永远最好，而是：

> **Curator 必须允许“现有 AI / Agent 已经够用”成为正式答案。**

几个稳定边界：

- 流程图：先澄清业务语义，AI 图是评审对象，不是业务真相；
- 数据对账：plain code-first 可以够用，但必须可复跑、有行数/金额/控制总额检查，模糊匹配不能猜；
- B 端原型：默认优先可持续修改的 coded prototype；已有成熟 Figma 设计体系时再倾向 Figma Make；
- 代码理解：repo-aware code Agent 通常已经够用，可靠性来自源码/测试/日志 grounding，而不是再叠加一个架构 Skill。

详细证据见 `docs/validation/`。

## 当前阶段：真实用户试用

停止为了覆盖率继续刷 Problem Card。

下一阶段只回答一个更重要的问题：

> **真实 ERP 同事会不会真的采用 Curator 的建议，并觉得它节省了搜索、学习或返工时间？**

真实试用重点记录：

- 用户带来的真实任务和材料；
- Curator 给了什么建议；
- 用户是否真的尝试；
- 是否降低搜索/学习/返工成本；
- 哪些建议无效或错误；
- 是否遗漏关键风险；
- 用户是否愿意再次使用。

## 当前不做

没有真实使用证明必要性之前，不建设：

- 大型资源数据库；
- 固定场景 taxonomy；
- 自动 Refresh 系统；
- 统一评分 / Gate；
- 每个候选强制 runtime test；
- unattended multi-card Loop；
- UP主/作者排行榜；
- 为单一失败案例增加一套新治理框架。

## 当前权威文档

- `docs/PROJECT_NORTH_STAR.md` — 长期产品边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前执行阶段
- `docs/validation/EVIDENCE_STATUS.md` — 当前证据状态
- `docs/SESSION_HANDOFF_CURRENT.md` — 新会话交接
- `skills/curating-erp-ai-resources/SKILL.md` — Minimal Curator V0.1

## 当前成功标准

> **一个真实 ERP / 企业信息化同事带着真实任务来，拿到建议后真的去用了，并认为节省的搜索/学习/返工成本足以让他下次继续使用。**
