# ERP AI Curator

面向 **SAP / Oracle / ERP / 企业信息化从业者** 的 AI 工作方式 Curator。

> **面对一个真实工作任务，普通 AI / 当前工具链是否已经够用？如果不够，互联网上已经存在的实操经验、Tool / Skill / MCP / 方法 / 教程中，什么最值得优先学习和采用？**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 想直接试用

当前版本：**0.7.0 — Controlled User Trial**。

普通试用用户/管理员先看：

- `docs/USER_TRIAL_GUIDE_V1.md`

Skill 包：

- `skills/curating-erp-ai-resources/`

试用不要求用户理解项目历史，也不要求跑项目测试协议。用户直接拿自己的真实问题使用即可。

当前发布裁决：

> **CONTROLLED USER TRIAL GO / BROAD RELEASE NO**

详见：`docs/validation/RELEASE_READINESS_ADVERSARIAL_20260830.md`。

## 项目维护者从这里开始

- `docs/PROJECT_MAP.md` — **当前导航权威；新 Agent / 新会话先读**
- `docs/PROJECT_NORTH_STAR.md` — 产品边界与最终用户结果
- `docs/OWNER_EXECUTION_RULES.md` — 云端/本地/Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段与下一步
- `docs/validation/EVIDENCE_STATUS.md` — 当前证据状态
- `skills/curating-erp-ai-resources/SKILL.md` — 当前 runtime Skill

历史/条件性设计不作为当前入口，具体分类见 `docs/PROJECT_MAP.md`。

## 当前 Skill

- version: **0.7.0**
- release class: **Controlled User Trial**
- product value: **Unvalidated**

0.7.0 的主要边界：

- 用用户真实 baseline 而不是裸模型做 A/B/C；
- 把“当前任务下优先推荐实践”与无证据的“全球最佳”分开；
- practitioner / author self-practice / implementation / official fact / curator synthesis 分层；
- `信息不足 != C`；
- C 不自动变成“让用户测试工具”；
- Runtime/local test 只在 decision-changing 时出现；
- runtime Skill 保持精简，项目历史留在项目层。

## 核心判断

### A — 当前工具链已够用

不为了推荐而搜索或安装新能力。

### B — 专门能力有明显增益

只有专门能力解决了一个具体、可观察的 capability gap，并且收益值得安装、学习、迁移、权限和治理成本时，才定向发现。

### C — 当前不值得复杂化

专门能力可能有价值，但现阶段成本/规模/不确定性不支持重投入。给最低成本学习/采用路径和升级信号。

## 外部证据顺序

真正需要外部资源时：

```text
independent practitioner / 真实复盘 / 失败经验
→ author self-practice（明确标注）
→ 原始 Tool / Skill / repo / 方法
→ 会改变采用判断的当前官方事实
→ 限制 / 反证 / curator synthesis
```

搜索摘要只能 discovery，不能冒充已读证据；多个平台复读同一 Demo 不算多份独立验证。

## Curation Pack 01

当前 pre-user pack 已完成并停止扩张：

- Case 001 — ERP 操作手册：B；
- Case 002 — Oracle EBS AI 开发：B；
- Case 003 — 多顾问周报/PPT 汇总：A；
- Case 004 — SAP Bug/系统 evidence access：A → conditional B。

Authority：`docs/validation/CURATION_PACK_01_ADVERSARIAL_REVIEW.md`。

这证明的是方法在真实来源问题上的基本区分度，**不是用户价值已经验证**。

## 两条证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 研究和推荐。

它不能证明用户已采用或产生价值。

### Lane B — REAL_USER_USE VALIDATION

真实同事收到推荐后，自然学习、采用、修改、忽略或拒绝，并给出具体原因。

这才用于验证：

- 是否比自己搜索/普通 AI 更省判断成本；
- 是否少选错工具；
- 是否漏掉企业约束或关键能力；
- 是否减少配置/返工；
- 用户是否愿意再次使用。

详见 `docs/REAL_USER_PILOT_V1.md`。

## 当前最重要的结论

### 已完成

> **方法/Skill/Harness 的 pre-user 构建和 controlled-trial readiness。**

### 尚未完成

> **North Star 用户结果目标。**

尚未证明 Curator 相比普通 AI / 用户自己搜索具有稳定、重复、足够大的真实用户增量价值。

所以当前正确动作不是继续闭门完善 Skill，而是进入小范围真实用户使用。

## 当前不做

在真实使用证明必要性之前，不建设：

- 大型资源数据库或自动 Refresh；
- 固定场景 taxonomy；
- 统一评分 / Gate；
- 多 Agent 编排；
- 每个候选强制 runtime；
- creator/UP 主排行榜；
- 让真实用户替项目执行测试协议；
- 为了保持 Agent 忙碌而制造任务。

## Public / open-source note

仓库当前公开，但尚未包含 repository `LICENSE` 文件。

这不阻塞受控试用；如果要正式声明 public/open-source release complete，需要 Owner 明确许可方式。Agent 不擅自选择许可证。
