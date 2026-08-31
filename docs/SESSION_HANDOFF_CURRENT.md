# ERP AI Curator — Current Session Handoff

Date: 2026-08-31
Status: **CURRENT / CONTROLLED REAL-USER USE**

> 新会话不要从历史聊天或旧 validation 文档恢复当前用户推荐。先读 `docs/PROJECT_MAP.md`；历史 evidence 只能用于理解项目演化，不能直接替代当次 fresh curation。

## 1. 最小读取顺序

```text
docs/PROJECT_MAP.md
→ docs/PROJECT_NORTH_STAR.md
→ docs/OWNER_EXECUTION_RULES.md
→ docs/CURRENT_EXECUTION_PLAN_V3.md
→ docs/validation/EVIDENCE_STATUS.md
```

只有具体任务需要时再读 Runtime Skills、Trial Guide、Real User Use Validation 或历史材料。

## 2. 当前产品

ERP AI Curator 是**一个产品**，面向真实 ERP / ToB / 企业信息化工作问题。

核心用户结果：

> **真正需要找实践时，替用户筛出当前值得学的 practitioner workflow；真正需要做能力选型时，判断当前工具是否够用、是否存在值得采用成本的能力缺口。**

默认不是：工具目录、执行 SOP、用户测试协议、资源数据库或工具实验室。

## 3. Current Runtime — 0.9.1

### Practice Curator

`skills/curating-erp-ai-resources/`

- best practices / tutorials / real workflows / cases / practitioner resources；
- 正常外部策展先做当前 fresh discovery；
- 项目 validation/history/prior packs 只能作为 lead，不能决定当前排名；
- 最终外部资源本次重新打开；
- AI 工作流快速变化时检查当前/近期候选；
- 宽搜明显漏掉用户 practitioner 生态时做有选择的 targeted recall；
- 不主动做 Tool/Skill/MCP adoption；
- reference：`practitioner-discovery.md`。

### Capability Advisor

`skills/advising-erp-ai-capabilities/`

- current toolchain enough?；
- add/install/choose/compare Tool/Skill/MCP/plugin/Agent/workflow?；
- concrete capability gap → minimum useful upgrade or explicit no-upgrade；
- reference：`evidence-and-safety.md`。

两个 Skill metadata.version 都是 `0.9.1`。

Authorities：

- `docs/validation/CURATOR_090_RUNTIME_RESPONSIBILITY_SPLIT.md`
- `docs/validation/CURATOR_091_FRESH_CURATION_EVIDENCE_ISOLATION.md`

## 4. Why 0.9.1

0.9.0 已初步修复 practice-only 请求被 Tool/Skill 选型吸走的问题，但随后本地日志证明新的“较好答案”仍被历史 P04 validation 强烈影响：

- 只有一批 4 个 broad Web query；
- 没有定向搜索 Bilibili/公众号/小红书/知乎；
- 最终两篇人人都是产品经理资源由本地 `rg` 从历史 P04 文件找到，再直接打开；
- `Castaldo-Solutions/process-builder` 也来自历史 P04，而且本次没有重新打开；
- 最终用户回答展示了内部 P04 validation 链接；
- 本次没有真实 Web 访问失败来解释这些缺口。

因此当前根因是：**historical-evidence contamination + freshness gap + broad-search recall bias**。

Cloud 定向 sanity search 同日立即发现新的 2026-07 Bilibili drawio-skill 更新内容、2026-06 供应链/WMS 产品经理 CodeX→Draw.io 实践等候选。它们未必一定排进 Top 3，但足以证明 serious candidate pool 不是历史 P04 可以静态封闭的。

## 5. Adversarial boundary

不要把 0.9.1 扩成：

- newest-wins；
- B站/公众号/小红书/知乎固定平台配额；
- resource DB / auto refresh；
- 第三个 Router Skill；
- A/B/C runtime taxonomy；
- scoring/Gate/creator ranking；
- Browser/Graph Engineering/host-policy workaround as Curator rules。

Best ≠ newest；但旧资源不能因为“以前入选过”就自动继续获胜。

## 6. Historical evidence

Curation Pack / P04 等历史研究保持有效的项目研究价值。

新边界：

> **历史项目结论不能作为普通用户当前 external curation 的独立外部证据或默认排序。**

可复用：作者名、关键词、URL lead、已知风险提示。  
不可直接复用：当前 Top 3 排序、当前性结论、未重新打开的外部资源、面向用户的内部 validation 链接。

## 7. Current release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

试用入口：`docs/USER_TRIAL_GUIDE_V1.md`。

产品价值仍未验证。

## 8. Next

0.9.1 合并后继续自然 controlled use。

最重要的 practice-only 观察仍是：

> `给我找下做流程图的最佳实践`

期望：

- 当前 external discovery 先发生；
- 宽搜漏掉明显中文 practitioner 生态时有 targeted recall；
- final resources 全部本次打开；
- freshness/current applicability 被考虑；
- 不向普通用户展示内部 validation 文件。

失败时先取 search/open/source 日志，不继续根据答案表面加规则。

## 9. Cloud / Local / Owner

Cloud 能做就继续直接做，包括真实反馈证据审查、Web/GitHub discovery、窄缺陷修正和 authority/Harness 维护。

Local Agent 只在本地 repo/runtime/ERP 环境/受保护 evidence 或具体宿主 trigger/load/search 行为验证真正需要时接力。

Owner 当前唯一潜在明确裁决项仍是 repository license（仅当要声明 public/open-source release complete 时）。
