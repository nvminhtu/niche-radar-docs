# Phase 75 · Local App 2.0

> Sau khi bản Web **xong Version 10**, đóng gói phần còn lại của Version 1 (Phase 7, 9–30.2) + Version 9 (analytics) + Version 10 (dùng thử, license) vào **app Mac** một lần — như Phase 74 đã làm cho Phase 1–6. Đây là **bản bán đầu tiên**.
>
> **Đổi 2026-10-26:** Version 2 (YouTube, Amazon, Maps) không gói ở đây nữa — vào app qua bản cập nhật [Phase 81](phase-81-release-auto-update.md) khi làm xong. Bảng "Làm gì" dưới còn nhắc Phase 31–35: bỏ phần đó khi code.

<span class="chip chip--todo">Chưa làm · sau Phase 74 · khi xong Version 10</span>

## Chạy thế nào

```mermaid
flowchart LR
  W[Bản Web<br/>Phase 31–35 đã xong] --> R[Review nhanh<br/>từng phase trên 3 niche]
  R --> P[Gói vào app Mac<br/>Tauri + sidecar Node]
  P --> M[Migration DB<br/>bảng YouTube · Amazon · Maps]
  M --> B[.dmg mới<br/>ký + notarize]
  B --> U[Cập nhật<br/>máy đang dùng 1.x]
```

## Làm gì

| | |
|---|---|
| :material-check-all: **Review trước khi gói** | 3 niche thật chạy qua Phase 31–35 ở bản Web, ghi lỗi còn lại |
| :material-package-variant: **Gói vào app** | các collector mới vào sidecar; `yt-dlp` (nếu dùng) gói kèm hoặc bỏ |
| :material-database-arrow-up: **Migration DB** | bảng mới dùng ULID; mở app 1.x cũ lên 2.0 không mất dữ liệu |
| :material-key: **Cài đặt key** | YouTube Data API, Places API, AI — nhập trong app, lưu trong Keychain |
| :material-google-chrome: **Job Claude in Chrome** | xuất / nhập file job từ app (nút "Mở thư mục job") |
| :material-apple: **Phát hành** | `.dmg` mới ký + notarize, ghi What's New |

<div class="box box--star" markdown>
**Xong khi**

- App 1.x có dữ liệu thật → cài 2.0 → dữ liệu còn đủ, đếm từng bảng trước / sau
- Trên app: tra 1 niche ra đủ khối YouTube + Amazon + Maps (khối nào bị chặn thì báo đúng)
- Mở ≤ 5 giây, test xanh, bản web vẫn chạy
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tính năng tra cứu mới (chỉ gói những gì Phase 31–35 đã xong)
- Auto-update, bản Windows (xét lại khi có người dùng ngoài)
</div>

Plan code chi tiết: [Phase 75](../superpowers/plans/2026-10-25-niche-radar-phase75-local-app-2.md)
