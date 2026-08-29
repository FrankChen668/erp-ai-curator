# Real Task Intake — 真实问题进入项目的最小闭环

> Current intake rule for AI Leverage Model V3.

## 1. 目的

ERP AI Curator 的上游必须是真实工作问题，而不是资源分类、工具清单或测试题。

现阶段最重要的输入渠道是内部 AI 培训问卷、访谈、实际求助和项目工作中已经发生的问题。

原则：

> **保留原始问题，先判断用户是在直接执行任务，还是在寻找更好的 AI 工作方式；后者才进入 AI leverage 诊断。**

不再把“是否需要外部资源”作为唯一入口。

## 2. 可接受来源

1. `REAL_USER`：真实泛 ERP / 企业信息化从业者提交的问题；
2. `OWNER_REAL`：项目负责人自己真实遇到的问题；
3. `REPRESENTATIVE`：为边界覆盖设计的问题，只做测试；
4. `SYNTHETIC`：纯构造题，只做回归。

产品价值主要看前两类。

角色已知才记录，不为了平衡矩阵猜角色。

## 3. 最小记录字段

```text
Task ID
Source
Role（已知才填）
Original problem（原文，不润色）
Context / attachment（有则保留）
Intent: direct execution / AI-work-method / explicit-resource / uncertain
AI leverage diagnosis（进入 V3 才填）
Mode: A / B / C
Recommendation / working approach
Owner judgement
Observed use（有则记录）
```

不建立复杂表单、统一评分或 candidate JSON。

## 4. 问卷如何进入

培训问卷本来就在收集：

- 真实工作卡点；
- 当前怎么处理；
- 希望 AI 帮到哪里；
- 输入材料；
- 期望输出；
- 可脱敏附件。

这比“你想学哪个 AI Tool”更适合作为项目上游。

收到回答后：

1. 原文保存；
2. 有明确角色才标记；
3. 不先改写成“适合 Skill 的标准场景”；
4. 判断真实意图；
5. 若是 AI 工作方式探索，进入 `PROTOCOL_V3.md`；
6. 根据结果判断 Mode A / B / C；
7. 只有 Mode B 确实需要外部方案时才搜索；
8. 记录是否愿意采用 / 分享，以及实际行为。

## 5. Triage：什么问题进入 V3

### A. Direct execution — Curator 不抢占

例如：

- “帮我解释这个财务业务逻辑。”
- “帮我改这段 Java 代码。”
- “帮我写项目周报。”
- “根据这些需求直接做一个原型。”

这些问题可以由普通 AI 直接执行。

### B. AI-work-method — 进入 V3

例如：

- “这个需求分析工作怎么用 AI 做得更好？”
- “我要快速理解一个陌生 Java 供应链系统，AI 有什么比较好的做法？”
- “接手一个陌生财务模块，怎么借助 AI 快速建立整体认识？”
- “这个事情值得装一个专门 Skill 吗？”

用户没有说 Tool / Skill，也应该进入，因为他在选择 AI 工作方式。

### C. Explicit-resource — 进入 V3 的 Mode B 判断

例如：

- “有没有能生成 editable draw.io 的 Skill？”
- “Codex 接第三方模型哪个方案现在靠谱？”

### D. Uncertain — 看一次性还是可复用工作方式

例如：

> “我想自动整理会议纪要和行动项。”

如果只是整理这一次会议，直接执行；如果是在选择一个长期稳定的 AI 工作方式，进入 V3。

## 6. 问题池不是场景目录

不按以下方式建设：

- SAP 场景 20 个；
- Oracle 场景 20 个；
- 财务场景 20 个；
- 供应链场景 20 个；
- 开发场景 20 个。

这些可以作为问题背景，但不能成为运行逻辑。

正确方式是保留真实问题，然后观察重复出现的工作需求和 AI 杠杆类型。

## 7. 去重只用于发现重复需求

只做语义聚类，不覆盖原文。

多个问题可能都属于“快速理解陌生系统”，但：

- SAP 模块；
- Java 定制供应链；
- 自研财务系统；

其输入、约束和最优 AI 做法可能不同。

聚类帮助发现共性，不把问题硬改成统一 Prompt。

## 8. 什么时候才沉淀产品机制

真实问题反复出现后，才考虑：

- 常见 AI leverage pattern；
- Starter Pack；
- 轻量搜索先验；
- Skill trigger；
- 持久化资源；
- 自动刷新。

不为了“覆盖泛 ERP”建立一个巨大的场景知识库。

## 9. 当前执行方式

云端直接负责：

- 收集 / 整理真实问题；
- AI leverage 判断；
- 必要时 Web / GitHub 搜索；
- 阅读、比较与核验；
- 形成可执行工作方式建议；
- 更新 GitHub 证据。

本地低能力 Agent 不进入产品判断链路；只有必须接触本地环境时做受限执行。
