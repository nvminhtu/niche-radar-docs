# Phase 77 · Local App 4.0

> Gói Phase 41–44 (đã soát ở [Phase 45](../web/phase-45-review-4.md)) vào **app Mac** một lần — như
> [Phase 76](phase-76-local-app-3.md) đã làm cho Version 3. Thuộc mục App: **chỉ làm khi bản Web xong Version 9**.

<span class="chip chip--todo">Chưa làm · sau Phase 76 · khi xong Version 9</span>

## Chạy thế nào

```mermaid
flowchart LR
  W[Bản Web<br/>Phase 41–45 đã xong] --> P[Gói vào app Mac<br/>Tauri + sidecar Node]
  P --> K[Key trong Keychain<br/>API tìm kiếm · Gemini]
  K --> B[.dmg 4.0<br/>ký + notarize]
```

## Làm gì

| | |
|---|---|
| :material-package-variant: **Gói vào app** | collector top 10, kệ AI, cột kệ yếu, nút xuất gói GEO |
| :material-console: **Engine trên máy** | `codex exec` / `claude -p` có trên máy thì dùng, không có thì ẩn engine đó, Gemini vẫn chạy |
| :material-database-arrow-up: **Migration DB** | bảng top 10, câu trả lời AI, điểm kệ (ULID). Mở app 3.x lên 4.0 không mất dữ liệu |
| :material-apple: **Phát hành** | `.dmg` 4.0 ký + notarize, ghi What's New |

<div class="box box--star" markdown>
**Xong khi**

- App 3.x có dữ liệu thật → cài 4.0 → đếm từng bảng trước / sau, không mất dòng
- Trên app: tra kệ Google + kệ AI cho 1 niche chạy được, test xanh, bản Web vẫn chạy
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tính năng mới (chỉ gói những gì Phase 41–44 đã xong)
- Auto-update ([Phase 81](phase-81-release-auto-update.md)), bản Windows
</div>

Plan code chi tiết: [Phase 77](../superpowers/plans/2026-10-25-niche-radar-phase77-local-app-4.md)
