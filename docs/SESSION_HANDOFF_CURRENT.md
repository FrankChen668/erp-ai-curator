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

ERP AI Curator 是**真实 ERP / ToB / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心问题：

> **当前 AI / 工具链是否已经够用？如果不够，什么已经存在的实践、Tool / Skill / MCP / 方法 / 教程最值得在当前任务和约束下优先学习/采用？如果用户明确要找最佳实践/教程，就替他真正完成 practitioner/resource 筛选。**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. 当前 Skill — 0.8.1

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

0.8.0 完成 runtime simplification；0.8.1 只增加两条由真实 Codex Desktop 日志证明必要的执行要求：

- **query intent preservation**：如果原问题是“用 AI/Agent/Tool 改善某工作”，practitioner discovery 至少保留一条 `AI/tool × role/industry/artifact` query，不能退化成纯领域最佳实践搜索；
- **candidate investigation**：明确找实践/教程时，必须实际打开至少一个 practitioner/creator 候选；如果宿主 policy/coverage/access 阻止，则明确 `coverage/policy gap`，不能用官网补位后声称完成。

Runtime 仍只有两个按需 reference：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

关键行为仍然必须成立：

- 明确找最佳实践/教程时，真正给 practitioner 资源，不用官网+自写教程代替；
- 当前工具已经够用时，不因为 Curator 身份强推 Tool/Skill；
- author self-practice 不冒充独立验证；
- official 主要核验当前事实；
- 强匹配优先，少推荐，结论稳定即停；
- 诊断/理解默认 read-only，权限最小化。

## 4. 触发 0.8.1 的实际日志

本次 Codex Desktop 运行不是干净的 0.8.0 独立测试：前半段先用了 0.6.1/拟议 0.6.2 并进行了官方导向搜索，之后才同步 `main@d6165fa` 到 0.8.0 并继续同一上下文。

但同步后的日志直接证明：

- `SKILL.md 0.8.0` 和两个 references 确实被读取；
- 第二批搜索仍丢掉 AI / 产品经理 / ToB / ERP 语境；
- Bilibili、公众号、小红书、知乎、人人都是产品经理、掘金/CSDN 未实际定向搜索；
- 已出现的中文 practitioner 候选基本未打开；
- 最终来源仍由 official/standard/implementation 主导。

Authority：`docs/validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`。

## 5. Host risks — 当前不要塞回 Skill

日志还暴露：

- Codex Web policy 可能存在 technical→primary-source-only 冲突；
- Graph Engineering 被“多步骤任务”错误触发，属于 Skill collision；
- Browser/Chrome 可用但未调用，是否需要 source-acquisition fallback 仍未知。

这些都还没有足够证据成为 Curator runtime 规则。

## 6. Curation Pack 01 — CLOSED

Authority：`docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`。

- Case 001 — ERP 操作手册：历史 B；
- Case 002 — Oracle EBS AI 开发：历史 B；
- Case 003 — 周报/PPT 汇总：历史 A；
- Case 004 — SAP Bug / system evidence access：历史 A → conditional B。

旧 A/B/C 标签仅是历史分析记录，不再定义 runtime。不要重新启动 pre-user case accumulation。

## 7. 当前发布裁决

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

不要把“能投用户试用”写成“产品目标已经验证完成”。

## 8. 当前下一步

0.8.1 合并后，在**全新 Codex Desktop 上下文**同步最新 `main`，再用同一句自然问题重跑：

> “使用这个 skill 给我找下做流程图的最佳实践”

不修改 Skill、不复用旧搜索上下文、不人为指定必须搜的平台。只返回可观察执行事实：实际 query、reference、打开的 practitioner 候选、最终来源角色、明确的 host policy/coverage 失败。

若仍失败，再区分 Skill execution、host source policy、search coverage、Skill collision 或 source acquisition；不要继续靠最终答案猜根因。

## 9. Cloud / Local / Owner

Cloud 能做就继续直接做，包括：真实反馈证据审查、当前 Web/GitHub practitioner discovery、窄缺陷修正、GitHub authority 维护。

Local Agent 只在真实决策依赖本地 repo/runtime/ERP 环境/受保护 evidence，或必须验证某个宿主真实 Skill/reference 路由行为时接力。

Owner 当前只有一个潜在明确裁决项：**如果要声明 public/open-source release complete，需要选择 repository license。** Agent 不擅自选择许可证。

## 10. 绝对不要复活

除非真实 evidence 证明必要，不要重新启动：

- Gate/scoring/taxonomy/validator；
- synthetic benchmark loop；
- 更多 pre-user Curation Card；
- resource DB / auto refresh；
- creator/UP 主排行榜；
- source-adapter framework as default architecture；
- multi-Agent orchestration；
- user tool-test protocol；
- card-specific permanent rules。
