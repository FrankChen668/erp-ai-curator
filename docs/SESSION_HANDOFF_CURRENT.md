# ERP AI Curator — Current Session Handoff

Date: 2026-08-30
Status: **CURRENT / CONTROLLED REAL-USER USE**

> 新会话先读 `docs/PROJECT_MAP.md`，不要从历史聊天恢复当前状态。

## 1. 当前产品

ERP AI Curator 是**真实 ERP / ToB / 企业信息化工作问题的 AI 实践与现成资源 Curator**。

核心目标：

> **替用户找到最值得学习/采用的现成 AI 实践与资源，并判断是否真的需要新增能力。**

## 2. Current Skill — 0.8.1

- `skills/curating-erp-ai-resources/SKILL.md`
- release class: **CONTROLLED USER TRIAL**
- user-use value: **UNVALIDATED**

Runtime 仍保持简化主链：

```text
理解真实任务
→ 判断用户要找实践、做采用选择，或两者都有
→ practitioner-first discovery
→ 核验 serious candidates
→ 选择少量高匹配资源/做法并停止
```

0.8.1 只增加两个由真实日志直接证明必要的执行要求：

1. **Query intent preservation**：如果原问题是“用 AI/Agent/Tool 改善某工作”，practitioner discovery 至少保留一条 `AI/tool × role/industry/artifact` query，不能退化成纯领域最佳实践搜索；
2. **Candidate investigation**：明确找实践/教程时，必须实际打开至少一个 practitioner/creator 候选；如果宿主 policy/coverage/access 阻止，则明确 `coverage/policy gap`，不能用官网补位后声称完成。

Runtime references 仍只有：

- `references/practitioner-discovery.md`
- `references/evidence-and-safety.md`

## 3. Triggering evidence

Codex Desktop 本地执行日志显示：

- 运行前半段先用了旧 `0.6.1` 并发生一次拟议 `0.6.2` 修改，随后才同步到 `0.8.0`，因此整次运行不是干净的 0.8.0 独立测试；
- 但同步后 `SKILL.md 0.8.0`、`practitioner-discovery.md` 和 `evidence-and-safety.md` 确实被读取；
- 第二批 query 仍丢掉 AI / 产品经理 / ToB / ERP 语境；
- Bilibili、公众号、小红书、知乎、人人都是产品经理、掘金/CSDN 未实际定向搜索；
- 已出现的中文 practitioner 候选基本未打开；
- 最终来源仍由 official/standard/implementation 主导。

Authority：`docs/validation/CURATOR_081_PRACTITIONER_EXECUTION_PATCH.md`。

## 4. Host risks — do not push into Skill without more evidence

- Codex Web policy 可能存在 technical→primary-source-only 冲突；
- Graph Engineering 被错误触发，属于宿主 Skill collision；
- Browser/Chrome 可用但未调用，是否需要 fallback 仍未知。

这些不是 0.8.1 runtime 规则。

## 5. Current release

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

产品价值仍未验证。

## 6. Next

0.8.1 合并后，下一条高价值 evidence：在**全新 Codex Desktop 上下文**同步最新 `main` 后，用同一句自然问题重跑，不修改 Skill、不复用旧搜索上下文，并返回实际 query/reference/打开候选/最终来源角色。

若仍失败，再区分：Skill execution、host source policy、search coverage、Skill collision 或 source acquisition；不要继续靠最终答案猜根因。
