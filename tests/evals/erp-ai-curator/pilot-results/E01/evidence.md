# E01 Evidence

## 使用的 prompt（原样，未改写）

> 我想给 SAP/Oracle 实施顾问找能用 Claude Code 或类似 Agent 生成可编辑 draw.io 业务流程图的 AI Skill/实操资源。少而精，中文有高质量的可以优先。

## 是否独立上下文

是。baseline 与 with-skill 各由一个全新启动的独立子代理执行，互不共享上下文：

- baseline 代理未读取任何 Skill 文件；
- with-skill 代理先读取 `skills/erp-ai-curator/SKILL.md` 及 3 个 references 后再执行。

## 是否有 Web 能力

两组均具备并真实使用了 WebSearch + WebFetch，结果文件均含实际打开过的原始链接清单与失败记录。

## 推荐数量

| 组 | 最终推荐数 | 是否违反 0–2 契约 |
|---|---|---|
| baseline | 4（2 个主力资源 + 1 个官方 XML 参考 + 1 篇中文教程） | 不适用（baseline 无此契约） |
| with-skill | 2 | 否 |

## 原始链接

**baseline**

- https://github.com/jgraph/drawio-mcp
- https://github.com/jgraph/drawio-mcp/blob/main/plugins/claude-code/README.md
- https://github.com/jgraph/drawio-mcp/blob/main/shared/xml-reference.md
- https://raw.githubusercontent.com/github/awesome-copilot/main/skills/draw-io-diagram-generator/SKILL.md
- https://mdnice.com/writing/d58e907042c64da694f226ad93752030

**with-skill**

- https://github.com/jgraph/drawio-mcp
- https://github.com/github/awesome-copilot/tree/main/skills/draw-io-diagram-generator

（另有 1 个够格但需迁移的候选未占推荐位：https://dev.classmethod.jp/en/articles/claude-code-trying-out-drawio-skill-for-aws-architecture/）

## 高风险题是否查当前官方

本题命中 Skill 定义的高风险事实类别（安装与配置、版本兼容）。

- **baseline**：查阅了官方仓库与插件 README，并自行发现中文教程（2026-04-29）的安装步骤早于官方插件化重构（2026-06-26），已在文中标注过时。
- **with-skill**：明确触发 `volatile-fact-check.md`，并完成 6 项核验，其中判定第三方中文教程的安装命令（复制 SKILL.md 到 `~/.claude/skills/drawio`）已被官方 2026-06-26 重构推翻，按"第三方与官方冲突时不推荐第三方"全部排除。

## 明显异常

1. **两组均发现同一关键事实**（官方安装方式已改版），但 baseline 选择"推荐并标注过时"，with-skill 选择"排除"。这是本轮最主要的 A/B 行为差异，供业务 Owner 判断。
2. **with-skill 发现官方材料自相矛盾**：`jgraph/drawio-mcp` 的 README 写 "XML only"，而当前 SKILL.md 写"有 CLI 时优先 Mermaid"。with-skill 如实标注该不一致，未粉饰为确定结论。
3. **with-skill 排除了一个高度相关候选**（`drawio-diagrams-enhanced`，BPMN/泳道/RACI，Odoo 背景），原因是其唯一可能上游为符号链接、无法确认实体，按"识别 fork 与 upstream"原则放弃。
4. **baseline 抓取失败 1 次**（ima.qq.com 返回知识库目录页，无正文），已如实排除该候选。
5. **with-skill 抓取失败 3 次**：旧 SKILL.md 路径 404、GitHub 目录页无正文、上游为 symlink。
6. **中文侧的结论一致**：两组均未找到够格的中文原创实操，baseline 推荐了 1 篇实测中文教程（标注安装步骤过时），with-skill 未给中文资源留位。
