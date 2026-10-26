# Niche Radar Phase 20 — Trang kết quả Research — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** mở trang là trả lời được **"niche này có đáng xem tiếp không"** trong 30 giây; nguồn lỗi biết ngay, chạy lại đúng nguồn đó.

**Spec:** [Phase 20 · Trang kết quả Research](../../web/phase-20-research-page.md) · **Cần trước:** Phase 12, 13, 17, 18 (số cho hàng đầu trang),
Phase 22 (cột cờ trên bảng đối thủ). **Làm sau Phase 22 dù số nhỏ hơn** — trang này sắp lại các khối mà 12–22 thêm vào;
làm trước thì phải sắp lại lần nữa.

## Mục tiêu · làm · không làm

- **Xong khi:** anh mở 3 niche, trả lời "đáng xem tiếp không" chỉ từ hàng số đầu trang (khớp với đọc cả trang) · giả lập lỗi
  từng nguồn → khối báo đúng lý do, chạy lại riêng được · đo thời gian tới khi hàng số hiện (trước / sau) · screenshot 1340 + 375 đã Read.
- **Làm:** hàng số đầu trang, sắp khối theo câu hỏi, trạng thái từng nguồn, chạy lại 1 nguồn, so lần tra trước, 4 nút đi tiếp.
- **Không làm:** nguồn mới / đổi cách tính · làm nhanh collector (Version 5) · đổi hệ giao diện (Phase 29).

## Global Constraints

- Chỉ sắp lại, gom gọn, sửa trạng thái — không đổi công thức nào (test cũ giữ nguyên xanh).
- 1 cột; bảng rộng cuộn trong khối (`overflow-x-auto`), không vỡ trang ở 375px.
- Trạng thái nguồn 4 mức: **đủ · thiếu · lỗi · bị chặn tạm**, map từ `source_jobs.errorCode` (`RATE_LIMITED` → bị chặn tạm…) trong 1 bảng ở `lib/source-state.ts`.
- Chạy lại 1 nguồn dùng `retrySource` đã có (`POST /research/:id/retry`); mở rộng cho review / listing / AI nếu chưa có.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/answer-row.ts` (mới) | 5 số: điểm v2 + gợi ý · số đối thủ đáng gờm · xu hướng 12 tháng · lời chê nặng nhất · có ai thu tiền thật |
| `web/src/lib/source-state.ts` | 4 mức + câu lý do thường ("Google chặn tạm, thử lại sau ~15 phút") |
| `web/src/lib/run-compare.ts` (mới) | tìm run trước cùng `term + country`, trả mũi tên cho số chính |
| `web/src/components/RunDashboard.tsx` | thứ tự: Có nhu cầu không → Ai đang làm → Họ bị chê gì → Ai thu tiền → Còn chỗ trống → Kết luận; khối thô gập lại |
| `web/src/components/AnswerRow.tsx` (mới) | hàng số, bấm nhảy tới khối (`id` + scroll) |
| `web/src/components/SourceBlock.tsx` | dòng nguồn + giờ lấy + trạng thái + nút chạy lại |
| `web/src/server/app.ts` | `/research/:id` trả thêm `answer`, `compare`; `retry` nhận nguồn mới |
| `web/tests/answer-row.test.ts`, `source-state.test.ts`, `run-compare.test.ts` | fixture lỗi từng nguồn |

## Tasks

### Task 1: Đo trước
- [ ] Đo thời gian tới khi khối đầu tiên có số (3 niche, `performance.now()` trong trình duyệt) → ghi "trước".

### Task 2: Hàng số đầu trang
- [ ] `answer-row.ts` + test (thiếu số → "chưa đo", không đoán). `AnswerRow` bấm nhảy khối.

### Task 3: Sắp khối + gập khối thô
- [ ] `RunDashboard` theo 6 câu hỏi; mỗi nhóm 1 tiêu đề câu hỏi; dữ liệu thô (bảng keyword đầy đủ, Trends chi tiết) gập mặc định.

### Task 4: Trạng thái + chạy lại 1 nguồn
- [ ] 4 mức + lý do thường; nút chạy lại giữ phần đã có. Test fixture: mỗi nguồn lỗi → đúng nhãn + đúng nút.

### Task 5: So lần trước + đi tiếp
- [ ] `run-compare.ts`: đối thủ mới, rating, xu hướng có mũi tên.
- [ ] Cuối trang đúng 4 nút: Collect · Explore sâu · Xuất (Phase 16) · Làm evidence pack.

### Task 6: Soát
- [ ] Đo lại thời gian → "sau". Anh thử 3 niche. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: review plan — thêm Phase 17, 22 vào Cần trước; thứ tự làm thật: sau Phase 22.
