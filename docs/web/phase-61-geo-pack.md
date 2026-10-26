# Phase 61 · Gói GEO + trang cần viết

> Niche đã chọn → xuất **gói GEO**: bộ câu hỏi + regex tên đối thủ đúng định dạng `scripts/geo.py` của App-AI-Skills,
> kèm **danh sách trang cần viết** để được Google và AI nhắc. Đây là cầu nối từ "chọn niche" sang "ra mắt".

<span class="chip chip--todo">Chưa làm · sau Phase 60</span>

## Chạy thế nào

```mermaid
flowchart LR
  N[Niche đã chọn] --> Q[Câu hỏi chưa ai<br/>trả lời tốt · Phase 60]
  N --> B[Tên đối thủ<br/>Phase 1–2, B01]
  Q --> T[questions.tsv]
  B --> R[brands.tsv]
  Q --> P[Trang cần viết<br/>AI Cite · Phase 26.4]
  T & R & P --> Z[geo-pack/<br/>dán vào apps/.../marketing/geo-test/]
```

## Làm gì

| | |
|---|---|
| :material-file-delimited: **`questions.tsv`** | `id · nhóm · câu hỏi`, 10–40 câu, đúng định dạng `geo.py run` |
| :material-regex: **`brands.tsv`** | `nhóm · regex tên app`, mỗi đối thủ một dòng + dòng `*` để trống cho domain của mình (điền khi có) |
| :material-file-document-edit: **Trang cần viết** | mỗi câu hỏi: loại trang nên viết (bài so sánh "X vs Y", "best app for…", hướng dẫn "how to…", trang alternative) · trang AI đang trích cho câu đó · 1 dòng lý do. Lý do viết qua lớp AI Cite Phase 26.4, có trích dẫn |
| :material-folder-zip: **Xuất** | thư mục `geo-pack/` + `README.md` ngắn ghi lệnh chạy `geo.py run` / `analyze` làm mốc trước ra mắt |

<div class="box box--rules" markdown>
**Luật**

- Định dạng file theo đúng `geo.py` hiện tại. `geo.py` đổi định dạng → sửa phase này, không sửa `geo.py` cho hợp
- Chỉ xuất gói. Không viết bài, không đăng, không tạo file trong repo App-AI-Skills thay người dùng
</div>

<div class="box box--star" markdown>
**Xong khi**

- 1 niche thật xuất gói → `python3 scripts/geo.py run <dir>` + `analyze` chạy được, không sửa tay
- Danh sách trang cần viết có ≥ 5 dòng, mỗi lý do có trích dẫn qua kiểm Phase 26.4
- Gói mở bằng `/app-geo` (Pha 1 — Bộ câu hỏi) dùng được luôn
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Viết nháp bài (việc của `/oneclicktool-blog`)
- Đo lại sau ra mắt, so mốc (việc của `/app-geo` + `geo.py compare`)
</div>

Plan code chi tiết: [Phase 61](../superpowers/plans/2026-10-25-niche-radar-phase44-geo-pack.md)
