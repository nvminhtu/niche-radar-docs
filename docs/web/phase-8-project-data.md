# Phase 8 · Project + dữ liệu chuyển máy (Web)

> Gom tra cứu thành **project** có đánh giá, và làm dữ liệu **chuyển được giữa các máy**: xuất / nhập, backup / restore.
> Phần **vỏ app Mac** (Tauri) làm cùng đợt, nay tách sang [Phase 56 · Local App 1.0](../app/phase-56-local-app-1.md) ở mục App.

<span class="chip chip--done">Xong 2026-10-25</span>

## Làm gì

| | |
|---|---|
| :material-folder-multiple: **Project** | gom run / explore thành project · trạng thái **đang xem / ứng viên / loại**, kết luận, ghi chú |
| :material-database-sync: **Dữ liệu chuyển máy được** | khoá ULID (nhập file không đụng nhau), `schema_version`, tự backup trước khi nâng DB, `NR_DATA_DIR` |
| :material-export: **Xuất / nhập** | gói project `.niche.json` · CSV từng bảng · báo cáo `.md` · nhập lại không nhân đôi |
| :material-backup-restore: **Backup / restore** | Cài đặt → Dữ liệu: backup ngay, restore, mở thư mục dữ liệu |

<div class="box box--star" markdown>
**Xong khi** (đạt 2026-10-25)

- Xuất project → nhập máy khác: số dòng bằng nhau, nhập lại không nhân đôi
- Backup → xoá DB → restore đủ · DB thật lên ULID không mất dòng (22 run · 12 explore · 1220 app)
- Test xanh, bản web `npm run dev` vẫn chạy
</div>

[Spec đầy đủ (gồm cả phần app)](../superpowers/specs/2026-10-24-niche-radar-phase8-local-app.md)
