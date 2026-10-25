# App Mac · làm khi xong Version 9 (Phase 74–81)

> App Mac **bọc lại đúng giao diện Web** bằng Tauri (code ở `app/`), không viết UI lần hai. Vì vậy mục này
> **chỉ bắt đầu khi [bản Web](../web/index.md) xong Version 9** (Phase 1–65: đủ nguồn, AI, so sánh, SEO / GEO,
> tốc độ, test, CI, bảo mật, tài khoản) — gói một lần cho bản Web đã chín, thay vì gói lại sau mỗi version.
> Mọi việc riêng của app (gói, ký, CSP, Keychain, deep link, license key, CI build, auto-update) chỉ nằm ở mục này.

<span class="chip chip--todo">Chờ xong Version 9 · Phase 74 đã có code từ trước luật này</span>

<div class="box box--star" markdown>
**Luật thứ tự**

- Bản Web xong **Version 1–9** (tới Phase 65) → làm App theo thứ tự 74 → 75 → 76 → 77 → 78 → 79 → 80 → 81 → rồi mới làm tiếp Web **Version 10–12** (bán Pro, marketing, tính năng mới); tính năng của Version 10–12 vào app qua bản cập nhật (Phase 81)
- Trang phase Web **không** nhắc app; việc riêng của app chỉ ghi ở mục này
- Phần riêng của app (setup trong app, CSP Tauri, Keychain, deep link, license key…) gom ở Phase 79; phần Pro (license key, khôi phục mua, lượt AI) làm khi tới Version 10
- App là **Phase 74–81** (trước gọi là Version 13) — số giữ nguyên dù làm trước Version 10. Số cũ (trước 2026-10-25) để tra CHANGELOG / commit: 56 = phần app của 8 · 57 = 17 · 58 = 22b · 59 = 27b · 60 = 31 · 61 = 55b · 62 = 37 · 63 = 38
- Phase 74 (phần app của Phase 8 cũ) đã code xong + có `.dmg` (2026-10-25): giữ nguyên, thử trên máy mới khi tới lượt App
- Lỗi app phát hiện giữa chừng → sửa ở `web/` nếu là lỗi giao diện / API; lỗi vỏ Tauri ghi vào [Appendix](../appendix.md)
</div>

## Các phase App

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">74</span>
<div class="step__body">
<h3>Local App 1.0 <span class="chip chip--doing">Code xong sớm · có .dmg · thử máy mới để sau</span></h3>
<p>Đóng gói bản Web thành app Mac (Tauri + sidecar Node), .dmg ký + notarize. Project + xuất / nhập ở lại Web (Phase 8).</p>
<a class="go" href="phase-74-local-app-1/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">75</span>
<div class="step__body">
<h3>Local App 2.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói phần còn lại của Version 1 (Phase 7, 9–28.2) + Version 2 (YouTube, Amazon, Google Maps) vào app Mac một lần, migration DB không mất dữ liệu, .dmg mới.</p>
<a class="go" href="phase-75-local-app-2/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">76</span>
<div class="step__body">
<h3>Local App 3.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói so sánh đối thủ + AI Cite (Phase 37–39) vào app, migration DB, .dmg 3.0.</p>
<a class="go" href="phase-76-local-app-3/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">77</span>
<div class="step__body">
<h3>Local App 4.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói kệ Google + kệ AI + gói GEO (Phase 41–44), key trong Keychain, .dmg 4.0.</p>
<a class="go" href="phase-77-local-app-4/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">78</span>
<div class="step__body">
<h3>App Mac nhẹ <span class="chip chip--todo">Chưa làm</span></h3>
<p>Mở ≤ 3 giây, ít RAM khi rảnh, sidecar Node + .dmg nhỏ hơn — đo so với mốc Phase 46.</p>
<a class="go" href="phase-78-light-mac-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">79</span>
<div class="step__body">
<h3>Phần riêng của app Mac <span class="chip chip--todo">Chưa làm</span></h3>
<p>Việc chỉ app mới có, tách từ Phase 30.1, 58, 62, 67–69: setup trong app, CSP + quyền Tauri, Keychain, đăng nhập qua deep link, license key, khôi phục mua, lượt AI.</p>
<a class="go" href="phase-79-app-only/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">80</span>
<div class="step__body">
<h3>Build app Mac trên CI <span class="chip chip--todo">Chưa làm</span></h3>
<p>Runner macOS build Tauri + sidecar, ký Developer ID, notarize bằng secret.</p>
<a class="go" href="phase-80-mac-build-ci/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">81</span>
<div class="step__body">
<h3>Release + auto-update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gắn tag → .dmg lên GitHub Releases kèm What's New, app tự thấy bản mới.</p>
<a class="go" href="phase-81-release-auto-update/">Xem chi tiết →</a>
</div>
</div>
</div>

Build app chỉ bằng `npm run mac` (ký + notarize) — xem [Cách dùng](../cach-dung.md).
