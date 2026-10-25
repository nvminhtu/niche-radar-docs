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

## Thứ tự: Web xong hết → mới tới App

<div class="nr-forms" markdown>
<div class="nr-web" markdown>
### :material-web: 1 · Web — làm trước, làm hết

- Code ở `web/` · chạy: `npm run dev` → mở `localhost:3200`
- Version 1 → 12: nguồn dữ liệu, AI, so sánh, SEO / GEO, tốc độ, test, CI, bảo mật, tài khoản, bán Pro, marketing
- <span class="chip chip--doing">Đang làm · Phase 7, 9–11.2 tiếp theo</span>
- [Mở lộ trình Web →](web/index.md)
</div>
<div class="nr-app" markdown>
### :material-apple: 2 · App Mac — Version 13, phase cuối cùng

- **Bọc lại đúng giao diện Web** bằng Tauri → không viết 2 lần · code ở `app/`
- Gói một lần cho bản Web đã chín, **sau mọi phase tính năng**: Phase 56 → 57 → 58 → 59 → 60 → 61 → 62 → 63
- <span class="chip chip--todo">Chờ Web xong · Phase 56 đã có .dmg từ trước</span>
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
| Web | 1 · MVP | Google Play, App Store, Trends, Feature Gap, AI, validate, UI, tài khoản, setup, tutorial | 1–9, 18, 10–11.2 | <span class="chip chip--doing">Đang làm</span> |
| Web | 2 | Nguồn mới + AI: YouTube, Amazon, Google Maps | 13–17 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 3 | So sánh đối thủ + AI Cite (so sánh niche dời lên V1) | 19–22 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 4 | Kệ Google, kệ AI, gói GEO | 23–27 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 5 | Performance | 28–30 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 6 | Automation test + review kết quả | 32–35b | <span class="chip chip--todo">Chưa làm</span> |
| Web | 7 | CI cho PR + quy trình nhánh | 36, 39 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 8 | Security, tài khoản trên máy, refactor | 40–43 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 9 | Firebase, Analytics, sync project | 44–47 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 10 | Bán Pro: lifetime / subscription | 48–51 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 11 | Marketing: định vị, landing, kênh, lịch 6 tuần | 52–55 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 12 | Tính năng mới — mới ghi plan | — | <span class="chip chip--todo">Chưa đánh số</span> |
| App | 13 · cuối cùng | Local App 1.0 → 4.0, app nhẹ, phần riêng app, build trên CI, auto-update | 56–63 | <span class="chip chip--todo">Chờ Web xong</span> |

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
