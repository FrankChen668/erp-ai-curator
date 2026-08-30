# ERP AI Curator — AI Leverage Model V3

Status: **CURRENT DETAILED WORKING MODEL**
Runtime authority: `skills/curating-erp-ai-resources/SKILL.md` 0.7.0
Navigation: `docs/PROJECT_MAP.md`

> 本文解释“为什么这样判断”；普通 runtime 不需要默认全文加载。

## 1. 第一性问题

泛 ERP / 企业信息化从业者真正需要的不是更多 AI 链接，而是：

> **面对这个真实工作任务，我现有 AI / Agent / 工具链已经够不够？如果不够，什么已经存在的实践/能力最值得采用，并且收益是否值得它的学习、迁移、权限和治理成本？**

因此产品核心是：

`AI Leverage Diagnosis → Practitioner-first Curation → Adoption Decision`

## 2. 真实 baseline

比较对象不是“裸模型”，而是用户当前已经拥有并能使用的：

- 通用 AI / Coding Agent；
- 企业批准的 AI；
- IDE / repo / knowledge base；
- 内部 exporter / pipeline / automation；
- ALM / test / data / office 工具。

新 Tool / Skill / MCP 必须相对这个 baseline 产生可解释增益。

## 3. Frame：只抓会改变判断的任务信息

```text
real work context
+ actual materials
+ concrete action/problem
+ expected deliverable
+ current AI/toolchain
+ hard constraints
```

Hard constraints 常见包括：

- 数据/源码能否离开环境；
- 本地/云端；
- 特定可编辑/机器协议格式；
- ERP/应用版本；
- 系统/数据库权限；
- 成本、复跑、审计、企业账号。

不先做场景 taxonomy。

## 4. Leverage：A/B/C

### A — 当前工具链已够用

适合：

- 主要是理解、总结、规划、改写、生成草稿；
- 输入材料已经齐全；
- 现有 Agent 可以读取所需材料；
- 没有特殊格式、系统访问、确定性处理等能力缺口；
- 新工具只是“可能更方便”，增量价值不清楚。

A 不等于凭模型记忆做 ERP 专业判断。业务、代码、配置、接口等重要结论仍应 source-grounded。

### B — 专门能力有明显增益

当出现一个 current baseline 无法很好提供的**可观察 capability gap**，且收益值得采用成本时进入 B。

常见 gap：

- 原生可编辑/机器协议格式；
- 真实 repo / system / metadata access；
- runtime observation/action；
- deterministic reconciliation/validation；
- repeated structured maintenance；
- 专业交互/设计系统；
- local/privacy/enterprise integration。

专门能力更强不等于 B。必须同时考虑：

- 安装/学习；
- 迁移；
- 账号/权限；
- 数据外发；
- 长期维护/治理。

### C — 可能有增益，但现在不值得复杂化

C 只在以下逻辑成立时使用：

- capability gap 真实存在；
- 专门路线也可能解决；
- 但当前任务频率/规模、采用成本或证据不确定性使重投入暂时不值。

C 默认给：

- 最低成本学习/采用路径；
- 明确 upgrade signal。

**C 不等于“信息不足”，也不等于“让用户先测试工具”。**

如果某个技术不确定性会直接改变采用结论、静态证据又无法解决，才做最小验证。

## 5. Practitioner-first discovery

只有采用判断需要外部实践/资源时才进入 discovery。

默认顺序：

```text
independent practitioner / real workflow / failure experience
→ author self-practice（明确角色）
→ original Tool / Skill / repo / method
→ decision-changing current official facts
→ counterevidence / curator synthesis
```

为什么 practitioner 在前：用户首先要知道别人怎么做、实际输入输出、哪里返工、对什么任务真省时间。

为什么官方仍重要：版本、安装、兼容、价格、隐私、许可证、edition、当前原生能力必须回原始/官方事实。

> Practitioner-first ≠ practitioner-authority.  
> Official fact anchor ≠ official recommendation priority.

## 6. Search 不是积累链接

研究的目标是替用户完成取舍，不是把选择工作留给用户。

纪律：

- strong match > coverage；
- 0 个资源合法；
- 默认 0–1 个主资源；
- 第二个只有在采用边界明显不同才保留；
- social repetition 不等于 independent corroboration；
- 领先答案有 material uncertainty 时主动找反证；
- 结论稳定就停。

平台数量、搜索次数、链接数量都不是 KPI。

## 7. Existing ecosystem before builder

已经存在的 PM/BA Skill 库、Agent 教程、社区实践、Tool 官方 examples、作者系列都应先作为 feeder ecosystem。

Curator 做的是：

```text
real ERP problem
→ discover existing ecosystem
→ inspect concrete content
→ verify implementation/current facts
→ compress recommendation
```

只有现有生态确实不能覆盖关键问题时才补 `curator synthesis`，并明确标注。

## 8. Dynamic facts 与稳定洞见分开

教程可能同时包含：

- stable practice insight；
- version-coupled setup instruction。

前者可以继续保留，后者需要当前核验。

不要因为操作步骤过时就丢掉仍成立的方法洞见，也不要因为方法洞见不错就默认旧安装命令仍可用。

## 9. Source Adapter 只是条件性 acquisition capability

当前普通 Web/GitHub 能完成大多数公开 discovery。

只有同时满足时才考虑已批准 source adapter：

1. 某个平台内容可能 material 改变推荐；
2. 普通路径无法获得足够正文/字幕；
3. 已存在合适的 read-only acquisition capability；
4. 增加的复杂度/风险值得。

Source Adapter 不拥有最终判断，也不是当前默认产品架构。

详细历史/条件性设计：

- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

## 10. Runtime / local test

不自动进入：

`static review → install → runtime → artifact → benchmark`

最小验证只在结果会改变采用判断时出现，例如：

- practitioner 证据对关键能力冲突；
- 隐私/权限/兼容静态无法判断；
- 精确本地复现是采用前提；
- 准备把能力作为内部长期标准；
- 两方案真实差异无法从现有证据判断。

Runtime 是决策工具，不是可信度仪式。

## 11. “最佳实践”的证据边界

产品目标可以是寻找最佳做法，但单次输出默认应说：

> **在当前任务、baseline、约束和已取得证据下，最值得优先借鉴/采用的实践。**

只有有足够覆盖证据时才使用 universal `best / unique / validated`。

作者自实践可以证明“怎么操作/如何实现”，不能自动证明“独立用户一致认为值得采用”。

## 12. Curator 与执行任务的边界

触发 Curator：用户在选择/学习可复用 AI 工作方式。

不触发 Curator：用户只是让 Agent 完成当前一次性任务。

即使进入 Curator，也不要自动扩展成：

- 完整执行 SOP；
- 项目实施计划；
- 用户工具测试协议。

除非用户本身明确请求这些产物。

## 13. Success / unresolved risk

一次成功 curation 应让用户感觉：

> **“我知道这个任务当前最值得采用什么做法，也知道为什么、不适用在哪里、从哪个可信资源开始。”**

当前最大的产品风险仍未解决：

> **强模型 + 普通搜索可能已经足够好，以至于 Curator 没有稳定额外价值。**

这个问题只能由真实用户实际收到推荐后的采用/拒绝/反馈继续验证，不能靠增加规则、Gate 或内部 benchmark 证明。
