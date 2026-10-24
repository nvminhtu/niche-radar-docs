# niche-radar — Giới hạn nguồn dữ liệu & cách chia sẻ cho người khác

> Ngày: 2026-10-24 · Áp dụng cho v1 và phase 2. Các con số "giới hạn" của nguồn không chính thức là
> **quan sát/ước lượng**, không phải cam kết của Google — có thể đổi bất cứ lúc nào.

## 1. Giới hạn từng nguồn

| Nguồn | Chính thức? | Phí | Giới hạn | Khi vượt | Tool đang làm gì |
|---|---|---|---|---|---|
| **App Store** (iTunes Search API) | Có, của Apple, không cần key | Miễn phí | Apple ghi **khoảng 20 request/phút/IP** ("subject to change"). Không công bố giới hạn ngày (về lý thuyết ~28.800/ngày nếu đều 20/phút) | HTTP 403 → tool báo `RATE_LIMITED` | 1 request / 3 giây (= 20/phút), timeout 20 giây |
| **Google Play** (`google-play-scraper`) | **Không** — cào trang Play | Miễn phí | Không công bố. Gọi dồn dập → Google trả 429/503 hoặc chặn IP tạm thời (vài phút tới vài giờ). Thư viện có thể **gãy khi Google đổi trang** | Lỗi → `RATE_LIMITED`/`NETWORK`, nút Thử lại | 1 request/giây, timeout 20 giây, chỉ gọi chi tiết app không trùng |
| **Google Trends** (`google-trends-api`) | **Không** — gọi endpoint nội bộ của trang Trends | Miễn phí | Chặt nhất trong 4 nguồn: vài chục request liên tục là dính **429**; IP datacenter/VPS bị chặn nhanh hơn IP nhà; đôi khi đòi cookie | Trả HTML thay JSON → `RATE_LIMITED` | Chỉ 2 request mỗi lần tra (seed), retry 2s → 5s → 10s, cache 24 giờ |
| **Reddit** (API chính thức, OAuth) | Có | Miễn phí cho dùng cá nhân / phi thương mại | **100 request/phút** cho mỗi OAuth client. Dùng thương mại cần thoả thuận riêng với Reddit | 429 → `RATE_LIMITED` | 1 request/giây, cần key trong `.env.local` |
| Google autocomplete (phase 2) | Không chính thức (`suggestqueries.google.com`) | Miễn phí | Không công bố, nhẹ hơn Trends nhưng vẫn chặn khi dồn dập | Lỗi → giữ gợi ý của nguồn kia | 1 request/giây, cache 7 ngày |

### Một lần tra tốn bao nhiêu request

| Nguồn | v1: 1 lần tra (seed + 5 gợi ý) | Phase 2: 1 lần "Mở rộng" |
|---|---|---|
| Play | 1 suggest + 6 search + tối đa ~180 chi tiết app (thực tế 40–60) → **1–3 phút** | ~27–35 suggest |
| App Store | 6 search → ~18 giây | số liệu: tối đa 50 search → ~2,5 phút |
| Trends | 2 | 0 |
| Google suggest | 0 | ~27–35 |
| Reddit | 1 token + 6 search | 0 |

**Ước lượng thực tế cho một người dùng, một IP nhà:** vài chục lần tra/ngày chạy ổn. Tra liên tục hàng trăm
lần/ngày thì Play và Trends gần như chắc chắn bị chặn tạm thời. Cache 24 giờ giúp tra lại cùng niche không tốn
request.

### Proxy — có cần không?

- **Chạy local trên máy mỗi người: không cần proxy.** Mỗi người dùng IP nhà của họ, giới hạn tính riêng.
- **Chạy trên server (VPS, Vercel…) cho nhiều người dùng chung:** Trends và Play bị chặn rất nhanh vì IP datacenter
  + mọi người chung một IP. Muốn chạy kiểu này phải dùng **proxy dân cư (residential proxy)** xoay IP:
  - tốn tiền (thường tính theo GB băng thông),
  - vùng xám về điều khoản dịch vụ của Google (cào dữ liệu không qua API chính thức),
  - vẫn không đảm bảo — Google chặn cả dải proxy phổ biến.
- **Thay thế có trả phí, ổn định hơn proxy:** dịch vụ SERP như SerpApi (có Google Trends, Google Play), DataForSEO
  (có dữ liệu keyword App Store/Play + search volume). Trả theo lượt gọi.
- **Google Trends API chính thức:** Google đã công bố bản alpha (2025), chỉ cấp cho người được duyệt — chưa dùng
  được cho tool cá nhân.

**Quyết định cho niche-radar:** giữ mô hình **mỗi người chạy local, không proxy**. Không triển khai server dùng
chung trong v1/phase 2.

## 2. Chia sẻ cho người khác dùng

### Cách A — mỗi người tự chạy local (hiện tại, khuyến nghị)

Người nhận cần:

1. **Node.js 22** (cài từ nodejs.org hoặc nvm).
2. **Công cụ build native** cho `better-sqlite3`:
   - macOS: `xcode-select --install` (Command Line Tools).
   - Windows: Visual Studio Build Tools (gói "Desktop development with C++"), hoặc dùng WSL.
3. Lấy code: repo hiện **chưa có remote** → cần đưa lên GitHub (private, mời người dùng) hoặc gửi file zip
   (không kèm `node_modules/`, `data/`, `dist/`, `.env.local`).
4. Chạy:
   ```bash
   npm install
   cp .env.example .env.local   # tuỳ chọn: điền key Reddit của chính họ
   npm run dev                  # http://localhost:3200
   ```
5. **Key Reddit:** mỗi người tự tạo app "script" ở reddit.com/prefs/apps. Không chia sẻ key của bạn (giới hạn 100
   req/phút tính theo key, và key gắn với tài khoản Reddit của bạn).

Mỗi người có DB riêng (`data/niche.db`) và giới hạn IP riêng. Server chỉ nghe `127.0.0.1` nên **không** mở được từ
máy khác trong mạng LAN — đó là chủ ý (chống gọi lén).

### Cách B — app desktop macOS (cho người không rành kỹ thuật) — **không dùng Electron**

Quyết định 2026-10-24: không dùng Electron (nặng RAM). Chọn một trong hai:

- **Tauri (Rust):** vỏ nhẹ, dùng WebView có sẵn của macOS nên ít RAM; giữ được giao diện React hiện có (Vite build ra web tĩnh, hợp với Tauri). Phần lấy
  dữ liệu chạy Node đi kèm dạng sidecar (giữ nguyên `google-play-scraper`, `google-trends-api`), hoặc viết lại dần
  bằng Rust.
- **SwiftUI native:** mượt và nhẹ nhất trên Mac, nhưng phải viết lại toàn bộ giao diện và phần lấy dữ liệu (không có
  thư viện Play/Trends cho Swift — phải tự cào), tốn công nhất.

Chung cho cả hai:
- Người dùng tải `.dmg`, kéo vào Applications, bấm icon. Vẫn chạy trên máy họ, IP của họ → không cần proxy.
- DB đặt ở `~/Library/Application Support/niche-radar/`, ô nhập key Reddit trong app thay cho `.env.local`.
- Ký + notarize bằng tài khoản Apple Developer ($99/năm); không ký thì người dùng phải chuột phải → Open.
- Nằm ở **Appendix (Phase 6)** của plan tổng (`2026-10-24-niche-radar-master-plan.md`).

### Cách C — host một web cho mọi người (không khuyến nghị lúc này)

Cần: VPS (không phải Vercel — job nền chạy vài phút + file SQLite không hợp serverless), đăng nhập/phân quyền,
proxy dân cư hoặc dịch vụ SERP trả phí, giới hạn lượt tra mỗi người, Postgres thay SQLite. Là một dự án khác hẳn.

## 3. Việc cần cập nhật vào code/README (theo dõi)

- [x] README: thêm tóm tắt giới hạn nguồn + link tài liệu này.
- [ ] README: mục "Cài cho người khác" (Cách A).
- [ ] Hiện cảnh báo trên UI khi một nguồn trả `RATE_LIMITED`: "Nguồn đang chặn tạm thời — thử lại sau 10–30 phút"
      (nằm trong Phase 1 của plan tổng).
- [ ] (Tuỳ chọn) Đếm số request mỗi nguồn trong ngày, hiện ở trang chủ để biết mình đang dùng nhiều tới đâu.
- [ ] App desktop Tauri hoặc SwiftUI (Phase 6 — Appendix), không Electron.
