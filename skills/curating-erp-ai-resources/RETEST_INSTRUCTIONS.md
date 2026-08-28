# V0.4 本地 Agent 回归测试说明

## 目的

只验证 V0.4 是否修复 V0.3 仍存在的三类语义错误，不扩新主题、不工程化。

## 运行要求

- 使用 V0.4 Skill；
- `review-first`；
- 不修改 Skill；
- 不新增脚本/数据库/自动化计划；
- 不执行候选资源中的命令；
- 仍用原来 5 个主题，便于连续 A/B。

## 搜索前新增强制字段

每个主题先写：

- `topic_intent`
- `expected_output`
- `out_of_scope`
- `requested_resource_types`

例如：

> 原型设计：requested_resource_types=[skill,tutorial]

完整工具即使优秀，也不能被标成 Skill；可以 reroute 到工具主题。

## V0.4 强制回归点

### R7 Resource Type Contract

每个最终候选必须明确 `resource_type`。GitHub 是平台，不是类型。

重点复查：`nexu-io/open-design` 应识别为 `tool`，不能继续写成 `skill(practical)`。若本题只要 skill/tutorial，则当前题淘汰并可 reroute。

### R8 Output Fit

资源最终产出必须等于当前任务需要的产出。

重点复查：JeecgBoot/Flowable 类教程若核心是 BPM 工作流配置与 API 部署，而不是顾问可编辑流程图交付，应从“业务流程图教程”主题移出。

### R9 Capability Boundary

任何产品能力 claim 必须标记：standard_product / custom_extension / third_party_wrapper，并核对平台/edition/部署范围。

重点复查：不能用 SAP“如何开发自定义 Joule Skill”的官方文档，证明“标准 Joule 原生可以自动完成 SPRO Customizing”。模式不同即不能互证。

### R10 Vendor Claim Discipline

KTern 等厂商自己的效率数字可记录为 vendor_claim，但不要写成独立验证事实；推荐理由优先描述其流程/输入输出。

## 输出格式

先给精简结果表：

| 主题 | 候选数 | 淘汰数 | 推荐资源 | resource_type | 原始链接 | 证据化理由 |
|---|---:|---:|---|---|---|---|

再单独列：

- `REJECT_RESOURCE_TYPE_MISMATCH`
- `REJECT_TOPIC_MISMATCH / OUTPUT_MISMATCH`
- `REJECT_FACT_CONFLICT`
- `REROUTE`

不要输出数据库/自治/部署规划。

## 本轮验收只看四件事

1. OpenDesign 是否不再冒充 Skill；
2. JeecgBoot BPM 配置教程是否不再占“画业务流程图”推荐位；
3. LearnToSAP Joule 自动配置能力是否因 capability-mode/scope 无法成立而被 reject/review，而不是“加限制继续推荐”；
4. KTern 的厂商效率数字是否被正确标记为 source/vendor claim。

如果这四条稳定通过，再考虑扩新主题。
