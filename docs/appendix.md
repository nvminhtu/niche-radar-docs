# Appendix · Chưa xếp / Không làm

> Muốn làm mục nào → xếp vào một phase, sửa Master Plan trước. **Không làm lén.**

## Đã xếp vào phase (2026-10-24)

| Mục cũ ở Appendix | Giờ ở |
|---|---|
| App Mac (Tauri) | [App Mac + Windows](app/index.md) (khi xong Version 10) |
| Cờ đối thủ yếu · MCP có sẵn · MCP của app · Chrome Web Store · giá IAP nhiều nước · theo dõi định kỳ · search volume trả phí | ứng viên [Phase 9 · Small Features Update](web/phase-9-small-features.md) |
| Host cho nhiều người | không làm (2026-10-26) — bán app chạy trên máy, xem [Version 10](web/version-10.md) |

## Chưa xếp (2026-10-26)

| Mục | Từ đâu | Ghi chú |
|---|---|---|
| Chế độ tối (dark mode) cho bản Web / app | soát [Phase 25](web/phase-25-ui-ux.md) — app chỉ có giao diện sáng | sáng đã đạt AA; làm khi người mua xin |
| Xuất phạm vi 1 Explore / cả DB qua hộp Xuất chung · JSONL · file JSON Schema | cắt khỏi [Phase 15](web/phase-15-export.md) khi kéo lên sớm | Explore còn nút CSV cũ, cả DB có Backup; làm khi có tool khác cần đọc |

## Không làm (chốt 2026-10-26)

Anh chốt: **bán app Mac + Windows tải về + dùng thử + license**, học mô hình phân phối của
[Wow Keywords](doi-thu-tham-khao.md#wow-keywords). Phase không ra tiền và không thêm người dùng đẩy xuống dưới vạch
**⛔ KO LÀM** ở menu. Trang phase giữ lại để tra, chip ghi "Không làm".

| Không làm | Phase | Vì sao | Thay bằng |
|---|---|---|---|
| Account: tài khoản, đăng nhập Firebase, sync project, lớp tài khoản trên máy | 30, 59, 62, 63 (+ phần xoá tài khoản của 65) | app bán bằng license key, dữ liệu ở máy | license key ([Version 10](web/version-10.md)) · xuất / nhập file ([Phase 8](web/phase-8-project-data.md)) |
| Performance | V5: 46–48 · App 78 | không ra tiền; mốc 2026-10-25 đã ổn (mở ~0,14 s) | — |
| Test tự động | V6: 50–53b | không ra tiền | test hiện có vẫn chạy trước khi merge |
| CI cho PR, quy trình nhánh, build app trên CI | V7: 54, 57 · App 80 | không ra tiền | build + ký trên máy (`npm run mac`) |
| Security audit, refactor, review 8.0 | V8: 58, 60, 61 | không ra tiền | bảo mật tối thiểu cho app bán ở [Phase 35](app/phase-35-app-only.md) |
| Local App 3.0, 4.0 | App 76, 77 | gói theo version chậm | bản cập nhật qua [Phase 37](app/phase-37-release-auto-update.md) |
| Gói lượt AI kèm Pro | phần của 69 | mình gánh tiền AI | AI người dùng đã có (Claude Code, Codex, Ollama, key riêng) |

## Không làm (từ trước)

| Không làm | Vì sao | Thay bằng |
|---|---|---|
| Dịch vụ ước tính trả phí hằng tháng (Sensor Tower, AppTweak, Appfigures, MobileAction) | tốn tiền cho tool nội bộ, số ước tính | proxy miễn phí + Phase 5 verified |
| Sinh concept, giá, spec, checklist ra mắt | pipeline App-AI-Skills đã làm | `/app-research` → `/app-money` → `/app-spec` · brief tính năng (khách · vấn đề · MVP · giá thử) đã gộp vào gói LLM của [Phase 15](web/phase-15-export.md) |
| Tự đăng bài / quảng cáo / thu tiền | việc của người dùng | Phase 7 soạn nháp + lưu số |
| AI tự đưa ra con số | dễ bịa | số từ collector, AI chỉ trích dẫn |
| Dữ liệu TikTok / X | không lấy miễn phí ổn định | Reddit; X đọc tay |
| Electron | nặng | Tauri |

## Nguồn gap bị Bỏ (Phase 14, 2026-10-26)

Chấm ở [Bản đồ nguồn gap](web/gap-sources-map.md). Đừng xét lại nếu chưa có lý do mới (đổi điều khoản, có API mới).

| Nguồn | Vì sao bỏ |
|---|---|
| YouTube suggest · Amazon autocomplete · Pinterest Trends · TikTok Creative Center | chỉ cho thấy cái đã có / hàng vật lý; Amazon, Pinterest, TikTok cấm quét |
| Exploding Topics · Glimpse · AnswerThePublic | trả phí, không có tín hiệu gap; autocomplete miễn phí cho cùng kết quả |
| Indie Hackers · Quora · Discord · nhóm Facebook · MacRumors | gap của founder / nhiễu / cấm quét / không mở được |
| Setapp · Raycast Store · VS Code · WordPress · Figma · G2 · Capterra · Trustpilot · SaaSHub | không có chỗ chê, lệch tệp, hoặc cấm quét kể cả nội dung công khai |
| Acquire · Flippa · Indie Hackers products · Starter Story · Gumroad · Notion / Excel template · CodeCanyon | bằng chứng tiền yếu hoặc cấm quét; TrustMRR đã thay |
| producthunt-mcp-server | không license, bỏ từ 2025-04, API Product Hunt cấm dùng thương mại |

**Ứng viên (chưa xếp phase):** gom chủ đề bằng BERTopic + sentence-transformers thay từ điển tay ở Phase 11 · cờ "top 3
là diễn đàn" cho Phase 59 · nút tiền tố "alternative / vs / free" cho Phase 40 · nhắc theo lịch WWDC cho Phase 42 ·
hạ Amazon (Phase 53–54) xuống ứng viên — chờ anh duyệt.

## Ứng viên từ Phase 12 (2026-10-26)

- Q&A Gap vào hộp **Xuất** của Phase 15 (CSV / JSON / gói AI) — giờ chỉ có **Tải .md**
- Ô nhập key StackApps ở Cài đặt (giờ đọc `STACKEXCHANGE_KEY` từ `.env.local`)
- Chủ đề mới cho từ điển: mạng / IP / hosts, terminal multiplexer (tmux), quyền admin (sudo), ổ cứng / phân vùng
- Thêm site Stack Exchange khác (Ask Ubuntu, Unix & Linux) — chỉ khi có nhu cầu ngoài Mac

[Master Plan §7](superpowers/specs/2026-10-24-niche-radar-master-plan.md)
