# Phase 4 · Feature Gap Matrix

> Biết **đối thủ đang thiếu tính năng gì** — chỗ để app mình khác biệt (wedge).

<span class="chip chip--todo">Chưa làm</span>

## Chạy thế nào

```mermaid
flowchart LR
  APPS[Top 5 app mỗi store<br/>từ Phase 1–2] --> R[Bản nháp luật từ khoá<br/>mô tả · IAP · review]
  R --> Q{Ô còn ?}
  Q -->|Tuyến A| AI[AI API key<br/>điền + câu nguồn]
  Q -->|Tuyến B| CH[Claude in Chrome<br/>đọc trang listing]
  AI --> M[Feature Gap Matrix]
  CH --> M
  M --> W[Khoảng trống<br/>≤ 1/5 app có → wedge]
```

## Bảng trông thế nào

| Tính năng | App A | App B | App C | … |
|---|---|---|---|---|
| Offline | Có | Có | Không | |
| Không quảng cáo | Trả phí | Không | Có | |
| Widget | Có | ? | Không | |
| Mua một lần | Không | Không | Không | ← **khoảng trống** |

*Bảng minh hoạ, không phải dữ liệu thật.* Mỗi ô `Có / Không / Trả phí / ?` đều kèm **câu nguồn** + link.

## Làm gì

| | |
|---|---|
| :material-format-list-checks: **Hàng mặc định** | offline · không quảng cáo · widget · đồng bộ · mua một lần · subscription · dùng thử · AI · xuất dữ liệu · không cần tài khoản (sửa được) |
| :material-text-search: **Bản nháp không AI** | luật từ khoá trên mô tả + IAP + review → điền ô chắc chắn, còn lại `?` |
| :material-key: **Tuyến A — AI API key (tối thiểu)** | một provider, key trong `.env.local`, tắt mặc định; AI điền ô `?`, bắt buộc trả câu nguồn |
| :material-google-chrome: **Tuyến B — Claude in Chrome** | tool xuất *matrix job* `.json` → Claude mở từng trang listing đọc → nhập kết quả lại. Không cần key trong app |
| :material-lightbulb-on: **Cột "Khoảng trống"** | tính năng ≤ 1/5 app có → gợi ý wedge |

<div class="box box--star" markdown>
**Xong khi**

- 3 niche có matrix 5 app × 10 hàng, ≤ 20% ô còn `?`, mọi ô `Có/Không` có câu nguồn
- Chạy được cả tuyến A và tuyến B ít nhất 1 lần
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Lớp AI đầy đủ (chọn provider, trần chi phí, trang cài đặt, AI miễn phí trong trình duyệt) — [Phase 6](phase-6-ai-web.md)
- AI tự điền ô không có câu nguồn
</div>
