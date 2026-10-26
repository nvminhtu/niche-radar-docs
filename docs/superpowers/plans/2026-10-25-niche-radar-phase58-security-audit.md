# Niche Radar Phase 58 — Kiểm + vá bảo mật — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi mục vá xong thì `npm run check` xanh (có test giữ lại) rồi commit.
> Steps dùng checkbox (`- [ ]`). Claude không đọc, in hay đổi giá trị key của anh.

**Goal:** soát mọi chỗ đang mở theo **phiếu kiểm**, vá mục đỏ, test giữ lại — trước khi có người ngoài đăng nhập và trả tiền.

**Spec:** [Phase 58 · Kiểm + vá bảo mật](../../web/phase-58-security-audit.md) · **Cần trước:** Phase 54 (CI để chạy `npm audit`).

## Mục tiêu · làm · không làm

- **Xong khi:** mọi mục phiếu có kết quả · mục đỏ đã vá kèm test · `npm audit` không còn lỗ hổng mức cao · quét lịch sử git không thấy secret
  (thấy thì anh đổi key, ghi vào phiếu).
- **Làm:** `security/checklist.md`, token API mỗi lần mở, chặn `Origin` lạ + Host lạ (DNS rebinding), hiện chữ an toàn, Dependabot, quét secret.
- **Không làm:** pentest thuê ngoài / chứng nhận · đăng nhập qua mạng · đổi framework.

## Global Constraints

- Server chỉ nghe `127.0.0.1` (đã có). Thêm:
  - **Token**: sinh 32 byte ngẫu nhiên lúc server khởi động, nhúng vào HTML trang (meta tag) do chính server trả; client gửi header `X-NR-Token`;
    thiếu / sai → 401. Route tĩnh không cần token.
  - **Origin + Host**: chỉ nhận `Origin` = origin của app (`http://127.0.0.1:<port>` / `http://localhost:<port>` / origin Tauri ở Phase 79);
    `Host` khác `127.0.0.1|localhost:<port>` → 403 (chặn DNS rebinding).
- Hiện chữ cào về: không `dangerouslySetInnerHTML` với dữ liệu ngoài; link qua 1 hàm `safeHref()` chỉ cho `http(s)`.
- Dependabot: `.github/dependabot.yml` cho `web/`, `app/`, `mcp/`, GitHub Actions.
- Quét secret: `gitleaks` (chạy tay hoặc trong CI) trên toàn lịch sử; kết quả không in giá trị (`--redact`).
- Log: 1 hàm `redact()` dùng ở mọi chỗ ghi log lỗi AI / provider.

## File đụng tới

- `security/checklist.md` (mới) — phiếu: mục · cách kiểm · kết quả · ngày
- `web/src/server/app.ts`, `index.ts`, `lib/api-guard.ts` — token, Origin, Host
- `web/src/client/page-cache.ts` / chỗ gọi `fetch` chung — gửi `X-NR-Token`
- `web/src/lib/safe.ts` (mới) — `safeHref`, `redact`
- component hiện link / chữ cào về — dùng `safeHref`
- `.github/dependabot.yml` (mới), `.github/workflows/ci.yml` — Dependabot + bước `npm audit --audit-level=high` + gitleaks
- `web/src/demo/demo-fetch.ts` — demo không cần token
- `web/tests/security-*.test.ts`

## Tasks

### Task 1: Phiếu kiểm
- [ ] `security/checklist.md` đủ 5 nhóm (API cục bộ · key · chữ cào về · thư viện · secret trong repo), mỗi mục cách kiểm.

### Task 2: Token + Origin + Host
- [ ] Middleware trong `api-guard.ts`; client gửi token; test: thiếu token 401, Origin lạ 403, Host lạ 403, đúng → 200.

### Task 3: Chữ + link an toàn
- [ ] Grep `dangerouslySetInnerHTML` / `href={` nhận dữ liệu ngoài → sửa; test review có `<script>` hiện dạng chữ, link `javascript:` bị bỏ.

### Task 4: Thư viện + secret + log
- [ ] Dependabot, `npm audit` (vá mức cao), gitleaks lịch sử (anh đổi key nếu lộ), `redact()` cho log. Test `redact`.

### Task 5: Điền phiếu
- [ ] Mọi mục có kết quả + ngày. CHANGELOG, chip, ROADMAP.

## Tiến độ

- 2026-10-25: viết plan.
