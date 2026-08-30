# ERP AI Curator

面向 **SAP / Oracle / ERP / 企业信息化从业者** 的 AI 工作方式 Curator。

> **面对一个真实工作任务，普通 AI / 当前工具链是否已经够用？如果不够，互联网上已经存在的实操经验、Tool / Skill / MCP / 方法 / 教程中，什么最值得优先学习和采用？**

项目不是 AI 工具大全、教程百科、资源数据库或工具实验室。

## 从这里开始

当前项目地图：

- `docs/PROJECT_MAP.md` — **当前导航权威；新 Agent / 新会话先读**
- `docs/PROJECT_NORTH_STAR.md` — 产品边界
- `docs/OWNER_EXECUTION_RULES.md` — 云端/本地/Owner 执行边界
- `docs/CURRENT_EXECUTION_PLAN_V3.md` — 当前阶段与下一步
- `docs/validation/EVIDENCE_STATUS.md` — 当前证据状态
- `skills/curating-erp-ai-resources/SKILL.md` — 当前 runtime Skill

历史/条件性设计不作为当前入口，具体分类见 `docs/PROJECT_MAP.md`。

## 当前 Skill

- path: `skills/curating-erp-ai-resources/SKILL.md`
- version: **0.7.0**
- stage: **Curation pilot — user-use value unvalidated**

0.7.0 不是“更多规则”的版本，而是一次项目级校准：

- 用用户真实 baseline 而不是裸模型做 A/B/C；
- 把“当前任务下优先推荐实践”与无证据的“全球最佳”分开；
- practitioner / author self-practice / implementation / official fact / curator synthesis 分层；
- C 不再自动变成“让用户测试工具”；
- Runtime/local test 仍只在 decision-changing 时出现；
- runtime Skill 保持精简，项目历史留在项目层。

## 核心判断

### A — 当前工具链已够用

不为了推荐而搜索或安装新能力。

### B — 专门能力有明显增益

只有专门能力解决了一个具体、可观察的 capability gap，并且收益值得安装、学习、迁移、权限和治理成本时，才定向发现。

### C — 当前不值得复杂化

专门能力可能有价值，但现阶段成本/规模/不确定性不支持重投入。给最低成本学习/采用路径和升级信号。

**信息不足不是 C。**

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

## 两条必须分开的证据 Lane

### Lane A — REAL_USER_ORIGIN CURATION

真实同事/问卷/Owner 的真实问题，由 Curator 先完成研究和推荐。

当前案例：

- `docs/curation-cases/CASE_001_ERP_OPERATING_MANUAL.md`
- `docs/curation-cases/CASE_002_ORACLE_EBS_DEVELOPMENT.md`

它们证明“Curator 能针对真实来源问题形成可审查推荐”，**不证明用户已采用或产品已产生价值**。

### Lane B — REAL_USER_USE VALIDATION

真实同事收到推荐后，自然地学习、采用、修改或拒绝，并给出具体反馈。

这才用于验证：

- 是否比自己搜索/普通 AI 更省判断成本；
- 是否少选错工具；
- 是否漏掉企业约束或关键能力；
- 用户是否愿意再次带真实问题回来。

详见 `docs/REAL_USER_PILOT_V1.md`。

## 当前可信结论

已完成的 P01/P03/P04/P06/P07 等异构任务研究支持一个稳定方法骨架：

1. 真实任务和当前 baseline 优先；
2. 专门方案必须对应 capability gap；
3. external adoption evidence 优先 practitioner 真实经验；
4. 重要事实回原始/官方/source/system 证据；
5. runtime/local test 只是决策工具；
6. 结论稳定就停。

当前 evidence authority：`docs/validation/EVIDENCE_STATUS.md`。

**尚未证明**：Curator 相比普通 AI / 用户自己搜索有稳定、重复的真实用户价值。

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

## 当前阶段

> **先完成少量高区分度的 REAL_USER_ORIGIN curation，持续吸收自然出现的 REAL_USER_USE 反馈；不要把更多内部自测冒充产品验证。**

云端能完成的研究、审查、GitHub 维护继续由 Cloud 直接推进；只有本地文件/runtime/企业环境确实会改变结论时，才交给 Local Agent。
