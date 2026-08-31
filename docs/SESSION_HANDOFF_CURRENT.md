# ERP AI Curator — Current Session Handoff

Date: 2026-08-31
Status: **CURRENT / SOURCE ACQUISITION PILOT**

> 新会话先读 `docs/PROJECT_MAP.md`。不要从历史聊天、P04 或旧 validation 恢复当前推荐；历史 evidence 只能用于理解项目演化或提供 search lead。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

当前具体执行再读：

- `docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`
- `docs/local-agent/SOURCE_ACQUISITION_PILOT_TASK.md`
- `docs/SOURCE_ADAPTER_ARCHITECTURE_V3.md`
- `docs/SOURCE_ADAPTER_LIFECYCLE_V3.md`

## 2. 当前产品

ERP AI Curator 是**一个产品**，面向真实 ERP / ToB / 企业信息化工作问题。

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
- broad search 漏掉明显 practitioner 生态时做 targeted recall；
- 不主动做 Tool/Skill/MCP adoption。

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- current baseline；
- concrete capability gap；
- minimum useful upgrade or explicit no-upgrade。

两 Skill metadata.version 都是 `0.9.1`。

**Pilot 期间不要继续改 Runtime。**

## 4. 为什么当前重点上移到 Source Acquisition

Repeated real runs across more than one Agent host show the same remaining pattern:

- broad Web Search 可以返回官方文档、GitHub、CSDN、普通博客和少量 practitioner 内容；
- 小红书、公众号、Bilibili、知乎等中文 practitioner 池经常没有进入候选；
- 0.9.0 diagnostic 明确没有做这些平台的 targeted discovery；
- 另一 Agent 在 2026-08-31 的独立 broad-search 运行也出现类似缺失。

这意味着剩余问题不能继续只解释成“某个宿主没听 Skill”。

当前最强假设是：

> **ordinary broad Web discovery / indexing / original-content acquisition 对中文 practitioner 生态存在重复、物质性的覆盖缺口。**

这不证明每个平台都需要 Adapter，也不证明社媒内容天然更好。

## 5. Current Pilot

Authority：`docs/validation/SOURCE_ACQUISITION_PILOT_20260831.md`。

顺序：

```text
P0 targeted normal Web
→ P1 WeChat lightweight discovery
→ P2 Bilibili search/transcript
→ P3 Xiaohongshu isolated read-only
```

Zhihu normal-Web-first，暂不引入专用 Adapter。

### P0

先证明显式 `site:` / source-qualified targeted search 是否已经足够。

### P1

WeChat candidate：`zjp1997720/wechat-article-search`。低成本 discovery-only 优先验证。

### P2

Bilibili candidate：`XZXZZX-Ai/bilibili-mcp`。只用 search / metadata / transcript；凭据本地保存。

### P3

Xiaohongshu candidate：`xpzouying/xiaohongshu-mcp`。最高 acquisition value potential，也有最高 login/browser/write-surface 风险；仅在 P0–P2 不能稳定决策时进入，且只允许 read-only qualification。

## 6. Pilot 判断标准

Adapter 不是因为“能搜到内容”就合格。

必须证明：

1. normal Web 难以可靠获得的 practitioner evidence 被获取；
2. 能读到足以判断的原始内容/provenance；
3. materially 改变 candidate pool、ranking、rejection reason、confidence 或 coverage boundary；
4. 安全/凭据/维护成本合理。

否则保持 CONDITIONAL / REMOVED，不进入长期 Runtime。

## 7. Adversarial boundary

不要重新引入：

- platform quota；
- newest-wins；
- crawler/resource DB/auto-refresh；
- creator ranking；
- third Router Skill；
- custom adapter framework before simple composition fails；
- auto-install/update inside ordinary user requests；
- publish/comment/like/favorite/follow/message 等社媒写动作。

## 8. Current release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

另外允许：**staged local source-acquisition pilot**。

产品价值、全宿主兼容、长期 Adapter 架构均未验证。

## 9. Next actor

### Local Agent

执行：`docs/local-agent/SOURCE_ACQUISITION_PILOT_TASK.md`。

继续到真正需要 Owner 本地登录/QR/credential/client restart，或出现安全阻塞，或后续阶段已不再 decision-changing 时才停。

### Cloud

收到 P0/P1/P2/P3 结果或本地 branch/commit 后：

- 审查 source acquisition 是否真的改变推荐；
- 决定 adapter status：APPROVED / CONDITIONAL / PILOT / REMOVED；
- 只有证据证明需要时才修改 Runtime routing 或 permanent architecture。

### Owner

只处理无法由 Agent 完成的本地登录/QR/credential/restart 动作，以及未来 repository license 这种真正 Owner 决策。
