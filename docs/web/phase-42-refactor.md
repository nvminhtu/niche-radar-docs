# Phase 42 · Refactor

> **Refactor** = dọn lại code mà không đổi cách tool chạy. Mọi nguồn dữ liệu theo một khuôn chung, file to tách nhỏ,
> code chết gỡ đi. Mục đích: lần sau thêm nguồn hay sửa lỗi nhanh hơn.

<span class="chip chip--todo">Chưa làm · sau Phase 40</span>

## Chạy thế nào

```mermaid
flowchart LR
  K[Khuôn Collector chung] --> N[Chuyển từng nguồn<br/>mỗi nguồn 1 PR]
  N --> C[CI xanh<br/>Phase 36]
  C --> N
  C --> T[Tách file > 400 dòng<br/>gỡ code chết]
  T --> V[So phiếu review<br/>trước / sau]
```

## Làm gì

| | |
|---|---|
| :material-puzzle: **Khuôn `Collector`** | tên · giới hạn gọi · cache · `fetch` · `parse`. Mọi nguồn trong `web/src/collectors/` (Play, App Store, Trends, TrustMRR…) theo khuôn này |
| :material-file-tree: **Tách file to** | file > 400 dòng tách nhỏ (hiện có `web/src/server/app.ts`) |
| :material-broom: **Gỡ code chết** | code / export không ai dùng |
| :material-shape: **Kiểu dữ liệu chung** | gom kiểu dùng chung về một chỗ |
| :material-lock: **Giữ nguyên** | không đổi API, không đổi giao diện |

<div class="box box--star" markdown>
**Xong khi**

- Test + E2E xanh
- Phiếu review kết quả ([Phase 35](version-6.md)) giữ nguyên điểm trước và sau refactor
- Thêm thử 1 nguồn giả chỉ cần 2 file: 1 file collector + 1 file test
- Không còn file nào > 400 dòng
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Đổi framework (React, Hono, Drizzle)
- Viết lại collector bằng ngôn ngữ khác
- Tính năng mới, đổi giao diện
- Refactor nhiều nguồn trong một PR
</div>

[Tổng quan Version 8](version-8.md)
