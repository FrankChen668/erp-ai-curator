# 给 SAP/Oracle 实施顾问的「Agent 生成可编辑 draw.io 业务流程图」资源推荐（少而精）

先说结论：**不要找"通用画图 Skill"凑数，真正能用的一条主线只有 draw.io 官方那条。** 下面 5 个是我实际打开原始页面核对过的，按"该装哪个 / 该读哪个"排序。

---

## 1. draw.io 官方 Claude Code 插件（Skill）—— 主线，必装

- **原始链接**：https://github.com/jgraph/drawio-mcp
- **是什么**：draw.io（jgraph）官方仓库，提供 4 种接入方式：MCP App Server、MCP Tool Server（npm 包 `@drawio/mcp`）、**Assistant Plugins（Claude Code / Codex CLI / GitHub Copilot）**、Project Instructions。Claude Code 用的就是其中第 3 种。
- **安装（官方 README 现行命令）**：
  ```
  /plugin marketplace add jgraph/drawio-mcp
  /plugin install drawio@drawio
  ```
  或本地加载：`claude --plugin-dir ./plugins/claude-code`
- **注意一个坑**：网上大量中文教程还在让你 `cp drawio/SKILL.md ~/.claude/skills/drawio/` 并写路径是 `skill-cli/`。**这个目录已经重构掉了**——`skill-cli/` 被合并进 `plugins/claude-code/`（技能文件在 `plugins/claude-code/skills/drawio/SKILL.md`）。老教程的命令现在会 404。
- **对你最关键的一点**：它生成的是**原生 `.drawio` XML**，导出 PNG/SVG/PDF 时用 `--embed-diagram` 把 XML 嵌进文件，所以**导出的图片拖回 draw.io 还能继续改**——这才是"可编辑"的落点，而不是截图片。
- **格式支持（我核对过仓库 README 的对照表）**：Claude Code 插件这一路**只支持 XML（原生格式）**；Mermaid 和 CSV 只有 MCP Tool Server 与 Project Instructions 支持。所以别指望在 Claude Code 里 `/drawio` 直接吃 Mermaid。
- **前置依赖**：要用导出功能，必须装 draw.io Desktop（CLI）。

## 2. nilecui/diagram_wk（drawio-diagrams-enhanced）—— 中文，且最贴你的业务场景

- **原始链接**：https://github.com/nilecui/diagram_wk
- **技能路径**：`.claude/skills/drawio-diagrams-enhanced/SKILL.md`
- **README 是中英双语的**（这点对中文用户很友好），覆盖的图类型正好是实施交付物那一套：
  - 泳道图（CFF 跨职能流程图）→ 对应"财务/销售/仓库"多部门职责切分
  - BPMN → 对应流程蓝图
  - RACI 责任分配矩阵、WBS、甘特、PERT/CPM、风险矩阵、干系人图（PMP/PMBOK 系列）
- **内置了形状与配色规范表**（开始/成功 `#d5e8d4`/`#82b366`、处理步骤 `#dae8fc`/`#6c8ebf`、决策 `#fff2cc`/`#d6b656` 等），Agent 照表出图，风格能统一——这比让模型每次自由发挥靠谱得多。
- **实测痕迹**：仓库里有 `approval_flowchart.drawio`（审批流）和 `software_dev_wbs.drawio` 两个成品，说明是真跑通过的。
- **缺点，要如实说**：仓库只有 2026-01-17 的一次提交记录，**基本不再维护**。建议当成"规范与模板参考"抄进你自己的 SKILL.md，而不是长期依赖它。

## 3. Harrsion-H/ai-drawio-skill —— 官方的中文优化 fork，工程化更完整

- **原始链接**：https://github.com/Harrsion-H/ai-drawio-skill
- **定位**：官方 drawio-mcp 的 fork，重点是 `skill-drawio/` 这个统一技能目录。仓库简介是中文（"根据官方MCP，整理优化出的一套纯CLI skill，可用于claude code、openclaw等agent"），但 README 和脚本是英文。
- **安装**：
  ```
  npx skills add Harrsion-H/ai-drawio-skill
  # 或 cp -r skill-drawio ~/.claude/skills/drawio
  ```
- **比官方多出来的东西，正好补官方的短板**：
  - **Mermaid 优先**：流程图/时序图/ER/类图/状态图/甘特/思维导图等标准类型默认走 Mermaid，让 draw.io 的解析器自动布局——比手工摆 XML 坐标稳得多。需要精确定位、容器/图层、行业形状时才上 XML。
  - **`search_shapes` 形状搜索**（`skill-drawio/scripts/` 带搜索索引，CI 自动同步）：SKILL 里明确写了"带有特定任务类型的 BPMN"属于**应该先搜形状**的场景。你要画标准 BPMN 网关/事件，这个比让模型瞎编 style 字符串强。
  - **XSD 驱动的 `validate-mxfile.js`**：生成后强制跑一遍校验，不合规就修，不允许交付坏 XML。
  - 语义化 ID 规范（`user__login-form` 而不是 `2`），后续让 Agent 增量改图时定位准确得多。
- **最后更新**：2026-05-10（mcp-app-server 相关提交）。

## 4. draw.io 官方：AI 生成图的提示词写法（读完能省一半返工）

- **原始链接**：https://www.drawio.com/docs/best-practice/write-query-generate-diagram/
- 要点（官方原文）：先写图类型（"sequence diagram - ..."）、加 `vertical`/`horizontal` 控制方向、术语前后一致、细节给足但拆成多条短查询（生成器有长度上限，超出直接忽略）。
- **对你最重要的一条限制，官方明文写了**：*Mermaid does not support technical diagrams with more complex notations such as AWS, Azure, BPMN*。也就是说——**业务流程（BPMN、泳道）必须走 XML + BPMN 形状库，别指望 Mermaid 自动布局**。这直接决定了你该用第 1 条还是第 3 条。
- 另外官方提醒：不要把敏感业务信息写进查询。

## 5. BPMN 2.0 形状规范（中文站）—— 把它抄进 SKILL.md，图才有业务语义

- **原始链接（中文）**：https://www.drawio.com.cn/post/88.html
- **英文原版**：https://www.drawio.com/blog/bpmn-2-0.html
- 内容：池（Pool）与泳道（Lane）的职责分组、任务/子流程（底部 `+` 标记）、事件（圆圈，实心/空心、粗/细/虚线轮廓区分中断与否）、**网关四种类型：互斥(or) / 包容(and-or) / 并行(and) / 基于事件**，以及**顺序流（实线实箭头，绝不跨池）vs 消息流（虚线，圆头→空心三角）** 的区别。
- **怎么用**：把这套规则贴进你的 SKILL.md，Agent 才会画出"审批驳回走包容网关、跨系统用消息流"这种对顾问评审有意义的图，而不是一堆方块加箭头。

---

## 针对你这个角色的落地建议

1. **主线用第 1 条（官方插件）**，保证"可编辑 .drawio"这个底线；中文场景和 Mermaid 便利度用第 3 条补充。
2. **建一个你自己的 `SKILL.md` 增量**：把第 2 条的配色/形状规范表 + 第 5 条的 BPMN 语义规则 + 你公司的 SAP/Oracle 术语（如"过账""三单匹配""MM/FI/SD 模块"）写进去。这是别人给不了你的部分。
3. **导出一律用 `.drawio.png` 双扩展名 + `--embed-diagram`**，交付给客户的图片对方也能双击改。
4. **别删 `.drawio` 源文件**。

---

## 附：我没推荐但值得一说的

- **classmethod 的实操避坑文（英文，2026-04-10）**：https://dev.classmethod.jp/en/articles/claude-code-trying-out-drawio-skill-for-aws-architecture/
  虽然是拿 AWS 架构图做的实验，但踩的坑是通用的：图标线条发黑（要显式写 `strokeColor=#ffffff`）、标签压住图标（用 `verticalLabelPosition=bottom;verticalAlign=top`）、连线盖住图形（mxGraph 中同层 edge 总在 vertex 之上，要做 `edge_layer` / `shape_layer` 双层结构）、缺边界（没定义 group 容器）。文章的结论很实在：**官方 Skill 只覆盖通用 draw.io 知识，领域样式规则得自己写进 SKILL.md**。另外它点出一个硬限制——Claude Code 看不到渲染结果，复杂图的边标签坐标是算出来的，往往需要手调。

---

## 运行记录

### 实际使用的搜索关键词
1. `Claude Code skill generate draw.io diagram`
2. `draw.io mermaid AI agent 生成流程图 skill`
3. `Claude Code Skill 中文 教程 业务流程 BPMN drawio 生成`
4. `SAP 实施顾问 AI 生成 流程图 drawio 中文 实操`
5. `drawio BPMN 2.0 shape library 业务流程 泳道 官方文档`

### 实际打开过的原始链接（WebFetch 逐个核对，非仅看搜索摘要）
| 链接 | 核对结果 |
|---|---|
| https://github.com/jgraph/drawio-mcp | ✅ 存在。确认四种接入方式、`skill-cli/` → `plugins/claude-code/` 重构、官方安装命令、各方式格式支持对照表（Claude Code 插件仅 XML） |
| https://github.com/Harrsion-H/ai-drawio-skill | ✅ 存在。确认是官方 fork、`skill-drawio/` 目录、安装命令、`references/mxfile.xsd`、`scripts/` 形状索引、最后更新 2026-05-10 |
| https://skill4agent.com/zh/skill/harrsion-h-ai-drawio-skill/drawio | ✅ 打开。是该 Skill 的**中文翻译版**页面（原仓库为英文），据此确认了 Mermaid/XML 决策表与后端检测逻辑 |
| https://github.com/nilecui/diagram_wk | ✅ 存在。README 中英双语，确认支持泳道/BPMN/RACI/WBS，含配色规范表与两个 .drawio 成品；仅 1 次提交（2026-01-17） |
| https://www.drawio.com/docs/best-practice/write-query-generate-diagram/ | ✅ 打开。确认提示词规则与"Mermaid 不支持 BPMN"这一关键限制 |
| https://www.drawio.com.cn/post/88.html | ✅ 打开。draw.io 中文站 BPMN 2.0 形状说明（原发布于 2021-04-27，为英文博客的中译） |
| https://dev.classmethod.jp/en/articles/claude-code-trying-out-drawio-skill-for-aws-architecture/ | ✅ 打开。发布时间 2026-04-10，确认作者、环境与四类问题的成因/解法 |
| https://github.com/awesome-copilot | ❌ 404 / 指向无关个人用户页 |
| https://github.com/github/awesome-copilot | ⚠️ 仓库存在（GitHub 官方组织下的社区集合），但根目录页与 README **未列出** `draw-io-diagram-generator`，无法从原始来源确认该 Skill 归属 |

### 遇到的异常或失败
1. **`awesome-copilot` 相关 Skill 无法溯源**：两个 Skill 聚合站（claudeskills.info、getclaudeskills.com）都详细描述了 `github/awesome-copilot` 的 `draw-io-diagram-generator`（含 `assets/templates/flowchart.drawio` 等模板、validate 脚本），但我打开 `github/awesome-copilot` 根目录后，**README 只给出分类跳转，没有逐个列出 skill 名称，正文中检索不到 `draw-io-diagram-generator`**。因为无法从一手来源确认，我**没有把它列入正式推荐**，只在此记录。若要采用，需再打开 `docs/README.skills.md` 或 https://awesome-copilot.github.com/skills 复核。
2. **大量中文二手教程的安装命令已过期**：CSDN、语雀、腾讯云开发者社区等文章仍在写 `https://github.com/jgraph/drawio-mcp/tree/main/skill-cli` 这个路径，但该目录已被重构移除。我在推荐里做了显式修正。
3. **第 2 条（nilecui/diagram_wk）维护度低**：仅一次提交，属于"能用但别长期绑定"的资源，已在正文中标注。
4. 搜索结果中出现的若干"AI 生成流程图网站推荐"类文章（如 aijiaohuan.net）内容泛泛、含明显营销成分且与 Agent/Claude Code 无关，已主动剔除。

### 声明
本文所有资源名称、仓库地址、安装命令、日期与功能描述，均来自上述实际联网抓取的页面内容，未使用训练记忆编造。
