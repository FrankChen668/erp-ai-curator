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

## 3. 当前 Skill — 0.8.2

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

0.8.0 完成 runtime simplification；0.8.1 修 query intent / practitioner investigation；0.8.2 只修 candidate selection：

- **audience/ecosystem fit**：同质量时优先用户语言/地区/职业生态匹配的 practitioner；海外资源只有明显更强或本地覆盖不足时才上位；
- **artifact fit**：推荐内容/能力必须真的支持用户需要的交付物，例如 SVG-only 不等于 editable draw.io；
- **no incidental install**：最佳实践/教程请求本身不构成安装 Tool/Skill 的理由。

Runtime 仍只有两个按需 reference：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

Authority：`docs/validation/CURATOR_082_CANDIDATE_SELECTION_PATCH.md`。

## 4. 触发 0.8.2 的真实结果

0.8.1 的新鲜运行已经能找到 practitioner 内容，但最终优先了日文 Qiita 实践，并额外推荐 `html-svg-diagrams` Skill。

诊断：

- practitioner discovery 有改善；
- 但候选排序没有保住中文泛 ERP / ToB / 产品经理生态；
- editable draw.io 目标与 SVG Skill 能力不匹配；
- 用户未要求新 Tool/Skill，却出现安装建议。

这不是“日本资源不能用”；是 audience/artifact fit 没有成为选择优先级。

## 5. Host risks — 当前不要塞回 Skill

仍记录但不写入 runtime：

- Codex technical→primary-source policy 潜在冲突；
- Graph Engineering Skill collision；
- Browser/Chrome fallback 是否必要未验证。

## 6. Curation Pack 01 — CLOSED

旧 A/B/C 标签仅是历史分析记录，不定义 runtime。不要重新启动 pre-user case accumulation。

## 7. 当前发布裁决

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

产品价值仍未验证。

## 8. 当前下一步

继续自然 controlled use。重点观察：

- 是否优先出现用户职业/语言生态匹配的 practitioner；
- 海外资源是否真的有明显增量价值；
- 推荐 Tool/Skill 是否匹配目标 artifact；
- 未要求新能力时是否仍出现不必要安装建议。

只有重复真实缺陷再修，不继续内部堆规则。

## 9. Cloud / Local / Owner

Cloud 能做就继续直接做，包括真实反馈证据审查、Web/GitHub discovery、窄缺陷修正和 authority 维护。

Local Agent 只在本地 repo/runtime/ERP 环境/受保护 evidence 或具体宿主行为验证真正需要时接力。

Owner 当前唯一潜在明确裁决项仍是 repository license（仅当要声明 public/open-source release complete 时）。

## 10. 绝对不要复活

除非真实 evidence 证明必要，不要重新启动 Gate/scoring/taxonomy、synthetic benchmark、更多 pre-user Case、resource DB、creator ranking、source-adapter default architecture、multi-Agent orchestration 或 user tool-test protocol。
