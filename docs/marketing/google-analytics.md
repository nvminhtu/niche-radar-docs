# Google Analytics + Search Console — đo số

> Kênh đo, không phải kênh kéo khách. Chưa có số mốc thì không biết blog, free tool hay Reddit có đang chạy. Làm phần
> này **trước mọi kênh khác**.

<span class="chip chip--todo">Chưa làm · 2026-11-02 · chờ khoá service account</span>

<div class="box box--goal" markdown>
**Đích**

- Mỗi tuần có **1 dòng số** trong bảng ở cuối trang: GA4 28 ngày + Search Console 28 ngày + lượt tải từ blog.
- Biết được **kênh nào ra khách** (Organic Search, Referral từ AI, Social, Direct) và **bài nào ra lượt tải**.

**Xong khi:** đã ghi số mốc tuần 0 · bảng số tuần có đủ cột từ tuần 1 · event lượt tải từ blog hiện trong GA4.
</div>

## Đọc số cho đúng

- **"Active user / tháng" của GA4 = 28 ngày cuộn**, không cộng số từng ngày lại (người quay lại bị đếm nhiều lần).
- **Tách 2 loại khách**: khách đọc landing / blog và khách đã tải app. Mục tiêu 2.000 là khách **web** (landing + blog).
- **Tín hiệu sớm nhất của blog là impressions** trên Search Console, không phải số trên GA. Click và active user đến sau.
- Chi tiết cách đọc số GA4 + phễu tính ngược: [Research · SaaS làm marketing](../web/research-marketing-saas.md).

## Đợt 0 · Mở lại bảng đo + ghi số mốc (tuần 0)

- [ ] **(Anh)** đặt khoá service account vào đúng `~/.config/gcp/oneclicktool-sa.json` (MCP `google-analytics` và `search-console` cùng dùng file này; 2026-11-02 cả hai báo thiếu file)
- [ ] **(Anh)** thêm email service account vào property GA4 của shotmatic.app (quyền Viewer) và vào Search Console (quyền Đọc)
- [ ] Claude ghi **số mốc GA4 28 ngày**: active user · new user · sessions · kênh (Organic Search, Direct, Referral, Social) · top 20 trang vào đầu tiên
- [ ] Claude ghi **số mốc Search Console 28 ngày**: impressions · click · CTR · vị trí TB · số bài đã index / bị loại
- [ ] Soát 64 bài blog: bài nào **đã index**, bài nào chưa (gửi lại sitemap nếu cần)
- [ ] Soát CTA `/download?ref=blog-<slug>` có vào GA4 không, để đếm được blog nào ra lượt tải

## Việc hằng tuần

- [ ] Mở GA4 + Search Console, ghi 1 dòng vào bảng dưới (Claude làm qua MCP `google-analytics` + `search-console`)
- [ ] Ghi riêng số khách đến từ **Referral ChatGPT / Perplexity / Gemini** (kênh [AEO / GEO](aeo-geo.md))
- [ ] Ghi số lượt tải theo `ref=` để biết bài / tool / Reddit nào ra lượt tải

## Bảng số tuần

Chưa có khoá thì ghi `chưa đo`.

| Tuần · ngày đo | GA4 (28 ngày) | Search Console (28 ngày) | Lượt tải từ blog |
|---|---|---|---|
| 0 · 2026-11-02 | active user `chưa đo` · Organic `chưa đo` | impressions `chưa đo` · click `chưa đo` · bài top 10 `chưa đo` | `chưa đo` |

## Liên quan

[Tổng quan · 2.000 active user / tháng](../web/PLAN-ANALYTICS-2000-active-users-per-month.md) ·
[Phase 46.2 · Từ khoá + blog + Search Console](../web/phase-46-2-seo-keyword-blog-gsc.md) ·
[Phase 29 · Analytics + báo lỗi](../web/phase-29-analytics-errors.md)
