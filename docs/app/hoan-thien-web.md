# Hoàn thiện Web · Phase 18–26 + 38–45 (gom mọi việc dang dở)

> Gom **mọi tính năng Web còn dang dở** của Version 1 vào một chỗ, ghi rõ **đã tới đâu · còn gì · có chặn bản bán đầu
> không**. Phần AI tách hẳn sang [Phase 27](phase-27-ai-cua-ban.md) (bộ máy AI) và [Phase 28](phase-28-ai-tinh-nang.md)
> (AI cho từng tính năng).

<span class="chip chip--doing">Đang làm · plan 2026-10-26 · 13 mục xong · 5 việc chờ chạy thật · 18 mục còn làm</span>

<div class="nr-stats" markdown>
<div><b>13</b><span>mục xong</span></div>
<div><b>5</b><span>việc chờ chạy thật</span></div>
<div><b>9</b><span>Phase 18–26 · phải xong trước bản bán</span></div>
<div><b>10</b><span>Phase 38–45 · vào bằng bản cập nhật</span></div>
</div>

<div class="box box--goal" markdown>
**Vì sao gom lại.** Đã chốt bán **app Mac + Windows** (thị trường đã có người trả tiền — [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords)
bán $79, 250 lượt tải Mac sau 4 ngày). Lộ trình cũ có ~20 phase Web chưa làm xếp trước app → quá lâu mới có thứ để bán.
Hoàn thiện Web chia đôi: **Phase 18–26** là những thứ người mua mở app ra thấy ngay (phải xong trước), **Phase 38–45** đi sau bằng bản cập nhật
tự động ([Phase 37](phase-37-release-auto-update.md)).
</div>

**Cần xong trước:** không — làm song song được với Bước 0 của [Phase 27](phase-27-ai-cua-ban.md).

## Đã xong (Phase 1–17)

| Phase | Tính năng | Trạng thái |
|---|---|---|
| [1](../web/phase-1-google-play.md) | Google Play: cây keyword, điểm cơ hội, bản đồ ngách, CSV | ✅ Xong |
| [2](../web/phase-2-app-store.md) | App Store: gợi ý iOS, gói IAP / cột Tiền, review iOS | ✅ Xong |
| [3](../web/phase-3-google-trends.md) | Google Trends: Top 10, so ≤ 5 keyword, mùa vụ, top nước | ✅ Xong |
| [4](../web/phase-4-feature-gap.md) | Feature Gap Matrix: top 5 app × 10 tính năng, câu nguồn, "Không nói" | ✅ Xong · tuyến AI chờ → Phase 27 |
| [6](../web/phase-6-ai-web.md) | Lớp AI chung, chủ đề than + tóm tắt qua job Claude | ✅ Xong · tuyến 1 bấm chờ → Phase 27 |
| [8](../web/phase-8-project-data.md) | Project, xuất / nhập, backup / restore, ULID + backup trước migrate | ✅ Xong |
| [9](../web/phase-9-small-features.md) | Nhãn mô hình tiền, mức nặng than, điểm v2 +2 trục, theo dõi 7/30/90 ngày | ✅ 4 mục ưu tiên xong |
| [10](../web/phase-10-i18n.md) | Khung đa ngôn ngữ vi · en · es | ✅ Khung xong · **mới dịch header, menu, Cài đặt** |
| [12](../web/phase-12-qa-gap.md) | Q&A Gap: Stack Exchange + Ask HN | ✅ Xong · 2.264 câu thật |
| [13](../web/phase-13-github-gap.md) | GitHub Feature Request Gap | ✅ Xong · 78 repo, 736 issue |
| [14](../web/phase-14-gap-sources.md) | Research nguồn tìm gap | ✅ Xong |
| [16](../web/phase-16-decision-board.md) | Bàn quyết định long-tail + fake-door Pro | ✅ Xong |
| [17](phase-17-local-app-1.md) | Vỏ app Mac Tauri + Node sidecar, `.dmg` notarize | ✅ Có `.dmg` 0.8.0 |

## Code xong — chỉ còn chạy thật (việc của anh)

Không cần code thêm. Mỗi dòng xong là phase lên chip xanh.

| Phase | Còn gì | Ai làm |
|---|---|---|
| [7](../web/phase-7-review-validate.md) Review + Validate | chọn 1 niche, chạy 1 vòng test bán trước thật, nhập số | anh |
| [11](../web/phase-11-reddit-gap.md) Reddit Gap | lưu 10 trang r/MacOS từ Chrome, nhập ≥ 500 bài, kiểm tay 30 bài (chuyên mục ≥ 80 %, chủ đề ≥ 70 %) | anh lưu file · Claude kiểm |
| [15](../web/phase-15-export.md) Export | mở CSV bằng Google Sheets, xem dấu + cột | anh |
| [16](../web/phase-16-decision-board.md) fake-door | gắn `VITE_GA_ID` → `npm run demo:deploy`; **đọc số ngày 2026-11-23** (ngưỡng ≥ 20 email Pro + ≥ 30 % chọn có trả tiền) | anh gắn ID · Claude deploy + đọc số |
| [17](phase-17-local-app-1.md) App Mac | thử `.dmg` trên một tài khoản macOS mới (chưa cài Node) | anh |

## Phase 18–26 · Phải xong trước bản bán đầu

Người mua mở app ra là thấy những chỗ này. Thứ tự làm từ trên xuống.

| # | Phase | Đã có | Còn thiếu (phần không AI) |
|---|---|---|---|
| 1 | [18 · Đối thủ bị chê gì](../web/phase-18-competitor-complaints.md) | ✅ xong 2026-10-26 | ~~gộp cùng ý ("crash" · "keeps crashing"), app nào bị chê, tách lỗi vs thiếu tính năng, review 3★ "ước gì", bảng app × lời chê~~ |
| 2 | [19 · Ai là khách hàng](../web/phase-19-ai-la-khach.md) | — | loại khách theo vai từ keyword · review 1–3★ của Phase 18 · đối thủ · Reddit / Q&A, bảng loại khách có dẫn chứng, mục Đối tượng của evidence pack — không đoán giới tính / tuổi |
| 3 | [20 · Chấm sức khoẻ niche](../web/phase-20-niche-health.md) | 7 yếu tố, trọng số + 4 mẫu, BUILD / TEST THÊM / BỎ | giải thích từng yếu tố, độ tin, cờ chặn, back-test (5 niche hiện 4,5–5,4 điểm, chưa niche nào ≥ 6) |
| 4 | [21 · Collect](../web/phase-21-collect.md) + [22 · Quản lý Project](../web/phase-22-project-manage.md) | + Collect từng keyword, trạng thái / kết luận / ghi chú | 5 loại item, gom hàng loạt, chụp số lúc gom · tìm / lọc / thẻ / gộp, lý do loại, bước tiếp (**1 migration chung**) |
| 5 | [23 · Trang kết quả Research](../web/phase-23-research-page.md) | các khối xếp theo thứ tự phase thêm vào | **đầu trang là câu trả lời** (BUILD / TEST THÊM / BỎ + 3 lý do), sắp lại khối theo câu hỏi chọn niche, chạy lại từng nguồn lỗi |
| 6 | [10 · Tiếng Anh đủ cả app](../web/phase-10-i18n.md) | khung vi · en · es, mới dịch header / menu / Cài đặt | dịch **en** hết mọi trang (bán quốc tế như Wow Keywords) — vi giữ, es để sau |
| 7 | [24 · Setup trong app](../web/phase-24-setup.md) | — | trang Setup lần đầu: kiểm máy + **nối AI** (dùng bộ dò của [Phase 27](phase-27-ai-cua-ban.md)) — bỏ phụ thuộc Backlog 01 Account (đã KO LÀM) |
| 8 | [25 · UI / UX](../web/phase-25-ui-ux.md) | — | soát theo checklist, sửa header tràn 40px ở ~1009px, xem 1340 + 375 |
| 9 | [26 · Review cụm](../web/phase-26-review-core.md) | — | review lại Phase 18–25 + Phase 27 + Phase 28 đợt 1 trên DB thật trước khi gói app ([Phase 34](phase-34-local-app-2.md)) |

## Phase 38–45 · Sau bản bán đầu (vào bằng bản cập nhật)

| Phase | Đã có | Còn thiếu (phần không AI) |
|---|---|---|
| [38 · Doanh thu thật](../web/phase-38-revenue.md) | cột Tiền, nhãn mô hình tiền, job TrustMRR | nguồn công khai khác, nhãn verified vs ước — phần khớp tên bằng AI ở Phase 28 |
| [39 · Backup tự động](../web/phase-39-backup-restore.md) | backup / restore bấm tay, tự backup trước migrate | tự backup theo lịch, giữ có chừng, kiểm toàn vẹn, restore 1 project |
| [40 · Explore](../web/phase-40-explore-tree.md) | cây ≤ 100 keyword, bản đồ ngách, Flow niche | lọc rác / tên thương hiệu bằng luật, Research hàng loạt — gộp cùng nghĩa bằng AI ở Phase 28 |
| [41 · Hồ sơ đối thủ](../web/phase-41-competitor-profile.md) | bảng đối thủ trong Research | trang riêng mỗi đối thủ, cờ đối thủ yếu |
| [42 · Theo dõi tự chạy](../web/phase-42-tracking.md) | chụp số tay, so lần trước, mốc 7/30/90 | tự chạy theo lịch, chỉ báo thay đổi đáng chú ý |
| [43 · Evidence pack + test bán trước](../web/phase-43-evidence-presell.md) | evidence `.md`, nháp test bán trước | chạy hết 1 vòng thật (nối Phase 7) |
| [44 · So sánh niche](../web/phase-44-compare-niche.md) | — | đặt 2–4 niche cạnh nhau |
| [45 · Tutorial nút ?](../web/phase-45-tutorial.md) | trang `/guide` 4 bước | nút ? từng khối |
| [9 · ứng viên còn lại](../web/phase-9-small-features.md) | — | chưa chốt — chọn bằng góp ý người mua |
| [10 · es](../web/phase-10-i18n.md) | — | tiếng Tây Ban Nha |

## Dời khỏi Version 1 (sang phase AI)

| Phase cũ | Sang | Vì sao |
|---|---|---|
| [28.1 · Tóm tắt niche (AI)](../web/phase-28-1-ai-summary.md) | [Phase 28](phase-28-ai-tinh-nang.md) | thành nút 1 bấm chạy trên AI của người dùng |
| [27.6 · Cài đặt AI](../web/phase-27-6-ai-settings.md) | [Phase 27](phase-27-ai-cua-ban.md) | Cài đặt AI giờ là "nối AI bạn đã có" |
| [27.3 · MCP của app](../web/phase-27-3-mcp.md) | [Phase 27](phase-27-ai-cua-ban.md) | MCP là một nửa của bộ máy AI (AI gọi app) |
| [27.7 · AI của người dùng](../web/phase-27-7-ai-cost-plans.md) | [Phase 27](phase-27-ai-cua-ban.md) | làm sớm, trước bán — là điểm bán chính |
| [27.4 · Hỏi dữ liệu (AI Cite)](../web/phase-27-4-ai-cite-ask.md) | [Phase 27](phase-27-ai-cua-ban.md) khung chat | có MCP + khung chat là hỏi được ngay |

<div class="box box--star" markdown>
**Xong khi**

- Code xong chờ chạy thật: 5 dòng đều có số chạy thật, chip phase lên xanh
- Phase 18–26: 9 mục xong, mỗi mục qua "Xong khi" của trang phase gốc; app chạy trọn **không nối AI nào** (tắt AI vẫn tra niche,
  chấm điểm, gom project, xuất file được)
- Toàn bộ UI có tiếng Anh, không còn chữ Việt cứng trong code (kiểm bằng script quét chuỗi)
- Xem tận mắt 1340 + 375 mọi trang, console sạch
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Mọi phần gọi AI — [Phase 27](phase-27-ai-cua-ban.md) / [Phase 28](phase-28-ai-tinh-nang.md)
- Account, Version 5–8 — vẫn [KO LÀM](../appendix.md#khong-lam-chot-2026-10-26)
- Nguồn mới (YouTube, Amazon, Maps — Version 2) trước bản bán đầu
</div>

[← Plan bán app](plan-ban-app.md) · [Phase 27 →](phase-27-ai-cua-ban.md)
