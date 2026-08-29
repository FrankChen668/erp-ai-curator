# E01 eval 结果 — with-skill

## 第一部分：面向用户的最终回答

### 任务理解

你要找的是：SAP/Oracle 实施顾问可用的、能用 **Claude Code 或类似 Agent** 生成**可编辑 draw.io 业务流程图**的 AI Skill/实操资源。关键约束是"可编辑"——即产出 `.drawio` 原生 XML 文件，能在 draw.io 里继续拖拽修改，而不是一次性 PNG 图片。中文高质量资源可优先（同等质量下的 tie-breaker）。

### 推荐（2 个）

| 资源 | 类型 | 为什么值得看 | 能得到什么 | 重要限制 |
|---|---|---|---|---|
| [drawio-mcp — Draw.io Plugin for Claude Code](https://github.com/jgraph/drawio-mcp)（draw.io 官方团队） | Skill（Claude Code 插件） | 官方基准实现：在 Claude Code 里用自然语言描述流程即生成原生 `.drawio` 文件，官方团队持续维护，是"Agent 画可编辑图"最不容易踩坑的选择。 | 装好后直接描述流程即产出可编辑 `.drawio`；用 Mermaid 或 draw.io XML 两种方式构图，可选 ELK 自动布局，导出 PNG/SVG/PDF 时把 XML 嵌入文件（拖回 draw.io 仍可编辑）；同一仓库还提供 MCP Server 与 Project Instructions，共 4 种接入方式。 | Mermaid 自动转图、ELK 布局、图片导出依赖本地 draw.io Desktop；只生成 `.drawio` 文件（或 URL 模式）则无需桌面版。 |
| [drawio-skill — From Text to Professional Diagrams](https://github.com/Agents365-ai/drawio-skill)（Agents365-ai） | Skill（社区增强，兼容 Claude Code 等 6 种 Agent） | 内置 **BPMN 与跨功能泳道（cross-functional swimlane）预设**，正对 ERP 顾问画跨部门业务流程/泳道图的场景；仓库有 **README_CN.md 中文文档**，活跃维护（2026-08 仍在发版）。 | 11 种图表预设（BPMN、泳道、ERD、时序、C4 等），自然语言生成可编辑 `.drawio`，自动布局 + 渲染自检自动修复，10000+ 官方图标（AWS/Azure/GCP/BPMN 等）搜索，还能把代码库/数据库/SQL 直接转成图。 | 第三方社区项目（非 draw.io 官方）；Mermaid 转换与 ELK 布局要求 draw.io Desktop ≥ 30；功能多，学习曲线比官方插件略陡。 |

### 为什么没有推荐更多

- **中文教程类**：搜索到的高质量中文内容（腾讯云开发者社区、mdnice 等）基本是公众号文章转载，原始出处不可追溯，且内容与官方 drawio-mcp 仓库高度重合（安装步骤、格式说明）。按"原始来源优先"不作为推荐位；官方仓库 README 本身已足够当实操指南。
- **SAP 原生方案（相邻提示，不计入推荐）**：SAP Signavio 的 AI-assisted process modeler（text-to-process）可把文字直接转成 BPMN 图。但按 SAP 官方博客信息，它需 Signavio 商业许可，产出的是 Signavio 内的 BPMN 模型而非 draw.io 文件，也不属于"Claude Code/Agent"工作流，与你的约束不符，故不占推荐位。
- **专门的 BPMN skill（sparklabx/drawio-ai-kit 的 drawio-bpmn）**：能力与推荐 2 重叠，且需额外安装 npm CLI，安装链更长，未入选。
- 其余搜索结果（如 aijiaohuan.net 等"AI 流程图网站盘点"）为内容农场/盘点文，无实操产出，直接排除。

### 给你的实操建议（基于已打开内容）

- **只想先用起来、少折腾**：装官方插件（Claude Code 内 `/plugin marketplace add jgraph/drawio-mcp` 后 `/plugin install drawio@drawio`），说一句"画一个订单到收款（OTC）端到端流程泳道图"即可得到 `.drawio` 文件。
- **需要规范的 BPMN/泳道语义、或想要中文文档辅助**：装 drawio-skill（`npx skills add Agents365-ai/365-skills -g`），看 README_CN.md。
- 两个方案中，官方插件在需要 Mermaid 转图/导出图片时要求 draw.io Desktop，drawio-skill 要求 draw.io Desktop ≥ 30；如果只是生成可编辑的 `.drawio` 文件，可以不用桌面版，直接用网页版（app.diagrams.net）打开继续编辑。

---

## 第二部分：运行记录

### 1. 实际使用的搜索关键词

| # | 关键词 | 语言 | 覆盖角度 |
|---|---|---|---|
| 1 | Claude Code draw.io skill generate editable diagram skill | 英文 | 按工具环境 + 产出物 |
| 2 | Claude 生成 drawio 可编辑流程图 Skill 教程 | 中文 | 中文侧资源 |
| 3 | drawio-mcp-server Claude generate drawio files | 英文 | 官方 MCP 项目 |
| 4 | SAP 顾问 AI 生成业务流程 drawio 流程图 实践 | 中文 | ERP 专属 + 中文 |
| 5 | SAP Oracle implementation consultant generate business process flow diagram AI agent | 英文 | ERP 专属 |
| 6 | draw.io BPMN skill Claude Code ERP consultant 业务流程 泳道 | 中英混合 | 补 BPMN/泳道专门 skill |

### 2. 实际打开过的原始链接及结论

| 链接 | 打开方式 | 读到什么 / 结论 |
|---|---|---|
| github.com/jgraph/drawio-mcp/blob/main/plugins/claude-code/README.md | WebFetch | 官方 Claude Code 插件 README。确认：插件 marketplace 安装命令（`/plugin marketplace add jgraph/drawio-mcp` → `/plugin install drawio@drawio`）及手动复制 SKILL.md 方式；生成原生 `.drawio`；Mermaid/XML 双路径；ELK 布局；PNG/SVG/PDF 内嵌 XML 保持可编辑；draw.io Desktop 仅 Mermaid 转图/布局/导出需要。→ 作为推荐 1。 |
| mdnice.com/writing/d58e907042c64da694f226ad93752030（《说一句话,流程图就画好了——手把手教你用 AI 画 draw.io》） | WebFetch | 中文实操教程，覆盖官方 drawio-mcp 的 5 种接入方式、实战 prompt、工具对比，质量高；但页面无作者署名、无原始公众号出处（判断为转载），且内容与官方仓库重合。→ 不作为推荐对象。 |
| github.com/Agents365-ai/drawio-skill | WebFetch | 官方仓库 README。确认：兼容 Claude Code 等 6 种 Agent（Agent Skills 格式）；11 种预设含 BPMN、Cross-Functional Swimlane；有 README_CN.md；三种安装方式；要求 draw.io ≥ 30（Mermaid 转换/ELK）；生成可编辑 `.drawio`；2026-08-28 发布 v2.3.0，活跃维护。→ 作为推荐 2。 |
| cloud.tencent.com/developer/article/2654888（《draw.io发布官方Skill,可编辑AI生成的图表》） | 搜索结果摘要（未单独 WebFetch） | 转载自公众号"PM智圈-PMAIhub"（原始发表 2026-03-01），讲解官方 skill 的两步安装与避坑点。内容与官方仓库重合，无独立原始出处。→ 不作为推荐对象。 |

### 3. 实际读取的 references 及读取环节（顺序）

1. **source-strategy.md** — 开始联网搜索前读取。指导：多角度关键词（按动作/工具环境/产出物/人群）、原始来源优先、ERP 专属与通用可迁移并行、中文是 tie-breaker 而非质量豁免、1-2 个明显更强候选即可停止。
2. **selection-heuristics.md** — 第一轮搜索后出现多个候选（官方 skill、官方 MCP、中文教程、第三方 skill）需要横向取舍时读取。指导：核心三问（task fit / 能得到什么 / 差异化）、官方资源 dual-role（user resource vs evidence anchor）、star 是弱证据、避免为覆盖全面保留重复候选、语言 tie-breaker 只在质量相当时生效。
3. **volatile-fact-check.md** — 确定推荐中包含"安装与配置"信息（两个推荐项的安装命令、draw.io Desktop 依赖、版本要求 ≥ 30）时读取。指导：安装/配置类必须回到当前官方/原始来源核验，第三方与官方冲突时不推荐第三方，不执行命令验证。

### 4. 高风险事实核验

- **触发项**：安装与配置（两个推荐项的安装命令）；模型/环境兼容（Claude Code、draw.io Desktop 版本要求）；依赖（draw.io Desktop / draw.io ≥ 30）。
- **结果：核验通过。** 推荐 1 的安装命令与依赖来自 jgraph 官方 README（WebFetch 原文）；推荐 2 的安装命令与 draw.io ≥ 30 要求来自 Agents365-ai 官方仓库 README（WebFetch 原文）。第三方中文教程中的安装命令与官方一致，未发现冲突。
- **边界遵守**：未运行任何安装命令验证，未下载未知程序。SAP Signavio 的 GA 时间与新能力仅作为"相邻说明"引用 SAP 官方博客自述信息，并注明是厂商来源，不进入推荐位。

### 5. 遇到的异常或失败

- 无 WebFetch 抓取失败。
- mdnice 页面无作者署名、无原始公众号出处，无法从转载站回到原始出处（如实记录，作为该中文候选不入推荐位的原因之一）。
- 搜索引擎返回多篇"AI 流程图网站盘点"类内容农场文章（aijiaohuan.net 等），无实操产出，已排除。

### 6. 中文 tie-breaker 的处理

用户提示"中文有高质量的可以优先"。处理路径：
- 优先评估中文侧候选（腾讯云开发者社区、mdnice、CSDN 共 3 篇相关文章）。
- 质量核验后：中文侧高质量内容均为公众号转载、无原始出处、与官方仓库高度重合，不满足"原始来源优先"，未占推荐位。
- 推荐 2（Agents365-ai/drawio-skill）自带 README_CN.md 中文文档，在功能相当的基础上以中文优势计入推荐理由——即中文仅作为同等质量下的 tie-breaker，未因此豁免转载内容。

### 7. 停止条件

达到 source-strategy 的停止条件：已有 2 个明显强于其他候选的资源（官方插件 + 场景增强 skill），继续搜索反复遇到同一批转载或更弱候选（内容农场盘点文、泛化教程）。
