# Cloud Product Validation — 执行方案

## 1. 目标

先回答一个问题：

> ERP AI Curator 这套“理解任务 + 搜索 + 阅读原文 + 横向取舍”的方法，能否稳定产出真正值得分享的资源？

在这个问题没有被真实结果证明前，不再开发新 Skill、不加脚本、不做数据库。

## 2. 责任划分

### 云端负责

- 真实互联网检索；
- 打开原始资源；
- 判断 task fit；
- 高风险事实核验；
- 形成 0–2 个最终推荐；
- 记录 Review Card；
- 根据失败模式调整产品设计；
- GitHub 文档与后续 Skill 实现。

### Product Owner 负责

只做最终业务判断：

- 值得分享
- 一般
- 不值得分享

不要求 Product Owner 管测试协议、分支、Agent 失败或重跑。

### 本地 Agent

暂时退出关键路径。

以后仅用于：

- 拉取 / 提交文件；
- 运行确定性检查；
- 可机械验证的批量操作。

禁止让其自行判断产品 PASS、修改 Eval 设计或解释业务目标。

## 3. 第一轮真实任务集

直接使用 10 个代表性任务，不做 baseline：

1. SAP / Oracle 顾问生成可编辑 draw.io 业务流程图
2. 顾问快速生成可评审交互原型
3. Claude Code 当前第三方 / 低成本模型配置
4. Codex CLI 当前第三方 / 低成本模型方案
5. SAP Fit-to-Standard / Fit-Gap 的 AI 实战方法
6. Oracle 实施需求调研 / Solution Design 的 AI 方法
7. SAP 陌生模块快速学习方法 / prompt framework
8. Oracle Fusion 陌生模块快速学习方法 / prompt framework
9. 只找“能读代码并生成架构图”的 Agent Skill
10. Oracle EBS 老版本 AI 自动 Fit-Gap 成熟开源 Skill（稀缺题）

这些任务覆盖：

- 丰富资源 / 稀缺资源；
- Skill / Tool / 教程；
- 高风险配置；
- ERP 专属 / 通用迁移；
- 需要正确 abstain 的场景。

## 4. 每题执行协议

### Step 1 — 定义完整任务

只提炼：

- 谁使用；
- 要完成什么；
- 最终要得到什么；
- 用户显式限制。

不拆成复杂 schema。

### Step 2 — 搜索

同时覆盖：

- 官方 / 原始仓库；
- GitHub Skill / Tool；
- 中文实操；
- 英文高质量实操；
- ERP 专属资源；
- 可直接迁移的通用资源。

不设固定查询次数。

### Step 3 — 阅读原文

最终候选必须打开原始内容。

不得只依赖：

- 搜索摘要；
- 聚合站；
- Star；
- AI 二次摘要。

若一个 Skill 正常工作依赖 references / assets / 子文档，要读与当前任务直接相关的部分，不能只看入口 README。

### Step 4 — 比较

主要回答四个问题：

1. 是否匹配**完整任务意图**？
2. 点开后具体能得到什么？
3. 是否比其他候选明显更值得花时间？
4. 有没有关键限制会让它对当前用户失效？

不打统一数字分。

### Step 5 — 高风险事实核验

命中安装 / 配置 / API / 版本 / 价格 / 原生能力边界时，回当前官方或原始来源。

### Step 6 — 输出

正式推荐 0–2 个。

相邻资源可以作为 optional note，但不能伪装成完整任务匹配。

## 5. 验收方式

### 第一层：Product Owner Shareability

每题只评：

- **值得分享**
- **一般**
- **不值得分享**

### 第二层：失败归因

失败只归到一个主要原因：

- 任务理解错
- 搜索覆盖不足
- 候选原文没读透
- 横向选择错误
- 高风险事实错误
- 过度 abstain
- 该主题本身无高质量公开资源

### 第一轮目标

10 题中：

- ≥ 8 题“值得分享”：进入正式 Skill 固化；
- 6–7 题：继续调整产品方法，不开发；
- ≤ 5 题：重新评估是否值得做成 Skill。

这里不使用 recommendation count、JSON 合法性或 validator 通过率作为产品成功指标。

## 6. Skill 何时重新实现

只有第一轮真实任务验证通过后，才重新实现。

届时采用最小结构：

```text
skills/erp-ai-curator/
├── SKILL.md
└── references/
    ├── source-strategy.md
    ├── selection-heuristics.md
    └── volatile-fact-check.md
```

第一版仍然：

- 0 scripts；
- 0 database；
- 0 Gate；
- 0 score；
- 0 candidate JSON。

并且不会把 10 个测试题的答案写进 Skill。

## 7. 后续 A/B 的位置

A/B 不取消，但延后。

顺序改成：

1. 先验证“这套方法产出的结果是否值得分享”；
2. 再把方法固化成 Skill；
3. 最后用 fresh tasks 比较 Skill vs ordinary prompt，验证 Skill 是否真的增加稳定性。

这样 A/B 测的是“Skill 是否值得存在”，而不是拿它代替产品验证。

## 8. GitHub 工作方式

- `main`：只放已经确认的设计结论；
- `reset/cloud-validation-v1`：本轮重新盘点和执行方案；
- PR #4：关闭但不删除，作为 Phase 4 Pilot 历史证据；
- 后续云端验证结果单独进入 `docs/cloud-validation/`。

## 9. 当前停止项

直到 Cloud Product Validation 完成前，停止：

- Round 4 / Round 5；
- 新增 Eval case 自动跑；
- 本地子 Agent 编排；
- Skill 修补；
- scripts / validator；
- resource DB / CSV；
- refresh automation。

唯一主线：

> **真实任务 → 真搜索 → 真阅读 → 少量推荐 → Product Owner 判断。**
