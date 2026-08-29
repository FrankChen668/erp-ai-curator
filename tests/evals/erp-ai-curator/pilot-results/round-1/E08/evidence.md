# E08 Evidence

## 使用的 prompt（原样，未改写）

> Oracle Fusion SCM 我不熟，想找 AI 辅助快速学习模块的高质量方法、教程或 prompt framework。没有好的就明确说没有。

## 是否独立上下文

是。baseline 与 with-skill 各由一个全新启动的独立子代理执行，互不共享上下文：

- baseline 代理未读取任何 Skill 文件；
- with-skill 代理先读取 `skills/erp-ai-curator/SKILL.md` 及 3 个 references 后再执行。

## 是否有 Web 能力

两组均具备并真实使用了 WebSearch + WebFetch，结果文件均含实际打开过的原始链接清单与失败记录。

## 推荐数量

| 组 | 最终推荐数 | 是否违反 0–2 契约 |
|---|---|---|
| baseline | 4（另附 1 个"补充参考"与 1 套代理自行推导的 prompt 框架） | 不适用（baseline 无此契约） |
| with-skill | 1 | 否 |

## 原始链接

**baseline**

- https://blogs.oracle.com/fusioncoe/basics-of-prompt-engineering
- https://blogs.oracle.com/fusioncoe/best-practices-for-prompts-in-ai-agent-studio
- https://terillium.com?p=58018/
- https://www.oracle.com/au/customer-success/navigator/

（补充参考，未占正式推荐位：https://www.oracle.com/ua/scm/ai/）

**with-skill**

- https://github.com/SimonKreis-Richard/oracle-fusion-docs-mcp

## 高风险题是否查当前官方

本题在 EVAL_PLAN 中主要考察 0 推荐能力，不属于高风险配置题。但两组均发生了事实核验动作：

- **baseline**：自行排查出两处时效问题 —— Oracle 官方博客中"Race to Certification 免费到 2025-10-31"已过期；2023 年的 LinkedIn prompt 清单（SCM 仅 4 条）已跨多个 Oracle 版本迭代，均主动排除。
- **with-skill**：因推荐候选涉及"安装与配置"，触发 `volatile-fact-check.md` 一次。回到 npm 官方包页面交叉核对，发现第三方 MCP 索引站（LobeHub）仍写旧的 Python `uvx` 安装命令，而仓库已于 2026-06 迁移到 npm，按"第三方与原始来源冲突时不采用第三方"处理，并在回答中提示用户勿照抄旧命令。

## 明显异常

1. **两组的"0 推荐"判断出现实质分歧**（本轮最显著差异）：
   - baseline 在正文中明确承认"专门用 AI 学 Oracle Fusion SCM 的 prompt framework 一篇都没有"，但仍推荐了 4 个**需要用户自行迁移**的资源，并额外提供了一套代理自己推导的 prompt 框架；
   - with-skill 只推荐 1 个工具（把官方文档接入 AI 的 MCP server），并主动淘汰了**最接近字面需求**的 Udemy《Oracle Fusion + AI: Functional Consultant Crash Course》，理由是"教的是用 AI 产出交付物而非学模块"+"要求 3 年以上 ERP 经验，与用户'我不熟'冲突"。
2. **两组均判定该主题在公开互联网上近乎空白**，结论方向一致，差异在于是否用"需迁移的近似资源"填补。
3. **baseline 抓取失败 3 次**：两个 Oracle MyLearn 页面为 SPA（只返回标题）、官方 PDF 返回二进制流无法解析。baseline 因此**放弃推荐 Oracle University 的两条官方学习路径**，理由是未能亲自打开原始页面确认。
4. **with-skill 无技术层失败**：10 次 WebSearch + 4 次 WebFetch 全部成功返回；失败发生在内容层面（中文侧基本只有培训机构 SEO 页）。
5. **with-skill 的推荐发生了类型替换**：用户字面要"方法 / prompt framework"，实际推荐的是 Tool（MCP server）。代理已在回答中说明替换理由（真正的瓶颈是 AI 对 Fusion 的记忆不可靠，而非不会写 prompt）。此替换是否成立，需业务 Owner 判定。
