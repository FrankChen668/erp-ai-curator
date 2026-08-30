# Curation Case 001 — ERP 操作手册批量制作与版本维护

Date: 2026-08-30
Status: **REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE**
Produced with Skill: `curating-erp-ai-resources` `0.6.3`

> 来源是 2026-08 训前调研中的真实同事问题。本文是 Curator 对真实来源问题形成的推荐，不代表该同事已经看到、采用或验证了推荐。

## 1. 真实问题

角色：实施顾问。

- 多部门需要分别制作 ERP 操作手册；
- 通常几十份，每份约 50–80 页；
- 当前人工截屏、粘贴、画箭头/方框/编号、写步骤；
- UI 改动后，需要反复替换截图并同步修改文字；
- 希望最终仍能得到可编辑 Word / Markdown。

## 2. Curator 结论

> **B — 值得优先采用“capture-assisted task documentation（操作捕获辅助的任务型文档）”模式；但不要把自动截图工具当成完整 ERP 操作手册生成器。**

当前最值得借鉴的做法是：

1. 按任务/角色拆小文档，而不是维护超长单体手册；
2. 用流程捕获工具承担点击、截图、基础标注等机械劳动；
3. 业务目的、角色权限、前置条件、异常和注意事项仍由顾问/AI基于真实项目材料补充；
4. 截图只用于确实需要视觉定位的步骤，不机械地每一步一张图；
5. 尽量分离易变化 UI 层与相对稳定的业务说明，降低维护成本；
6. 云端/本地选择首先服从客户截图和数据边界。

这是 `curator synthesis`，不是某个来源声明的行业标准。

## 3. 最值得看的 practitioner 经验

主资源：Technical Writing 社区关于 Tango / Scribe 的实际使用讨论：

https://www.reddit.com/r/technicalwriting/comments/1bjvacf/which_is_better_tango_or_scribe/

决策价值：

- 有使用者认为 capture 工具明显减少步骤捕获和更新清理；
- 也有团队认为对正式 client-facing 文档增益有限；
- 技术写作者提醒这类工具更适合简单 task-based 文档，不应替代完整 technical writing；
- screenshot-per-step 会放大 UI 变化后的维护量。

因此真正值得吸收的不是“全自动生成整本手册”，而是**让自动捕获只承担机械 UI 层工作**。

## 4. 原始能力核验

### Guidde — 云端/企业批准环境候选

当前官方资料显示 Desktop App 支持 Windows/macOS 桌面流程捕获、step-by-step 文档、编辑以及 Word/Markdown/PDF/PPTX 等导出。

- https://help.guidde.com/en/articles/9760354-desktop-application
- https://help.guidde.com/en/articles/7003131-export-guiddes-and-playlists

适用含义：可减少截图、步骤绑定和基础文档生成的机械劳动；官方能力不能证明它理解客户 ERP 业务规则、角色权限和例外。

### Folge — local-first 边界候选

当前官方资料显示支持 Windows/macOS 本地点击捕获、截图、编辑、标注/模糊，并导出 Word、Markdown、PDF、PPT 等；官方描述为本机处理。

- https://folge.me/

适用含义：如果 ERP 截图不能离开项目环境，本地 capture/annotation/export 能力比云端 AI 自动写作更关键。

## 5. 优先推荐实践

```text
真实 ERP 任务/角色
→ 按任务拆分
→ capture tool 处理点击 / 截图 / 基础标注
→ 稳定文本承载业务目的、前置条件、角色、异常和注意事项
→ 只在需要视觉定位处保留截图
→ 输出到 Word / Markdown / 知识库等可维护载体
→ UI 变化时优先更新受影响模块
```

普通多模态 AI 适合组织章节、润色步骤和解释截图，但不会天然解决连续截图、点击绑定、大量标注、UI 维护和企业数据边界。

## 6. 采用边界

更值得引入专门 capture/documentation 能力：

- 手册数量和截图量大；
- 主要时间耗在捕获、标注、排版和维护；
- 需要可继续编辑的输出；
- 同类任务会反复发生。

可能不值得：

- 只是偶尔几页说明；
- 正式交付的难点主要是复杂业务解释而非截图劳动；
- 安装/审批/云端权限成本高于节省的机械劳动。

## 7. 给用户的最小 Curator 输出

> **不要把目标设成“AI 自动写完整 ERP 手册”。更成熟的做法是把手册拆成任务型模块，让 capture 工具接管截图/点击/基础标注，让 AI 和顾问负责业务上下文与文字；截图只用于真正需要视觉定位的地方。云端允许时可看 Guidde 这类方案，截图不能外发时优先看 Folge 这类 local-first 方案。**

## 8. Evidence boundary

已完成：真实问题重构、practitioner 正反经验筛选、原始能力核验和 Curator synthesis。

尚未证明：真实同事采用、节省时间、降低返工或优于普通 AI/自搜索。这些只能来自后续 `REAL_USER_USE` 反馈。