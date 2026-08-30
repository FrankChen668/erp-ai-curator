# ERP AI Curator — Project-wide Calibration 2026-08-30

Status: **CALIBRATION / REMEDIATION RECORD**

> 本文件记录一次从仓库事实出发的全面盘点、第一性审查、对抗性复审、优秀 Skill/Harness 学习与整改。它不是新的产品框架；当前权威入口仍是 `docs/PROJECT_MAP.md`。

## 1. 审查范围

本轮重新检查：

- 根 README 与当前 repo tree；
- North Star / Current Plan / Handoff / Evidence Status / Owner Rules；
- current runtime Skill 与 3 个 references；
- AI Leverage、Adversarial、Skill Blueprint、Project Workflow；
- Source Adapter architecture/lifecycle；
- Phase-01 的 21 个优秀 Skill pattern study / design synthesis；
- 当前 `tests/`、archive、validation 资产；
- 近期 PR #39–#58 的关键演化与偏航记录。

没有把旧聊天结论当 authority。

## 2. 第一性重新确认：产品核心没有坏

从用户价值出发，ERP AI Curator 的必要工作仍然是：

```text
真实企业工作问题
+ 用户当前 AI / 工具链 baseline
+ 交付物 / 硬约束
→ 判断有没有 capability gap
→ 必要时发现真实 practitioner 实践
→ 核验原始 Tool / Skill / repo / method
→ 只核验会改变采用判断的当前事实
→ 压缩成少量值得优先学习/采用的建议
```

因此以下主干继续保留：

- real-task-first；
- current-stack / General-AI-first；
- capability-gap + adoption-cost；
- practitioner-first，而不是 official-feature-list-first；
- existing ecosystem before builder；
- source/project/system grounded；
- runtime/local test only when decision-changing；
- 0 recommendation 合法、强匹配优先、结论稳定即停。

**结论：不推倒重来。**

## 3. 第一轮发现的问题

### P0-1 — Authority / fact drift

观察到：

- 根 README 仍写 Skill `0.6.0`，实际 runtime 已是 `0.6.3`；
- `PROJECT_WORKFLOW.md` 已声明 historical，却仍把已历史化的 `PROTOCOL_V2` 写成 current authority；
- `SKILL_BLUEPRINT_V3.md` 仍写“do not implement”，但 Skill 已多轮实现；
- top-level 历史/条件性设计与当前 authority 并列，增加新 Agent 误读风险。

根因：项目缺少一个**单一导航地图 + 机械一致性约束**。

### P0-2 — REAL_USER_ORIGIN 与 REAL_USER_USE 混名

Case 001/002 来源于真实问卷问题，但由 Cloud 研究生成；原路径却叫 `docs/pilot/PILOT_CASE_*`。

这会把两件事混淆：

- 真实问题来源；
- 真实用户已经使用产品。

根因：provenance 与 adoption evidence 没有在文件结构上硬分开。

### P0-3 — “最佳实践”措辞超过证据覆盖

当前项目目标确实是帮用户找最佳做法，但某个具体 case 的证据可能只是：

- 一个 author self-practice；
- 少量 community discussion；
- 当前可见候选集合。

如果 runtime 默认逼 Agent 写“最佳”，容易把 decision-relative recommendation 误写成 universal claim。

### P1-1 — C 模式仍有 test-coordinator 回弹

0.6.3 已明确 Curator ≠ test coordinator，但部分详细 working-model/reference 仍保留“C 必须最小试验”的历史表达。

这会再次把“暂不值得复杂化”执行成“让用户替项目测试工具”。

### P1-2 — Runtime Skill package 混入项目历史 README

`skills/curating-erp-ai-resources/README.md` 记录版本演化与 Pilot 状态，并与 `SKILL.md` 重复。

问题不是多一个文件，而是它会独立 drift，并占用 runtime/reviewer attention。

### P1-3 — 没有 deterministic project contract check

已经发生过：版本、路径、current authority、case lane 的事实漂移，需要人工发现。

这些都属于机器可判问题，却没有自动检查。

### P1-4 — Source Adapter 条件性设计容易产生 architecture gravity

WeChat / Xiaohongshu / Bilibili adapter 设计本身有价值，但还没有证明它应成为当前默认架构。它应该是 **conditional design**，不是 current product dependency。

## 4. 向优秀 Skill / Harness 学到什么

本项目此前的 21-Skill 研究已经得到一组正确结论，本轮重新确认这些结论仍适用：

- Anthropic `skill-creator`：description 是 trigger 核心；progressive disclosure；真实 prompt 行为比规则数量重要；
- `academy-guide`：strong match 才推荐，最多 1–2，弱匹配时 silence better than noise；
- `deep-research`：搜索为决策服务，主动防 confirmation/accumulation；同源复读不是独立证据；
- `skill-creator-plus`：judgment 用 instructions，deterministic work 才适合 scripts/validators；
- `xlsx`：机器校验通过不等于业务/逻辑正确；
- Agent Skills spec：主 `SKILL.md` 保持核心流程，复杂材料按需进入 references；
- OpenAI Harness Engineering：给 Agent **map, not a huge manual**；真正重要的不变量用机械约束，而不是继续堆说明。

内部研究 authority：

- `docs/phase-01-skill-research/SKILL_PATTERN_STUDY.md`
- `docs/phase-01-skill-research/DESIGN_SYNTHESIS.md`

外部设计参考：

- https://agentskills.io/specification
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- https://openai.com/index/harness-engineering/

## 5. 对抗性复审：第一轮结论哪里可能错

### Attack A — 是否因为文档漂移就要重构整个产品？

否。

North Star 和方法主干在多次异构任务上已经反复收敛。文档 drift 说明的是 Harness/事实层不稳，不证明产品逻辑必须推倒。

### Attack B — 是否应该新增更多 Gate/validator 来防偏航？

否。

高判断任务如果继续转成 fields/Gates，会重演 V0.4：Agent 优化“通过检查”，而不是“给用户做更好的选择”。

只对**确定性事实**机械检查：文件、版本、路径、reference、状态名、链接。

### Attack C — 是否应该把所有历史文档删掉？

否。

历史资产有证据价值。正确做法是通过 Project Map 降权，并让 current authority 不再引用错误历史入口。

### Attack D — 是否应该马上改 Skill 名称？

暂不改。

`curating-erp-ai-resources` 确实偏 resource-centric，但当前 `description` 才是主要 trigger。没有真实 trigger failure 证明重命名收益值得迁移成本，先不制造无价值改动。

### Attack E — 是否应该马上激活 Source Adapter 架构？

否。

只有重复、material source acquisition gap 真正改变推荐质量时才激活。当前先保持 conditional design。

### Attack F — 既然产品要找最佳实践，是否应该对所有 case 搜更多来源？

否。

“最佳”在产品目标层可以成立；在单次 recommendation 层应写成**当前任务/约束/已取得证据下最值得优先借鉴**。来源数量不是质量。

## 6. 已执行整改

### R1 — 建立单一 Project Map

新增 `docs/PROJECT_MAP.md`：

- 给 current authority 明确层级；
- 明确新会话默认读取顺序；
- 把历史/conditional docs 降权；
- 把 REAL_USER_ORIGIN / REAL_USER_USE 分成两个 Lane。

### R2 — Skill 0.7.0

运行时 Skill 校准为：

- current baseline first；
- A/B/C by capability gap + adoption cost；
- information missing != C；
- practitioner/author/implementation/official/synthesis 分层；
- decision-relative recommendation，不滥用 universal “best”；
- C 默认低成本学习/采用路径，不自动测试；
- 0 资源合法、默认最多一个主资源；
- Curator 与 execution coach/test coordinator 明确分离。

### R3 — Runtime Skill 减负

删除 Skill 目录中的历史 README；运行时只保留 `SKILL.md + references/`。

### R4 — Case lane 重命名

旧 `docs/pilot/PILOT_CASE_001/002` 删除，迁移为：

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md`
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md`

统一状态：

> `REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE`

### R5 — Pilot contract 重新定义

`docs/REAL_USER_PILOT_V1.md` 现在只负责 `REAL_USER_USE VALIDATION`，不再把 Cloud curation 或问卷 problem origin 算作用户采用。

### R6 — Current facts 同步

README / Current Plan / Handoff / Evidence Status 同步到 0.7.0 和两 Lane 模型。

### R7 — Mechanical Harness

新增 `scripts/check_project_contract.py` 与 GitHub Action（见仓库），只检查机器可判的项目 contract：

- current authority 文件存在；
- Skill version 与 current docs 一致；
- runtime Skill package 无历史 README；
- references 存在；
- old Pilot case path 已消失；
- curation cases 明确写 `NOT USER-USE EVIDENCE`；
- Project Map 相对 Markdown 链接有效。

它**不判断推荐质量、不打分、不替代真实用户证据**。

## 7. 明确没有做的整改

本轮故意不做：

- Skill rename；
- resource DB / refresh；
- fixed scenario taxonomy；
- scoring/Gate；
- recommendation-quality validator；
- source adapter 安装/激活；
- multi-Agent orchestration；
- 新 synthetic benchmark；
- 把 83 份问卷批量全部 curation；
- 为 Case 001/002 写永久场景答案。

原因：没有第一性证据说明删掉这些“不做项”后用户结果会明显变差。

## 8. 整改后再校准

整改完成后必须满足：

- `PROJECT_MAP` 是唯一导航入口；
- current docs 的 Skill version 完全一致；
- case provenance/adoption lane 从目录和状态名即可判断；
- runtime Skill 不再携带项目历史 README；
- C 不再默认指向用户 test protocol；
- high-evidence wording 有显式边界；
- project contract checker 通过；
- PR diff 不引入新框架/新 taxonomy/新 scoring；
- Source Adapter 仍是 conditional design；
- REAL_USER_USE 仍未被错误宣布为已验证。

任何一项不成立，都不能宣布本轮校准完成。

## 9. 最终项目结论

当前最准确的状态不是“Skill 已完善”或“产品已验证”，而是：

> **产品方法骨架已经稳定；0.7.0 完成了项目/Harness 级校准；当前正在做 bounded REAL_USER_ORIGIN curation，REAL_USER_USE 产品价值仍未验证。**

最大剩余风险仍然是：

> **强模型/普通搜索本身是否已经足够好，以至于 Curator 没有稳定的额外价值。**

这不能靠更多规则或内部 validator 解决。

## 10. 近阶段与下一步

当前近阶段：`Curation Pack 01`。

已有 B 类真实来源 Case 001/002。下一步 Cloud 直接完成：

1. Case 003 — 多顾问周报/PPT 汇总与数据准确性，作为 A/no-new-tool 边界候选；
2. Case 004 — 程序 Bug / ERP system-access boundary；
3. 对 4 个 case 做一次 bounded adversarial review，然后停止批量 curation。

不要预设 Case 003/004 的 A/B/C；结果必须从真实问题、当前 baseline 和证据重新判断。

REAL_USER_USE 反馈只要自然出现，立即进入 Evidence Status；不要求用户替项目执行测试。