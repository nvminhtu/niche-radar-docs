# Phase 3 · Google Trends

> Biết nhu cầu **đang lên hay xuống**, ở **nước nào**, có **mùa vụ** không.

<span class="chip chip--doing">Có cơ bản · 12 tháng + related queries cho 1 keyword (từ v1)</span>

## Chạy thế nào

```mermaid
flowchart LR
  TOP[Top 10 cơ hội<br/>từ Phase 1–2] --> T[Google Trends]
  T --> D[Lên / Xuống / Phẳng<br/>12 tháng]
  T --> S[So 5 keyword]
  T --> C[Theo nước / vùng]
  T --> M[Mùa vụ 5 năm]
  T --> RT[Related topics]
```

## Làm gì

| | |
|---|---|
| :material-trending-up: **Cột xu hướng** | lên / xuống / phẳng cho từng keyword Top 10 |
| :material-chart-line: **So 5 keyword** | cùng một biểu đồ (giới hạn của Trends) |
| :material-earth: **Theo nước / vùng** | nước nào quan tâm nhất |
| :material-calendar-sync: **Mùa vụ 5 năm** | đỉnh theo mùa (back-to-school, đầu năm…) |
| :material-tag-multiple: **Related topics** | chủ đề liên quan ngoài related queries |

Chỉ hỏi Trends cho **Top 10** — Trends chặn rất nhanh nếu hỏi nhiều. Chống bị chặn: gom request, cache dài cho
dữ liệu 5 năm, backoff.

<div class="box box--star" markdown>
**Xong khi**

- Top 10 của 3 niche thật có cột xu hướng, một lần chạy không bị Trends chặn
- So 5 keyword + theo nước + mùa vụ chạy được trên 1 niche thật
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Hỏi Trends cho cả 100 keyword
- Số lượt tìm thật (Trends chỉ cho chỉ số tương đối 0–100)
</div>
