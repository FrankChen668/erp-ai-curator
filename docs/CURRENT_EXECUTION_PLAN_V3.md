# ERP AI Curator — Current Execution Plan

Date: 2026-08-31
Status: **CURRENT — CONTROLLED REAL-USER USE**

> Navigation authority: `docs/PROJECT_MAP.md`. Product authority: `docs/PROJECT_NORTH_STAR.md`.

## 0. Owner execution rule

Cloud/ChatGPT continues every useful cloud-executable next step. It stops only for a genuine Owner decision, Local Agent-only access/runtime, or external evidence barrier. Authority: `docs/OWNER_EXECUTION_RULES.md`.

## 1. Product objective

> **面对真实 ERP / ToB / 企业信息化工作任务，帮用户找到真正值得学习的现成 AI 实践；当用户明确做能力选型时，再判断当前工具链是否够用、是否值得新增能力。**

Product remains one Curator. Runtime 0.9.0 uses two single-responsibility Skills:

```text
Practice intent
→ curating-erp-ai-resources
→ practitioner discovery / inspection / selection

Capability intent
→ advising-erp-ai-capabilities
→ current baseline / concrete gap / minimum useful upgrade or no-upgrade
```

Curator 不是工具目录、资源数据库、执行 SOP 生成器或工具认证实验室。

## 2. Current Runtime — 0.9.0

### Practice Curator

`skills/curating-erp-ai-resources/SKILL.md`

负责：最佳实践、教程、真实 workflow/case、值得先学的 practitioner 资源。

默认不做：Tool/Skill/MCP 安装/采用判断。

Reference：

- `references/practitioner-discovery.md`

### Capability Advisor

`skills/advising-erp-ai-capabilities/SKILL.md`

负责：当前工具链是否够、是否存在具体能力缺口、是否值得新增 Tool/Skill/MCP/plugin/Agent/workflow、最小升级是什么。

默认不做：泛最佳实践/教程资源策展。

Reference：

- `references/evidence-and-safety.md`

Release class: **CONTROLLED USER TRIAL**  
Product value: **UNVALIDATED**

Authority：`docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`。

## 3. Why 0.9.0

同一句真实自然请求：

> “使用这个 skill 给我找下做流程图的最佳实践”

连续版本表现：

- 0.7.x：官网/规范 + 模型自写教程；
- 0.8.1：找到 practitioner，但又推荐 SVG Skill + 安装命令；
- 0.8.2：即使已经写入 no-incidental-install guardrail，仍直接推荐 `mermaid-visualizer`、installs/Stars、安全审计和安装命令。

这说明问题不再是“Skill body 少一条规则”，而是原 description 同时承载实践策展和能力选型，导致强 Tool/Skill/MCP 语义污染 practice-only 请求。

因此 0.9.0 把边界前移到 Skill metadata/description 层，不再继续 0.8.x patch-on-patch。

## 4. Adversarial constraints

0.9.0 明确不做：

- 第三个 Router Skill；
- A/B/C runtime taxonomy；
- language/platform quota；
- creator scoring/ranking；
- Tool marketplace scan as default；
- Browser/Graph Engineering/host-policy workaround；
- duplicated broad references across both Skills。

两 Skill 是**运行职责拆分**，不是两个产品。

## 5. Host/Harness risks remain separate

此前真实日志仍暴露：

- Codex Web policy 可能存在 `technical questions → primary sources only` 冲突；
- Graph Engineering Skill collision / over-triggering；
- Browser/Chrome 是否需要 source-acquisition fallback 未验证。

这些没有足够证据成为 Curator Runtime 规则。

## 6. Curation Pack 01 — closed

Authority: `docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`.

- Case 001 — ERP 操作手册：历史 B；
- Case 002 — Oracle EBS 开发：历史 B；
- Case 003 — 多顾问周报/PPT 汇总：历史 A；
- Case 004 — SAP Bug/system evidence access：历史 A → conditional B。

旧标签仅是历史分析证据，不定义 0.9.0 Runtime。

## 7. Current milestone — Controlled REAL_USER_USE

受控试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

允许真实 ERP/企业信息化用户用自然问题使用；不要求固定 benchmark、工具测试协议、长问卷或为了覆盖类别继续制造 Case。

当前最重要的未验证目标：

> **Curator 是否能持续比普通 AI/自搜索更高信任、更低噪声地找到值得学的实践，并在能力选型时减少错装/错选，且这个差异足以让真实用户再次使用？**

## 8. Cloud / Local Agent boundary

Cloud owns：

- 自然真实反馈的证据审查；
- 当前 Web/GitHub practitioner discovery 与事实核验；
- 窄缺陷修正；
- GitHub authority/Harness 维护。

Local Agent 只在真实决策依赖本地 repo/runtime、企业 ERP 环境、受保护 evidence，或必须验证具体宿主 Skill trigger/reference/Web 行为时接力。

Agent 可用性本身不是派活理由。

## 9. Release boundary

### GO

- controlled user trial。

### HOLD

- organization-wide mandatory standard；
- “产品价值已验证”声明；
- 全宿主兼容声明；
- public/open-source release completion。

公开/open-source 发布仍需要 Owner 明确 repository license。

## 10. Anti-drift

真实用户未暴露必要性前，不新增：

- synthetic validation loop；
- fixed scenario taxonomy；
- scoring/Gate；
- resource database/refresh；
- mandatory runtime benchmark；
- 第三个 Router Skill；
- multi-Agent orchestration；
- creator ranking；
- source-adapter framework as default architecture；
- card-specific permanent rules；
- user test protocol as default output。

## 11. Next

0.9.0 合并后继续自然 controlled use。

最高价值观察仍是原始 practice-only 请求：

> “使用这个 skill 给我找下做流程图的最佳实践”

预期：只触发 Practice Curator，并输出 practitioner practice/resources，而不是 Skill 安装建议。

另外自然观察一个明确 capability 请求，例如：

> “我现在 ChatGPT + draw.io 已经够了吗，要不要装专门 Skill？”

预期：由 Capability Advisor 先确认具体 gap，可以合法得出“不需要新增”。

如果仍失败，优先取宿主 trigger/load/search 证据，不再根据最终答案继续加 Runtime 规则。
