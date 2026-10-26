# Niche Radar Phase 26.7 — Chi phí AI theo gói — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` xanh rồi commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** người dùng Pro không làm chi phí AI vượt tiền họ trả: BYOK, gói lượt AI kèm Pro có trần, hoặc cả hai — theo số Phase 66.

**Spec:** [Phase 26.7 · Chi phí AI theo gói](../../web/phase-26-7-ai-cost-plans.md) · **Cần trước:** Phase 30 (% chi phí AI tối đa, trần lượt), Phase 26.6 (provider, sổ chi phí), Phase 31–68.

## Mục tiêu · làm · không làm

- **Xong khi:** 1 người Pro dùng hết trần → AI dừng, phần không AI vẫn chạy · chi phí AI tháng ≤ % doanh thu trong `money.md` (số dashboard, ghi ngày) ·
  hết lượt → 0 lần gọi AI tính tiền mình (log) · BYOK key sai → báo rõ, **không** lùi sang key của mình.
- **Làm:** chọn cách (theo `money.md`), BYOK, bộ đếm lượt + trần tháng, hiện lượt còn lại, hết lượt báo.
- **Không làm:** tự trừ tiền thêm / bán lượt lẻ · đổi giá Pro · model mới · lượt dùng chung team.

## Global Constraints

- **Gói lượt AI** cần key của mình ở **server mình**, không ở máy người dùng → proxy AI là Cloud Function `functions/src/ai-proxy.ts`
  (kiểm Firebase ID token + `entitlement` Pro + bộ đếm). Key của mình trong Secret Manager, không bao giờ xuống máy người dùng.
- **BYOK** giữ như Phase 26.6 (key trên máy, gọi thẳng provider). Hai tuyến tách bạch trong `aiAsk`: `route = 'byok' | 'pro-pool'`; BYOK lỗi key
  → lỗi rõ, không tự đổi sang `pro-pool`.
- Bộ đếm: `usage/{uid}/months/{YYYY-MM}` `{ calls, costUsd }`, tăng trong transaction **trước** khi gọi provider; vượt trần → 429 "hết lượt tháng này".
- "Lượt" = 1 việc AI (themes / summary / ask…) theo bảng quy đổi trong `money.md`, không theo token (dễ hiểu cho người dùng).
- Báo cáo chi phí tháng: Function lịch `usage-report` cộng `costUsd` vs doanh thu (Lemon Squeezy API) → ghi `reports/ai-cost/{YYYY-MM}`.

## File đụng tới

- `functions/src/ai-proxy.ts`, `usage-report.ts` (mới) — proxy có trần + báo cáo
- `web/src/lib/ai/settings.ts`, `providers.ts` — tuyến `byok` / `pro-pool`, `proPoolAsk` gọi proxy
- `web/src/lib/ai/quota.ts` (mới) — đọc lượt còn lại
- `web/src/components/AiQuota.tsx` (mới), `SettingsPage.tsx` — hiện lượt còn, chọn BYOK / pool
- `firestore.rules` — `usage` chỉ đọc với chủ
- `functions/test/ai-proxy.test.ts`, `web/tests/ai-route*.test.ts`

## Tasks

### Task 1: Chọn cách
- [ ] Theo `money.md`: BYOK / pool / cả hai — ghi vào trang phase. Chỉ BYOK → bỏ Task 2–3, giữ Task 4.

### Task 2: Proxy + bộ đếm
- [ ] `ai-proxy.ts`: token, Pro, transaction đếm, trần, gọi provider. Test: vượt trần → 429, không gọi provider (mock đếm 0 lần).

### Task 3: Client + lượt còn lại
- [ ] `proPoolAsk`, `AiQuota`, hết lượt → báo, phần không AI chạy (E2E).

### Task 4: BYOK rõ ràng
- [ ] Key sai → lỗi rõ; test không lùi sang pool.

### Task 5: Đo tháng đầu
- [ ] `usage-report` chạy; chi phí / doanh thu ≤ % trong `money.md` (ghi số + ngày; chưa đủ 1 tháng → `chưa đo`). CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
