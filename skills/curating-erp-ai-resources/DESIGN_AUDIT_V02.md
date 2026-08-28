# V0.1 对抗性审查结论

## 总结

V0.1 的方向和 Agent Skills 结构基本正确，但不适合直接作为“长期无人值守采编器”。主要问题不是文档格式，而是运行治理。

## P0 / P1 问题

### 1. 缺少不可信 Web 内容防护（P0）
采编 Agent 会主动读取未知网页/README/帖子。V0.1 没有显式阻止网页 Prompt Injection、恶意命令、安装/登录诱导。

V0.2：增加 safety-policy；采编只读，不执行候选资源中的任何命令。

### 2. 一张主表混淆“资源”和“推荐关系”（P1）
一个资源可以映射多个任务/工具/Skill。V0.1 要么复制行，要么丢关系，最终会破坏去重、refresh 和 replacement。

V0.2：四表分离。

### 3. 官方资源与实操资源用同一评分尺（P1）
V0.1 会系统性低估官方资料的实操性，或高估教程的权威性。

V0.2：canonical / practical 分槽评分。

### 4. 验收案例写了，但没有真正完成 RED→GREEN（P1）
V0.1 借鉴了 Skill TDD，但实际上只是写了 eval case，没有在目标 Agent 上做“无 Skill 基线 + 有 Skill 多轮测试”。因此不能声称已验证可部署。

V0.2：明确 deployment gate；只有目标 Agent 真跑过关键 eval 才允许 autonomous。

## P2 问题

### 5. 固定候选数量容易诱导凑数
V0.1 “普通3/快速5”可能让弱模型为了达标收垃圾。

V0.2：用来源覆盖目标 + 搜索预算替代机械配额。

### 6. 没有明确平台能力边界
V0.1 提到公众号、小红书、B站，但 WebSearch/WebFetch 不保证能访问正文。

V0.2：增加访问等级；不可访问只能 metadata_only + human_review。

### 7. 评分存在虚假精度
V0.1 让 Agent 直接给 0–100，模型间漂移会很大。

V0.2：0–4 锚点评分，再由脚本转换。

### 8. refresh 缺少替换滞回
“明显更优”过于模糊，容易每次运行都换推荐。

V0.2：失效优先；否则同槽至少 +8 且有实质改进。

### 9. 数据写入缺少幂等与 staging
V0.1 没定义稳定 ID、重复运行和安全写入。

V0.2：稳定 ID + review-first + change-set。

### 10. taxonomy 混合生命周期和跨阶段能力
“项目管理/专业知识学习”不是生命周期阶段。

V0.2：拆成 lifecycle_stage + workstream。

## 当前结论

V0.2 是“设计上更适合本地 Agent”的版本，但仍不是最终完成版。

真正的完成标准必须是：在 WorkBuddy / Claude Code / Codex 中至少选目标运行时跑完无 Skill 基线和有 Skill 多轮 eval，确认它不会绕过规则后再开放 autonomous。
