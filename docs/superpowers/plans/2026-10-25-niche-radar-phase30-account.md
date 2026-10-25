# Niche Radar Phase 30 — Account + Flow người dùng — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). License key chỉ làm khi đã có quyết định bán (Version 10).

**Goal:** khi có **người khác** dùng tool: hồ sơ trên máy, luồng lần đầu tới quyết định không cần tài liệu, đường nhận góp ý.

**Spec:** [Phase 30 · Account + Flow](../../web/phase-30-account.md) · **Cần trước:** Phase 30.1 (Setup), Phase 29 (luồng chính đã gọn).

## Mục tiêu · làm · không làm

- **Xong khi:** 1 người ngoài cài app, tra 1 niche, gửi 1 góp ý — không hỏi anh · góp ý hiện trong danh sách Phase 9 có nhãn phân loại.
- **Làm:** hồ sơ trên máy (tên, nơi lưu dữ liệu), luồng lần đầu (onboarding nhẹ trong trang chủ), nút góp ý → file / email / issue → phân loại.
- **Không làm:** server nhiều người · sync cloud · thanh toán khi chưa quyết bán. License key (mẫu RAM Rescue) chỉ ghi khung, bật ở Phase 67–68.

## Global Constraints

- Hồ sơ = 1 dòng `settings` (`profile.name`, `profile.dataDir`), không mật khẩu, không gửi đi đâu.
- Đổi nơi lưu dữ liệu: backup trước, chép DB sang chỗ mới, kiểm (`verify` của Phase 19), rồi mới đổi `NR_DATA_DIR` qua file cấu hình.
- Luồng lần đầu: **không** tour bắt buộc (luật Phase 30.2) — trang chủ khi DB rỗng hiện 3 bước + 1 ô gõ niche mẫu.
- Góp ý: lưu file `feedback/<ulid>.json` trong thư mục dữ liệu + nút "Gửi" mở `mailto:` / trang issue GitHub với nội dung soạn sẵn
  (không tự gửi). Không kèm đường dẫn máy, key.
- Phân loại góp ý luật từ khoá: lỗi · tính năng mới · khó dùng · khác → dòng mới trong mục "Ứng viên" của trang Phase 9
  (Claude chép tay khi soát, tool chỉ xuất `.md`).

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/profile.ts` (mới) | đọc / ghi hồ sơ, đổi nơi lưu an toàn |
| `web/src/lib/feedback.ts` (mới) | lưu góp ý, phân loại, xuất `.md` |
| `web/src/server/app.ts` | `GET/POST /profile` · `POST /profile/data-dir` · `POST /feedback` · `GET /feedback.md` |
| `web/src/client/HomePage.tsx` | màn lần đầu khi DB rỗng |
| `web/src/components/FeedbackButton.tsx` (mới), `AppShell.tsx` | nút góp ý ở chân trang |
| `web/src/client/SettingsPage.tsx` | mục Hồ sơ |
| `web/tests/profile.test.ts`, `feedback.test.ts` | |

## Tasks

### Task 1: Hồ sơ + đổi nơi lưu
- [ ] `profile.ts`; đổi nơi lưu: backup → chép → verify → đổi. Test trên thư mục tạm.

### Task 2: Luồng lần đầu
- [ ] DB rỗng → 3 bước (Gõ niche · Xem kết quả · Lưu project) + niche mẫu; đếm số bấm tới khi lưu project đầu tiên.

### Task 3: Góp ý
- [ ] Nút + form ngắn (loại, mô tả, màn đang ở); lưu file; Gửi = `mailto:` / issue soạn sẵn. Phân loại + xuất `.md`. Test.

### Task 4: Người ngoài thử
- [ ] 1 người ngoài cài theo trang Setup (Phase 30.1), tra 1 niche, gửi 1 góp ý. Ghi chỗ họ vướng (không ghi tên thật).
- [ ] Góp ý vào danh sách Phase 9 có nhãn. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
