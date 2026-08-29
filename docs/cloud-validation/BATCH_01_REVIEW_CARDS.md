# Cloud Product Validation — Batch 01

日期：2026-08-29

说明：本批次不做 baseline，不验证 Skill。本批次只验证产品问题本身：**给定真实 ERP 工作任务，是否能稳定筛出 0–2 个值得继续投入时间的资源。**

Product Owner 只需在每题最后标记：`值得分享 / 一般 / 不值得分享`。

---

## CV01｜SAP / Oracle 顾问生成可编辑 draw.io 业务流程图

### 正式推荐

1. **jgraph/drawio-mcp** — draw.io 官方 Agent Skill / Plugin  
   https://github.com/jgraph/drawio-mcp
   - 直接生成原生 `.drawio`；
   - Claude Code、Codex 等都有插件 / Skill 路径；
   - 支持 Mermaid / XML、自动布局、可编辑导出；
   - 官方仓库的 linked reference 已包含 BPMN-style swimlanes / cross-functional flowcharts。

2. **Agents365-ai/drawio-skill** — 社区增强 Skill  
   https://github.com/Agents365-ai/drawio-skill
   - 明确提供 BPMN、Cross-functional swimlane 等 preset；
   - 有中文 README；
   - 当前仍活跃维护；
   - 更适合需要大量图形预设和自动自检的人。

### 关键限制

官方方案更稳；社区方案更强但更重。不要再推荐只讲旧版手工安装的中文教程。

**Product Owner：待判断**

---

## CV02｜顾问快速生成可评审的交互原型

### 正式推荐

1. **kurenn/claude-prototype** — Claude Code prototype Skill  
   https://github.com/kurenn/claude-prototype
   - 输出真实可点击 HTML 原型，不是静态图；
   - 强调 stakeholder review；
   - 内置 persona / state / feedback loop；
   - 无复杂 build step，适合需求讨论和快速评审。

2. **JimLiu/baoyu-design** — 本地 Agent Design Skill  
   https://github.com/JimLiu/baoyu-design
   - 可生成 mockup、interactive prototype、wireframe、dashboard、mobile UI；
   - 输出 self-contained HTML；
   - 有简体中文文档；
   - 对非设计师顾问更容易直接拿来做评审材料。

### 不推荐为主项

`prototype-to-figma-skill` 很强，但它更偏“已有 working prototype → Figma handoff”，不是需求初期快速做原型的第一工具。

**Product Owner：待判断**

---

## CV03｜Claude Code 接 OpenRouter / 第三方模型，当前有效方法

### 正式推荐

1. **OpenRouter — Claude Code Integration**  
   https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration
   - OpenRouter 官方维护；
   - 当前配置围绕 `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN`；
   - 明确写出兼容限制和 `/logout`、`/status` 等排错步骤；
   - 适合作为当前配置入口。

2. **musistudio/claude-code-router**  
   https://github.com/musistudio/claude-code-router
   - 更适合真正要切换 DeepSeek / Gemini / OpenAI-compatible 等非 Anthropic 模型；
   - 本地 gateway + 多模型路由；
   - 活跃社区项目。

### 关键限制

Anthropic 对“通过第三方 gateway 跑非 Claude 模型”不提供官方支持保证。因此要明确区分：**技术可运行 ≠ Anthropic 官方支持**。

**Product Owner：待判断**

---

## CV04｜Codex CLI 第三方 / 低成本模型方案

### 正式推荐

1. **OpenRouter — Codex CLI with OpenRouter**  
   https://openrouter.ai/blog/tutorials/codex-cli-openrouter/
   - 当前明确使用 `[model_providers.openrouter]`；
   - `wire_api = "responses"`；
   - `base_url = "https://openrouter.ai/api/v1"`；
   - 使用 profile 切换模型，步骤直接可执行。

### 证据锚点（不占推荐位）

OpenAI Codex 当前 schema 明确支持用户自定义 `model_providers` 与 `model_provider`，`wire_api` 当前 schema 默认是 Responses：  
https://github.com/openai/codex/blob/main/codex-rs/core/config.schema.json

### 关键限制

- **CLI/TUI 与 Codex Desktop 要分开看。** 当前社区 issue 显示 Desktop 对 custom provider / model picker 仍存在明显限制；
- project-local `model_providers` 也出现过被忽略的问题，稳妥做法是 user-level `~/.codex/config.toml` + profile；
- 所以本题只推荐“Codex CLI 路径”，不把它泛化成 Desktop 完整支持。

**Product Owner：待判断**

---

## CV05｜SAP Fit-to-Standard / Fit-Gap 的 AI 实战资源

### 正式推荐

1. **SAP Cloud ALM — Requirement Generation**  
   https://www.sap.com/products/technology-platform/cloud-alm-requirement-generation.html
   - 这是非常直接的 Fit-to-Standard 场景：从 workshop transcript / meeting notes 自动生成业务需求；
   - 使用预定义 requirement template；
   - 结合 SAP Activate / SAP Best Practices 辅助提出 solution proposal；
   - 和“AI 帮顾问做 Fit-to-Standard 后的需求沉淀”高度匹配。

2. **SAP Joule for Consultants — Across the SAP Project Lifecycle**  
   https://learning.sap.com/courses/introducing-sap-joule-for-consultants/applying-sap-joule-for-consultants-across-the-sap-project-lifecycle
   - 官方明确把 Explore 阶段定位为 fit-gap analysis；
   - 讲解如何用 Joule 查询标准流程、配置选项和设计依据；
   - 更适合作为方法与使用思路补充。

### 关键限制

这两项都是 SAP 产品生态能力，不是“通用 Agent Skill”。如果用户没有 Cloud ALM / Joule for Consultants 权限，迁移价值会下降。

**Product Owner：待判断**

---

## CV06｜Oracle 实施需求调研 / Solution Design 的 AI 实战方法

### 正式推荐

**0 个。**

当前公开资源里能找到：

- Oracle 官方需求定义方法；
- Oracle AI Agent Studio 的 prompt engineering；
- Oracle Fusion 内置 AI / agent 开发资料；

但没有找到一个真正面向 **Oracle 实施顾问需求调研 / Solution Design 工作本身**、可以直接照着用的 AI 方法 / Skill / 实战案例。

### 相邻资源（不占推荐位）

Oracle 官方的 requirements 基线：  
https://docs.oracle.com/en/cloud/saas/analytics/26r1/fawig/define-business-requirements-use-cases.html

它适合做“正确的需求结构是什么”的依据，但不是 AI 方法。

**Product Owner：待判断**

---

## CV07｜SAP 陌生模块快速学习方法 / Prompt Framework

### 正式推荐

1. **Prompting with SAP Joule for Consultants**  
   https://learning.sap.com/courses/outlining-use-cases-for-sap-joule-for-consultants-in-finance/prompting-with-sap-joule-for-consultants
   - 给出 Who / What / How 框架；
   - 强调角色、业务问题、输出结构；
   - 明确要求 consultant 验证答案；
   - 可直接迁移成“陌生模块学习”的提问框架。

2. **Introducing SAP Joule for Consultants（含中文版）**  
   https://learning.sap.com/courses/introducing-sap-joule-for-consultants-zh
   - 官方面向 Consultant；
   - 覆盖角色化 prompting、SAP Activate 生命周期、Prompt Library；
   - 对临时进入陌生 SAP 模块的人比泛 ChatGPT prompt 更可靠，因为 Joule for Consultants 基于 SAP 专属知识源。

### 关键限制

核心价值依赖 Joule for Consultants 的访问权限。若没有权限，这两项更多是 prompt 结构参考，而不是完整替代方案。

**Product Owner：待判断**

---

## CV08｜Oracle Fusion 陌生模块快速学习的 AI 方法 / Prompt Framework

### 正式推荐

**0 个。**

当前能找到很多：

- Oracle Fusion AI Agent Studio prompt engineering；
- Oracle 官方 Fusion 课程；
- Oracle 内置 AI Agent 使用资料；

但没有发现一份真正解决：

> “我是 Oracle Fusion 某模块新手，如何用 AI 系统理解业务流程、配置链路、关键对象，并验证回答”

的高质量公开方法 / prompt framework。

### 相邻资源（不占推荐位）

`oracle-fusion-docs-mcp` 可以把 Agent 接到 Oracle 文档，解决“AI 靠记忆乱答”的问题：  
https://github.com/SimonKreis-Richard/oracle-fusion-docs-mcp

但它是文档检索 Tool，不是学习方法，因此不占正式推荐位。

**Product Owner：待判断**

---

## CV09｜只找“读取代码仓库并生成架构图”的 Agent Skill

### 正式推荐

1. **beadnall/codemap**  
   https://github.com/beadnall/codemap
   - 明确是 Claude Skill；
   - 直接读取 codebase 并生成可探索架构图；
   - 强调从代码和文档中挖真实架构事实，而不是按目录树画盒子；
   - 还能通过 GitHub API 分析未 clone 仓库。

2. **okaneconnor/agent-skills — excalidraw-diagram**  
   https://github.com/okaneconnor/agent-skills
   - 明确定位为分析 software / infrastructure codebase 后生成 Excalidraw 架构图；
   - 可覆盖 architecture overview、auth flow、data flow、deployment topology、sequence flow；
   - 强调每个 shape / arrow 回溯到 repo `file:line` 证据。

### 关键限制

`codemap` 更偏深度理解和可探索视觉；`excalidraw-diagram` 更偏传统架构交付图。两者用途不同，保留 2 个有真实差异。

**Product Owner：待判断**

---

## CV10｜Oracle EBS 老版本 AI 自动 Fit-Gap 成熟开源 Skill

### 正式推荐

**0 个。**

搜索能找到 Oracle EBS Fit-Gap / implementation simulation 项目，但没有发现同时满足以下条件的资源：

- Oracle EBS 老版本专用；
- AI 自动 Fit-Gap；
- Agent Skill；
- 开源；
- 成熟可落地。

例如 `Oracle-EBS-AP-AR-Implementation-Simulation` 是实施模拟 / Fit-Gap 学习项目，不是 AI Skill，不能冒充答案。

本题应明确返回没有，而不是拿 SAP、Oracle Fusion 或普通需求分析 Skill 填空。

**Product Owner：待判断**

---

# Batch 01 初步观察

本轮 10 题里：

- **明确有强资源：7 题**（CV01/02/03/04/05/07/09）
- **合理 0 推荐：3 题**（CV06/08/10）

说明这个产品并不是“每题都应该找到东西”。它真正的价值恰好包括：

1. 找到当前真正强的资源；
2. 把官方事实和用户资源分开；
3. 在稀缺主题上明确保持空缺；
4. 不用相邻资源填答案。

下一步只需要 Product Owner 对 10 题做业务判断：`值得分享 / 一般 / 不值得分享`。
