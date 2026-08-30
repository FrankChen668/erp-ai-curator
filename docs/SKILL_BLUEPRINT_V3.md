# ERP AI Curator — Historical Skill Blueprint V3

Status: **SUPERSEDED DESIGN RECORD / NOT RUNTIME AUTHORITY**

> 本文件曾是 Skill 实现前的设计蓝图。当前 runtime Skill 已经演化到 `0.7.0`，因此本文件不再提供 CURRENT implementation instructions。

## 当前 Skill

- runtime: `skills/curating-erp-ai-resources/SKILL.md`
- navigation: `docs/PROJECT_MAP.md`
- product boundary: `docs/PROJECT_NORTH_STAR.md`
- current execution: `docs/CURRENT_EXECUTION_PLAN_V3.md`

## 历史上保留下来的有效设计思想

以下原则经过后续实践仍然成立，并已经进入当前 North Star / Skill：

- Skill 处理 AI 工作方式选择，不维护固定资源数据库；
- 真实任务和用户当前 baseline 优先；
- capability gap 决定是否引入专门能力；
- practitioner-first discovery；
- current official facts 只做必要兜底；
- progressive disclosure；
- scripts 只处理 deterministic work；
- runtime/local test 只在可能改变采用判断时做；
- 来源 Adapter 只能按需、read-only、作为 evidence acquisition capability。

## 已退出当前路线的内容

不要从历史 blueprint 恢复：

- 实现前阶段门槛；
- 固定 Mode C 测试协议；
- Source Adapter 作为默认产品架构；
- 本地 Agent 实现作为关键路径；
- 任何和当前 0.7.0 runtime Skill 冲突的旧流程细节。

完整历史仍可从 Git history 获取；当前设计校准见 `docs/PROJECT_CALIBRATION_20260830.md`。
