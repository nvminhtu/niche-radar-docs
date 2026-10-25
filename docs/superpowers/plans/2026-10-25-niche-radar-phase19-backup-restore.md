# Niche Radar Phase 19 — Backup / restore dữ liệu — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Test chạy trên thư mục tạm (`NR_DATA_DIR`), không đụng DB thật.

**Goal:** dữ liệu **không được mất**: backup tự chạy, tự dọn, tự kiểm; restore xem trước được, lấy lại được **một project**.

**Spec:** [Phase 19 · Backup / restore](../../web/phase-19-backup-restore.md) · **Cần trước:** Phase 8 (`backupDb`,
`listBackups`, `checkDbFile`, `restoreDb`, `importBundle` trong `lib/portable.ts`).

## Mục tiêu · làm · không làm

- **Xong khi:** server chạy qua 3 ngày (giả lập giờ) → đúng 3 bản ngày, dọn đúng luật giữ · tắt server giữa lúc backup → bản
  đó trượt kiểm, gắn đỏ, DB không hỏng · xoá DB → restore bản mới nhất → đếm dòng bằng nhau · restore 1 project không
  nhân đôi · test xanh · screenshot Cài đặt → Dữ liệu đã Read.
- **Làm:** backup tự động (ngày + trước nhập / gộp / xoá hẳn), giữ 7 ngày + 4 tuần + 6 tháng, thư mục ngoài, kiểm sau backup,
  restore xem trước, restore 1 project, nén `.zip` khi ra thư mục ngoài, "Backup cuối".
- **Không làm:** backup lên cloud gắn tài khoản (Phase 63) · mã hoá backup.

## Global Constraints

- Backup bằng API backup của SQLite (`better-sqlite3` `db.backup()`), không copy file thô khi đang ghi. Ghi ra `*.partial` rồi
  đổi tên sau khi kiểm xong — bản bị ngắt giữa chừng không bao giờ trông như bản tốt.
- Kiểm: `PRAGMA integrity_check` + đếm dòng từng bảng; kết quả lưu file `.json` cạnh bản backup.
- Dọn bản thừa: đưa vào Thùng rác (macOS: `osascript`/`trash` qua hàm `moveToTrash`; nơi khác: thư mục `backups/.trash`),
  không `rm` thẳng.
- Restore luôn tạo bản an toàn trước; bản trượt kiểm không cho restore.
- Giờ lấy qua tham số `now` để test giả lập 3 ngày.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/backup/schedule.ts` (mới) | `ensureDailyBackup(db, now)` gọi lúc server khởi động + mỗi giờ; `retention(list, now)` 7/4/6 |
| `web/src/lib/backup/verify.ts` (mới) | integrity + đếm dòng → `{ ok, counts, error }` |
| `web/src/lib/portable.ts` | `backupDb` ghi `.partial` → kiểm → đổi tên; `backupBefore(reason)` gọi trước import / merge / xoá hẳn |
| `web/src/lib/backup/restore-project.ts` (mới) | mở bản cũ chỉ đọc, `exportProject` từ bản đó → `importBundle` vào DB hiện tại |
| `web/src/lib/backup/external.ts` (mới) | thư mục ngoài (lưu `settings`), nén `.zip` |
| `web/src/server/index.ts`, `app.ts` | hẹn giờ; `GET /data` thêm `lastGood`, `POST /data/backup-dir`, `GET /data/backups/:name/preview`, `POST /data/restore-project` |
| `web/src/client/SettingsPage.tsx` + `AppShell.tsx` | danh sách có nhãn đỏ / xanh, xem trước so số dòng, chọn thư mục ngoài, "Backup cuối" ở chân trang, báo vàng > 3 ngày |
| `web/tests/backup-*.test.ts` | |

## Tasks

### Task 1: Backup an toàn + kiểm
- [ ] `.partial` → `verify` → đổi tên; ghi `.json` kết quả. Test: ngắt giữa chừng (giả lập lỗi) → không có bản "tốt" mới, DB gốc nguyên.

### Task 2: Tự động + giữ có chừng
- [ ] `ensureDailyBackup` (lần chạy đầu trong ngày) + backup trước nhập gói / gộp project / xoá hẳn.
- [ ] `retention`: giữ 7 ngày + 4 tuần + 6 tháng, phần thừa vào Thùng rác. Test giả lập 3 ngày, 40 ngày, 200 ngày.

### Task 3: Xem trước + restore
- [ ] Preview: số dòng từng bảng bản chọn vs DB hiện tại + ngày.
- [ ] Restore cả DB: backup an toàn trước, chặn bản đỏ. Test: xoá DB → restore → `countRows` bằng nhau.

### Task 4: Restore 1 project
- [ ] `restore-project.ts` qua `exportProject` → `importBundle`. Test: restore project đã có → không nhân đôi (uid).

### Task 5: Thư mục ngoài + UI
- [ ] Chọn thư mục ngoài (iCloud Drive / Dropbox do anh chọn), bản ra ngoài nén `.zip`.
- [ ] Cài đặt → Dữ liệu + chân trang "Backup cuối: hôm nay 09:12 · 14 MB", báo vàng > 3 ngày không có bản tốt.

### Task 6: Soát
- [ ] Chạy kịch bản Xong khi trên thư mục dữ liệu tạm; screenshot Cài đặt → Dữ liệu 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
