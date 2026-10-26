# Phase 18 · Đối thủ bị chê gì

> Từ "vài cụm từ lặp lại" thành **bản đồ lời chê**: app nào bị chê gì, chê kiểu gì, chê mới nổi hay chê cũ,
> và người dùng **ước gì** — mọi dòng có câu nguyên văn. **Không AI** (AI ở [Phase 27.1](phase-27-1-ai-summary.md)).

<span class="chip chip--todo">Chưa làm · plan 2026-10-25</span>

<div class="box box--goal" markdown>
**Hiện có (bản đầu ở Phase 1–2).** `complaints.ts` đếm cụm 1–3 từ trong review 1–2★ của top app Play + iOS, giữ cụm
xuất hiện ≥ 3 review, kèm câu trích. Chạy nhanh, không AI — nhưng còn trùng ý ("crash" · "keeps crashing"), không biết
app nào bị chê, không tách lỗi với thiếu tính năng, bỏ qua review 3★ (chỗ người dùng nói "ước gì").
Mỗi app chỉ đọc **150 review mới nhất** (Play) và **60** (App Store, proxy apps.apple.com vì RSS đã chết), cache bị ghi
đè mỗi 7 ngày — app lớn thì 150 review chỉ phủ vài ngày, nên **không so được "90 ngày trước"** từ một lần lấy.
</div>

**Cần xong trước:** [Phase 2](phase-2-app-store.md) (review iOS) · [Phase 9](phase-9-small-features.md) (bảng mức nặng)

## Chạy thế nào

```mermaid
flowchart LR
  R[Review 1–3★<br/>top 5 app × 2 store] --> N[Chuẩn hoá<br/>gốc từ · đồng nghĩa]
  N --> C[Cụm lời chê]
  C --> T[Gắn loại<br/>luật từ khoá]
  C --> A[Bảng app × cụm]
  C --> H[Mới nổi<br/>so lần lấy trước]
  R --> W[Câu 'ước gì'<br/>review 3★]
```

## Làm gì

| | |
|---|---|
| :material-database-arrow-down: **Lấy đủ review** | top 5 app mỗi store: Play 200 review mới nhất / app (hiện 150), App Store 100 (5 trang × 20, hiện 60 — gọi thưa như cũ). Giữ **1–3★** (hiện chỉ 1–2★; 3★ cho phần "ước gì"), có ngày + số sao; phiên bản chỉ Play có. Cache 7 ngày như hiện tại |
| :material-history: **Nhớ review đã thấy** | mỗi lần lấy, review mới ghi vào lịch sử theo app (khoá = hash nội dung, ngày thấy lần đầu) — **không ghi đè** như cache. Đây là nền cho "mới nổi" và cho cache AI ở [Phase 27.1](phase-27-1-ai-summary.md) |
| :material-merge: **Gộp cùng ý** | gốc từ (crash / crashes / crashing), bảng đồng nghĩa sửa được (`ads` = `advertisement` = `commercials`), bỏ tên app + tên thương hiệu khỏi cụm |
| :material-tag-multiple: **Loại lời chê** | luật từ khoá: Lỗi / crash · Mất dữ liệu · Ép trả phí / giá · Quảng cáo · Thiếu tính năng · Khó dùng · Đồng bộ / tài khoản · Khác. Dùng chung bảng mức nặng của Phase 9 |
| :material-table-account: **App nào bị chê gì** | bảng app × loại lời chê, ô = số review + bấm ra câu trích. Thấy ngay app nào yếu ở đâu |
| :material-trending-up: **Mới nổi** | so review **mới thấy ở lần lấy này** với lịch sử đã lưu: cụm có ≥ 3 review mới và tỉ lệ ≥ 2× trước đó → "mới nổi" (thường là bản cập nhật hỏng hoặc vừa đổi giá). App nhỏ mà 200 review đã phủ ≥ 180 ngày thì so thẳng theo ngày (90 ngày gần nhất vs 90 ngày trước). Lần lấy đầu, chưa đủ ngày → ghi "chưa có lần trước để so", không đoán |
| :material-lightbulb-on: **Người dùng ước gì** | lọc câu "wish / would be nice / please add / missing / need a way to" ở review 1–3★ → danh sách tính năng được xin, đếm số lần |
| :material-filter: **Lọc + mở gốc** | lọc theo store, app, loại, khoảng thời gian; câu trích bấm mở đúng trang review / app |
| :material-file-export: **Ra ngoài** | cụm + câu trích vào evidence pack và gói xuất ([Phase 15](phase-15-export.md)) |

<div class="box box--rules" markdown>
**Luật**

- Mỗi cụm ≥ 3 review khác nhau, mỗi câu trích **khớp nguyên văn** review gốc (kiểm bằng code như Phase 6)
- Không dịch, không viết lại câu của người dùng
- Luật gộp và luật loại nằm trong 1 file, có test; thêm từ mới không cần sửa code
</div>

<div class="box box--star" markdown>
**Xong khi**

- 3 niche thật: kiểm tay top 10 cụm mỗi niche, ≥ 8/10 cụm có nghĩa (không phải từ rác)
- Gộp cùng ý làm số cụm trùng ý giảm rõ (đếm trước / sau trên cùng 3 niche, ghi số)
- Bảng app × loại đọc được ở 1340px, mọi ô bấm ra câu trích đúng app
- Danh sách "ước gì" có ≥ 5 dòng ở ít nhất 2 / 3 niche
- Mới nổi: test 2 lần lấy giả (cụm tăng / không tăng) đúng nhãn; niche thật lần đầu hiện "chưa có lần trước để so"
- Test xanh, screenshot đã Read
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- AI gom chủ đề / viết tóm tắt — [Phase 27.1](phase-27-1-ai-summary.md)
- So sánh 2–5 đối thủ cạnh nhau — [Phase 55](phase-55-compare-competitor.md)
- Lấy review ngoài 2 store (Reddit, YouTube…) — [Phase 11](phase-11-reddit-gap.md), [Phase 51](phase-51-youtube-ai.md)
</div>

Plan code chi tiết: [Phase 18](../superpowers/plans/2026-10-25-niche-radar-phase12-competitor-complaints.md)
