# ERP AI Curator — Minimal Curator V0.1

当前 Skill 版本：`0.6.1`

定位：

> 面对真实 ERP / 企业信息化工作任务，先判断普通 AI 是否已经够用；只有存在明确能力缺口且收益超过采用成本时，才推荐少量 Tool / Skill / MCP / 方法 / 教程。

## V0.6.1 做了什么

这是一次**运行时硬化**，不是方法论重写：

- 将 Pilot 状态、跨卡验证等项目治理信息移出运行时 `SKILL.md`；
- 将重复原则压缩为 4 个核心判断；
- 增加少量“判断边界”正反例，避免重新滑向场景答案表；
- 运行时只保留两份按需 reference：`decision-boundaries.md` 与 `evidence-and-safety.md`；
- V0.4 的 Gate、评分、taxonomy、validator、旧 eval 等资产移入仓库 `archive/curator-v0.4-runtime-assets/`，保留历史但不再随当前 Skill 运行；
- 保持 A/B/C、General-AI-first、capability-gap、evidence-grounded、decision-changing runtime 等核心方法不变。

## 当前阶段

Minimal Curator V0.1 仍是 **real-user pilot candidate**。

内部异构任务验证支持“方法可进入 Pilot”，但尚未证明真实用户相对普通 Agent 获得稳定增量价值。

下一步仍然是：让真实 ERP / 企业信息化同事带真实任务使用，并观察他们是否真正采用建议、减少错误工具选择/搜索配置/返工，或暴露新的方法缺陷。

## 当前可分发 Skill 结构

```text
curating-erp-ai-resources/
├── SKILL.md
├── README.md
└── references/
    ├── decision-boundaries.md
    └── evidence-and-safety.md
```

详细项目验证、Pilot 合同和历史研发资产属于仓库治理内容，不是运行时 Skill 的依赖。
