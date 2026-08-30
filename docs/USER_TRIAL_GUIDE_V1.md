# ERP AI Curator — Controlled User Trial Guide V1

Date: 2026-08-30
Status: **CONTROLLED TRIAL ENTRYPOINT**
Skill: `curating-erp-ai-resources` `0.8.2`

## 1. 这是什么

ERP AI Curator 帮泛 ERP / ToB / 企业信息化从业者做两件事：

- **找实践**：别人已经有哪些值得学的 AI 实战、教程、工作流或现成资源？
- **做选择**：当前 AI/Agent 已经够不够？是否真的值得再加 Tool / Skill / MCP / 新工作流？

它不是工具大全，也不是用几个官网链接重新写一篇通用教程。

## 2. 谁适合用

适合 SAP / Oracle / ERP 实施顾问、项目经理、产品经理、解决方案、开发、测试、数据和运维人员，尤其是已经在使用 ChatGPT、Codex、WorkBuddy、Claude Code、Qoder 等工具的人。

## 3. 安装/导入

Skill 包：

```text
curating-erp-ai-resources/
├── SKILL.md
└── references/
    ├── practitioner-discovery.md
    └── evidence-and-safety.md
```

整体导入，不要只复制 `SKILL.md` 丢掉 references。

0.8.2 仍处于受控试用阶段，不声明所有 Agent Skills 宿主都已验证兼容。

## 4. 用户怎么问

不需要模板，直接说真实问题即可，例如：

- “给我找下产品经理/ToB 场景下，用 AI 提升流程图工作的最佳实践和高质量教程。”
- “我要维护几十份 ERP 操作手册，有没有别人已经跑通的 AI 做法？”
- “Oracle EBS 二开现在用什么 AI 工作方式更合理？”
- “我们每周合并很多顾问周报，有没有必要再装专门工具？”
- “SAP 程序报错，我已经有 dump 和代码，是否值得接 MCP/Joule？”

如果会改变建议，可以自然补充：当前工具、真实材料、最终交付物、数据/源码边界、系统权限、版本和任务频率。

## 5. 用户应该得到什么

如果问**最佳实践/教程**，优先得到：

1. 1–3 个真正值得看的实操资源；
2. 作者/平台/可点击链接；
3. 为什么匹配你的角色、职业生态、任务和交付物；
4. 如果只能看一个，先看哪个；
5. 作者自实践、营销、版本、语言/生态差异、权限或 coverage gap 等重要边界。

如果你的语言、地区或职业生态很明确，同等质量下应该优先匹配该生态的 practitioner；海外资源不是不能推荐，但需要有明显增量价值，或本地存在真实 coverage gap。

如果目标交付物有明确格式，例如 editable draw.io、PPTX、Word、BPMN、Visio、Markdown 或代码，推荐内容/Tool/Skill 必须真正支持该 artifact，不能用相邻格式偷换。

“找最佳实践/教程”本身不代表你需要安装新 Tool/Skill。只有确实存在具体能力缺口时才应该提出新增能力。

如果原问题明确是“**用 AI/Agent/Tool 改善某项工作**”，最终资源搜索不应退化成纯领域知识搜索。

如果宿主的搜索策略、平台访问或权限阻止读取 practitioner 内容，应明确 `coverage/policy gap`，而不是用官网替代后声称已经完成最佳实践 curation。

## 6. Web / 平台覆盖

完整的实践 curation 通常需要可用 Web/search/fetch。

中文 ERP / ToB / 产品/项目语境会优先关注 Bilibili、公众号、小红书、知乎/人人都是产品经理/掘金/CSDN/独立博客，以及相关 GitHub 项目，但没有固定平台配额。

如果只能发现标题/摘要而读不到正文或字幕，应明确 `coverage/policy gap`。只有已有批准的 read-only source adapter 能实质补足证据时才按需使用，不为了覆盖率自动安装第三方组件。

## 7. 企业安全边界

- 不上传组织不允许外发的客户数据、源码、凭据、日志或截图；
- 诊断/理解默认 read-only；
- Tool/MCP 能写入不代表当前任务需要写权限；
- AI 输出是待复核建议，不是 ERP 系统事实；
- 版本、权限、隐私、兼容、价格等会改变选择的事实需要当前来源核验。

## 8. 试用不是测试协议

真实用户正常使用即可，不需要跑固定题目、对比多个模型或填写复杂评分。

自然反馈最有价值，例如：推荐资源是不是你真正想看的、是否少搜了很多东西或少选错工具、是否推荐了多余工具、是否漏掉真实环境/权限/版本约束、下次是否还愿意继续用。

## 9. 当前发布边界

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

尚未证明 Curator 比普通 AI / 自己搜索稳定更好，也没有证明固定节省多少时间或适合企业统一强制使用。
