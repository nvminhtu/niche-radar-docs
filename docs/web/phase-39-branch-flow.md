# Phase 39 · Quy trình nhánh

> Khoá `main`: chỉ vào được qua PR có CI xanh. Mỗi phase một **nhánh** (bản sao code để làm riêng), xong mới gộp và
> gắn tag. Ghi hết cách làm vào [Quy trình build](../quy-trinh-build.md).

<span class="chip chip--todo">Chưa làm · sau Phase 38</span>

## Chạy thế nào

```mermaid
flowchart LR
  N[Nhánh phaseN-tên<br/>cắt từ main] --> P[Pull request]
  P --> C[CI xanh<br/>Phase 36]
  C --> M[Merge main<br/>anh đồng ý]
  M --> T[Gắn tag<br/>anh đồng ý]
  T --> R[Bản mới<br/>Phase 37–38]
```

## Làm gì

| | |
|---|---|
| :material-shield-lock: **Bảo vệ `main`** | không đẩy thẳng lên `main`, phải qua PR + CI xanh |
| :material-source-branch: **Mỗi phase một nhánh** | tên `phaseN-<tên>` như bước Implement đang ghi |
| :material-file-document-edit: **Quy trình build** | thêm mục nhánh → PR → tag → release vào `quy-trinh-build.md` |
| :material-check-decagram: **Chạy thử 1 vòng** | lấy 1 phase thật đi đủ vòng để kiểm quy trình |

<div class="box box--star" markdown>
**Xong khi**

- 1 phase thật đi đủ vòng nhánh → PR → CI → merge → tag → bản mới
- Thử đẩy thẳng lên `main` → GitHub từ chối
- Trang Quy trình build có mục nhánh, PR, tag, release và vẫn qua `docs:build --strict`
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tự động merge PR
- Claude tự merge hoặc gắn tag khi anh chưa đồng ý
- Tính năng mới cho app
</div>

[Tổng quan Version 7](version-7.md)
