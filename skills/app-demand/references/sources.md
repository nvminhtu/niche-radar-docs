# app-demand — nguồn và tool đã kiểm (2026-10-14)

Số sao GitHub đo bằng `gh api repos/<repo>` ngày 2026-10-14. Đo lại trước khi trích.

## Nguồn dữ liệu dùng trong skill

| Nguồn | Cách lấy | Cho biết | Không cho biết |
|---|---|---|---|
| TrustMRR `startup/<slug>.md` | `demand_research.py trustmrr` (công khai) | doanh thu 30 ngày/tổng/MRR **verified**, provider, X follow, giá + persona + kênh (tự khai) | tìm theo từ khoá (phải WebSearch `site:trustmrr.com`) |
| TrustMRR `api/ai/discovery` | `trustmrr-discover` (công khai) | 25 tăng nhanh nhất + 25 mới | lọc, phân trang |
| TrustMRR `api/v1/startups` | `trustmrr-list` — cần `TRUSTMRR_API_KEY` (người dùng tự tạo ở dashboard) | lọc theo category, teamSize, MRR, growth; 10 dòng/trang, 10 lần/phút | tìm chữ (script lọc tại chỗ bằng `--q`) |
| App Store | `store_research.py` (endpoint công khai Apple) | hạng, số đánh giá (proxy), tuổi app, autocomplete, review, IAP | lượt tải, doanh thu |
| Google Play | `demand_research.py play` (trang HTML) | lượt cài dạng dải, ★, số review, có IAP/ads, ngày cập nhật | doanh thu; HTML đổi thì regex hỏng → SKIP |
| Hacker News | `demand_research.py hn` (Algolia, không key) | Show HN đối thủ mới, comment than/so sánh | người dùng phổ thông |
| GitHub | `demand_research.py github` (10 lần/phút không token) | đồ free thay thế, có còn được bảo trì | |
| Reddit | WebSearch `site:reddit.com …` (search.json trả rỗng khi gọi thẳng, đo 2026-10-14) | câu than, "is there an app" | |
| X | người dùng tự tìm bằng câu trong method.md §2 | ai đang hỏi, ai đang ra mắt | |
| Google Trends | MCP `google-trends` (`compare_keywords`, `get_related_queries`) | xu hướng tương đối | lượng tìm tuyệt đối |

## Skill/tool trên GitHub đã xem — lấy gì, bỏ gì

| Repo | ★ | Lấy | Không cài vì |
|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 54,576 | `customer-research` (3 chế độ, độ tin cao/vừa/thấp, lệch mẫu), `competitors` (kỷ luật bằng chứng: "không thấy" ≠ "không có", ghi ngày) | bộ marketing chung cho SaaS; phần research đã gom ở đây. Đáng xem lại khi làm landing/CRO/ASO |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | 54,106 | khung market research nhiều bước | cả một quy trình dev agile, nặng so với nhu cầu |
| [slavingia/skills](https://github.com/slavingia/skills) | 10,871 | `validate-idea` (validate bằng bán, cờ đỏ/xanh), `first-customers` (vòng tròn đồng tâm, bán trước khi launch) | ngắn, đã gom hết ý chính |
| [facundoolano/google-play-scraper](https://github.com/facundoolano/google-play-scraper) | 2,981 | — | Node + npm; `demand_research.py play` đủ cho nhu cầu, không thêm phụ thuộc. Cần đào sâu (review Play hàng loạt) thì cài |
| [facundoolano/app-store-scraper](https://github.com/facundoolano/app-store-scraper) | 1,432 | — | `store_research.py` đã phủ bằng endpoint công khai |
| [JoMingyu/google-play-scraper](https://github.com/JoMingyu/google-play-scraper) | 1,017 | — | bản Python, push cuối 2024-08 |
| [ailabs-393/ai-labs-claude-skills](https://github.com/ailabs-393/ai-labs-claude-skills) | 457 | — | `startup-validator` chung chung, không có nguồn số |

Dịch vụ trả phí (Sensor Tower, Appfigures, AppMagic…) có ước lượng doanh thu app nhưng là **ước lượng** — nếu người dùng
có tài khoản và đưa số, ghi nhãn `proxy (ước lượng của <dịch vụ>)`, không bao giờ `verified`.
