# 34 · Đào review: gom theo nghĩa + chấm nỗi đau đúng hơn

> Plan 2 · mục 34. Nâng [mục 27 Review Mining](phase-plan2-27-review-mining.md): **gom review theo nghĩa** bằng model chạy
> trên máy, nên "Too many ads" và "Ads keep interrupting me" vào chung một nhóm. Mỗi nhóm có tên đọc được, có đủ 9 thông tin,
> và điểm nỗi đau /100 không bị lệch khi nhóm nhỏ hay app quá to. Không cần AI trả phí.

<span class="chip chip--todo">Spec 2026-11-18 · spike xong 2026-11-18 · chốt MiniLM-L12 nhiều tiếng · chưa code</span>

<div class="box box--danger" markdown>
**Ngoài quyết định 2026-11-07:** ShotMatic đang dừng thêm tính năng để dồn sức cho [Marketing](../marketing/index.md).
Mục 27 còn phần chưa commit (27.6). Nên commit 27 trước rồi mới code mục này.
</div>

## Vì sao làm

Ngày 2026-11-18 anh dán đề xuất "Module 03 Pain Point Clustering + Module 04 Pain Point Intelligence". Đối chiếu với
mục 27 đã code:

| Đề xuất | Mục 27 đang có | Còn thiếu |
|---|---|---|
| Gom theo nghĩa, không theo keyword | Gom theo cụm 1–3 chữ sau khi gộp đồng nghĩa (`complaints.ts`) | **Thiếu hẳn.** Câu khác chữ cùng ý bị tách ra nhiều nhóm |
| Tên nhóm dễ hiểu | Tên là cụm chữ thô, vd. "lost" | Tên đọc được, vd. "Mất dữ liệu sau khi cập nhật" |
| Số review · % review chê · sao TB · mức nặng · câu trích · version | Có | Câu trích nên là câu **đại diện**, không phải 3 câu đầu |
| Xu hướng theo thời gian | Chỉ 1 con số (30 ngày gần nhất so với trước) | Đường nhỏ theo tuần |
| Đối thủ liên quan | Có danh sách app trong nhóm | Ghi rõ app nào bị nặng nhất |
| Nhận ngôn ngữ | Chỉ đọc `lang=en` | Đọc review tiếng địa phương ở 17 nước |
| Bỏ trùng | Bỏ trùng đúng chữ (hash) | Bỏ trùng **gần giống** (copy, spam) |
| Gộp / tách nhóm | Gộp + đổi tên bằng tay. ✦ AI chỉ gợi ý gộp trong khung chat | Gợi ý gộp bằng số, **tách** nhóm, bấm áp gợi ý |
| Điểm nỗi đau 30·30·20·20 | Có, phần chưa đo bỏ khỏi mẫu số | Tần suất chưa trừ hao cỡ mẫu và chưa cân app to / app nhỏ |

Kết luận: phần chấm điểm (Module 04) **đã có khoảng 80%**. Chỗ hổng thật là Module 03: gom theo nghĩa.

## Học từ tool top + repo top (tra 2026-11-18)

Các số độ đúng dưới đây là hãng tự công bố, chưa ai kiểm độc lập.

- **[Appbot](https://appbot.co/blog/appbot-vs-appfollow/):** mỗi review gắn chủ đề, keyword, cụm chữ, cảm xúc, có
  "Custom Topics" theo từ ngữ riêng của app. Hãng tự ghi độ đúng 93%+.
  → Học: bộ chủ đề có sẵn + cho người dùng thêm chủ đề riêng.
- **[AppFollow](https://appfollow.io/compare-appfollow-vs-appbot):** bộ phân loại có sẵn hơn 30 loại, thêm được tag AI riêng,
  có tóm tắt review bằng AI.
  → Học: 9 loại chê của mình là khung, cụm theo nghĩa nằm bên dưới.
- **[Thematic](https://www.getthematic.com/product/tag-and-theme):** gom từ dưới lên (bottom-up). Mọi theme lần ngược về
  được câu gốc. Có Theme Editor để gộp, tách, đổi tên. Khi chạy lại trên dữ liệu mới, theme mới được **thêm vào** cây cũ,
  không xoá phần anh đã sửa.
  → Học: sửa tay phải sống sót qua lần đọc lại.
- **[Enterpret](https://www.enterpret.com/guides/the-5-steps-to-split-a-feedback-theme-that-has-grown-too-broad):** đổi tên khi
  một nhóm là 1 vấn đề nói nhiều cách. Tách khi nhóm chứa nhiều vấn đề. **Không tách chỉ vì nhóm to.** Trước khi gộp, hỏi
  2 nhóm có cùng nguyên nhân không ([hướng dẫn gộp](https://www.enterpret.com/guides/the-5-questions-to-ask-before-you-merge-two-feedback-themes)).
  → Học: gợi ý tách chỉ hiện khi trong nhóm có ≥ 2 cụm con rõ ràng.
- **[BERTopic](https://github.com/maartengr/bertopic)** (repo Python phổ biến nhất cho topic modeling): embedding → giảm chiều
  (UMAP) → gom (HDBSCAN) → đặt tên bằng c-TF-IDF (gộp cả nhóm thành 1 văn bản rồi lấy chữ đặc trưng). HDBSCAN để nhiều câu
  ở ngoài nhóm. Một bài trên review app có khoảng một nửa review ra ngoài nhóm, nên có bước gán lại.
  → Học: cách đặt tên c-TF-IDF và bước gán lại câu lẻ. Không chép UMAP + HDBSCAN (lý do ở 34.3).
- **[FeClustRE](https://arxiv.org/html/2510.18799v1)** (bài 2025, code mở): gom phân cấp (hierarchical) tính năng trong review app,
  tự chỉnh ngưỡng, rồi LLM gắn nhãn.
  → Học: gom phân cấp hợp với số review của 1 app, và cho tách / gộp dễ vì đã có sẵn cây.
- **Actor "pain miner" trên [Apify](https://apify.com/george.the.developer/app-review-pain-miner):** chạy phần tính toán cố định
  trước, LLM chỉ viết báo cáo nếu có key.
  → Đúng hướng của ShotMatic: code đếm số, AI chỉ đặt tên / viết lời.
- **[Transformers.js](https://huggingface.co/Xenova/all-MiniLM-L6-v2/tree/main/onnx):** chạy model embedding trong Node.
  `all-MiniLM-L6-v2` bản int8 nặng 23 MB, 384 chiều, nhưng chủ yếu tiếng Anh. Bản nhiều tiếng như
  [`multilingual-e5-small`](https://huggingface.co/Xenova/multilingual-e5-small) có 118M tham số. Cỡ file int8 **chưa đo**.
- **Nhận ngôn ngữ:** [`eld`](https://www.npmjs.com/package/eld) là JS thuần, không phụ thuộc. `franc` được đánh giá yếu với câu ngắn.
  Chưa có số so sánh trên review thật, nên phải tự đo (34.1).

## Không làm (và vì sao)

- **UMAP + HDBSCAN.** JS không có thư viện tốt. Một lượt đào thường ra vài trăm tới khoảng 5.000 câu chê, nên gom phân cấp
  trên cosine chạy thẳng được (5.000 câu ≈ 12,5 triệu cặp, phải đo thời gian ở 34.3).
- **Gọi API embedding trả phí** (OpenAI, Voyage…). Trái ý "không phụ thuộc AI trả phí".
- **Theo dõi theo lịch, báo động.** Giữ như mục 27: chỉ so với lần đọc trước khi anh bấm đọc lại.
- **Cảm xúc nhiều mức** (giận, buồn…). Sao + mức nặng đã đủ để chấm điểm.

## 34.0 · Thử trước (spike): đã làm 2026-11-18

App Mac gói server bằng esbuild và chạy Node đi kèm (`app/scripts/build-mac.sh`). Spike chạy trong thư mục nháp, **chưa thêm
thư viện nào vào repo**. Máy: Mac arm64, Node 22.19, `@huggingface/transformers` 3.x, `onnxruntime-node` 1.21, model bản int8 (`q8`).

**Đo 2 model** trên 1.803 câu chê thật (1.500 review 1–3★ trong `review_seen`, nhiều app):

| Đo | `multilingual-e5-small` | `paraphrase-multilingual-MiniLM-L12-v2` |
|---|---|---|
| Model trên đĩa | 129 MB | 145 MB |
| Nạp model (đã có trên máy) | — | 0,5 giây |
| Embed 1.000 câu | 4,0 giây | 3,7 giây |
| RAM cả tiến trình | 951 MB | 974 MB |
| 4 câu "ads" của bản đề xuất, giống nhau | 0,85 – 0,90 | 0,45 – 0,64 |
| "Too many ads" ↔ cùng ý tiếng Nhật / tiếng Việt | 0,87 / 0,90 | 0,95 / 0,95 |
| "Too many ads" ↔ câu khác ý (crash, mất ghi chú) | 0,82 / 0,82 | 0,15 / 0,14 |

**Chốt model: `paraphrase-multilingual-MiniLM-L12-v2`.** Cả 2 đều dưới ngưỡng anh đặt (150 MB, 30 giây cho 1.000 câu). Nhưng e5-small
cho mọi cặp câu gần như cùng điểm (0,82–0,90), nên không tách được câu cùng ý với câu khác ý. MiniLM tách rõ, và câu cùng ý khác
tiếng ra 0,95.

**Đường chạy:**
- Bản Node của Transformers.js **chỉ có đường native** (`cpu` qua `onnxruntime-node`). Đường WASM báo lỗi `Unsupported device`, nên bỏ.
- **Gói thử kiểu app Mac chạy được.** Gói bằng esbuild `--format=cjs`, để `onnxruntime-node` ở ngoài (external) giống `better-sqlite3`,
  và chỉ chép bản Mac arm64.
  - App nặng thêm khoảng **33 MB**: 31 MB `onnxruntime-node` arm64 (`onnxruntime_binding.node` + `libonnxruntime.1.21.0.dylib`),
    1,1 MB `onnxruntime-common`, server.cjs thêm khoảng 1,5 MB.
  - Bản gói đọc model đã tải sẵn, nạp xong và embed 3 câu trong 0,55 giây.
- **Chưa thử:** ký + notarize với file `.dylib` mới (`npm run mac`), và bản Windows (cần file `win32-x64`).
- **Model không nhét vào `.dmg`.** Lần đầu bấm "Gom theo nghĩa" thì tải về thư mục dữ liệu (`NR_DATA_DIR`), có thanh tiến độ
  và nút Huỷ. Không có mạng hoặc tải hỏng thì dùng lại cách gom chữ của mục 27, và ghi rõ đang dùng cách nào.

**Nhận ngôn ngữ (`eld`, bộ dữ liệu `medium`, 1,9 MB):** chạy trên 80 review chê thật mỗi nước (Evernote, Play):

| Nước | Đúng tiếng | Ra tiếng Anh | Khác |
|---|---|---|---|
| JP (`ja`) | 80 / 80 | 0 | 0 |
| VN (`vi`) | 69 / 80 | 10 | 1 |
| BR (`pt`) | 73 / 80 | 6 | 1 |
| DE (`de`) | 73 / 80 | 7 | 0 |

Phần "ra tiếng Anh" phần lớn có thể là review viết bằng tiếng Anh ở store nước đó (chưa đọc từng câu để chắc).

**Đọc tiếng địa phương đáng làm:** Evernote, 150 review mới nhất mỗi lượt.
- Đọc bằng `lang=en` thì Play trả **đúng cùng 121 review chê** cho cả JP, VN, BR, DE.
- Đọc bằng tiếng nước đó thì ra 137 / 103 / 111 / 131 review chê **khác hẳn nhau**.
- Nghĩa là trước giờ chọn nhiều nước mà vẫn đọc `en` thì gần như chỉ đọc lại 1 bộ review.

**Gom thử** (liên kết trung bình, 1.165 câu: Habitica tiếng Anh + Evernote JP + VN):

| Ngưỡng | Nhóm ≥ 3 câu | Câu ngoài nhóm | Thời gian gom |
|---|---|---|---|
| 0,55 | 116 | 49% | 2,6 giây |
| 0,50 | 135 | 34% | 2,7 giây |

- **Đúng:** review chê quảng cáo tiếng Nhật và tiếng Việt vào **chung 1 nhóm** (25 câu). Các câu "muốn dùng offline" vào 1 nhóm.
- **Lộ 4 lỗi phải sửa trong code:**
  1. Câu trùng y hệt lặp lại do Habitica được đọc ở nhiều nước. Phải bỏ trùng trước khi gom (34.3 bước 1).
  2. **Câu khen nằm trong review 1–3★** ("Great app", "fantastic app") thành nhóm to nhất. Phải lọc câu khen trước (34.3 bước 0).
  3. Câu quá chung ("làm gì đi chứ") gom thành nhóm vô nghĩa. Bỏ câu không có danh từ / quá ngắn sau khi chuẩn hoá.
  4. Cách gom thử đơn giản chạy O(n³). Với 1.165 câu mất 2,6 giây, ước chừng 5.000 câu sẽ mất vài phút. Code thật dùng
     NN-chain (O(n²)) hoặc chặn số câu.

## 34.1 · Tách câu, chuẩn hoá, nhận ngôn ngữ

- **Đơn vị gom là câu, không phải cả review.** "Slow and too expensive" phải vào cả nhóm Lỗi lẫn nhóm Giá (đã có luật ở 27.4).
  Một review vẫn chỉ đếm 1 lần trong mỗi nhóm.
- **Chuẩn hoá:** bỏ emoji lặp, kéo dài chữ ("sooooo" → "so"), bỏ câu dưới 3 chữ, giữ nguyên chữ gốc để trích.
- **Nhận ngôn ngữ** bằng `eld` cho từng review. Ghi vào cột mới `lang` của `review_seen`.
- **Đọc review tiếng địa phương:** store đọc theo `lang` của nước (JP → `ja`, VN → `vi`…) thay vì luôn `en`. Model nhiều tiếng
  đặt câu khác tiếng vào chung không gian, nên review Nhật và Anh cùng ý sẽ vào cùng nhóm. 9 loại chê theo luật vẫn chỉ
  hiểu tiếng Anh. Câu không phải tiếng Anh lấy loại chê theo **nhóm nghĩa** nó rơi vào (đa số câu trong nhóm thuộc loại nào).
- **Tiếng theo nước** (anh chốt làm luôn 2026-11-18):

  | Nước | Tiếng đọc |
  |---|---|
  | US · GB · CA · AU · IN · PH | `en` |
  | DE · FR · ES · IT | `de` · `fr` · `es` · `it` |
  | BR · MX | `pt` · `es` |
  | JP · KR · VN · TH · ID | `ja` · `ko` · `vi` · `th` · `id` |

  Play đọc bằng `lang` của bảng trên. App Store trả review theo storefront của nước, vốn đã là tiếng địa phương, nên chỉ cần
  ghi `lang` nhận được bằng `eld`. Ô chọn nước có thêm 1 nút **"Chỉ đọc tiếng Anh"** cho ai muốn như cũ.
- **Phần chấm điểm với câu không phải tiếng Anh:** chữ "bỏ app" ở 34.7 (refund, uninstall…) chỉ có tiếng Anh. Câu tiếng khác
  không cộng phần này, chỉ dùng sao + loại chê của nhóm. Ghi rõ "chưa đo chữ bỏ app với tiếng x" trong ⓘ, không dịch đoán.
- **Câu trích + tên nhóm:** giữ chữ gốc. Tên nhóm bằng c-TF-IDF lấy theo tiếng chiếm nhiều nhất trong nhóm. ✦ AI đặt tên lại
  (tuỳ chọn) thì đặt theo ngôn ngữ giao diện, kèm bản dịch câu trích có nhãn **AI dịch**.
- **Bỏ trùng giữa các nước** (mục 27) vẫn giữ: Play có thể trả cùng review ở nhiều nước cùng tiếng (vd. US và GB), đếm 1 lần.
- **Kiểm ở 34.9:** lượt chạy thật thêm 1 app ở JP hoặc VN, đếm số review đọc được bằng `en` so với tiếng địa phương.

## 34.2 · Embedding trên máy

- Model chốt ở 34.0: `Xenova/paraphrase-multilingual-MiniLM-L12-v2`, bản int8, 145 MB, 384 chiều.
- Lưu vector vào bảng mới `review_vectors` (khoá: hash câu + tên model). Đọc lại hay thêm app thì chỉ embed câu mới.
  Đổi model thì embed lại từ đầu.
- Chạy trong worker riêng để server không đứng. Có tiến độ "đã xử lý x / y câu".

## 34.3 · Gom theo nghĩa

0. **Lọc câu khen:** trong review 1–3★ vẫn có câu khen ("Great app, but…"). Câu có cosine với tâm của bộ câu khen mẫu
   cao hơn tâm câu chê mẫu thì bỏ khỏi phần gom chê (bộ mẫu khoảng 20 câu mỗi bên, nhiều tiếng, đặt trong code).
1. **Bỏ trùng gần giống:** 2 câu cùng app có cosine ≥ 0,95 thì coi là trùng (copy, spam, review dán lại). Mỗi người vẫn đếm 1.
2. **Gom phân cấp** (agglomerative, liên kết trung bình, cosine), cắt cây ở ngưỡng mặc định **0,5** (spike: 0,5 → 34% câu ngoài nhóm, 0,55 → 49%; chỉnh ở 34.10).
3. **Có dẫn hướng:** 9 loại chê của mục 27 làm "hạt mầm". Một nhóm có ≥ 60% câu thuộc 1 loại thì gắn loại đó, để thanh loại chê
   và mức nặng vẫn dùng được.
4. **Câu lẻ:** câu không vào nhóm ≥ 3 người thì gán vào nhóm có tâm gần nhất nếu cosine ≥ 0,45. Còn lại đưa vào "Khác".
   Số câu ở "Khác" hiện ra, không giấu.
5. **Sửa tay sống sót qua lần đọc lại:** nhóm anh đã gộp, đổi tên hay tách được giữ theo **tâm nhóm** (vector trung bình).
   Lần đọc sau, câu mới gần tâm nào thì vào nhóm đó. Nhóm mới chỉ được thêm, không xoá nhóm cũ (học Thematic).

## 34.4 · Tên nhóm + câu đại diện

- **Tên bằng code (không AI):** c-TF-IDF lấy 2–3 cụm chữ đặc trưng nhất của nhóm so với các nhóm khác. Tên = cụm chữ gần tâm
  nhất, viết hoa đầu câu, vd. "Too many ads". Thay cho cụm thô "lost" hiện nay.
- **✦ AI đặt tên lại** (tuỳ chọn, AI trên máy): gửi 5 câu đại diện, nhận tên ngắn 3–6 chữ theo ngôn ngữ giao diện. Gắn nhãn
  **AI suy luận**. AI không đổi số.
- **Câu đại diện:** 3 câu gần tâm nhất, lấy từ các app khác nhau nếu có, dài 8–40 chữ. Có link về store.

## 34.5 · Thẻ nhóm đủ 9 thông tin

Thẻ trong tab Nỗi đau xếp **1 cột**. Số ngắn nằm ngang thành chip, phần chữ xếp dọc:

1. Tên nhóm (+ nhãn Tính ra / AI suy luận).
2. Số người (review khác nhau).
3. % trên review chê.
4. Sao trung bình.
5. Mức nặng (Nhẹ / Vừa / Nặng / Rất nặng).
6. Xu hướng: đường nhỏ theo **tuần** trong 12 tuần gần nhất. Dưới 20 review có ngày thì ghi "chưa đo".
7. 3 câu đại diện.
8. Version bị nhiều nhất: version đỉnh + "bắt đầu từ version x" nếu nhóm gần như không có trước đó.
9. Đối thủ liên quan: app nào trong bộ đang so cũng bị, kèm % từng app, app bị nặng nhất đứng đầu.

Chữ giải thích dài gập vào ⓘ (giao diện bớt chữ, giống trang YouTube Soi kênh).

## 34.6 · Gộp + tách

- **Gợi ý gộp bằng số:** 2 nhóm có tâm cosine ≥ 0,85 thì hiện "Có vẻ cùng 1 vấn đề", kèm 2 câu đại diện mỗi bên. Bấm **Gộp** là gộp.
- **Gợi ý tách:** chạy gom lại bên trong 1 nhóm với ngưỡng chặt hơn. Chỉ hiện nút **Tách** khi ra ≥ 2 nhóm con, mỗi nhóm ≥ 3 người
  (luật Enterpret: không tách chỉ vì to). Anh xem nhóm con rồi bấm chọn.
- **✦ AI gợi ý gộp** (đã có ở 27.4) trả về lệnh có cấu trúc. Thêm nút **Áp gợi ý**. Code kiểm từng lệnh: chỉ gộp các nhóm đang có.
- Tất cả lưu vào `review_group_edits` như cũ, thêm kiểu `split`. Nút "Về như cũ" vẫn còn.

## 34.7 · Điểm nỗi đau /100 chuẩn hơn

Giữ công thức của bản đề xuất và mục 27: **PPS = 30·F + 30·S + 20·T + 20·U**, mỗi phần từ 0 tới 1. Phần chưa đo thì bỏ khỏi
mẫu số. Sửa cách đo từng phần:

| Phần | Mục 27 đang đo | Mục 33 đổi |
|---|---|---|
| F · Tần suất | Số review của nhóm ÷ review chê. Đạt 25% thì đủ điểm | **Cận dưới Wilson** (độ tin 90%) của tỉ lệ đó, nên 3/10 không thắng 60/400. Nhiều app: tính tỉ lệ **từng app** rồi lấy trung bình, để app có 1.000 review không lấn app có 100 |
| S · Mức nặng | `severity` của loại chê + cộng nếu sao TB ≤ 1,5 | Thêm chữ "bỏ app": refund, uninstall, cancel, switched to, lost all… (đếm có, không đoán) |
| T · Xu hướng | 30 ngày gần nhất so với phần còn lại | Giữ. Nhưng chỉ tính khi cả 2 khoảng đều có ≥ 10 review có ngày. Thêm chiều: nhóm mới xuất hiện sau 1 version |
| U · Chưa ai giải | Số app cùng bị ÷ số app (cần ≥ 2 app) | Trừ bớt khi developer đã trả lời "fixed in x.y" và nhóm giảm hẳn sau version đó |

- Bản đề xuất nhắc chuẩn hoá theo **số người dùng**. Store không cho số người dùng thật. Lượt tải Play là khoảng (vd. 1M+),
  nên **không** dùng để chia. Chỉ dùng số review đã đọc của từng app (đã cân ở F).
- Trọng số vẫn là **quy ước ShotMatic**, chưa kiểm bằng app thật. ⓘ ghi công thức + nguồn. Đổi luật thì đổi `MINE_RULES`.

## 34.8 · Xuất cho Claude Code / AI của anh

- File xuất (.md / .json) thêm: tên nhóm, 9 thông tin ở 34.5, điểm từng phần, câu đại diện, tên model đã dùng.
  **Không** xuất vector.
- Tool MCP `get_review_clusters` (chỉ đọc) để Claude Code đọc thẳng nhóm của 1 lượt đào.

## 34.9 · Kiểm độ đúng

- Bộ test cặp câu: 4 câu "ads" trong bản đề xuất phải vào cùng 1 nhóm. Thêm khoảng 10 bộ như vậy (crash, sync, giá…),
  và các cặp **không** được gộp (vd. "search slow on mobile" với "search slow on web" của Enterpret là quyết định của anh, ghi lại).
- File 60 review gán nhãn tay của 27.8 (chưa làm): làm luôn ở đây. Đo **độ thuần** của nhóm (% câu trong nhóm cùng nhãn) ≥ 80%.
- Chạy thật 3 lượt: Habitica Play Đọc sâu · 1 app iOS · 1 app ở JP hoặc VN (tiếng địa phương). So số nhóm, % ở "Khác",
  thời gian, với cách gom chữ của mục 27. Ghi bảng số vào trang này.

## 34.10 · Chỉnh ngưỡng

Ngưỡng 0,5 / 0,45 / 0,85 / 0,95 ở trên là **điểm bắt đầu**. Chỉ 0,5 có số từ spike 34.0, còn lại chưa đo. Sau 34.9, chọn ngưỡng cho % ở "Khác" dưới 25% mà độ thuần
vẫn ≥ 80%. Không cho người dùng tự kéo ngưỡng ở bản đầu, chỉ có nút "Gom chặt hơn / lỏng hơn" (3 nấc).

## Chia việc

1. ~~34.0 spike~~ (xong 2026-11-18). Còn lại của phần này: ký + notarize với `.dylib`, bản Windows.
2. DB: cột `lang` cho `review_seen`, bảng `review_vectors`, thêm kiểu `split` cho `review_group_edits`.
3. `web/src/lib/review-text.ts` (hàm thuần): tách câu, chuẩn hoá, nhận ngôn ngữ. Test kèm.
4. `web/src/lib/review-embed.ts`: tải model, worker, cache vector.
5. `web/src/lib/review-cluster.ts` (hàm thuần, nhận vector): bỏ trùng gần giống, gom phân cấp, gán câu lẻ, c-TF-IDF, câu đại diện,
   gợi ý gộp / tách, giữ sửa tay theo tâm. Test kèm (vector giả, không cần model).
6. `review-mining.ts`: điểm 34.7, thêm 9 thông tin của thẻ. Test kèm.
7. Collector đọc theo `lang` của nước (34.1).
8. Giao diện `ReviewMining.tsx`: nút Gom theo nghĩa + tiến độ tải model, thẻ nhóm mới, gộp / tách, chữ 3 ngôn ngữ.
9. Xuất + MCP `get_review_clusters`.
10. 34.9 + 34.10, `npm run check` xanh, xem 960px + 1340px, sáng + tối.

## Anh chốt

1. **Model: nhiều tiếng** (anh chốt 2026-11-18). Ứng viên đầu là `multilingual-e5-small` bản int8, sau đó tới
   `paraphrase-multilingual-MiniLM-L12-v2`. Spike 34.0 đo cỡ file, thời gian nạp model và thời gian embed 1.000 câu rồi chọn 1.
   Nếu cả 2 đều quá 150 MB hoặc embed 1.000 câu quá 30 giây thì báo lại anh, không tự lùi về model tiếng Anh.

2. **Đọc review tiếng địa phương: làm luôn đợt này** (anh chốt 2026-11-18). Cách làm ở 34.1.

3. **Thứ tự: commit mục 27 rồi spike ngay** (anh chốt 2026-11-18). Mục 27.6 đã commit (`5e0c362`), spike 34.0 xong cùng ngày.
