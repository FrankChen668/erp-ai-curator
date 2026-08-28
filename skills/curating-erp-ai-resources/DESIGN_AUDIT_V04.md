# V0.4 第一性原理 / 对抗性修正说明

## 1. 本轮不是继续“加规则”

V0.3 已经证明硬 Gate 能显著降低 false recommendation。剩余问题不是搜索能力，而是 Agent 会把“看起来有用”的资源强行解释成当前题目需要的资源。

因此 V0.4 只修两个根因：

1. **对象身份不清**：tool / skill / tutorial / official_doc 混淆；
2. **能力边界不清**：standard product / custom extension / third-party wrapper 混淆。

## 2. 第一性原理

一个资源能否推荐，至少需要四个事实同时成立：

> 它是什么 → 用户要做什么 → 它实际产出什么 → 它声称的能力在什么边界内成立。

任何一个被偷换，推荐就可能“看起来合理、实际错误”。

## 3. V0.3 真实失败映射

### F1 OpenDesign 被标成 Skill

根因：把 GitHub 仓库形态/支持 Agent Skills 与资源自身类型混淆。

V0.4：新增 `requested_resource_types`、`resource_type`、`gate_resource_type_fit`。

### F2 JeecgBoot BPM 教程占流程图教程位

根因：只检查“流程相关”，没有检查最终交付物。

V0.4：新增 `gate_output_fit`；核心产出不同即错主题/reroute。

### F3 Joule 扩展能力被当成标准产品能力

根因：官方锚点的“能力模式”与第三方 claim 不同，却被当成同一证据。

V0.4：capability claim 强制记录 claim/anchor capability mode 与 platform scope；不同模式不能互证。

### F4 厂商指标被事实化

根因：来源自身的 marketing/performance claim 被改写成客观事实。

V0.4：vendor_claim 只能按来源声称表达，不能成为主要推荐证据。

## 4. 为什么没有重做数据架构

正式四表仍可保留。新增字段主要存在于 staging candidate review；只有 `resource_type` 本来就在 resources 表中。

这避免为了修语义判断而引入第五张正式表或新工程。

## 5. V0.4 的成功标准

不是脚本 0 ERROR，而是原 5 主题复跑时：

- OpenDesign 不再被叫 Skill；
- BPM 工作流配置不再冒充流程图绘制；
- 自定义 Joule Skill 文档不再证明标准 Joule 原生配置能力；
- 没有好资源时继续允许 0 推荐。
