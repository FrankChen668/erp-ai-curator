# ERP AI Curator — Current Session Handoff

Date: 2026-08-31
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

只有具体任务需要时再读 Runtime Skills、Trial Guide、Real User Use Validation 或历史材料。

## 2. 当前产品

ERP AI Curator 是**一个产品**，面向真实 ERP / ToB / 企业信息化工作问题。

核心用户结果：

> **真正需要找实践时，替用户筛出值得学的 practitioner workflow；真正需要做能力选型时，判断当前工具是否够用、是否存在值得采用成本的能力缺口。**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. Current Runtime — 0.9.0

0.9.0 不再用一个 Skill 同时承担两个默认行为。

### Practice Curator

`skills/curating-erp-ai-resources/`

- best practices / tutorials / real workflows / cases / practitioner resources；
- 不主动做 Tool/Skill/MCP adoption；
- reference：`practitioner-discovery.md`。

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- current toolchain enough?；
- add/install/choose/compare Tool/Skill/MCP/plugin/Agent/workflow?；
- concrete capability gap → minimum useful upgrade or explicit no-upgrade；
- reference：`evidence-and-safety.md`。

两个 Skill metadata.version 都是 `0.9.0`。

Authority：`docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`。

## 4. Why 0.9.0

同一句 practice-only 请求连续暴露串台：

> “使用这个 skill 给我找下做流程图的最佳实践”

- 0.7.x：官网/规范 + 模型自写教程；
- 0.8.1：practitioner discovery 改善，但随后推荐 SVG Skill + 安装；
- 0.8.2：已有 no-install guardrail，仍直接推荐 `mermaid-visualizer`、安装量/Stars/安全审计和安装命令。

因此根因上移为：**一个 description 同时包含“最佳实践”和“Tool/Skill/MCP 采用”语义，practice-only 请求仍被能力选型吸引。**

0.9.0 用 description/trigger 单一职责拆分解决，不再继续在同一个 body 里补规则。

## 5. Adversarial boundary

不要重新引入：

- 第三个 Router Skill；
- A/B/C runtime taxonomy；
- scoring/Gate；
- language/platform quota；
- creator ranking；
- broad Tool marketplace scan；
- Browser/Graph Engineering/host-policy workaround as Curator rules。

两个 Runtime Skills 不是两个产品。

## 6. Historical evidence

Curation Pack 01 保持关闭。旧 A/B/C 标签只是历史分析记录，不定义 0.9.0 Runtime。

0.7.x / 0.8.x flowchart 结果保留为真实负面执行证据；它们证明了串台问题，但不能证明 0.9.0 已修复或产品价值已验证。

## 7. Current release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

当前真正未验证的是：Curator 是否比普通 AI/自搜索更稳定地找到高价值实践、减少错选，并让用户愿意再次使用。

## 8. Next

0.9.0 合并后继续自然 controlled use。

最重要的两个自然请求：

- practice-only：`给我找下做流程图的最佳实践` → 应只进入 Practice Curator；
- capability-only：`我现在 ChatGPT + draw.io 够不够，要不要装 Skill？` → 应进入 Capability Advisor。

如果宿主仍串台，先取实际 trigger/load/search 证据，再决定是否需要宿主级修正；不要再靠最终答案给 Skill 加补丁。

## 9. Cloud / Local / Owner

Cloud 能做就继续直接做，包括真实反馈证据审查、Web/GitHub discovery、窄缺陷修正和 authority/Harness 维护。

Local Agent 只在本地 repo/runtime/ERP 环境/受保护 evidence 或具体宿主 trigger/load 行为验证真正需要时接力。

Owner 当前唯一潜在明确裁决项仍是 repository license（仅当要声明 public/open-source release complete 时）。
