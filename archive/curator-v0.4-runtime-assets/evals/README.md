# Eval 使用说明

V0.4 的 eval 不是“看 Agent 会不会生成漂亮答案”，而是检查它是否**拒绝错误候选**。

推荐在同一目标运行时（TRAE / WorkBuddy 等）固定模型、固定主题，先跑旧版再跑 V0.4，对比：

- false recommendation：不该推荐却推荐的数量；
- upstream errors：fork 未追上游；
- fact conflicts：与官方冲突却未淘汰；
- topic mismatch：高质量但错主题资源；
- unsupported superlatives：无证据“最好/唯一”；
- forced fill：没有好资源时是否仍硬凑。

V0.4 的优先通过项：E01、E03、E11、E12、E13、E15、E16、E18、E19、E20。

通过标准不是“17/17 一次全过”，而是关键错误连续多轮不再复现，且推荐质量没有因过严而明显下降。

V0.4 新增重点指标：resource type mismatch、output mismatch、capability-mode mismatch、platform-scope mismatch。
