# 分类体系

## 第一原则

主入口回答“ERP 项目现在要完成什么任务”。工具和 Skill 是独立视图，不与项目阶段混为一类。

## topic_type

- task
- tool
- skill

## lifecycle_stage

仅表示时间/实施生命周期：

1. 售前与方案
2. 项目准备
3. 调研与需求
4. 蓝图与方案设计
5. 配置与开发
6. 测试与数据迁移
7. 上线与切换
8. 运维与优化
9. cross_stage

## workstream

用于表达跨阶段能力，避免把“项目管理”“知识学习”硬塞成生命周期阶段：

- project_management
- business_analysis
- solution_design
- development
- testing
- data_migration
- integration
- documentation
- knowledge_learning
- ai_engineering
- other

## task 示例

- 需求访谈整理
- 需求提取与分类
- Fit/Gap 分析
- 业务流程图/BPMN
- 原型设计
- 方案架构图
- 集成接口梳理
- SAP/Oracle 模块快速学习
- 代码库快速理解
- ABAP/Java/SQL/脚本辅助
- 测试用例设计
- 缺陷定位
- 数据映射与校验
- Cutover 计划
- 操作手册
- 会议纪要与 Action
- RAID / 风险分析
- 项目计划审查
- 周报/月报
- 方案/文档审查
- Agent/自动化工作流搭建

## role_tags

- SAP 顾问
- Oracle 顾问
- ERP 业务顾问
- 实施顾问
- 解决方案顾问
- 项目经理
- 产品经理
- 开发人员
- 测试人员
- 数据/集成顾问

## 工具入口

工具是 topic，不是 resource。一个工具主题可以被多篇资源推荐，一个资源也能同时映射多个任务。

常见工具：ChatGPT、Codex、Claude/Claude Code、TRAE、WorkBuddy/CodeBuddy、OpenCode、Gemini CLI、Cursor 等。

## Skill 入口

Skill 主题重点关注：
- 原始仓库/市场页
- 解决的问题
- 支持的 Agent/工具
- 安装与维护状态
- 映射的 ERP 任务
- 最佳实操资源

不要把单个 Prompt 当成 Skill。


## resource_type 与 topic_type 不得混淆

`topic_type` 是用户浏览入口；`resource_type` 是候选资源自身是什么。

- 完整产品/桌面应用/CLI：resource_type=tool；
- 可加载的 Agent Skill：resource_type=skill；
- 操作文章/视频：resource_type=tutorial；
- 官方能力页/指南：resource_type=official_doc；
- 案例：resource_type=case。

GitHub 只是承载平台，不决定 resource_type。一个 GitHub 仓库可能是 tool，也可能是 skill。

如果当前用户明确只要 Skill/教程，tool 候选即使质量很高也不能占位；应转入 tool 入口或其它合适主题。
