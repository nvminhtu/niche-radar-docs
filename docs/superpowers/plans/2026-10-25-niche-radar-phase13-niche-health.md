# Niche Radar Phase 13 — Chấm sức khoẻ niche — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** điểm v2 **đọc được và tin được**: mỗi yếu tố giải thích trong 1 phút, cờ chặn rủi ro điểm không thấy, back-test
bằng niche đã biết kết quả.

**Spec:** [Phase 13 · Chấm sức khoẻ niche](../../web/phase-13-niche-health.md) · **Cần trước:** Phase 7 + 9 (`score-v2.ts`,
`score-config.ts`, `HealthBlock.tsx`), Phase 12 (lời chê theo loại — cho cờ & giải thích "Đau").

## Mục tiêu · làm · không làm

- **Xong khi:** anh giải thích được từng yếu tố của 3 niche từ màn hình · back-test ≥ 5 niche đã biết kết quả, bảng trong
  trang phase · cờ chặn bật đúng ≥ 2 niche có rủi ro thật · test xanh cho công thức + cờ · screenshot đã Read.
- **Làm:** mở từng yếu tố, nhãn độ tin, cờ chặn, ngưỡng do anh đặt, back-test, lưu điểm theo thời gian, 1 đoạn kết luận không AI.
- **Không làm:** AI tự chấm / tự quyết BUILD · so nhiều niche (Phase 28) · đo tự động trục Tiếp cận / Hợp sức.

## Global Constraints

- Điểm = tổng có trọng số của số **đang hiện**; ai cũng tính lại tay được. Yếu tố chưa đo **bỏ khỏi tổng** (không coi 0 / 5) và báo.
- Nhãn độ tin dùng 4 mức hiển thị: **đo** · **ước (proxy)** · **tự chấm** · **chưa đo** (ánh xạ từ `Factor.trust` hiện có).
  % đã đo < 60% → gợi ý tối đa TEST THÊM.
- Cờ chặn là **luật cố định** trong `web/src/lib/health-flags.ts`, mỗi cờ trả `{ key, label, reason, source }`.
- Ngưỡng BUILD / TEST THÊM / BỎ lưu ở `settings` (`score.thresholds`) kèm lịch sử `{ value, reason, date }`.
- Quyết định cuối của anh (CỔNG 1) — UI ghi rõ "gợi ý".

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/score-v2.ts` | mỗi `Factor` thêm `inputs` (số đầu vào + nguồn + ngày) và `formula` (chuỗi đọc được) |
| `web/src/lib/health-flags.ts` (mới) | 5 cờ: thương hiệu lớn ≥ 3/5 top · cần backend / tài khoản bắt buộc · tên loại bão hoà (4.3) · nội dung bản quyền · Trends giảm 2 năm |
| `web/src/lib/score-config.ts` | ngưỡng mặc định + đọc / ghi ngưỡng có lý do |
| `web/src/lib/health-summary.ts` (mới) | ghép câu kết luận từ mẫu |
| `web/src/db/schema.ts` + migration mới | `score_history` (runId, term, country, score, measuredPct, decision, flags json, takenAt) |
| `web/src/server/app.ts` | `/research/:id/health` trả thêm `flags`, `summary`; `POST /settings/score-thresholds`; `GET /scores/history?term=` |
| `web/src/components/HealthBlock.tsx` | bấm yếu tố mở chi tiết, nhãn độ tin, cờ, đoạn kết luận |
| `web/src/client/SettingsPage.tsx` | sửa ngưỡng + ô lý do + lịch sử |
| `web/src/lib/evidence.ts` | thêm đoạn kết luận + cờ |
| `web/tests/score-v2*.test.ts`, `health-flags.test.ts` | |

## Tasks

### Task 1: Giải thích từng yếu tố
- [ ] Mỗi yếu tố trong `factors()` trả `inputs[]` (`{ label, value, source, date }`) + `formula` — vd "Cạnh tranh 3/10 vì top 5 có 2 app > 100k rating".
- [ ] `HealthBlock`: bấm yếu tố → khung mở (1 cột) hiện công thức + đầu vào + link nguồn.
- [ ] Test: mỗi yếu tố có `formula` không rỗng khi `value !== null`; tổng tính lại tay khớp `scoreV2`.

### Task 2: Độ tin + yếu tố chưa đo
- [ ] Nhãn 4 mức trên từng yếu tố; điểm tổng ghi "đo N%".
- [ ] Bỏ yếu tố chưa đo khỏi tổng (chia lại theo trọng số còn lại), hiện dòng "chưa đo: …".
- [ ] < 60% đo → gợi ý không vượt TEST THÊM. Test.

### Task 3: Cờ chặn
- [ ] `health-flags.ts`: danh sách thương hiệu lớn (file luật), dò "account required / sign in / server" trong mô tả (listing cache Phase 4),
      tên loại bão hoà (dùng lại danh sách 4.3 của repo App-AI-Skills, chép vào file luật), từ khoá bản quyền, Trends 24 tháng giảm.
- [ ] Cờ ép gợi ý xuống TEST THÊM / BỎ; mỗi cờ có lý do + nguồn. Test từng cờ.

### Task 4: Ngưỡng + lịch sử điểm
- [ ] Ngưỡng ở Cài đặt, mỗi lần sửa bắt nhập lý do, lưu lịch sử.
- [ ] Migration `score_history` (backup trước); ghi 1 dòng mỗi lần chấm xong.
- [ ] Project hiện đường điểm theo thời gian (dùng `TrendLine`), nối Phase 23.

### Task 5: Kết luận không AI + back-test
- [ ] `health-summary.ts`: "Tiền rõ (3 app thu subscription), đau vừa, cạnh tranh đông; cờ: thương hiệu lớn" → evidence pack.
- [ ] Back-test ≥ 5 niche đã biết kết quả (app đã ra mắt của mình, niche đã bỏ — tên app chưa ra mắt **không** ghi vào docs,
      dùng nhãn "niche A…"). Bảng điểm vs kết quả thật vào trang phase; chỉnh trọng số mẫu nếu lệch, ghi lý do.

### Task 6: Soát
- [ ] Anh thử 3 niche: giải thích được từng yếu tố. Screenshot 1340 + 375, Read. Chip phase, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Back-test cũ (Phase 7): 5 niche 4,5–5,4 điểm, chưa niche nào ≥ 6.
