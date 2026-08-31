# P3 Xiaohongshu Read-Only Qualification Result

Date: 2026-08-31
Branch: `validation/source-acquisition-pilot-p3-xiaohongshu`
Repository baseline: `origin/main` / `415623aa6451b4854719c825c379d546f27a5670`

## Proposed status

**REMOVED** — provider-level qualification outcome for `xpzouying/xiaohongshu-mcp` in this pilot. This does not claim that Xiaohongshu has no useful practitioner content; the platform capability remains an unqualified coverage gap.

Cloud owns the architecture/promotion decision. This file records local evidence only.

## 1. Scope and pin

The reviewed candidate was:

`xpzouying/xiaohongshu-mcp`

The controlled pin was:

`6fb866a7db4e3dcce8dc00a0dde07370f3b12946`

The cloud-observed `332d196854a9eac0d2b8c2c0e3d0cc43139d724c` was compared with the selected pin. The exact diff was one README change (WeChat QR image reference); no source, manifest or executable change was present. The existing Phase A evidence for `6fb866a...` was therefore retained and not repeated.

## 2. Phase A evidence retained

The existing static qualification record establishes that the candidate exposes 18 MCP tools:

- read/status or discovery: `check_login_status`, `get_login_qrcode`, `list_feeds`, `search_feeds`, `get_feed_detail`, `user_profile`, `get_my_profile`, `get_unread_count`, `list_notifications`;
- account/content mutation: `delete_cookies`, `publish_content`, `publish_with_video`, `post_comment_to_feed`, `reply_comment_in_feed`, `like_feed`, `favorite_feed`, `reply_notification`, `like_notification`.

The minimum read-only subset for this pilot is `check_login_status`, `search_feeds`, and `get_feed_detail`, with `get_login_qrcode` only for the Owner-local authentication boundary. `list_feeds`/profile and notification reads are not needed for the smoke test.

The MCP server registers the broad tool set in one server. The checked-in MCP configuration exposes the server URL but does not provide a per-tool allowlist, and no practical host-level read-only restriction was demonstrated. Therefore the write/social surface remains present even though this pilot did not invoke it. No publish, comment, reply, like, favorite, follow, message, upload, delete, edit or account operation was invoked.

The candidate uses browser automation through Go Rod and `headless_browser`. It can write a cookie/session file, a fingerprint seed, browser cache data and logs. Its browser cache is populated from `https://cdn.one-world.ai/browsers/<version>/...` and the source verifies the downloaded archive against the CDN-provided `SHA256SUMS`. The candidate's README also documents GitHub Release binaries and Docker, but neither was substituted for the exact reviewed commit.

## 3. Isolated setup evidence

- `go` was not available on the host before setup.
- No system Go, SDK, package manager, installer, PATH, registry or user-environment change was made.
- The source build used only an official `go1.24.0.windows-amd64.zip` extracted under a temporary pilot directory. The `go.dev` SHA-256 was verified before extraction:
  `96b7280979205813759ee6947be7e3bb497da85c482711116c00522e3bb41ff1`.
- Go module/build caches and both build outputs were kept under the same temporary pilot directory. The source build completed for the MCP server and login executable. No binary or cache was copied into this repository.
- The temporary login process received explicit temporary `COOKIES_PATH`, `LOCALAPPDATA`, `TEMP` and `TMP` locations. It did not reuse the user's browser profile or existing cookie file.
- The source's Windows browser asset was not an exact candidate release artifact; it was the candidate's own runtime dependency and was requested from its declared CDN. The declared Windows archive was 189,954,738 bytes.

## 4. Stop point and failure classification

The temporary login executable started successfully and reached the candidate's first-run browser preparation step. It did not reach QR display or manual authentication.

Observed sequence:

1. The candidate attempted to download its Windows browser archive to the isolated temporary cache.
2. The single-stream download remained active but progressed very slowly.
3. After approximately ten minutes, the candidate reported `context deadline exceeded (Client.Timeout or context cancellation while reading body)` and automatically began retry 2/3.
4. The temporary login process was then closed. No QR payload was read or recorded, and no login action was requested from the Owner.

This is **not** evidence that Xiaohongshu search returned no relevant content. The platform search/detail path was not reached. It is an operational/supply-chain qualification cost: the exact-pin source build required a portable toolchain, and first-run execution additionally requires a large runtime browser download whose isolated acquisition timed out in this environment. The host cannot safely widen the setup to system installation or an unverified different release binary.

## 5. Phase C result

Phase C was not executed because the run stopped before the QR/login boundary:

- login status after startup: not obtained through the adapter tool;
- keyword search: not executed;
- post/detail reads: not executed;
- candidate count and practitioner evidence: none collected;
- account content mutation: none.

Accordingly, this pilot cannot distinguish platform-level content absence, low-fit candidates, inaccessible original content, or search failure. It only establishes that this provider did not reach the required read path within the bounded isolated setup cost.

## 6. Comparison with existing evidence

| Acquisition path | Current evidence | P3 implication |
|---|---|---|
| Normal Web | Two targeted Xiaohongshu queries returned zero useful recall in P0 | Confirms the original coverage gap, not Xiaohongshu content quality |
| WeChat | Strong original-content acquisition; Cloud status remains `PILOT` | Demonstrated a materially working read/discovery path |
| Bilibili | `CONDITIONAL`; normal-Web discovery plus anonymous metadata/comments; search/transcript credential-gated | Partial enrichment exists without completing credential setup |
| Xiaohongshu provider tested here | No QR/login, search or detail evidence; broad write surface; first-run browser download timed out | Provider is proposed `REMOVED` for this qualification; no value claim about the platform |

The key question — whether Xiaohongshu produced serious practitioner evidence that changed the candidate pool, ranking, rejection reason, confidence or coverage boundary — remains unanswered. This run produced no content evidence on which to claim such an uplift.

## 7. Boundary for any future work

Do not reinstall or promote this provider from this result. A future replacement would need a smaller enforceable read-only surface, exact pinned provenance, and a proportionate isolated runtime path before any Owner-local QR action. No cookies, tokens, QR images/payloads, browser profiles, downloaded corpora or binaries are part of this repository result.
