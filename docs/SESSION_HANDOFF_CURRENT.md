# ERP AI Curator — Current Session Handoff

Date: 2026-08-30
Status: **CURRENT / CONTROLLED REAL-USER USE**

> 新会话不要从历史聊天或旧 validation 文档恢复状态。先读 `docs/PROJECT_MAP.md`。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

只有具体任务需要时再读 runtime Skill、Trial Guide、Real User Use Validation、AI Leverage、Adversarial Review 或历史材料。

## 2. 当前产品

ERP AI Curator 是**真实 ERP / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心问题：

> **当前 AI / 工具链是否已经够用？如果不够，什么已经存在的实践、Tool / Skill / MCP / 方法 / 教程最值得在当前任务和约束下优先学习/采用？如果用户明确要找最佳实践/教程，就替他真正完成 practitioner/resource 筛选。**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.1**
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

0.7.1 保留：

- 真实 baseline first；
- capability gap + adoption cost 决定 A/B/C；
- `信息不足 != C`；
- practitioner-first，author self-practice 不冒充独立验证；
- 默认“当前任务下优先推荐”，不滥用“最佳/唯一/已验证”；
- C 不自动让用户测试工具；
- runtime/local test 只在 decision-changing 时做；
- Curator != execution coach / test coordinator。

新增真实缺陷修正：

> **`A = 不新增 Tool/Skill` ≠ `A = 不需要找最佳实践/教程`。**

当用户明确请求最佳实践/教程/实战资源：

- practitioner discovery 是任务本身；
- 中文泛 ERP / ToB / 产品经理/顾问语境优先检查 Bilibili、公众号、小红书及相关 practitioner 生态；
- official/standard 主要用于事实/能力/标准核验；
- 输出优先给 1–3 个真正值得看的实操资源和优先级，再做 synthesis；
- official-only + 模型自写教程不是合格完成。

Runtime reference：`references/practitioner-discovery.md`。

## 4. 触发 0.7.1 的真实受控试用缺陷

用户明确要求：

> “使用这个 skill 给我找下做流程图的最佳实践”

0.7.0 的实际答案：

- 判 A；
- 引用 OMG / Camunda / Microsoft / ASQ；
- 自己总结 8 条画图规则和 Prompt；
- 没有筛出用户期待的 B站/公众号/小红书/产品经理/ToB AI 实战资源。

Cloud 随后用公开 Web 即发现多个强匹配 Bilibili practitioner/tutorial 候选，因此失败不是内容稀缺，而是 runtime discovery routing 不够可执行。

这是一条真实 Controlled User Trial defect，不是 synthetic card。

## 5. Curation Pack 01 — CLOSED

Authority：`docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`。

- Case 001 — ERP 操作手册：B；
- Case 002 — Oracle EBS AI 开发：B；
- Case 003 — 周报/PPT 汇总：A；
- Case 004 — SAP Bug / system evidence access：A → conditional B。

Pack 不重新打开。0.7.1 由真实用户反馈触发。

## 6. 当前发布裁决

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

不要把“能投用户试用”写成“产品目标已经验证完成”。

## 7. 当前下一步

当前 immediate action：

1. 完成 0.7.1 practitioner discovery patch；
2. 同一个流程图 Prompt 做 bounded regression；
3. Project Contract / PR adversarial review 通过后合并；
4. 继续 controlled real-user use。

原宿主如果随后重新运行同一 Prompt，结果是额外 cross-host/runtime evidence，不应成为 Cloud 合并窄修正的前置阻塞。

## 8. Cloud / Local / Owner

Cloud 能做就继续直接做，包括：真实反馈证据审查、当前 Web/GitHub practitioner discovery、窄缺陷修正、GitHub authority 维护。

Local Agent 只在真实决策依赖本地 repo/runtime/ERP 环境/受保护 evidence，或必须验证某个宿主真实 Skill/reference 路由行为时接力。

Owner 当前只有一个潜在明确裁决项：**如果要声明 public/open-source release complete，需要选择 repository license。** Agent 不擅自选择许可证。

## 9. 绝对不要复活

除非真实 evidence 证明必要，不要重新启动：

- V0.4 Gate/scoring/taxonomy/validator；
- synthetic benchmark loop；
- 更多 pre-user Curation Card；
- resource DB / auto refresh；
- creator/UP 主排行榜；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- user tool-test protocol；
- 已失效 P03/P07 Result 01；
- 历史 `PROJECT_WORKFLOW.md` 的旧 CURRENT/NEXT。
