# 15 · Theo dõi ngách YouTube + chấm giai đoạn video

> Plan 2 · mục 15. Khi Săn kênh nhỏ (mục 11) tìm ra một kênh nhỏ đang nổ view, ta **gom các kênh cùng ngách vào một danh sách theo dõi**.
> Máy đọc lại danh sách đó **mỗi ngày** và gắn cho từng video một nhãn: **sắp nổ · đang nổ · đã nổ**.
> Agent (Claude) đọc được kết quả qua MCP. Không cần key, không cần AI.

<span class="chip chip--doing">15.7 đã code 2026-11-15 · 15.1–15.6 chờ anh duyệt</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này ghi lại góp ý của Tran (2026-11-15). Chỉ code khi anh chốt.
</div>

## Vì sao làm

Góp ý của Tran, tóm lại:

- vidIQ, 1of10, TubeLab, OutlierKit đều đã có **tìm video vượt trội** (video nổ gấp nhiều lần mức trung bình của kênh), lại có kho dữ liệu khổng lồ.
  Từ 2026-09, chính YouTube Studio cũng có tab Research. Ta không thắng được ở khoản dữ liệu.
- Phần họ **không làm thành quy trình**: kênh nhỏ nổ view → gom mọi kênh cùng ngách → theo dõi mỗi ngày → nhận ra xu hướng trong ngách rồi làm theo.
- Xu hướng là chạy bằng agent, nên thêm nhãn video **sắp nổ / đang nổ / đã nổ** để agent có cái mà đọc.

Các tool kia chỉ chụp số tại **một thời điểm**. Muốn biết một video đang lên hay đã hết đà thì phải có số của **nhiều ngày**. Đó là chỗ mục này lấp vào.

## Đã có sẵn, dùng lại

| Có sẵn | Ở đâu | Dùng cho |
|---|---|---|
| Phễu Săn kênh nhỏ 100 → 10 → 3 | `collectors/youtube-hunt.ts`, `lib/youtube-hunt.ts` | nguồn kênh đầu tiên cho danh sách theo dõi |
| Đọc 1 kênh + 30 video gần nhất (~0,9 giây / kênh) | `collectors/youtube-channel.ts` | lần đọc mỗi ngày |
| View / giờ, × kênh | `lib/yt-trend-verdict.ts` | đầu vào để chấm giai đoạn |
| Nhãn 🚀 Sắp nổ · 🔥 Đang nổ · 🏆 Đã nổ (làm 2026-11-14, đang hiện ở Soi 1 kênh, Kênh trend, kết quả tìm) | `lib/video-heat.ts`, `client/heat-ui.tsx` | giữ nguyên chip + hàng đếm, chỉ đổi cách tính khi có số nhiều ngày |
| Theo dõi định kỳ (PRO, mốc 7 / 30 / 90 ngày) | `lib/tracking.ts` | cách hiện "đến hạn / quá hạn" và cách khoá PRO |
| Mini app thanh menu bật server web (máy dev) | `app/mini/` | chạy lịch hằng ngày khi web không mở |
| MCP niche-radar, `get_youtube` | `mcp/tools.ts` | thêm tool cho agent |

## Luồng

### 1 · Tạo danh sách theo dõi

- Trên trang kết quả Săn kênh nhỏ có nút **＋ Theo dõi ngách này**. Bấm vào thì thêm 3 kênh đã chốt và mọi kênh đã qua bước lọc 2 (tối đa 30 kênh).
  Tên danh sách là chủ đề đã săn, nước giữ theo lần săn.
- Trên trang Soi 1 kênh có nút **＋ Thêm vào danh sách theo dõi** (chọn danh sách có sẵn hoặc tạo mới).
- Trong trang danh sách có thể dán link kênh để thêm hoặc bỏ kênh.
- Tuỳ chọn **Tìm kênh cùng ngách**: lấy cụm keyword của kênh đã chốt, chạy lại bước 1 của phễu, rồi đề xuất kênh mới. Kênh mới chỉ vào danh sách khi anh tick.

### 2 · Đọc lại mỗi ngày

- Mỗi danh sách được đọc **1 lần / ngày**: số sub của kênh và 30 video gần nhất kèm số view.
  30 kênh mất khoảng 30 giây, chạy chung hàng đợi YouTube hiện có.
- Server web đang chạy (app Mac, hoặc mini app thanh menu trên máy dev) thì máy tự đọc lúc 7:00 sáng (giờ máy). Không có thì lần mở web đầu tiên trong ngày sẽ hiện thanh **Chưa đọc hôm nay · Đọc ngay**.
- Máy tắt cả ngày thì ngày đó không có số. Không đoán bù: biểu đồ để trống ngày đó.
- Lần đầu thấy một video thì ghi lại giờ thấy. Từ đó tuổi video tính theo số ta tự ghi, không dùng chữ ước lượng "3 weeks ago".

### 3 · Chấm giai đoạn từng video

**Đã có bản 1 lần tra** (`lib/video-heat.ts`, 2026-11-14): chỉ dựa vào tuổi video và view ÷ mức nền của kênh.
Video vượt kênh trong 30 ngày thì là Đang nổ, cũ hơn là Đã nổ. Vì chỉ có số của một lần tra, bản này không phân biệt được
video **vẫn đang lên** với video **đã hết đà**.

Mục này thêm cách tính thứ hai, chỉ dùng khi video đã có **từ 2 lần đọc** trong danh sách theo dõi. Video chưa đủ số thì vẫn dùng cách cũ.
Chip, icon và hàng đếm giữ nguyên, chỉ thêm chấm nhỏ "theo số nhiều ngày" trong ⓘ để biết nhãn được tính bằng cách nào.

Mỗi video có **view thêm / ngày** (lấy số hôm nay trừ lần đọc trước, chia số ngày). Mức chuẩn của kênh là **trung vị view thêm / ngày** của các video trong kênh tuổi 2–30 ngày.

| Nhãn | Khi nào | Ý nghĩa |
|---|---|---|
| 🚀 **Sắp nổ** | video ≤ 3 ngày tuổi, view / giờ ≥ 3× trung vị view / giờ của các video ≤ 3 ngày trong kênh | còn sớm, đáng làm theo ngay |
| 🔥 **Đang nổ** | view thêm / ngày ≥ 3× mức chuẩn của kênh, và hôm nay ≥ 70% hôm qua | vẫn đang lên, chủ đề còn nóng |
| 🏆 **Đã nổ** | tổng view ≥ 10× sub (hoặc ≥ 5× trung vị view của kênh), và view thêm / ngày < 30% ngày cao nhất | đã chứng minh có cầu nhưng hết đà, làm lại phải có góc mới |
| · Thường | còn lại | |

- Ngày đầu video chỉ có 1 lần đọc, nên nhãn theo cách cũ (`videoHeat`). Từ ngày thứ hai thì chuyển sang cách mới.
- Mọi ngưỡng là quy ước của ShotMatic, không phải số đo. Cách mới viết thành hàm `videoHeatTrend` trong `web/src/lib/video-heat.ts`, có test.
- Không hứa "dự đoán viral". Nhãn chỉ nói video **đang** chạy thế nào so với chính kênh của nó.

### 4 · Xu hướng trong ngách

Gom tiêu đề của các video **Sắp nổ + Đang nổ** trong cả danh sách và rút cụm keyword lặp lại (dùng lại cách rút keyword của mục 11).

- **Cụm mới**: tuần này có ở ≥ 2 kênh, tuần trước chưa có ở kênh nào.
- **Cụm đang nóng**: có ở ≥ 3 kênh, tổng view thêm / ngày tăng so với tuần trước.
- **Cụm nguội**: tuần trước nóng, tuần này không còn video Đang nổ nào.
- Bấm vào cụm thì mở *Tìm ý tưởng* với cụm đó (giống keyword ở mục 11).

## Trang danh sách theo dõi

Trang YouTube có thẻ lối vào thứ năm **Theo dõi ngách**. Mở ra là các danh sách. Mỗi danh sách hiện số đếm 🚀 / 🔥 / 🏆 của hôm nay và giờ đọc gần nhất.

Trong 1 danh sách, từ trên xuống:

- **Dải hôm nay**: hàng đếm 🚀 Sắp nổ · 🔥 Đang nổ · 🏆 Đã nổ có sẵn trong `heat-ui.tsx` (bấm để lọc), giờ đọc gần nhất, nút Đọc ngay.
- **Cụm keyword**: chip Mới / Nóng / Nguội, mỗi chip kèm số kênh đang làm.
- **Video**: thumbnail, nhãn, thanh × mức chuẩn của kênh, đường nhỏ view thêm / ngày trong 14 ngày, tên kênh. Mặc định xếp Đang nổ trước.
- **Kênh**: sub hôm nay và mức tăng sub trong 7 ngày, số video Đang nổ, nút Soi kênh.

Theo luật UI bớt chữ: giải thích nhãn và ngưỡng gập vào ⓘ, không viết thành đoạn văn trên trang.

## Cho agent

### 15.7 · Agent tự tra YouTube (học từ TubeLab MCP)

<span class="chip chip--done">Làm 2026-11-15 · đã code, chưa ra bản</span>

TubeLab và vidIQ đều bán **YouTube Data MCP**: người dùng hỏi Claude hoặc ChatGPT "ngách của tôi đang trend gì?",
AI tự gọi tool tìm video vượt trội, soi kênh, đọc phụ đề, rồi trả lời bằng số thật.

Trước mục này, MCP của ShotMatic chỉ có `get_youtube`, **đọc lại lượt đã tra**, không tra mới được. Giờ có thêm 5 tool, dùng lại đúng hàm của trang YouTube:

| Tool | Làm gì | Dùng lại |
|---|---|---|
| `youtube_outliers` | chủ đề + nước → video vượt kênh (× kênh), view ÷ sub, nhãn nổ, điểm Cầu / Chỗ, kênh, comment | Tra niche |
| `youtube_hunt` | chủ đề + nước + kỳ → chạy đủ phễu 100 → 10 → 3, kênh chốt + điểm + keyword + video nổ | Săn kênh nhỏ (3 bước trong 1 lần) |
| `youtube_channel` | link kênh / link video / @tên → sức khoẻ, cầu, nhóm nội dung, keyword, video vượt / tụt kèm nhãn nổ + videoId | Soi 1 kênh |
| `youtube_transcript` | 1–5 id video → hook 30 giây đầu, mốc từng đoạn, cụm lặp, chữ / phút, lời mẫu đầu-giữa-cuối | phụ đề client IOS + bảng `video_transcripts` |
| `youtube_job` | hỏi tiến độ lượt tra đang chạy, xong thì trả kết quả | sổ việc của Buồng lái |

`get_youtube` đọc thêm được lượt Săn kênh nhỏ và Soi 1 kênh (theo searchId), video có nhãn nổ, bỏ câu "chưa có phụ đề".

**Cách chạy**

- Tool là loại "ghi" như `start_research`: cần app đang mở + bật **Cho AI thêm dữ liệu**. Mỗi lượt tra lưu vào lịch sử trang YouTube như khi tự bấm.
- Chạy nền trong sổ việc, nên **Buồng lái thấy**, và tab cùng loại trên trang YouTube bị khoá như khi tự bấm. Mỗi loại chỉ 1 lượt một lúc.
- Xong trong 20 giây thì trả kết quả luôn. Lâu hơn thì trả mã việc (`social:12`), agent gọi `youtube_job` sau khoảng 30 giây.
- Lượt đã có thì dùng lại: Tra niche và Soi kênh trong 7 ngày, Săn kênh trong ngày.
- Mỗi kết quả kèm nguồn `YouTube #id · ngày · youtubei.js` và vừa trần 8.000 ký tự của tool (bớt comment, kênh, video thừa trước).
- Không key, không AI trong tool: tool chỉ trả số. Phần nhận xét để agent làm.
- **Không làm bản chạy trên máy chủ** (dán URL vào claude.ai như TubeLab): phải có server, tài khoản và giới hạn lượt gọi, trái với hướng chạy trên máy.

**Chạy thật 2026-11-15** (YouTube thật, DB tạm, đi qua API `/api/mcp/youtube/*`):

- `youtube_outliers` "habit tracker app": xong sau ~30 giây (lần đầu trả mã việc, hỏi lại là có).
- `youtube_channel` kênh của video đầu: 9 giây, 10 video vượt kênh.
- `youtube_transcript` video đó: phụ đề tiếng Anh 1.586 chữ, có hook.
- `youtube_hunt` "habit tracker" (US, tháng): 110 giây, phễu 100 → 5 kênh qua lọc, kênh chốt 387–4.810 sub, điểm 49–73.

**Còn chờ anh chốt:** giới hạn bản Free qua MCP (đề xuất 3 lượt tra mới / ngày). Hiện chưa giới hạn riêng, chỉ có giới hạn chung 20 lần ghi / phút và mỗi loại 1 lượt một lúc.

Câu hỏi mẫu cho Claude Desktop / Claude Code: "ngách X đang có video nào nổ?", "soi kênh này rồi gợi ý 10 tiêu đề", "đọc lời video này, hook là gì?".

Code: `web/src/lib/youtube-agent.ts` (chạy phễu đủ + đổi kết quả cho AI), `web/src/server/mcp-write-api.ts` (API), `web/src/mcp/write-tools.ts` (tool). Test: `web/tests/youtube-agent.test.ts`.

### Danh sách theo dõi

- `list_watchlists`: các danh sách, số kênh, ngày đọc gần nhất, số đếm 3 nhãn.
- `get_watchlist`: video theo nhãn (kèm view, view thêm / ngày, × mức chuẩn, link), cụm keyword Mới / Nóng / Nguội, ngày đọc. Mỗi số kèm nguồn (Theo dõi #id, ngày đọc).
- `add_to_watchlist` (tool ghi, cần bật "Let AI add data"): thêm kênh theo link. Không xoá, không đổi số.

**vidIQ MCP**: không nối vào server, để giữ đúng tiêu chí không cần key. Agent của người dùng gọi song song vidIQ MCP (dữ liệu lớn, mỗi lần gọi tốn credit) và niche-radar (theo dõi ngách hằng ngày).
Trong hướng dẫn, ghi một đoạn mẫu cho Claude: "lấy cụm Nóng từ niche-radar → hỏi vidIQ về từ khoá đó".

## Lưu số

| Bảng mới | Cột chính |
|---|---|
| `yt_watchlists` | id, tên, nước, nguồn (hunt #id / tay), giờ tạo, bật / tắt |
| `yt_watch_channels` | watchlistId, channelId, tên, giờ thêm, nguồn |
| `yt_channel_snaps` | channelId, ngày, sub |
| `yt_video_snaps` | videoId, channelId, ngày, view, giờ thấy lần đầu, tiêu đề |

Mỗi video có 1 dòng / ngày. 30 kênh × 30 video ≈ 900 dòng / ngày / danh sách. Sau 90 ngày, máy gộp số cũ còn 1 dòng / tuần.

## Chia việc

1. **15.1** Bảng + nút ＋ Theo dõi ngách ở Săn kênh nhỏ + trang danh sách (chưa có nhãn). Đọc tay bằng nút Đọc ngay.
2. **15.2** Thêm `videoHeatTrend` vào `video-heat.ts` + test, nối vào hàng đếm có sẵn, thêm đường 14 ngày.
3. **15.3** Lịch đọc mỗi ngày trong server web + thanh "Chưa đọc hôm nay".
4. **15.4** Cụm keyword Mới / Nóng / Nguội.
5. **15.5** Tool MCP danh sách theo dõi + đoạn hướng dẫn dùng chung với vidIQ MCP.
6. **15.6** Tìm kênh cùng ngách (đề xuất kênh mới cho danh sách).
7. **15.7** Agent tự tra YouTube: `youtube_outliers`, `youtube_hunt`, `youtube_channel`, `youtube_transcript`, `youtube_job`, sửa `get_youtube`. **Đã code 2026-11-15.**

Làm xong 15.1 + 15.2 là đã cho Tran thử được. Nhãn cần ít nhất 2 ngày số, nên nên bật danh sách sớm để có số chạy dần.

## Cần anh chốt

- **Free hay PRO?** Đề xuất: Free có 1 danh sách tối đa 10 kênh, PRO không giới hạn và có đọc tự động mỗi ngày (giống Theo dõi định kỳ).
- **Số kênh tối đa / danh sách**: đề xuất 30 (khoảng 30 giây / lần đọc).
- **Giờ đọc tự động**: đề xuất 7:00 sáng.
- **Làm ngay hay sau Marketing?**
- ~~15.7 làm trước hay sau?~~ Anh chốt làm trước (2026-11-15), đã code.
- **Giới hạn bản Free qua MCP**: đề xuất 3 lượt tra mới / ngày, đọc lại lượt cũ thì không giới hạn.

## Giới hạn

- Số liệu chỉ có từ ngày bắt đầu theo dõi. Không có lịch sử view theo ngày của quá khứ (YouTube không cho xem khi không đăng nhập).
- Kết quả không đăng nhập gần như không có Shorts (đo 2026-11-12), nên danh sách hợp với kênh video dài.
- 30 video gần nhất / kênh: video cũ hơn mà bỗng nổ lại sẽ không được thấy. Đây là trường hợp hiếm, ghi chú trong ⓘ.
- Máy tắt thì không đọc. Ngày trống được để trống, không bịa số.
