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

## 3. 当前 Skill — 0.8.2

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

0.8.0 完成 runtime simplification；0.8.1 修正 query intent / practitioner investigation；0.8.2 只增加三条 candidate-selection 边界：

- **audience/ecosystem fit**：同质量时优先用户语言/地区/职业生态匹配的 practitioner；跨语言资源只有明显更强或本地覆盖不足时才上位；
- **artifact fit**：推荐内容/能力必须真的支持用户需要的交付物，例如 SVG-only 不等于 editable draw.io；
- **no incidental install**：最佳实践/教程请求本身不构成安装 Tool/Skill 的理由。

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

Authority：`docs/validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md`。

## 4. 触发 0.8.2 的真实结果

新鲜 0.8.1 运行已经能找到 practitioner 内容，但最终优先了日文 Qiita 实践，并额外推荐 `html-svg-diagrams` Skill。

直接问题：

- 中文泛 ERP / ToB / 产品经理生态没有在 candidate selection 中被保留；
- editable draw.io 目标与 SVG Skill 能力不一致；
- 用户未要求新 Tool/Skill，却出现安装建议。

这不是“日本资源不能用”；是 audience/artifact fit 与 adoption restraint 没有成为选择优先级。

## 5. Host risks — 当前不要塞回 Skill

此前日志仍暴露：

- Codex Web policy 可能存在 technical→primary-source-only 冲突；
- Graph Engineering 被“多步骤任务”错误触发，属于 Skill collision；
- Browser/Chrome 可用但是否需要 source-acquisition fallback 仍未知。

这些没有足够证据成为 Curator runtime 规则。

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

继续自然 controlled use，重点观察：

- 是否优先出现用户职业/语言生态匹配的 practitioner；
- 海外资源是否真的有明显增量价值；
- 推荐 Tool/Skill 是否匹配目标 artifact；
- 未要求新能力时是否仍出现不必要安装建议。

只有重复真实缺陷再修，不继续内部堆规则。

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
