# Nhu cầu thật của người dùng — đọc cái người ta cần, không chỉ cái bảng xếp hạng cho thấy

Bảng xếp hạng nói **app nào đang được cài**. Nó không nói **vì sao**, cũng không nói **người ta sẽ đổi sang
app nào**. Một ý tưởng chỉ đáng làm khi gọi tên được *lúc dùng*, *việc được làm xong*, *chỗ đau* — và chỉ ra
bằng chứng cho từng cái. Pha 3–4 của app-research dùng lăng kính này.

## 1. Bốn câu hỏi (ý tưởng nào cũng phải trả lời đủ)

| Câu hỏi | Trả lời tốt | Trả lời hỏng |
|---|---|---|
| **Lúc nào** mở app? | "mỗi lần gửi video qua Discord bị quá 25 MB" | "khi cần" |
| **Việc gì** được làm xong? | "file nhỏ lại dưới giới hạn, không phải chỉnh gì" | "tiện" |
| **Đau ở đâu** với thứ đang dùng? | "trả $4.99/tháng cho một việc làm 2 lần/tuần" (trích 3 app) | "app dở" |
| **Vì sao đổi** sang mình? | "làm y vậy, offline, mua đứt một lần" | "của mình tốt hơn" |

Ô nào không điền được bằng bằng chứng trong file research → ý tưởng chưa sẵn sàng. Không điền bằng cảm giác.

## 2. Thang bằng chứng — chắc cỡ nào nhu cầu là thật?

Mạnh → yếu. Chỉ gọi là **thật** khi có **2+ bậc khác nhau**:

1. **Câu nói nhu cầu** trong review của app đang xếp hạng, ở **2+ app khác nhau** — "I wish…",
   "would be great if…", "is there an app that…" (`mine` → Need lines).
2. **Từ đi kèm trong autocomplete** — `free`, `offline`, `no subscription`, `simple`, `for mac` (`hints`).
3. **App mới của dev nhỏ đang leo** đúng định vị đó.
4. **Reddit hỏi thẳng** — r/macapps, r/iphone, r/productivity: "is there an app that…" (§5).
5. **Google Trends** — chỉ nói cỡ và mùa, không nói nhu cầu.

## 3. Đau → hứa → chứng minh

Một chỗ đau chỉ thành định vị khi app **làm được** cái hứa:

| Đau (từ review) | Hứa | Chứng minh trong app |
|---|---|---|
| subscription cho một công cụ đơn giản | "mua đứt một lần" | giá một lần (app-money), không cần tài khoản |
| paywall ngay khi mở | "dùng được thật trước khi trả" | bản free làm trọn việc chính, giới hạn số lần/cỡ |
| mất dữ liệu / sync hỏng | "dữ liệu nằm trên máy bạn" | lưu local, xuất file được |
| bỏ rơi, không cập nhật macOS mới | "chạy trên macOS mới nhất" | Swift 6 + SwiftUI, min macOS trong app.json |
| đòi upload file lên cloud | "không file nào rời máy" | xử lý on-device (ImageIO/AVFoundation), không network |
| rối, quá nhiều nút | "một việc, một cú kéo thả" | màn chính một hành động |

## 4. App Mac nhỏ — tín hiệu riêng

App tiện ích Mac nhỏ (menu bar, kéo thả, dọn file, clipboard, cửa sổ…) sống theo luật khác app điện thoại:

| Tín hiệu | Đọc ra |
|---|---|
| `search --mac` ra toàn **iphone-on-mac** ở top | chưa ai làm bản **Mac gốc** tử tế → khoảng trống |
| app Mac gốc đứng đầu nhưng tuổi > 5 năm, review "not updated" | ông lớn đang bỏ rơi → vào được |
| review than **subscription** ở app đầu | cửa cho **mua đứt** |
| đối thủ ngoài store bán mua đứt (trang hãng, Setapp) | người dùng Mac chịu trả tiền cho việc này — ghi giá + nguồn |
| Apple vừa làm sẵn tính năng đó trong macOS | **rủi ro bị "Sherlock"** — ghi rõ, thường là giết ý tưởng |
| review than Electron/nặng/tốn pin | định vị "native, nhẹ" có giá trị |

Giới hạn dữ liệu Mac (đo 2026-09-22): Apple chỉ còn bảng **top free Mac tổng** (`macchart`), không có theo thể
loại, không có paid/grossing. App Mac gốc trả **0 đánh giá** qua API → dùng **nhịp review** của `mine`
(bao nhiêu review, ngày cũ nhất/mới nhất) làm tín hiệu "còn người cài". `hints` là autocomplete của store iPhone —
dùng làm tín hiệu nhu cầu chung, không phải của riêng Mac.

## 5. Reddit (người dùng hỏi thẳng)

Reddit chính thức bị chặn ở máy này; archive arctic-shift chạy qua script của repo Book khi repo đó nằm cạnh:

```bash
R=../../Book-AI-skills/.claude/skills/reddit-scout/scripts/reddit_fetch.py
python3 $R posts --subreddit macapps --title "is there an app" --limit 50
python3 $R posts --subreddit macapps --title "<chủ đề>" --limit 50
```

Tìm bằng `--title` (rẻ); tìm full-text hay timeout. Điểm số trong archive vô nghĩa (luôn ~1) — đọc bài, đừng xếp
hạng theo điểm. Script không có hoặc timeout 2 lần → ghi `Reddit: chưa đo`.

## 6. Bẫy

- **Than quảng cáo / giá có ở mọi app free** — chỉ là vệ sinh, không phải khác biệt, trừ khi autocomplete cũng cho
  thấy người ta gõ `no subscription` / `free`.
- **Lời nói ≠ hành vi.** Người ta xin tính năng sâu nhưng dùng thứ đơn giản. Bảng xếp hạng nói *cái gì*, review nói
  *thiếu gì*.
- **Một hit không phải xu hướng.** 3+ app mới của nhiều dev khác nhau mới là xu hướng còn chỗ.

## 7. Câu hook một dòng

> "Là **<thứ quen thuộc>** nhưng **<một điểm khác>**, dành cho lúc **<khoảnh khắc>**, để **<việc được làm xong>** —
> không **<chỗ đau của app đầu>**."

Phải hai câu mới nói xong → là hai app, hoặc chưa phải app nào.
