# ERP AI Curator — Minimal Curator V0.1

当前 Skill 版本：`0.6.3`

定位：

> 面对真实 ERP / 企业信息化工作任务，先判断普通 AI 是否已经够用；如果不够，优先从互联网上已经存在的实操经验、Tool / Skill / MCP / 方法 / 教程中筛选最值得学习和采用的最佳实践。

## V0.6.3 做了什么

这是一次**产品边界 Harness 修正**，不是方法论扩张：

- 保留 0.6.2 的 A/B/C、General-AI-first、capability-gap、evidence-grounded 和 adoption-consistency；
- 明确 Curator 的默认产物是“最佳实践 / 现成资源采用建议”，不是完整执行 SOP；
- 优先输出 practitioner 实操 / 复盘 / 失败经验，再核验原始 Tool / Skill / repo 和当前官方事实；
- 明确真实用户后续采用/修改/拒绝用于验证 Curator，但不把用户变成工具测试员；
- 不新增 SAP/Oracle/ERP 场景答案、评分、Gate、强制 runtime 或工具目录。

## 当前阶段

Minimal Curator V0.1 仍是 **real-user pilot candidate**。

当前产品问题不是“能否指导用户按步骤测试工具”，而是：

> **能否针对真实 ERP 工作问题，从高噪声互联网资源中压缩出少量真正值得学习/采用的最佳实践，并且明显优于用户自己漫无目的地搜索？**

真实用户后续是否采用这些建议，仍用于验证产品价值。

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
