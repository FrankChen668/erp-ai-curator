# Eval Plan

## 1. Eval 的目标

不是验证 Skill 文件是否合法，而是回答：

> **加载 ERP AI Curator 后，同一个 Agent 是否更稳定地产出“值得直接分享给 ERP 同事”的资源推荐？**

## 2. A/B 方法

每个 Prompt 同时运行两组：

### Baseline

- 同一个 Agent；
- 同样的 Web / GitHub 能力；
- 不加载 ERP AI Curator；
- 只给用户原始 Prompt。

### With Skill

- 同一个 Agent；
- 同样的工具；
- 加载新 `erp-ai-curator` Skill；
- 使用完全相同 Prompt。

尽量在同一时间窗口运行，减少搜索结果时效差异。

如果运行环境支持独立 subagent / clean session，必须使用独立上下文，避免 baseline 被 Skill 内容污染。

## 3. 人工评价优先

每个运行结果由业务 Owner 盲评，尽量不显示是 baseline 还是 with-skill。

对每条最终推荐标记：

- 值得分享；
- 一般；
- 不值得分享。

同时判断整题：

- resolved；
- unresolved；
- 正确 abstain（0 推荐且确实应该留空）。

## 4. 10 个首轮真实任务

这些是 Eval，不是 Skill 规则样本；实现不能针对具体资源名写死。

### E01 — 可编辑业务流程图

> 我想给 SAP/Oracle 实施顾问找能用 Claude Code 或类似 Agent 生成可编辑 draw.io 业务流程图的 AI Skill/实操资源。少而精，中文有高质量的可以优先。

检查：

- 是否理解“可编辑业务流程图”而不是 BPM 引擎部署；
- 是否能发现真正 Skill / 可用方案；
- 是否输出少量强候选。

### E02 — 原型设计

> 我们顾问经常要快速做需求原型。帮我找现在值得用的 AI 原型 Skill、Tool 或实操教程，最好能直接产出可评审的交互原型。

检查：

- 默认允许不同资源类型竞争；
- 不把 Tool 冒充 Skill；
- 更关注实际可用输出。

### E03 — Claude Code 第三方模型配置

> Claude Code 接 OpenRouter 或其他第三方模型，现在有没有靠谱的配置方法？给我当前还有效的资源，不要旧教程。

检查：

- 必须触发强事实核验；
- 当前官方/原始配置优先；
- 旧变量/endpoint 冲突不得推荐。

### E04 — Codex 低成本模型

> Codex CLI 有没有比较靠谱的第三方模型或低成本模型接入方案？我希望是当前还能用的，不要只给泛泛介绍。

检查：

- 当前版本和兼容范围；
- 不把旧 Claude Code 方案泛化给 Codex；
- 能区分官方、第三方 wrapper、实践教程。

### E05 — SAP Fit-to-Standard

> 找一些 SAP 顾问用 AI 做需求调研、Fit-to-Standard 或 Fit-Gap 的实战方法、案例或工具。不要泛 AI use-case workshop。

检查：

- task fit；
- 不因 SAP 官方而推荐错题资源；
- vendor claim 只作为来源声称。

### E06 — Oracle 需求分析

> Oracle 实施项目需求调研、solution design 这块，有没有真正可借鉴的 AI 实战资源？最好是顾问能直接照着思路用的。

检查：

- 不拿 SAP 资源硬填 Oracle；
- 允许 0 推荐；
- 通用高质量方法若可迁移，可说明迁移边界。

### E07 — SAP 陌生模块学习

> 我临时要接触一个不熟的 SAP 模块，想找用 AI 快速理解业务流程、配置链路和关键对象的方法或 prompt framework。给真正有结构的方法，不要“问 Joule 就行”这种泛建议。

检查：

- 方法是否真正支持模块学习；
- 不把 Joule custom Skill 开发文档当学习方法；
- 不接受夸大的标准产品能力。

### E08 — Oracle 陌生模块学习

> Oracle Fusion SCM 我不熟，想找 AI 辅助快速学习模块的高质量方法、教程或 prompt framework。没有好的就明确说没有。

检查：

- 0 推荐能力；
- 不凑普通 prompt list；
- 英文优质资源可以优先于弱中文资源。

### E09 — 明确只要 Skill

> 只帮我找 Agent Skill：能够读取代码仓库并辅助生成架构图或系统关系图。不要普通桌面 Tool，也不要纯教程。

检查：

- 用户明确限定后，resource type 成为硬条件；
- 不把 Tool / MCP / repo 工具冒充 Skill。

### E10 — 稀缺主题 / Abstain

> 帮我找一个专门针对 Oracle EBS 老版本实施顾问、用 AI 自动做 Fit-Gap 的成熟开源 Skill。只要真正成熟、可以落地的；没有就不要推荐。

检查：

- 是否能正确保持空缺；
- 不因为题目要求就硬找一个近似项。

## 5. 定量辅助检查

这些只做行为检查，不评价资源“好不好”：

- 默认推荐数是否 ≤2；
- 是否有原始链接；
- 用户明确限定类型时是否违反；
- 高风险配置题是否有当前官方/原始核验依据；
- 是否出现明显不存在/无法打开的链接；
- 是否出现“最好/最强”等无证据表述；
- 是否把厂商自述数字写成独立事实。

不要给候选打统一 100 分制。

## 6. 关键指标

沿用 Phase 2：

- Shareability；
- Useful Resolution Rate；
- Task Fit；
- Correction Count；
- Trust failures；
- 结果冗余。

首轮目标：

- 推荐资源 `值得分享` ≥80%；
- 10 题中至少 7 题 resolved（包含业务 Owner 认可的正确 abstain）；
- Shareability 明显高于 baseline；
- Trust failure 不高于 baseline。

## 7. 迭代纪律

一次 Eval 失败后，不立即加规则。

先分类：

- 任务理解；
- 搜索覆盖；
- 选择错误；
- 类型混淆；
- 时效；
- 事实冲突；
- 过度推荐；
- 过度 abstain；
- 语言偏差；
- 流程成本。

**只有 2–3 个独立测试重复出现同类失败，才考虑把修复固化到 Skill。**

优先修最小位置：

1. SKILL.md 一句话提醒；
2. reference heuristic；
3. 最后才是 deterministic script。

## 8. 防过拟合

- 不允许在 Skill 中写 E01–E10 的具体资源答案；
- 不允许为某个历史错误新增专用字段；
- 第二轮 Eval 必须至少新增 5 个未见过的 ERP 任务；
- old V0.4 五题只能占部分回归，不得成为全部测试集。