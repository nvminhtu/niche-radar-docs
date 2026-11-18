# 8 · YouTube theo quốc gia + Kênh trend

> Plan 2 · mục 8. Trang YouTube tra được theo nước, và có thêm tab **Kênh trend theo nước**: xem tuần này kênh nào đang ăn view
> ở 1 nước. Không key, không AI.

<span class="chip chip--done">Làm 2026-11-11 · đã code, chưa ra bản</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Anh chốt làm mục này ngày 2026-11-11 (cách B, không key).
</div>

## Đã đo trước khi làm (2026-11-11)

- **Đổi nước mà gõ chữ tiếng Anh thì kết quả gần như y hệt.** Tìm "music", "gaming" ở US và VN ra cùng top video.
  Ra đúng chất từng nước là nhờ **keyword tiếng địa phương**: tìm "nhạc" ở VN ra kênh Việt.
- Gợi ý YouTube (`suggestqueries`, `ds=yt`) đặt `gl` + `hl` theo nước thì trả chữ địa phương thật
  (VN: "anh trai vượt ngàn chông gai", JP: "アンパンマン").
- **YouTube đã bỏ trang Trending.** Gọi `browse FEtrending` qua youtubei.js trả lỗi 400 ở US, VN, JP; thư viện không còn hàm trending.
- Để giao diện YouTube tiếng Việt thì ngày đăng thành "7 ngày trước", hàm đọc số hiện tại không hiểu → tool luôn đọc bằng `lang: 'en'`.

## Tra niche theo nước

- Ô chọn nước có cờ cạnh ô keyword (16 nước: US, GB, CA, AU, IN, PH, VN, JP, KR, TH, ID, BR, MX, ES, DE, FR), mặc định US.
- Gợi ý gửi `gl=<nước>` + `hl=<ngôn ngữ nước đó>`; tìm video dùng phiên InnerTube đặt `location=<nước>`.
- Câu tra lưu là `vn|keyword`; US giữ keyword trơn nên lượt tra cũ vẫn mở được. Chọn nước khác US thì form nhắc gõ keyword bằng tiếng nước đó.

## Kênh trend theo nước

1. Lấy gợi ý YouTube của nước đó cho 6 từ mồi (chữ Latin + chữ bản địa, ví dụ JP: あ か さ た), chọn xen kẽ 15 cụm đang được tìm.
2. Mỗi cụm tìm video **đăng tuần này, phổ biến nhất** (`upload_date: week`, `prioritize: popularity`).
3. Gom theo kênh, xếp theo **tổng view tuần này** của các video lọt top; lấy số sub của 15 kênh đầu.
4. Kênh dưới 100K sub mà view tuần ≥ số sub có nhãn **kênh nhỏ đang lên** (quy ước ShotMatic, không phải số đo).

Trang ghi rõ: đây là **ước lượng từ kết quả tìm kiếm, không phải bảng xếp hạng chính thức**. Kết quả giữ 1 ngày (tra niche giữ 7 ngày).

**Chạy thật 2026-11-11:** mỗi nước ~29 giây, 15 cụm, 0 lỗi. VN: 282 video, 173 kênh (đầu bảng có MixiGaming, FPT Bóng Đá);
US: 274 video, 181 kênh, 5 kênh nhỏ đang lên; JP: 261 video, 155 kênh, cụm và kênh đều tiếng Nhật.

## Code

- Collector: `web/src/collectors/youtube.ts` (`YT_COUNTRIES`, `collectYoutubeTrend`, `pickTrendTerms`).
- Dựng kết quả + câu tra: `web/src/lib/social.ts` (`youtubeTrendView`, `youtubeQuery`, `parseYoutubeQuery`).
- API: `POST /api/social/search` nhận `country`, hoặc `trend: true` + `country` (`web/src/server/social-api.ts`).
- Giao diện: gạt *Tra niche / Kênh trend theo nước* ở trang YouTube (`web/src/client/SocialPage.tsx`).
- Test: `web/tests/social.test.ts`.
