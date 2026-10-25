# Niche Radar Phase 72 — Dogfood làm nội dung — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự. Steps dùng checkbox (`- [ ]`). Claude soạn, anh đăng. Không lộ niche của app riêng.

**Goal:** dùng chính Niche Radar làm marketing: mỗi tuần 1 báo cáo niche công khai; chạy Version 4 cho từ khoá của Niche Radar để có mốc GEO trước ra mắt.

**Spec:** [Phase 72 · Dogfood làm nội dung](../../web/phase-72-dogfood-content.md) · **Cần trước:** Phase 70 (landing + email), Phase 41–44 (kệ Google / AI, gói GEO), Phase 16 (xuất Markdown).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 báo cáo niche đăng được, mỗi báo cáo có trích dẫn từ lần chạy tool thật · mốc GEO của Niche Radar có `README-RESULT.md`
  (số `x / N` + ngày + engine) · không báo cáo nào lộ niche của app riêng.
- **Làm:** báo cáo niche hằng tuần → bài blog (`/oneclicktool-blog`, tiếng Anh) + thread kênh chính + mồi email; Version 4 cho chính nó; đo mốc GEO; việc từ khoảng trống.
- **Không làm:** trang báo cáo tự động · bịa số · tính năng mới cho báo cáo đẹp · Claude đăng bài.

## Global Constraints

- Chọn niche báo cáo: **không** nằm trong danh sách niche đang nhắm (đối chiếu `research/*` của App-AI-Skills + `scripts/private-words.txt` của repo docs) — kiểm trước khi viết.
- Báo cáo = xuất Markdown (Phase 16) + lời viết thêm; số giữ nguyên nguồn + ngày; chưa đo → `chưa đo`.
- Bài blog theo `/oneclicktool-blog` (`check_post.py`, phễu về `product: niche-radar`); ảnh blog Codex sinh.
- Mốc GEO: gói GEO (Phase 44) cho từ khoá "niche research tool", "app idea finder"… → `/app-geo` (`geo.py run` + `analyze`) →
  `marketing/geo-test/YYYY-MM-DD/README-RESULT.md`.
- Câu AI không nhắc Niche Radar → việc (trang alternative, bài how-to) ghi vào lịch Phase 73.

## File đụng tới

| File | Việc |
|---|---|
| `marketing/reports/NN-<niche>.md` (mới) | báo cáo tuần |
| repo oneclicktool.app: bài blog | qua `/oneclicktool-blog` |
| `marketing/<kênh>/NN-*.md` | thread nháp (khuôn Campaign Promo Desk) |
| `marketing/geo-test/<ngày>/` | mốc GEO |
| `marketing/gtm.md` | việc từ khoảng trống |

## Tasks

### Task 1: Mốc GEO trước
- [ ] Gói GEO cho từ khoá của Niche Radar → `geo.py run` + `analyze` → `README-RESULT.md`. Ghi việc từ khoảng trống.

### Task 2: Báo cáo tuần 1–3
- [ ] Mỗi tuần: chọn niche (kiểm không trùng danh sách riêng), chạy tool, viết báo cáo có trích dẫn.

### Task 3: Thành bài
- [ ] Mỗi báo cáo → bài blog (`check_post.py` qua) + thread nháp + mồi email; anh đăng, đánh `status: posted`.
- [ ] Chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
