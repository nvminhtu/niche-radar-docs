# Phase 28.15 · Hỏi AI / AI Agent — mỗi lượt tốn bao nhiêu token

> Người dùng muốn minh bạch khi dùng AI Agent: hỏi một câu thì tốn bao nhiêu token, chiếm bao nhiêu % sức chứa của AI.
> Trước đây khung chỉ hiện "6s · 1 data reads" (lượt xong) hoặc "Stopped" (lượt dừng) — không có số nào.

<span class="chip chip--done">Xong 2026-10-29</span>

!!! note "Sửa 2026-10-30"
    Bỏ giá `~$…` khỏi dòng từng lượt và dòng tổng phiên trong khung chat — người dùng gói Pro/Max không bị trừ tiền nên số $
    gây hiểu lầm. Giá ước tính vẫn còn ở sổ dùng AI (Cài đặt → AI).

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** mỗi câu trả lời trong Hỏi AI và AI Agent có một dòng token; cuối khung có tổng của cả phiên chat.
  Chỉ số thật đọc từ Claude Code / Codex — không đo được thì ghi `chưa đo`.
- **Cần làm:**
    - Dòng của từng lượt: `19.7k tokens (in 4 · cache 19.6k · out 62) · 10% of context · ~$0.03`.
    - Dòng phiên (ngay trên ô gõ): `This session: 76.8k tokens · 2 turns · ▬ 18% of context (200.0k) · ~$0.03`,
      thanh màu xanh / vàng từ 50% / đỏ từ 80%. Rê chuột vào ⓘ: giải thích token, cache, khung nhớ, giá.
    - Lượt bị Dừng / lỗi vẫn hiện phần đã tốn: `spent so far 57.2k tokens … 18% of context`.
    - Tổng phiên lưu theo id phiên chat → mở lại AI Agent (nối tiếp phiên cũ) vẫn thấy tổng các lượt trước.
- **KHÔNG làm:** không đo hạn mức 5 giờ / tuần của gói Claude Pro/Max (Anthropic không công bố số token → `chưa đo`);
  không đổi giá, license, trang mua; không lưu câu hỏi / câu trả lời.

## Số lấy từ đâu

| Số | Claude Code | Codex |
|---|---|---|
| Token vào / cache / ra | sự kiện `result` → `usage` (cộng mọi lần gọi API của lượt) | `turn.completed` → `usage` (cached tách khỏi input) |
| Khung nhớ đang dùng | lần gọi API cuối của lượt (`usage.iterations`) | chưa đo (Codex chỉ báo tổng lượt) |
| Cỡ khung nhớ | `modelUsage.<model>.contextWindow`; thiếu thì giả định Claude 4.x = 200k, bản `[1m]` = 1M | chưa đo |
| Giá | `total_cost_usd` — giá API niêm yết Claude Code tự tính | chưa đo |
| Lượt bị Dừng | cộng `message.usage` của từng câu trả lời đã nhận; không có giá | — |

Giá chỉ để biết cỡ: dùng gói Claude Pro/Max thì không bị trừ tiền, mà trừ vào hạn mức của gói.

Nút Dừng giờ gọi `POST /api/ai/chat/stop {runId}` (mỗi lượt có runId riêng) thay vì cắt kết nối — luồng vẫn mở nên
server gửi được phần token đã tốn. Lượt dừng / lỗi có token cũng được ghi vào sổ dùng AI (Cài đặt → AI).

## Code

- `web/src/lib/ai/chat-usage.ts` — đọc token, % khung nhớ, cộng dồn phiên (dùng chung server + trình duyệt).
- `web/src/lib/ai/chat.ts` — `done` / `error` kèm `usage`.
- `web/src/components/ChatUsage.tsx` — dòng phiên, chữ của từng lượt, lưu tổng theo phiên, nút Dừng.
- Test: `web/tests/chat-usage.test.ts`.

## Xong khi

- [x] Hỏi AI thật (Claude Code · Sonnet 4.6): câu trả lời có dòng token + % khung nhớ + giá; dòng phiên cộng đúng.
- [x] Bấm Dừng giữa lượt: lượt đó hiện "spent so far …", tổng phiên cộng thêm.
- [x] `npm run check` xanh.
