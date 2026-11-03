# Phase 52 · YouTube Research (AI)

> Để AI **xem / đọc thay mình** video và comment của niche: người xem than gì, xin gì, đang dùng app / tool nào —
> có trích dẫn kèm mốc thời gian.

<span class="chip chip--done">Xong bản đầu 2026-11-02 · tuyến comment → khung Hỏi AI</span>

<div class="box box--star" markdown>
**Đã làm (2026-11-02)** — khối "Người xem nói gì" trong tab YouTube

- Lấy comment 5 video nhiều view nhất của keyword gốc (3 trang ≈ 60 comment / video), không lưu tên người comment
- Nút ✦ gửi khung Hỏi AI một câu hỏi có sẵn comment (xếp theo lượt thích, ≤ 3.900 ký tự): gom chủ đề than · xin tính năng · tool được nhắc, mỗi ý kèm câu nguyên văn + nhãn video `[vN]`, rồi 3 ý tưởng app
- Dùng lớp AI đang có (Claude Code / Codex trên máy) — tắt AI thì Phase 51 vẫn chạy

**Chưa làm:** phụ đề (vẫn hỏng như đo ở Backlog 27) · tuyến Gemini đọc link · tóm tắt video có mốc giây · đẩy nhu cầu sang Feature Gap Matrix · bảng thử tuyến
</div>


## Chạy thế nào

```mermaid
flowchart TB
  V[Top video<br/>từ Phase 51] --> TR[Phụ đề<br/>youtubei.js]
  V --> CM[Comment top 200<br/>mỗi video]
  TR & CM --> L[Lớp AI chung<br/>Phase 6]
  V -->|tuỳ chọn| G[Gemini đọc thẳng<br/>link YouTube]
  V -->|tuỳ chọn| CH[Claude in Chrome<br/>mở trang video]
  L & G & CH --> P[Chủ đề than · xin tính năng<br/>· tool được nhắc]
  P --> Q[Trích dẫn<br/>link + mốc giây]
```

## Chọn tuyến AI

| Tuyến | Đọc gì | Tiền | Ghi chú |
|---|---|---|---|
| **Phụ đề + comment → lớp AI Phase 6** (đề xuất chính) | chữ đã lấy bằng `youtubei.js` | theo tuyến đã chọn ở Phase 6 (có thể 0 đ) | rẻ nhất, dùng lại toàn bộ Phase 6 |
| **Gemini API đọc link YouTube** | cả hình + tiếng của video | trả theo lượt (rẻ với Flash) | hợp video không có phụ đề / demo app trên màn hình — kiểm giới hạn lúc làm |
| **Claude in Chrome** | trang video + comment trong trình duyệt của anh | gói Claude đang có | tool xuất *job* `.json` (danh sách video + câu hỏi) → Claude đọc → nhập kết quả `.json` |

**Đo 2026-11-02 ([Backlog 27](phase-backlog-27-youtube-chrome-skill.md#bang-thu-buoc-0-o-2026-11-02)):** comment lấy được (200 / video, 16 giây), **phụ đề không lấy được** bằng YouTube.js lẫn yt-dlp → tuyến chính tạm là **comment**, phụ đề đi qua Gemini hoặc vidIQ.

Không biết tuyến nào tốt hơn → chạy cùng **bài thử chuẩn** trên 10 video của 1 niche (như Bước 0 Phase 6), ghi
chất lượng · thời gian · tiền rồi chọn.

## Làm gì

| | |
|---|---|
| :material-emoticon-angry: **Chủ đề than** | gom comment thành chủ đề + số lần + câu nguyên văn |
| :material-lightbulb-on: **Xin tính năng** | "wish there was an app that…", "how do I…" → danh sách nhu cầu chưa ai đáp |
| :material-apps: **Tool / app được nhắc** | app, web, template người xem đang dùng → nối sang đối thủ ở Phase 1–2 |
| :material-text-box-check: **Tóm tắt video** | 5 dòng mỗi video, mỗi câu có mốc giây bấm được |
| :material-table-plus: **Vào Feature Gap Matrix** | tính năng được xin nhiều → gợi ý hàng mới cho matrix Phase 4 |

<div class="box box--rules" markdown>
**Luật AI** (giống Phase 6)

- AI không bịa số — view, sub, số comment lấy từ Phase 51
- Mọi câu kèm link video + mốc giây hoặc link comment
- Tắt AI → Phase 51 vẫn chạy
</div>

<div class="box box--star" markdown>
**Xong khi**

- Bảng thử tuyến điền đủ (ít nhất phụ đề + comment và 1 tuyến khác)
- 3 niche thật có chủ đề than + xin tính năng, mọi câu có trích dẫn bấm được
- Mỗi lần tra dưới trần chi phí đặt sẵn
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Tải video về máy, xử lý video bằng ffmpeg
- Đăng comment / tương tác với kênh
</div>

Plan code chi tiết: [Phase 52](../superpowers/plans/2026-10-25-niche-radar-phase32-youtube-ai.md)
