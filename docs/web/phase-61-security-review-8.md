# Phase 61 · Review bảo mật + 8.0

> Tự **tấn công thử** theo phiếu Phase 58 để chắc các chỗ vá chặn được thật. Sửa chỗ hỏng, rồi ra bản 8.0 qua CI
> của Version 7.

<span class="chip chip--skip">Không làm · 2026-10-26</span>

<div class="box box--danger" markdown>
**Không làm (chốt 2026-10-26):** security / refactor — không ra tiền, không thêm người dùng. Phần bảo mật tối thiểu cho app bán (CSP, quyền Tauri, key trong Keychain) đã nằm ở [Phase 79](../app/phase-79-app-only.md). Trang giữ lại để tra, không code.
</div>

<div class="nr-review-stop" markdown>
**⏸ REVIEW PHASE — dừng lại soát.** Đối chiếu "Xong khi" của các phase trước trên niche thật, sửa lỗi xong
mới làm tiếp phase sau.
</div>

## Chạy thế nào

```mermaid
flowchart LR
  P[Phiếu Phase 58] --> A[Tấn công thử<br/>từng mục]
  A -->|lọt| F[Sửa + test]
  F --> A
  A -->|bị chặn| E[Ảnh / log<br/>làm bằng chứng]
  E --> R[Tag 8.0 → CI<br/>anh đồng ý]
```

## Các lần thử

| Thử | Mong đợi |
|---|---|
| Trang web lạ gọi API cục bộ | bị từ chối (thiếu token / `Origin` lạ) |
| Review có `<script>` | hiện ra dạng chữ, không chạy |
| Key lọt log | log không có key |

## Làm gì

| | |
|---|---|
| :material-sword-cross: **Tấn công thử** | chạy từng lần thử trên bản build, không phải bản dev |
| :material-camera: **Bằng chứng** | mỗi lần thử có ảnh hoặc log, ghi vào `security/checklist.md` |
| :material-wrench: **Sửa** | lọt chỗ nào → sửa + test → thử lại |
| :material-tag: **Ra bản 8.0** | gắn tag `v8.0.0` sau khi CI xanh ([Version 7](version-7.md)) |

<div class="box box--star" markdown>
**Xong khi**

- Mọi lần thử đều bị chặn, có ảnh / log làm bằng chứng
- Bản 8.0 cài đè 7.x không mất dữ liệu (đếm từng bảng trước / sau)
- Bản 7.x tự nhận bản 8.0 qua auto-update
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Thuê pentest bên ngoài, chứng nhận bảo mật
- Tính năng mới
- Claude tự gắn tag 8.0 khi anh chưa đồng ý
</div>

[Tổng quan Version 8](version-8.md)

Plan code chi tiết: [Phase 61](../superpowers/plans/2026-10-25-niche-radar-phase61-security-review-8.md)
