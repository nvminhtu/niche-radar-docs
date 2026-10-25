# Quy trình build

> Mỗi phase đi đúng **6 bước, theo thứ tự này**. Không nhảy bước, không code khi chưa có plan.

<div class="box box--goal" markdown>
<p style="font-size:1.25em;font-weight:700;margin:0 0 .4em">📄 Spec ➜ 🗺️ Plan + 🎨 Mockup ➜ 🔨 Implement ⇄ 🔁 Update plan ➜ 📦 Build ➜ ✅ Test ➜ 🚀 Xong</p>

**⇄** = làm task → cập nhật plan → làm task tiếp, lặp tới hết task · ✅ trượt "Xong khi" → quay lại 🔨
</div>

```mermaid
flowchart TB
  S["📄 1 · Spec<br/>mục tiêu · làm · không làm · xong khi"] ==> P["🗺️ 2 · Plan + 🎨 Mockup<br/>chia task · vẽ màn mới"]
  P ==> I["🔨 3 · Implement<br/>1 task · test xanh · commit"]
  I ==> U["🔁 4 · Update plan<br/>tick task · ghi lệch"]
  U -. còn task / lệch plan .-> I
  U ==>|hết task| B["📦 5 · Build<br/>npm run build · npm start"]
  B ==> T["✅ 6 · Test<br/>3 niche thật · screenshot"]
  T -. trượt .-> I
  T ==>|đạt| D(["🚀 Xong · merge main"])
```

## 6 bước

<div class="steps" markdown>
<div class="step" markdown>
<span class="step__n">1</span>

### 📄 Spec — chốt làm gì

- **Làm:** viết phase vào [Master Plan](superpowers/specs/2026-10-24-niche-radar-master-plan.md) §3: **mục tiêu ·
  làm gì · không làm gì · xong khi** (đo được). Trang tóm tắt `phase-N-*.md` cho site.
- **Ra file:** master plan §3 Phase N + `docs/web/phase-N-*.md` (phase gói / build app Mac: `docs/app/`).
- **Qua bước khi:** anh chốt phạm vi. Việc ngoài phạm vi → master plan §4 "Đang pending".
</div>

<div class="step" markdown>
<span class="step__n">2</span>

### 🗺️ Plan + 🎨 Mockup — chia task, vẽ màn mới

- **Plan code:** `docs/superpowers/plans/YYYY-MM-DD-niche-radar-phaseN-<tên>.md` — Global Constraints, Tasks dạng
  checkbox, mỗi Task nêu file đụng tới + test cần viết. Khung theo plan Phase 1.
- **Mockup:** chỉ cho màn mới / khối mới. Claude viết prompt vào `design/mockups/phaseN/image-prompts.md`, **Codex sinh
  ảnh** (`codex exec`) vào `design/mockups/phaseN/`, Claude mở từng ảnh ra soát. Không tự vẽ bằng SVG/HTML.
- **Qua bước khi:** anh xem plan + mockup, đồng ý.
</div>

<div class="step" markdown>
<span class="step__n">3</span>

### 🔨 Implement — làm từng task

- Nhánh `phaseN-<tên>` cắt từ `main`.
- Mỗi Task: viết test → code → `npm run check` (gốc repo; = test + typecheck + lint trong `web/`) **xanh** → commit.
- UI bám mockup bước 2.
</div>

<div class="step" markdown>
<span class="step__n">4</span>

### 🔁 Update plan & Implement — giữ plan đúng với code

- Xong Task → tick checkbox, ghi 1–2 dòng vào mục **Tiến độ** của plan.
- Gặp lệch (bug thật, endpoint chết, đổi cách làm) → **sửa plan trước, code sau**. Ghi rõ "thêm ngoài plan: vì sao".
- Việc mới ngoài phạm vi → master plan §4, **không làm lén**.
- Còn task → quay lại 🔨. Hết task → 📦.
</div>

<div class="step" markdown>
<span class="step__n">5</span>

### 📦 Build — chạy bản build, không phải bản dev

- Trong `web/`: `npm run build` → `npm start` (một process, cổng 3200) — mở được, không lỗi console.
- `npm run docs:build` (strict) — site tài liệu không gãy link.
</div>

<div class="step" markdown>
<span class="step__n">6</span>

### ✅ Test — đo thật, nhìn tận mắt

- Trong `web/`: `npm test` + `npm run smoke -- "<niche>" US` (gọi thật các nguồn).
- Chạy thật **3 niche**, ghi số đo (số keyword, thời gian, lỗi, ngày) vào mục **Kết quả chạy thật** của plan.
- Screenshot 1280 + 375 của mọi màn đổi → **mở ra xem**, so với mockup.
- Đối chiếu từng dòng **Xong khi** ở bước 1. Trượt dòng nào → quay lại 🔨.
- **Đạt** → cập nhật chip trạng thái (master plan §3 + `phase-N-*.md`) → merge `main` khi anh đồng ý.
</div>
</div>

## Luật

<div class="box box--rules" markdown>
- **Không plan, không code.** Chưa có file plan bước 2 thì chưa mở nhánh.
- **Build xanh ≠ xong.** Xong = đạt hết "Xong khi" + screenshot đã xem.
- **Plan luôn khớp code.** Đọc plan là biết code đang ở đâu.
- **Số đo có ngày + nguồn.** Không đo được ghi `chưa đo`.
- **Merge `main` cần anh đồng ý.**
- **UI chưa có tính năng thì disable, không xoá.** Nút / ô / mục thuộc phase chưa làm vẫn hiện nhưng xám, không bấm được,
  ghi `Phase N` + tooltip "chưa làm" (class `soon-chip`, danh sách ở `web/src/lib/features.ts`). Làm xong phase thì bật lên.
</div>

## Đang ở bước nào

Cập nhật 2026-10-24 theo nhánh `main` (mọi nhánh `phase1` → `phase7` đã merge vào `main`).

- **1 · Google Play** — ✅ **Xong** — có UI Loading + Flow niche (`871589c`)
- **2 · App Store** — ✅ **Xong** — cột Tiền + Store, câu than 2 store (`59f3d13`)
- **3 · Google Trends** — ✅ **Xong** — Top 10, so 5 keyword, mùa vụ (`206ff34`, `8622164`)
- **4 · Feature Gap Matrix** — ✅ **Xong** — tuyến B (job Claude) chạy thật 3 niche (`d47aea5`)  
  → Tiếp: tuyến A chờ anh tạo key Claude API
- **5 · Verified Sites** — ⏸️ **Tạm dừng** — trang TrustMRR cấm quét, tìm theo từ khoá cần key (`fee7191`)  
  → Tiếp: dời sang tuyến Claude in Chrome ở Phase 6
- **6 · Tích hợp AI (Web)** — ✅ **6 · Test** xong — Cài đặt AI, chủ đề than có trích dẫn, tóm tắt niche (`4ac7098`)  
  → Tiếp: tuyến A chờ key
- **7 · Review + Validate** — 🟡 **Code xong** — sức khoẻ niche v2, evidence pack, test bán trước (`55bf8c0`)  
  → Tiếp: anh chạy vòng test bán trước + nhập số thật
- **8 · Local App** — 📄 **1 · Spec** đã duyệt · phần Project làm sớm: Collect niche + trang Projects (`e8a921d`)  
  → Tiếp: plan code app Mac (Tauri) sau Phase 7
- **9 · Small Features** — 📄 Spec trong Master Plan  
  → Tiếp: chốt danh sách ưu tiên
- **11 · UI / UX** — 📄 Spec · đã làm lẻ: bảng Lịch sử + phân trang, chip nguồn +N (`b2cf354`), trang Hướng dẫn (`3258c0d`)
- **12 · Account** — 📄 Spec trong Master Plan  
  → Tiếp: xét lại khi có người dùng ngoài
- **12.1 · Setup trong Web** — 📄 Plan: [trang Setup + Kiểm tra máy + Hỏi AI](web/phase-12-1-setup.md)
- **12.2 · Tutorial (nút ?)** — 📄 Plan: [nút ? mỗi tính năng, hình bước ít chữ](web/phase-12-2-tutorial.md)
- **13–55 · Version 2–11** — 📄 Plan trong docs, chưa code
- **Version 12** — 📄 Danh sách ứng viên
