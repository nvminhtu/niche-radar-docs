# Phase 6 · Tích hợp AI (bản Web)

> Để AI **đọc thay mình** review, Reddit, trang listing — có nguồn, tắt được, và **thử cả đường miễn phí**
> (AI chạy ngay trong trình duyệt / trên máy) trước khi bắt trả tiền theo lượt.

<span class="chip chip--todo">Chưa làm · có phần thử nghiệm, chưa chắc làm được hết</span>

## Chạy thế nào

```mermaid
flowchart LR
  subgraph Tuyến AI
    A[A · API key<br/>Claude · Gemini Flash · OpenAI]
    B[B · Extension miễn phí<br/>Claude in Chrome · Gemini in Chrome]
    C[C · AI trong trình duyệt<br/>Chrome built-in AI · WebLLM · Transformers.js]
    D[D · Model trên máy<br/>Ollama · LM Studio]
  end
  A & B & C & D --> L[Lớp AI chung<br/>chọn tuyến · trần chi phí · cache]
  R[Review 1–2★<br/>Play + iOS] --> L
  RD[Bài Reddit] --> L
  LS[Mô tả · What's New] --> L
  L --> TH[Chủ đề than<br/>+ câu nguyên văn]
  L --> TG[Nhãn Reddit]
  L --> M[Feature Gap Matrix<br/>tự động đủ]
  L --> S[Tóm tắt niche<br/>5 dòng có nguồn]
```

## Bước 0 — thử từng tuyến trước khi xây

<div class="box box--goal" markdown>
Một bài thử chuẩn: **gom 200 review 1–2★ của 1 niche thành chủ đề, mỗi chủ đề có câu nguyên văn**.
Chạy bài này trên từng tuyến, ghi **chất lượng · thời gian · tiền · máy cần gì** → chọn ≤ 2 tuyến để xây.
Tuyến nào không chạy được thì ghi lý do và bỏ, không cố.
</div>

| Tuyến | Là gì | Tiền | Câu hỏi phải trả lời ở Bước 0 |
|---|---|---|---|
| **A · API key** | key riêng trong `.env.local` (Claude mặc định, Gemini Flash rẻ) | trả theo lượt | trần chi phí mỗi lần tra đủ thấp chưa? |
| **B · Extension miễn phí** | tool xuất *job* `.json` → extension AI đọc trang / file → nhập kết quả lại (như tuyến B Phase 4) | gói đang có | extension nào nhận file / trả kết quả có cấu trúc được? |
| **C · AI trong trình duyệt** | Chrome built-in AI (Gemini Nano: Summarizer, Prompt API) · WebLLM (model nhỏ trên WebGPU) · Transformers.js (gom chủ đề bằng embedding, không cần LLM) | 0 đ | Prompt API cho trang web đã mở chưa? model nhỏ có trả câu nguồn đúng không? máy cần GPU / bao nhiêu GB? |
| **D · Model trên máy** | Ollama / LM Studio mở API ở `localhost` | 0 đ | model 7–8B trên Mac M-series đủ tốt + đủ nhanh cho 200 review không? |

## Làm gì (sau Bước 0)

| | |
|---|---|
| :material-cog: **Lớp AI chung** | trang Cài đặt: chọn tuyến, nhập key, chọn model, trần chi phí mỗi lần tra, cache theo nội dung, log token + tiền ước tính |
| :material-emoticon-angry: **Chủ đề than** | gom review 1–2★ thành chủ đề (quảng cáo, mất dữ liệu, ép đăng ký…) + số lần + câu nguyên văn |
| :material-reddit: **Phân loại Reddit** | xin app · than app đang dùng · hỏi alternative · không liên quan |
| :material-table-check: **Feature Gap Matrix tự động** | nâng tuyến A [Phase 4](phase-4-feature-gap.md) lên lớp AI chung, đọc thêm What's New + review |
| :material-text-box-check: **Tóm tắt niche** | ai đau gì · đối thủ yếu ở đâu · ai đang thu tiền — mọi câu kèm nguồn |

<div class="box box--rules" markdown>
**Luật AI**

- AI **không bịa số** — số chỉ từ collector, AI chỉ đọc chữ và trả trích dẫn
- Không có AI nào bật → mọi tính năng Phase 1–5 vẫn chạy như cũ
- Tuyến miễn phí cho kết quả kém thì nói rõ trên UI ("model nhỏ — nên kiểm lại"), không giấu
</div>

<div class="box box--star" markdown>
**Xong khi**

- Bảng Bước 0 điền đủ 4 tuyến (chạy được / không, có số đo)
- 3 niche thật chạy đủ với tuyến đã chọn, mỗi lần tra dưới trần chi phí
- Mọi chủ đề / tóm tắt có trích dẫn bấm được; tắt AI thì app vẫn chạy
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Xây cả 4 tuyến — chỉ xây tuyến qua được Bước 0
- Gửi key của mình lên server nào khác ngoài provider
</div>
