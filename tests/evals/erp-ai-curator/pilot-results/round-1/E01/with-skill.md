# 给 SAP/Oracle 实施顾问：用 Agent 生成可编辑 draw.io 业务流程图的资源

先说判断：你要的不是"AI 给一张流程图"，而是**落一个 `.drawio` 源文件、之后能自己接着改**。这两条路差别很大，很多"AI 画图"工具止步于 PNG/SVG，改一个节点就得整张重来。下面两个资源都是围绕前者的，且互补：第一个负责"生成—自动布局—导出"的主链路，第二个补它缺的业务流程图/泳道写法规范。

| 资源 | 类型 | 为什么值得看 | 能得到什么 | 重要限制 |
|---|---|---|---|---|
| [draw.io 官方 Claude Code Skill（仓库 `jgraph/drawio-mcp`）](https://github.com/jgraph/drawio-mcp) | Skill（官方，draw.io/jgraph 自己维护） | 目前唯一由 draw.io 官方维护、直接产出**原生 `.drawio` 文件**的 Agent 技能，不是截图也不是 Mermaid 死图；SKILL.md 明确要求"图内标签语言跟随用户语言"，中文流程名、泳道名可直接生成，省掉导出后逐个改中文的返工 | 在 Claude Code 里一句 `/drawio 采购到付款流程，泳道：采购部/仓库/财务/应付`，本地得到可反复编辑的 `.drawio`；装了 draw.io 桌面版还能用 `--layout verticalFlow / horizontalFlow` 让 ELK 自动排版，导出 `.drawio.png/.svg/.pdf` 时 XML 内嵌，文件拖回 draw.io 仍可完整编辑 | ① **安装方式已改版**：网上大量中文教程里的 `mkdir -p ~/.claude/skills/drawio` + 复制 SKILL.md 已过时（2026-06 仓库把 `skill-cli/` 重构成插件）；当前官方写法是 `/plugin marketplace add jgraph/drawio-mcp` → `/plugin install drawio@drawio`，或从本地克隆 `claude --plugin-dir ./plugins/claude-code`。② 只有 **Mermaid 转换、ELK 布局、PNG/SVG/PDF 导出**这三件事需要 draw.io 桌面版；不装桌面版就走 XML 直出或 `url` 模式，照样拿到可编辑文件。③ 官方 README 能力表写 "XML only"，而当前 SKILL.md 正文写"有 CLI 时优先 Mermaid"，两处表述不一致，以 SKILL.md 为准、实际用前先确认。④ SKILL.md 只覆盖通用 draw.io 知识，**没有 BPMN / 跨职能泳道的专门规范** |
| [`draw-io-diagram-generator`（github/awesome-copilot）](https://github.com/github/awesome-copilot/tree/main/skills/draw-io-diagram-generator) | Skill（社区贡献，GitHub 组织仓库收录） | 它把"业务流程图"这类图的写法写死了，正好补上官方 skill 的空白：泳道容器样式串 `swimlane;startSize=30;...`、语义配色（开始/流程/判断/异常/结束各有固定 fillColor+strokeColor）、间距规则（同行 40–60px、层间 80–120px、默认画布 A4 横向 1169×827）、BPMN 走形状库，还附 9 项交付前 checklist | 可直接抄的 mxGraph XML 骨架与泳道/判定/连接的样式串，外加 `scripts/validate-drawio.py` 校验脚本——生成完跑一遍，自查 id 是否唯一、边的 source/target 是否存在、XML 是否合法，避免发给客户的 `.drawio` 打开是空白 | ① 该仓库官方 README **只**写了 `copilot plugin install` / `gh skills install`，**没有** `npx skills add ... --agent claude-code`；后者是各技能目录站写的，我没能在官方 README 里确认。稳妥做法：把 `skills/draw-io-diagram-generator/` 整个文件夹复制到你的 Agent 技能目录（SKILL.md + references + assets/templates + scripts 是自包含的）。② 纯 XML 手写坐标路线，无 Mermaid、无 ELK 自动布局，复杂图要自己算位置。③ 仓库 README 明确提示内容来自第三方贡献者，装前先看一遍 SKILL.md。④ SKILL.md 正文里脚本路径写的是 `.github/skills/...`，仓库实际目录是 `skills/...`，用时按实际目录改 |

## 为什么没有推荐更多

- **中文侧没找到同等质量的原创实操。** 搜到的基本是公众号转载站和"AI 画图工具推荐"类内容农场（其中一篇还写着"draw.io AI 个人版月费约 20 美元"这类无法核实的价格说法，不予采信）。唯一够格的中文原创（腾讯云开发者社区一篇 WorkBuddy+CodeBuddy 集成实战）讲的是第三方 skill，且其对比表称官方 jgraph skill"仅支持 Claude 系列""一次生成不可迭代"——这与官方仓库当前状态（已同时发布 Codex CLI、GitHub Copilot CLI 插件，且支持 ELK 布局与多轮修改）直接冲突，按"第三方与官方冲突时不推荐第三方"不列入。
- **ERP 原生路径是另一条路。** SAP Signavio 的 AI-assisted process modeler 确实能从文字/表格/图片生成 BPMN，但它既不走 Claude Code、产物也不是 `.drawio`，不在你这次的问题范围内，故不占推荐位。
- **还有一个够格但需自行迁移的**：日文技术媒体 DevelopersIO 的实机试用手记（英文）记录了官方 skill 出图后的真实缺陷与修法——连线压图标要用 `edge_layer`/`shape_layer` 双层结构、标签压图标用 `verticalLabelPosition=bottom`、边界缺失要用 group 容器。对"出图质量不满意"很有用，但它以 AWS 架构图为例，需要自己迁移到业务流程图，所以没占推荐位。链接：https://dev.classmethod.jp/en/articles/claude-code-trying-out-drawio-skill-for-aws-architecture/

## 建议的用法

两个一起装：官方 skill 当主链路（生成 + 自动布局 + 导出），第二个当"写法规范 + 交付前校验"。另外官方 skill 的 SKILL.md 是纯 Markdown，可以照 DevelopersIO 那篇的做法，把你们项目的绘图规范（配色、泳道命名、审批节点样式）追加成章节，出图一致性会明显提升。

---

## 运行记录

### 任务理解（Skill 流程第 1 步）

- 谁要用：SAP/Oracle 实施顾问（可能不是重度开发者，但已在用 Claude Code 一类的 Agent）
- 要完成什么动作：用 Agent 从文字描述生成 draw.io 业务流程图
- 最终希望得到什么可用结果：**可编辑的 `.drawio` 源文件**（不是静态图片、不是 Mermaid 代码、不是展示用图）

这个判断决定了后面所有取舍：凡是只产出 PNG/SVG 静态图、或产出 BPMN 供 Cloud ALM 导入的资源，都被判为输出物不符。

### 实际使用的搜索关键词（共 5 组）

1. `Claude Code skill generate drawio diagram editable .drawio file`（英文，按工具环境 + 产出物）
2. `Claude Code Agent 生成 draw.io 流程图 skill 可编辑`（中文，同上角度的中文侧覆盖）
3. `SAP 实施顾问 业务流程 AI 生成 drawio BPMN 泳道图 中文 实操`（按人群 + 产出物 + 中文）
4. `Claude Code drawio skill 实战 安装 踩坑 业务流程 泳道图 原创`（按动作"实战/踩坑" + 中文原创）
5. `claude agent skill drawio BPMN swimlane business process diagram generate`（英文，补 BPMN / 泳道角度）

按 `references/source-strategy.md` 要求变化了动作、工具环境、产出物、人群四个维度，中英文各覆盖。

### 实际打开过的原始链接（WebFetch，均为原始出处）

| 链接 | 读到了什么 | 结论 |
|---|---|---|
| https://github.com/jgraph/drawio-mcp | 4 种集成方式对比表、Claude Code 插件安装命令、插件化重构时间线、导出/CLI 依赖说明 | **推荐位 1**，全部关键事实出自此页 |
| https://raw.githubusercontent.com/jgraph/drawio-mcp/main/plugins/claude-code/skills/drawio/SKILL.md | SKILL.md 全文（275 行）：Mermaid/XML 取舍表、pipeline、ELK 布局预设、导出命令、CLI 定位、Windows/WSL2 坑、XML 规范、故障排查表 | **推荐位 1 的一手依据**，逐条核对了写法 |
| https://raw.githubusercontent.com/github/awesome-copilot/main/skills/draw-io-diagram-generator/SKILL.md | SKILL.md 全文（357 行）：触发条件、图表类型表（含 BPMN Workflow / 泳道）、最小 XML 骨架、语义配色表、泳道容器样式串、布局间距、模板与脚本清单、9 项校验清单 | **推荐位 2**，一手内容 |
| https://github.com/github/awesome-copilot | 仓库归属与治理、README 里 skill 的实际安装方式、活跃度（2026-08-28 仍有合并，PR 已到 #2844） | 用于核验 #2 的**安装事实**，结果否定了第三方镜像的命令 |
| https://github.com/github/awesome-copilot/tree/main/skills/draw-io-diagram-generator | 目录页 | 只返回 GitHub 导航框架，**未拿到有效内容**，无损失（已用 raw 文件取到全文） |
| https://dev.classmethod.jp/en/articles/claude-code-trying-out-drawio-skill-for-aws-architecture/ | 真实实机测试：环境（macOS / Cursor / Claude Code Opus 4.6 / Draw.io Desktop）、4 个具体问题与解法、作者往 SKILL.md 追加的 AWS 规范全文、已知局限 | 判定为够格但需迁移，放入"为什么没有推荐更多" |
| https://github.com/jgtolentino/insightpulse-odoo/tree/main/.claude/skills/drawio-diagrams-enhanced | 目标路径是**符号链接**（64 Bytes 的 symlink），拿不到实体内容 | 无法确认上游实体，放弃该候选 |

### 读了哪些 references

- `references/source-strategy.md` — 在**开始联网搜索前**读（SKILL.md 规定"开始联网搜索时"读），用于设计多角度关键词、确定原始来源优先顺序与中文 tie-breaker 规则
- `references/selection-heuristics.md` — 在**已有多个候选开始横向取舍时**读，用于三问比较、判定重叠、处理"官方资料是 user resource 还是 evidence anchor"、判定厂商自述数字
- `references/volatile-fact-check.md` — 在**候选涉及安装配置与版本时**读（见下）

### 是否触发了高风险事实核验：是

触发条件命中 `volatile-fact-check.md` 的两项：**安装与配置**、**模型与版本兼容**。核验动作与结果：

1. **官方 skill 的安装命令**——第三方中文教程普遍写 `mkdir -p ~/.claude/skills/drawio` + 复制 SKILL.md。回官方仓库核对，发现 2026-06-26 提交（`refactor: restructure skill-cli as Claude Code plugin + marketplace`）已把 `skill-cli/` 迁到 `plugins/claude-code/`，当前安装方式是 `/plugin marketplace add` + `/plugin install drawio@drawio`。→ **第三方旧教程判定为已过时，不采用、不推荐**。
2. **Mermaid 还是 XML**——官方 README 能力表写 Assistant Plugins 是 "XML only (native format)"，但当前 `plugins/claude-code/skills/drawio/SKILL.md` 正文明确"有 CLI 时优先 Mermaid，Mermaid 覆盖不了才用 XML"。两份官方材料自相矛盾。→ 以 SKILL.md 为准（它是实际驱动 Agent 的文件），并在推荐里**如实标注该不一致**，未粉饰成确定结论。
3. **是否需要 draw.io 桌面版**——这是最容易踩的坑，核对 SKILL.md 后确认是**分功能**的：Mermaid 转换 / ELK 布局 / 图片导出需要桌面版 CLI；纯 XML 直出与 `url` 模式不需要。→ 推荐里按分功能写清，未笼统说"需要/不需要"。
4. **awesome-copilot 的 Claude Code 安装命令**——技能目录站（claudeskills.info 等）给的是 `npx skills add github/awesome-copilot --skill draw-io-diagram-generator --agent claude-code`。回官方 README 核对，**README 未出现 `npx skills add`，也未出现 `.claude/skills`**，只给了 `copilot plugin install` 与（站点实现层面的）`gh skills install`。→ 按"无法确认即不包装成当前可用"，在推荐里标注该命令未获官方确认，并给出稳妥替代（复制整个 skill 文件夹到 Agent 技能目录）。
5. **版本**——官方插件 marketplace 标识为 `drawio@drawio v1.1.0`（该版本号在 2026-07-16 的 Codex CLI 镜像提交中被验证）。因是在兄弟端口的提交里验证的、非 Claude Code 页面直接标注，**未写进推荐正文**，仅记录于此，避免过度声称。
6. **价格类说法**——某中文内容农场文章称"draw.io AI 个人版月费约 20 美元"。无官方来源佐证，按"厂商/第三方自述数字不得改写成事实"处理，直接不采信，并成为淘汰该批资源的理由之一。

### 淘汰但未推荐的候选（不向用户展示，仅供审计）

- 各公众号转载 / 聚合站 / 内容农场的"AI 画图工具推荐"清单（aijiaohuan.net 等，cloud.tencent.com 上对微信文章的转载）——按 `source-strategy.md`，转载站与内容农场只作线索、不作推荐对象
- `Agents365-ai/drawio-skill` 及其中文推广型实操文——与当前官方状态冲突（见"为什么没有推荐更多"），按 `volatile-fact-check.md` 第三方与官方冲突时不推荐
- `drawio-diagrams-enhanced`（BPMN/泳道/RACI/PMBOK，Odoo ERP 背景）——内容与任务高度相关，但在 nilecui/SkillsBase、jim60105/copilot-prompt、cndoit18-dotfiles 等多处镜像/fork，唯一可能的上游 `jgtolentino/insightpulse-odoo` 对应路径是符号链接、拿不到实体。按"识别 GitHub fork 与 upstream，不要把 fork 当原作者独立成果"，无法确认上游故放弃
- SAP Signavio AI-assisted process modeler、SAP Community《Generate Process Models with GenAI》——ERP 原生、质量高，但输出物是 BPMN（供 Cloud ALM / Signavio 导入），非 `.drawio`，也非 Agent 驱动，输出物与用户任务不符

### 遇到的异常或失败

1. `https://raw.githubusercontent.com/jgraph/drawio-mcp/main/drawio/SKILL.md` 返回 **404**。原因：仓库 2026-06 重构后路径改为 `plugins/claude-code/skills/drawio/SKILL.md`，换路径后取到全文。这次失败反而是发现"安装方式已过时"的关键线索。
2. `github/awesome-copilot/tree/main/skills/draw-io-diagram-generator` 的 WebFetch 只返回 GitHub 页面导航框架，无正文。改用 raw 文件链接后成功取到 357 行全文。
3. `jgtolentino/insightpulse-odoo` 的 skill 路径返回的是符号链接（1 行 / 64 Bytes），无实质内容，该候选无法验证。
4. 官方 `jgraph/drawio-mcp` README 与 SKILL.md 关于"是否支持 Mermaid"表述冲突（详见核验项 2）。已在推荐中如实标注，未自行统一口径。
5. `awesome-copilot` 的 SKILL.md 正文里脚本路径写 `.github/skills/draw-io-diagram-generator/scripts/...`，与仓库实际目录 `skills/...` 不一致。已在推荐的限制栏提示用户按实际目录改。

### 中文 tie-breaker 的处理

`source-strategy.md` 规定中文优先是**同等质量下的 tie-breaker，不是质量豁免**；若中文侧只有二手转载、营销稿或过时内容，果断转向英文。本轮中文侧实际搜到的全部为转载站、内容农场或厂商产品推广文，无一篇达到可推荐质量，因此两个推荐位均为英文资源，但用中文写清了"为什么值得看 / 重点看哪部分 / 使用限制是什么"。
