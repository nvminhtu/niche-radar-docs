---
name: app-plan
description: "Variant của core:mvp-plan cho app — sau khi spec.md đã duyệt (Approved: yes) và trước/đang app-build: chia các lát cắt trong `## MVP` của apps/ACTIVE/<slug>/context-ai/spec.md thành plan/active/plan-mvp.md 4 phase (màn hình tĩnh · data/logic · nối UI + logic · visual design + assets), 'Xong khi' bằng lệnh test/chạy của repo, rồi giữ Step trong state.md. Dùng khi nói 'plan MVP app', 'chia phase build app', 'app đang ở phase nào', 'app-plan <slug>'. Không viết code."
argument-hint: "[slug]"
user-invocable: true
model: claude-sonnet-5-5
---

# app-plan — plan MVP của 1 app (variant `core:mvp-plan`)

Làm đúng quy trình và luật của skill **`core:mvp-plan`** (đọc SKILL.md của nó trước). File này chỉ nói phần riêng của app.

## Phần riêng của app

- **Thư mục sản phẩm:** `apps/<ACTIVE|BACKLOG>/<loại>/<slug>/` — tìm bằng `scripts/app_paths.py` (`app_dir`).
- **File plan:** `plan/active/plan-mvp.md` — file plan đầu tiên và duy nhất của MVP, chỉ sửa file này (khung
  `reference/README-APP-LAYOUT-01-APP-FOLDER.md`). Tạo bằng `python3 scripts/app.py change <slug> --type feature --title "MVP"`
  rồi viết 4 phase vào. Không tạo `plan/mvp/` (khuôn cũ của `core:mvp-plan`); MVP xong → `app.py plan-close <slug> --tag xong`.
- **PRD:** `apps/ACTIVE/<slug>/context-ai/spec.md`. Duyệt = có dòng `Approved: yes`. Chưa duyệt → dừng, bước kế `/app-spec <slug>`.
  Nguồn việc = mọi dòng `- [ ]` trong mục `## MVP` (mỗi dòng là một lát cắt màn hình + logic + dữ liệu + test).
  Đọc thêm `design.md` (token/màn) cho P1 và P4.
- **Map lát cắt vào phase** (một lát cắt có thể tách thành việc ở nhiều phase — mỗi việc ghi lát cắt gốc):

  | Phase | Việc từ lát cắt |
  |---|---|
  | P1 màn hình tĩnh | các màn + điều hướng với dữ liệu giả, đúng bảng màn hình trong spec, **bám ảnh `design/mockup/`** (bước 4b) |
  | P2 data / logic | model, lưu trữ, logic nghiệp vụ + unit test; StoreKit/billing ở chế độ test |
  | P3 nối UI + logic | từng lát cắt chạy thật end-to-end; lát cắt Paywall; quyền (permission) xin đúng lúc |
  | P4 visual design + assets | token màu/khoảng cách từ `design.md`, icon, ảnh (`core:asset-prompt`), dark mode |

- **"Xong khi" dùng lệnh của repo:** `python3 scripts/test_app.py <slug>` (Flutter) hoặc `cd apps/ACTIVE/<slug>/source/mac && make
  test` (macOS) → 0 failed; `python3 scripts/run_app.py <slug>` + ảnh `run/out/screenshot-*.png` cho P1/P4;
  `python3 scripts/check_design.py apps/ACTIVE/<slug>/context-ai/design.md` → 0 FAIL cho P4.
- **Khi build:** `app-build` tick `[x]` trong `spec.md` như cũ (bảng bước đếm ở đó) **và** tick việc tương ứng
  trong `plan/active/plan-mvp.md`.
- **Sinh bảng:** `python3 scripts/app.py status <slug>` rồi `python3 scripts/app_table.py`.
- **Lệnh kế tiếp khi báo:** `/app-build <slug>` (phase đang làm).
