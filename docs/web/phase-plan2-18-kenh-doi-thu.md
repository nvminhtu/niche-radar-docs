# 18 · Soi kênh: kênh đối thủ liên quan

> Plan 2 · mục 18. Trang **Soi 1 kênh** (mục 7) thêm khối **Kênh đối thủ**: tệp kênh mà chính YouTube xếp cạnh kênh đang soi,
> kèm số sub, số video, năm lập kênh, view giữa, × sub và nút soi tiếp. Đầu trang có thêm 3 chip sub · số video · năm lập kênh.
> Không cần key, không AI.

<span class="chip chip--done">Code 2026-11-15 · chưa commit</span>

## Vì sao làm

Anh hỏi 2 câu (2026-11-15):

1. Soi 1 kênh phải thấy ngay **số liệu cơ bản**: đã đăng bao nhiêu video, kênh có từ năm nào, bao nhiêu sub.
   Trước đây số này chỉ nằm ở hàng ô số bên dưới.
2. Muốn có **tệp kênh đối thủ liên quan** tới kênh đang soi, chứ không chỉ tìm theo top keyword.

Tìm theo keyword chỉ ra kênh dùng chung chữ trong tiêu đề. Cùng khán giả nhưng đặt tên khác (vd. kênh nhạc vẽ tay, kênh "café jazz")
thì tìm theo keyword bỏ sót.

## Cách làm

**Nguồn = cột "Video đề xuất" (watch next) bên phải video trên YouTube.** Đây là danh sách YouTube tự chọn cho cùng người xem.

1. Lấy **5 video nhiều view nhất** trong 30 video gần nhất của kênh, coi là video đại diện cho ngách.
2. Đọc cột đề xuất của từng video, khoảng 20 ô mỗi video. Bỏ mix / playlist vì không có kênh.
3. Đếm mỗi kênh hiện cạnh **bao nhiêu video gốc** (chấm cam x/5), rồi xếp kênh hiện nhiều nhất lên đầu.
   Bỏ chính kênh đang soi. Kênh chỉ hiện đúng 1 ô ở 1 video thì bỏ, coi là nhiễu.
4. Cộng thêm kênh đang **đứng #1 ở keyword** của kênh (số này đã có sẵn từ bảng Keyword và thứ hạng).
5. Lấy 8 kênh đầu. Mỗi kênh đọc trang kênh + About + 1 trang video để có sub, số video, năm lập kênh, view giữa và ngày đăng gần nhất.

Cột **× sub** = view giữa ÷ sub. Kênh nhỏ mà số này cao (≥ 3×, tô xanh) là kênh nhỏ đang thắng ngách, nên soi kỹ trước.

## Đã đo (2026-11-15)

- **Đọc thử trên Happiko (@happikochannel, 33,6K sub, US):** 6 video gốc, mỗi video có 20–21 ô đề xuất.
  Kênh hiện nhiều nhất: Doodle Jazz Band 7 lần, Music Drawing 7, seijuslog 6, heyhearhear 5, Morning On The Music 5.
  Tất cả đều cùng ngách playlist jazz / vẽ tay. Tìm theo keyword "jazz playlist" không ra phần lớn các kênh này.
- **Lượt Soi 1 kênh có thêm bước đối thủ chạy hết 17,5 giây**: 5 video gốc + 8 kênh, trong app chạy trên máy.
  Ra 8 kênh, có 1 kênh nhỏ đang thắng ngách là heyhearhear: 295 sub, view giữa 1,6K, 5,4× sub.
- `getChannels()` (tab Kênh nổi bật của chủ kênh) không có trong bản youtubei.js đang dùng. Tab này cũng do chủ kênh tự chọn,
  không phản ánh khán giả → không dùng.

## Đã code

- **Đầu trang Soi 1 kênh:** 3 chip sub · số video · năm lập kênh ("since 2014"), rê chuột thấy tuổi kênh.
- **Khối Kênh đối thủ** ngay dưới hàng ô số. Bảng có ảnh + tên kênh, nhãn "#1 ở keyword" nếu có, chấm đề xuất x/5, sub, số video,
  năm lập kênh, view giữa (có thanh), × sub, nút **Soi** để soi tiếp kênh đó.
- **Lượt soi cũ** (lưu trước khi có khối này) hiện nút **Soi lại để tìm đối thủ**. Nút này soi mới, bỏ bản lưu, giữ đúng nước của lượt cũ.
- **✦ AI phân tích kênh** nhận thêm danh sách đối thủ kèm số.
- **Agent (MCP `youtube_channel` / `get_youtube`)** nhận thêm mục `competitors`, có link để gọi `youtube_channel` soi tiếp.
- Code: `web/src/collectors/youtube-channel.ts` (`readWatchNext`, `relatedSeeds`, `pickRelated`, `briefOf`),
  `web/src/lib/channel-audit.ts`, `web/src/client/YoutubeChannel.tsx`. Test: `web/tests/channel-related.test.ts`.

## Giới hạn

- Đề xuất đo lúc soi, không đăng nhập, nước theo lượt soi. Người xem thật thấy đề xuất khác nhau. Chỉ dùng để tìm tệp, không coi là xếp hạng.
- Chỉ đọc 5 video gốc: kênh hiện cạnh 5/5 video là tín hiệu mạnh, còn 2/5 thì chỉ nên xem thêm.
- YouTube đổi cấu trúc trang (LockupView) là bước này gãy. Khi đó lượt soi vẫn chạy, chỉ ghi lỗi vào errors và khối đối thủ trống.

## Làm sau (chưa xếp lịch)

- So kênh đang soi với 2–3 kênh đối thủ cạnh nhau (trùng ý "so 3 kênh" ở [mục 17](phase-plan2-17-trend-keyword-so-kenh.md)).
- Đi tiếp 1 tầng: lấy đề xuất của video từ chính các kênh đối thủ để mở rộng tệp.
