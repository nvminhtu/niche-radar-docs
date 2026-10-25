# Phase 25 · Cài đặt AI + tuyến AI miễn phí

> Lớp AI chung đã có, nhưng mới chạy thật tuyến job Claude. Phase này cho chọn **nhiều nhà cung cấp** (tự mang key),
> thử lại **tuyến miễn phí** (AI trong Chrome, model trên máy) và cho thấy rõ mỗi lần tra tốn bao nhiêu.

<span class="chip chip--todo">Chưa làm · plan 2026-10-25</span>

<div class="box box--goal" markdown>
**Hiện có (Phase 6).** Trang Cài đặt AI: bật Claude API, chọn model, trần chi phí mỗi lần tra; tuyến B job Claude.
Bước 0 Phase 6: tuyến C (Gemini Nano trong Chrome) chưa thử vì cần tải model; tuyến D (Ollama llama3.1 8B) bỏ vì kém.
</div>

## Làm gì

| | |
|---|---|
| :material-key-chain: **Nhiều nhà cung cấp** | Claude (mặc định) · Gemini Flash · OpenAI — mỗi cái nhập key riêng, nút "thử key"; chọn tuyến cho từng việc (chủ đề than, Feature Gap, khớp tên doanh thu) |
| :material-google-chrome: **Thử lại tuyến C** | khi anh đồng ý tải model: Gemini Nano (Prompt API) chạy bài thử chuẩn của Phase 6 (110 review → chủ đề + câu nguyên văn), ghi chất lượng · thời gian |
| :material-laptop: **Thử lại tuyến D** | model trên máy mới hơn qua Ollama / LM Studio, cùng bài thử; đạt mới bật |
| :material-cash-multiple: **Sổ chi phí** | mỗi lần gọi AI ghi token vào / ra, tiền ước, việc gì, niche nào; tổng theo ngày / tháng, trần tháng |
| :material-test-tube: **Bài thử chuẩn 1 bấm** | chạy cùng 1 bài trên mọi tuyến đang bật → bảng so sánh, để chọn tuyến bằng số |

<div class="box box--rules" markdown>
**Luật**

- Key chỉ lưu trên máy (`.env.local` / file cài đặt trong thư mục dữ liệu), không ghi vào log, không đi theo gói xuất
- Không tự tải model lớn — hỏi anh trước, ghi dung lượng
- Tuyến nào trượt bài thử thì không bật, ghi lý do
</div>

<div class="box box--star" markdown>
**Xong khi**

- Bảng bài thử chuẩn điền đủ các tuyến đã thử (có số đo + ngày)
- ≥ 2 nhà cung cấp chạy được với key thật; sổ chi phí khớp với trang tính tiền của nhà cung cấp (sai ≤ 10%)
- Tắt hết AI → mọi tính năng không AI vẫn chạy
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Gói lượt AI kèm Pro / bán AI — [Phase 69](phase-69-ai-cost-plans.md)
- Key trong Keychain của app Mac — [Phase 79](../app/phase-79-app-only.md)
</div>
