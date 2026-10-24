# Cách dùng

## Chạy app

```bash
npm install
cp .env.example .env.local   # điền key Reddit (tuỳ chọn — không có thì 3 nguồn kia vẫn chạy)
npm run dev                  # mở http://localhost:3200
```

Dữ liệu nằm ở `data/niche.db`. Xoá file này = xoá sạch lịch sử.

## Explore một niche (tìm ngách)

1. Trang chủ → bấm **Explore niche** → gõ niche (tiếng Anh, ví dụ `meal planner`) → chọn nước → **Explore**.
2. Chờ khoảng 6 phút cho 100 keyword. Trang tự cập nhật: lấy gợi ý (≈ 1 phút), rồi đếm đối thủ từng keyword (≈ 3 giây/keyword).
3. Đọc kết quả:
    - **Cây ngách** — keyword gom theo đối tượng / dạng / nền tảng / tính năng. "Mở tiếp" để đào sâu một nhánh.
    - **Bảng keyword** — sắp theo điểm cơ hội. Chấm màu độ đông: xanh < 0.4 · vàng 0.4–0.7 · đỏ > 0.7.
    - **Bản đồ ngách** — góc trên bên trái (phổ biến cao, ít đối thủ) là chỗ đáng soi.
    - **Top cơ hội** — 10 keyword điểm cao nhất, bấm **Research sâu** (tối đa 5 cái một lần).
4. **Tải CSV** để mở bằng Numbers/Excel. **Mở rộng thêm** / **Mở tiếp** để lấy thêm ≤ 50 keyword.

![Bản đồ ngách](images/explore-map.jpg)

### Điểm cơ hội đọc thế nào

```
điểm = phổ_biến × (1 − độ_đông)
phổ_biến  0–100 : được Play/Google gợi ý ở càng nhiều truy vấn, hạng càng cao → càng cao
độ_đông   0–1   : log10(1 + tổng rating 5 app top App Store) / 6   (1 triệu rating ≈ 1.0)
```

!!! warning "Ước lượng, không phải lượt tìm thật"
    Độ đông đang lấy từ App Store, nên keyword chỉ mạnh trên Play có thể bị chấm "ít đông" sai.
    Phase 2 (App Store Search) sẽ tách độ đông riêng cho iOS và Play.

## Research 1 keyword

Trang chủ → **Research 1 keyword** → gõ keyword → **Research**. Kết quả cache 24 giờ; nút
"Tra lại (bỏ cache)" để lấy mới. Nguồn nào lỗi thì có nút **Thử lại** riêng nguồn đó.
Nút **Đọc review 1–2★** gom câu than lặp lại của top 3 app Play (cache 7 ngày).

## Khi bị chặn

Play, Trends, Google gợi ý không có API chính thức → gọi dồn dập sẽ bị chặn tạm (thường 10–30 phút).
Một người, mạng nhà, **vài chục lần tra/ngày là ổn**. Bị chặn thì đợi rồi bấm Thử lại.

## Lệnh hay dùng

| Lệnh | Làm gì |
|---|---|
| `npm run dev` | chạy app (web 3200 + API 3201) |
| `npm test` · `npm run typecheck` · `npm run lint` | kiểm code |
| `npm run smoke -- "<niche>" US` | gọi thật 4 nguồn, in số dòng lấy được |
| `npm run docs` | mở trang tài liệu này ở http://127.0.0.1:3210 |
| `npm run docs:build` | build tài liệu ra `site/` |
