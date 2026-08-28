# 给 SAP/Oracle 实施顾问：用 Agent 生成「可编辑」draw.io 业务流程图的资源推荐

先说结论：**draw.io 自己的官方项目 `jgraph/drawio-mcp` 就够用了**，而且是这一圈里唯一由 draw.io 团队（jgraph）维护、Apache-2.0、近期仍在高频更新的。你不需要去找第三方的"ERP 专用画图 Skill"——目前我没搜到任何一个真正面向 SAP/Oracle 业务流程、且经过验证的高质量中文 Skill，硬凑一个反而是坑。

对顾问场景来说，关键点有两条，我按这两条筛的：
- **产出必须是可继续编辑的原生 `.drawio` 文件**，不是截图、不是 SVG 图片。给客户的流程图改一轮就重画一遍，这件事必须消灭。
- **要能画泳道图 / 跨职能流程图**（角色 × 阶段），因为 SAP 的 MM/SD/FI 流程本质上都是跨部门的泳道图。

---

## 1. 首选：jgraph/drawio-mcp（draw.io 官方）

- 仓库：https://github.com/jgraph/drawio-mcp
- Claude Code 插件文档：https://github.com/jgraph/drawio-mcp/blob/main/plugins/claude-code/README.md

**为什么是它**

- **官方出品**，不是社区野路子。Apache-2.0 开源，仓库仍在活跃维护（近期提交包含 Codex CLI / GitHub Copilot CLI 插件、libavoid 边路由同步等）。
- **Claude Code 插件化安装**，两行命令，不用配 MCP、不用起服务：
  ```
  /plugin marketplace add jgraph/drawio-mcp
  /plugin install drawio@drawio
  ```
- **产出原生 `.drawio` 文件**，可继续手改；也能导出 PNG/SVG/PDF，且**导出的图片里内嵌了 XML**——把 `.drawio.png` 拖回 draw.io 还能完整还原编辑。对"发图给客户、客户还能改"这个场景非常实用。
- **两种写图方式**：装了 draw.io Desktop 就用 Mermaid（自动排版，流程图/时序图最稳）；没装也能直接写 XML 出图，或走 `url` 模式在浏览器打开。PNG/SVG/PDF 导出才依赖 Desktop。
- **支持泳道和跨职能流程图**——见第 2 条。
- **数据不出本机**（插件路线）：文件写在本地，导出走本地 Desktop CLI。给客户画流程图通常涉及真实业务流程，这条对顾问不是小事。托管版 `mcp.draw.io` 会把图表发到官方服务器，涉密流程别用那条路。

**怎么用（顾问场景的写法）**

```
/drawio:drawio 用泳道图画一个 SAP 采购到付款（P2P）流程：
泳道分别是 采购员、采购经理、仓库、财务；
步骤：创建采购申请 → 审批（金额>10万需经理审批）→ 转采购订单 → 收货过账 → 发票校验 → 付款；
审批不通过则退回申请。
```
注意插件命名空间是 `/drawio:drawio`（前面是插件名，后面是 skill 名）。实际上大多数时候你直接说"画个流程图"它就会自动触发，不用敲命令。

---

## 2. 配套必读：官方 XML 参考（泳道 / 跨职能图的规范在这里）

- 原文：https://github.com/jgraph/drawio-mcp/blob/main/shared/xml-reference.md
- raw 版（可直接喂给 Agent 或粘进 CLAUDE.md）：https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md

严格说这不是一个独立"资源"，而是上面那个插件运行时会去抓的提示词地基。**但我建议你单独看一眼，因为它里面明确写了两类对顾问最有用的图怎么生成：**

- **Swimlanes for grouped actors（BPMN-style flowcharts）**：给了固定参数（泳道高度 150、`startSize=110`、子节点 `y=45`、跨泳道连线必须 `parent="1"`），并明确要求"不要嵌套 pool、不要自算标题区偏移"。这段直接决定了 AI 画出来的泳道图是不是能看。
- **Cross-functional flowcharts（角色 × 阶段网格）**：用 `shape=table;childLayout=tableLayout` 做二维矩阵——行是角色、列是阶段。**这个比普通泳道更贴合 SAP 蓝图文档里的跨职能流程图**，是这份文档里最有价值的一段。
- 另外还有边路由的选择指南（`routing: "libavoid"` 保布局只重排连线 vs `postLayout: "elk"` 整体重排），以及"什么时候该/不该用 search_shapes"——其中明确写了 **BPMN 且需要特定任务类型图标时才去搜形状库**，普通流程图别搜，省时间也少出错。

实操建议：把 raw 链接的内容抓下来存成项目里的 `docs/drawio-xml-reference.md`，在 `CLAUDE.md` 里指过去。这样 Agent 每次画图都能读到，比让它现场去 GitHub 抓稳。

---

## 3. 备选：github/awesome-copilot 的 draw-io-diagram-generator

- Skill 页：https://claudeskills.info/skills/github/awesome-copilot/draw-io-diagram-generator
- SKILL.md 原文：https://raw.githubusercontent.com/github/awesome-copilot/main/skills/draw-io-diagram-generator/SKILL.md
- 安装：`npx skills add github/awesome-copilot --skill draw-io-diagram-generator --agent claude-code`

**和官方方案的区别（这是我把它列为备选而非首选的原因）**

- 它**带 5 个现成模板**（flowchart / architecture / sequence / ER / UML class）和**两个 Python 脚本**：`validate-drawio.py`（校验 XML 结构）和 `add-shape.py`（不改原始 XML 往已有图里加形状）。
- SKILL.md 里有完整的**排错表**（图在 VS Code 打开空白 = 缺 id=0/1；边不显示 = source/target id 对不上；显示 "Compressed" = base64 编码了要解压）和**交付前检查清单**。
- 它的 BPMN 支持是"用形状库"一句话带过，没有官方那份泳道/跨职能的具体规范，所以**画业务流程图不如官方方案**。
- 它假设你在 VS Code 里用 `hediet.vscode-drawio` 扩展。

**什么时候选它**：你已经装了 VS Code 的 drawio 扩展、希望有校验脚本兜底、画的图偏向系统架构/ER/时序而非业务泳道图时。如果你主要是画 SAP 业务流程，**直接用第 1 个**。

---

## 4. 中文实操教程（唯一一篇我确认过质量的）

**《说一句话，流程图就画好了——手把手教你用 AI 画 draw.io，效率提升 10 倍》**
- 链接：https://mdnice.com/writing/d58e907042c64da694f226ad93752030
- 发布时间：2026-04-29

**为什么推荐它**：这篇不是"AI 工具推荐清单"那种水文，而是把 `drawio-mcp` 的**五种接入方式全部实测写清楚了**——Claude.ai 网页版加远程 MCP、Claude Desktop 配 `npx @drawio/mcp`、Claude Code 装 skill、Claude 项目指令零安装、opencode 集成——每种都给了配置文件原文和命令。还给了可直接抄的 Prompt 模板：

```
帮我画一个[图表类型]，包含以下内容：
[列出关键节点/角色/步骤]
[如有需要，说明分支条件]
[如需特定图标，注明技术栈，如 AWS、Kubernetes]
```

**一个提醒**：文章写于 2026-04-29，而官方在 2026-06-26 把 Claude Code 的 skill 重构成了插件（`/plugin marketplace add` + `/plugin install`）。所以文章里"手动 `cp SKILL.md` 到 `~/.claude/skills/drawio`"那段安装法**已经过时**，命令也变成了 `/drawio:drawio`。看它的**思路和 Prompt 模板**，安装按第 1 条走。

---

## 给你的一条落地路径

1. 装 draw.io Desktop（导出图片和 Mermaid 自动排版都要它）。
2. Claude Code 里 `/plugin marketplace add jgraph/drawio-mcp` → `/plugin install drawio@drawio`。
3. 把 `shared/xml-reference.md` 抓到项目 `docs/` 下，`CLAUDE.md` 里指过去。
4. 画 P2P / O2C 这类跨部门流程时，**在提示词里明确说"用跨职能流程图（角色 × 阶段）"或"用泳道图，泳道是 X、Y、Z"**，并写出审批分支条件。这一步是成败关键——你不说，AI 默认画出来的就是一串方框。

---

## 运行记录

### 实际使用的搜索关键词

1. `Claude Code skill generate draw.io diagram xml`
2. `draw.io mermaid AI 生成 流程图 skill Claude`
3. `SAP Oracle 实施顾问 业务流程 流程图 AI 生成 drawio 中文 教程`
4. `drawio-mcp skill BPMN 业务流程 泳道图 生成 顾问`

### 实际打开过的原始链接（WebFetch 正文级抓取）

| 链接 | 用途 | 结果 |
|---|---|---|
| https://github.com/jgraph/drawio-mcp/blob/main/plugins/claude-code/README.md | 核实 Claude Code 插件安装命令、输出格式、依赖 | 成功，拿到完整 README |
| https://github.com/jgraph/drawio-mcp | 核实仓库归属、Star 量级、更新活跃度、四种集成方式 | 成功（页面较长，取到 README 全文与近期 commit 记录） |
| https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md | 核实是否覆盖泳道/BPMN/跨职能流程图规范 | 成功，拿到全文，确认含 "Swimlanes for grouped actors (BPMN-style flowcharts)" 与 "Cross-functional flowcharts" 两节 |
| https://raw.githubusercontent.com/github/awesome-copilot/main/skills/draw-io-diagram-generator/SKILL.md | 核实 skill 是否真实存在、模板与脚本内容 | 成功，拿到 SKILL.md 正文（含模板清单、校验脚本、排错表） |
| https://mdnice.com/writing/d58e907042c64da694f226ad93752030 | 核实中文教程的发布信息与实际内容 | 成功，拿到全文，确认发布于 2026-04-29 |
| https://ima.qq.com/wiki/?shareId=...（"Vibe Coding 精选实战宝典"） | 想核实一篇中文 drawio 实战文 | **失败**——该链接是 ima 知识库的导航/目录页，未返回正文内容，因此**未将这篇列入推荐** |

### 其他出现在搜索结果中、但未被采纳的链接

- `https://claudeskills.info/...`、`https://www.getclaudeskills.com/...`、`https://www.skillavatars.com/...`、`https://tomevault.io/...`、`https://gittrend.io/...`：这些是 Skill 聚合/镜像站，内容是对原仓库 README 的二次转述。**仅用于交叉验证**（例如从 gittrend 侧确认 drawio-mcp 已达 5.3k stars、从 tomevault 侧确认 skill 描述），不作为推荐资源本身给出。
- `https://www.aijiaohuan.net/gjtji/51415518.html`、`https://www.aijiaohuan.net/gjtji/51414638.html`（"6个AI生成流程图的网站推荐"等）：内容里关于 draw.io 的"AI 智能布局""每月 9.9 美元专业版"等描述与 draw.io 官方实际情况不符，疑似 AI 生成的内容农场文章，**已排除**。
- `https://blog.csdn.net/lyjluandy/article/details/154578904`（Claude Code + Mermaid）：只讲了"生成 Mermaid 再粘到 draw.io"的手工流程，产出不是可编辑 `.drawio`，与本次需求不符，**已排除**。

### 遇到的异常或失败

1. **ima.qq.com 那条链接抓不到正文**（返回的是知识库目录页）。放弃该候选，未凭搜索摘要下结论。
2. **github/awesome-copilot 的 skill 路径存在差异**：聚合站描述写的是 `.claude/skills/`，但 SKILL.md 正文里脚本路径是 `.github/skills/draw-io-diagram-generator/scripts/`。我在文中按 SKILL.md 原文标注路径，安装命令采用聚合站给的 `npx skills add github/awesome-copilot --skill draw-io-diagram-generator --agent claude-code`（未实际执行验证）。
3. **中文高质量的"ERP 专用"画图 Skill 没搜到**。三次中文向搜索（关键词 3、4 及首轮）均未返回面向 SAP/Oracle 业务流程的、可验证的专用 Skill 或中文实操资源。搜索结果里中文内容大多是把官方 README 翻译一遍的水文，或把 draw.io 本身说成"内置 AI 流程图"的失实文章。所以最终推荐以官方英文一手资料 + 一篇实测过的中文教程构成，没有为了"中文优先"而硬凑质量不达标的资源。
4. **某个搜索结果把仓库镜像到了 `github.krithiv.dev/miguelangelorocha/drawio-mcp`**，内容与官方一致但为镜像站，未采用。
5. **时间差风险**：中文教程（2026-04-29）早于官方插件化重构（2026-06-26），其安装步骤已过时。我已在推荐条目 4 中显式标注这一差异。
