# Plan 2 · 16.1 + 16.2 · Loại project + đầu trang — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Mỗi project có 1 loại cố định (App / YouTube / Sách) hiện bằng icon ở mọi chỗ, và đầu trang project nhìn phát biết ngay (loại, trạng thái, ngày sửa, việc tiếp).

**Architecture:** Thêm cột `projects.type` (migration mới, mặc định `app`). Loại đi qua `createProject` → API → client. Phần hiện tách thành hàm thuần có test (`lib/project-meta.ts`: thời gian tương đối, màu hạn) + component nhỏ (`ProjectTypeIcon`, `StatusBadge` có icon, `ProjectHeader`). Không đổi tab (đó là 16.3).

**Tech Stack:** TypeScript, Drizzle + SQLite (drizzle-kit generate), Hono, React + react-router, Tailwind v4, Vitest.

Spec: `docs/web/phase-plan2-16-trang-project.md` mục 16.1 và 16.2.

## Global Constraints

- 3 loại, đúng chuỗi: `app` · `youtube` · `book`. Project cũ = `app`. Không có loại khác.
- Nhãn hiện: App · YouTube · Sách (English: App · YouTube · Book).
- Trạng thái giữ nguyên 4 giá trị `'đang xem' | 'ứng viên' | 'đang build' | 'loại'`, chỉ thêm icon: 👀 đang xem · ⭐ ứng viên · 🔨 đang build · ✕ loại (icon vẽ bằng `SectionIcon`, không dùng emoji trong UI).
- Ngày sửa hiện tương đối (“vừa xong”, “{n} phút trước”, “{n} giờ trước”, “hôm qua”, “{n} ngày trước”, quá 30 ngày → ngày `YYYY-MM-DD`), ngày giờ đầy đủ trong `title`.
- Việc tiếp: hạn là hôm nay → màu cam (amber); quá hạn → màu đỏ (rose); còn lại xám.
- Đầu trang chỉ còn nút **⋯**; Đổi tên · Nhân bản · Lưu trữ / Bỏ lưu trữ · Xoá hẳn (khi đã lưu trữ) nằm trong menu ⋯.
- Gom 1 thứ vào project khác loại → `window.confirm` hỏi lại, không chặn cứng.
- Mọi chuỗi `tr()` mới phải có bản English trong `web/src/locales/en-text-project.ts` (file mới, gộp vào `en-text.ts`).
- Không hiện số phase / số mục trên UI. Không bịa số.
- Layout đứng từ 960px tới 1920px, không cuộn ngang cả trang; chữ dài `truncate` + `title`; con chứa chữ `min-w-0`, nút / icon / chip `shrink-0`; mặt thẻ `bg-surface`, xám dùng `zinc-*`.
- Code mới có test trong `web/tests/`. `npm run check` (gốc repo) xanh; sửa docs thì `npm run docs:build` xanh.
- Commit trailer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

---

### Task 1: Cột `projects.type` + lib + API

**Files:**
- Modify: `web/src/db/schema.ts` (bảng `projects`, ~dòng 276–300)
- Create: `web/drizzle/0028_*.sql` + `web/drizzle/meta/*` (sinh bằng `npm run db:generate` ở `web/`)
- Modify: `web/src/lib/projects.ts` (`ProjectSummary`, `listProjects`, `createProject`, `duplicateProject`)
- Modify: `web/src/server/app.ts:923` (`POST /api/projects`)
- Modify: `web/src/lib/projects-client.ts` (`PROJECT_TYPES`, `projectsApi.create`, `searchProjects` lọc `type`)
- Test: `web/tests/project-type.test.ts` (mới)

**Interfaces:**
- Produces: `PROJECT_TYPES = ['app', 'youtube', 'book'] as const` và `type ProjectType` export từ `@/db/schema`; `ProjectSummary.type: ProjectType`; `createProject(db, name, by?, type?: unknown)`; `projectsApi.create(name: string, type?: ProjectType)`; `ProjectQuery.type?: ProjectType | ''`.

- [ ] **Step 1: Viết test đỏ** — `web/tests/project-type.test.ts`. Dùng cùng cách dựng DB tạm như `web/tests/projects-api.test.ts` (đọc file đó, chép phần tạo DB / app). Các ca:

```ts
// 1. createProject không truyền loại → type 'app'
expect(createProject(db, 'A').type).toBe('app');
// 2. truyền 'book' → 'book'; truyền 'youtube' → 'youtube'
expect(createProject(db, 'B', undefined, 'book').type).toBe('book');
// 3. loại lạ → ProjectError 400
expect(() => createProject(db, 'C', undefined, 'game')).toThrow(ProjectError);
// 4. duplicateProject giữ loại
const b = createProject(db, 'D', undefined, 'youtube');
expect(duplicateProject(db, b.id).type).toBe('youtube');
// 5. getProject(db, id).type có mặt
// 6. API: POST /api/projects { name: 'E', type: 'book' } → 200, body.type === 'book'; { type: 'x' } → 400
// 7. searchProjects(list, { type: 'book' }) chỉ giữ project loại book; type '' / không có → giữ hết
```

- [ ] **Step 2: Chạy test, thấy đỏ** — `cd web && npx vitest run tests/project-type.test.ts`. Mong đợi: FAIL (`type` undefined / tham số thừa).

- [ ] **Step 3: Schema** — trong `web/src/db/schema.ts`, ngay trên `export const projects = sqliteTable(...)` thêm:

```ts
/** Plan 2 mục 16.1: loại project — App (niche app store) · YouTube · Sách. Project cũ = app. */
export const PROJECT_TYPES = ['app', 'youtube', 'book'] as const;
export type ProjectType = (typeof PROJECT_TYPES)[number];
```

và trong bảng `projects`, sau dòng `status: ...`:

```ts
  type: text('type', { enum: PROJECT_TYPES }).notNull().default('app'),
```

- [ ] **Step 4: Sinh migration** — `cd web && npm run db:generate`. Kiểm file `drizzle/0028_*.sql` chỉ có đúng 1 lệnh `ALTER TABLE \`projects\` ADD \`type\` text DEFAULT 'app' NOT NULL;`. Nếu drizzle-kit sinh thêm lệnh khác (bảng khác lệch snapshot) → dừng, báo lại, không sửa tay migration của người khác.

- [ ] **Step 5: lib/projects.ts**
  - `ProjectSummary` thêm `type: ProjectType;` (import `PROJECT_TYPES, type ProjectType` từ `@/db/schema`).
  - `listProjects`: thêm `type: p.type` vào object trả về (đọc hàm, thêm cạnh `status`).
  - Hàm kiểm:

```ts
function cleanType(v: unknown): ProjectType {
  if (v === undefined || v === null || v === '') return 'app';
  if (typeof v === 'string' && (PROJECT_TYPES as readonly string[]).includes(v)) return v as ProjectType;
  throw new ProjectError(tr('Loại project phải là app, youtube hoặc book'), 400);
}
```

  - `createProject(db: Db, name: unknown, by?: string, type?: unknown)`: `const ty = cleanType(type);` trước insert, thêm `type: ty` vào `values(...)`, và `log(db, p.id, 'tạo project', { name: p.name, by, type: ty })`.
  - `duplicateProject`: `createProject(db, <tên cũ>, undefined, p.type)`.

- [ ] **Step 6: API** — `web/src/server/app.ts:923` đổi thành:

```ts
  api.post('/projects', (c) => projectCall(c, true, (b) => { projectRoom(); return createProject(db(), b.name, undefined, b.type); }));
```

- [ ] **Step 7: projects-client.ts**
  - `export { PROJECT_TYPES } from '@/db/schema'; export type { ProjectType } from '@/db/schema';` (nếu import giá trị từ schema làm bundle client kéo cả drizzle → thay bằng hằng chép lại `export const PROJECT_TYPES: ProjectType[] = ['app', 'youtube', 'book'];` như cách file này đang chép `PROJECT_STATUSES`).
  - `create: (name: string, type?: ProjectType) => send<ProjectSummary>('POST', '/api/projects', { name, type }),`
  - `ProjectQuery` thêm `type?: ProjectType | '';` và trong `searchProjects` thêm `.filter((p) => !f.type || p.type === f.type)`.

- [ ] **Step 8: Chạy test xanh** — `npx vitest run tests/project-type.test.ts tests/projects-api.test.ts tests/collect.test.ts tests/portable.test.ts`. Mong đợi: PASS hết (portable chép cột tự động theo `PRAGMA table_info`, phải vẫn xanh).

- [ ] **Step 9: English** — tạo `web/src/locales/en-text-project.ts` theo khuôn `en-text-build.ts` (`export const projectEnText: Record<string, string> = { ... }`), thêm `'Loại project phải là app, youtube hoặc book': 'Project type must be app, youtube or book'`, rồi import + spread `...projectEnText` trong `en-text.ts` cạnh `...buildEnText`.

- [ ] **Step 10: Commit**

```bash
git add web/src/db/schema.ts web/drizzle web/src/lib/projects.ts web/src/server/app.ts web/src/lib/projects-client.ts web/src/locales/en-text-project.ts web/src/locales/en-text.ts web/tests/project-type.test.ts
git commit -m "feat(web): add project type app · youtube · book"
```

---

### Task 2: Hàm thuần đầu trang + icon loại / trạng thái

**Files:**
- Create: `web/src/lib/project-meta.ts`
- Modify: `web/src/components/SectionIcon.tsx` (thêm icon `book`, `hammer`, `x`)
- Create: `web/src/components/ProjectType.tsx`
- Modify: `web/src/components/ProjectStatus.tsx` (icon trong `StatusBadge`)
- Modify: `web/src/locales/en-text-project.ts`
- Test: `web/tests/project-meta.test.ts` (mới)

**Interfaces:**
- Consumes: `ProjectType`, `ProjectStatus` (Task 1).
- Produces:
  - `timeAgo(iso: string, now: Date): string` — chuỗi đã qua `tr()`.
  - `dueTone(nextDue: string | null, today: string): 'none' | 'later' | 'today' | 'over'` (`today` dạng `YYYY-MM-DD`).
  - `TYPE_META: Record<ProjectType, { label: string; icon: SectionIconName; tone: string }>`.
  - `<ProjectTypeIcon type size?: 'sm' | 'lg' />` — ô vuông bo góc có icon màu, `aria-label` = nhãn loại.
  - `<StatusBadge status />` giữ props cũ, thêm icon trước chữ.

- [ ] **Step 1: Test đỏ** — `web/tests/project-meta.test.ts`:

```ts
import { describe, expect, it } from 'vitest';
import { dueTone, timeAgo } from '@/lib/project-meta';

const now = new Date('2026-11-15T12:00:00Z');
describe('timeAgo', () => {
  it('dưới 1 phút', () => expect(timeAgo('2026-11-15T11:59:40Z', now)).toBe('vừa xong'));
  it('phút', () => expect(timeAgo('2026-11-15T11:35:00Z', now)).toBe('25 phút trước'));
  it('giờ', () => expect(timeAgo('2026-11-15T09:00:00Z', now)).toBe('3 giờ trước'));
  it('hôm qua (24–48 giờ)', () => expect(timeAgo('2026-11-14T08:00:00Z', now)).toBe('hôm qua'));
  it('ngày', () => expect(timeAgo('2026-11-10T12:00:00Z', now)).toBe('5 ngày trước'));
  it('quá 30 ngày → ngày', () => expect(timeAgo('2026-09-01T12:00:00Z', now)).toBe('2026-09-01'));
  it('tương lai (lệch đồng hồ) → vừa xong', () => expect(timeAgo('2026-11-15T12:05:00Z', now)).toBe('vừa xong'));
});
describe('dueTone', () => {
  it('không hạn', () => expect(dueTone(null, '2026-11-15')).toBe('none'));
  it('còn xa', () => expect(dueTone('2026-11-18', '2026-11-15')).toBe('later'));
  it('hôm nay', () => expect(dueTone('2026-11-15', '2026-11-15')).toBe('today'));
  it('quá hạn', () => expect(dueTone('2026-11-14', '2026-11-15')).toBe('over'));
});
```

Thêm 1 ca English: `setActiveLang('en')` (xem cách `web/tests/build-kit.test.ts` đổi ngôn ngữ) → `timeAgo('2026-11-15T09:00:00Z', now) === '3 hours ago'`, rồi trả về `'vi'`.

- [ ] **Step 2: Chạy, thấy đỏ** — `npx vitest run tests/project-meta.test.ts`.

- [ ] **Step 3: `web/src/lib/project-meta.ts`**

```ts
import { tr } from '@/lib/i18n';

/** Plan 2 mục 16.2: ngày sửa project dạng tương đối — “3 giờ trước”; quá 30 ngày thì hiện ngày. */
export function timeAgo(iso: string, now: Date): string {
  const ms = now.getTime() - new Date(iso).getTime();
  const min = Math.floor(ms / 60_000);
  if (min < 1) return tr('vừa xong');
  if (min < 60) return tr('{n} phút trước', { n: min });
  const h = Math.floor(min / 60);
  if (h < 24) return tr('{n} giờ trước', { n: h });
  if (h < 48) return tr('hôm qua');
  const d = Math.floor(h / 24);
  if (d <= 30) return tr('{n} ngày trước', { n: d });
  return iso.slice(0, 10);
}

/** Màu ô “việc tiếp”: hạn hôm nay = cam, quá hạn = đỏ. `today` = YYYY-MM-DD theo giờ máy. */
export function dueTone(nextDue: string | null, today: string): 'none' | 'later' | 'today' | 'over' {
  if (!nextDue) return 'none';
  return nextDue < today ? 'over' : nextDue === today ? 'today' : 'later';
}
```

(`'{n} phút trước'` đã có trong `ActivityMenu.tsx` — kiểm `en-text*.ts` đã có bản English chưa, có rồi thì không thêm lại.)

- [ ] **Step 4: Icon** — `web/src/components/SectionIcon.tsx`: thêm `'book' | 'hammer' | 'x'` vào `SectionIconName` và 3 path kiểu Lucide (viewBox 24, nét `currentColor`, giống các icon có sẵn):

```tsx
  book: <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20" />,
  hammer: <path d="m15 12-8.4 8.4a2.1 2.1 0 1 1-3-3L12 9M17.6 15 22 10.6M20.9 11.7l-1.3-1.3a2 2 0 0 1-.6-1.4V7.9l-2.3-2.3A5.3 5.3 0 0 0 12.9 4H9.7l.9.8a5.4 5.4 0 0 1 1.9 4.1V10l2 2h1.1c.5 0 1 .2 1.4.6l1.3 1.3" />,
  x: <path d="M18 6 6 18M6 6l12 12" />,
```

- [ ] **Step 5: `web/src/components/ProjectType.tsx`**

```tsx
import type { ProjectType } from '@/lib/projects-client';
import { lazyTr, tr, tx } from '@/lib/i18n';
import { SectionIcon, type SectionIconName } from './SectionIcon';

/** Plan 2 mục 16.1: mỗi loại project 1 icon + 1 màu — dùng ở đầu trang, danh sách Projects, nút + Collect. */
export const TYPE_META: Record<ProjectType, { label: string; icon: SectionIconName; tone: string }> = lazyTr({
  app: { label: 'App', icon: 'phone', tone: 'bg-blue-50 text-blue-700' },
  youtube: { label: 'YouTube', icon: 'play', tone: 'bg-rose-50 text-rose-700' },
  book: { label: tx('Sách'), icon: 'book', tone: 'bg-amber-50 text-amber-800' },
});

export function ProjectTypeIcon({ type, size = 'sm' }: { type: ProjectType; size?: 'sm' | 'lg' }) {
  const m = TYPE_META[type] ?? TYPE_META.app;
  return (
    <span role="img" aria-label={m.label} title={m.label}
      className={`inline-grid shrink-0 place-items-center ${m.tone} ${size === 'lg' ? 'h-10 w-10 rounded-xl' : 'h-6 w-6 rounded-md'}`}>
      <SectionIcon name={m.icon} className={size === 'lg' ? 'h-5 w-5' : 'h-3.5 w-3.5'} />
    </span>
  );
}
export const typeLabel = (t: ProjectType) => (TYPE_META[t] ?? TYPE_META.app).label || tr('App');
```

(Đọc `lazyTr` / `tx` trong `@/lib/i18n` để dùng đúng như `KIND_LABEL` trong `projects-client.ts`. Màu `blue-50` / `rose-50` / `amber-50` đã được `theme:dark` đổi cho chế độ tối — kiểm trong `globals.css`; thiếu thì chạy `npm run theme:dark`.)

- [ ] **Step 6: `StatusBadge` có icon** — `web/src/components/ProjectStatus.tsx`:

```tsx
const ICON: Record<ProjectStatus, SectionIconName> = { 'đang xem': 'eye', 'ứng viên': 'star', 'đang build': 'hammer', loại: 'x' };

export function StatusBadge({ status }: { status: ProjectStatus }) {
  return (
    <span className={`inline-flex shrink-0 items-center gap-1 rounded-full border px-2.5 py-0.5 text-xs font-medium ${TONE[status]}`}>
      <SectionIcon name={ICON[status]} className="h-3.5 w-3.5" />{tr(status)}
    </span>
  );
}
```

- [ ] **Step 7: English** — thêm vào `en-text-project.ts` mọi khoá mới chưa có: `'vừa xong': 'just now'`, `'{n} giờ trước': '{n} hours ago'`, `'hôm qua': 'yesterday'`, `'{n} ngày trước': '{n} days ago'`, `'Sách': 'Book'` (và `'{n} phút trước': '{n} min ago'` nếu chưa có ở file khác). Chạy test i18n có sẵn (tìm `tests/*i18n*`) để chắc không thiếu khoá.

- [ ] **Step 8: Chạy test xanh** — `npx vitest run tests/project-meta.test.ts` + test i18n. PASS.

- [ ] **Step 9: Commit**

```bash
git add web/src/lib/project-meta.ts web/src/components/SectionIcon.tsx web/src/components/ProjectType.tsx web/src/components/ProjectStatus.tsx web/src/locales/en-text-project.ts web/tests/project-meta.test.ts
git commit -m "feat(web): project type icon, status icons, relative time helpers"
```

---

### Task 3: Đầu trang project mới (16.2)

**Files:**
- Create: `web/src/components/ProjectHeader.tsx`
- Modify: `web/src/client/ProjectPage.tsx` (khối `<header className="page-heading ...">`, ~dòng 124–146)
- Modify: `web/src/locales/en-text-project.ts`
- Test: `web/tests/project-header.test.tsx` (mới; xem `web/tests/ui-shell.test.ts` để biết cách render React trong test của repo)

**Interfaces:**
- Consumes: `ProjectTypeIcon`, `StatusBadge`, `timeAgo`, `dueTone` (Task 2); `view.type` (Task 1).
- Produces: `<ProjectHeader view={view} itemCount busy nameEditor onRename onDuplicate onArchive onRemove />` — `nameEditor` là phần tử tên (h1 bấm đúp / ô sửa) ProjectPage truyền vào, để giữ nguyên logic đổi tên có sẵn.

- [ ] **Step 1: Test đỏ** — render `ProjectHeader` với `view` giả `{ name: 'draw for kids · US', type: 'app', status: 'đang build', updatedAt: <3 giờ trước>, nextStep: 'viết Spec', nextDue: <hôm nay>, archivedAt: null, tags: [] }`:
  - có `role="img"` tên “App”;
  - có chữ “đang build”;
  - có chữ “3 giờ trước” và phần tử đó có `title` chứa ngày giờ đầy đủ;
  - dòng việc tiếp chứa “viết Spec” và có class `text-amber-700`; đổi `nextDue` thành hôm qua → `text-rose-700`;
  - KHÔNG có nút “Đổi tên” hiện sẵn; bấm nút `aria-label="Thêm thao tác"` (⋯) → hiện “Đổi tên”, “Nhân bản”, “Lưu trữ”; bấm “Nhân bản” gọi `onDuplicate`;
  - `archivedAt` có giá trị → menu có “Bỏ lưu trữ” và “Xoá hẳn”.

- [ ] **Step 2: Chạy, thấy đỏ.**

- [ ] **Step 3: `ProjectHeader.tsx`** — bố cục 1 hàng `flex items-center gap-3 min-w-0`:
  1. `<ProjectTypeIcon type={view.type} size="lg" />`
  2. Khối `min-w-0 flex-1`: dòng 1 = `nameEditor` (h1 phải có `truncate` + `title={view.name}`); dòng 2 = hàng chip `flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-zinc-500`:
     - `<StatusBadge status={view.status} />`
     - đã lưu trữ → chip xám `tr('đã lưu trữ')` như cũ
     - `<span title={view.updatedAt.slice(0, 16).replace('T', ' ')}><SectionIcon name="clock" /> {tr('sửa {t}', { t: timeAgo(view.updatedAt, new Date()) })}</span>`
     - `<span>{itemCount} item</span>` (giữ đếm item, chữ nhỏ)
     - có `nextStep` → `<span className={tone}><SectionIcon name="calendar" /> {nextDue ? tr('hẹn {d}: {s}', { d: ddmm(nextDue), s: nextStep }) : nextStep}</span>` với `tone` = `today` → `font-medium text-amber-700`, `over` → `font-medium text-rose-700`, còn lại `text-zinc-600`; `ddmm('2026-11-18') === '18/11'`; phần chữ việc tiếp `truncate max-w-[28rem]` + `title`.
  3. Nút ⋯ `shrink-0` (`aria-label={tr('Thêm thao tác')}`, `aria-expanded`), mở menu nổi bên phải (`absolute right-0 top-full z-20 bg-surface border border-zinc-200 rounded-xl shadow-lg`), đóng khi bấm ngoài / Esc. Mục: Đổi tên · Nhân bản · Lưu trữ (hoặc Bỏ lưu trữ) · Xoá hẳn (chỉ khi đã lưu trữ, chữ `text-rose-700`). Tất cả `disabled={busy}`.
  - Dưới hàng chính giữ dòng thẻ `#tag` như cũ.
  - `today` cho `dueTone` lấy theo giờ máy: `new Date().toLocaleDateString('en-CA')`.

- [ ] **Step 4: Gắn vào `ProjectPage.tsx`** — thay khối `<header className="page-heading space-y-2">…</header>` bằng: link `← Projects` giữ nguyên ở trên, rồi `<ProjectHeader …/>` truyền `nameEditor` = đúng JSX h1 / input hiện có (h1 thêm `truncate` và `title`), `onRename={rename}`, `onDuplicate={() => void duplicate()}`, `onArchive={() => void save({ archived: !view.archivedAt })}`, `onRemove={() => void remove()}`. Bỏ dòng “Bước tiếp: …” cũ dưới header (đã lên chip). Xoá biến `overdue` nếu không còn dùng.

- [ ] **Step 5: English** — `'sửa {t}': 'edited {t}'`, `'hẹn {d}: {s}': 'due {d}: {s}'`, `'Thêm thao tác': 'More actions'` (các khoá Đổi tên / Nhân bản / Lưu trữ / Bỏ lưu trữ / Xoá hẳn đã có English — kiểm).

- [ ] **Step 6: Test xanh** — `npx vitest run tests/project-header.test.tsx` + test i18n. PASS.

- [ ] **Step 7: Commit**

```bash
git add web/src/components/ProjectHeader.tsx web/src/client/ProjectPage.tsx web/src/locales/en-text-project.ts web/tests/project-header.test.tsx
git commit -m "feat(web): project header with type, status icon, relative time, due tone, more menu"
```

---

### Task 4: Danh sách Projects + tạo có loại + nút Collect

**Files:**
- Modify: `web/src/client/ProjectsPage.tsx` (form tạo ~dòng 87, chip lọc ~dòng 114, bảng ~dòng 139–165)
- Modify: `web/src/components/CollectButton.tsx`
- Modify: `web/src/client/BooksResearch.tsx:741`
- Modify: `web/src/locales/en-text-project.ts`
- Test: `web/tests/project-type.test.ts` (thêm ca) + `web/tests/collect.test.ts` nếu cần

**Interfaces:**
- Consumes: `projectsApi.create(name, type)`, `ProjectQuery.type`, `ProjectTypeIcon`, `TYPE_META`, `timeAgo` (Task 1–2).
- Produces: `CollectButton` prop mới `projectType?: ProjectType` (mặc định `'app'`); hàm thuần `typeMismatch(project: { type: ProjectType }, want: ProjectType): boolean` export từ `CollectButton.tsx` hoặc `lib/project-meta.ts` (ưu tiên `lib/project-meta.ts` để test không cần render).

- [ ] **Step 1: Test đỏ** — trong `project-type.test.ts`: `typeMismatch({ type: 'app' }, 'book') === true`, `typeMismatch({ type: 'book' }, 'book') === false`.

- [ ] **Step 2: Chạy, thấy đỏ.**

- [ ] **Step 3: `typeMismatch`** trong `lib/project-meta.ts`:

```ts
import type { ProjectType } from '@/db/schema';
export const typeMismatch = (p: { type?: ProjectType }, want: ProjectType) => (p.type ?? 'app') !== want;
```

- [ ] **Step 4: ProjectsPage**
  - Form tạo: trước ô tên thêm nhóm 3 nút chọn loại (`role="radiogroup"`, mỗi nút `ProjectTypeIcon` + nhãn, `aria-pressed`), state `newType` mặc định `'app'`; submit gọi `projectsApi.create(name, newType)`.
  - Chip lọc: thêm 1 hàng chip loại (Tất cả · App · YouTube · Sách, mỗi chip có icon + số đếm) đặt trong searchParams `type` giống cách `status` đang làm, truyền `type` vào `searchProjects`.
  - Bảng: cột tên thêm `<ProjectTypeIcon type={p.type} />` trước tên (ô `flex items-center gap-2 min-w-0`, tên `truncate`); cột cập nhật đổi thành `timeAgo(p.updatedAt, now)` với `title` ngày giờ đầy đủ.

- [ ] **Step 5: CollectButton**
  - Prop `projectType?: ProjectType` (mặc định `'app'`).
  - Danh sách project trong popup: mỗi dòng thêm `<ProjectTypeIcon type={p.type} />` trước tên.
  - `addTo(p)`: nếu `typeMismatch(p, projectType)` → `if (!window.confirm(tr('“{name}” là project {a}, thứ này thuộc {b}. Vẫn thêm?', { name: p.name, a: TYPE_META[p.type].label, b: TYPE_META[projectType].label }))) return;`
  - `createAndAdd`: `projectsApi.create(name, projectType)`.
- [ ] **Step 6: BooksResearch** — `web/src/client/BooksResearch.tsx:741`: `<CollectButton target={{ term: v.keyword, country }} projectType="book" />`. (Tìm thêm `CollectButton` ở `BookHunt.tsx` / trang YouTube; có thì truyền `book` / `youtube` tương ứng.)

- [ ] **Step 7: English** — `'“{name}” là project {a}, thứ này thuộc {b}. Vẫn thêm?': '“{name}” is a {a} project and this belongs to {b}. Add anyway?'`, `'Loại project': 'Project type'`, nhãn chip “Tất cả” đã có.

- [ ] **Step 8: Test xanh** — `npx vitest run tests/project-type.test.ts tests/collect.test.ts` + test i18n. PASS.

- [ ] **Step 9: Commit**

```bash
git add web/src/client/ProjectsPage.tsx web/src/components/CollectButton.tsx web/src/client/BooksResearch.tsx web/src/lib/project-meta.ts web/src/locales/en-text-project.ts web/tests/project-type.test.ts
git commit -m "feat(web): project type in projects list, create form and collect button"
```

---

### Task 5: Docs + soát cả bộ

**Files:**
- Modify: `docs/web/phase-plan2-16-trang-project.md` (chip 16.1 + 16.2 đã code, ghi lại điều khác spec nếu có)
- Modify: `docs/web/index.md` (chip mục 16)
- Modify: `CHANGELOG.md` dưới `[Unreleased]`: `- Web: project có loại App / YouTube / Sách, đầu trang project có icon, ngày sửa tương đối, hạn việc tiếp đổi màu (Plan 2 mục 16.1–16.2).`

- [ ] **Step 1:** Cập nhật 3 file trên.
- [ ] **Step 2:** `npm run check` ở gốc repo → xanh. `npm run docs:build` → xanh.
- [ ] **Step 3: Commit**

```bash
git add docs/web/phase-plan2-16-trang-project.md docs/web/index.md CHANGELOG.md
git commit -m "docs(web): mark project type and header as coded"
```
