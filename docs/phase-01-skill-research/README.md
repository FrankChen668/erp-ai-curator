# Phase 1 — Open-source Skill Research

> 状态：完成第一轮研究。结论用于 Phase 2 产品设计，不代表已经决定下一版 Skill 架构。

## Problem

现有 V0.2–V0.4 主要通过内部迭代产生，逐渐出现“规则越来越多、业务目标越来越远”的偏航。

本阶段先回答：

> **成熟 Agent Skill 通常如何把专家经验交给 Agent？哪些设计模式对高判断的“资源采编/推荐”任务真正有效？**

## Inputs

- Anthropic 官方开源 Skills；
- 社区开源 Skills；
- Anthropic Agent Skills 官方工程文章；
- 当前 ERP AI Curator 的真实失败历史（仅用于提出研究问题，不用于强行验证旧方案）。

## Method

不是看“哪个 Skill 文件最长”，而是统一从以下维度分析：

1. Skill 解决的真实任务；
2. Trigger 设计；
3. 主流程自由度；
4. SKILL.md 与 references / scripts 的分工；
5. 是否有显式路由 / done condition；
6. 确定性逻辑如何验证；
7. 主观质量如何评价；
8. 如何处理事实时效；
9. 如何避免过度触发、弱匹配或错误推荐；
10. 如何迭代 Skill。

## Corpus

本轮实际研究 21 个 Skill。

### Anthropic 官方（18）

1. `skill-creator`
2. `doc-coauthoring`
3. `frontend-design`
4. `mcp-builder`
5. `claude-api`
6. `pdf`
7. `pptx`
8. `docx`
9. `xlsx`
10. `web-artifacts-builder`
11. `canvas-design`
12. `internal-comms`
13. `brand-guidelines`
14. `theme-factory`
15. `slack-gif-creator`
16. `algorithmic-art`
17. `academy-guide`
18. `discernment-nudge`

### 社区（3）

19. `Agents365-ai/drawio-skill`
20. `arjunprabhulal/agent-skills` → `deep-research`
21. `yaniv-golan/skill-creator-plus`

另参考：

- Anthropic Engineering: *Equipping agents for the real world with Agent Skills*
- Anthropic Engineering: *Effective context engineering for AI agents*

## Non-goals

本阶段明确不做：

- 不设计 V0.5；
- 不修改现有 `SKILL.md`；
- 不决定数据库 / CSV / staging 是否最终保留；
- 不把某个开源 Skill 直接复制进项目；
- 不把别人的所有做法视为“最佳实践”；
- 不以 Star 数决定设计质量。

## Deliverables

- `SKILL_PATTERN_STUDY.md`：21 个 Skill 的横向研究；
- `DESIGN_SYNTHESIS.md`：跨样本设计规律、反模式及对本项目的初步启示；
- `../PROJECT_WORKFLOW.md`：后续阶段与三方协作协议。

## Definition of Done

本阶段完成的判断标准：

- ≥20 个代表性样本已实际读取核心 SKILL.md；
- 至少能区分高判断型与高确定性任务的设计差异；
- 明确总结“应该借鉴什么”和“不能照搬什么”；
- 形成 Phase 2 可直接使用的研究结论；
- 未修改当前 Skill 实现。

## Findings — 一句话版本

> **成熟 Skill 的核心不是把 Agent 管得越来越死，而是在正确位置提供最少但足够的上下文：判断留给模型，确定性工作交给脚本，细节按需加载，最终用真实任务和用户结果验证 Skill 是否有增益。**

## Handoff to Phase 2

Phase 2 可以依赖：

- 本阶段提炼的设计模式；
- 21 个 Skill 的具体案例；
- 对 V0.x 偏航根因的研究性解释。

Phase 2 不应假设：

- V0.4 的 Gate / 四表 / validator 必须保留；
- 一定需要资源数据库；
- 一定需要多 Agent；
- 一定需要复杂评分；
- 一定要把所有事实都做 claim verification。

这些必须重新从产品价值证明。
