# Phase 33.2 · Chip PRO — bấm vào là ra bản PRO

> Bản Free chỉ có 2 lối tới màn mua: thanh "12/15 free searches left · Get PRO" dưới menu và nút Get PRO ở bước khoá của
> AI Agent. Người dùng đang đứng cạnh một tính năng PRO (nút AI, khung Hỏi AI, MCP…) không thấy ngay "cái này PRO mở được".

<span class="chip chip--done">Xong 2026-10-29</span>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** mọi tính năng PRO mới có đủ (bảng Free / PRO của [Phase 33.1](phase-33-1-go-live-review.md#bang-free-pro-anh-chot-2026-10-29))
  có một chip **★ PRO** ngay tại chỗ; bấm chip mở `/license?from=<chỗ>`, đầu màn mua nói đúng tính năng vừa bấm.
- **Cần làm:** 1 component chung `ProChip`, chỉ hiện ở bản Free (đã PRO và bản Web không thấy), gắn vào 7 chỗ dưới đây.
- **KHÔNG làm:** không đổi giá, số lượt Free, luật khoá, nút mua, link checkout / danh sách chờ; không thêm chặn mới
  (server vẫn chặn bằng 402 như Phase 33.1). Không gắn chip vào từng hàng bảng (thử nút "Explore từ đây" ở mỗi hàng: rối → bỏ).

## Chỗ có chip

| Chỗ | Chip | Màn mua ghi "PRO mở:" |
|---|---|---|
| Menu trên cùng, cạnh "New niche search" | ★ PRO | Tra niche không giới hạn + toàn bộ AI |
| Dưới ô tra niche (Research / Explore) | "Free: 12/15 searches left" + ★ PRO · unlimited | Tra / Explore không giới hạn |
| Cạnh mọi nút ✦ ở tiêu đề khối (Sức khoẻ niche, Explore, Bàn quyết định, Find Gaps, Project) | ★ PRO | AI không giới hạn (Free: 3 lần thử) |
| Cạnh nút "Chạy bằng AI" / "Điền bằng AI" | ★ PRO · 2/3 tries left | như trên |
| Đầu khung Hỏi AI | ★ PRO · 2/3 tries left (bấm thì đóng khung) | Khung Hỏi AI không giới hạn |
| AI Agent: tiêu đề khung chat + bước 3–7 | ★ PRO · all 7 steps · nhãn ★ PRO trên bước khoá | AI Agent đủ 7 bước + bộ .md |
| Cài đặt → MCP | ★ PRO · needs PRO | Nối MCP cho Claude / Codex |

Thêm: hết 3 lần thử AI thì nút ✦ dẫn thẳng sang màn PRO thay vì gửi câu hỏi rồi bị chặn.

**Hết lượt AI (2026-10-30, Tu):** bản Free dùng hết 3 lần thử thì phần AI **mờ đi** và nút mua **to, dễ bấm**
(`ProUpsell` trong `ProChip.tsx`):

- Khung Hỏi AI: câu hỏi mẫu + ô nhập mờ, không gõ được; trên ô nhập là thẻ "You have used all 3 free AI tries" + nút
  **★ Unlock PRO $39.99 · one-time** rộng hết khung. Server trả 402 giữa chừng → thay dòng lỗi đỏ bằng đúng thẻ đó (cả AI Agent).
- Nút ✦ ở tiêu đề khối: mờ xám, chip PRO nhỏ đổi thành nút Unlock PRO.
- Nút "Run with AI" / "Điền bằng AI": mờ xám (bấm sang màn PRO) + nút Unlock PRO cạnh bên.
- Chạy AI xong đọc lại license ngay → lần thử cuối vừa dùng là khung mờ luôn, không đợi đổi trang.

## Code

- `web/src/lib/pro-spots.ts` — danh sách chỗ + câu "PRO mở được gì", `proHref`, `isFree`.
- `web/src/components/ProChip.tsx` — chip + số lần thử AI còn lại.
- `web/src/client/LicensePage.tsx` — đọc `?from=` hiện dòng "★ PRO mở: …".
- Test: `web/tests/pro-spots.test.ts`.

## Xong khi

- [x] Bản Free (`NR_EDITION=research`, 3/15 lượt tra + 1/3 lần thử AI đã dùng): thấy chip ở cả 7 chỗ, bấm chip Hỏi AI ra
  `/license?from=ask` có dòng "★ PRO unlocks: Unlimited Ask AI chat".
- [x] 960px: cả trang không cuộn ngang.
- [x] `npm run check` xanh.
