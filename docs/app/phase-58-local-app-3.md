# Phase 58 · Local App 3.0

> Gói Phase 19–21 (Phase 18 gói ở Phase 57; đã soát ở [Phase 22](../web/phase-22-review-3.md)) vào **app Mac** một lần — như
> [Phase 57](phase-57-local-app-2.md) đã làm cho Version 2. Thuộc mục App: **chỉ làm khi hết phase Web**.

<span class="chip chip--todo">Chưa làm · sau Phase 57 · khi Web xong hết</span>

## Chạy thế nào

```mermaid
flowchart LR
  W[Bản Web<br/>Phase 18–22 đã xong] --> P[Gói vào app Mac<br/>Tauri + sidecar Node]
  P --> M[Migration DB<br/>bảng so sánh · lịch sử hỏi]
  M --> B[.dmg 3.0<br/>ký + notarize]
```

## Làm gì

| | |
|---|---|
| :material-package-variant: **Gói vào app** | màn so sánh, ô hỏi, báo cáo vào app Mac |
| :material-database-arrow-up: **Migration DB** | bảng mới (bộ so sánh, lịch sử hỏi, kết quả kiểm trích dẫn) dùng ULID. Mở app 2.x lên 3.0 không mất dữ liệu |
| :material-apple: **Phát hành** | `.dmg` 3.0 ký + notarize, ghi What's New |

<div class="box box--star" markdown>
**Xong khi**

- App 2.x có dữ liệu thật → cài 3.0 → đếm từng bảng trước / sau, không mất dòng
- Trên app: so 3 niche + hỏi 1 câu + xuất 1 báo cáo chạy được, test xanh, bản Web vẫn chạy
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tính năng mới (chỉ gói những gì Phase 18–21 đã xong)
- Auto-update ([Phase 63](phase-63-release-auto-update.md)), bản Windows
</div>
