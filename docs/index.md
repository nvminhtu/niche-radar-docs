---
hide:
  - navigation
  - toc
---

# niche-radar — Master Plan

> Gõ một niche → biết **keyword nào còn trống**, **đối thủ yếu ở đâu**, **nhu cầu lên hay xuống**.

Chọn niche đáng làm app từ Google Play, App Store, Google Trends, Reddit, Q&A, TrustMRR — không AI vẫn chạy, AI là tuỳ chọn.
**Chốt 2026-10-26:** bán dưới dạng **app Mac + Windows tải về, dùng thử rồi mua license** (học mô hình phân phối của
[Wow Keywords](doi-thu-tham-khao.md#wow-keywords)). Bản Web vẫn chạy local để test tính năng.

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

<div class="box box--goal" markdown>
**Mới 2026-10-26 — [Plan bán app Mac + Windows (A1–A3)](app/plan-ban-app.md):** [A1](app/phase-a1-hoan-thien-web.md) gom mọi việc Web dang dở · [A2](app/phase-a2-ai-cua-ban.md) AI của bạn (Claude Code, Codex, Ollama chạy trong app, MCP, khung chat, terminal nhúng) · [A3](app/phase-a3-ai-tinh-nang.md) nút AI cho từng tính năng đã làm. Thứ tự dưới đây đã gom theo A1–A3.
</div>

## Thứ tự: Web V1 → V9 → V10 → App Mac + Windows → V11 → V2–4, V12 · ⛔ KO LÀM

<div class="nr-forms" markdown>
<div class="nr-web" markdown>
### :material-web: 1 · Web local — làm + test tính năng

- Code ở `web/` · chạy: `npm run dev` → mở `localhost:3200`
- Version 1 (đang làm) → **Version 9** analytics, bỏ Account → **Version 10** dùng thử + license key
- Sau App: Version 11 marketing → Version 2, 3, 4, 12 tính năng mới (vào app qua bản cập nhật)
- <span class="chip chip--doing">Đang làm · Phase 7 · 10 Reddit Gap chờ dữ liệu thật · 10b xong · 16 Export · 16b · 10c GitHub Gap xong → 12–27</span>
- [Mở lộ trình Web →](web/index.md)
</div>
<div class="nr-app" markdown>
### :material-laptop: 2 · App Mac + Windows — thứ để bán

- **Bọc lại đúng giao diện Web** bằng Tauri → không viết 2 lần · code ở `app/`
- Gói khi bản Web **xong Version 10**: 75 → 79 → 82 (Windows Beta) → 81 (GitHub Releases + tự cập nhật)
- Tải miễn phí → dùng thử N ngày → mua đứt → license key, 2 máy, không tài khoản
- <span class="chip chip--todo">Chờ xong Version 10 · Phase 74 đã có .dmg từ trước</span>
- [Mở lộ trình App →](app/index.md)
</div>
</div>

<div class="box box--danger" markdown>
**⛔ KO LÀM (chốt 2026-10-26)** — không ra tiền, không thêm người dùng: **Account** (Phase 30, 59, 62, 63) ·
**Version 5** Performance · **Version 6** test tự động · **Version 7** CI · **Version 8** security / refactor ·
App 76, 77, 78, 80. Trang giữ lại để tra. [Danh sách + lý do](appendix.md#khong-lam-chot-2026-10-26)
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
| Web | 1 · MVP | Google Play, App Store, Trends, Feature Gap, AI, validate · Reddit / Q&A Gap · làm kỹ tính năng chính (12–27) · so sánh niche, UI, setup, tutorial | 1–11, 12–27, 28, 29, 30.1, 30.2 | <span class="chip chip--doing">Đang làm</span> |
| Web | 9 | Analytics + báo lỗi + trang Riêng tư — bỏ Account | 64–65 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 10 | Bán: dùng thử + license key + mua đứt, AI của người dùng | 66–69 | <span class="chip chip--todo">Chưa làm</span> |
| App | Mac + Windows | bản bán đầu, phần riêng app, Windows Beta, GitHub Releases + tự cập nhật | 75, 79, 82, 81 | <span class="chip chip--todo">Chờ xong Version 10</span> |
| Web | 11 | Marketing: định vị, landing, kênh, lịch 6 tuần | 70–73 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 2 | Nguồn mới + AI: YouTube, Amazon, Google Maps | 31a, 31–35 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 3 | So sánh đối thủ + AI Cite | 37–40 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 4 | Kệ Google, kệ AI, gói GEO | 41–45 | <span class="chip chip--todo">Chưa làm</span> |
| Web | 12 | Tính năng mới — mới ghi plan | — | <span class="chip chip--todo">Chưa đánh số</span> |
| ⛔ | KO LÀM | Account · V5 Performance · V6 test tự động · V7 CI · V8 security / refactor · App 76–78, 80 | 30 · 46–63 · 76–78 · 80 | <span class="chip chip--skip">Không làm</span> |

Việc chưa xếp phase hoặc không làm: [Appendix](appendix.md). Mỗi phase đi theo [Quy trình build](quy-trinh-build.md).

## Trông như thế này

<figure class="frame" markdown>
![Bảng keyword của niche budget tracker](images/explore-table.jpg)
</figure>

<div class="box box--danger" markdown>
**Không làm (cố ý)**

- AI tự đưa ra con số — AI (Phase 4, 6) chỉ đọc chữ và trích dẫn
- Lượt tìm "thật" — store không công khai, "phổ biến" là ước lượng
- Tài khoản, đăng nhập, host server cho nhiều người — app chạy trên máy, bán bằng license key
</div>

[Bản Master Plan đầy đủ (chữ)](superpowers/specs/2026-10-24-niche-radar-master-plan.md)
