# 关键示例

## 1. Claude Code 第三方模型配置

volatile。

正确：
1. 先找当前官方/原始事实锚点；
2. 再找中文实操；
3. practical 必须读到关键步骤；
4. 高赞旧教程若与当前官方冲突，直接淘汰。

最终可以是：官方说明 + 最佳中文实操，也可以只有一个。

## 2. 流程图 Skill

不要只搜“AI画流程图”。

同时找：
- Skill 原始仓库/市场页；
- 支持 Mermaid/draw.io/BPMN 等能力；
- 维护情况；
- 实际使用文章/视频；
- 映射到 ERP 的流程设计任务。

## 3. 访问受限的公众号

搜索结果能看到标题和摘要，但正文打不开。

只能：
- resources 记录 metadata_only；
- recommendation 状态 candidate；
- human_review=true。

不能因为搜索摘要看起来不错就自动推荐。

## 4. 同一资源多个入口

一篇 Claude Code 工作流文章同时适合：
- 需求文档审查
- 代码库理解
- Claude Code 工具入口

resources 只保存 1 条；recommendations 创建 3 条关系。

## 5. GitHub fork 看起来“能用”，但不是该推荐的原始仓库

错误：
- 搜到一个 Claude Code Router fork；
- README 可读、功能也对；
- 直接因为“有中文/能运行”推荐。

正确：
1. 先查 `fork`；
2. 追 parent/source；
3. 比较 upstream 当前维护、社区和功能；
4. fork 没有与当前 topic 直接相关的实质优势，就推荐 upstream。

## 6. 中文教程步骤完整，但关键配置与官方冲突

错误：
- 因为截图多、步骤完整、中文友好就判 practical 高质量。

正确：
1. 抽取 base URL、认证变量、模型名等 material claims；
2. 找当前官方集成文档；
3. critical claim 冲突则直接淘汰；
4. 不能用评分补救。

## 7. 官方资源很好，但解决的是另一个问题

例如官方 AI use-case workshop 很适合“发现 AI 机会”，但当前 topic 是“ERP 实施项目需求访谈 / Fit-Gap”。

即使来源权威，也要因为 G1 主题错配移到更合适 topic，而不是硬塞进当前推荐。

## 8. 没有好资源

搜索已覆盖，候选均因事实冲突、主题错配或正文不可核验被淘汰。

正确输出：

> 当前暂无 Gate 全 PASS 的推荐资源，保留空缺并记录搜索范围。

这不是执行失败。


## 9. GitHub 上的完整工具，不等于 Skill

用户问“原型设计有哪些 Skill 和教程”。搜到 OpenDesign：托管在 GitHub、支持 Claude Code/Codex，也有技能生态，但它自身是完整桌面工具。

正确：
- resource_type=tool；
- requested_resource_types=[skill,tutorial]；
- 当前请求 resource_type_fit=false；
- reroute 到 OpenDesign 工具入口或“原型设计推荐工具”。

错误：因为仓库里有 Skill/Plugin 字样就写成 skill(practical)。

## 10. 工作流配置教程，不等于流程图绘制教程

用户要的是“从业务描述得到可编辑 BPMN/Swimlane 图”。教程主要讲创建 BPM 系统节点、条件、Token、API 部署。

即使内容很实操，它的 expected_output 是“可执行工作流配置”，不是“顾问流程图交付物”。

正确：gate_output_fit=fail，并 reroute 到“AI 辅助 BPM/工作流配置”。

## 11. 自定义扩展文档不能证明标准产品原生能力

第三方文章声称标准 ERP AI 助手能自动完成配置链；官方找到的是“如何开发自定义 Skill/Agent 扩展并连接后端”。

正确：
- claim_capability_mode=standard_product；
- anchor_capability_mode=custom_extension；
- 不能互证；
- critical 时 reject，无法确认时 human_review。

不要用“官方支持扩展开发”偷换成“标准产品默认具备该能力”。
