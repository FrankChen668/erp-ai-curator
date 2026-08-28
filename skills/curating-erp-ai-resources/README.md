# ERP 顾问 AI 资源采编 Skill V0.4

面向 SAP / Oracle / ERP 顾问的 AI 实战资源采编 Skill。

核心目标不变：

> 搜索不是成果；经过淘汰后还能站得住的 0–2 个原始链接才是成果。

## V0.4 为什么改

V0.3 已明显修复 fork/upstream、官方事实冲突、错主题、强行填满等问题，但真实回归仍暴露三类语义错误：

1. **资源类型错标**：完整工具 OpenDesign 被写成 Skill；
2. **目标产出错配**：BPM 工作流配置教程被放进“业务流程图绘制教程”；
3. **能力层级偷换**：用“官方支持开发自定义 Joule Skill”去证明“标准 Joule 原生可以自动完成 SPRO 配置链”。

因此 V0.4 不增加工程复杂度，只增加两道语义纪律：

> **Resource Type Contract + Capability Boundary**

并把 G1 从单纯 Topic Fit 收紧为：

> **Task Fit + Output Fit + Resource Type Fit**

## V0.4 新规则

- GitHub 只是承载平台，不代表仓库就是 Skill；
- resource_type 必须是资源客观类型：tool / skill / tutorial / official_doc / case / collection / prompt_framework / other；
- 用户明确只找 Skill/教程时，完整 tool 不得占位，可 reroute 到工具主题；
- 资源最终产出必须与当前任务 expected_output 一致；
- 产品能力 claim 必须区分 standard_product / custom_extension / third_party_wrapper；
- capability mode、平台、edition、部署范围不一致时不能互证；
- 厂商自报效率数字只能作为 vendor_claim，不自动视为独立事实。

## 回归测试

继续使用原 5 个主题，不扩库。重点看：

- OpenDesign 是否被正确归为 tool；
- JeecgBoot BPM 工作流教程是否从“流程图绘制”移出；
- LearnToSAP Joule 自动配置能力是否因能力边界证据不足而被 reject/review；
- KTern 的效率数字是否改成厂商自报，而不是客观事实。

详见 `RETEST_INSTRUCTIONS.md` 与 `evals/scenarios.md`。

## 默认仍是 review-first

V0.4 的目标仍不是马上自治，而是先证明本地 Agent 的**语义分类和事实边界**稳定。
