# Current Evidence Status

Date: 2026-08-29

> Current product model is `AI_LEVERAGE_MODEL_V3.md`. Evidence created under the older resource-first model must not be silently treated as V3 validation.

## 1. 当前已经确认的事实

### A. 泛 ERP / 企业信息化工作里确实存在“AI 工作方式选择”问题

现有 OWNER_REAL 问题覆盖：

- editable 业务流程 / 架构图；
- 交互原型；
- Claude Code / Codex 模型路由；
- Fit-to-Standard / 需求分析；
- 陌生模块学习；
- 现有 Agent 项目的静态架构、运行链路与 workflow governance 区分。

这些问题不只属于 SAP / Oracle，也可以映射到定制供应链、财务、Java 企业系统和 Agent 开发工作。

### B. 后续偏航的根因已经找到

Phase 2 把产品定义成：

> 真实任务 → 从互联网筛 0–2 个资源。

Phase 3 又把触发条件进一步锁成：

> 用户必须明确在找 / 比较资源。

两层叠加后，产品自然滑向：

`resource search + official verification + 0–2 links`

这比最初目标更窄。

V3 已把核心改成：

`真实任务 → AI leverage diagnosis → Mode A/B/C → 必要时才定向发现`

### C. 判断层比搜索层更重要

过去反复出现的失败包括：

- 完整任务没理解，只匹配资源标签；
- 本来通用 AI 足够，却默认开始搜工具；
- 把官方材料自动当推荐位；
- 用相邻工具填空；
- 过早 abstain；
- 配置事实过时；
- 把 static map、runtime tracing、workflow graph 混为一谈。

这些都说明真正价值首先是“诊断哪种 AI 工作方式适合当前任务”。

### D. 重治理仍不是答案

V0.2–V0.4 已证明：Gate、评分、candidate JSON、validator 可以结构正确但产品判断错误。

V3 不恢复这些机制。

## 2. 现有 OWNER_REAL 证据如何重新解释

OR01–OR06 的**原始工作问题**仍然有效，因为它们来自真实工作需要。

但旧的推荐结果主要是在 resource-first 模型下产生，因此：

- 可以作为 discovery history；
- 可以作为 V3 replay 的输入；
- **不能直接算 V3 已验证通过。**

V3 必须重新回答一个更前置的问题：

> 这个任务到底需要专门 AI 方案吗，还是通用 AI / 低成本试验已经够？

## 3. REAL_USER 证据

**目前仍不足。**

已经找到内部 AI 培训需求问卷设计，并已建立问卷 → Real Task Intake 的桥接规则；但当前 File Library 没有实际答卷 / 汇总结果。

因此：

- 不伪造独立顾问 / PM / 开发人员需求；
- 不为了角色覆盖人为补题；
- 当前主要使用 OWNER_REAL 做产品模型回放与反证。

## 4. 角色范围的当前定义

不再局限于“SAP / Oracle 顾问”。

目标是泛 ERP / 企业信息化从业者，包括：

- 实施 / 业务顾问；
- 项目经理；
- 产品经理 / 解决方案人员；
- 开发人员；
- 标准 ERP、二开、集成、Java / .NET 定制企业系统等环境。

角色用于理解上下文，不建立人为配额。

## 5. 当前资产证据等级

| Asset | Evidence type | Current status |
|---|---|---|
| Phase 1 — 21 Skill study | design research | keep; many principles still valid |
| Phase 2 Product Vision | historical product hypothesis | partially superseded by V3 |
| Phase 3 Skill Architecture | historical implementation hypothesis | trigger/core-flow superseded by V3 |
| V0.2–V0.4 | failure evidence | archive only |
| PR #4 Phase 4 pilot | execution/failure evidence | closed, not merged |
| Starter Pack V0 | discovery inventory | candidate memory only, not fixed answers |
| OR01–OR06 original problems | OWNER_REAL input evidence | keep; replay under V3 |
| old OR01–OR06 recommendations | resource-first discovery evidence | do not treat as V3 validation |
| Trigger-negative cases | intent-boundary evidence | keep, reinterpret as execution vs AI-work-method boundary |
| Independent REAL_USER results | primary validation | insufficient today |

## 6. 目前还没有证明什么

- V3 工作模型在独立真实用户上稳定有效；
- V3 应该最终封装成 Skill；
- 固定资源缓存能明显提高效果；
- PM / developer 等角色已经被独立验证；
- 资源推荐应该永远是 0–2；
- 自动 refresh / 数据库有必要；
- 场景 taxonomy 有必要。

## 7. 当前主线

**Status: product-model reset + OWNER_REAL replay + real-user intake preparation. Not Skill implementation.**

当前工作：

1. 使用 V3 重新判断现有真实问题；
2. 优先识别 Mode A（通用 AI 足够），防止 over-tooling；
3. Mode B 才做定向发现；
4. Mode C 给低成本试验，不把不确定性包装成成熟方案；
5. 真实问卷答卷出现后，直接按 V3 处理；
6. 只有 V3 本身被证明有价值，再讨论 Skill 封装。

## 8. 当前主要风险

### Over-tooling

把所有“怎么用 AI”都回答成“装一个 Skill / Tool”。

### Resource gravity

因为仓库已经有 Starter Pack，就优先往已有资源上靠。

### Official-document gravity

因为官方容易核验，就花大量时间在官网，而不是先判断用户是否需要那个能力。

### Scenario explosion

为了覆盖泛 ERP，开始罗列 SAP / Oracle / 财务 / 供应链 / 项目管理 / 开发的几百个场景。

### Rebuilding governance

因为一次错误又新增一条 Gate、评分、字段或脚本。

出现以上趋势时应回到 `AI_LEVERAGE_MODEL_V3.md`。
