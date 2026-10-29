# Phase 28.12 · AI Agent — 2 chặng bước + nhật ký phiên đọc được

> Dùng thật xong thấy 2 chỗ khó hiểu ở trang Phiên săn (`/hunt/:id`): **7 chip bước** xếp lộn xộn 2 hàng, không biết
> chặng nào là thu thập dữ liệu, chặng nào là viết tài liệu; và nhật ký **"What the AI did in this session"** là danh sách
> chữ dài (`BRIEF: mac menu bar customizer — 2026-10-28 # Mac…`) xen dòng "Suggested next steps", nhìn không hiểu.

<span class="chip chip--done">Xong 2026-10-28</span>

## Mục tiêu · cần làm · KHÔNG làm

- **Mục tiêu:** liếc thanh bước biết đang ở chặng nào; liếc nhật ký biết AI đã viết tài liệu gì, lúc mấy giờ, gợi ý gì tiếp.
- **Cần làm:** A chia 7 bước thành 2 chặng · B làm lại hàng nhật ký.
- **KHÔNG làm:** đổi số bước, thứ tự, điều kiện mở bước (`flowAccess`), prompt từng bước; đổi cách ghi nhật ký ở máy chủ;
  dịch nhãn nút gợi ý (AI tự viết, giữ nguyên chữ AI viết).

## Việc

| | Việc | File | Xong khi |
|---|---|---|---|
| A | `FLOW_GROUPS`: **① Research niche** = Find niches · BEST pack · Collect more · Health check; **② Plan the app** (vi "Lên kế hoạch app") = Feature brief · Suggested spec · Build plan (Brief → Spec → Plan). Mỗi chặng 1 hàng: số chặng (✓ khi xong hết) + tên + "4/4 done", rồi chip bước; 2 chặng xếp dọc | `lib/hunt-flow.ts`, `components/HuntFlow.tsx` | thanh bước có 2 hàng có tên chặng |
| B | Hàng nhật ký: Brief / Spec / Plan là **nhãn màu** (BRIEF tím · SPEC xanh dương · PLAN xanh lá) + **tên tài liệu** (tiêu đề `#`, không có thì dòng đầu) + giờ; việc khác có icon tròn màu (+ thêm · ⌕ tra · ✗ loại · ★ giữ); "Gợi ý bước tiếp" thành dòng con "→ Next:" + chip nhỏ dưới việc trước nó | `components/HuntChat.tsx` | không còn chữ `#` / ngày dồn trong nhật ký |

**Tên chặng 2:** "Plan the app" — gói 3 tài liệu Brief (vấn đề + tính năng) → Spec (màn hình, Free/Pro) → Plan (việc theo
mốc), đúng thứ tự pipeline `app-spec` → `app-plan`.

## Kiểm

- `npm run typecheck`, `npx vitest run` (525/525), `eslint` 3 file.
- App thật `localhost:3200/hunt/10` ở 1340px: 2 chặng 4/4 + 3/3 done; nhật ký BRIEF "Mac Menu Bar Customizer — Feature
  Brief" 11:03 · SPEC "Mac Menu Bar Customizer — SPEC" 11:17 · PLAN "MenuBar Pro — kế hoạch xây dựng" 11:32, mỗi cái
  có "→ Next:" chip.
