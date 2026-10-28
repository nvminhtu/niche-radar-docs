# ShotMatic Phase 43 — Evidence pack + test bán trước — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`). Tool không tự đăng bài, không chạy quảng cáo, không thu tiền.

**Goal:** chạy **hết 1 vòng thật**: niche → evidence pack → `/app-demand` → test bán trước → số thật → BUILD / TEST THÊM / BỎ.

**Spec:** [Phase 43 · Evidence pack + test bán trước](../../web/phase-43-evidence-presell.md) · **Cần trước:** Phase 7
(`lib/evidence.ts`, `lib/validate.ts`, task AI `presale`), Phase 18, 20, 18.

## Mục tiêu · làm · không làm

- **Xong khi:** 1 niche thật đi hết vòng, quyết định đã ghi · `/app-demand` đọc evidence pack không sửa tay · Phase 7 chip → Xong.
- **Làm:** evidence pack đủ khung `templates/demand.md`, 1 bấm sang pipeline, ngưỡng khoá trước khi chạy, nhập số thật có
  nguồn, gợi ý quyết định.
- **Không làm:** landing thật để bán (Phase 46) · tạo tài khoản / đăng bài.

## Global Constraints

- Khung chuẩn = `templates/demand.md` của repo App-AI-Skills. Script so khung đọc file đó (đường dẫn trong `settings`
  `pipeline.repoDir`, không ghi đường dẫn máy vào docs); không có file → dùng bản khung chép trong `web/src/lib/demand-template.ts`.
- Ngưỡng ghi **trước**; bắt đầu test → khoá (`lockedAt`). Đổi sau khi có số → cho đổi nhưng ghi đỏ "đổi sau khi thấy số".
- Mọi số test có nguồn + ngày; thiếu → "chưa đo".
- Gợi ý chỉ là gợi ý — kết luận project do anh chốt.

## File đụng tới

- `web/src/lib/evidence.ts` — đối chiếu từng mục khung; mục thiếu "chưa đo" + link đi lấy; thêm "Ai thu tiền", lời chê, điểm + cờ
- `web/src/lib/demand-template.ts` (mới) — đọc mục của `templates/demand.md`
- `web/src/db/schema.ts` + migration mới — `validations`: `lockedAt`, `changedAfterLock`, `source`, `views`, `clicks`, `emails`, `replies`
- `web/src/lib/validate.ts` — khoá ngưỡng, ghi số có nguồn, `decision()` trả lý do
- `web/src/server/app.ts` — `GET /projects/:id/evidence.md` · `GET /projects/:id/app-demand` (lệnh copy sẵn + tên file) · `POST /research/:id/validations/:vid/lock`
- `ProjectPage.tsx`, khối Validate — nút "Làm evidence pack" + "Copy lệnh /app-demand", form ngưỡng khoá, nhập số, gợi ý + nút ghi vào kết luận
- `web/tests/evidence*.test.ts`, `validate*.test.ts`

## Tasks

### Task 1: Evidence pack đủ khung
- [ ] So mục với `templates/demand.md`; test: mọi mục có mặt (có số hoặc "chưa đo").

### Task 2: 1 bấm sang pipeline
- [ ] Ghi file vào thư mục `research/` của repo pipeline (do anh chọn ở Cài đặt) hoặc tải về; lệnh `/app-demand <file>` copy sẵn.

### Task 3: Ngưỡng khoá + số thật
- [ ] Migration + khoá; đổi sau khoá → cờ đỏ. Nhập lượt xem, click, email, trả lời + nguồn + ngày.
- [ ] `decision()` so ngưỡng → gợi ý + lý do. Test.

### Task 4: Chạy 1 vòng thật
- [ ] Anh chọn 1 niche → evidence pack → `/app-demand` đọc (không sửa tay) → anh chạy test bán trước (tay) → nhập số → quyết định.
- [ ] Ghi tóm tắt vòng (không tên app chưa ra mắt) vào trang phase. Phase 7 + 43 chip → Xong. ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Phase 7 đã code xong, chờ vòng thật.
