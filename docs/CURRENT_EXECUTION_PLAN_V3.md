# ERP AI Curator — Current Execution Plan

Date: 2026-08-30
Status: **CURRENT**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / 企业信息化工作任务，判断当前 AI / 工具链是否已经够用；如果不够，从互联网上已经存在的实践、Tool / Skill / MCP / 方法 / 教程中筛出少量真正值得优先学习和采用的方案。**

Main chain:

```text
real task + current baseline + hard constraints
→ AI leverage / capability-gap judgement
→ practitioner evidence when needed
→ original implementation verification
→ decision-changing official facts
→ compact adoption recommendation
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. 当前方法结论

历史异构任务 P01/P03/P04/P06/P07 与后续边界回归已经足以支持一个稳定方法骨架：

1. 从真实任务、材料、当前 baseline、交付物和硬约束开始；
2. A/B/C 由 capability gap + adoption cost 决定；
3. external adoption question 优先 practitioner experience，再核验 implementation / current facts；
4. source-grounded analysis 优先于模型记忆；
5. runtime/local test 只在 decision-changing 时出现；
6. 0 个资源合法；强匹配优先于覆盖率；
7. 结论稳定即停止。

**没有证据支持重建 Gate、评分、taxonomy、资源数据库或多 Agent pipeline。**

## 3. 当前 Skill

- `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.0**
- stage: **Curation pilot — user-use value unvalidated**

0.7.0 是项目级校准后的 runtime 版本：

- 用真实 baseline，不和裸模型比较；
- 默认说“当前任务下优先推荐实践”，不滥用“最佳/唯一/已验证”；
- `信息不足 != C`；
- C 默认给低成本学习/采用路径，不把用户变成测试员；
- Skill 主体只保留稳定流程，详细边界按需进 references。

## 4. 两条证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION（当前 Cloud 可持续推进）

真实同事/问卷/Owner 的真实问题 → Curator 研究与推荐。

当前已形成：

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md`
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md`

这类结果是**真实来源 curation output**，不是用户采用证据。

### Lane B — REAL_USER_USE VALIDATION（外部反馈 Lane）

真实同事收到推荐后自然学习、采用、修改、拒绝或忽略。

Authority: `docs/REAL_USER_PILOT_V1.md`。

只有 Lane B 能证明真实用户价值、节省搜索/判断成本、减少错选或返工。

## 5. 近阶段目标 — bounded Curation Pack 01

不要无限把 83 份问卷全部“做一遍”。只再补两个**高区分度**真实来源问题，使当前 curation pack 同时覆盖：

- 已确认需要专业能力的 B 类：Case 001 / 002；
- 一个应明确说“无需新增 Tool/Skill”的 A 类控制案例；
- 一个企业系统/权限/真实访问会改变推荐的边界案例。

目的不是覆盖率，而是确认 0.7.0 能在不同采用边界上稳定做 Curator。

完成 Pack 01 后，默认停止继续批量 curation，回看：

- 推荐是否真的比普通自搜索更有信息密度；
- 是否仍出现 over/under-tooling；
- 是否还会把 author self-practice 写成独立验证；
- 是否还会把 Curator 变成执行教练；
- 是否存在值得真实同事优先看到的结果。

这仍属于 Lane A，不冒充 Lane B 产品验证。

## 6. 下一执行动作

Cloud 下一步直接完成：

1. **Case 003 — 多顾问周报/PPT 汇总与数据准确性检查**：优先验证 A/no-new-tool 是否成立；
2. **Case 004 — SAP/ERP 程序 Bug 定位或运维系统访问边界**：验证什么时候 ordinary repo/log analysis 足够，什么时候真实系统/元数据访问才值得升级。

不要预设 A/B/C；按 0.7.0 从原始问题重新判断。

## 7. Cloud / Local Agent 边界

Cloud owns：

- public Web/GitHub research；
- practitioner / implementation / official fact separation；
- product judgement and adversarial review；
- GitHub authority maintenance；
- cloud-executable curation cases。

Local Agent 只在真实决策依赖以下内容时接力：

- 本地项目文件 / repo / runtime；
- 企业 ERP 环境；
- 当前系统元数据/日志/权限；
- Cloud 无法获得且会改变结论的受保护 evidence。

Agent 可用性本身不是派活理由。

## 8. Anti-drift

除非真实使用/明确 blocker 证明必要，不新增：

- synthetic validation loop；
- fixed scenario taxonomy；
- scoring / Gate；
- resource database / refresh；
- mandatory runtime benchmark；
- multi-Agent orchestration；
- creator ranking；
- source-adapter framework activation；
- card-specific permanent rules；
- user test protocol as Curator default output。

Source Adapter 设计目前只是 conditional design，只有重复、material acquisition gap 真正影响推荐时才重新激活。

## 9. 当前完成标准

近阶段完成不是“更多 Case 数量”，而是：

> **完成 4 个高区分度 REAL_USER_ORIGIN curation 后，能明确说明 0.7.0 在 A/B/系统访问边界上是否稳定；同时保持 REAL_USER_USE 仍为唯一产品价值验证 Lane。**
