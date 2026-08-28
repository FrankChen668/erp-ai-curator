# ERP AI Curator — 项目协作与阶段协议

> 状态：工作协议草案。用于约束云端设计、业务裁决与本地 Agent 执行之间的边界。

## 1. 第一性目标

本项目不是为了“做一个复杂的 Skill”，也不是为了“建设一个完备的资源数据库”。

项目只在一种情况下创造价值：

> **当 SAP / Oracle / ERP 顾问面对一个真实工作任务时，能够比自己搜索更快地找到少量真正值得点击、学习或使用的 AI 资源。**

任何工程设计、数据结构、脚本、评分体系和自动化，如果不能明显改善这一结果，都不应优先进入主线。

## 2. 三方角色

### 2.1 业务 Owner（用户）

负责：

- 定义真实业务需求与优先级；
- 判断最终推荐是否“真的值得分享给同事”；
- 裁决产品边界与取舍；
- 对阶段性方案给出 Go / Rework / Stop。

### 2.2 云端设计与审查（ChatGPT）

负责：

- 外部研究与开源方案对比；
- 第一性产品设计；
- Skill 架构设计；
- 对抗性审查；
- 为本地 Agent 编写明确 SPEC / Task / Acceptance Criteria；
- 审查 GitHub diff / PR / 测试证据；
- 发现偏航时回到产品目标，而不是继续补规则。

### 2.3 本地 Agent

负责：

- 按已批准的 SPEC 修改仓库；
- 执行本地测试、Skill Eval、脚本和实际运行；
- 记录可复核证据；
- 提交 branch / commit / PR。

硬边界：

- 不得自行改变产品目标；
- 不得为了让测试通过而修改验收标准；
- 不得把“补工程能力”作为默认解法；
- 发现 SPEC 不清、冲突或实现受阻时，报告问题，不自行重定义需求。

## 3. 阶段模型

### Phase 0 — Repository Cleanup

目的：把历史设计、测试产物、Skill 本体和冻结资产分开。

完成标准：

- 仓库结构清楚；
- V0.2–V0.4 历史资料保留但退出主线；
- staging 不再承载历史回归样本；
- 不修改 Skill 业务逻辑。

### Phase 1 — Open-source Skill Research

目的：先研究成熟 Skill 如何解决真实问题，避免重复造轮子。

主要责任：云端。

必须产出：

- `docs/phase-01-skill-research/README.md`
- `docs/phase-01-skill-research/SKILL_PATTERN_STUDY.md`
- `docs/phase-01-skill-research/DESIGN_SYNTHESIS.md`

完成标准：

- 至少研究 20 个有代表性的 Skill；
- 覆盖高判断型、工程型、确定性文件处理型、路由型、Skill Creator；
- 提炼可迁移设计模式与明确不适用模式；
- 不修改现有 Skill。

### Phase 2 — Product Design

目的：先设计产品，再设计 Skill。

必须回答：

1. 谁在什么场景下使用？
2. 用户输入是什么？
3. 核心任务是什么？
4. 最终输出是什么？
5. 明确不做什么？
6. 什么情况下需要强事实核验？
7. 怎样衡量“比不用 Skill 更好”？

必须产出：

- Product Vision
- Core User Journeys
- Product Contract（输入 / 输出 / 非目标）
- Success Metrics
- Adversarial Review
- Product Decision Record

**本阶段禁止写新 Skill 实现。**

### Phase 3 — Skill Architecture & Eval Design

目的：把已批准的产品设计转化为最小 Skill 架构。

重点：

- 以 Anthropic `skill-creator` / Agent Skills 最佳实践作为参考；
- 决定哪些属于 `SKILL.md`，哪些按需进入 `references/`；
- 只把确定性、重复性、可固定验证的工作下沉到 `scripts/`；
- 设计真实用户测试集与 baseline；
- 先定义 Eval，再完成实现规格。

必须产出：

- Skill Architecture
- Trigger Contract
- Context / Reference Routing
- Script-vs-Instruct Decision
- Eval Plan
- Implementation SPEC

### Phase 4 — Local Agent Implementation

目的：由本地 Agent 严格按 SPEC 实现。

每个 Task 必须写清：

- Goal
- Inputs
- Allowed Files
- Forbidden Changes
- Required Outputs
- Acceptance Criteria
- Test Commands
- Evidence Required
- Stop Conditions

本地 Agent 不获得产品重新设计权限。

### Phase 5 — Real-task Evaluation

目的：验证 Skill 是否真正改善用户结果。

至少包含：

- With-skill vs baseline；
- 真实 ERP 顾问任务；
- 用户定性评价；
- 推荐是否值得点击 / 分享；
- 是否出现明显错配、过时、凑数和幻觉；
- 用户纠正次数、任务完成成本等辅助指标。

**内部 JSON / validator 通过只能算工程证据，不能替代产品成功指标。**

### Phase 6 — Production & Maintenance

只有 Phase 5 证明 Skill 有稳定增益后，才讨论：

- 资源持久化；
- Refresh；
- 批量维护；
- 自动化；
- 数据库 / CSV / 网站；
- 更高自治级别。

## 4. 每阶段文档契约

每个阶段必须至少形成一个 README，固定包含：

1. **Problem**：本阶段解决什么问题；
2. **Inputs**：依据什么信息；
3. **Method**：怎么做；
4. **Non-goals**：本阶段明确不做什么；
5. **Deliverables**：形成哪些仓库成果；
6. **Definition of Done**：怎样才算结束；
7. **Decision / Findings**：最终结论；
8. **Handoff**：下一阶段可以依赖什么，不能假设什么。

目的不是增加文档负担，而是建立跨 Agent、跨会话、跨阶段的稳定事实源。

## 5. GitHub 协作原则

- `main`：只保留已确认稳定成果；
- 每个阶段 / 任务单独 branch；
- 重要设计通过文档和 PR diff 审查；
- 历史方案保留在 `docs/history/`，不让旧规则继续隐性控制新设计；
- 本地 Agent 的运行产物与正式产品文档分离；
- 未通过产品验收的实验不得被描述为“生产可用”。

## 6. 反偏航检查

每次计划新增以下内容前，先回答：

> **如果删掉它，最终顾问拿到的推荐会明显变差吗？**

若答案不明确，默认不增加：

- 新 Gate；
- 新评分维度；
- 新数据库表；
- 新脚本；
- 新自动化；
- 新运行状态；
- 新抽象层。

这条规则优先于“让系统看起来更完整”。
