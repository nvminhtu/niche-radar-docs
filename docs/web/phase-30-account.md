# Phase 30 · Account + Flow người dùng

> Khi có **người khác** dùng tool: tài khoản, luồng từ lúc mở app tới lúc ra quyết định, và **đường nhận tính năng mới**
> từ người dùng.

<span class="chip chip--skip">Không làm · 2026-10-26</span>

<div class="box box--danger" markdown>
**Không làm (chốt 2026-10-26):** bỏ tài khoản — app bán bằng license key, dữ liệu ở máy (học Wow Keywords). Trang giữ lại để tra, không code.
</div>

## Cách chạy

```mermaid
flowchart LR
  O[Mở app lần đầu] --> A[Tài khoản<br/>hồ sơ trên máy → đăng nhập khi cần]
  A --> OB[Hướng dẫn nhanh<br/>tra niche đầu tiên]
  OB --> P[Quản lý project<br/>của từng người]
  P --> FB[Nút góp ý / xin tính năng]
  FB --> TR[Phân loại<br/>lỗi · tính năng · câu hỏi]
  TR --> P9[Vào danh sách Phase 9]
```

## Làm gì

| | |
|---|---|
| :material-account: **Tài khoản** | bắt đầu bằng hồ sơ trên máy (tên, nơi lưu dữ liệu); đăng nhập thật chỉ khi có bán / chia sẻ |
| :material-key-variant: **License key** (nếu bán) | dùng lại mẫu Lemon Squeezy của RAM Rescue — dùng thử N ngày, kích hoạt key |
| :material-routes: **Flow người dùng** | lần đầu mở → tra niche đầu tiên → xem kết quả → lưu project, không cần đọc tài liệu |
| :material-folder-account: **Quản lý project** | project của từng người, chia sẻ bằng file (Phase 8), không sync cloud |
| :material-message-plus: **Tiếp nhận tính năng mới** | nút góp ý trong app → file / email / issue → phân loại → vào danh sách Phase 9 |

<div class="box box--star" markdown>
**Xong khi**

- 1 người ngoài (không phải anh) cài app, tra 1 niche, gửi 1 góp ý — không cần hỏi anh
- Góp ý đó hiện trong danh sách Phase 9 với nhãn phân loại
</div>

<div class="box box--danger" markdown>
**Không làm**

- Server nhiều người dùng, sync cloud realtime — chỉ khi có quyết định host (Idea Lab qua test)
- Thanh toán trong tool khi chưa có quyết định bán
</div>

Plan code chi tiết: [Phase 30](../superpowers/plans/2026-10-25-niche-radar-phase30-account.md)
