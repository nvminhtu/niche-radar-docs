# 19 · Soi kênh: làm theo kênh bằng mẫu kịch bản

> Plan 2 · mục 19. Trang **Soi 1 kênh** (mục 7) có 2 thay đổi:
> (A) tiêu đề video hiện đúng ngôn ngữ của nước đã chọn;
> (B) khối mới **Làm theo kênh**. Chọn các video đã chứng minh, AI đọc phụ đề thật và viết **1 mẫu kênh** + **1 mẫu cốt truyện cho mỗi video**.
> Mẫu viết xong thì dừng, không viết kịch bản đầy đủ.

<span class="chip chip--todo">Viết 2026-11-15 · chờ anh duyệt</span>

## Vì sao làm

Anh nêu 2 việc (2026-11-15):

1. Soi kênh lịch sử tiếng Việt mà bảng Từng video lẫn lộn tiêu đề tiếng Anh ("How did Guan Zhong…", "The Entire Life of Napoleon…")
   với tiếng Việt ("Tư Mã Ý…"). Chọn nước nào thì tiêu đề phải ra ngôn ngữ của nước đó.
2. Soi xong kênh, anh muốn **làm theo kênh**: chọn các video không flop, ra 1 khuôn chung của kênh
   (giọng kể, kiểu story, thể loại, người xem…), rồi đi chi tiết từng video để làm y chang hoặc hao hao.
   Chạy 5 video thì có 5 mẫu cốt truyện. Người hoặc AI đọc mẫu rồi viết kịch bản (sửa, cải tiến tính sau).

## A · Tiêu đề đúng ngôn ngữ

**Nguyên nhân (đọc code 2026-11-15):**

- Phiên InnerTube luôn tạo với `lang: 'en'` (`web/src/collectors/youtube.ts`), vì `parseAge` / `parseCount` chỉ đọc được
  chữ tiếng Anh ("3 days ago", "1.2K views").
- Kênh có đặt tiêu đề nhiều thứ tiếng (hoặc YouTube tự dịch tiêu đề) thì phiên tiếng Anh nhận bản tiếng Anh.
- `channelFull` gọi `ytSession()` không truyền nước, nên lúc nào cũng đọc kênh theo US, kể cả khi anh chọn VN.

**Cách sửa:**

1. `channelFull(id, gl)` nhận nước của lượt soi.
2. Số view, ngày đăng, độ dài vẫn đọc bằng phiên tiếng Anh như cũ (không đụng bộ đọc số).
3. Thêm 1 lượt đọc tab Videos bằng phiên có `lang = YT_COUNTRIES[gl].hl` (VN → `vi`), chỉ lấy `id → tiêu đề`,
   rồi ghép đè tiêu đề theo id. Nước có `hl = 'en'` thì bỏ qua lượt này.
4. Lượt đọc thêm lỗi → giữ tiêu đề tiếng Anh, ghi vào `errors`, lượt soi vẫn chạy.
5. Rút keyword từ tiêu đề (`channelKeywordCandidates`) dùng tiêu đề đã ghép, nên keyword cũng ra tiếng địa phương.

Thời gian thêm: `chưa đo` (ước 1–2 giây cho 3 trang video). Đo lại khi code.

## B · Khối Làm theo kênh

### Chọn video

- Bảng Từng video có thêm cột ô tick.
- App **tick sẵn** video đã chứng minh: × kênh ≥ 1 **và** đăng đủ 7 ngày (bỏ dòng "Running" vì còn quá mới để kết luận).
- Anh bỏ tick hoặc tick thêm tuỳ ý. Tối đa **10 video** một lượt (bằng `TRANSCRIPT_BATCH_MAX` của route đọc phụ đề).
- Video không có phụ đề → ghi "không có phụ đề", không đưa vào mẫu.

### Luồng

1. Nút **Đọc phụ đề + tạo mẫu kênh**: đọc phụ đề các video đã tick qua `POST /api/social/youtube/transcripts` (đã có,
   lưu bảng `video_transcripts`).
2. Nút ✦ **Mẫu kênh**: 1 câu hỏi gồm số liệu từng video (tiêu đề, view, × kênh, độ dài, ngày đăng) +
   phụ đề cắt gọn của mỗi video (đầu–giữa–cuối, cùng cách `transcriptSample`).
3. Dưới mỗi video đã tick: nút ✦ **Mẫu cốt truyện**: 1 câu hỏi với phụ đề dài hơn của riêng video đó,
   kèm mẫu kênh đã lưu (nếu có) để các mẫu cùng giọng.
4. Cả 2 loại đi đúng luồng ✦ hiện có: câu hỏi sang khung Hỏi AI → bản nháp về đúng khối → anh bấm **Dùng** (lưu), **Bỏ** hoặc **Hỏi lại**.
5. Nút **Copy Markdown** cho từng mẫu và **Copy cả bộ** (mẫu kênh + mọi mẫu video đã lưu).

### Mẫu kênh có gì

- Thể loại
- Người xem: tuổi, quan tâm gì
- Giọng kể: ngôi kể, nhịp, mức hài / nghiêm
- Kiểu story lặp lại giữa các video
- Công thức tiêu đề
- Công thức 30 giây đầu
- Độ dài hay dùng
- Điều kênh không bao giờ làm

### Mẫu cốt truyện 1 video có gì

- 1 câu premise
- Hook 30 giây đầu, trích lời thật trong phụ đề
- Các hồi theo mốc thời gian. Mỗi hồi: chuyện gì xảy ra, người xem cảm thấy gì, cú twist (nếu có)
- Kết + lời kêu gọi
- 2 hướng làm:
    - **Y chang**: giữ khung, đổi nhân vật / sự kiện
    - **Hao hao**: cùng cảm xúc, đề tài khác

### Luật cho câu hỏi AI

- Chỉ dựa trên phụ đề thật. Không chắc thì ghi "không có trong phụ đề".
- Viết bằng ngôn ngữ giao diện app. Câu trích từ phụ đề giữ nguyên tiếng gốc.
- Không viết kịch bản đầy đủ, chỉ viết mẫu.

### Lưu ở đâu

Dùng lại `magic-notes` (bảng ghi chú ✦ đang có), không thêm bảng:

- Thêm 2 việc vào `MAGIC_TASKS`: `channel-template`, `story-template`.
- `isMagicScope` nhận thêm `ytchannel:<channel ID>` và `ytvideo:<video ID>`.
- Mở lại kênh → đọc ghi chú đã lưu, mẫu vẫn còn.

## Code dự kiến

- `web/src/collectors/youtube-channel.ts`: `channelFull(id, gl)` + đọc tiêu đề theo ngôn ngữ nước, ghép theo id.
- `web/src/lib/story-template.ts` (mới): chọn sẵn video đã chứng minh, câu hỏi mẫu kênh, câu hỏi mẫu cốt truyện, ghép Markdown copy cả bộ.
- `web/src/lib/ai/magic-notes.ts`: 2 task + 2 kiểu scope mới.
- `web/src/client/YoutubeChannel.tsx`: ô tick trong bảng Từng video, khối Làm theo kênh, nút ✦ dưới từng video.
- Test: `web/tests/story-template.test.ts` (chọn sẵn, câu hỏi có đủ mục + số thật, Markdown), thêm ca ghép tiêu đề vào test collector kênh,
  ca scope / task mới vào test magic-notes.

## Giới hạn

- Video không có phụ đề (kể cả tự động) thì không làm được mẫu.
- Phụ đề tự động có thể sai chữ, nhất là tên riêng. Mẫu trích lời thật nên giữ cả lỗi đó.
- Mẫu kênh dựa trên tối đa 10 video đã tick, không phải cả kênh.
- Mục 18 đang sửa cùng file `youtube-channel.ts` / `YoutubeChannel.tsx` (chưa commit). Code mục 19 làm sau khi mục 18 commit.

## Không làm (anh chốt 2026-11-15)

- Không viết kịch bản đầy đủ, không sửa / cải tiến mẫu tự động. Dừng ở mẫu.
- Không gộp 6 mẫu vào 1 câu hỏi to: mỗi mẫu 1 lần hỏi để đủ sâu.
