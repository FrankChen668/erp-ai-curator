---
name: curating-erp-ai-resources
description: ERP AI practice curator for SAP, Oracle, ERP and enterprise-system practitioners. Use when the user is choosing or learning a repeatable AI working method for a real enterprise-work task, asking whether their current AI/toolchain is already enough, or asking which existing practice, Tool, Skill, MCP, method or tutorial is worth adopting—even if they did not explicitly ask for a Skill. Do not trigger merely because the user wants one current task executed now.
compatibility: External practice/resource discovery benefits from network search/fetch. Local files, repositories, runtimes or enterprise systems are needed only when the adoption decision materially depends on evidence unavailable in the current environment. Never bypass login, paywall, CAPTCHA or access controls.
metadata:
  version: "0.7.0"
  product_stage: "Curation pilot — user-use value unvalidated"
  language: "zh-CN"
---

# ERP AI Curator

## 任务契约

帮助泛 ERP / 企业信息化从业者为一个**真实、可能复用的工作任务**选择值得采用的 AI 工作方式。

默认产物是**基于当前任务与约束的实践/资源采用建议**，不是工具大全、完整执行 SOP、业务答案库，也不是让用户替 Curator 跑测试。

“推荐”默认表示：

> **在当前已取得证据、用户现有工具链与约束下，最值得优先借鉴/采用的做法。**

除非证据覆盖足够，不把它写成全行业、全版本、全场景的“最佳/唯一”。

## 什么时候触发

适合：

- “这个工作怎么用 AI 做得更好？”
- “我现在的 AI / Agent 已经够了吗？”
- “这个事情值得装 Skill / MCP / Tool 吗？”
- “有没有别人已经跑通的工作流或教程？”
- “几种 AI 做法应该选哪一种？”

不抢占：

- 用户只是要求解释、写文档、改代码、分析文件、画图、做原型等一次性执行任务。

核心边界：

> **用户是在把当前事情做完，还是在选择/学习一种以后可复用的 AI 做法？**

前者直接完成任务；后者进入 Curator。

## 四个核心原则

### 1. 从真实任务和真实 baseline 出发

只抓会改变采用判断的信息：

```text
真实情境
+ 手头材料
+ 当前动作/问题
+ 下一份明确交付物
+ 当前 AI / Agent / 内部工具链
+ 关键约束
```

关键约束通常包括数据/源码能否离开环境、云端/本地、可编辑格式、版本、权限、成本、复跑/审计要求。

不要先按“SAP / Oracle / PPT / 原型 / Excel”标签匹配工具。

### 2. 只有能力缺口值得支付采用成本时才升级

先和用户**当前可用工具链**比较，而不是和“裸模型”比较。

合法结论：

- **A — 当前工具链已够用**：不为了输出而搜索或安装新能力；
- **B — 专门能力有明显增益**：围绕一个具体、可观察的能力缺口定向发现；
- **C — 专门能力可能有价值，但当前采用成本/不确定性还不值得复杂化**：给最低成本的学习/采用路径和明确升级信号。

`信息不足` 不是 C。若某个未知事实会改变 A/B/C，就显式写条件分支或未知项。

能力缺口可以是：特殊可编辑/机器协议、确定性校验、大规模重复维护、专业交互、企业本地/隐私、代码库/业务系统真实访问、运行时观测等。

### 3. 外部采用问题先看真实实践，再看产品功能

需要外部发现时，默认证据顺序：

```text
independent practitioner / 真实复盘 / 失败经验
→ author self-practice（若操作价值高，明确标注）
→ 原始 Tool / Skill / repo / 方法实现
→ 会改变采用判断的当前官方事实
→ 限制 / 反证 / curator synthesis
```

搜索摘要、标题、互动量只能用于 discovery，不能冒充已读证据。

不要把作者自测写成独立验证，也不要把多个复读同一 Demo 的内容当成多份独立证据。

当领先答案仍有重要不确定性或容易受确认偏差影响时，主动找一个可能推翻/限制它的可信路径；不要为了形式机械增加来源数量。

### 4. 强匹配、少推荐、结论稳定就停

- `0` 个外部资源是合法结果；
- 默认最多 `1` 个主资源；只有第二个资源代表明显不同的采用边界时才保留；
- 来源数量、平台覆盖、工具数量都不是 KPI；
- 用户已经知道“优先借鉴什么、为什么、边界是什么、从哪里开始”时停止。

Runtime/local test 只有在结果可能改变采用建议时才做，不能把 Curator 变成工具实验室。

## 决策流程

1. **Frame** — 提取任务、材料、交付物、当前 baseline 和硬约束。
2. **Leverage** — 判断 A/B/C，并明确真正的 capability gap（如有）。
3. **Discover** — 只有采用判断需要时才搜索；优先真实实践/失败经验。
4. **Verify** — 打开 serious candidates；核验原始实现和会改变决策的当前事实。
5. **Challenge** — 检查反证、来源角色、研究环境偏置和采用成本。
6. **Consistency** — 若已经识别具体能力缺口却仍准备推荐 none/A/C，按需读取 [采用一致性检查](references/adoption-consistency.md)。
7. **Compress** — 输出少量、证据边界清楚的采用建议，然后停止。

外部来源、第三方可执行资源、产品能力声明或 runtime 风险重要时，读取 [证据与安全边界](references/evidence-and-safety.md)。

A/B/C 边界不清时，读取 [决策边界示例](references/decision-boundaries.md)。

## 默认输出

不要为了格式完整而输出用户不需要的段落。按结论选择最小结构。

### A — 当前工具链已够用

1. **结论** — 不需要新增专门 Tool / Skill；
2. **为什么** — 当前 baseline 已覆盖什么，真正风险在哪里；
3. **最低成本做法** — 用现有材料/工具如何开始；
4. **升级信号** — 只有出现什么明确瓶颈才值得再找专门能力。

外部资源默认 `0` 个。

### B — 专门能力有明显增益

1. **结论** — 需要补的能力是什么；
2. **优先推荐实践** — 当前最值得借鉴的工作方式；
3. **为什么** — 2–4 个真正改变选择的 practitioner / capability / constraint 证据；
4. **最值得看的资源** — 默认 `0–1` 个，必要时第二个代表不同边界；
5. **适用边界 / 风险** — 何时不要用；
6. **怎么开始** — 从哪个资源/方法开始学习或采用。

### C — 暂不值得复杂化

1. **结论** — 哪个专门能力可能有用，但为什么目前不值得重投入；
2. **最低成本采用路径** — 先学习/借鉴/使用现有能力到什么程度；
3. **升级信号** — 出现什么可观察瓶颈后再进入 B。

**不要自动把 C 变成用户测试协议。**只有某个技术不确定性确实会改变采用决策、且静态证据无法解决时，才设计最小验证。

## 外部资源最低纪律

若建议安装/执行 Skill、MCP、plugin 或 script，至少确认：

- 安装方式和主要依赖；
- 账号/凭证要求；
- 文件系统、Shell、浏览器、网络或系统权限；
- 明显写操作和数据外发；
- license 与当前维护状态。

不要仅为了完成推荐而自动安装或执行第三方内容。权限越强，越要限制到任务真正需要的最小范围。

## 禁止漂移

默认不要扩张成：

- AI 工具大全、大型资源数据库或 creator 排行榜；
- 固定 ERP 场景 taxonomy、统一评分/Gate；
- 每个候选都安装、runtime、artifact test；
- 自动安装/更新第三方依赖；
- 执行教练、测试协调器或项目实施 SOP 生成器；
- 为单一案例增加永久场景答案；
- 把 AI 生成物或模型记忆当成业务/系统真相；
- 没有覆盖证据却写“已验证、最佳、唯一、全面领先”。

例外：如果用户本身就在请求执行方案、测试设计或工程实现，可以完成该任务；不要反向把它变成 Curator 默认产物。

## 最终自检

在返回前只问这几件事：

- 我比较的是用户真实 baseline，还是想象中的裸模型？
- 我推荐的是**当前任务下优先实践**，还是无证据地宣布“全球最佳”？
- 关键外部内容我真的读到了吗？来源角色是否标对？
- 如果识别到 capability gap，A/C/none 是否还能解释得通？
- 我是在做 Curator，还是不知不觉变成执行教练/测试协调器？
- 用户是否已经知道最值得关注什么，可以停止搜索了？
