# WorkBuddy / CodeBuddy 运行建议

本 Skill 不依赖 WorkBuddy，但如果首个落地运行时是 WorkBuddy / CodeBuddy，建议采用最小权限。

## 第一轮建议工具

允许：
- WebSearch
- WebFetch
- Read（仅 Skill 与资源库目录）
- Write/Edit（仅 staging、资源库、备份）
- StructuredOutput（如可用）

可选：
- Agent / 子代理：只用于并行搜索不同来源；不是必要依赖。
- Bash：默认不需要。若要运行 bundled scripts，只对白名单脚本开放，不给宽泛 Shell 权限。

## 不建议第一轮开放

- 读取用户凭证/浏览器 Cookie；
- 任意目录 Read/Write；
- 任意 Bash；
- 自动安装第三方 Skill/MCP/插件；
- 绕过登录或验证码的浏览器自动化。

## 平台说明

WebSearch/WebFetch 能否读取微信公众号、小红书、B站正文取决于平台和当前访问能力。Skill 必须按实际结果降级：

- 能读正文：content_checked；
- 只能看到搜索摘要/简介：metadata_only；
- 需要登录/验证码：human_review。

不要把“工具具有 WebFetch”误解为“所有平台都能完整爬取”。
