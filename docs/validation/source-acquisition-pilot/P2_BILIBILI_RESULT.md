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

## No-credential adapter-level testing

After confirming credentials were not configured, the MCP server was started via stdio JSON-RPC and each read-oriented tool was exercised against the three P0 Bilibili candidate BVIDs. No credentials, cookies, or secrets were supplied at any point.

### Tools that succeeded without credentials

**`get_video_metadata`** — returned title, duration and publication date for all three P0 Bilibili candidates. Stats (view/like/coin/favorite) and author name were absent from the no-credential response.

| BVID | Title | Duration | Pubdate |
|---|---|---|---|
| BV1xyNfe1EKP | deepseek+draw.io绘制流程图 | 420 s | 2025-02-13 |
| BV1SZ421n7Cm | 用Kimi+drawio，10 秒生成流程图，支持再编辑 | 52 s | 2024-04-22 |
| BV1PM5JzSEQx | AI+drawio+提示词一键生成高质量图 | 199 s | 2025-04-18 |

**`get_video_chapters`** — succeeded for BV1xyNfe1EKP; returned an empty chapter list (the video has no chapters). No credential error.

**`get_video_comments`** — succeeded without credentials for all three candidates, returning brief top-10 hot comments with content text. This is the most significant no-credential finding because it provides practitioner feedback not available through P0 normal-Web snippets.

Practitioner-relevant comment evidence (paraphrased, non-attributing):

- BV1xyNfe1EKP: a commenter states draw.io output looks better than Mermaid code output; another asks about Mermaid availability.
- BV1SZ421n7Cm: a commenter opines that Kimi is better at long-text processing while another tool (星火) is better for flowcharts/mind maps; another says many tools can do this and it is not particularly intelligent.
- BV1PM5JzSEQx: a commenter recognizes the generated XML as mxGraph format; another reflects that AI has advanced from drawing flowcharts to visual design within a year; a commenter asks about version differences for the edit-drawing feature.

### Tools that returned COOKIE_EXPIRED without credentials

**`search_bilibili_videos`** — returned `COOKIE_EXPIRED` for the task-relevant query `AI draw.io 流程图 产品经理 ERP`. The search capability is unavailable without Bilibili credentials.

**`get_video_info`** (subtitle/transcript summary) — returned `COOKIE_EXPIRED` for BV1xyNfe1EKP. Subtitle and transcript summary are unavailable without credentials.

**`get_video_transcript`** — returned `COOKIE_EXPIRED` for BV1xyNfe1EKP. Full transcript text is unavailable without credentials.

The adapter's own `next_steps_zh` for all three credential-gated tools consistently directs running `bilibili-mcp config` then `bilibili-mcp check`, and explicitly warns not to paste Cookie values into MCP client config files.

## Capability classification summary

| Capability | Anonymous (no credential) | Requires credential | Verified this run | Not verified this run |
|---|---|---|---|---|
| Video metadata (title/duration/pubdate) | Yes | — | Yes — 3 BVIDs | Stats/author fields absent without credentials |
| Video chapters | Yes | — | Yes — 1 BVID (empty list) | Remaining 2 BVIDs not tested for chapters |
| Video comments | Yes | — | Yes — 3 BVIDs, brief mode | Detailed mode / replies not tested |
| Video search | — | Yes (COOKIE_EXPIRED) | Verified as credential-gated | No search results obtained |
| Video info (subtitle/transcript summary) | — | Yes (COOKIE_EXPIRED) | Verified as credential-gated | No subtitle/transcript content obtained |
| Video transcript (full text) | — | Yes (COOKIE_EXPIRED) | Verified as credential-gated | No transcript text obtained |

## Evidence assessment

What the no-credential run added beyond P0:

1. **Confirmed metadata for all three P0 Bilibili candidates** — titles and durations match P0 snippets, adding structured confirmation that the P0-discovered videos are real and task-relevant.
2. **Practitioner comment evidence** — the comments provide genuine practitioner opinions about draw.io vs Mermaid, Kimi vs other tools for flowcharts, and recognition of mxGraph as the underlying format. This is real practitioner signal that was not available through P0 normal-Web recall.

What the no-credential run could not provide:

1. **No new candidate discovery** — `search_bilibili_videos` requires credentials, so the adapter could not surface Bilibili candidates beyond the three P0 already found.
2. **No transcript-level evidence** — both `get_video_info` and `get_video_transcript` require credentials. The Runbook's target measurement ("does transcript-level evidence change judgement versus P0 title/snippet evidence") could not be completed.

## Exact stop point

The remaining Runbook operations require local Bilibili credential setup and client reconnection before `search_bilibili_videos`, `get_video_info`, and `get_video_transcript` can run. This is an Owner-local action.

Per the Runbook and task boundary, execution stops here. No setup command was run, no Cookie or credential value was requested/received/displayed, no MCP client was modified or restarted, and no optional ASR was installed.

## P2 proposed status

`CONDITIONAL`

Reason: the adapter provides useful no-credential read paths (metadata confirmation, practitioner comments) that add evidence beyond P0 normal-Web recall. However, the two capabilities most likely to change the final recommendation — search (new candidate discovery) and transcript (content-level evidence) — require Owner-local credential setup that was not available within the autonomous boundary. The cost and permission boundary is material and remains unresolved by this pilot.
