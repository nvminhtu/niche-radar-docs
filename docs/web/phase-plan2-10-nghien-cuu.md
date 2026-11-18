# 10.1 · Nghiên cứu cho Keyword Intelligence

**Phase 1 của mục 10: soi repo hiện có, thư viện biểu đồ, bộ skill và sản phẩm tham khảo — để chọn đúng trước khi code.**

Đọc 2026-11-13. Số sao / ngày cập nhật lấy từ GitHub API hôm đó, sẽ cũ đi theo thời gian.

## Repo Niche Radar đang có gì

- **Stack:** Vite + React 19 + TypeScript + Tailwind v4 + Hono + SQLite (drizzle). Biểu đồ: Recharts 3. Test: Vitest.
  Không dùng Next.js, shadcn hay TanStack Table — engine theo stack này, không viết lại.
- **Số keyword thật đã có (miễn phí, không key):**
    - Explorer (cây keyword): độ phổ biến 0–100 (từ số lần + hạng được Play / Google / App Store gợi ý),
      tổng rating top 5 App Store, số app Play / App Store, nhóm (đối tượng · dạng · nền tảng · tính năng), quan hệ cha–con.
    - Google Trends: chỉ số quan tâm tương đối 0–100 theo tuần, 12 tháng (chỉ keyword đã bấm “xem xu hướng”).
    - Trang Keyword (1 seed): hạng app theo từng keyword gợi ý, rating, lượt cài, ngày ra mắt / update.
- **Không có:** lượt tìm tuyệt đối (search volume), CPC, độ khó SEO (KD), thứ hạng website. Các số này cần nguồn trả phí
  hoặc tài khoản (xem bảng nguồn số ở trang [10 · Keyword Intelligence](phase-plan2-10-keyword-engine.md)).

## Thư viện biểu đồ

| Thư viện | License | Hợp với | Ghi chú |
|---|---|---|---|
| Recharts (đang dùng) | MIT | line, area, bar, scatter / bubble, radar, treemap đơn giản | Hợp React, đã khớp theme sáng / tối của app. Không có network graph. |
| Apache ECharts | Apache-2.0 | network graph, treemap / sunburst nhiều tầng, heatmap lịch, dữ liệu rất lớn (canvas) | Gói lớn → chỉ tải khi mở chart cần (lazy-load). |
| TradingView Lightweight Charts | Apache-2.0 | chuỗi thời gian kiểu tài chính: crosshair, zoom, pan | File NOTICE yêu cầu ghi nguồn TradingView (mặc định hiện logo). Chỉ đáng dùng khi có chuỗi ngày dài. |
| Plotly.js | MIT | biểu đồ khoa học, 3D | Gói rất nặng, trùng việc với ECharts. |
| nivo | MIT | chart React đẹp sẵn | Trùng việc với Recharts. |
| Chart.js | MIT | chart canvas phổ thông | Trùng việc. |
| uPlot | MIT | chuỗi thời gian cực nhanh | Chỉ cần khi > 100K điểm. |
| visx | MIT | khối dựng D3 thấp tầng | Tự vẽ nhiều, tốn công. |

**Chốt (anh duyệt 2026-11-13):** giữ Recharts cho mọi chart; thêm ECharts **chỉ** cho network graph và cluster map
(treemap nhiều tầng) ở Phase 4, tải lười. Không thêm Lightweight Charts lúc này: dữ liệu thời gian dài nhất mới là
53 điểm tuần của Trends — Recharts đủ. Không cài 2 thư viện cho cùng 1 việc.

## Bộ skill tham khảo

| Repo | License | Lấy gì | Không lấy |
|---|---|---|---|
| anthropics/skills | không ghi license ở gốc repo | khung SKILL.md chuẩn, cách viết description | không chép nguyên |
| coreyhaines31/marketingskills | MIT | đã cài trong máy (`marketing-skills:*`): ai-seo, programmatic-seo, competitors | — |
| marketingskills/seo | MIT | ý `keyword-opportunity-finder`, `seo-priority-score`: chấm điểm có độ tin + tác động | các skill cần GSC / GA4 của website |
| SvaraNova/skills | MIT | nguyên tắc “dùng stack sẵn có”, kiểm 3 bề rộng, chart có bản thay thế cho người đọc màn hình | skill video |
| raghuramsirigiri/raghuram-skills | MIT | `chart-honesty`, `sanity-check`: soát chart nói dối (trục cắt, gộp đơn vị) | xuất HTML / slide |
| gptnius/skills-library | không rõ (NOASSERTION) | chỉ đọc danh mục | **không chạy** `bootstrap.sh` (kéo code từ 46 repo khác) |

Các skill riêng cho engine (chọn chart, chấm cơ hội, soát dữ liệu…) để sau Phase 3, khi engine đã chạy thật — viết skill
từ code thật chứ không viết trước.

## Sản phẩm tham khảo

| Sản phẩm | Học cái gì | Niche Radar làm thế nào |
|---|---|---|
| Google Keyword Planner | khoảng lượt tìm, cạnh tranh quảng cáo, mùa vụ | chưa có số → giữ chỗ, xám “sắp có” |
| vidIQ / TubeBuddy | 1 điểm tổng + điểm thành phần, giải thích vì sao | điểm cơ hội có bảng phần, trọng số sửa được |
| Ahrefs / Semrush | ma trận lượt tìm × độ khó, phân bố độ khó, ý định tìm kiếm | ma trận phổ biến × độ đông (đổi tên trục cho đúng số) |
| Google Trends | chỉ số tương đối, so nhiều keyword | ghi rõ “chỉ số tương đối, không phải lượt tìm” |
| CoinMarketCap / TradingView | chọn kỳ, rê chuột xem số, so nhiều đường | so tối đa 5 đường, tooltip đủ số |
| OctopusOn SEO Keyword Research (Apache-2.0 / MIT) | gom cụm theo chữ (nhanh, miễn phí) và theo SERP; gộp biến thể hoa / thường / dấu | Phase 4: gom cụm theo chữ trước |

## Rủi ro đã thấy

- **Gộp sai 2 loại “cạnh tranh”:** cạnh tranh quảng cáo (Google Ads), độ khó SEO (KD) và độ đông app store (rating top 5)
  là 3 số khác nhau. Engine giữ riêng từng loại, mỗi số mang nhãn nguồn.
- **Trends không phải lượt tìm:** 2 keyword cùng 50 điểm ở 2 lượt tra khác nhau không so được với nhau.
- **Độ phổ biến là ước lượng:** từ gợi ý tìm kiếm, không phải lượt tìm thật — luôn ghi “ước lượng”.
