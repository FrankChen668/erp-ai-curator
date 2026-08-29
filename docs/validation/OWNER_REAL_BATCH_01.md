# OWNER_REAL Batch 01 — Cloud Review Cards

Date: 2026-08-29

Purpose: run Protocol V2 on the currently evidenced `OWNER_REAL` problems. These are stronger than synthetic evals, but they are still not broader `REAL_USER` validation.

Important: older conversations did not always preserve the exact original wording in the repository. Therefore the task text below is marked as **reconstructed from project context**, not falsely presented as a verbatim quote.

---

## OR01 — 可编辑 draw.io 业务流程图

**Source:** OWNER_REAL  
**Role:** implementation / product consultant  
**Original problem status:** reconstructed from project context  
**Need external resource?** yes

### Real need

希望 Agent 能直接生成 **可编辑 draw.io** 的业务流程图，而不是静态图片；最好能支持泳道 / 跨职能流程，并能在 Claude Code / Codex 一类本地 Agent 中使用。

### Recommendation 1 — jgraph/drawio-mcp

https://github.com/jgraph/drawio-mcp

**Why this is the default pick**

- draw.io 官方仓库；
- 当前明确提供 Claude Code、Codex CLI、GitHub Copilot plugin；
- plugin 直接生成原生 `.drawio`，可继续编辑；
- 官方 `shared/xml-reference.md` 已包含 BPMN-style swimlane / cross-functional guidance；
- 不需要因为“业务流程图”再叠加一个只为泳道补能力的第二 Skill。

**Critical limitation**

- hosted MCP App 会把 diagram request 发到 draw.io server；严格数据隔离时应选本地 Tool Server / Assistant Plugin；
- PNG / SVG / PDF 本地导出依赖 draw.io Desktop CLI，但 `.drawio` 本体不依赖导出。

### Recommendation 2 — Agents365-ai/drawio-skill（高级场景）

https://github.com/Agents365-ai/drawio-skill

只在以下需要出现时保留为第二推荐：

- 想要更多预设（BPMN / cross-functional / C4 / architecture 等）；
- 想从 codebase / Terraform / Kubernetes / SQL 自动反推图；
- 想要视觉 self-check / auto-fix 等更重工作流。

对于普通 ERP 业务流程图，**官方 jgraph 方案已经够强，优先从 1 个资源开始。**

### Cloud judgement

High confidence。当前结论比旧 Batch 01 更收敛：默认 1 个主推荐，第二个只在高级需求出现时进入推荐位。

**Owner judgement:** pending  
**Observed use:** pending

---

## OR02 — 快速生成可评审的交互原型

**Source:** OWNER_REAL  
**Role:** consultant / product manager  
**Original problem status:** reconstructed from project context  
**Need external resource?** yes

### Real need

从需求快速生成可以给客户 / 业务评审的交互原型，最好低门槛、可在本地 Agent 里直接迭代，而不是只输出静态 UI 图。

### Recommendation 1 — JimLiu/baoyu-design

https://github.com/JimLiu/baoyu-design

**Why**

- Agent Skill，支持 Claude Code / Cursor / Codex 等本地 Agent；
- 可做 interactive prototype、wireframe、mockup、dashboard 等；
- 输出 self-contained HTML，可直接预览和继续修改；
- 有简体中文 README；
- 当前仓库活跃，且工作流明确支持浏览器预览和指点式二次修改。

**Critical limitation**

这是通用设计 Skill，不理解 ERP 业务本身。最终原型是否有价值，仍高度依赖输入需求、业务约束和评审反馈。

### Recommendation 2 — kurenn/claude-prototype

https://github.com/kurenn/claude-prototype

**Why it remains differentiated**

- 更窄地针对 stakeholder review / sales demo / design exploration；
- 强调 discovery Q&A 后再建原型；
- 输出 clickable HTML，零 build step；
- 有明确 feedback / assess 流程。

**When to choose which**

- 想要更综合、更强设计能力、多 Agent：`baoyu-design`；
- 想要更轻、更专注“快速可评审原型”：`claude-prototype`。

### Cloud judgement

High confidence。两个资源不是为了凑数，而是分别代表“综合设计引擎”和“窄场景原型工作流”。

**Owner judgement:** pending  
**Observed use:** pending

---

## OR03 — Claude Code / Codex 第三方或低成本模型路径

**Source:** OWNER_REAL  
**Role:** developer / advanced Agent user  
**Original problem status:** reconstructed from project context  
**Need external resource?** yes

### Real need

希望在 Claude Code / Codex 中使用 OpenRouter 或第三方 / 低成本模型，同时避免照着已经过时的环境变量、proxy 教程或 model 配置踩坑。

### Recommendation 1 — OpenRouter Ori Harness

https://openrouter.ai/blog/announcements/ori-harness/

**Why this becomes the default entry**

OpenRouter 在 2026-08-04 发布 Ori Harness，当前明确支持：

- `ori claude`
- `ori codex`
- `ori opencode`
- `ori hermes`

它把不同 harness 的配置差异和部分模型兼容设置收进一个官方 setup path。对于“我要尽快可用”比手写多组变量更合理。

### Manual evidence anchors — 不默认占第二推荐位

Claude Code 官方 OpenRouter 文档：
https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration

Codex CLI 官方 OpenRouter 指南：
https://openrouter.ai/blog/tutorials/codex-cli-openrouter/

这些用于需要手工控制配置、排错或理解兼容边界时。

### Critical limitations

- OpenRouter 当前明确说明：Claude Code **只保证 Anthropic first-party provider 的完整兼容性**；非 Anthropic 模型“能运行”不等于 Claude Code 官方支持；
- Codex CLI custom provider 与 Desktop / App surface 必须分开判断；
- 这是高波动主题，推荐时必须重新打开当前官方页面，不把本文件中的配置值当永久真相。

### Cloud judgement

High confidence。**当前默认先推 Ori，而不是继续维护一批旧的“低成本模型手工配置教程”。**

**Owner judgement:** pending  
**Observed use:** pending

---

## OR04 — AI 改善 Fit-to-Standard / Fit-Gap / 需求分析

**Source:** OWNER_REAL  
**Role:** implementation consultant  
**Original problem status:** reconstructed from project context  
**Need external resource?** yes

### Real need

希望找到比“AI 可以帮你写需求”更具体的实践：AI 如何进入真实实施项目的 Fit-to-Standard、Fit-Gap、需求沉淀或 solution design 工作。

### SAP Recommendation 1 — SAP Cloud ALM AI-Assisted Requirement Generation

https://help.sap.com/docs/cloud-alm/applicationhelp/ai-assisted-requirement-generation-65a0305515864d94bb9b02d39eb259f8

**Why**

- 直接针对 Fit-to-Standard workshop transcripts / documentation；
- 把 workshop 内容生成 implementation requirement；
- SAP Activate 2026-07 更新中已经把 AI-assisted requirement generation / workshop summary prompt 写入相关实施 procedure；
- 这是“AI 真正进入顾问交付链”的当前实例，不是泛方法论。

### SAP Recommendation 2 — SAP Joule for Consultants: Project Lifecycle

https://learning.sap.com/courses/introducing-sap-joule-for-consultants/applying-sap-joule-for-consultants-across-the-sap-project-lifecycle

**Why**

- 明确按 SAP Activate 生命周期组织；
- Explore 阶段直接讨论 fit-gap analysis；
- 覆盖标准流程、配置选项、设计依据等典型顾问问题。

### Oracle Recommendation — Oracle Fusion + AI: Functional Consultant Crash Course

https://www.udemy.com/course/oracle-fusion-cloud-chatgpt-functional-consultant/

**Why it now enters the candidate set**

- 2026-05 更新，明确面向 Oracle Fusion functional / implementation consultant；
- 不是泛 Prompt 课，课程直接覆盖：workshop notes → requirement summary、BRD / MD050 / functional design、UAT scenarios、troubleshooting、client communication；
- 使用一个五元素框架：Role / Context / Task / Format / Constraints；
- 作者公开经历中可看到 Oracle Cloud Fusion implementation / go-live 项目经验。

**Critical limitation**

- 非 Oracle 官方；
- 课程很短（约 40 分钟），更像实战入门框架而不是完整 methodology；
- 当前公开可见的课程口碑样本较少，因此**任务匹配高，但可信度只给 medium**；
- 不把课程自述的效率数字当独立事实。

### Cloud judgement

SAP：high confidence。  
Oracle：**从“0 推荐”修正为“1 个 medium-confidence、高任务匹配候选”**。这次纠正说明：对资源稀缺主题不能过早 abstain，需要至少一次更深的跨源搜索。

**Owner judgement:** pending  
**Observed use:** pending

---

## OR05 — 用 AI 快速学习陌生 SAP / Oracle 模块

**Source:** OWNER_REAL  
**Role:** implementation consultant  
**Original problem status:** reconstructed from project context  
**Need external resource?** yes

### Real need

临时进入陌生模块时，希望 AI 帮助建立：业务流程 → 配置链路 → 关键对象 / 表 / 主数据 → 常见问题 → 验证路径，而不是泛泛地“问 ChatGPT”。

### SAP Recommendation 1 — Prompting with SAP Joule for Consultants

https://learning.sap.com/courses/outlining-use-cases-for-sap-joule-for-consultants-in-finance/prompting-with-sap-joule-for-consultants

**Why**

- 给出 Who / What / How prompt framework；
- 明确要求 role、business problem、output structure；
- 强调验证回答、迭代 prompt；
- 可以直接迁移成陌生模块学习的提问骨架。

### SAP Recommendation 2 — Introducing SAP Joule for Consultants

https://learning.sap.com/courses/introducing-sap-joule-for-consultants

**Why**

- 面向 Consultant，不是泛 AI 课程；
- 覆盖 role-aware prompting、SAP Activate 生命周期和 consultant tasks；
- 当前课程提供中文版本；
- 官方说明其知识源包含大量 SAP 专属 / 非公开支持资料，这是通用 Web AI 不具备的优势。

### Oracle result

**仍然 0 个正式推荐。**

本轮更深搜索发现了 Oracle Fusion 顾问 AI 实战课，但它解决的是 requirements / design / UAT / troubleshooting，并没有提供一套“如何用 AI 系统学习陌生 Oracle 模块”的学习方法。

当前 Oracle 公开资源仍主要是：

- Fusion 产品课程；
- AI Agent Studio 开发 / 配置；
- 产品内置 AI Agent 使用说明。

因此 OR05 的 Oracle 子问题仍保持空缺。若真实 Oracle 顾问反复提出这个需求，**它更可能需要我们自己沉淀方法资产，而不是继续寻找并不存在的完美外部 Skill。**

### Cloud judgement

SAP：medium-high confidence；Oracle：current public gap remains meaningful after deeper search。

**Owner judgement:** pending  
**Observed use:** pending

---

# Batch conclusion

## What this batch supports

1. `OWNER_REAL` 问题确实可以驱动一个小型资源决策层；
2. draw.io / prototype / model routing 三类问题能形成明确、当前可用的推荐；
3. SAP 顾问 AI 资源开始出现非常具体的官方实践，不再只是泛 prompting；
4. Oracle 顾问侧并非“完全没有资源”：需求 / 设计 / UAT 场景已找到一个高匹配但中等可信度的实战课程；
5. Oracle“陌生模块 AI 学习方法”仍然是明显空缺；
6. 对稀缺主题，**第一次搜不到 ≠ 应立即判 0 推荐**，需要至少一次有针对性的跨源深搜；深搜后仍无强匹配，才把 abstain 视为较高置信结论。

## What this batch does NOT support

- 不证明 PM 场景已经验证；
- 不证明开发人员覆盖充分；
- 不证明 Skill 是最终形态；
- 不证明上述资源已经被目标用户实际使用；
- 不授权建设大型资源数据库。

## Next cloud action

优先接收真实培训问卷和实际求助问题，并按 `REAL_TASK_INTAKE.md` 进入同一闭环。

在没有更多 `REAL_USER` 数据前，云端继续：

1. 对高价值 Starter Pack 做当前性维护；
2. 对反复出现但外部资源弱的主题判断：继续搜索，还是转成内部自建方法资产。
