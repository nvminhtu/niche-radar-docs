# Niche Radar Phase 21 — Explore: cây keyword + bản đồ ngách — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự, mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [ ]`).

**Goal:** cây **sạch hơn** (ít rác, ít trùng), nguồn gợi ý rõ hơn, điểm cơ hội **giải thích được**, từ cây đi thẳng sang Research hàng loạt.

**Spec:** [Phase 21 · Explore](../../web/phase-21-explore-tree.md) · **Cần trước:** Phase 1 (`lib/explore.ts`, `explore-view.ts`), Phase 2 (`appstore_hint`).

## Mục tiêu · làm · không làm

- **Xong khi:** 3 niche thật: keyword rác trong top 30 trước / sau lọc (ghi số), sau ≤ 3/30 · gộp cùng nghĩa không nuốt keyword
  khác nghĩa (kiểm tay 20 nhóm) · Research hàng loạt 5 lá chạy hết không bị chặn · test xanh · screenshot cây + bản đồ đã Read.
- **Làm:** lọc rác (xem lại được), gộp cùng nghĩa, lọc theo nguồn gợi ý, giải thích điểm, chọn lá → Research hàng loạt (lần lượt), bản đồ nhóm theo ý định.
- **Không làm:** số lượt tìm thật trả phí · làm nhanh Explore (Phase 47).

## Global Constraints

- **Không tự xoá keyword**: lọc / gộp chỉ gắn cờ (`filtered`, `mergedInto`) trên `explore_nodes`; mục "đã lọc" bỏ lọc được.
- Luật lọc + danh sách chặn (thương hiệu, tên app top) trong `web/src/lib/explore-rules.ts`, sửa được ở Cài đặt (lưu `settings`).
- Gộp cùng nghĩa bằng khoá chuẩn hoá: gốc từ + bỏ stopword ("app", "for") + sắp từ; giữ biến thể bên trong nút.
- Research hàng loạt: **lần lượt** (1 lượt một lúc), dùng `startResearch` + hàng đợi **lưu ở bảng `research_queue`** (không
  chỉ trong bộ nhớ): server khởi động lại thì lá `running` dở về `queued` và chạy tiếp. Giữ rate limit hiện có. Phase 23
  dùng chung hàng đợi này.
- Nhãn "ước lượng — không phải lượt tìm thật" giữ nguyên cạnh điểm cơ hội.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/db/schema.ts` + migration mới | `explore_nodes`: `filtered` (lý do), `mergedInto` (nodeId); bảng `research_queue` (explorationId, nodeId, runId, status) |
| `web/src/lib/explore-rules.ts` (mới) | luật rác: thương hiệu, tên app top trong run, số nhiều / thứ tự từ, ngoài niche (không chứa từ nào của seed và không ở nhóm) |
| `web/src/lib/explore.ts` | áp luật sau khi dựng cây; `mergeKey()`; `popularity()` trả thêm `explain` |
| `web/src/lib/batch-research.ts` (mới) | hàng đợi lần lượt, hoãn khi bị chặn |
| `web/src/server/app.ts` | `POST /explore/:id/nodes/:nodeId/unfilter` · `/unmerge` · `POST /explore/:id/batch-research` · `GET /explore/:id/batch` |
| `ExploreDashboard.tsx`, `NicheMap.tsx`, `KeywordTable.tsx`, `ExploreShared.tsx` | mục "đã lọc", nút gộp, chip nguồn + lọc nguồn, tooltip điểm, ô tick + "Research N lá", bản đồ nhóm theo ý định + ô tìm |
| `web/tests/explore-rules.test.ts`, `batch-research.test.ts` | |

## Tasks

### Task 1: Đo trước
- [ ] 3 niche: đếm tay keyword rác trong top 30 → "trước".

### Task 2: Lọc rác (xem lại được)
- [ ] `explore-rules.ts` + migration cờ; mục "đã lọc" + nút bỏ lọc. Test từng luật.

### Task 3: Gộp cùng nghĩa
- [ ] `mergeKey` ("budget app" · "budgeting app" · "app for budget" → 1); nút hiện biến thể, bỏ gộp được.
- [ ] Test: không gộp "budget app" với "budget planner".

### Task 4: Nguồn gợi ý + giải thích điểm
- [ ] Chip nguồn (Play · Google · App Store) trên từng keyword, lọc theo nguồn.
- [ ] Tooltip / bấm: phổ biến bao nhiêu, độ đông bao nhiêu, từ đâu.

### Task 5: Research hàng loạt
- [ ] Tick 3–10 lá → hàng đợi lần lượt + tiến độ; bị chặn → hoãn, báo. Test với deps giả.
- [ ] Khởi động lại giữa chừng: `resumeQueue()` lúc server start. Test: 5 lá, dừng sau lá 2 → chạy tiếp 3 lá, không chạy lại lá đã xong.

### Task 6: Bản đồ ngách
- [ ] Nhóm theo ý định (tính năng · đối tượng · nền tảng · khác — dùng `classify`), lọc nhóm, tìm keyword.

### Task 7: Soát
- [ ] Đếm lại rác → "sau"; kiểm tay 20 nhóm gộp; chạy 5 lá. Screenshot 1340 + 375, Read. Chip, ROADMAP, CHANGELOG.

## Tiến độ

- 2026-10-25: viết plan. Explore hiện ~6 phút / niche.
- 2026-10-26: review plan — hàng đợi lưu DB, chạy tiếp sau khi tắt server (Phase 23 dùng chung).
