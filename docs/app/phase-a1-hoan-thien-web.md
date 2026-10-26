# Phase A1 · Hoàn thiện Web (gom mọi việc dang dở)

> Gom **mọi tính năng Web còn dang dở** của Version 1 vào một chỗ, ghi rõ **đã tới đâu · còn gì · có chặn bản bán đầu
> không**. Phần AI tách hẳn sang [Phase A2](phase-a2-ai-cua-ban.md) (bộ máy AI) và [Phase A3](phase-a3-ai-tinh-nang.md)
> (AI cho từng tính năng).

<span class="chip chip--doing">Đang làm · plan 2026-10-26 · 13 mục xong · 5 việc chờ chạy thật · 18 mục còn làm</span>

<div class="nr-stats" markdown>
<div><b>13</b><span>mục xong</span></div>
<div><b>5</b><span>việc chờ chạy thật (A1.0)</span></div>
<div><b>8</b><span>A1.1 · phải xong trước bản bán</span></div>
<div><b>10</b><span>A1.2 · vào bằng bản cập nhật</span></div>
</div>

<div class="box box--goal" markdown>
**Vì sao gom lại.** Đã chốt bán **app Mac + Windows** (thị trường đã có người trả tiền — [Wow Keywords](../doi-thu-tham-khao.md#wow-keywords)
bán $79, 250 lượt tải Mac sau 4 ngày). Lộ trình cũ có ~20 phase Web chưa làm xếp trước app → quá lâu mới có thứ để bán.
A1 chia đôi: **A1.1** là những thứ người mua mở app ra thấy ngay (phải xong trước), **A1.2** đi sau bằng bản cập nhật
tự động ([Phase 81](phase-81-release-auto-update.md)).
</div>

**Cần xong trước:** không — làm song song được với Bước 0 của [Phase A2](phase-a2-ai-cua-ban.md).

## Đã xong (Version 1)

| Phase | Tính năng | Trạng thái |
|---|---|---|
| [1](../web/phase-1-google-play.md) | Google Play: cây keyword, điểm cơ hội, bản đồ ngách, CSV | ✅ Xong |
| [2](../web/phase-2-app-store.md) | App Store: gợi ý iOS, gói IAP / cột Tiền, review iOS | ✅ Xong |
| [3](../web/phase-3-google-trends.md) | Google Trends: Top 10, so ≤ 5 keyword, mùa vụ, top nước | ✅ Xong |
| [4](../web/phase-4-feature-gap.md) | Feature Gap Matrix: top 5 app × 10 tính năng, câu nguồn, "Không nói" | ✅ Xong · tuyến AI chờ → A2 |
| [6](../web/phase-6-ai-web.md) | Lớp AI chung, chủ đề than + tóm tắt qua job Claude | ✅ Xong · tuyến 1 bấm chờ → A2 |
| [8](../web/phase-8-project-data.md) | Project, xuất / nhập, backup / restore, ULID + backup trước migrate | ✅ Xong |
| [9](../web/phase-9-small-features.md) | Nhãn mô hình tiền, mức nặng than, điểm v2 +2 trục, theo dõi 7/30/90 ngày | ✅ 4 mục ưu tiên xong |
| [9c](../web/phase-9c-i18n.md) | Khung đa ngôn ngữ vi · en · es | ✅ Khung xong · **mới dịch header, menu, Cài đặt** |
| [10b](../web/phase-10b-qa-gap.md) | Q&A Gap: Stack Exchange + Ask HN | ✅ Xong · 2.264 câu thật |
| [10c](../web/phase-10c-github-gap.md) | GitHub Feature Request Gap | ✅ Xong · 78 repo, 736 issue |
| [11](../web/phase-11-gap-sources.md) | Research nguồn tìm gap | ✅ Xong |
| [16b](../web/phase-16b-decision-board.md) | Bàn quyết định long-tail + fake-door Pro | ✅ Xong |
| [74](phase-74-local-app-1.md) | Vỏ app Mac Tauri + Node sidecar, `.dmg` notarize | ✅ Có `.dmg` 0.8.0 |

## A1.0 · Code xong — chỉ còn chạy thật (việc của anh)

Không cần code thêm. Mỗi dòng xong là phase lên chip xanh.

| Phase | Còn gì | Ai làm |
|---|---|---|
| [7](../web/phase-7-review-validate.md) Review + Validate | chọn 1 niche, chạy 1 vòng test bán trước thật, nhập số | anh |
| [10](../web/phase-10-reddit-gap.md) Reddit Gap | lưu 10 trang r/MacOS từ Chrome, nhập ≥ 500 bài, kiểm tay 30 bài (chuyên mục ≥ 80 %, chủ đề ≥ 70 %) | anh lưu file · Claude kiểm |
| [16](../web/phase-16-export.md) Export | mở CSV bằng Google Sheets, xem dấu + cột | anh |
| [16b](../web/phase-16b-decision-board.md) fake-door | gắn `VITE_GA_ID` → `npm run demo:deploy`; **đọc số ngày 2026-11-23** (ngưỡng ≥ 20 email Pro + ≥ 30 % chọn có trả tiền) | anh gắn ID · Claude deploy + đọc số |
| [74](phase-74-local-app-1.md) App Mac | thử `.dmg` trên một tài khoản macOS mới (chưa cài Node) | anh |

## A1.1 · Phải xong trước bản bán đầu

Người mua mở app ra là thấy những chỗ này. Thứ tự làm từ trên xuống.

| # | Phase | Đã có | Còn thiếu (phần không AI) |
|---|---|---|---|
| 1 | [12 · Đối thủ bị chê gì](../web/phase-12-competitor-complaints.md) | đếm cụm 1–3 từ trong review 1–2★, câu trích | gộp cùng ý ("crash" · "keeps crashing"), app nào bị chê, tách lỗi vs thiếu tính năng, review 3★ "ước gì", bảng app × lời chê |
| 2 | [13 · Chấm sức khoẻ niche](../web/phase-13-niche-health.md) | 7 yếu tố, trọng số + 4 mẫu, BUILD / TEST THÊM / BỎ | giải thích từng yếu tố, độ tin, cờ chặn, back-test (5 niche hiện 4,5–5,4 điểm, chưa niche nào ≥ 6) |
| 3 | [14 · Collect](../web/phase-14-collect.md) + [15 · Quản lý Project](../web/phase-15-project-manage.md) | + Collect từng keyword, trạng thái / kết luận / ghi chú | 5 loại item, gom hàng loạt, chụp số lúc gom · tìm / lọc / thẻ / gộp, lý do loại, bước tiếp (**1 migration chung**) |
| 4 | [20 · Trang kết quả Research](../web/phase-20-research-page.md) | các khối xếp theo thứ tự phase thêm vào | **đầu trang là câu trả lời** (BUILD / TEST THÊM / BỎ + 3 lý do), sắp lại khối theo câu hỏi chọn niche, chạy lại từng nguồn lỗi |
| 5 | [9c · Tiếng Anh đủ cả app](../web/phase-9c-i18n.md) | khung vi · en · es, mới dịch header / menu / Cài đặt | dịch **en** hết mọi trang (bán quốc tế như Wow Keywords) — vi giữ, es để sau |
| 6 | [30.1 · Setup trong app](../web/phase-30-1-setup.md) | — | trang Setup lần đầu: kiểm máy + **nối AI** (dùng bộ dò của [A2](phase-a2-ai-cua-ban.md)) — bỏ phụ thuộc Phase 30 Account (đã KO LÀM) |
| 7 | [29 · UI / UX](../web/phase-29-ui-ux.md) | — | soát theo checklist, sửa header tràn 40px ở ~1009px, xem 1340 + 375 |
| 8 | [27 · Review cụm](../web/phase-27-review-core.md) | — | review lại 12–20 + A2 + A3 đợt 1 trên DB thật trước khi gói app ([Phase 75](phase-75-local-app-2.md)) |

## A1.2 · Sau bản bán đầu (vào bằng bản cập nhật)

| Phase | Đã có | Còn thiếu (phần không AI) |
|---|---|---|
| [18 · Doanh thu thật](../web/phase-18-revenue.md) | cột Tiền, nhãn mô hình tiền, job TrustMRR | nguồn công khai khác, nhãn verified vs ước — phần khớp tên bằng AI ở A3 |
| [19 · Backup tự động](../web/phase-19-backup-restore.md) | backup / restore bấm tay, tự backup trước migrate | tự backup theo lịch, giữ có chừng, kiểm toàn vẹn, restore 1 project |
| [21 · Explore](../web/phase-21-explore-tree.md) | cây ≤ 100 keyword, bản đồ ngách, Flow niche | lọc rác / tên thương hiệu bằng luật, Research hàng loạt — gộp cùng nghĩa bằng AI ở A3 |
| [22 · Hồ sơ đối thủ](../web/phase-22-competitor-profile.md) | bảng đối thủ trong Research | trang riêng mỗi đối thủ, cờ đối thủ yếu |
| [23 · Theo dõi tự chạy](../web/phase-23-tracking.md) | chụp số tay, so lần trước, mốc 7/30/90 | tự chạy theo lịch, chỉ báo thay đổi đáng chú ý |
| [24 · Evidence pack + test bán trước](../web/phase-24-evidence-presell.md) | evidence `.md`, nháp test bán trước | chạy hết 1 vòng thật (nối A1.0 Phase 7) |
| [28 · So sánh niche](../web/phase-28-compare-niche.md) | — | đặt 2–4 niche cạnh nhau |
| [30.2 · Tutorial nút ?](../web/phase-30-2-tutorial.md) | trang `/guide` 4 bước | nút ? từng khối |
| [9 · ứng viên còn lại](../web/phase-9-small-features.md) | — | chưa chốt — chọn bằng góp ý người mua |
| [9c · es](../web/phase-9c-i18n.md) | — | tiếng Tây Ban Nha |

## Dời khỏi Version 1 (sang phase AI)

| Phase cũ | Sang | Vì sao |
|---|---|---|
| [17 · Tóm tắt niche (AI)](../web/phase-17-ai-summary.md) | [A3](phase-a3-ai-tinh-nang.md) | thành nút 1 bấm chạy trên AI của người dùng |
| [25 · Cài đặt AI](../web/phase-25-ai-settings.md) | [A2](phase-a2-ai-cua-ban.md) | Cài đặt AI giờ là "nối AI bạn đã có" |
| [26 · MCP của app](../web/phase-26-mcp.md) | [A2](phase-a2-ai-cua-ban.md) | MCP là một nửa của bộ máy AI (AI gọi app) |
| [69 · AI của người dùng](../web/phase-69-ai-cost-plans.md) | [A2](phase-a2-ai-cua-ban.md) | làm sớm, trước bán — là điểm bán chính |
| [38 · Hỏi dữ liệu (AI Cite)](../web/phase-38-ai-cite-ask.md) | [A2](phase-a2-ai-cua-ban.md) khung chat | có MCP + khung chat là hỏi được ngay |

<div class="box box--star" markdown>
**Xong khi**

- A1.0: 5 dòng đều có số chạy thật, chip phase lên xanh
- A1.1: 8 mục xong, mỗi mục qua "Xong khi" của trang phase gốc; app chạy trọn **không nối AI nào** (tắt AI vẫn tra niche,
  chấm điểm, gom project, xuất file được)
- Toàn bộ UI có tiếng Anh, không còn chữ Việt cứng trong code (kiểm bằng script quét chuỗi)
- Xem tận mắt 1340 + 375 mọi trang, console sạch
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Mọi phần gọi AI — [A2](phase-a2-ai-cua-ban.md) / [A3](phase-a3-ai-tinh-nang.md)
- Account, Version 5–8 — vẫn [KO LÀM](../appendix.md#khong-lam-chot-2026-10-26)
- Nguồn mới (YouTube, Amazon, Maps — Version 2) trước bản bán đầu
</div>

[← Plan bán app](plan-ban-app.md) · [Phase A2 →](phase-a2-ai-cua-ban.md)
