# Niche Radar Phase 11 — Research nguồn tìm gap — Implementation Plan

> **For agentic workers:** phase **chỉ research, không code**. Mỗi Task xong thì `npm run docs:build` (strict) xanh rồi
> commit. Steps dùng checkbox (`- [ ]`). Không đăng ký, không trả phí, không nhập key, không cài MCP chưa đọc code.

**Goal:** so **mọi nguồn** tìm gap / keyword niche trên cùng một thang, chọn top 3 nguồn đáng có phase code riêng.

**Spec:** [Phase 11 · Research nguồn tìm gap](../../web/phase-11-gap-sources.md) · **Cần trước:** không (chạy song song được với Phase 10).

## Mục tiêu · làm · không làm

- **Xong khi:** trang **Bản đồ nguồn gap** ≥ 30 nguồn đủ 6 tiêu chí + kết luận + link + ngày kiểm · ≥ 10 MCP và ≥ 10 repo
  / tool đã kiểm · ≥ 8 phương pháp ghi Niche Radar đã có chưa · top 3 nguồn đề xuất kèm lý do + phase cũ nên gộp / đổi ·
  phần kiến thức chung lên Product Growth Playbook (tiếng Anh).
- **Làm:** 1 trang docs mới + bảng dữ liệu, đề xuất top 3.
- **Không làm:** code collector · đăng ký / trả phí · cài MCP cộng đồng chưa đọc code · quét số lượng lớn · bịa số.

## Global Constraints

- Thang 6 tiêu chí (Mạnh / Vừa / Yếu + 1 câu lý do + link): tín hiệu gap · đo được độ quan tâm · lấy được dữ liệu ·
  chi phí · rủi ro điều khoản · hợp loại app.
- Luật kết luận cố định: tín hiệu Mạnh + lấy được (không "cấm") → **Làm phase riêng** · Mạnh nhưng chỉ làm tay →
  **Làm tay khi cần** · Yếu → **Bỏ**.
- Mọi số (giá, sao, ngày commit) đo tại nguồn, ghi ngày `2026-10-xx`; chưa đo → `chưa đo`.
- Kiểm "lấy được không" bằng vài trang mở tay (built-in browser / Claude in Chrome), không cào hàng loạt.
- Tài liệu 1 cột dọc; bảng chỉ dùng cho cột ngắn (tên, chấm, kết luận) — lý do dài để dưới từng nguồn.

## File đụng tới

- `docs/web/gap-sources-map.md` (mới) — Bản đồ nguồn gap: bảng tóm tắt + mục từng nguồn
- `docs/web/phase-11-gap-sources.md` — chip trạng thái, link sang bản đồ, kết quả
- `mkdocs.yml` — thêm bản đồ vào nav dưới Phase 11
- `docs/appendix.md` — nguồn bị Bỏ + lý do (để khỏi xét lại)
- Product Growth Playbook (repo riêng) — 1 skill / trang tiếng Anh: cách chấm nguồn gap + phương pháp — không tên niche đang nhắm

## Tasks

### Task 1: Khung trang + thang chấm
- [x] Tạo `gap-sources-map.md`: thang 6 tiêu chí, luật kết luận, bảng tóm tắt (Nguồn · Nhóm · Tín hiệu · Lấy được ·
      Chi phí · Điều khoản · Hợp app · Kết luận · Ngày kiểm), mục chi tiết 1 cột.
- [x] Nối nav + link từ trang Phase 11. `npm run docs:build` xanh.

### Task 2: Kiểm ≥ 30 nguồn
- [x] Tìm kiếm / xu hướng: Pinterest Trends, TikTok Creative Center, Google Autocomplete + People also ask, YouTube /
      Amazon suggest, Exploding Topics, Glimpse, AnswerThePublic.
- [x] Cộng đồng: Apple Community, Ask Different, Super User, Hacker News (Ask HN), Indie Hackers, Product Hunt, Quora,
      Discord, X search, nhóm Facebook.
- [x] Chợ app / review: Mac App Store, Setapp, Raycast Store, Chrome Web Store, VS Code Marketplace, WordPress plugins,
      Shopify App Store, Figma Community, AlternativeTo, G2, Capterra, Trustpilot.
- [x] Bằng chứng tiền: TrustMRR (đã có), Acquire.com, Flippa, Indie Hackers products, Starter Story, Gumroad, Etsy,
      marketplace template Notion / Excel.
- [x] Yêu cầu tính năng: GitHub issues (feature request, 👍), Canny / Featurebase công khai, Upwork / Fiverr.
- [x] Dữ liệu của mình: Search Console oneclicktool.app (`/fix`) qua MCP đã nối — chỉ đọc.
- [x] Mỗi nguồn: mở thật ≥ 1 trang, đọc điều khoản (link), chấm 6 tiêu chí, kết luận, ngày.

### Task 3: ≥ 10 MCP
- [x] Đang có: Google Trends, Search Console, Google Analytics — ghi dùng cho nguồn nào.
- [x] Kiểm: Apify, Firecrawl, Exa, Tavily, Perplexity, Bright Data, DataForSEO, MCP cộng đồng cho Reddit / HN / Product
      Hunt / YouTube transcript / App Store. Mỗi cái: làm gì, free / trả phí (giá + nguồn + ngày), chính chủ hay cộng đồng.
- [x] MCP cộng đồng: đọc code trước, ghi quyền nó đòi; đòi ghi / gửi dữ liệu đi lạ → ghi "không dùng".

### Task 4: ≥ 10 repo / tool
- [x] google-play-scraper, app-store-scraper, yt-dlp, Crawlee, Playwright, Scrapy, trafilatura, kho dump Reddit
      (Arctic Shift), BERTopic, KeyBERT, sentence-transformers, repo "awesome" indie / scraping.
- [x] Mỗi cái: link, số sao + ngày commit gần nhất (đo trên GitHub), license, còn chạy không, dùng cho nguồn nào.

### Task 5: ≥ 8 phương pháp
- [x] SERP do diễn đàn chiếm · "X alternative / X vs Y / X free" · "I'd pay for / is there an app / wish there was" ·
      đợt đổi nền tảng (WWDC) · unbundling tool lớn · template bán chạy · extension nhiều dùng điểm thấp · JTBD từ review ·
      Upwork việc lặp lại · Search Console của mình.
- [x] Mỗi cái: làm thế nào, nguồn nào, Niche Radar đã có chưa (link phase), nên thêm không.

### Task 6: Top 3 + đẩy kiến thức chung
- [x] Chọn top 3 nguồn "Làm phase riêng": lý do, phase cũ nên gộp / đổi (so với YouTube 31–32, Amazon 33–34, Maps 35).
      Ghi là **đề xuất** — anh duyệt mới đánh số phase.
- [x] Nguồn Bỏ → `appendix.md`.
- [x] Viết bản tiếng Anh dạng phương pháp lên Product Growth Playbook (đúng `SKILL_TEMPLATE.md`, có nguồn), push main.
- [x] Chip phase → xong, ROADMAP, CHANGELOG (nhãn Docs). Mở trang ở ~1340px xem không có cột hẹp.

## Tiến độ

- 2026-10-25: viết plan.
- 2026-10-26: xong. 52 nguồn · 17 MCP · 21 repo · 12 phương pháp ở `docs/web/gap-sources-map.md`; top 3 chờ duyệt; Search Console `chưa đo` (thiếu khoá MCP trên máy).
