# Đối thủ · Đối tác · Tham khảo

> Sổ ghi các sản phẩm, công ty, trang web liên quan tới Niche Radar. Anh gửi link → Claude mở trang thật, ghi vào
> đúng nhóm. Mọi số (giá, lượt dùng) ghi nguyên văn kèm **ngày xem**; trang không ghi thì để `chưa đo`, không đoán.

**Ba nhóm**

- **Đối thủ** — làm cùng việc hoặc gần việc của Niche Radar (tìm niche, nghiên cứu keyword / app, đo đối thủ)
- **Đối tác** — có thể nối, bán chung, dùng dữ liệu của nhau, hoặc là nơi đưa Niche Radar tới người dùng
- **Tham khảo** — học cách làm: giá, landing, tính năng, cách ra mắt, công cụ

**Mỗi mục ghi:** link · làm gì · cho ai · giá (nguyên văn + ngày) · giống / khác Niche Radar ở đâu · học được gì
(trỏ về phase liên quan) · ngày thêm.

## Đối thủ

### Wow Keywords

- **Link:** [wowkeywords.com](https://wowkeywords.com/) · tải bản cài: [GitHub Releases](https://github.com/Kronop/wowkeywords-releases/releases) · [MCP docs](https://wowkeywords.com/docs/mcp)
- **Làm gì:** app nghiên cứu keyword + tối ưu App Store (ASO) chạy trên máy, cho Mac (macOS 14+, chỉ Apple Silicon) và Windows 11 x64 (beta)
- **Cho ai:** người có app trên App Store muốn lên hạng ở nhiều nước (trang không nói rõ đối tượng)
- **Giá (xem 2026-10-26):** **$79 mua một lần**, "Lifetime access. No subscription." Trang ghi "15 licenses left at $79. Then $89." và
  "Up $10 every 20 licenses". Mỗi license dùng trên 2 máy. Không có dùng thử
- **Founder / công ty:** trang không ghi (chỉ "© 2026 Wow Keywords"); tài khoản GitHub phát hành là `Kronop`
- **Thêm ngày:** 2026-10-26 · **đánh giá lại:** 2026-10-26 (đọc trang chủ, trang tải, MCP docs, 24 bản phát hành trên GitHub)

#### Tính năng (đọc trang thật 2026-10-26)

- **Research:** gõ keyword tiếng Anh → app dịch thành cụm người bản xứ gõ thật (VD Đức gõ "kalorienzähler"), kiểm ở 50 nước
- **Track:** hạng của app mình ở từng nước (VD "2/15 in the top 10"), lịch sử hạng hằng ngày, app nào đang đứng trên mình
- **Optimize:** AI viết lại tên / phụ đề / ô keyword, chấm "reach" + "difficulty", bấm **Create version** để điền sẵn bản mới
  trong App Store Connect — không tự gửi duyệt
- **Brainstorm:** mô tả app → AI gợi keyword ngách ít cạnh tranh, làm được cả khi chưa có app
- **Volume / difficulty:** điểm 0–100 tự tính từ kết quả App Store thật — volume ước từ việc top 50 app nhắm cụm đó sát
  cỡ nào, difficulty từ số rating của top 10. Họ tự ghi: không phải số lượt tìm hằng tháng
- **MCP:** server chạy trong app, **53 tool**, thêm vào Claude Code / Codex / Cursor / Claude Desktop / Windsurf bằng 1 bấm.
  Agent làm được cả việc ghi (thêm app, chạy kiểm hạng, audit, đẩy lên App Store Connect khi được bảo)
- **AI:** không bán credit AI — app gọi Claude Code, Codex, OpenCode hoặc Ollama của người dùng. Phải nối được 1 AI mới
  qua bước setup (từ bản 1.0.6)

#### Mô hình phân phối — thứ đáng học

Số tải lấy từ GitHub API ngày 2026-10-26, đếm file `.dmg` / `Setup.exe` của mọi bản (chưa trừ người tải lại bản mới).

- **Tải miễn phí, mở app phải nhập license key.** Trang tải: "drag Wow Keywords to Applications, then enter your license key".
  Không dùng thử, không tài khoản
- **Repo phát hành riêng, public; code giữ kín.** File cài nằm ở `Kronop/wowkeywords-releases` (repo chỉ chứa Release), nút
  "Download for Mac" trỏ thẳng vào file `.dmg` trên GitHub → host 0 đồng, có số tải công khai
- **Ra bản rất dày.** 0.1.0 ngày 2026-10-22 → 1.0.0 ngày 2026-10-24 → 1.1.0 ngày 2026-10-26: **12 bản Mac trong 3 ngày**,
  mỗi bản có ghi chú bằng lời thường ("setup now stops within seconds and says so")
- **App tự cập nhật** từ bản 1.0.8 ("downloads, checks and installs updates itself") — người đã cài không phải tải lại tay
- **Windows ra cùng lúc, ghi rõ Beta và chưa ký** ("unsigned, so Windows may show a security warning") — không chờ mua
  chứng chỉ ký mới ra Windows
- **Thanh toán Stripe trực tiếp:** `/buy` chuyển thẳng sang `checkout.stripe.com`. Mất key → nhập email ở `/license` để
  gửi lại. Chuyển license sang máy khác trong Cài đặt
- **Giá bậc thang công khai:** +$10 sau mỗi 20 license, đếm ngược số còn lại ngay cạnh nút mua — vừa gấp vừa thật
- **Số tải đến 2026-10-26:** Mac `.dmg` **250 lượt** qua 13 bản (nhiều nhất 1.0.11: 91) · Windows `Setup.exe` **60 lượt** qua 11 bản
- **Công nghệ:** **Electron** — lệnh MCP trong docs dùng `ELECTRON_RUN_AS_NODE=1`, tên file `-arm64-mac.zip` là kiểu của
  electron-builder. Trang web là Next.js (thẻ `next-size-adjust`)
- *Suy đoán, chưa chắc:* nếu giá khởi điểm là $49 (số gạch trên trang) và tăng $10 mỗi 20 license thì tới $79 đã bán
  khoảng 65 license trong ~4 ngày. Không dùng số này làm bằng chứng

#### So với Niche Radar

- **Giống:** app chạy trên máy, dữ liệu ở máy, đọc App Store theo keyword, có MCP, AI tuỳ chọn
- **Khác:** Wow Keywords tối ưu **app đã có** (hạng, listing, ghi App Store Connect). Niche Radar chọn **niche nên làm**
  từ nhiều nguồn (Play, App Store, Trends, Reddit, Q&A, lời chê đối thủ, ai đang thu tiền) rồi ra BUILD / TEST THÊM / BỎ
- **Họ hơn:** volume + difficulty có công thức, đa quốc gia + tự dịch keyword, ghi thẳng App Store Connect, MCP 53 tool,
  có bản Windows
- **Mình hơn:** nhiều nguồn ngoài App Store, đọc lời chê + khoảng trống tính năng, bằng chứng doanh thu, kết luận nên làm hay
  không. MCP của mình ([Phase 26.3](web/phase-26-3-mcp.md)) trả lời được "niche nào đáng build", không chỉ "mình đứng hạng mấy"
- **Không có moat dữ liệu:** họ cũng chỉ đọc App Store công khai. Thứ bán được là luồng làm việc + cách phân phối

#### Áp vào Niche Radar (chốt 2026-10-26)

- Bán **app Mac + Windows** tải về, dữ liệu trên máy, không tài khoản — [App Mac + Windows](app/index.md)
- File cài trên GitHub Releases public, app tự cập nhật — [Phase 36](app/phase-36-release-auto-update.md)
- Windows ra bản Beta chưa ký trước — [Phase 35](app/phase-35-windows-app.md)
- License key + 2 máy + tìm lại key bằng email, giá mua đứt bậc thang; **khác họ: có dùng thử** — [Version 10](web/version-10.md)
- AI chạy trên thứ người dùng đã trả (Claude Code, Codex, Ollama, key riêng), không bán lượt AI — [Phase 26.7](web/phase-26-7-ai-cost-plans.md)
- MCP là điểm bán ngay trên landing — [Phase 26.3](web/phase-26-3-mcp.md)

## Đối tác

Chưa có.

## Tham khảo

Chưa có.
