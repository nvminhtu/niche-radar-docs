# Phase 40 · Explore niche — cây keyword + bản đồ ngách

> Explore mở 1 niche thành ~100 keyword. Phase này làm cây **sạch hơn** (ít rác, ít trùng), **rộng hơn** (thêm nguồn
> gợi ý), điểm cơ hội **giải thích được**, và từ cây đi thẳng sang Research hàng loạt.

<span class="chip chip--doing">Một phần · soát code 2026-10-27: có bản đồ ngách theo nhóm + Research sâu nhiều lá · chưa lọc keyword rác, chưa gộp cùng nghĩa, chạy lá chưa nối lại được sau khi tắt server</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 1).** Gợi ý Play + Google → cây ≤ 100 keyword → đếm đối thủ từng keyword → điểm cơ hội
`phổ biến × (1 − độ đông)` → bản đồ ngách + Top 10, Flow niche (chốt lá làm long-tail), CSV. Explore mất ~6 phút;
cây còn keyword trùng nghĩa, tên thương hiệu, từ không liên quan.
</div>

**Cần xong trước:** [Phase 1](phase-1-google-play.md) (cây keyword) · [Phase 2](phase-2-app-store.md) (gợi ý App Store)

## Làm gì

| | |
|---|---|
| :material-broom: **Lọc rác** | bỏ tên thương hiệu / tên app có sẵn, keyword chỉ khác số nhiều / thứ tự từ, keyword ngoài niche (luật + danh sách chặn sửa được) — keyword bị lọc vẫn xem được ở mục "đã lọc" |
| :material-merge: **Gộp cùng nghĩa** | "budget app" · "budgeting app" · "app for budget" → 1 nút, giữ các biến thể bên trong |
| :material-source-branch-plus: **Nguồn gợi ý** | gợi ý App Store **đã có từ Phase 2** (nguồn `appstore_hint`, đo 2026-10-24: `water reminder` 23/100 keyword, 10 chỉ App Store gợi ra) — phase này chỉ làm rõ hơn trên UI nguồn nào gợi ý, lọc theo nguồn |
| :material-calculator-variant: **Điểm cơ hội giải thích được** | di chuột / bấm → phổ biến bao nhiêu, độ đông bao nhiêu, từ đâu; nhãn "ước lượng — không phải lượt tìm thật" giữ nguyên |
| :material-select-group: **Chọn lá → Research hàng loạt** | tick 3–10 lá → chạy Research lần lượt (không song song cho đỡ bị chặn), có hàng đợi + tiến độ. Hàng đợi lưu trong DB: tắt server / đóng app giữa chừng, mở lại chạy tiếp lá còn lại |
| :material-map: **Bản đồ ngách dễ đọc** | nhóm theo ý định (tính năng · đối tượng · nền tảng · khác), lọc nhóm, tìm keyword trên bản đồ |

<div class="box box--rules" markdown>
**Luật**

- Không tự xoá keyword: lọc / gộp đều xem lại và bỏ lọc được
- Thêm nguồn gợi ý phải giữ giới hạn gọi của từng nguồn (rate limit hiện có)
</div>

<div class="box box--star" markdown>
**Xong khi**

- 3 niche thật: đếm keyword rác trong top 30 trước / sau lọc (ghi số), sau lọc ≤ 3 / 30
- Gộp cùng nghĩa không nuốt keyword khác nghĩa (kiểm tay 20 nhóm gộp)
- Research hàng loạt 5 lá chạy hết không bị chặn, có kết quả từng lá; tắt server sau lá 2 → mở lại chạy tiếp lá 3
- Test xanh, screenshot cây + bản đồ đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Số lượt tìm thật trả phí (DataForSEO, Keyword Planner) — Appendix
- Làm nhanh Explore — [Backlog 06](phase-backlog-06-fast-collector.md)
</div>

Plan code chi tiết: [Phase 40](../superpowers/plans/2026-10-25-niche-radar-phase21-explore-tree.md)
