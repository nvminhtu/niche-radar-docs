# Niche Radar Phase 31 — Mô hình tiền — Implementation Plan

> **For agentic workers:** phase **đo + viết**, không code thanh toán. Steps dùng checkbox (`- [ ]`). Không bịa giá, không hứa doanh thu.
> Anh duyệt `money.md` — Claude không tự ghi `Approved`.

**Goal:** chốt Free gồm gì, Pro gồm gì, lifetime / subscription / cả hai, giá bao nhiêu — mọi số có nguồn.

**Spec:** [Phase 31 · Mô hình tiền](../../web/phase-31-money-model.md) · **Cần trước:** Phase 29 (phễu GA4), Phase 27.6 (sổ chi phí AI), Phase 27.4, 57, 60 (log AI thật).

## Mục tiêu · làm · không làm

- **Xong khi:** `money.md` có bảng gói, giá, lý do từng số kèm nguồn · mỗi giá đối thủ có link + ngày · chi phí AI trung bình / niche từ log thật ·
  ghi % doanh thu tối đa cho chi phí AI (Phase 27.7 dùng) · anh duyệt.
- **Làm:** đo giá đối thủ, đo chi phí AI, đọc phễu, chọn mô hình + độ dài dùng thử, viết `money.md` theo `/app-money`.
- **Không làm:** tạo sản phẩm Lemon Squeezy / code thanh toán · khoá lại tính năng đã Free · gói team, mã giảm giá, affiliate.

## Global Constraints

- `money.md` đặt `docs/money.md` (nội bộ — **không** sync sang repo docs public: thêm vào danh sách bỏ của `scripts/sync.py` ở repo docs,
  hoặc để ở `context-ai/` ngoài `docs/`). Khung theo template `money.md` của App-AI-Skills (`/app-money`), chạy checker của repo đó nếu khớp được.
- Giá đối thủ: tool nghiên cứu niche / keyword / app (vd. Sensor Tower, Appfigures, AppTweak, Exploding Topics, Gummysearch-kiểu, vidIQ…) —
  mở trang giá chính chủ, ghi gói + giá + chu kỳ + link + ngày. Không thấy giá công khai → `chưa đo`.
- Chi phí AI / niche = trung bình `ai_calls.costUsd` theo `runId` trên ≥ 10 niche thật (sổ chi phí Phase 27.6), tách theo việc.
- Luật store / Lemon Squeezy: không gọi subscription là quyên góp; chu kỳ ≥ 7 ngày; có Restore — ghi sẵn cho Phase 68.

## File đụng tới

- `money.md` (chỗ chốt ở trên) — bảng gói, giá, dùng thử, số máy / license, % chi phí AI tối đa, lý do + nguồn
- `docs/web/phase-31-money-model.md` — tóm tắt (không số nội bộ nhạy cảm nếu sync public)
- `scripts/ai-cost-report.ts` (mới) — in chi phí AI / niche từ DB

## Tasks

### Task 1: Đo giá đối thủ
- [ ] ≥ 8 tool, mỗi dòng gói · giá · chu kỳ · link · ngày.

### Task 2: Đo chi phí AI
- [ ] `ai-cost-report.ts` trên DB thật: trung bình, p90 / niche, theo việc.

### Task 3: Đọc phễu
- [ ] Phễu GA4 30 ngày: % qua từng bước; tính năng nào giữ người (ghi số + ngày; chưa đủ dữ liệu → `chưa đo`).

### Task 4: Viết money.md
- [ ] Free / Pro, lifetime và / hoặc subscription, giá, dùng thử N ngày, số máy / license, % chi phí AI tối đa, mỗi số có lý do + nguồn.
- [ ] Anh duyệt. Chip, ROADMAP, CHANGELOG (Docs).

## Tiến độ

- 2026-10-25: viết plan.
