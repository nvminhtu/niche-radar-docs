# Niche Radar Phase 30.2 — Tutorial trong Web (nút ?) — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Hình do Codex sinh (`codex_image.sh`), Claude không tự vẽ.

**Goal:** mỗi tính năng có nút **?**: 1 câu làm gì + 2–4 hình bước — xem 10 giây là hiểu.

**Spec:** [Phase 30.2 · Tutorial trong Web](../../web/phase-30-2-tutorial.md) · **Cần trước:** Phase 30.1 (`AskAi` dùng lại kiểu popover), Phase 29.

## Mục tiêu · làm · không làm

- **Xong khi:** mọi tính năng `status: 'done'` trong `features.ts` có nút ? + ≥ 2 hình bước · mỗi khung đạt luật chữ (script kiểm) ·
  1 người ngoài hiểu Explore chỉ bằng nút ? · screenshot khung ? của 3 tính năng (sáng + tối) đã Read.
- **Làm:** `HelpButton` + khung nổi, `steps` trong `features.ts`, hình Codex sinh, đánh dấu đã xem, trang Guide dùng lại.
- **Không làm:** video · tour bắt buộc · bản tiếng Anh.

## Global Constraints

- Một nguồn nội dung: `features.ts` thêm `id` (khoá ổn định) + `steps: { img: string; caption: string }[]`.
- Luật chữ: `what` ≤ 15 chữ, `caption` ≤ 10 chữ bắt đầu bằng động từ, ≤ 4 bước. Kiểm bằng **test** (`features.test.ts`) — chạy trong `npm run check`.
  Trượt luật → sửa nội dung / tính năng (ghi Phase 29), không nới luật.
- Hình: `web/public/help/<id>/01.png…`, 1 Style lock (màu app, nét ít) trong `design/help/style-lock.txt`; prompt từng hình
  ở `design/help/<id>.txt`; Codex sinh ra `design/help/raw/` → Claude mở xem, chọn, đổi tên, nén.
- Chưa có hình → khung chỉ hiện chữ.
- Đã xem lưu localStorage (try/catch); không tự bật tour.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/features.ts` | `id`, `steps`, rút gọn `what` |
| `web/src/components/HelpButton.tsx` (mới) | nút ? + khung nổi (Esc / bấm ngoài đóng, nút **Thử ngay** → `to`) |
| Các khối: `RunHeader`, `ExploreDashboard`, `ComplaintsBlock`, `GapMatrixBlock`, `AiTaskBlock`, `CollectButton`, `HealthBlock`, `SettingsPage` (Backup)… | gắn `HelpButton id=…` cạnh tiêu đề |
| `web/src/client/GuidePage.tsx` | dùng `steps` |
| `design/help/` | style lock, prompt, raw |
| `web/public/help/` | hình đã chọn |
| `web/tests/features.test.ts` | luật chữ + mọi `done` có ≥ 2 bước |

## Tasks

### Task 1: Dữ liệu + luật chữ
- [ ] Thêm `id`, viết `steps` (chữ) cho mọi tính năng `done`; test luật chữ xanh.

### Task 2: HelpButton
- [ ] Component + gắn vào mọi khối; đã xem đổi màu nhạt. Test render (khung mở / đóng).

### Task 3: Hình
- [ ] Style lock + prompt từng bước → `codex_image.sh` chạy nền → mở từng hình, chọn, đặt vào `web/public/help/<id>/`.

### Task 4: Soát
- [ ] 1 người ngoài thử Explore chỉ bằng nút ?. Screenshot khung ? 3 tính năng, sáng + tối, Read.
- [ ] Guide dùng chung nội dung. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
