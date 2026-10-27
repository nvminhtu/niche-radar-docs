# App Mac + Windows · sản phẩm để bán (Phase 17, 34–37)

> **Chốt 2026-10-26:** Niche Radar đến tay khách bằng **app Mac + Windows tải về**, dùng thử rồi mua license — mô hình
> học từ [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords). Bản Web vẫn chạy local (`npm run dev`) để **test tính năng**;
> app **bọc lại đúng giao diện Web** bằng Tauri (code ở `app/`), không viết UI lần hai.
> Mọi việc riêng của app (gói, ký, Keychain, license key, Windows, auto-update) chỉ nằm ở mục này.

<span class="chip chip--todo">Làm sau Phase 33 (Version 10) · Phase 17 đã có .dmg từ trước</span>

<div class="box box--star" markdown>
**Luật thứ tự**

- Bản Web xong **Phase 1–33** (Hoàn thiện Web, AI, Version 9 analytics, Version 10 dùng thử + license) → làm App theo thứ tự
  34 → 35 → 36 → 37 → rồi Phase 38–63 vào app qua bản cập nhật (Phase 37)
- Trang phase Web **không** nhắc app; việc riêng của app chỉ ghi ở mục này
- Phase 17 (phần app của Phase 8 cũ) đã code xong + có `.dmg` (2026-10-25): giữ nguyên
- Lỗi app phát hiện giữa chừng → sửa ở `web/` nếu là lỗi giao diện / API; lỗi vỏ Tauri ghi vào [Appendix](../appendix.md)
- Đánh số lại 2026-10-26: 74 → 17 · 75 → 34 · 79 → 35 · 82 → 36 · 81 → 37 · 76, 77, 78, 80 → Backlog 18–21
- Số cũ hơn (trước 2026-10-25) để tra CHANGELOG / commit: 56 = phần app của 8 · 57 = 17 · 58 = 22b · 59 = 27b · 60 = 31 · 61 = 55b · 62 = 37 · 63 = 38
</div>

## Các phase App — làm

<div class="steps nr-phases" markdown>
<div class="step" markdown>
<span class="step__n">17</span>
<div class="step__body">
<h3>Local App 1.0 <span class="chip chip--doing">Code xong sớm · có .dmg · thử máy mới để sau</span></h3>
<p>Đóng gói bản Web thành app Mac (Tauri + sidecar Node), .dmg ký + notarize. Project + xuất / nhập ở lại Web (Phase 8).</p>
<a class="go" href="phase-17-local-app-1/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">34</span>
<div class="step__body">
<h3>Local App 2.0 — bản bán đầu tiên <span class="chip chip--todo">Chưa làm</span></h3>
<p>Gói hết Version 1 + Version 9 (analytics) + Version 10 (dùng thử, license) vào app Mac một lần, migration DB không mất dữ liệu, .dmg mới.</p>
<a class="go" href="phase-34-local-app-2/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">35</span>
<div class="step__body">
<h3>Phần riêng của app <span class="chip chip--todo">Chưa làm</span></h3>
<p>Setup trong app (tìm Claude Code / Codex), CSP + quyền Tauri, key + ngày dùng thử trong Keychain, license key, mở checkout bằng trình duyệt ngoài.</p>
<a class="go" href="phase-35-app-only/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">36</span>
<div class="step__body">
<h3>App Windows (Beta) <span class="chip chip--todo">Chưa làm · plan 2026-10-26</span></h3>
<p>Cùng app Tauri build cho Windows 11 x64: sidecar Node bản Windows, bộ cài .exe, ra Beta chưa ký như Wow Keywords, ký sau khi có đơn.</p>
<a class="go" href="phase-36-windows-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">37</span>
<div class="step__body">
<h3>Release + auto-update <span class="chip chip--todo">Chưa làm</span></h3>
<p>Build trên máy bằng 1 lệnh → .dmg + .exe lên GitHub Releases public kèm ghi chú lời thường, app tự thấy bản mới và cập nhật.</p>
<a class="go" href="phase-37-release-auto-update/">Xem chi tiết →</a>
</div>
</div>
</div>

<hr class="nr-skip-line">

## ⛔ KO LÀM — Backlog 18–21 (chốt 2026-10-26)

Không ra tiền, không thêm người dùng. Tính năng mới vào app qua bản cập nhật (Phase 37) thay vì gói theo version;
build ký trên máy bằng lệnh có sẵn thay vì CI.

<div class="steps nr-phases nr-skip" markdown>
<div class="step" markdown>
<span class="step__n">B18</span>
<div class="step__body">
<h3>Local App 3.0 <span class="chip chip--skip">Không làm · thay bằng bản cập nhật Phase 37</span></h3>
<p>Gói so sánh đối thủ + AI Cite vào app.</p>
<a class="go" href="phase-backlog-18-local-app-3/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B19</span>
<div class="step__body">
<h3>Local App 4.0 <span class="chip chip--skip">Không làm · thay bằng bản cập nhật Phase 37</span></h3>
<p>Gói kệ Google + kệ AI + gói GEO vào app.</p>
<a class="go" href="phase-backlog-19-local-app-4/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B20</span>
<div class="step__body">
<h3>App Mac nhẹ <span class="chip chip--skip">Không làm · performance</span></h3>
<p>Mở ≤ 3 giây, ít RAM, .dmg nhỏ hơn. Mốc đo 2026-10-25 đã ổn: mở ~0,14 s, RAM nghỉ ≈ 200 MB.</p>
<a class="go" href="phase-backlog-20-light-mac-app/">Xem chi tiết →</a>
</div>
</div>
<div class="step" markdown>
<span class="step__n">B21</span>
<div class="step__body">
<h3>Build app Mac trên CI <span class="chip chip--skip">Không làm · CI</span></h3>
<p>Runner macOS build + ký + notarize. Thay bằng build trên máy (`npm run mac`).</p>
<a class="go" href="phase-backlog-21-mac-build-ci/">Xem chi tiết →</a>
</div>
</div>
</div>

Build app Mac chỉ bằng `npm run mac` (ký + notarize) — xem [Cách dùng](../cach-dung.md).
