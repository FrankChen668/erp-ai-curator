# ERP AI Curator — Controlled User Trial Guide V1

Date: 2026-08-31
Status: **CONTROLLED TRIAL ENTRYPOINT**
Runtime: `0.9.2`

## 1. 这是什么

ERP AI Curator 帮泛 ERP / ToB / 企业信息化从业者做两件不同的事：

- **找实践**：别人现在有哪些值得学的 AI 实战、教程、工作流或案例？
- **做能力选择**：当前 AI/Agent 已经够不够？是否真的值得再加 Tool / Skill / MCP / 新工作流？

0.9.x 由两个单职责 Runtime Skill 承担这两件事，避免“找最佳实践”自动变成“推荐安装 Skill”。

## 2. Runtime Skills

```text
skills/
├── curating-erp-ai-resources/
│   ├── SKILL.md
│   └── references/
│       └── practitioner-discovery.md
└── advising-erp-ai-capabilities/
    ├── SKILL.md
    └── references/
        └── evidence-and-safety.md
```

两者整体导入。0.9.2 仍处于受控试用阶段，不声明所有 Agent Skills 宿主都已验证兼容。

## 3. 谁适合用

适合 SAP / Oracle / ERP 实施顾问、项目经理、产品经理、解决方案、开发、测试、数据和运维人员，尤其是已经在使用 ChatGPT、Codex、WorkBuddy、Claude Code、Qoder 等工具的人。

## 4. 用户怎么问

直接说真实问题即可，不需要模板。

### 找实践 → Practice Curator

- “给我找下产品经理/ToB 场景下，用 AI 提升流程图工作的最佳实践和高质量教程。”
- “我要维护几十份 ERP 操作手册，有没有别人已经跑通的 AI 做法？”
- “有没有实施顾问用 AI 做需求分析的真实案例？”

这类请求应该优先得到 practitioner 实操资源，不应该自动收到 Tool/Skill 安装建议。

### 做能力选择 → Capability Advisor

- “我现在 ChatGPT + draw.io 已经够了吗，要不要装专门 Skill？”
- “Oracle EBS 二开值得接什么 Agent/Tool 吗？”
- “SAP 程序报错，我已经有 dump 和代码，是否值得接 MCP/Joule？”
- “这两个 MCP 哪个更适合我们的环境？”

这类请求应该先判断具体能力缺口；没有缺口时，合法答案就是“现有工具已够”。

### 两者都有

- “先帮我找流程图最佳实践，再看看有没有必要装新的 Skill。”

两种职责可以同时执行，不需要第三个 Router Skill。

## 5. 找实践时应该得到什么

优先得到：

1. 1–3 个真正值得看的实操资源；
2. 作者/平台/可点击链接；
3. 为什么匹配你的角色、职业生态、任务和交付物；
4. 为什么它比其它 serious candidates 更值得先看；
5. 如果只能看一个，先看哪个；
6. 当 AI 工作流/工具变化较快时，资源日期、版本或当前适用性的关键边界；
7. 作者自实践、营销、语言/生态差异、权限或 coverage gap 等重要边界。

### 0.9.2 的 fresh curation 边界

正常用户请求应该基于**本次外部搜索和本次实际打开的资源**成立：

- 不能因为项目仓库昨天已经有一个 P04/历史验证结果，就直接沿用旧 Top 3；
- 历史项目文档中的作者名、URL、关键词可以作为搜索线索，但最终资源要在本次重新打开核验；
- AI/Agent/Skill/Tool 工作流变化较快时，要主动看近期候选；**最新不等于最好**，但不能默认忽略 freshness；
- 中文 practitioner 任务如果 serious candidates 只来自一个中文 practitioner pool，或者其余候选主要是官方/厂商/GitHub/英文来源，应对最可能改变排序的 1–2 个额外 practitioner pool 做定向补搜；这不是平台配额；
- 某个平台零召回/读不到不代表平台没有优质内容，必要时应明确 `coverage/policy gap`；
- 普通用户回答不应把项目内部 validation 文档当外部实践依据展示，除非用户明确问项目内部证据。

如果用户语言、地区或职业生态明确，同等质量下优先匹配该生态的 practitioner；海外资源可以推荐，但需要有明显增量价值或本地存在真实 coverage gap。

如果目标交付物有明确格式，例如 editable draw.io、PPTX、Word、BPMN、Visio、Markdown 或代码，推荐资源必须真正匹配该 artifact。邻近任务不能仅因 SAP/ERP/tool 标签更强就挤进 Top 推荐。

官方文档通常用于核验当前能力/格式/兼容性，不需要为了凑满 3 个资源与 practitioner 实践并列。

## 6. 做能力选择时应该得到什么

应该直接知道：

- **现有工具已够**；或
- **值得补能力**：具体缺口是什么、最小值得补什么；或
- **条件式升级**：哪个真实条件出现后再升级。

不应该因为某个 Tool/Skill installs、Stars、功能更多或刚好出现在搜索结果里就推荐采用。

只有用户明确要求安装/配置时，才提供安装命令或执行安装。

## 7. Web / 平台覆盖

完整的实践 curation 通常需要可用 Web/search/fetch。

中文 ERP / ToB / 产品/项目语境会优先关注 Bilibili、公众号、小红书、知乎/人人都是产品经理/掘金/CSDN/独立博客，以及相关 GitHub 实践，但没有固定平台配额。

如果宽搜没有出现这些最可能的 practitioner 池，或者候选过度集中在单一中文平台，也不能直接等价为“其它平台没有好内容”；应按任务相关性选择性补做 targeted discovery。

如果只能发现标题/摘要而读不到正文或字幕，应明确 `coverage/policy gap`。只有已有批准的 read-only source adapter 能实质补足证据时才按需使用。

## 8. 企业安全边界

- 不上传组织不允许外发的客户数据、源码、凭据、日志或截图；
- 诊断/理解默认 read-only；
- Tool/MCP 能写入不代表当前任务需要写权限；
- AI 输出是待复核建议，不是 ERP 系统事实；
- 版本、权限、隐私、兼容、价格等会改变能力选型的事实需要当前来源核验。

## 9. 试用不是测试协议

真实用户正常使用即可，不需要跑固定题目、对比多个模型或填写复杂评分。

自然反馈最有价值，例如：推荐资源是不是你真正想看的、是不是当前仍适用、是否少搜了很多东西、是否推荐了多余工具、是否漏掉真实环境/权限/版本约束、下次是否还愿意继续用。

## 10. 当前发布边界

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

尚未证明 Curator 比普通 AI / 自己搜索稳定更好，也没有证明固定节省多少时间或适合企业统一强制使用。
