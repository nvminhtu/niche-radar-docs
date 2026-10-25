---
hide:
  - navigation
  - toc
---

# niche-radar — Master Plan

> Gõ một niche → biết **keyword nào còn trống**, **đối thủ yếu ở đâu**, **nhu cầu lên hay xuống**.

Tool nội bộ để chọn niche cho app của mình. Tra Google Play, App Store, Google Trends, TrustMRR — Phase 1–5 không cần AI, không tốn phí; AI vào ở Phase 4 (tuỳ chọn) và Phase 6.

<div class="nr-stats" markdown>
<div><b>100</b><span>keyword mỗi lần explore</span></div>
<div><b>~6 phút</b><span>cho 100 keyword đủ số liệu</span></div>
<div><b>3</b><span>nguồn: Play · App Store · Trends</span></div>
<div><b>0 đ</b><span>Phase 1–5: không AI, không API trả phí</span></div>
</div>

<div class="box box--star" markdown>
**Theo dõi tiến độ:** trang này là bản nội bộ — mở nhanh ở
[nvminhtu.github.io/niche-radar-docs](https://nvminhtu.github.io/niche-radar-docs/). Chip ở mỗi phase và màu ở menu
trái (xanh = xong, vàng = đang làm) là trạng thái thật.
</div>

## Thứ tự: Web Version 1–9 → App Mac → Web Version 10–12

<div class="nr-forms" markdown>
<div class="nr-web" markdown>
### :material-web: 1 · Web — làm trước, làm hết

- Code ở `web/` · chạy: `npm run dev` → mở `localhost:3200`
- Version 1 → 9: nguồn dữ liệu, AI, so sánh, SEO / GEO, tốc độ, test, CI, bảo mật, tài khoản
- Sau App Mac: Version 10 → 12 — bán Pro, marketing, tính năng mới
- <span class="chip chip--doing">Đang làm · Phase 7 · tiếp theo 9b → 10–25</span>
- [Mở lộ trình Web →](web/index.md)
</div>
<div class="nr-app" markdown>
### :material-apple: 2 · App Mac — làm khi xong Version 9

- **Bọc lại đúng giao diện Web** bằng Tauri → không viết 2 lần · code ở `app/`
- Gói một lần khi bản Web **xong Version 9** (Phase 1–63): 72 → 73 → 74 → 75 → 76 → 77 → 78 → 79
- <span class="chip chip--todo">Chờ xong Version 9 · Phase 72 đã có .dmg từ trước</span>
- [Mở lộ trình App →](app/index.md)
</div>
</div>

## Chạy thế nào

```mermaid
flowchart LR
  U([Bạn gõ niche]) --> UI[Web / App Mac<br/>giao diện]
  UI --> API[Máy chủ nhỏ<br/>chạy trong máy]
  API --> P[Google Play]
  API --> S[App Store]
  API --> G[Google gợi ý]
  API --> T[Google Trends]
  P & S & G & T --> DB[(Lưu lại<br/>SQLite)]
  DB --> R[Cây keyword · Bản đồ ngách<br/>Top cơ hội · CSV]
```

Mọi thứ chạy trong máy bạn. Tra lại cùng niche trong 24 giờ lấy từ bộ nhớ, không gọi lại.
Chi tiết: [Hệ thống chạy thế nào](he-thong.md).

## Lộ trình tóm tắt

| Mục | Version | Nội dung | Phase | Trạng thái |
|---|---|---|---|---|
| Web | 1 · MVP | Google Play, App Store, Trends, Feature Gap, AI, validate · làm kỹ tính năng chính (10–25) · so sánh niche, UI, tài khoản, setup, tutorial | 1–9b, 10–25, 26–28.2 | <span class="chip chip--doing">Đang làm</span> |
| Web | 2 | Nguồn mới + AI: YouTube, Amazon, Google Maps | 29–33 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 3 | So sánh đối thủ + AI Cite (so sánh niche dời lên V1) | 35–38 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 4 | Kệ Google, kệ AI, gói GEO | 39–43 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 5 | Performance | 44–46 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 6 | Automation test + review kết quả | 48–51b | <span class="chip chip--todo">Chưa làm</span> |
| Web | 7 | CI cho PR + quy trình nhánh | 52, 55 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 8 | Security, tài khoản trên máy, refactor | 56–59 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 9 | Firebase, Analytics, sync project | 60–63 | <span class="chip chip--todo">Chưa làm</span> |
| App | sau Version 9 | Local App 1.0 → 4.0, app nhẹ, phần riêng app, build trên CI, auto-update | 72–79 | <span class="chip chip--todo">Chờ xong Version 9</span> |
| Web | 10 | Bán Pro: lifetime / subscription | 64–67 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 11 | Marketing: định vị, landing, kênh, lịch 6 tuần | 68–71 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 12 | Tính năng mới — mới ghi plan | — | <span class="chip chip--todo">Chưa đánh số</span> |

Việc chưa xếp phase hoặc không làm: [Appendix](appendix.md). Mỗi phase đi theo [Quy trình build](quy-trinh-build.md).

## Trông như thế này

<figure class="frame" markdown>
![Bảng keyword của niche budget tracker](images/explore-table.jpg)
</figure>

<div class="box box--danger" markdown>
**Không làm (cố ý)**

- AI tự đưa ra con số — AI (Phase 4, 6) chỉ đọc chữ và trích dẫn
- Lượt tìm "thật" — store không công khai, "phổ biến" là ước lượng
- Bán / host cho nhiều người — tool nội bộ
</div>

[Bản Master Plan đầy đủ (chữ)](superpowers/specs/2026-10-24-niche-radar-master-plan.md)
