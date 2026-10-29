# Phase 28.11 · AI Agent — chọn model, biết AI nào đang chạy, chat gọn

> Khung **AI Agent** (trang Phiên săn `/hunt/:id`) phải cho người dùng: **chọn model** ngay trong ô chat (kiểu menu model
> của Claude), **thấy rõ AI nào đang chạy** (tên hãng tô đậm: **CLAUDE** / **CHATGPT** / **GEMINI**), nội dung chat
> **ít chữ thừa, ít khung**, và **biết AI đang trả lời** (vòng xoay + đồng hồ). Kèm đổi tên menu **Q&A Gap → Find Gaps**.

<span class="chip chip--done">Xong 2026-10-28</span>

<div class="box box--goal" markdown>
**Hiện có — đối chiếu code ngày 2026-10-28 (trước khi sửa).**

- Đầu khung: "Runs on your Claude Code · model unknown · uses your plan" — dài, bị cắt, "model unknown" khi CLI chưa
  trả lời lượt nào. Tên AI không nổi bật.
- Chọn model: `<select>` nhỏ "Claude Code · default" trong `ChatComposer.tsx` — không thấy model nào đang chọn, không mô tả.
- Nội dung: "What the AI did in this session" là hộp nền xám, mỗi dòng 2 dòng chữ có cả `##` Markdown; việc AI làm trong
  câu trả lời đóng khung viền; câu người dùng là hộp xám; link "Show guides again" nằm lẻ dưới ô chat.
- Đang trả lời: chỉ 1 chấm nhấp nháy + "Đang hỏi AI…", khi đã có chữ thì không còn dấu hiệu đang chạy.
</div>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** nhìn khung AI Agent 2 giây biết AI nào, model nào, AI đang làm gì; đổi model ≤ 2 bấm.
- **Cần làm:** A đổi tên Q&A Gap · B tên AI tô đậm theo hãng · C menu chọn model · D chat gọn · E vòng xoay đang trả lời.
- **KHÔNG làm:** đổi AI (Claude ↔ ChatGPT) ngay trong chat — vẫn ở Cài đặt, menu model có lối sang; thêm model mới hay
  đổi bảng `MODELS`; đổi luật danh tính model (Phase 28.7 T1: model chỉ ghi khi CLI xác nhận); đổi tool, prompt, MCP;
  đổi định dạng file `.md` xuất Q&A Gap (tiêu đề `# Q&A Gap — …` giữ nguyên).

## Việc

| | Việc | File | Xong khi |
|---|---|---|---|
| A | Menu **Q&A Gap → Find Gaps** (vi "Tìm gap", es "Buscar brechas"), tiêu đề trang + chữ Cài đặt theo | `locales/en.ts · vi.ts · es.ts`, `RedditGapPage.tsx` | menu More features ghi Find Gaps |
| B | `AiBrand`: chấm màu + tên hãng **in đậm, viết hoa** (Claude cam · ChatGPT xanh lá · Gemini xanh dương) + phần còn lại nhạt ("Code", "Codex") | `components/AiBrand.tsx` | đầu khung ghi "Runs on ● **CLAUDE** Code"; dòng đầu mỗi câu trả lời cũng vậy |
| C | `ModelPicker`: chip "● **CLAUDE** · Opus ⌄" → menu: tên model + 1 câu (Opus giỏi nhất · Sonnet cân bằng · Haiku nhanh), ✓ model đang dùng, lối "Đổi AI ở Cài đặt →"; Esc / bấm ngoài để đóng | `components/ModelPicker.tsx`, `ChatComposer.tsx` | chọn model lưu Cài đặt, lượt sau dùng model đó |
| D | Chat gọn: nhật ký phiên bỏ hộp nền, 1 dòng/việc, bỏ ký tự Markdown; việc trong câu trả lời bỏ khung viền (vạch trái); câu người dùng là bong bóng bên phải; "Show guides again" vào menu ⋯; ẩn "model unknown" ở dòng đầu câu trả lời | `HuntChat.tsx`, `ChatMessage.tsx`, `ChatPanel.tsx` | không còn hộp lồng hộp trong khung chat |
| E | Đang trả lời: vòng xoay + "Claude đang suy nghĩ… / đang dùng `tool`… / đang viết…" + giây đếm; nút ■ Dừng có vòng xoay quanh | `ChatMessage.tsx` (`Thinking`), `ChatComposer.tsx` | thấy vòng xoay suốt lượt, kể cả khi chữ đang chảy |

Hỏi AI (`ChatPanel`) dùng chung `ChatComposer` + `ChatMessage` nên cũng có B · C · E và bong bóng câu hỏi.

## Kiểm

- `npm run typecheck`, `npx vitest run` (525 test, có `ui-contrast` — chữ không dùng `text-zinc-300/400`), `eslint src/components`.
- Xem trên app thật `localhost:3200/hunt/10` ở 1340px: đầu khung, menu model, nhật ký phiên; lượt trả lời giả lập
  (chặn `fetch` trong trình duyệt, không gọi CLI) cho thấy "Claude is using niche_search… 7s" + nút Dừng xoay.
