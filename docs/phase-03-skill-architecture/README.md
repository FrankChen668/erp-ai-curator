# Phase 3 — Skill Architecture & Eval Design

> **SUPERSEDED FOR CURRENT IMPLEMENTATION DECISIONS (2026-08-29).**
>
> This phase is preserved as historical implementation design. Its trigger contract required the user to explicitly seek resources and its core flow started from resource discovery; V3 has replaced that model.
>
> Current authority:
> - `docs/AI_LEVERAGE_MODEL_V3.md`
> - `docs/SKILL_BLUEPRINT_V3.md`
> - `docs/ADVERSARIAL_REVIEW_V3.md`
> - `docs/validation/PROTOCOL_V3.md`
>
> Do **not** execute the old `IMPLEMENTATION_SPEC.md` unless the project explicitly returns to the resource-first architecture.

## Historical Goal

把 Phase 2 已确认的产品契约翻译成**最小可测试 Skill 架构**，并先定义 Eval，再允许本地 Agent 实现。

本阶段不追求“功能完整”，只追求：

> Skill 是否能稳定改善资源推荐质量，而不把高判断任务重新做成规则流水线。

## Inputs

- `docs/phase-02-product-design/PRODUCT_VISION.md`
- `USER_JOURNEYS_AND_CONTRACT.md`
- `SUCCESS_METRICS.md`
- `ADVERSARIAL_REVIEW.md`
- `DECISION_RECORD.md`
- Phase 1 对 Anthropic `skill-creator`、`academy-guide`、`deep-research` 等 Skill 的研究。

## Architecture Principles worth keeping

1. **High judgment stays in instructions.** 推荐取舍不脚本化。
2. **Progressive disclosure.** 主 Skill 只放核心路线，细节按需加载 references。
3. **No premature scripts.** 第一版不新增 scripts。
4. **No inherited V0.4 machinery by default.** 不继承 Gate/score/candidate JSON/四表。
5. **Eval before expansion.** 先跑真实任务 A/B，再决定补什么。
6. **Skill-creator is an authoring method, not product authority.**

这些原则仍可被 V3 继承，但旧 trigger / resource-first flow 不再是当前方案。

## Historical Deliverables

- `SKILL_ARCHITECTURE.md`
- `EVAL_PLAN.md`
- `IMPLEMENTATION_SPEC.md`

## Historical Definition of Done

- 目标 Skill 的 trigger 清楚；
- 主 SKILL.md 职责明确且轻量；
- references 的加载条件明确；
- script-vs-instruct 决策明确；
- 10 个真实 Eval prompt 已定义；
- baseline 与 human review 方法明确；
- 本地 Agent 的允许文件、禁止事项、验收标准和停止条件明确。

## Non-goals

- 不修改当前 `skills/curating-erp-ai-resources/`；
- 不实现新 Skill；
- 不迁移旧数据；
- 不运行大规模 Eval；
- 不增加数据库、Refresh、autonomous mode。

## Current Handoff

Do not hand the old Phase 3 implementation spec to a local Agent.

If Skill implementation is resumed later, start from `SKILL_BLUEPRINT_V3.md` and only after V3 real-task evidence justifies packaging the working model as a Skill.
