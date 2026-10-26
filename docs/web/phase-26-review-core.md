# Phase 26 · Review cụm tính năng chính

> Soát lại **Phase 18–27.3** như Phase 7 đã làm cho 1–6: chạy 5 niche thật qua mọi tính năng vừa làm kỹ, đối chiếu từng
> "Xong khi", sửa lỗi, cập nhật Hướng dẫn / About, ra bản Web mới.

<span class="chip chip--done">Xong 2026-10-26 · 5 niche chạy hết luồng 0 lỗi chặn · 8 phase soát · 5 mục chờ anh · bản Web 0.10.0</span>

<div class="nr-review-stop" markdown>
**⏸ REVIEW PHASE — dừng lại soát.** Đối chiếu "Xong khi" của các phase trước trên niche thật, sửa lỗi xong
mới làm tiếp phase sau.
</div>

## Làm gì

| | |
|---|---|
| :material-clipboard-check: **Phiếu soát từng phase** | mỗi phase 12–26: "Xong khi" đạt / trượt + bằng chứng (số đo, screenshot) |
| :material-account-search: **5 niche thật đi hết luồng** | Research → Explore → collect → chấm điểm → theo dõi → xuất / gói LLM → evidence pack; ghi chỗ vướng |
| :material-bug: **Sửa lỗi** | nhỏ sửa ngay; lớn ghi Master Plan §4 "Đang pending" |
| :material-book-open-variant: **Hướng dẫn + About** | cập nhật danh sách Tính năng chính / phụ (`features.ts`), trang Hướng dẫn, Cách dùng |
| :material-tag: **Ra bản** | tăng version Web, CHANGELOG, chip từng phase cập nhật |

<div class="box box--star" markdown>
**Xong khi**

- Phiếu soát điền đủ 15 phase, phase trượt có lý do + việc còn lại
- 5 niche thật chạy hết luồng không lỗi chặn
- Test xanh, screenshot luồng chính đã Read, bản Web mới có CHANGELOG
</div>

<div class="box box--danger" markdown>
**Không làm ở phase này**

- Thêm tính năng mới — chỉ soát + sửa
</div>

## Kết quả (2026-10-26)

### 5 niche thật đi hết luồng

Dev server + bản sao DB thật, gọi đúng API mà giao diện gọi: Research → đầu trang → Ai là khách → Sức khoẻ → Bị chê gì → Explore → tạo
project → Collect hàng loạt (5 loại) → Collect lại → chụp số + đọc Theo dõi → Xuất gói AI (32k) → Xuất CSV project → evidence pack → `.niche.json`.
**5/5 niche, 15 bước mỗi niche, 0 lỗi chặn.**

| Niche (loại) | Gợi ý · điểm · đo | Cờ bật | Ai là khách | Collect / gom lại | Gói AI | Đối tượng TODO |
|---|---|---|---|---|---|---|
| multi monitor menu bar (app Mac) | TEST THÊM · 5 · 55 % (hạ vì đo < 60 %) | — | 0 loại | 5 thêm / 0 trùng | ~5,9k token | 5 |
| habit tracker (iOS tiêu dùng) | TEST THÊM · 5,7 · 75 % | bão hoà 4.3 | 4 loại | 9 / 0 | ~11,4k | 3 |
| bubble shooter (Android) | TEST THÊM · 4,6 · 55 % | — | 2 loại | 9 / 0 | ~10,5k | 3 |
| budget tracker (SaaS / web) | TEST THÊM · 4,7 · 75 % | — | 4 loại | 9 / 0 | ~12,6k | 3 |
| marketing (niche xấu: rộng, đông) | TEST THÊM · 4,5 · 75 % | — (hãng lớn 2/5) | 0 loại | 9 / 0 | ~11,6k | 3 |

Thời gian: mọi bước < 350 ms, trừ **Bị chê gì lần đầu 38–53 s** (đọc review qua mạng, sau đó cache 7 ngày). Explore chỉ có sẵn cho
budget tracker — không chạy Explore mới (~6 phút mạng / niche); luồng Explore → Collect đã đo ở Phase 21 (100 keyword / 239 ms).

**Chỗ vướng ghi được**

- Niche xấu "marketing" chỉ ra TEST THÊM 4,5 (sát ngưỡng BỎ 4): top lẫn app lớn ngoài danh sách hãng (Grab, Target, PhonePe), cờ hãng lớn
  2/5 chưa tới 3. **Không chỉnh** luật cho khớp đáp án; điểm đúng là "gợi ý", lý do hiện rõ (cạnh tranh 1,9/10 · 11,3M rating top 10).
- Menu bar app Mac: Ai là khách ra 0 loại — keyword / mô tả không nhắm nhóm người nào; đúng dữ liệu.
- **Sửa ngay (lỗi nhỏ):** nút xám "Làm evidence pack" trong Bàn quyết định ghi **Phase 24** (số cũ trước khi đánh số lại) → Phase 43; tooltip
  "Phase 10" ở GitHub Gap → Phase 11; `features.ts` thiếu Phase 19 · 22 · 23 (trang chủ / Hướng dẫn / About không thấy) → thêm, sửa mô tả
  Collect + Sức khoẻ; Hướng dẫn bước 3 nói theo trang kết quả mới.

### Phiếu soát

**Phase 18 · Đối thủ bị chê gì** — đạt. 3 niche top 10 có nghĩa 10/10, cụm trùng ý → 0 (trang phase). Review 26: 5 niche ra 13–15 cụm,
82–418 review 1–2★.

**Phase 19 · Ai là khách hàng** — đạt một phần.
- ≥ 3 loại khách / niche: đạt 2/3 niche gợi ý (habit 4, budget 4); pomodoro 1, bubble shooter 2 — niche rộng.
- Kiểm tay 20 câu review / niche ≥ 16/20: **trượt mốc số lượng** — review 1–3★ chỉ có 0–3 câu tự giới thiệu / niche; 6/6 câu đúng sau sửa.
  Việc còn lại: đọc thêm review 4–5★ (bản sau).
- Bảng đọc được 1340, ô bấm ra dẫn chứng: đạt. Evidence pack mục Đối tượng 5 → 3 TODO: đạt.

**Phase 20 · Chấm sức khoẻ niche** — đạt một phần.
- Giải thích từng yếu tố từ màn hình (công thức + đầu vào + nguồn): đạt — **chờ anh thử 3 niche**.
- Back-test ≥ 5 niche đã biết kết quả: **trượt** — chỉ 2 niche (nhóm RAM) có kết quả thật. Cần anh ghi kết quả ≥ 3 niche nữa.
- Cờ chặn bật đúng ≥ 2 niche rủi ro thật: đạt (bão hoà 4.3 ở habit tracker ×2, dual monitor wallpaper).

**Phase 21 · Collect** — đạt. 6 chỗ gom, 100 keyword / 239 ms, gom lại 0 dòng trùng (Review 26: 5/5 niche 0 trùng), round-trip `.niche.json`
có test, migration chung 0 dòng mất.

**Phase 22 · Quản lý Project** — đạt. Không thêm migration; tìm keyword ra đúng project; lọc thẻ + trạng thái; gộp không nhân đôi + nhật ký;
1340 + 375.

**Phase 23 · Trang kết quả Research** — đạt một phần.
- Fixture lỗi từng nguồn → đúng lý do + chạy lại riêng: đạt. Đo thời gian hàng câu trả lời 602–649 ms: đạt. 1340 + 375: đạt
  (`design/review-26/research-habit-1340.jpg`, `…-375.jpg`).
- "Anh trả lời đáng xem tiếp không chỉ từ hàng đầu trang": **chờ anh** mở 3 niche.

**Phase 24 · Setup** — đạt một phần. Kiểm tra máy báo đúng thiếu Node · Node cũ · thiếu CLT (test) + 1 lần thật (Terminal Node 18.16);
Hỏi AI 4 AI, câu hỏi đã che. **Chờ anh**: thử trang Setup tĩnh trên Mac sạch (user macOS mới, chưa Node).

**Phase 25 · UI / UX** — đạt. 10 chỗ vướng có trạng thái; 4 sửa có số trước / sau; ảnh sau `design/ui-25/`. VoiceOver đọc thật: chưa thử.

**Phase 27 · AI của bạn (đợt 1, đã vào main)** — soát theo test có sẵn: cầu AI Claude Code / Codex (Kiểm tra trong Cài đặt) + MCP 10 tool
chỉ đọc (`mcp.test.ts`, `ai-cli.test.ts` xanh trong 395 test). 27.4 khung chat đang làm ở main, **Phase 28 chưa làm** → soát ở lần review sau.

### Việc chờ anh (không tự làm được)

1. Mở 3 niche: đọc từng yếu tố Sức khoẻ có hiểu không (Phase 20) + trả lời "đáng xem tiếp?" chỉ từ đầu trang (Phase 23).
2. Ghi kết quả thật (bán được / không / bị từ chối) cho ≥ 3 niche → chạy lại back-test Phase 20.
3. Thử trang Setup máy trên Mac sạch (Phase 24).
4. VoiceOver đọc trang Research + Project (Phase 25).
5. Merge nhánh `phase19-26` vào main.

### Ra bản

Web **0.9.0 → 0.10.0** (`web/package.json`, `version.ts`, `tauri.conf.json` — test `version.test.ts`), CHANGELOG mục `[0.10.0]`.
Không build lại `.dmg` (chỉ build bằng `npm run mac` khi ra bản app).

Plan code chi tiết: [Phase 26](../superpowers/plans/2026-10-25-niche-radar-phase27-review-core.md)
