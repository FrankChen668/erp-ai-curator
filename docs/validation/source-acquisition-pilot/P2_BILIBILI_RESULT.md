# P2 — Bilibili Qualification

Date: 2026-08-31
Runtime under test: curating-erp-ai-resources 0.9.1 (unchanged)
Pilot branch: validation/source-acquisition-pilot-local
Candidate: `XZXZZX-Ai/bilibili-mcp`
Pinned commit: `b25b394bce0d05973a8afd7029651509bf407567`

## Pre-install inspection

The fixed-commit codeload archive was obtained and inspected in a temporary directory. No source files or binaries were copied into this repository.

Observed source surface:

- Package: `@xzxzzx/bilibili-mcp` version `1.13.1`; license `Apache-2.0`; Node requirement `>=20.0.0`.
- Runtime dependencies include `@modelcontextprotocol/sdk`, `commander`, `dotenv` and `quick-lru`; package lock is present.
- The tool schema exposes read-oriented tools for credentials/status, video info/metadata/chapters, comments, transcripts, video search, creator search, favorite-video listing and creator-content reading.
- No publish, comment-write, like, favorite-write, follow, message or upload tool was selected or invoked. The exposed comment/favorite capabilities are read/discovery paths in the inspected schema.
- Default API base is `https://api.bilibili.com`; source also accesses Bilibili video, subtitle and space URLs.
- Credential manager reads `BILIBILI_SESSDATA`, `BILIBILI_BILI_JCT`, `BILIBILI_DEDEUSERID` or the global file `~/.bilibili-mcp/config.json`; setup can write that global file.
- README requires local credential setup and client reconnection before the MCP credential check. Optional local ASR is explicitly outside this first smoke test.

## Non-credential installation and diagnostic

In the temporary pinned source directory:

```text
npm ci --ignore-scripts --no-audit --no-fund: success, 147 packages added
npm run build: success
node dist/cli.js doctor --json: success
node dist/cli.js check: success, reported credentials not configured
```

Observed diagnostic output, with no secret values:

```json
{
  "package_name": "@xzxzzx/bilibili-mcp",
  "version": "1.13.1",
  "runtime": {"node": "v24.14.1", "platform": "win32", "arch": "x64"},
  "credentials": {"configured": false, "source": "none", "loadable": false},
  "asr": {"status": "not_installed", "model": null, "device": null},
  "status": "needs_credentials"
}
```

The plain check reported:

```text
配置状态：未配置
请使用以下方法之一配置凭证：
1. bilibili-mcp setup
2. 设置环境变量
3. 创建 .env 文件
```

## Exact stop point

The next Runbook operation would require local Bilibili credential setup and then client reconnection before `check_bilibili_credentials` and the read-only search/transcript smoke test can run.

This is an Owner-local action. Per the Runbook and task boundary, execution stops here. No setup command was run, no Cookie or credential value was requested/received/displayed, no MCP client was modified or restarted, and no optional ASR was installed.

P2 proposed status for review: `CONDITIONAL`.

Reason: the source has a read-only search/transcript surface, but this run has no transcript-level evidence because credential setup and client reconnection are required. The cost and permission boundary is material and remains unresolved by this pilot.
