# 23 · Trang YouTube: gom 3 nhóm + chạy nhiều lượt cùng lúc

> Plan 2 · mục 23. Trang YouTube có 5 thẻ và sắp có thêm 2 việc (mục 15, mục 21). Mục này gom 5 thẻ thành **3 nhóm theo việc**,
> cho **gõ nhiều keyword / link một lần**, và chuyển các lượt sang **hàng chờ ở máy chủ** chạy được nhiều luồng cùng lúc.
> Không đổi nội dung bên trong từng kết quả.

<span class="chip chip--todo">Viết 2026-11-15 · anh đã duyệt · plan code: docs/superpowers/plans/2026-11-15-plan2-23-youtube-gom-nhom-chay-nhieu.md</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục này ghi lại yêu cầu anh đưa ra ngày 2026-11-15. Chỉ code khi anh chốt.
</div>

## Vì sao làm

Anh nói (2026-11-15): tool YouTube giờ phình to rồi, cần gom nhóm cho UI thuận tiện, và cần chạy được nhiều lượt tìm,
nhiều luồng cùng lúc.

## Trang đang có gì (đọc code 2026-11-15)

- **5 thẻ ngang hàng** (`web/src/client/YoutubeEntry.tsx`): Tìm ý tưởng · Săn kênh nhỏ view nổ · Xem đang trend gì · Soi 1 kênh · So kênh.
  Màn rộng thì 5 thẻ nằm 1 hàng, màn hẹp thì xuống 2–3 hàng. Thêm mục 15 (Theo dõi ngách) và mục 21 (Keyword đang tìm) sẽ lên 7 thẻ.
- **Mỗi thẻ 1 lượt một lúc**: `web/src/server/social-api.ts` trả lỗi 409 "Tab này đang chạy — đợi lượt trước xong" khi thẻ đó đang có lượt chạy.
  Các thẻ khác nhau thì đã chạy song song được (`socialAreaBusy(area, mode)` trong `web/src/lib/social-jobs.ts`).
- **Mỗi lượt chạy trọn trong 1 request** (khoảng 30–110 giây). Nếu đóng tab giữa chừng thì trình duyệt không nhận được kết quả, nhưng máy chủ vẫn chạy và lưu vào SQLite.
- **Đã chạy nhiều phần ở 2 chỗ, nhưng do trình duyệt điều khiển và chạy lần lượt**: Đang trend nhiều nước (`runMulti`) và So kênh (`runCompare`), cùng trong `web/src/client/SocialPage.tsx`.
  Mỗi lần gọi 1 request rồi đợi xong mới gọi request tiếp.
- **AI qua MCP đã chạy nền** (mục 15.7): `/api/mcp/youtube/*` dùng chung sổ việc `social-jobs`, chờ 20 giây rồi trả mã việc để hỏi lại.

## 23.1 · Gom 3 nhóm + chip chế độ

Hàng thẻ to chỉ còn 3 thẻ, chọn theo việc anh muốn làm:

| Nhóm | Chip chế độ bên trong | Ghi chú |
|---|---|---|
| 🔍 **Tìm ngách** | `Tìm ý tưởng` · `Đang trend` | Mục 21 thêm chip `Keyword đang tìm` (nếu tách riêng) |
| 🎯 **Săn kênh** | `Săn kênh nhỏ` | Mục 15 thêm chip `Theo dõi ngách` |
| 📺 **Soi kênh** | `Soi từng kênh` · `So kênh` | Soi 1 kênh đổi tên thành Soi từng kênh vì nay soi được nhiều kênh một lần |

- Thẻ nhóm: icon to + tên. Nhóm nào đang có lượt chạy thì thẻ có vạch chạy ở đáy và chữ "{n} đang chạy".
- Dưới thẻ là **hàng chip chế độ** của nhóm đang chọn, kèm 1 dòng mô tả chế độ đang chọn (như dòng mô tả hiện tại).
  Nhóm chỉ có 1 chế độ thì vẫn hiện chip, để sau này thêm chế độ không phải đổi bố cục.
- **Thanh dính** khi cuộn: `YouTube / Soi kênh / Soi từng kênh / <tên kênh>` (thêm 1 nấc nhóm vào thanh đang có).
- **Không đổi khoá chế độ** (`niche` · `hunt` · `trend` · `channel` · `compare`). Link cũ, lịch sử, `localStorage` (`niche-radar.youtubeMode`)
  và MCP vẫn chạy như cũ, nhóm được suy ra từ chế độ.
- Mỗi chế độ vẫn là một khung giữ nguyên trạng thái (như 2026-11-15): chuyển nhóm hay chuyển chip thì lượt đang chạy vẫn chạy tiếp.
- Trang KDP dùng chung `EntryCards`: thêm tuỳ chọn `groups`, KDP không truyền thì giữ nguyên 3 thẻ như cũ.

## 23.2 · Gõ nhiều một lần

Ô nhập của các chế độ dưới đây đổi thành ô nhiều dòng, **mỗi dòng 1 mục** (dán danh sách cách nhau bằng dấu phẩy thì cũng tách ra):

| Chế độ | Mỗi dòng là | Tối đa / lần | Kết quả |
|---|---|---|---|
| Tìm ý tưởng | 1 keyword | 10 | 1 kết quả / keyword |
| Săn kênh nhỏ | 1 chủ đề | 5 | 1 lượt săn / chủ đề, mỗi lượt tự chạy hết 3 bước |
| Soi từng kênh | 1 link / @handle kênh | 10 | 1 kết quả / kênh |
| So kênh | 1 link kênh | 3 (giữ như cũ) | 1 bảng so chung |
| Đang trend | (chọn nước, đã chọn nhiều nước được) | giữ như cũ | gộp như cũ |

- Chỉ nhập 1 dòng thì vẫn chạy và mở kết quả như bây giờ.
- Dòng trùng thì bỏ. Dòng sai (link không phải kênh) thì báo đỏ ngay dòng đó, các dòng khác vẫn chạy.
- Nút chạy ghi rõ số lượt: "Tra 4 keyword", "Soi 3 kênh".

## 23.3 · Hàng chờ ở máy chủ, nhiều luồng

**Máy chủ:**

- API mới `POST /api/social/youtube/batch` nhận `{ mode, items[], country, force }`. Mỗi mục được ghi vào sổ `social-jobs`
  với trạng thái `queued`, rồi API trả ngay danh sách mã việc, không đợi chạy xong.
- **1 hàng chờ chung cho YouTube**, chạy tối đa **3 việc cùng lúc** (`YT_CONCURRENCY`, mặc định 3).
  Hàng chờ dùng chung cho cả trang web và AI qua MCP. Việc dư thì chờ theo thứ tự bấm.
- Chạy song song cả trong một chế độ. **Bỏ lỗi 409** "Tab này đang chạy" ở các chế độ YouTube, thay bằng xếp hàng.
  Hai lượt giống hệt nhau (cùng chế độ + mục + nước) mà lượt trước chưa xong thì không chạy lại, chỉ trả mã việc đang có.
- Lượt săn kênh nhỏ chiếm 1 luồng cho cả 3 bước.
- Đang trend nhiều nước và So kênh chuyển sang hàng chờ của máy chủ: mỗi nước / mỗi kênh là 1 việc, máy chủ tự gộp khi xong hết.
  Như vậy rời trang hay đóng tab thì vẫn gộp được.
- Sổ việc thêm trạng thái `queued` và `cancelled`. Việc còn `queued` thì huỷ được (`POST /api/social/jobs/:key/cancel`).
  Việc đang chạy thì để chạy hết, không huỷ giữa chừng.
- Tắt máy chủ thì mất hàng chờ, giống sổ việc bây giờ. Lượt đã xong vẫn còn trong SQLite.

**Trang web: dải Hàng chờ**

- Nằm dưới hàng chip chế độ, chỉ hiện khi có việc. Hiện việc của **chế độ đang xem** trước, các chế độ khác gom thành 1 chip "+{n} ở chế độ khác".
- Mỗi việc là 1 chip nhỏ: ⏳ chờ (thứ tự trong hàng) · vòng quay + đồng hồ khi đang chạy · ✓ xong · ⚠ lỗi (rê chuột xem lý do) · nút × để bỏ chip.
- **Chip như tab con:** bấm chip đã xong thì mở kết quả ngay bên dưới, chip đang mở được tô đậm. Việc xong đầu tiên của lượt bấm tự mở.
  Các việc xong sau không tự nhảy sang, để khỏi giật trang lúc anh đang đọc.
- Giữ tối đa **8 chip đã xong / chế độ**, việc chưa xong luôn hiện (1 lần bấm có thể ra 10 việc). Chip đã xong mà cũ nhất thì rời dải, vẫn mở lại được ở Lịch sử.
- Trang đọc trạng thái bằng `/api/activity` đang có (đã hỏi định kỳ cho Buồng lái), không cần kênh realtime mới.
- Buồng lái (`ActivityMenu`) hiện được việc `queued`.

## Đã đo / chưa đo

- **Chưa đo:** chạy song song 3 luồng (hoặc 5 luồng) qua `youtubei.js` có bị YouTube chặn hay chậm lại không. Số 3 là mình chọn cho an toàn,
  chưa có số đo. Lúc code sẽ chạy thật 5 keyword với 1 · 3 · 5 luồng, ghi thời gian + số lỗi vào mục này rồi mới chốt mặc định.
- `web/src/collectors/youtube.ts` đã có `createLimiter` (`web/src/lib/rate-limit.ts`). Sẽ đọc xem bộ giới hạn đó là chung cho cả máy chủ
  hay riêng từng lượt, vì 3 luồng chạy cùng lúc phải dùng chung 1 bộ giới hạn.

## Chia việc

1. **23.1** Gom nhóm: `YoutubeEntry.tsx` (nhóm + chip + thanh dính), `SocialPage.tsx` (chọn nhóm từ chế độ). Có test suy nhóm từ chế độ.
2. **23.3 máy chủ:** hàng chờ trong `social-jobs.ts` (`queued`, giới hạn luồng, chặn chạy trùng, huỷ), API `batch` + `cancel`,
   bỏ 409 ở YouTube, MCP dùng chung. Có test: 5 việc với giới hạn 3 thì đúng 3 việc chạy cùng lúc, huỷ việc đang chờ, lượt trùng trả mã việc cũ.
3. **23.2 + dải Hàng chờ:** ô nhiều dòng cho 3 chế độ, dải chip, mở kết quả bằng chip.
4. Chuyển Đang trend nhiều nước + So kênh sang hàng chờ của máy chủ (gộp ở máy chủ).
5. Đo 1 · 3 · 5 luồng, chốt `YT_CONCURRENCY`. Xem tận mắt ở 960px và 1340px, cả sáng lẫn tối, English lẫn tiếng Việt.

## Giới hạn

- Hàng chờ nằm trong bộ nhớ, tắt máy chủ là mất các việc chưa chạy.
- Tối đa / lần (10 · 5 · 10) là số tự đặt để 1 lần bấm không giữ máy quá lâu. Ví dụ 5 lượt săn × khoảng 110 giây, chạy 3 luồng thì mất khoảng 4 phút.
- Chưa tách Free / PRO cho số lượt gõ một lần. Ghi chú cho sau: Free chỉ 1 dòng, PRO mới được nhiều dòng.
