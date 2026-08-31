# Curation Case 005 — 客户 Workshop / 会议材料 → 可评审需求包

Date: 2026-08-31  
Status: **REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE**  
Runtime: `0.9.1`  
Source: 2026-08 训前调研中重复出现的实施顾问 / 项目经理真实问题语义（P01）

> 这是一份准备直接发给真实同事使用的 Lane A 结果。它证明的是“Curator 已形成可用推荐”，不证明用户已经采用、节省时间、减少返工或优于普通 AI / 自搜索。

## 1. 真实问题

典型情境：

- 刚完成客户访谈、需求调研或 Workshop；
- 手头有会议录音 / 转写、纪要、现状流程、RFP / 需求 Excel 和附件；
- 第二天需要形成第一版可评审需求包；
- 不能接受 AI 自己补业务事实或把讨论意见写成已确认需求。

期望交付：

- 结构化需求清单；
- 待确认问题；
- 冲突 / 遗漏；
- 当前痛点与约束；
- 初步 Fit/Gap 或蓝图输入；
- 能回到原始会议 / 材料的来源追溯。

## 2. Curator 结论

> **当前最值得先学的不是“一键会议纪要”或“一键 PRD”，而是 source-grounded requirement synthesis：让 AI 承担提取、结构化、交叉检查和格式劳动，同时强制保留未知项、冲突和来源追溯；业务判断、优先级和冲突裁决仍由顾问完成。**

对 ERP / ToB 项目，最小可复用链路应是：

```text
原始会议 / 项目材料
→ 原子事实与需求提取
→ 标注来源 / 发言人 / 位置
→ 需求 + 待确认 + 冲突 + 遗漏分离
→ 顾问复核业务含义
→ 组装为需求包 / BRD / FS 初稿
→ 逐条回查来源后再进入评审
```

这是 Curator synthesis，不是某一来源声明的行业标准。

## 3. 最值得先看的 3 个资源

### 1）IIBA 2026 practitioner case — **先看这个**

**How AI Enhances Business Analysis Without Replacing Professional Judgment**  
IIBA / Stacie A. Benson（Senior Business Analyst）

https://www.iiba.org/business-analysis-blogs/how-ai-enhances-business-analysis-without-replacing-professional-judgment/

为什么排第一：

- 是 2026 年真实 BA 项目案例，不是工具功能介绍；
- 实际处理 30 位 stakeholder、9 个 division、12 场 focus group；
- 用 AI 处理 transcript thematic analysis，再由 BA 反复重组、核验；
- 最终 Word 交付保留 supporting examples 和对原始讨论的 traceability；
- 作者明确记录了一个真实失败模式：AI 会过度放大早期 transcript 中偶发观点，因此必须检查跨场次一致性。

对 ERP 顾问最有价值的不是 Copilot 本身，而是这个工作方式：**先确定分析方法，再让 AI 加速材料综合；输出必须回到 stakeholder evidence，AI 不能替顾问做业务结论。**

边界：英文、BA 语境，不是 SAP / Oracle 专属；但工作单元与 ERP Workshop 高度同构。

### 2）2026 BA Playbook — **最容易今晚直接照着跑**

**How Business Analysts Use AI for Requirements Gathering and User Stories**  
FreeAcademy.ai，2026-06-06

https://freeacademy.ai/blog/ai-for-requirements-gathering-business-analysts

为什么值得看：

- 直接从 workshop notes / raw transcript → structured requirements；
- 要求区分 functional / non-functional、stakeholder、已明确 priority；
- 单列 ambiguity / contradiction，并明确“不要发明不存在的需求”；
- 后续继续覆盖 user story、acceptance criteria、BRD/FRD 和 requirements traceability matrix；
- 把“没有 linked user story 的 requirement”作为 coverage gap 暴露出来。

它比通用“帮我总结会议”更接近实施顾问真正需要的交付物。

边界：这是 practical playbook，不是独立的 ERP 项目效果验证；其中 prompt 应按项目模板和数据边界调整。

### 3）中文 WorkBuddy 需求评审纪要模板 — **适合本地快速起步，但不要照单全收**

**把会议笔记、录音扔给AI，3分钟按需出会议纪要（WorkBuddy 提示词资产包 · 职场通用版）**  
知乎 / 微盛AI·企微管家，更新于 2026-07-02

https://zhuanlan.zhihu.com/p/2056016461232084982

值得借鉴的部分：

- 对需求评审单独拆出：需求确认清单、变更记录、待确认事项、风险、下一步；
- 明确要求不确定项标 `[待确认]`，不要脑补；
- 变更前 / 变更后 / 变更原因 / 影响范围这一结构很适合项目追溯；
- 待确认事项增加“不确认会怎样”，有助于把 open issue 转成真正可推进的问题。

但不要照单全收：

- 来源是机构号模板资产，不是独立使用验证；
- 文中“只有纸质笔记几个关键词也可让 AI 推断完整框架”的建议与 ERP 需求取证边界冲突，**不应采用**；
- 对真实项目，只能从已有材料提取和标未知，不能让模型补出“完整需求”。

## 4. 推荐的实际工作方式

不要把全部材料一次丢进去让 AI “写完整需求文档”。优先拆成三步：

### Step A — 只做事实 / 需求提取

输入会议转写、纪要、流程文档或需求表。

要求 AI：

- 每条输出独立 ID；
- 区分已确认事实、需求、意见、假设；
- 标明来源文件 / 发言人 / 段落或时间位置；
- 没说的不补；
- 模糊、矛盾和缺口单列。

### Step B — 做交叉检查，而不是继续扩写

把多个来源放在一起检查：

- 同一需求是否表述冲突；
- 是否存在遗漏角色、异常、权限、数据范围、接口或前置条件；
- 哪些点只有单一来源，尚未形成共识；
- 哪些需求没有对应来源或验收条件。

### Step C — 最后才组装交付文档

在顾问确认后，再组装成项目需要的：

- 需求清单；
- Open Questions；
- Fit/Gap 输入；
- BRD / FS / 蓝图初稿；
- Traceability table。

这样做的核心价值是：**先保持证据，再生成文档；不要让“文档看起来完整”反过来掩盖事实缺口。**

## 5. 给真实用户的最小 Curator 输出

> 你这个场景最值得先学的不是“一键把录音变 PRD”，而是“有来源追溯的需求综合”。建议先看 IIBA 2026 的真实 BA 案例，理解 transcript → 分析 → 人工复核 → traceable deliverable 的完整链路；然后直接照 FreeAcademy 的 workshop notes → structured requirements → ambiguity/conflict → traceability 工作流跑你的材料。如果你使用 WorkBuddy，知乎那套需求评审纪要模板可以拿来做中文输出骨架，但只吸收“确认/变更/待确认/风险/下一步”的结构，不能让 AI 根据零散关键词补完整业务事实。先让 AI 提取和标未知，再由你确认，最后才组装 FS/需求包。

## 6. 企业数据边界

- 客户录音、未公开蓝图、账号、合同、生产数据等是否允许进入云端 AI，服从组织和项目政策；
- 不允许外发时，先使用获批企业环境 / 本地环境，或者做必要脱敏；
- “AI 能读”不等于“数据允许上传”；
- 来源追溯不能暴露不应传播的敏感原文。

## 7. Freshness / coverage boundary

本次为 2026-08-31 fresh discovery + fresh inspection。

已实际检查：

- IIBA 2026 practitioner case；
- FreeAcademy 2026 BA playbook；
- 知乎 2026 WorkBuddy 会议模板；
- 同时检查了近期中文 B 端产品 / PRD / 会议纪要候选，但多数更偏工具推广、通用 PRD 或单纯语音转写，没有超过前三项对 `Workshop → traceable requirement package` 的直接任务匹配。

未证明：这是所有中文平台上的绝对 Top 3；当前推荐成立于本次可访问证据范围。

## 8. Evidence boundary

这是 **Lane A — REAL_USER_ORIGIN CURATION**。

尚未证明：

- 真实同事是否实际采用；
- 是否比普通 AI / 自己搜索更省时间；
- 是否减少需求遗漏或返工；
- 是否愿意带第二个真实问题回来。

下一条能改变产品判断的证据只能来自真实用户自然使用后的反馈，不应再用 synthetic test 或内部评分替代。
