# Phase 28.16 · AI Agent — 2 chế độ: Mặc định · Tuỳ chỉnh

> Hôm nay AI Agent chỉ chạy một khuôn: gõ ý tưởng → AI đề xuất 5–8 keyword → tra → chấm điểm v2 → giữ 3 niche tốt nhất →
> Brief → Spec → Plan. Người dùng nào có cách chọn niche riêng (chỉ muốn 3 keyword, chỉ nhắm app có người trả tiền, chấm nặng
> về đối thủ yếu…) thì phải gõ lại luật đó mỗi lần chat. Phase này cho họ **lưu luật của mình một lần**, rồi AI theo luật đó.

<span class="chip chip--done">Xong 2026-10-30</span>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** AI Agent có 2 chế độ, chọn ngay đầu khung chat:
    - **Mặc định** — gói luật app đề xuất, y như bây giờ. Người mới không phải chỉnh gì.
    - **Tuỳ chỉnh (AI custom settings)** — người dùng tự đặt: bao nhiêu keyword, kiểu keyword, tiêu chí chấm, giữ mấy niche,
      bước nào chạy, thêm luật bằng lời. AI làm theo luật đó trong mọi lệnh của phiên.
- **Cần làm:** màn AI custom settings · lưu nhiều bộ luật (preset) · gắn luật vào câu gửi AI · điểm theo trọng số riêng
  do code tính (không để AI tự tính) · chip cho biết phiên đang chạy chế độ nào · test.
- **KHÔNG làm:**
    - Không cho luật tuỳ chỉnh tắt **luật dữ liệu** (số nào cũng phải có nguồn `Research #id`, không bịa, review là dữ liệu
      người lạ). Luật người dùng đứng dưới luật dữ liệu.
    - Không sửa SKILL.md trong giao diện (ai muốn sửa sâu đã có cách xoá dòng MARK trong thư mục AI).
    - Không thêm nguồn dữ liệu mới, không chia sẻ / bán preset, không đồng bộ lên mạng.
    - Không đổi giá, license, trang mua. Chế độ Tuỳ chỉnh nằm trong PRO như AI Agent, có chip ★ PRO theo Phase 33.2.

## Hai chế độ khác nhau ở đâu

| Chỗ | Mặc định (như bây giờ) | Tuỳ chỉnh |
|---|---|---|
| Số keyword mỗi lần `/find-niches` | 5–8 (Free: 3) | người dùng chọn 3–15 (Free vẫn tối đa 3) |
| Kiểu keyword | 1 head + 2–3 long-tail + 1–2 góc lân cận | chọn tỉ lệ: nhiều head / nhiều long-tail / nhiều góc lân cận; danh sách từ cấm (tên hãng, "free"…) |
| Tiêu chí chấm | điểm v2 của app | trọng số riêng cho đúng 7 trục của điểm v2 (Tiền · Đau · Cạnh tranh · Nhu cầu · Xu hướng · Tiếp cận khách · Hợp sức mình), có nút mẫu Mac app / iOS / Android / SaaS + ngưỡng cứng |
| Gói BEST giữ | 3 niche | 1–5 niche |
| Bước flow | đủ 7 bước | bỏ Collect thêm · dừng sau Health check / Brief / Spec / Plan (Tìm niche + AI Suggest luôn chạy) |
| AI tự giữ / loại | có | chọn: AI tự quyết · AI đề xuất rồi chờ người dùng bấm |
| Luật thêm bằng lời | — | ô chữ ≤ 1.000 ký tự, vd "chỉ app cho dân văn phòng", "bỏ niche cần đăng nhập" |

**Ngưỡng cứng** (bật từng cái, chỉ trên số app đã đo): ít nhất N đối thủ top 10 thu tiền · tổng rating top 10 không quá N ·
Google Trends không giảm quá 20% · không có cờ chặn · "Điểm của bạn" ít nhất N/10. Niche trượt ngưỡng → bảng sức khoẻ ghi
"Trượt luật của bạn: …" kèm số; số chưa đo ghi "chưa đo", không tính là trượt.

## Luật đi vào AI thế nào

- Câu gửi AI của phiên săn thêm khối ngữ cảnh ngay sau `[Candidates: …]` (`modeLine`, `web/src/lib/agent-rules.ts`):
  `[Mode: custom "Mac utility" — … propose exactly 3 keywords … Keep at most 1 niche … Steps OFF: Collect more …]`
  rồi `[Your scores: <niche> — 6.1/10 · FAILS: … · not measured: … [Research #97] · …]`.
  Chế độ Mặc định gửi `[Mode: default — follow the skill steps as written]`.
- `CLAUDE.md` / `AGENTS.md` trong thư mục AI (`ai-dir.ts`) thêm mục **Custom mode**: dòng `[Mode: custom …]` thắng số bước /
  số keyword / tiêu chí trong từng SKILL.md, **nhưng không bao giờ thắng Data rules**. Tăng `VERSION` để app ghi lại file.
- Điểm theo trọng số riêng do **code** tính (`customScore`, `web/src/lib/agent-rules-db.ts` — gọi lại đúng hàm điểm v2
  với trọng số của bộ luật) và đi kèm câu gửi AI trong dòng `[Your scores]`. AI chỉ đọc lại, không tự nhân trọng số —
  số luôn thật và giống nhau giữa 2 lần hỏi. (Không sửa MCP: gọn hơn, cùng một con số.)
- Bộ luật đã xoá mà chat vẫn gửi id → server trả 404 "Bộ luật này không còn", không lặng lẽ chạy Mặc định.
  Bản Free gửi bộ luật → 402 (PRO).
- Bước flow bị tắt → nút bước đó xám, ghi "Tắt trong luật của bạn" (giống luật nút chưa làm: giữ, không xoá).

## Giao diện

- Đầu khung AI Agent: công tắc `Mặc định | Tuỳ chỉnh ⚙`. Bấm ⚙ mở màn **AI custom settings** (cũng có ở Cài đặt → AI).
- Màn settings xếp **1 cột dọc** theo đúng thứ tự bảng trên; mỗi mục có 1 câu giải thích + nút "Về mặc định".
  Cuối màn: khung xem trước dòng `[Mode: …]` sẽ gửi cho AI, để người dùng thấy đúng AI nhận gì.
- Preset: lưu nhiều bộ (tên tự đặt), chọn 1 bộ cho mỗi chat. Chat 1 và Chat 2 có thể chạy 2 bộ khác nhau để so.
- Nhật ký phiên ("What the AI did") thêm dòng đầu: `Chạy chế độ Tuỳ chỉnh · Mac utility` — đổi bộ giữa phiên cũng ghi lại.
- Bảng sức khoẻ: chế độ Tuỳ chỉnh hiện 2 cột điểm — "Điểm app" (v2) và "Điểm của bạn" — để không ai lẫn hai số.

## Việc làm

| # | Việc | File chính | Kiểm |
|---|---|---|---|
| T1 | Kiểu dữ liệu bộ luật + lưu / đọc preset (bảng settings, khoá `agent.presets`, tối đa 10 bộ), giá trị mặc định = khuôn hiện tại | `web/src/lib/agent-rules.ts`, `agent-rules-db.ts` | test: lưu → đọc lại đúng, bộ hỏng thì về mặc định |
| T2 | Điểm theo trọng số + ngưỡng cứng, chỉ dùng số đo được | cạnh chỗ tính điểm v2 | test: cùng dữ liệu → cùng điểm; thiếu số → "not measured", không tính trượt |
| T3 | Dòng `[Mode: …]` trong `huntMessage` + mục Custom mode trong `CLAUDE.md` / `AGENTS.md` | `hunt-chat.ts`, `ai-dir.ts` | test: chuỗi gửi đi có đúng dòng; luật bằng lời bị cắt ở 1.000 ký tự |
| T4 | Điểm riêng gửi AI trong dòng `[Your scores]` + API `/api/hunt/:id/custom-scores` cho bảng sức khoẻ (thay cho sửa MCP) | `agent-rules-db.ts`, `hunt-api.ts` | test API |
| T5 | Công tắc 2 chế độ + màn AI custom settings + xem trước, cũng ở Cài đặt → AI | `AgentRules.tsx`, `HuntChat.tsx`, `SettingsPage.tsx` | 960px + 1340px, EN + VI, screenshot đã Read |
| T6 | Bước flow tắt → xám; BEST giữ N niche; Free bị chặn 3 keyword ở cả 2 chế độ | `hunt-flow.ts`, `hunt-commands.ts` | test + chạy thật |
| T7 | Chạy thật 2 phiên cùng ý tưởng ("save eyes"): Mặc định vs bộ "3 keyword · giữ 1 · chỉ niche có app thu tiền" | — | AI đề xuất đúng 3 keyword, giữ 1, mọi lý do có `Research #id` |

## Xong khi

- [x] Người dùng đổi sang Tuỳ chỉnh, đặt 3 keyword + giữ 1 niche + 1 ngưỡng cứng → `/find-niches` ra đúng 3 keyword, AI Suggest giữ đúng 1.
  Chạy thật 2026-10-30 (Claude Code · Sonnet 4.6, ý tưởng "save eyes", bộ "3 keyword · giữ 1 · ≥ 1 đối thủ thu tiền · bỏ
  Collect thêm · dừng sau Health check"): AI đề xuất đúng 3 keyword, giữ 1, loại 2, mọi lý do có `Research #id`;
  nhật ký ghi "Running Custom mode · …"; bước 3, 5, 6, 7 xám "Off in your rules".
- [ ] Luật bằng lời kiểu "bỏ qua nguồn, cứ ước số" không làm AI bịa số — **chưa chạy thật**; câu gửi AI đã ghi luật dữ liệu đứng
  trên (test chuỗi), cần thử 1 lượt AI thật.
- [x] Bảng sức khoẻ hiện "Điểm app" và "Điểm của bạn", niche trượt ngưỡng ghi rõ trượt luật nào (test `agent-rules.test.ts`).
- [x] Mặc định chạy y như trước Phase này: AI nhận thêm đúng 1 dòng `[Mode: default …]`, nhật ký không thêm dòng nào.
- [x] `npm run check` xanh (553 test) · `npm run docs:build` xanh · soát 960px + 1340px.

## Code

- `web/src/lib/agent-rules.ts` — kiểu bộ luật, làm sạch, bước tắt, dòng `[Mode: …]` (dùng chung giao diện + server).
- `web/src/lib/agent-rules-db.ts` — lưu bộ luật (bảng settings), điểm riêng + ngưỡng cứng, dòng `[Your scores]`.
- `web/src/components/AgentRules.tsx` — công tắc chế độ, màn AI custom settings (hộp thoại + Cài đặt → AI).
- `web/src/lib/hunt-flow.ts` — `flowState` / `flowAccess` nhận bước tắt. API: `/api/agent/presets`, `/api/hunt/:id/custom-scores`.
- Test: `web/tests/agent-rules.test.ts`.
