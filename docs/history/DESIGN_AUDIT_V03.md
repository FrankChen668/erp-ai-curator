# V0.3 对抗性修正记录

## 第一性问题

真正目标不是“让 Agent 搜得更广”，而是：

> 在不执行外部不可信指令的前提下，让 Agent 对候选资源做足够可靠的拒绝判断，最终只留下能直接服务 ERP 顾问任务、且关键事实站得住的少量链接。

## V0.2 实跑暴露的根因

### 1. 评分发生得太早

V0.2 虽然写了硬门槛，但没有把“Gate 全 PASS 才能评分”做成强状态机，Agent仍会先形成推荐倾向，再用评分和推荐理由合理化。

### 2. Topic Fit 太抽象

“对 ERP 顾问有价值”范围过宽，导致高质量但错主题的 SAP AI Workshop 被塞进需求分析主题。

### 3. Provenance 没有结构化 fork/upstream 规则

“尽量检查是否原始仓库”不足以阻止 Agent 推荐 fork。

### 4. “与官方冲突则淘汰”缺少 material claim 提取步骤

Agent没有先抽取 API、环境变量、产品能力等重要声明，因此无法稳定触发冲突判断。

### 5. 输出语言诱发虚假确定性

“最佳、唯一、最完整”让 Agent用语言包装不充分比较的结果。

### 6. 完成偏差

固定测试 5 主题后，Agent产生“每题都要给答案”的倾向，导致后两题硬凑。

## V0.3 修正

- 引入 G0–G5 Candidate Gates；
- 状态机规定 `gate_passed` 前不得评分；
- Topic Fit 使用“角色→动作→结果”因果句；
- GitHub fork 必须解析 upstream；
- material claim 建立 supported/conflict/unclear 核验；
- critical conflict 一票否决；
- 明确 0 推荐是合法成功；
- 禁止无证据超级词；
- E11–E17 全部取自真实失败。

## V0.3 仍未解决的风险

- 本地 Agent 的 WebSearch/WebFetch 覆盖能力仍可能影响公众号、小红书、B站正文核验；
- Agent 对“critical claim”的抽取可能漏项；
- 某些官方文档本身分散或更新滞后，需要 human_review；
- 评分仍然依赖模型判断，只能用于 Gate 后的排序；
- V0.3 还没有在目标 TRAE/WorkBuddy 上完成真实回归测试。

## 通过标准

V0.3 不以“文件写完”为完成。

至少用同一批 5 个主题复跑，并重点检查：

- E11 fork/upstream；
- E12 配置事实冲突；
- E13 topic mismatch；
- E14 unsupported superlatives；
- E15 产品能力夸大；
- E16 0 推荐。

这些行为明显改善后，才考虑 V0.4 或扩大建库。
