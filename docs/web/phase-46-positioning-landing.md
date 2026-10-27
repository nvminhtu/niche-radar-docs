# Phase 46 · Landing shotmatic.app — định vị + email

> Viết **một câu** nói rõ Niche Radar cho ai, giải quyết gì, khác tool khác ở đâu. Rồi dựng **chỗ của mình**:
> landing riêng **[shotmatic.app](https://shotmatic.app)** + form email + đo lượt bấm. Có chỗ này trước thì mọi bài đăng
> sau mới đếm được người về.

<span class="chip chip--done">Xong · landing live 2026-10-27 · shotmatic.app</span>

**Kết quả (2026-10-27, kiểm trên trang live):** [shotmatic.app](https://shotmatic.app) (tiếng Anh) có đủ khối bán hàng:

| | |
|---|---|
| :material-target: **Câu định vị** | hook "Find the app niche that is still open." · nỗi đau "Code is the cheap part. The wrong niche is expensive." · chạy trên AI anh đã trả tiền (không thêm subscription) |
| :material-emoticon-sad-outline: **Nỗi đau + khác biệt** | so 3 niche cạnh nhau (màn Compare thật) · mọi thứ kiểm tay gom 1 màn · AI Hunt thay GummySearch (đóng 01/12) vì không cần Reddit API |
| :material-play-circle-outline: **Demo** | khối "Click through real results" + nút sang demo site |
| :material-tag-outline: **Giá** | $39 mua đứt, dùng trọn đời · dùng thử miễn phí trong lúc beta |
| :material-email-outline: **Form email** | ô email "Get the trial, plus the playbook" → EmailOctopus (list One Click Tool) · thêm `/scorecard`, `/download` |
| :material-chart-line: **GA4** | `G-58F6TSQ8M9`, sự kiện `generate_lead` khi gửi email · `file_download` (đo tự động của GA4) |
| :material-post-outline: **Blog** | [Phase 46.1](phase-46-1-landing-blog.md) — 7 bài, SEO · AEO · GEO |
| :material-help-circle-outline: **FAQ + CTA cuối** | có |

**Còn treo, chuyển sang phase sau (không làm ở 46):**

- `checkout_click` — chưa có nút mua thật (đang beta dùng thử miễn phí). Gắn khi mở bán [Version 10](version-10.md).
- Video demo quay từ app thật — trang đang dùng ảnh màn thật + demo site, chưa có video.

Bản plan gốc (giữ để đối chiếu):

## Câu định vị (5 dòng)

Theo Pha 1 của `/app-gtm`. Anh duyệt 5 dòng này **trước** khi dựng landing — sai định vị thì mọi bài sau đều phí.

| Dòng | Điền gì |
|---|---|
| **Cho ai** | một nhóm hẹp, gọi được tên chỗ họ tụ tập (vd indie dev / người làm app nhỏ đang tìm niche) |
| **Việc họ cần xong** | chọn được 1 niche đáng làm, có số, không đoán |
| **Họ đang dùng** | tool khác, tự mò tay, hoặc không làm gì |
| **Khác một câu** | nhiều nguồn + AI có trích dẫn + chạy trên máy |
| **Bằng chứng** | link thread / review thật. Không có link thì định vị là đoán |

## Làm gì

| | |
|---|---|
| :material-target: **Định vị** | 5 dòng ở bảng trên, ghi vào `marketing/gtm.md` qua `/app-gtm` (Pha 0 điểm xuất phát + Pha 1) |
| :material-emoticon-sad-outline: **3 nỗi đau** | lấy từ chính dữ liệu Reddit / review mà tool đọc được về "app idea", "niche". Mỗi nỗi đau có link nguồn |
| :material-web: **Landing riêng** | **shotmatic.app** (tiếng Anh, repo landing ShotMatic): hook · video demo quay từ app thật · 3 nỗi đau · tính năng · giá khớp [Version 10](version-10.md) · FAQ · CTA |
| :material-file-document-check: **Khúc cuối = Brief + Spec** | dải các bước kết bằng hồ sơ Brief + Spec + Plan, ảnh tab Brief thật + hồ sơ mẫu `.md` thật của 1 niche dogfood ([Phase 28.5](phase-28-5-brief-plan.md#tren-landing-demo-khach-nhin-la-hieu-khuc-cuoi-co-brief)) |
| :material-email-outline: **Form email** | form trên landing + mồi một dòng. Anh tự mở tài khoản dịch vụ email |
| :material-chart-line: **GA4 sự kiện** | `download`, `checkout_click`, `generate_lead`. Link đo nguồn dạng `?utm_source=<kênh>&utm_campaign=niche-radar` |
| :material-check-decagram: **Kiểm** | `check_landing.py` tới 0 lỗi, mở trang xem tận mắt ở 1280 và 375 |

<div class="box box--star" markdown>
**Xong khi**

- 5 dòng định vị có bằng chứng, anh duyệt
- Landing live, `check_landing.py` qua, đã xem ở 1280 + 375
- Gửi 1 email test → vào đúng danh sách
- Bấm thử nút tải / mua / gửi email → GA4 thấy đủ 3 sự kiện `download`, `checkout_click`, `generate_lead`
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Đăng bài ở kênh nào (để Phase 47–49)
- Bịa số người dùng, lời khen của khách trên landing
- Đổi giá so với [Version 10](version-10.md)
- Quảng cáo trả tiền
</div>

[Tổng quan Version 11](version-11.md)

Plan code chi tiết: [Phase 46](../superpowers/plans/2026-10-25-niche-radar-phase70-positioning-landing.md)
