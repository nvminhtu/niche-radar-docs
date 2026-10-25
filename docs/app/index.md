# Version 13 · App Mac — phase cuối cùng (56–63)

> App Mac **bọc lại đúng giao diện Web** bằng Tauri (code ở `app/`), không viết UI lần hai. Vì vậy mục này
> **chỉ bắt đầu khi mọi phase ở [mục Web](../web/index.md) đã xong** — gói một lần cho cả bản Web đã chín,
> thay vì gói lại sau mỗi version.

<span class="chip chip--todo">Chờ Web xong · Phase 56 đã có code từ trước luật này</span>

<div class="box box--star" markdown>
**Luật thứ tự**

- Mọi phase tính năng ở mục Web (Version 1–12, tới Phase 55) xong hết → mới làm App, theo thứ tự 56 → 57 → 58 → 59 → 60 → 61 → 62 → 63
- Phase Web chỉ làm phần Web; phần riêng của app (CSP Tauri, Keychain, deep link, license key…) gom ở Phase 61
- App là **Version 13, Phase 56–63** — đánh số sau mọi phase Web. Số cũ (trước 2026-10-25) để tra CHANGELOG / commit: 56 = phần app của 8 · 57 = 17 · 58 = 22b · 59 = 27b · 60 = 31 · 61 = 55b · 62 = 37 · 63 = 38
- Phase 56 (phần app của Phase 8 cũ) đã code xong + có `.dmg` (2026-10-25): giữ nguyên, thử trên máy mới khi tới lượt App
- Lỗi app phát hiện giữa chừng → sửa ở `web/` nếu là lỗi giao diện / API; lỗi vỏ Tauri ghi vào [Appendix](../appendix.md)
</div>

## Các phase App

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">56</span>
<div class="step__body">
<h3>Local App 1.0 <span class="chip chip--doing">Code xong sớm · có .dmg · thử máy mới để sau</span></h3>
<p>Đóng gói bản Web thành app Mac (Tauri + sidecar Node), .dmg ký + notarize. Project + xuất / nhập ở lại Web (Phase 8).</p>
<a class="go" href="phase-56-local-app-1/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">57</span>
<div class="step__body">
<h3>Local App 2.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói phần còn lại của Version 1 (Phase 7, 9–12.2) + Version 2 (YouTube, Amazon, Google Maps) vào app Mac một lần, migration DB không mất dữ liệu, .dmg mới.</p>
<a class="go" href="phase-57-local-app-2/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">58</span>
<div class="step__body">
<h3>Local App 3.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói so sánh đối thủ + AI Cite (Phase 19–21) vào app, migration DB, .dmg 3.0.</p>
<a class="go" href="phase-58-local-app-3/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">59</span>
<div class="step__body">
<h3>Local App 4.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói kệ Google + kệ AI + gói GEO (Phase 23–26), key trong Keychain, .dmg 4.0.</p>
<a class="go" href="phase-59-local-app-4/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">60</span>
<div class="step__body">
<h3>App Mac nhẹ <span class="chip chip--todo">Chưa làm</span></h3>
<p>Mở ≤ 3 giây, ít RAM khi rảnh, sidecar Node + .dmg nhỏ hơn — đo so với mốc Phase 28.</p>
<a class="go" href="phase-60-light-mac-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">61</span>
<div class="step__body">
<h3>Phần riêng của app Mac <span class="chip chip--todo">Chưa làm</span></h3>
<p>Việc chỉ app mới có, tách từ Phase 12.1, 40, 44, 49–51: setup trong app, CSP + quyền Tauri, Keychain, đăng nhập qua deep link, license key, khôi phục mua, lượt AI.</p>
<a class="go" href="phase-61-app-only/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">62</span>
<div class="step__body">
<h3>Build app Mac trên CI <span class="chip chip--todo">Chưa làm</span></h3>
<p>Runner macOS build Tauri + sidecar, ký Developer ID, notarize bằng secret.</p>
<a class="go" href="phase-62-mac-build-ci/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">63</span>
<div class="step__body">
<h3>Release + auto-update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gắn tag → .dmg lên GitHub Releases kèm What's New, app tự thấy bản mới.</p>
<a class="go" href="phase-63-release-auto-update/">Xem chi tiết →</a>
</div>
</div>
</div>

Build app chỉ bằng `npm run mac` (ký + notarize) — xem [Cách dùng](../cach-dung.md).
