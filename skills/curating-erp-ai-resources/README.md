# ERP AI Curator — Minimal Curator V0.1

当前 Skill 版本：`0.6.2`

定位：

> 面对真实 ERP / 企业信息化工作任务，先判断普通 AI 是否已经够用；只有存在明确能力缺口且收益超过采用成本时，才推荐少量 Tool / Skill / MCP / 方法 / 教程。

## V0.6.2 做了什么

这是一次**Harness 一致性补丁**，不是方法论扩张：

- 保留 0.6.1 的四个核心原则、A/B/C、General-AI-first、capability-gap、evidence-grounded 和 decision-changing runtime；
- 不新增 SAP/Oracle/ERP 场景答案；
- 增加一个按需 `adoption-consistency.md`：只有当 Agent 已识别具体能力缺口、却仍准备输出“无需专门资源 / 继续普通 AI / 先低成本试验”时才读取；
- 要求 Agent 明确解释为什么该能力缺口尚不足以跨过采用成本，避免从“反过度工具化”滑向“under-tooling”；
- 不新增评分、Gate、强制资源推荐或新一轮内部 benchmark。

0.6.1 的隔离边界回归发现 Case 5/38 存在 under-tooling，但没有证明永久领域规则缺失。0.6.2 因此只提升**执行可见性与一致性**，不把案例答案写回 Skill。

## 当前阶段

Minimal Curator V0.1 仍是 **real-user pilot candidate**。

下一份有价值的产品证据仍然来自真实 ERP / 企业信息化同事在真实任务上的实际采用、修改、拒绝和结果，而不是继续内部刷题。

## 当前可分发 Skill 结构

```text
curating-erp-ai-resources/
├── SKILL.md
├── README.md
└── references/
    ├── adoption-consistency.md
    ├── decision-boundaries.md
    └── evidence-and-safety.md
```

详细项目验证、Pilot 合同和历史研发资产属于仓库治理内容，不是运行时 Skill 的默认依赖。
