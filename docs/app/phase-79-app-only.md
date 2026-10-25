# Phase 79 · Phần riêng của app Mac (bảo mật, đăng nhập, Pro)

> Gom mọi việc **chỉ app Mac mới có** mà các phase Web 11.1, 40, 44, 49–51 đã tách ra: bản Web làm phần chung trước,
> app Mac làm phần riêng ở đây — **sau khi bản Web xong Version 9** và sau khi app đã gói đủ tính năng (Phase 74 → 76).

<span class="chip chip--todo">Chưa làm · sau Phase 78 · khi xong Version 9</span>

## Chạy thế nào

```mermaid
flowchart LR
  W[Web xong<br/>Version 1–9] --> P[App đã gói đủ<br/>Phase 74 → 76]
  P --> S[Bảo mật app<br/>CSP · quyền Tauri · Keychain]
  S --> A[Đăng nhập<br/>deep link]
  A --> K[Pro trên app<br/>license key · khôi phục · lượt]
  K --> C[Phase 80 · 81<br/>CI + release]
```

## Làm gì

> Version 10 (bán Pro) làm **sau** App, nên 3 dòng cuối (license key, khôi phục mua, BYOK + lượt AI) làm khi tới
> Version 10: bản Web xong phần Pro trước, rồi gắn vào app ở bản cập nhật.

| Việc | Tách từ |
|---|---|
| **Setup trong app** — Node + SQLite đã gói sẵn, chỉ kiểm phần tuỳ chọn (key AI, Ollama, Claude in Chrome) | [Phase 30.1](../web/phase-30-1-setup.md) |
| **CSP chặt** cho WebView Tauri · chỉ mở quyền Tauri cần · key AI giữ trong **Keychain** | [Phase 58](../web/phase-58-security-audit.md) |
| **Đăng nhập trong app** — mở trình duyệt đăng nhập (Google / Apple / email link) rồi quay lại app qua **deep link** | [Phase 62](../web/phase-62-firebase-auth.md) |
| **License key** mẫu RAM Rescue — kích hoạt khi không đăng nhập · **checkout** mở từ app | [Phase 67](../web/phase-67-payments.md) |
| Nút **Khôi phục mua** trong app | [Phase 68](../web/phase-68-paywall-trial.md) |
| **BYOK** key trong Keychain · hiện **lượt AI còn lại** trong app | [Phase 69](../web/phase-69-ai-cost-plans.md) |

<div class="box box--star" markdown>
**Xong khi**

- `.dmg` mới: CSP + quyền Tauri qua phiếu bảo mật Phase 58, key không còn trong file thường
- Đăng nhập 3 cách trên app, deep link quay lại đúng app
- Mua test → license key kích hoạt được trên app không đăng nhập · khôi phục mua chạy · lượt AI hiện đúng
- Test xanh, screenshot app đã Read
</div>

<div class="box box--danger" markdown>
**Không làm**

- Tính năng mới không có ở bản Web
- Mac App Store / thanh toán trong app của Apple
- Làm trước khi bản Web xong Version 9
</div>
