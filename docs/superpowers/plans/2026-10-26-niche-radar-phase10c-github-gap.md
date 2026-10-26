# Niche Radar Phase 10c — GitHub Feature Request Gap — Implementation Plan

> **For agentic workers:** làm từng Task theo thứ tự. Mỗi Task xong thì `npm run check` (gốc repo) xanh rồi mới commit.
> Steps dùng checkbox (`- [x]`). Không tạo / nhập token GitHub thay anh, không comment / 👍 / mở issue.

**Goal:** từ issue nhiều 👍 của các repo app Mac / extension, tìm **tính năng người dùng xin mà maintainer không làm**,
xếp theo điểm, gom theo chủ đề và repo, kèm link.

**Spec:** [Phase 10c · GitHub Feature Request Gap](../../web/phase-10c-github-gap.md) · **Cần trước:** Phase 10 (luật chủ
đề, `countMacApps`, trang `/reddit`), Phase 10b (trang "Gap hỏi đáp" có tab, bảng `qa_fetches`-kiểu cache) · **Nguồn quyết
định:** [Bản đồ nguồn gap](../../web/gap-sources-map.md).

## Mục tiêu · làm · không làm

- **Xong khi:** chạy thật nhóm "App Mac menu bar" + "App Mac" (ghi số repo, issue, lệnh, thời gian) · kiểm tay 30 issue:
  loại đúng ≥ 85 %, số phận đúng ≥ 90 % · top 10 mở được và đúng là tính năng chưa có · `.md` chọn được 1 ý tưởng app
  Mac / plugin · test fixture thật.
- **Làm:** bảng `gh_repos`, `gh_issues`; 4 nhóm repo có sẵn + dán tay; collector Search API có xử lý rate limit; phân loại
  loại + số phận; điểm gap từng issue; gom theo chủ đề / repo; tab GitHub; xuất `.md`; token tuỳ chọn ở Cài đặt.
- **Không làm:** comment / 👍 / mở issue · lưu login · repo private, Discussions, PR · cào web GitHub · tạo token thay anh ·
  đọc cây comment.

## Đo trước (2026-10-26, từ máy làm việc)

- Search API không token: `x-ratelimit-limit: 10` (lệnh / phút, nhóm `search`).
- `repo:rxhanson/Rectangle is:issue is:open label:enhancement` → 2 issue, 0 👍. `repo:rxhanson/Rectangle is:issue reactions:>=5`
  → 24 issue, đầu bảng 38 👍. ⇒ **lọc theo 👍, không lọc theo nhãn**.
- Issue "Move window to next/previous desktop": 22 👍, nhãn `wontdo`, `state_reason: completed` ⇒ "không làm" phải xét **nhãn
  hoặc** `not_planned`.
- `repo:raycast/extensions is:issue reactions:>=10` → 25 issue; có issue 43 👍 `not_planned`.
- Số repo mỗi nhóm: menubar ≥ 500★ 38 · macos-app ≥ 1.000★ 88 · chrome-extension ≥ 1.000★ 235 · obsidian-plugin ≥ 500★ 121.

## Global Constraints

- **Không lưu người dùng:** bỏ `user`, `assignee(s)`, `closed_by` trong collector, trước khi ghi DB.
- **Rate limit:** đọc `x-ratelimit-remaining` / `x-ratelimit-reset`; còn 0 thì chờ tới `reset`; ≥ 1 giây giữa hai lệnh;
  lỗi 403 / 429 có `retry-after` thì chờ đúng số giây đó. Cache 7 ngày theo repo.
- **Token tuỳ chọn:** `GITHUB_TOKEN` từ Cài đặt / `.env.local`, gửi header `Authorization: Bearer`. Không có thì chạy không token.
  Không ghi token ra log, file xuất hay DB khác ngoài chỗ Cài đặt đang lưu key.
- **Chạy nền:** một nhóm 50 repo không token ≈ 5 phút. Dùng lại cơ chế job / tiến độ đang có của Research (không viết cơ chế mới).
- **Dùng lại:** `topicsOf`, luật chủ đề `reddit-rules.ts`, `countMacApps` của Phase 10; khung tab của trang Gap hỏi đáp (Phase 10b).
- Luật loại + số phận trong **một file** `web/src/lib/gh-rules.ts`.
- Migration số kế tiếp sau migration của Phase 10b; backup DB trước migrate (Phase 8).
- Test không gọi mạng: collector nhận `fetch` tiêm vào; fixture JSON thật đã bỏ `user`.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/db/schema.ts` + migration mới | `gh_repos`, `gh_issues` |
| `web/src/lib/gh-rules.ts` | 4 nhóm repo (câu search), mẫu nhãn / tiêu đề cho loại, mẫu "không làm" |
| `web/src/lib/gh-collect.ts` | tìm repo theo nhóm, lấy issue theo repo, rate limit, chuẩn hoá |
| `web/src/lib/gh-gap.ts` | phân loại, điểm, bảng issue, gom chủ đề / repo, `.md` |
| `web/src/server/app.ts` | `GET /api/gh`, `POST /api/gh/fetch`, `GET /api/gh/gap`, `GET /api/gh/export.md` |
| `web/src/client/…` (tab GitHub trong trang Gap hỏi đáp) | chọn nhóm / dán repo, tiến độ, bảng, 2 khung gấp |
| `web/src/client/SettingsPage.tsx` (hoặc nơi đang nhập key) | ô token GitHub tuỳ chọn |
| `web/src/lib/features.ts`, `web/src/locales/*` | mục Phase 10c; chữ qua `useT()` |
| `web/tests/gh-*.test.ts` + `web/tests/fixtures/gh/` | fixture Search API thật (bỏ `user`) |

## Tasks

### Task 1: Bảng + luật
- [x] `gh_repos`: `fullName` (khoá), `stars`, `pushedAt`, `description`, `topics` json, `group` (`menubar` · `mac-app` ·
      `chrome-ext` · `obsidian` · `manual`), `archived`, `hasIssues`, `fetchedAt`, `issuesFetchedAt`.
- [x] `gh_issues`: khoá `(repo, number)`, `title`, `body` (≤ 500), `labels` json, `plus1`, `reactions`, `comments`, `state`,
      `stateReason`, `createdAt`, `closedAt`, `url`, `fetchedAt`.
- [x] `gh-rules.ts`: 4 câu search nhóm (đã đo ở trên), mẫu loại tính năng / lỗi theo nhãn + tiêu đề, mẫu "không làm"
      `wont|won't|wontfix|wontdo|not planned|out of scope|declined`, mẫu tên repo bỏ qua `^awesome`.
- [x] Test migrate trên DB đang có dữ liệu Phase 10 / 10b (backup được tạo).

### Task 2: Collector
- [x] `findRepos(group, fetcher)` → `search/repositories?q=<câu nhóm>&sort=stars&per_page=50`; bỏ archived, tắt issue, `awesome-…`.
- [x] `addManualRepos(list)` → `GET /repos/{owner}/{repo}` từng repo (rate limit core, rộng hơn search), kiểm tồn tại.
- [x] `fetchIssues(repo, fetcher)` → `search/issues?q=repo:{repo} is:issue reactions:>=5&sort=reactions-+1&per_page=100`.
- [x] Rate limit + `retry-after` + cache 7 ngày; trả tiến độ (repo thứ mấy / tổng, lệnh còn lại).
- [x] Test với fixture thật: có `user` (bị bỏ), hết lượt (chờ reset — đồng hồ giả), repo không có issue, trùng issue.

### Task 3: Phân loại + điểm
- [x] `kindOf(issue)` → `feature` · `bug` · `other`; `fateOf(issue, now)` → `declined` · `done` · `pending` (kèm số năm).
- [x] `topicsOf` của Phase 10 cho tiêu đề + thân.
- [x] Điểm = log2(1 + 👍) × log2(2 + comment) × min(3, số năm treo) × (declined ? 1,5 : 1); chỉ tính `feature` có
      `declined` hoặc `pending` ≥ 1 năm. Số năm: declined = đóng − mở; pending = hôm nay − mở. Xuất chuỗi công thức.
- [x] `byTopic`: số issue, tổng 👍, số repo khác nhau, số app Mac (`countMacApps`). `byRepo`: số tính năng bị từ chối, tổng 👍.
- [x] Test: ví dụ Rectangle (nhãn `wontdo` + `completed` → `declined`), `not_planned` → `declined`, issue lỗi không vào bảng.

### Task 4: API + màn hình + xuất
- [x] API: `GET /api/gh` (nhóm, repo, lần lấy cuối, lệnh còn lại, có token không) · `POST /api/gh/fetch` (`{ group }` hoặc
      `{ repos: [...] }`, chạy nền) · `GET /api/gh/gap?group=` · `GET /api/gh/export.md?group=`.
- [x] Tab **GitHub** trong trang Gap hỏi đáp: chọn nhóm / ô dán repo → Lấy dữ liệu → tiến độ → bảng issue (cột công
      thức có `title`) → khung gấp "Theo chủ đề", "Theo repo". 1 cột.
- [x] Cài đặt: ô token GitHub tuỳ chọn (che như các key khác), câu hướng dẫn tạo token chỉ đọc công khai.
- [x] `.md`: top 30 issue + top 10 chủ đề, mỗi dòng có link.
- [x] `features.ts`: "Gap GitHub · tính năng bị từ chối" (Phase 10c). Chữ qua `useT()` (vi, en, es).

### Task 5: Chạy thật + soát
- [x] Chạy nhóm "App Mac menu bar" + "App Mac". Ghi số repo, số issue, số lệnh, thời gian vào "Kết quả chạy thật".
- [x] Kiểm tay 30 issue (loại, số phận), ghi tỷ lệ. Mở top 10, kiểm đúng là tính năng chưa có.
- [x] Xuất `.md`, chọn 1 ý tưởng app Mac / plugin, ghi vào đây.
- [x] Screenshot tab GitHub ở 1340 và 375, Read ảnh. Cập nhật chip phase, ROADMAP, CHANGELOG (nhãn Web), `docs/cach-dung.md`.

## Tiến độ

- 2026-10-26: anh duyệt (đề xuất B từ Phase 11), viết plan. Đo trước: Search API không token 10 lệnh / phút; phải lọc theo 👍.
- 2026-10-26: code xong Task 1–5, merge main. 308 test xanh.

## Kết quả chạy thật

Xong 2026-10-26 — số đo, kiểm tay và ý tưởng chọn được ghi ở [trang phase](../../web/phase-10c-github-gap.md#ket-qua-chay-that-2026-10-26). Lệch plan: repo thuộc nhiều nhóm (`groups` json) thay vì 1 cột `group`; chữ trong tab chưa qua `useT()` (trang Gap hỏi đáp Phase 10 / 10b cũng chưa dịch).
