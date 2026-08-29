# Current Evidence Status

Date: 2026-08-29

> Current product model is `AI_LEVERAGE_MODEL_V3.md`. Current execution authority is `CURRENT_EXECUTION_PLAN_V3.md`. Historical resource-first evidence must not be silently treated as V3 validation.

## 1. What is currently supported by evidence

### A. The real product problem exists

泛 ERP / 企业信息化从业者确实存在两类相邻问题：

1. 当前工作到底应该怎样用 AI；
2. 当需要外部能力时，哪些 Skill / Tool / 方法 / 教程真正值得采用。

OWNER_REAL 问题已经覆盖 editable diagram、interactive prototype、model routing、Fit-to-Standard / requirements、陌生模块学习、Agent architecture 等真实工作。

### B. Resource-first was too narrow

旧 Phase 2/3 把产品收窄成：

`真实任务 → 搜索互联网 → 0–2 推荐`

V3 已改成：

`真实任务 → AI leverage diagnosis → Mode A/B/C → 必要时定向发现`

当前 baseline 是用户已有 AI + Agent + 工具链，而不是裸模型。

### C. Heavy governance is a demonstrated failure mode

V0.2–V0.4 已证明：Gate、评分、candidate JSON、validator 可以结构正确但产品判断错误。

V3 不恢复这些机制。

### D. Resource curation itself remains a core capability

当用户明确需要寻找外部方案时，Curator 必须能从高噪声互联网中找出少量真正值得使用/学习/分享的资源。

T01/T02 已提供以下证据：

- 官方资料适合承担事实锚点，但不应该自动占据主推荐位；
- GitHub / practitioner / community 内容可以提供更强的实操价值；
- `Practical Companion` 必须真的增加操作步骤、案例、Prompt、失败经验或采用判断，而不是为了结构完整凑一个社区链接；
- `内容适配度高` 与 `项目成熟度高` 是不同判断。

### E. T01 exposed discovery recall risk

T01 第一次搜索偏向成熟 SaaS/官方结果，补测后才发现更贴近本地 Agent / 可运行 HTML 原型的方法。

因此当前已知风险是：

> Selection 可以合理，但 Discovery Recall 仍可能受搜索入口和来源可访问性影响。

这只是观察，不建立固定平台搜索配额。

### F. T02 showed better task-fit reasoning, but maturity uncertainty remains

T02 已经能围绕：

`调研材料 → 未决事项 → Fit/Gap → 决策 → 需求 → 方案 → 测试追溯`

来选择资源，而不是只搜索“AI 写 BRD”。

但主候选的维护度、真实项目采用度仍弱，因此当前正确定位是：

> strong-fit candidate / worth piloting, not proven enterprise standard.

### G. Chinese practitioner coverage is a real acquisition uncertainty

T01/T02 的本地 Codex 路径对 Bilibili / Xiaohongshu / WeChat practitioner content 的发现和正文读取覆盖较弱。

当前不能得出“中国高质量内容很少”的简单结论，因为至少混合了：

- acquisition/access gap；
- discovery/index bias；
- true domain scarcity / quality mismatch。

因此当前正在验证条件式来源 Adapter，而不是建立中国内容爬虫数据库。

## 2. Current source-adapter hypothesis

当前假设：

> Curator 负责判断；普通 Web/GitHub 先行；只有当具体来源能力缺口会影响推荐时，Codex 才调用已安装、已审查、只读的来源 Skill/MCP。

当前 Pilot 候选：

- WeChat discovery: `zjp1997720/wechat-article-search`
- WeChat reader: `Githun1314/agent-wechat-reader`
- Bilibili: `XZXZZX-Ai/bilibili-mcp`
- Xiaohongshu: `xpzouying/xiaohongshu-mcp`

云端已完成候选研究和部分静态安全审查，但以下内容**仍未被证明**：

- Windows 本地实际安装是否稳定；
- read-only 边界是否实际可控；
- 登录/凭证流程是否可接受；
- Codex 是否能可靠组合 Curator + 多个 Skill/MCP；
- Adapter 是否会实际提升最终推荐质量，而不只是增加链接数量。

## 3. REAL_USER evidence

**仍不足。**

当前已经有问卷设计和 Survey Bridge，但没有实际独立用户答卷数据进入项目。

因此：

- 不伪造角色需求；
- 不用 OWNER_REAL 自测冒充独立 REAL_USER 验证；
- Source Adapter pilot 主要验证运行可行性与采编增量，不证明最终市场/组织价值。

## 4. Role scope

目标用户是泛 ERP / 企业信息化从业者，包括：

- 实施 / 业务顾问；
- 项目经理；
- 产品经理 / 解决方案人员；
- 开发人员；
- SAP / Oracle 标准实施、二开和集成；
- Java / .NET 等定制供应链、财务、采购、制造和其他企业系统。

角色用于理解上下文，不建立配额。

## 5. Asset evidence level

| Asset | Evidence type | Current status |
|---|---|---|
| Phase 1 — representative Skill study | design research | keep |
| Phase 2/3 resource-first design | historical hypothesis | superseded for current decisions |
| V0.2–V0.4 | failure evidence | archive only |
| Starter Pack V0 | discovery memory | search prior only |
| OR01–OR06 original problems | OWNER_REAL input | keep |
| V3 owner/boundary replay | design falsification | useful, not independent validation |
| T01 prototype curation | OWNER_REAL curation behaviour | useful; exposed recall issue |
| T02 requirements/Fit-Gap curation | OWNER_REAL curation behaviour | useful; exposed fit-vs-maturity issue |
| Source coverage finding | acquisition evidence | active hypothesis |
| Source Adapter architecture/lifecycle | design hypothesis | awaiting local qualification |
| Independent REAL_USER results | primary validation | insufficient |

## 6. What remains unproven

- V3 is consistently better for independent real users;
- V3 should ultimately be packaged as a Skill;
- native Codex multi-Skill/MCP orchestration is reliable enough;
- WeChat/Xiaohongshu/Bilibili adapters materially improve final curation;
- all current adapter candidates are safe/stable enough to keep;
- an adapter registry needs software rather than a small reference file;
- resource caching/database/automatic refresh is needed;
- scenario taxonomy is needed.

## 7. Current mainline

**Status: V3 product validation + source-adapter qualification pilot. Not production Skill implementation.**

Immediate sequence:

1. local qualification of pinned source adapters;
2. read-only smoke tests;
3. explicit multi-Skill/MCP routing test;
4. fresh curation A/B uplift test;
5. repeat only if uplift is material;
6. then decide whether to package a minimal Curator Skill.

See `docs/CURRENT_EXECUTION_PLAN_V3.md` for ownership and stop conditions.

## 8. Current main risks

### Over-tooling

把所有问题回答成“再装一个 Tool/Skill”。

### Adapter sprawl

因为一个平台访问失败就永久增加一个 Adapter。

### Runtime/install mixing

让 Curator 在正常采编任务中自动发现、安装或更新第三方 Skill。

### Platform checklist drift

因为已经安装微信/小红书/B站 Adapter，就每个主题全部搜索一遍。

### Resource gravity

因为已有候选或 Starter Pack，就优先往旧答案靠。

### Official-document gravity

因为官网容易核验，就忽略真正能降低同事上手成本的实战资源。

### Self-validation

把本地 Agent 的 PASS、测试数量或 OWNER_REAL replay 当成独立用户证明。

### Rebuilding governance

因为一次失败就增加新的 Gate、评分、数据库或自动化。

出现以上趋势时，应回到 `AI_LEVERAGE_MODEL_V3.md` 与 `CURRENT_EXECUTION_PLAN_V3.md`。
