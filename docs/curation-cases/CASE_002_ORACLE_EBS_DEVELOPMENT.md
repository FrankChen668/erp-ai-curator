# Curation Case 002 — Oracle EBS 开发如何更有效地使用 AI

Date: 2026-08-30
Status: **REAL_USER_ORIGIN CURATION READY — NOT USER-USE EVIDENCE**
Originally produced with Skill: `0.6.3`  
Re-reviewed against Skill: `0.7.0` — **recommendation stable**

> 来源是 2026-08 训前调研中的真实开发人员问题——“找到一款更适合 EBS 开发的 AI 工具”。本文是对真实来源问题形成的 Curator 推荐，不代表该开发人员已经看到、采用或验证了推荐。

## 1. 真实问题

角色：开发人员。

当前材料：系统截图、代码/日志、数据库/SQL。

当前方式：把需求拆成若干步骤让通用 AI 协助，最后人工整合。

期望：AI 更稳定地参与 Oracle EBS 定制开发，并产出更接近可用代码的结果。

`EBS 开发`不是单一技术面，可能涉及 PL/SQL、Forms、OAF、Reports、Workflow、接口、并发程序、APEX/ORDS 扩展以及 R12.2 在线补丁/EBR 等约束。

## 2. Curator 结论

> **B — 当前最值得优先借鉴的是“EBS Context Engineering + Coding Agent”，而不是继续寻找一个神奇的 EBS 专用 AI。**

当前证据更支持：**工具第二，上下文第一。**

真正影响 AI 在 EBS 开发中是否好用的，不只是模型支持 PL/SQL，还包括它能否持续获得：

- 当前 EBS 版本与模块；
- 团队自己的定制代码和对象结构；
- 命名、日志、异常处理、部署与回滚规范；
- Oracle EBS coding standards / R12.2 约束；
- 已有 API、表、包、接口和项目级设计说明；
- 编译、测试和非生产验证结果。

## 3. 最值得看的直接 EBS 实践

主资源：JMJ Cloud — Make Claude Code Your Most Productive Oracle EBS Developer

https://jmjcloud.com/blog/oracle-ebs-monorepo/

该实践的核心不是“Claude 比其他模型更懂 EBS”，而是：

1. 将 EBS custom extensions / integrations 纳入结构稳定的 monorepo；
2. 把表 DDL、PL/SQL 包、视图、FNDLOAD、部署脚本等放在可预测路径；
3. 用根级和项目级 `CLAUDE.md` 固化 schema、对象、命名、日志、部署等团队规则；
4. Agent 每次工作时读取这些上下文；
5. 仓库先承担主要上下文源，不必为了理解代码就给 Agent 数据库凭据。

### 证据边界

这是 JMJ Cloud 自己的实践/方法论，属于 `author self-practice`，不是独立第三方对照实验。它能证明“这种工作方式如何落地”，不能证明“Claude Code 是 EBS 的最佳工具”或其效果数字可外推为行业事实。

## 4. 相邻 practitioner 证据

Cloud Nueva 的开发者记录了 GitHub Copilot 在 PL/SQL/ORDS 开发中的实际使用，并涉及 EBS sales-order 相关 ORDS 开发：

https://blog.cloudnueva.com/vibe-coding-an-apex-deployment-tool-in-python-using-github-copilot

它支持更谨慎的判断：主流 Coding Agent 已能帮助 PL/SQL 日常开发，但收益随任务变化，也不会自动获得 EBS 项目语义。

Oracle Forum 上的 EBS 维护人员也有寻找更适合 Oracle SQL/PLSQL AI assistant 的真实需求，但该帖子没有形成足够强的采用证据，只作为 demand/coverage signal：

https://forums.oracle.com/ords/apexds/post/any-ai-code-assistant-tool-for-oracle-ebs-developement-4410

## 5. 原始 / 官方能力核验

### Oracle E-Business Suite Developer's Guide

https://docs.oracle.com/cd/E26401_01/doc.122/e22961/index.html

官方资料包含 coding standards、standard development environment、EBS application framework、R12.2 online patching/customization preparation 等内容。

含义：EBS 定制开发存在必须进入 AI 工作上下文的正式产品规范，不能只依赖模型的 PL/SQL 常识。

### GitHub Copilot repository custom instructions

https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions

当前 GitHub 支持 repository-wide、path-specific 和 agent instructions。这说明“把 EBS 团队开发规范工程化进仓库上下文”不是 Claude Code 专属技巧，可以迁移到不同 Coding Agent。

### Oracle Code Assist

https://www.oracle.com/cn/application-development/code-assist/

Oracle 当前将其描述为面向 Java、SuiteScript、PL/SQL 和 OCI application development 优化的 AI code companion，并支持组织代码库/开发规范定制。

但当前公开信息不足以证明它对 Oracle E-Business Suite custom development 比成熟通用 Coding Agent + EBS context 有稳定、可重复的采用优势，因此本轮不把它作为默认答案。

## 6. 优先推荐实践：EBS Context Engineering + Coding Agent

```text
EBS 版本 / 模块 / 真实需求
→ 将 custom code / DDL / interfaces / deployment scripts 纳入版本库
→ 固化团队开发规则与对象地图（CLAUDE.md / AGENTS.md / copilot instructions 等）
→ 加入必要的 Oracle EBS 官方开发规范/引用
→ Coding Agent 基于仓库上下文分析、生成或修改小范围代码
→ 输出代码 + 假设 + 影响范围 + 测试/部署说明
→ 在非生产环境编译、测试、回归
```

这套实践的价值在于直接解决稳定瓶颈：**项目上下文缺失**。它还能跨 Claude Code、Codex、Copilot 等 Agent 迁移；模型变化后，团队沉淀的代码结构、规范和引用仍然有效。

## 7. 何时才升级到更重的 Tool / MCP / 系统连接

只有真实瓶颈变成以下问题时，再考虑更重能力：

- 必须实时读取数据库对象、元数据或执行计划；
- 关键 EBS 系统事实不在仓库/文档中；
- 代码库很大，普通 repo exploration 已成为明确瓶颈；
- 需要受控的系统查询/调试，而不仅是生成代码；
- 数据、源码、凭据与企业权限允许对应连接方式。

理解/生成阶段默认不因为“AI 能连接数据库”就授予数据库写权限。

## 8. 不推荐的做法

- 只问“哪个 AI 最懂 EBS”，然后频繁换模型；
- 只贴一段 PL/SQL，却不给版本、对象关系、团队规范和调用上下文；
- 把模型生成的“完整代码”当成可直接上线代码；
- 为了获得更多上下文直接给生产数据库或 APPS 高权限凭据；
- 把 Oracle Code Assist 的 PL/SQL 优化能力等同于 EBS 专用能力。

## 9. 给用户的最小 Curator 输出

> **先别急着找“EBS 专用 AI”。当前更值得借鉴的是把 EBS custom code、DDL、接口、部署脚本和团队规范集中成 Agent 可读的项目上下文，再用成熟 Coding Agent 工作。JMJ Cloud 提供了一个直接 EBS 落地案例，但它是作者自实践，不是独立对照证明；Oracle 官方 Developer's Guide 应作为规范源。Claude Code/Codex/Copilot 都可以承载这种模式。Oracle Code Assist 可以继续关注，但目前公开证据不足以证明它应该取代这套方法成为默认选择。**

## 10. 0.7.0 re-review

按 0.7.0 重新检查 current baseline、capability gap、adoption cost、来源角色和 high-evidence wording 后：

- B 仍成立：问卷中的 baseline 是把需求拆开交给通用 AI 再人工整合，持久项目上下文仍是明确缺口；
- 推荐重点是 Context Engineering 方法，不把 Claude/Codex/Copilot 任一工具写成 universal winner；
- JMJ Cloud 明确保持 `author self-practice`，Oracle/GitHub 页面只承担 implementation/current-fact 角色；
- 更重 DB/MCP 连接只在真实系统访问成为瓶颈时升级，默认不授予写权限。

因此 recommendation stable，无需重跑工具排行榜式搜索。

## 11. Evidence boundary

已完成：真实问题重构、直接 EBS author self-practice、相邻 practitioner evidence、Oracle 官方规范、当前 Coding Agent 上下文能力与 Oracle Code Assist 边界核验。

尚未证明：真实用户采用、节省开发时间、减少缺陷/返工或优于普通 AI/自搜索。这些只能来自后续 `REAL_USER_USE` 反馈。
