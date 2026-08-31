# ERP AI Curator — Current Session Handoff

Date: 2026-08-31
Status: **CURRENT / CONTROLLED REAL-USER USE + SOURCE-COMPOSITION QUESTION OPEN**

> 新会话先读 `docs/PROJECT_MAP.md`。不要从历史聊天、旧 validation、P04 或已关闭 Pilot 恢复当前推荐；历史 evidence 只能用于理解项目演化或提供 search lead。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

当前如涉及 source composition，再读：

- `docs/validation/REUSE_BEFORE_BUILD_SOURCE_COMPOSITION_20260831.md`
- `docs/validation/SOURCE_COMPOSITION_UNCERTAINTY_20260831.md`

真实用户试用读：

- `docs/USER_TRIAL_GUIDE_V1.md`
- `docs/REAL_USER_PILOT_V1.md`

## 2. 当前产品

ERP AI Curator 是**一个产品、两个 Runtime 职责**，面向真实 ERP / ToB / 企业信息化工作问题。

核心用户结果：

> **找实践时替用户筛出当前值得学的 practitioner workflow；做能力选型时判断现有工具是否够、是否存在值得采用成本的能力缺口。**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库、社媒爬虫平台或工具实验室。

## 3. Current Runtime — 0.9.1 FROZEN

### Practice Curator

`skills/curating-erp-ai-resources/`

- fresh external discovery；
- historical project evidence = lead only；
- final external resources 本次重新打开；
- fast-changing AI workflow 考虑 currentness/freshness；
- broad search 漏掉明显 practitioner 生态时做 selective targeted recall；
- 不主动做 Tool/Skill/MCP adoption。

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- current baseline；
- concrete capability gap；
- minimum useful upgrade or explicit no-upgrade。

两 Skill metadata.version 都是 `0.9.1`。

**当前不要修改 Runtime。** Draft PR #74 只是行为保持型规则清理候选，在冻结解除前不合并。

## 4. 上一阶段已证明什么

P0–P4 source-acquisition investigation 已关闭。

已支持：

- broad Web 对中文 practitioner 生态存在真实 recall/acquisition 缺口；
- targeted normal Web 是最低成本 fallback，但不是完整解法；
- WeChat provider 一次正向、一次 metadata-only，当前 `PILOT / UNSTABLE`；
- Bilibili provider `CONDITIONAL`；
- `xpzouying/xiaohongshu-mcp` provider 因权限面、工具链、浏览器运行时和维护成本被 `REMOVED`；
- provider qualification 与平台内容价值必须分开。

这批证据不验证产品价值，也不证明应该长期维护一套平台 Adapter 架构。

## 5. 当前架构方向

工作原则：

> **REUSE BEFORE BUILD**

优先顺序：

```text
Curator
→ normal Web / GitHub
→ 当中文 source recall 物质性不足时，优先复用成熟外部 research Skill
→ 严肃候选需要动态/login-state 原文时，再用成熟 browser-access fallback
→ Curator 独立判断证据
```

不要恢复 one-provider-per-platform 工程，也不要建设 adapter registry/framework。

## 6. 当前未决问题

P5 mature-Skill composition 只得到部分证据：

- discovery 层增加了 Bilibili candidates；
- 原文读取 fallback 因 Chrome CDP 未启用而没有实际执行；
- 因此 `discovery → original reading → Curator judgement` 没有端到端完成。

当前结论：

> **MATURE-SKILL COMPOSITION EFFECTIVENESS — INCONCLUSIVE / OPEN**

不能从 P5 推导“已解决”，也不能推导“已失败/应放弃 Source Acquisition”。

进一步证据只在真实 ERP/ToB 任务中、且能改变候选/排序/置信度/coverage 判断时才收集；不要再为填矩阵跑 synthetic platform test。

## 7. 当前真正里程碑

> **REAL_USER_USE product value validation**

尚未证明：Curator 比普通 AI / 用户自搜索更省判断成本、更少错选、更当前、更可信，并且这个差异足以让真实用户继续使用。

当前发布边界：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

## 8. Adversarial boundary

不要重新引入：

- platform quota；
- newest-wins；
- crawler/resource DB/auto-refresh；
- creator ranking；
- third Router Skill；
- per-platform adapter engineering；
- custom adapter framework before mature composition is disproven；
- auto-install/update inside ordinary user requests；
- publish/comment/like/favorite/follow/message 等社媒写动作；
- 用 Lane A / synthetic evidence 冒充 REAL_USER_USE。

## 9. Next actor

### Cloud

- 继续真实任务的 Curator / Capability Advisor 使用与证据审查；
- 收到自然 REAL_USER_USE 反馈时更新 evidence authority；
- 仅在真实任务出现 decision-changing source gap 时，审查 mature-Skill composition 的端到端证据；
- 维护 GitHub 当前 authority 一致性。

### Local Agent

只在下一份 decision-changing evidence 需要本地 runtime、Chrome/CDP、企业环境、受保护源或本地仓库能力时接力。不要为了“有 Agent 可用”制造任务。

### Owner

只处理 Agent 无法替代的真实产品/业务裁决、登录/credential/restart、本地账户动作，以及未来 repository license 等 Owner 决策。
