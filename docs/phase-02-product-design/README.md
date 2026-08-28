# Phase 2 — Product Design

## Problem

V0.2–V0.4 已证明：如果过早把资源采编写成 Gate、JSON、评分和 Validator，Agent 会逐渐优化“怎样通过规则”，而不是“怎样找到真正值得分享的资源”。

本阶段不继续修旧 Skill，而是先回答：**ERP AI Curator 到底是什么产品、为谁创造什么价值、怎样才算做对。**

## Inputs

- Phase 1 对 21 个代表性 Agent Skill 的研究；
- V0.2–V0.4 的真实失败案例；
- 当前业务目标：为 SAP / Oracle / ERP 项目人员筛选可直接学习、使用或借鉴的高价值 AI 资源；
- 用户要求：少而精、实操优先、中文优先但不牺牲质量、允许无推荐、保留原始链接。

## Method

1. 从最终用户价值重新定义产品；
2. 区分“Skill 操作者”和“资源最终使用者”；
3. 定义输入、核心决策、输出和非目标；
4. 设计真实用户旅程；
5. 定义与普通搜索/普通 Prompt 的对比验收；
6. 从反方向做压力测试，主动寻找方案失效条件；
7. 形成明确决策记录，为 Phase 3 Skill Architecture 提供稳定输入。

## Non-goals

本阶段明确不做：

- 不修改 `SKILL.md`；
- 不设计新的 Gate / Candidate JSON / 评分脚本；
- 不恢复四表数据库；
- 不开发 Refresh / autonomous mode；
- 不让本地 Agent 开始实现；
- 不把 Phase 1 研究模式机械复制进产品。

## Deliverables

- `PRODUCT_VISION.md`
- `USER_JOURNEYS_AND_CONTRACT.md`
- `SUCCESS_METRICS.md`
- `ADVERSARIAL_REVIEW.md`
- `DECISION_RECORD.md`

## Definition of Done

Phase 2 只有满足以下条件才结束：

1. 能用一句话说明产品价值；
2. 明确谁操作、谁最终受益；
3. 明确默认输入和默认输出；
4. 明确什么资源该推荐、什么情况下应保持沉默；
5. 明确何时需要强事实核验，何时不需要；
6. 明确为什么它可能优于普通搜索/普通 Prompt，并设计可证伪的 Eval；
7. 对核心方案完成压力测试并记录保留/修改/否决；
8. 形成可以直接交给 Phase 3 做 Skill Architecture 的产品契约。

## Current Decision

Phase 2 的核心假设是：

> **ERP AI Curator 不是资源数据库，也不是事实审计器；它是一个面向 ERP 真实工作任务的资源决策压缩器。它替操作者完成搜索、阅读、比较和取舍，输出极少量可直接分享给同事的原始资源。**

该假设在本阶段被进一步约束，并将在 Phase 5 通过真实任务和 baseline 对比验证。

## Handoff

Phase 3 可以依赖本目录中的产品契约和决策，但不能默认继承 V0.4 的工程结构。任何旧资产都必须重新证明它对产品结果有必要性。