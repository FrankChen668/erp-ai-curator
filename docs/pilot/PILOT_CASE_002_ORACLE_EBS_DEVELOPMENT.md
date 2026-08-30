# Pilot Case 002 — Oracle EBS 开发如何更有效地使用 AI

Date: 2026-08-30
Status: **BEST-PRACTICE CURATION READY — AWAITING REAL USER FEEDBACK / ADOPTION**
Skill: `curating-erp-ai-resources` `0.6.3`

> 来源：2026-08 训前调研中的真实开发人员问题——“找到一款更适合 EBS 开发的 AI 工具”。本文件不是工具排行榜，也不要求用户先测试多个 AI；目标是把现有实践压缩成最值得采用的 EBS AI 开发方式。

## 1. 真实问题

角色：开发人员。

当前材料：系统截图、代码/日志、数据库/SQL。

当前方式：把需求拆成若干步骤让通用 AI 协助，最后人工整合。

期望：AI 能更稳定地参与 Oracle EBS 定制开发，并产出更接近“完整可用”的代码。

关键现实：`EBS 开发`不是一个单一技术面，可能涉及 PL/SQL、Forms、OAF、Reports、Workflow、接口、并发程序、APEX/ORDS 扩展以及 R12.2 在线补丁/EBR 等约束。

## 2. Curator 0.6.3 结论

> **B — 值得采用专门的“EBS Context Engineering + Coding Agent”工作方式，但不建议把问题理解成“寻找一个神奇的 EBS 专用 AI”。**

当前证据更支持：**工具第二，上下文第一。**

真正决定 AI 在 EBS 开发里是否好用的，不只是模型是否支持 PL/SQL，而是它能否持续获得：

- 当前 EBS 版本与模块；
- 团队自己的定制代码和对象结构；
- 命名、日志、异常处理、部署与回滚规范；
- Oracle EBS coding standards / R12.2 约束；
- 已有 API、表、包、接口和项目级设计说明；
- 编译、测试和非生产验证结果。

因此，最值得推广的不是“统一换成某款 EBS AI”，而是把团队定制资产变成 Coding Agent 可读、可追踪的工程上下文。

## 3. 最值得看的 practitioner 实践

### 主资源：JMJ Cloud — Make Claude Code Your Most Productive Oracle EBS Developer

https://jmjcloud.com/blog/oracle-ebs-monorepo/

这是当前找到的最直接 EBS + Coding Agent 实操案例。

它描述的核心不是“Claude 比其他模型更懂 EBS”，而是：

1. 将 EBS custom extensions / integrations 统一进结构稳定的 monorepo；
2. 把表 DDL、PL/SQL 包、视图、FNDLOAD、部署脚本等放在可预测路径；
3. 用根级和项目级 `CLAUDE.md` 固化 schema、对象、命名、日志、部署等团队规则；
4. Agent 每次工作时直接读取这些上下文；
5. 在这种结构下，通用 Coding Agent 才能生成更符合团队实际标准的 EBS 定制代码。

作者还明确强调：Claude Code 在这个模式下不需要数据库凭据，仓库本身先承担上下文源。

### 证据边界

这是 JMJ Cloud 自己的实践/方法论，属于 **author self-practice**，不是独立第三方对照实验；其“144 projects”等效果声明不能外推成行业事实。

但它对本问题很有价值，因为它给出了完整、可复用的输入结构和失败原因：通用 AI 生成“generic PL/SQL”的根因常常是缺团队上下文，而不是单纯模型能力不足。

## 4. 相邻 practitioner 证据

Cloud Nueva 的开发者记录自己使用 GitHub Copilot 做 PL/SQL/ORDS 开发，称代码补全在不同任务上带来不同程度的效率提升，并用于 EBS sales-order 相关 ORDS 开发。

https://blog.cloudnueva.com/vibe-coding-an-apex-deployment-tool-in-python-using-github-copilot

它支持一个更谨慎的结论：**主流 Coding Agent 已能给 PL/SQL 开发带来实际帮助，但收益取决于任务类型，并不能自动获得 EBS 项目语义。**

Oracle Forum 上 2025 年也有 EBS 维护人员直接提问“有没有更适合 Oracle SQL / PL/SQL 的 AI assistant”，反映了通用 Coding AI 在 EBS 场景中的真实需求，但该帖子本身几乎没有形成高质量采用答案，因此只作为需求/coverage evidence，不作为最佳实践证明。

https://forums.oracle.com/ords/apexds/post/any-ai-code-assistant-tool-for-oracle-ebs-developement-4410

## 5. 原始 / 官方能力核验

### Oracle E-Business Suite Developer's Guide

https://docs.oracle.com/cd/E26401_01/doc.122/e22961/index.html

Oracle 官方文档明确包含：

- coding standards；
- standard development environment；
- EBS application framework；
- R12.2 online patching / customization preparation；
- PL/SQL 等开发规范。

这说明 EBS 定制开发天然存在“必须进入 AI 上下文”的产品规范，不能只依赖模型的 PL/SQL 常识。

### GitHub Copilot repository custom instructions

GitHub 当前官方支持 repository-wide、path-specific 和 agent instructions，可用 `.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、`AGENTS.md` 等给 Agent 持久项目上下文。

https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions

这说明“把 EBS 开发规范工程化进仓库上下文”不是 Claude Code 专属技巧，而是可以迁移到不同 Coding Agent 的通用方法。

### Oracle Code Assist

Oracle 当前页面将 Oracle Code Assist 描述为面向 Java、SuiteScript、PL/SQL 和 OCI application development 优化的 AI code companion，并支持组织代码库/开发规范定制。

https://www.oracle.com/cn/application-development/code-assist/

但当前公开页面仍强调 limited availability，且没有足够证据证明它对 Oracle E-Business Suite custom development 比成熟通用 Coding Agent + EBS context 更有稳定优势。

因此本轮不把 Oracle Code Assist 作为默认答案，只保留为 PL/SQL/Oracle-native 路线的后续候选。

## 6. 最佳实践卡片

### 推荐模式：EBS Context Engineering + Coding Agent

```text
EBS 版本 / 模块 / 真实需求
→ 将 custom code / DDL / interfaces / deployment scripts 纳入版本库
→ 固化团队开发规则与对象地图（CLAUDE.md / AGENTS.md / copilot instructions 等）
→ 加入必要的 Oracle EBS 官方开发规范/引用
→ Coding Agent 基于仓库上下文分析、生成或修改小范围代码
→ 输出代码 + 假设 + 影响范围 + 测试/部署说明
→ 在非生产环境编译、测试、回归
```

### 为什么这是“最佳实践”，而不是某个工具推荐

因为它直接解决 EBS AI 开发中最稳定的瓶颈：**项目上下文缺失**。

它还能在 Claude Code、Codex、Copilot 等 Agent 之间迁移；即使以后模型变化，团队沉淀的代码结构、规则和官方规范仍然有价值。

## 7. 什么时候才升级到更重的 Tool / MCP / 系统连接

只有当真实瓶颈从“仓库上下文不足”变成下面这些问题时，再考虑升级：

- 必须实时读取数据库对象、元数据或执行计划；
- 必须访问仓库中不存在的 EBS 系统事实；
- 代码库非常大，普通 repo exploration 已经成为明显瓶颈；
- 需要受控的系统查询/调试能力，而不是仅生成代码；
- 数据、源码和凭据边界允许对应的连接方式。

理解/生成阶段默认不因为“AI 能连接数据库”就授予数据库写权限。

## 8. 不推荐的做法

- 只问“哪个 AI 最懂 EBS”，然后频繁换模型；
- 只把一段 PL/SQL 粘给聊天 AI，却不给版本、对象关系、团队规范和调用上下文；
- 把模型生成的“完整代码”当作可直接上线代码；
- 为了让 AI 更聪明，直接给生产数据库或 APPS 高权限凭据；
- 把 Oracle Code Assist 的 PL/SQL 优化能力直接等同于 EBS 专用能力。

## 9. 给用户的最小 Curator 输出

如果把结论发给提出问题的 EBS 开发人员，应传达：

> **先别急着找“EBS 专用 AI”。更成熟的实践是把 EBS custom code、DDL、接口、部署脚本和团队规范集中成 Agent 可读的项目上下文，再用成熟 Coding Agent 工作。当前直接 EBS 实践提供了一个很有参考价值的落地案例，但还不是独立对照证明；Oracle 官方 Developer's Guide 应作为规范源。Claude Code/Codex/Copilot 都可以承载这种模式。Oracle Code Assist 可以继续关注，但目前公开证据不足以证明它应该取代这套方法成为默认选择。**

最值得先看的实操资源：JMJ Cloud 的 EBS monorepo + Claude Code 案例。

## 10. Evidence / validation boundary

当前完成的是：

- 真实 EBS 开发问题重构；
- 直接 EBS practitioner 实践筛选；
- 相邻 PL/SQL practitioner evidence；
- Oracle EBS 官方开发规范核验；
- 当前 Coding Agent project-context 能力核验；
- Oracle Code Assist 当前能力/availability 边界核验；
- Curator synthesis。

这已经是 Curator 的产品输出，但还不是“真实用户采用后价值已验证”的证据。
