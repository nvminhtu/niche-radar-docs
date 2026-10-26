# Niche Radar Phase 47 — Chọn 2 kênh — Implementation Plan

> **For agentic workers:** phase **chấm + chọn**, không code, không đăng. Steps dùng checkbox (`- [ ]`). Anh duyệt.

**Goal:** chấm ICE từng kênh rồi chọn **đúng 2 kênh chính** làm đều tay 6 tuần.

**Spec:** [Phase 47 · Chọn 2 kênh](../../web/phase-47-two-channels.md) · **Cần trước:** Phase 46 (`marketing/gtm.md` có định vị).

## Mục tiêu · làm · không làm

- **Xong khi:** bảng ICE đủ mọi kênh ứng viên, mỗi điểm có lý do, Confidence có link · đúng 2 kênh `chính`, mỗi kênh có tần suất · dạng bài · ai làm · anh duyệt.
- **Làm:** liệt kê kênh (6 + thêm nếu có bằng chứng), chấm ICE trong `marketing/gtm.md`, chọn 2 chính + 1 dài hạn, nhịp mỗi kênh, danh sách sub nếu chọn Reddit.
- **Không làm:** > 2 kênh chính · đăng bài · chấm theo cảm giác · quảng cáo / mua follow.

## Global Constraints

- Chấm theo `references/channels.md` của `/app-gtm`; Confidence = link indie **cùng ngách** (tool cho dev / indie) thắng ở kênh đó, kèm ngày đọc.
- Điểm = I × C × E (1–5 mỗi ô), ghi lý do 1 dòng / ô.
- Kết quả nằm trong mục `## Chọn kênh` của `marketing/gtm.md`; `check_gtm.py` phải qua phần này.
- Reddit: `marketing/reddit/subs.md` — mỗi sub: luật tự quảng bá (link luật), ngày đọc; giọng theo `/app-reddit`.

## File đụng tới

- `marketing/gtm.md` — bảng ICE + chọn + nhịp
- `marketing/reddit/subs.md` (nếu chọn Reddit) — danh sách sub + luật
- `docs/web/phase-47-two-channels.md` — tóm tắt kết quả

## Tasks

### Task 1: Liệt kê + bằng chứng
- [ ] 6 kênh (X build in public, Reddit, Indie Hackers, Product Hunt, YouTube, SEO blog) + kênh khác có bằng chứng; mỗi kênh tìm ≥ 1 link Confidence.

### Task 2: Chấm + chọn
- [ ] Điền ICE, chọn 2 `chính` + 1 `dài hạn` + `phụ` / `bỏ` có lý do. `check_gtm.py` qua phần này.

### Task 3: Nhịp
- [ ] Mỗi kênh chính: bài / tuần, dạng bài, ai làm (Claude soạn, anh đăng). Reddit → `subs.md`.
- [ ] Anh duyệt. Chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
