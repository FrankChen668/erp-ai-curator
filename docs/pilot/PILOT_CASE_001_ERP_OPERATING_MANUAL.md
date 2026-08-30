# Pilot Case 001 — ERP 操作手册批量制作与版本维护

Date: 2026-08-30
Status: **RECOMMENDATION READY — AWAITING REAL COLLEAGUE ACTION**
Skill: `curating-erp-ai-resources` `0.6.2`

> 这是来自 2026-08 训前调研的真实同事工作问题。当前只形成了行动前推荐；在同事实际尝试、修改或拒绝之前，不属于 REAL_USER adoption evidence。

## 1. 真实任务

角色：实施顾问。

详细问题聚焦操作手册：

- 多部门需要分别制作 ERP 操作手册；
- 通常几十份，每份约 50–80 页；
- 当前人工截屏、粘贴、画箭头/方框/编号、写步骤；
- 系统 UI 改动后，需要反复替换截图并同步修改文字；
- 主要痛点是截图/文字版本漂移、大量重复劳动、不同部门版本碎片化。

期望：形成可编辑 Word / Markdown 操作手册初稿，包含截图、标注、步骤说明、角色化结构，并在 UI 变化后尽量局部更新而不是整本重做。

## 2. Curator 0.6.2 判断

> **条件化 B — 已存在明确专业能力缺口，值得试用专门的流程捕获/文档生成能力；具体主方案由截图数据是否允许进入云端决定。**

这次不再停留在“普通 AI 先试试看”，原因是已经观察到普通 AI 无法单独解决的能力缺口：

1. **桌面 ERP 实际操作捕获**：需要跟随真实点击生成步骤和截图，而不是事后逐张整理；
2. **截图与步骤绑定**：需要自动建立“第 N 步 ↔ 对应界面”的关系；
3. **可编辑交付**：最终要进入 Word / Markdown，而不是只生成视频或分享链接；
4. **变更维护**：核心价值不只是第一次生成，而是 UI 变化后能局部替换/更新；
5. **企业数据边界**：截图可能包含客户/业务信息，决定能否采用云端方案。

上述能力缺口已经足以跨过“是否值得评估专业能力”的门槛，因此 `Specialized resource: none` 不再自洽。

## 3. 当前最小推荐

### Branch A — 项目允许将脱敏/测试环境截图上传到批准的云端服务

**主候选：Guidde Desktop（Business / Enterprise 路线）**

为什么进入主候选：

- 官方文档显示 Windows/macOS Desktop App 可直接捕获桌面工作流；
- 捕获后会生成 step-by-step 文档，可编辑文字、图片和布局；
- 支持导出 Word、Markdown、PDF、PPTX 等；
- 可替换单个步骤图片而保留其他内容；
- Enterprise 提供版本历史能力。

Decision-changing official evidence:

- Desktop capture: https://help.guidde.com/en/articles/9760354-desktop-application
- Word / Markdown export: https://help.guidde.com/en/articles/7003131-export-guiddes-and-playlists
- Document editor / image replacement: https://help.guidde.com/en/articles/9997243-the-document-editor
- Version history: https://help.guidde.com/en/articles/10696558-version-history-control

边界：这些是厂商能力说明，不等于已经证明适合当前 ERP 项目；必须通过一个真实短流程试用确认截图、文字、标注、导出和更新返工是否真的下降。

### Branch B — 客户/项目截图不能进入云端，或尚未批准

**替代候选：Folge（local-first）**

为什么是不同边界的备选：

- 官方说明它在 Windows/macOS 本地捕获鼠标点击并生成截图步骤；
- 支持标注、重排；
- 支持 Word、Markdown、PDF、PPT 等导出；
- 官方明确宣称全部在本机处理、无需强制云端。

Evidence:

- https://folge.me/
- https://folge.me/help/guide/

边界：Folge 更偏“本地捕获/标注/导出”，并不能从当前公开证据证明它会像 AI 工具一样自动生成高质量 ERP 业务步骤文字。若需要文字生成，应在组织批准的本地/企业 AI 中处理导出的步骤和截图。

## 4. 为什么没有继续列 Scribe / Tango / 更多工具

当前目标不是做工具大全。

现有公开信息已经足以形成一个可执行采用决策：

- 云端可用 → 先试能覆盖“桌面捕获 + 文档生成 + Word/Markdown + 局部更新”的 Guidde；
- 云端不可用 → 先试 local-first Folge，再配合批准的本地/企业 AI。

继续扩充候选不会改变本轮下一步，只会增加比较成本。

## 5. Practitioner 反证 / 限制

公开 technical-writing 社区讨论对这类 capture-based 工具有两个反复出现的提醒：

- 对简单、任务型 step-by-step 文档确实有价值；
- 真正困难往往不是“第一次生成”，而是产品/UI 持续变化后的维护、复核和重做。

这正是为什么本 Pilot 不以“生成了一份漂亮手册”为成功，而必须故意测试一次 UI 变化后的局部维护。

References:

- https://www.reddit.com/r/technicalwriting/comments/1bjvacf/which_is_better_tango_or_scribe/
- https://www.reddit.com/r/software/comments/1vkg1d9/looking_for_a_scribe_alternative_that_is_easy_to/

这些是 practitioner/community evidence，不是产品能力权威事实。

## 6. 给真实同事的最小试用动作

不要拿整套几十份手册开始。

只选 **1 个真实、可脱敏/测试环境执行、5–10 页规模的典型流程**，最好包含 8–15 个操作步骤。

执行：

```text
真实 ERP 流程
→ 用批准的 Branch A 或 Branch B 工具完整走一遍并捕获
→ 导出 Word 或 Markdown
→ 顾问修正步骤文字、截图标注、角色/权限说明
→ 人为制造/选择一个已有 UI 变化（1–2 个步骤）
→ 只更新受影响步骤
→ 记录实际返工
```

### 必须观察的不是“好不好看”，而是：

1. 是否减少了手工截图、裁图、画标注、编号；
2. 自动生成的步骤文字有多少需要重写；
3. Word / Markdown 是否真的可继续编辑和交付；
4. UI 变化后能否只改受影响步骤；
5. 是否出现权限、截图敏感数据、云端上传等阻塞；
6. 同事下次是否愿意继续用这个方法。

不要求打分；短文本事实即可。

## 7. 同事试完后只需返回

```text
实际用了：Guidde / Folge / 其他 / 没有试
是否按推荐执行：照做 / 修改 / 拒绝
得到的产物：
最省事的地方：
最费事或错误的地方：
UI 改动后更新是否更轻：
是否有隐私/权限/环境问题：
下次是否还会用：会 / 不会 / 看情况，因为……
```

如同事直接拒绝，也要记录具体原因；例如截图不能上传、安装受限、导出格式不满足、维护反而更麻烦。具体拒绝同样是有效 Pilot evidence。

## 8. Stop / next actor

Cloud 已完成：任务重构、0.6.2 采用判断、当前资源核验、最小试用设计。

**下一执行者：真实同事。**

在同事实际执行或明确拒绝之前，不再做内部 benchmark，不扩充工具清单，不调用 Local Agent 模拟用户行为。

结果返回后，Cloud 立即继续：

- 判断推荐是否真正有增量；
- 检查 0.6.2 是否仍 over/under-tooling；
- 必要时做最窄 Harness/Skill 修正；
- 否则进入下一条真实任务。
