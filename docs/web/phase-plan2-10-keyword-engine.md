# 10 · Keyword Intelligence

> Plan 2 · mục 10. Biến cây keyword của Explorer thành trang **Soi cơ hội**: ma trận cơ hội, xếp hạng có giải thích điểm,
> độ đông app store, ý định tìm kiếm, so xu hướng, nguồn số và soát dữ liệu. Làm theo bản blueprint 8 phase anh gửi
> 2026-11-13, chia nhỏ: làm Phase 1–3 rồi dừng cho anh duyệt.

<span class="chip chip--doing">Phase 1–3 làm 2026-11-13 → 14, chưa ra bản · Phase 4–8 chưa làm</span>

## Quyết định đã chốt (2026-11-13)

- **Chỗ đặt:** module trong Niche Radar. Code ở `web/src/keyword-engine/`, 1 trang mới `/intel/:id`, mở từ nút *Soi cơ hội* ở Explorer.
- **Nguồn số:** chỉ dùng số miễn phí đã có. Chart nào cần lượt tìm / CPC / độ khó SEO thì nguồn để sẵn, hiện xám *sắp có*, không số giả.
- **Thư viện biểu đồ:** Recharts (đang dùng). ECharts chỉ cho 2 chart khó (network graph, treemap cụm) ở Phase 4, tải lười.
- **Phạm vi lần này:** Phase 1–3, xem tận mắt trên số thật rồi dừng.

## Luật của engine

- **Mỗi số mang nhãn nguồn:** nguồn, ngày lấy, nước, đơn vị, trạng thái (*thật* · *ước* · *suy ra* · *thiếu*). Số thiếu là `null`, không bao giờ là 0.
- **3 kiểu “cạnh tranh” tách riêng, không gộp:** độ đông app store (tổng rating top 5 App Store) ≠ cạnh tranh quảng cáo Google Ads ≠ độ khó SEO (KD).
  Trang hiện tại chỉ có kiểu đầu.
- **Google Trends là chỉ số tương đối 0–100**, không phải lượt tìm. Mỗi keyword lấy ở lượt tra riêng nên thang không so thẳng được;
  chart so xu hướng mặc định chia mỗi đường cho mức trung bình của chính nó (100 = mức thường).
  Chuỗi có hơn nửa số tuần bằng 0 (quá ít người tìm) không vẽ, trang ghi số keyword bị bỏ.
- **Điểm cơ hội là quy ước của ShotMatic, không phải chuẩn ngành.** 6 chiều: cầu 25% · dễ chen 25% · tăng trưởng 15% · ý định 15% · CPC 10% · độ đều 10%.
  Trọng số sửa được trên trang (lưu trong trình duyệt). Chiều thiếu số bị bỏ và trọng số chia lại trên phần còn lại;
  phần có số dưới 50% tổng trọng số thì không chấm (ghi *chưa đủ số*). Mỗi điểm có bảng phần đóng góp.
- **Ý định tìm kiếm suy từ từ ngữ** (best, vs, download, how to, near me…), không phải nhãn Google. Không khớp luật nào → *Chưa rõ*,
  không tự gán *Tìm tên cụ thể* vì tool chưa có danh sách thương hiệu; nhóm *Chưa rõ* không được cộng điểm ý định.

## Checklist 8 phase

- [x] **Phase 1 · Nghiên cứu** — stack hiện có, số đang có / chưa có, so thư viện chart, repo skill, sản phẩm tham khảo, rủi ro.
  Trang [10.1 · Nghiên cứu](phase-plan2-10-nghien-cuu.md).
- [x] **Phase 2 · Data model + nguồn số + chấm điểm** — kiểu dữ liệu có nhãn nguồn, đọc cây Explorer thành bộ keyword, đoán ý định,
  điểm cơ hội có độ tin, phép tính cho chart, soát dữ liệu (trùng hoa / thường / dấu, số ngoài khoảng, ngày tương lai, Trends thiếu tuần, trộn nước…). Có test.
- [x] **Phase 3 · 5 chart lõi trên số thật** — trang *Soi cơ hội*: khối kết luận + top 3, ô số, ma trận cơ hội (bấm chấm xem điểm),
  xếp hạng Top 10 / 20 / 50 + bảng phần điểm + sửa trọng số, độ đông app store 5 bậc (bấm cột để lọc), ý định tìm kiếm (2 cách đo, bấm nhãn để lọc),
  so xu hướng tối đa 5 keyword, nguồn số, soát dữ liệu. Soát 960px tối và 1340px sáng, không cuộn ngang.
- [ ] **Phase 4 · Chart nâng cao** — network graph keyword, treemap cụm (ECharts, tải lười), lịch sử theo lần tra, so đối thủ.
- [ ] **Phase 5 · Đủ màn hình + xuất** — các màn hình còn lại của blueprint, xuất CSV / ảnh chart.
- [ ] **Phase 6 · AI trợ lý** — trả lời có dẫn số + nguồn, không tự sinh số.
- [ ] **Phase 7 · Nguồn trả phí / có tài khoản** — nối Google Ads Keyword Planner, DataForSEO hoặc Search Console khi anh chốt nguồn.
- [ ] **Phase 8 · Skill + test giao diện** — skill cho agent, test chạy trình duyệt.

## Nguồn số

| Nguồn | Trạng thái | Cho số gì | Chi phí / quota |
|---|---|---|---|
| Explorer (Play / Google / App Store gợi ý, rating top 5) | Đã nối | độ phổ biến 0–100, độ đông app store, số app | miễn phí, đã có |
| Google Trends (qua Explorer, bấm *Xem xu hướng*) | Đã nối | chỉ số quan tâm tương đối theo tuần, 12 tháng | miễn phí, đã có |
| Google Ads Keyword Planner | Sắp có | lượt tìm / tháng (dạng khoảng), CPC, cạnh tranh quảng cáo | cần tài khoản Google Ads · quota `chưa đo` |
| DataForSEO | Sắp có | lượt tìm, CPC, độ khó SEO | trả phí · giá `chưa đo` |
| Google Search Console | Sắp có | lượt hiện / bấm thật của site mình | cần quyền site · miễn phí |

Không scrape hay lách giới hạn của nguồn nào.

## Rủi ro đang thấy

- Phần lớn keyword của cây là tên chung → ý định *Chưa rõ* chiếm đa số, điểm cơ hội chủ yếu dựa vào cầu + dễ chen.
- Trends chỉ có ở keyword đã bấm *Xem xu hướng* và keyword nhỏ hay bị Trends ghi 0 → chart so xu hướng nhiều cây sẽ trống.
- Đường chia ma trận là trung vị của chính cây đó: so tương đối trong niche, không phải ngưỡng tuyệt đối giữa các niche.
