# Plan · Data research · 10 bài từ keyword đang lên trên Google Trends

<span class="chip chip--todo">Plan · chờ duyệt · 2026-11-08 · khung trang đã dựng ở nhánh `footer-data-research`</span>

<div class="box box--goal" markdown>
**Nó là gì**

Một mục mới trên shotmatic.app: **`/research`**. Mỗi bài là một keyword đang được tìm nhiều trên Google Trends, chạy qua
chính ShotMatic, rồi đăng **ảnh chụp kết quả thật** kèm phần đọc số. Người đọc thấy tool làm được gì trên đúng chủ đề họ
đang tìm, còn site có bài nhắm vào keyword có lượng tìm thật.

**Target:** 10 bài trong 8 tuần. Bài đầu lên trước 2026-12-01 để kịp đỉnh Năm Mới.

**Xong khi:** 10 bài live ở `/research`, mỗi bài có ít nhất 4 ảnh thật của ShotMatic và số Trends có ngày đo.
</div>

Ngày 2026-11-07 đã chốt chưa viết bài mới tới khi có số Search Console. Ngày 2026-11-08 Tu yêu cầu mục này, nên plan này
là ngoại lệ: bài data research khác bài blog thường vì nó vừa là bài SEO vừa là demo của sản phẩm.

## Trên site đã có gì

- **Footer mới** kiểu AppTweak trên mọi trang: 5 cột link (Product, Free tools, Resources, About, Legal), Follow us,
  ô email "Never miss a niche report". Mục Follow us mới có GitHub releases và RSS. Có tài khoản TikTok, YouTube hay X
  của ShotMatic thì thêm vào `FOLLOW` trong `components/niche-radar/SiteFooter.jsx`.
- **Trang `/research`**: liệt kê bài, cách làm 4 bước, danh sách keyword sắp ra, ô email. Trang để `noindex` cho tới khi
  có bài đầu, sau đó tự vào sitemap.
- **Chủ đề blog mới `data-research`**: bài vẫn nằm ở `/blog/<slug>` nên ăn sẵn RSS, sitemap, llms.txt, JSON-LD.
- **Menu blog** có thêm mục Research.

## 10 keyword và thứ tự đăng

Số lấy từ Google Trends, US, 12 tháng, đo 2026-11-08. Số Trends là tương đối trong từng lần so sánh, nên chỉ so được trong
cùng một keyword (đỉnh so với lúc thường). Từ tháng 7/2026 mọi đường đều tụt cùng lúc, có thể do Google đổi cách lấy mẫu,
nên đọc đỉnh của mùa trước làm mốc. Thứ tự đi theo mùa: bài cần có trước đỉnh 3 đến 6 tuần để Google kịp index.

**1 · habit tracker app** — đăng trước 2026-12-01. Tuần 2025-12-28 lên 9, lúc thường 2 đến 3: gấp 3 lần quanh Năm Mới.

**2 · budget app** — đăng trước 2026-12-08. Cao nhất tuần 2026-01-25 (23), giữ 18 đến 22 suốt quý 1.

**3 · calorie tracker app** — đăng trước 2026-12-08. Đứng đầu nhóm "tracker app" (100). "calorie counter" lên đỉnh tuần
2026-01-04 (24, lúc thường 14).

**4 · bible app** — đăng trước 2026-12-15. Tuần 2025-12-28 lên 23, lúc thường 12.

**5 · GLP-1 tracker app** — đăng trước 2026-12-15. "free glp1 tracker app" là truy vấn đang lên (+100% trong 3 tháng)
trong nhóm "tracker app". Ít đối thủ viết, dễ là bài khác biệt nhất.

**6 · language learning app** — đăng trước 2027-01-05. Đỉnh tháng 2 và tháng 6 (48 đến 54). "language learning app"
đang lên +400% trong 3 tháng.

**7 · period tracker app** — đăng trước 2027-01-12. Không theo mùa nhưng đứng thứ 3 trong nhóm "tracker app" (69).

**8 · journal app** — đăng trước 2027-01-19. Tuần 2026-01-25 lên 67, đỉnh năm 2026-06-07 (100).

**9 · dog training app** — đăng trước 2027-02-15. Lượng tìm lớn nhất trong các keyword đã so, đỉnh tháng 4 (100).
Đây là bài "dog care" Tu nêu ví dụ. "dog training tips" đang lên +1050%.

**10 · sleep tracker app** — đăng trước 2027-02-22. Bật lên từ 3 tới 25 trong tháng 3 đến tháng 4/2026.

Trước khi viết mỗi bài, đo lại keyword đó trên Google Trends và Google Autocomplete. Số trên chỉ để xếp thứ tự.

## Mỗi bài làm thế nào

1. **Đo lại Trends** cho keyword: 12 tháng US, truy vấn top và đang lên. Ghi ngày đo.
2. **Chạy ShotMatic** với keyword đó (US). Xem `source_jobs` trước khi tin số: `Play 0` có thể là chưa đo được.
3. **Chụp 5 ảnh** cùng một lượt chạy (xem mục dưới).
4. **Đẩy ảnh lên `app-demo`** ở `shotmatic/research/<slug>/`, đợi `curl -I` trả 200 rồi mới push repo shotmatic
   (luật trong `CLAUDE.md` của repo shotmatic).
5. **Viết bài** theo skill `shotmatic-blog`, `topic: data-research`, `keyword:` đúng như trong danh sách trên để trang
   `/research` tự gạch keyword khỏi mục "Coming next".
6. **Chạy `npm run blog:check`**, build, mở bài ở 1340px và 375px, rồi commit.

## 5 ảnh cần chụp mỗi keyword

Tên file đánh số để bài nào cũng xếp giống nhau. Định dạng `.webp`, rộng 1600px, chụp app ở chế độ sáng.

- **`01-score.webp`** — điểm sức khoẻ niche và nhãn tin cậy.
- **`02-top-apps.webp`** — top app trên Google Play và App Store, có rating và lượt tải.
- **`03-complaints.webp`** — phàn nàn từ review 1–2★.
- **`04-trends.webp`** — đường Google Trends 12 tháng và truy vấn liên quan.
- **`05-gap.webp`** — khoảng trống, chỗ app nhỏ có thể chen vào.

Mỗi ảnh trong bài có chú thích ghi ngày chụp, ví dụ
`![Top habit tracker apps on Google Play and the App Store](https://nvminhtu.github.io/app-demo/shotmatic/research/habit-tracker-app/02-top-apps.webp "ShotMatic result, US, captured 2026-11-20")`.

## Khung một bài

- **Tiêu đề:** `<Keyword>: niche data from Google Play, the App Store and Google Trends (<tháng năm>)`.
- **The short answer** 40–60 từ: niche này đông hay thưa, người dùng ghét gì, khe hở ở đâu.
- **H2 dạng câu hỏi**, mỗi H2 đi kèm một ảnh: Is demand rising? Who already owns the top spots? What do users complain
  about? Where is the gap? How to check your own niche?
- **`evidence:`** ghi ngày chạy ShotMatic và ngày đo Trends.
- **CTA cuối:** tải ShotMatic chạy keyword của bạn (khối `PostCta` có sẵn).

## Cần Tu làm

- Duyệt danh sách 10 keyword và thứ tự đăng.
- Chụp 5 ảnh cho keyword số 1 (habit tracker app) trước 2026-11-24.
- Gửi link các tài khoản mạng xã hội của ShotMatic nếu có, để thêm vào footer.
