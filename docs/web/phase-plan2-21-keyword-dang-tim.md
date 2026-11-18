# 21 · YouTube trend: keyword đang được tìm + Google Trends

> Plan 2 · mục 21. Tab **Xem đang trend gì** của trang YouTube thêm phần **keyword**: chữ người dùng đang gõ,
> chữ nào đang lên theo **Google Trends lọc YouTube Search**, và vài biểu đồ đọc một lần là biết nên làm keyword nào.
> Không cần key, không cần AI.

<span class="chip chip--todo">Viết 2026-11-15 · chốt + code 2026-11-16</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này ghi lại câu anh hỏi ngày 2026-11-15. Chỉ code khi anh chốt.
</div>

## Vì sao làm

Anh hỏi (2026-11-15): tab trend đang cho xem kênh và video trend, vậy có xem được **keyword người dùng đang tìm** không,
kết hợp **Google Trends**, và dùng chart (tròn, cột, kiểu hiện đại) để **nhìn một phát là biết** được không.

## Tab trend đang có gì (đọc code 2026-11-15)

- **Bảng "Đang được tìm"** (`web/src/client/YtTermBoard.tsx`): hỏi ô gợi ý của YouTube bằng vài chữ đầu theo từng nước
  (`a`, `m`, `s`… cho US · `đ`, `c`… cho VN, ở `web/src/collectors/youtube.ts`), gom thành cụm có nhãn, số video và kênh dẫn đầu.
  Đây là chữ người dùng gõ thật, nhưng **không có lượt tìm**. YouTube không công bố số này.
- **Chart cho kênh** (`web/src/components/charts/YtTrendCharts.tsx`): thanh top kênh, thanh chia theo cỡ kênh,
  bản đồ nhiệt kênh × nước, chấm sub / view, đường lịch sử.
- **Chưa có:** Google Trends cho keyword trong tab này, và chưa có chart nào cho keyword.

## Đã có sẵn, dùng lại

- `youtubeTrend()` (Phase 51.1, gọi trong `web/src/lib/social.ts` ở tab Tìm ý tưởng): đưa tối đa 5 keyword qua Trends lọc YouTube Search
  trong 1 lần gọi, cache 1 ngày, bị chặn thì ghi lỗi mà phần khác vẫn đủ.
- `cachedTrends()` (`web/src/lib/trends-deep.ts`): cache mọi lần gọi Trends trong DB.
- Khối Rising queries của Soi 1 kênh (mục 17.2, `web/src/collectors/channel-trends.ts`).
- Khối kết luận `VerdictCard` và hàng chấm `DotRow` (`web/src/client/verdict-ui.tsx`), thư viện `recharts` có sẵn cột, tròn, chấm.

## Đã đo (2026-11-15)

- **Trends lọc YouTube Search, 5 keyword trong 1 lần gọi:** `interestOverTime` với minecraft · roblox · fortnite · asmr · mukbang, nước US, 90 ngày.
  Trả về trong 0,9 giây, 91 điểm mỗi ngày, cùng một thang 0–100 nên so được với nhau (trung bình 52 · 50 · 24 · 71 · 7).
- **Rising queries lọc YouTube Search, 1 keyword:** `relatedQueries` "minecraft", US, 90 ngày, mất 3,8 giây.
  5 dòng đầu đều là Breakout (tăng vọt từ gần 0).
- **RSS Trending now của Google theo nước:** `trends.google.com/trending/rss?geo=VN` trả 200, 10 chủ đề, có số tìm ước lượng ("200+").
  Đây là tìm trên **Google**, không phải YouTube.
- **Không làm được:** biết số lượt tìm thật trên YouTube, hay video nào đang nằm trong tab Trending (YouTube đã bỏ trang này, `FEtrending` trả 400, đo 2026-11-11).

## 21.1 · Khối kết luận đầu phần keyword

Một thẻ `VerdictCard` đứng đầu: **"Nên làm: early morning routine"** + số lớn (mức tìm 0–100) + 1 dòng lý do
("đang lên 40% · mới 6 video trong tuần"). Chọn keyword có mức tìm cao, đang lên và ít video nhất trong 5 keyword đã đưa qua Trends.
Giải thích cách chọn gập vào ⓘ.

## 21.2 · Đường xu hướng 5 keyword

- Lấy 5 cụm đầu của bảng "Đang được tìm", đưa qua `youtubeTrend()` (1 lần gọi, khoảng 1 giây).
- Kỳ theo nút kỳ của tab: **Tuần → 7 ngày · Tháng → 90 ngày · Năm → 12 tháng**.
- Vẽ đường nhiều màu, mỗi đường 1 keyword, rê chuột xem số từng ngày. Mỗi keyword có nhãn **Lên / Ngang / Xuống** (so nửa sau với nửa đầu kỳ).
- Trong bảng "Đang được tìm" thêm cột nhỏ: sparkline + nhãn cho 5 cụm này. Các cụm còn lại có nút **Đo Trends** (đo thêm 5 cụm / lần bấm).

## 21.3 · Cột "Đang lên"

- Rising queries lọc YouTube Search cho **2 keyword đầu** (khoảng 8 giây, chạy sau khi phần khác đã hiện).
- Vẽ cột ngang, dài theo % tăng. **Breakout** vẽ thành cột đầy + chip lửa, đứng trên cùng.
- Bấm một dòng là mở tra keyword đó ở tab Tìm ý tưởng.

## 21.4 · Bong bóng cầu – cung

- Mỗi keyword là 1 bóng. **Trục ngang** = mức tìm trên Trends (cầu) · **trục dọc** = số video đăng trong kỳ có chữ đó (cung) ·
  **cỡ bóng** = tổng view của các video đó.
- Chia 4 góc có chữ mờ: **Nên làm** (tìm nhiều, ít video) · **Đông** (tìm nhiều, nhiều video) · **Ngách nhỏ** · **Bỏ qua**.
- Chỉ vẽ keyword đã có số Trends. Thiếu số thì không vẽ, không đoán.

## 21.5 · Vòng tròn chia nhóm

- Donut chia keyword (hoặc view) theo nhóm nội dung đã có sẵn (`hasFormatData`, `countFormats`): game, nhạc, hướng dẫn…
- **Tối đa 5 phần**, phần còn lại gộp thành "Khác". Không dùng pie nhiều lát vì khó so.
- Giữa vòng ghi số lớn: nhóm chiếm nhiều nhất + %.

## 21.6 · Google đang tìm gì hôm nay

- Cột bên: 10 chủ đề từ RSS Trending now theo nước đang chọn, mỗi dòng có số tìm ước lượng ("200+").
- Ghi rõ **"trên Google, không phải YouTube"**. Chủ đề nào cũng có trong bảng "Đang được tìm" thì gắn chip "cũng tìm trên YouTube".

## Chi phí gọi Trends mỗi lượt

| Phần | Lần gọi | Thời gian (đo 2026-11-15) |
|---|---|---|
| 21.2 Đường 5 keyword | 1 | ~0,9 giây |
| 21.3 Rising 2 keyword | 2 | ~7,6 giây |
| 21.6 RSS Trending now | 1 | chưa đo thời gian |

Tất cả đi qua cache 1 ngày. Lượt chạy nhiều nước thì chỉ đo nước đầu tiên, nước khác bấm mới đo, để không bị Google chặn.

## Chia việc

1. 21.2 + 21.1: nối `youtubeTrend()` vào lượt trend, lưu kèm kết quả, vẽ đường + nhãn + thẻ kết luận. Hàm chọn keyword "Nên làm" là hàm thuần có test.
2. 21.3: rising chạy sau, cập nhật tại chỗ.
3. 21.4 + 21.5: hai chart mới trong `YtTrendCharts.tsx`, hàm tính số ở `web/src/lib/yt-trend-charts.ts` có test.
4. 21.6: collector RSS + cache + cột bên.
5. Soát 960px và 1340px, sáng / tối, tiếng Việt / English (skill `tool-chart`).

## 21.7 · Lọc theo chủ đề + đối tượng ước đoán

Anh hỏi thêm (2026-11-16): lọc bảng keyword theo sở thích, tuổi, giới tính, nghề được không.

- **Không có số thật cho tuổi, giới tính, nghề theo keyword.** YouTube chỉ cho chủ kênh xem người xem của chính kênh mình;
  Google Trends và YouTube không công khai số này theo keyword. Tool không làm cột tuổi / giới / nghề.
- **Chủ đề (sở thích) = thể loại YouTube** của 2 video xem nhiều nhất mỗi cụm (`getBasicInfo` → `category`, ví dụ Gaming,
  Film & Animation, Music). Đo 2026-11-16: "siêu nhân", VN, 3 video, 80–170 ms / video. Đây là số thật của YouTube.
- Chip lọc theo chủ đề nằm trên bảng "Đang được tìm"; donut 21.5 chia theo chủ đề này (tối đa 5 phần + "Khác").
- **Chip "đối tượng (đoán)"**: Trẻ em / Game thủ / Nghe nhạc / Học / Làm đẹp, suy từ thể loại + chữ trong cụm
  (ví dụ "cho bé", "kids", "hoạt hình"). Ghi rõ là đoán trong ⓘ, không phải số đo.

## Đã chốt (2026-11-16)

1. Đo Trends **tự động** cho 5 cụm đầu mỗi lượt trend; cụm khác bấm **Đo thêm 5 cụm**.
2. Rising **tự gọi** cho 2 cụm đầu.
3. **Có làm** 21.6 Google Trending now, ghi rõ nguồn là Google.
4. Thêm 21.7 lọc chủ đề + chip đối tượng ước đoán.

## Giới hạn

- Google Trends chỉ cho **thang 0–100 tương đối**, không cho số lượt tìm thật. Số trên UI ghi "mức tìm", không ghi "lượt tìm".
- Trends dễ chặn khi gọi dồn: luôn qua cache, bị chặn thì phần kênh / video vẫn hiện đủ, phần keyword ghi lỗi.
- Keyword nhiều nước khác ngôn ngữ thì đo theo nước của keyword đó, không gộp các nước vào một thang.

## Nguồn

- Đo trực tiếp bằng thư viện `google-trends-api` (`property: 'youtube'`) và RSS `trends.google.com/trending/rss`, 2026-11-15.
- Mục liên quan: [17 · Soi kênh: Google Trends, keyword, so kênh](phase-plan2-17-trend-keyword-so-kenh.md).
