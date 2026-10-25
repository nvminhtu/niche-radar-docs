# App Mac — sau khi Web xong hết

> App Mac **bọc lại đúng giao diện Web** bằng Tauri (code ở `app/`), không viết UI lần hai. Vì vậy mục này
> **chỉ bắt đầu khi mọi phase ở [mục Web](../web/index.md) đã xong** — gói một lần cho cả bản Web đã chín,
> thay vì gói lại sau mỗi version.

<span class="chip chip--todo">Chờ Web xong · Phase 8 đã có code từ trước luật này</span>

<div class="box box--star" markdown>
**Luật thứ tự**

- Web xong hết (Version 1–12) → mới làm App, theo thứ tự 8 → 17 → 22b → 27b → 31 → 37 → 38
- Số phase giữ như cũ để khớp code (`web/src/lib/features.ts`), CHANGELOG và commit cũ
- Phase 8 đã code xong + có `.dmg` (2026-10-25): giữ nguyên, phần thử trên máy mới làm khi tới lượt App
- Lỗi app phát hiện giữa chừng → sửa ở `web/` nếu là lỗi giao diện / API; lỗi vỏ Tauri ghi vào [Appendix](../appendix.md)
</div>

## Các phase App

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">8</span>
<div class="step__body">
<h3>Local App <span class="chip chip--doing">Code xong sớm · có .dmg · thử máy mới để sau</span></h3>
<p>Đóng gói Phase 1–6 thành app Mac (Tauri + sidecar Node), project, xuất / nhập giữa các máy.</p>
<a class="go" href="phase-8-local-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">17</span>
<div class="step__body">
<h3>Local App 2.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói Phase 12–16 (YouTube, Amazon, Google Maps) vào app Mac một lần, migration DB không mất dữ liệu, .dmg mới.</p>
<a class="go" href="phase-17-local-app-2/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">22b</span>
<div class="step__body">
<h3>Local App 3.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói so sánh niche / đối thủ + AI Cite (Phase 18–21) vào app, migration DB, .dmg 3.0.</p>
<a class="go" href="phase-22b-local-app-3/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">27b</span>
<div class="step__body">
<h3>Local App 4.0 <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói kệ Google + kệ AI + gói GEO (Phase 23–26), key trong Keychain, .dmg 4.0.</p>
<a class="go" href="phase-27b-local-app-4/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">31</span>
<div class="step__body">
<h3>App Mac nhẹ <span class="chip chip--todo">Chưa làm</span></h3>
<p>Mở ≤ 3 giây, ít RAM khi rảnh, sidecar Node + .dmg nhỏ hơn — đo so với mốc Phase 28.</p>
<a class="go" href="phase-31-light-mac-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">37</span>
<div class="step__body">
<h3>Build app Mac trên CI <span class="chip chip--todo">Chưa làm</span></h3>
<p>Runner macOS build Tauri + sidecar, ký Developer ID, notarize bằng secret.</p>
<a class="go" href="phase-37-mac-build-ci/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">38</span>
<div class="step__body">
<h3>Release + auto-update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gắn tag → .dmg lên GitHub Releases kèm What's New, app tự thấy bản mới.</p>
<a class="go" href="phase-38-release-auto-update/">Xem chi tiết →</a>
</div>
</div>
</div>

Build app chỉ bằng `npm run mac` (ký + notarize) — xem [Cách dùng](../cach-dung.md).
