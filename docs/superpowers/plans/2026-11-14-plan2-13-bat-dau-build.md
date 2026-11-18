# Mục 13 · Nút Bắt đầu build — Plan code

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Một nút trên trang Research tạo (hoặc mở lại) project build đã gom sẵn keyword · đối thủ · lời chê · khoảng trống, có tab Build 5 bước và xuất bộ build cho Claude Code.

**Architecture:** Project build = phiên AI Agent sẵn có (`projects.kind = 'hunt'`, tạo bằng `huntFromRun`) + trạng thái mới `đang build`. Hàm thuần `pickBuildItems` chọn đồ gom từ dữ liệu 1 lượt Research; `buildFromRun` (async) đọc lời chê / khoảng trống **chỉ từ cache** (không gọi mạng) rồi gom bằng `addItems`. Bộ build = `saveHuntDocs` + CSV + `complaints.md` + `START.md` ghi vào `<thư mục AI>/briefs/<tên>/`.

**Tech Stack:** TypeScript, Hono (server), React + react-router, Drizzle + SQLite, Vitest, Tailwind v4.

**Spec:** [docs/web/phase-plan2-13-bat-dau-build.md](../../web/phase-plan2-13-bat-dau-build.md)

## Global Constraints

- Mọi chữ hiện trên UI bọc `tr('…')` tiếng Việt và có bản tiếng Anh trong `web/src/locales/en-text-build.ts` (test `i18n-text.test.ts` đỏ nếu thiếu).
- Không hiện số mục / số phase trên UI.
- Gom: keyword ≤ 20 · đối thủ ≤ 10 · lời chê ≤ 8 · khoảng trống ≤ 5. Khi bấm nút: không gọi AI, không tra lại, không gọi mạng.
- Bản Free: gom + tạo project không cần PRO. Viết Brief / Spec / Plan cần PRO (giữ như hiện tại). Xuất bộ build: không khoá PRO (tài liệu chỉ có khi đã viết bằng PRO; CSV vẫn ra).
- Layout: đứng được 960px → 1920px, chữ dài `truncate` + `title`, con chứa chữ `min-w-0`, nút `shrink-0`, mặt thẻ `bg-surface`, xám dùng `zinc-*`.
- Code mới kèm test trong `web/tests/`. Xong: `npm run check` ở gốc repo xanh, `npm run docs:build` xanh.
- Cây làm việc đang có thay đổi chưa commit của việc khác (`web/src/client/heat-ui.tsx`, `web/src/locales/en-text-visual.ts`, `CHANGELOG.md`) — **không** `git add -A`; chỉ add đúng file của task.
- Commit theo `<type>(<scope>): <làm gì>`, scope `web` hoặc `docs`.

## Bản đồ file

| File | Việc |
|---|---|
| `web/src/db/schema.ts` · `web/src/lib/projects.ts` · `web/src/lib/projects-client.ts` · `web/src/components/ProjectStatus.tsx` | trạng thái project `đang build` |
| `web/src/lib/build-start.ts` (mới) | `pickBuildItems` (thuần) · `gatherBuildInputs` (cache) · `buildFromRun` |
| `web/src/lib/export/build-kit.ts` (mới) | `saveBuildKit`, `complaintsMd`, `startMd` |
| `web/src/server/app.ts` | `POST /api/build/from-run` · `POST /api/projects/:id/build-kit` |
| `web/src/server/hunt-api.ts` | `/from-run` dùng `buildFromRun` (gộp 2 đường) |
| `web/src/components/StartBuildButton.tsx` (mới) · `web/src/components/RunHeader.tsx` | nút ▶ Bắt đầu build |
| `web/src/components/BuildTab.tsx` (mới) · `web/src/client/ProjectPage.tsx` | tab Build 5 bước |
| `web/src/locales/en-text-build.ts` (mới) · `web/src/locales/en-text.ts` | chữ tiếng Anh |
| `web/tests/build-start.test.ts` · `web/tests/build-kit.test.ts` (mới) | test |

---

### Task 1: Trạng thái project `đang build`

**Files:**
- Modify: `web/src/db/schema.ts:281`
- Modify: `web/src/lib/projects.ts:11`
- Modify: `web/src/lib/projects-client.ts:7`
- Modify: `web/src/components/ProjectStatus.tsx:4-8`
- Create: `web/src/locales/en-text-build.ts`
- Modify: `web/src/locales/en-text.ts` (import + spread)
- Test: `web/tests/build-start.test.ts`

**Interfaces:**
- Produces: `ProjectStatus` gồm `'đang build'`; `PROJECT_STATUSES = ['đang xem', 'ứng viên', 'đang build', 'loại']`.

- [ ] **Step 1: Viết test đỏ**

```ts
// web/tests/build-start.test.ts
import { describe, expect, it } from 'vitest';
import { createDb } from '@/db/client';
import { createProject, getProject, updateProject } from '@/lib/projects';

describe('trạng thái đang build', () => {
  it('project nhận trạng thái "đang build"', () => {
    const db = createDb(':memory:');
    const p = createProject(db, 'draw for kids');
    updateProject(db, p.id, { status: 'đang build' });
    expect(getProject(db, p.id).status).toBe('đang build');
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ**

Run: `cd web && npx vitest run tests/build-start.test.ts`
Expected: FAIL — `Trạng thái phải là: đang xem · ứng viên · loại`

- [ ] **Step 3: Sửa code**

`web/src/db/schema.ts:281`:
```ts
  status: text('status', { enum: ['đang xem', 'ứng viên', 'đang build', 'loại'] }).notNull().default('đang xem'),
```
(SQLite không có CHECK cho enum này — không cần migration; kiểm lại bằng `grep -n "CHECK" web/src/db/client.ts` → không có dòng nào về status.)

`web/src/lib/projects.ts:11`:
```ts
export const PROJECT_STATUSES = ['đang xem', 'ứng viên', 'đang build', 'loại'] as const;
```

`web/src/lib/projects-client.ts:7`:
```ts
export const PROJECT_STATUSES: ProjectStatus[] = ['đang xem', 'ứng viên', 'đang build', 'loại'];
```

`web/src/components/ProjectStatus.tsx` — thêm tông xanh dương:
```ts
const TONE: Record<ProjectStatus, string> = {
  'đang xem': 'border-zinc-200 bg-zinc-50 text-zinc-600',
  'ứng viên': 'border-emerald-200 bg-emerald-50 text-emerald-800',
  'đang build': 'border-blue-200 bg-blue-50 text-blue-800',
  loại: 'border-rose-200 bg-rose-50 text-rose-700',
};
```
và sửa chú thích: `/** Nhãn trạng thái đánh giá của project: đang xem · ứng viên · đang build · loại. */`

`web/src/locales/en-text-build.ts`:
```ts
/**
 * Bản tiếng Anh cho nút Bắt đầu build + tab Build (2026-11-14). Gộp vào `enText` (en-text.ts). Khoá = đúng chữ tiếng Việt trong code.
 */
export const buildEnText: Record<string, string> = {
  'đang build': 'building',
};
```
`web/src/locales/en-text.ts`: thêm `import { buildEnText } from './en-text-build';` cạnh `visualEnText` và `...buildEnText,` trong object gộp.

- [ ] **Step 4: Tìm chỗ khác liệt kê trạng thái**

Run: `cd web && grep -rn "'ứng viên', 'loại'\]" src | grep -v ITEM_STATUSES`
Expected: chỉ còn dòng của `ITEM_STATUSES` (trạng thái item, không đổi). Dòng nào khác của trạng thái project thì thêm `'đang build'` vào đúng chỗ.

- [ ] **Step 5: Chạy test, thấy xanh**

Run: `cd web && npx vitest run tests/build-start.test.ts tests/i18n-text.test.ts tests/collect.test.ts`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add web/src/db/schema.ts web/src/lib/projects.ts web/src/lib/projects-client.ts web/src/components/ProjectStatus.tsx web/src/locales/en-text-build.ts web/src/locales/en-text.ts web/tests/build-start.test.ts
git commit -m "feat(web): add building project status"
```

---

### Task 2: `pickBuildItems` — chọn đồ gom (hàm thuần)

**Files:**
- Create: `web/src/lib/build-start.ts`
- Test: `web/tests/build-start.test.ts` (thêm describe)

**Interfaces:**
- Consumes: `KeywordRow`, `CompetitorRow` (`@/lib/run-view`), `Complaint` (`@/lib/complaints`), `GapRowView` (`@/lib/feature-gap`).
- Produces:
```ts
export const BUILD_LIMITS = { keyword: 20, competitor: 10, complaint: 8, gap: 5 } as const;
export type BuildRun = { id: number; seed: string; country: string };
export type BuildInputs = { keywords: KeywordRow[]; competitors: CompetitorRow[]; complaints: Complaint[]; gapRows: GapRowView[]; gapApps: number };
export function pickBuildItems(run: BuildRun, inp: BuildInputs): Record<string, unknown>[]; // target cho addItems
```

Luật chọn (ghi đúng vào chú thích đầu file):
- Keyword: keyword gốc (`origin === 'seed'`) trước, rồi keyword gợi ý xếp **ít đối thủ nhất** (`playCount + appstoreCount` tăng dần), tối đa 20. Không có dòng seed thì vẫn thêm `run.seed`.
- Đối thủ: nhiều rating nhất (`ratingsCount` giảm dần, null = 0), cả 2 store, tối đa 10, bỏ trùng `url`.
- Lời chê: `count × severity.weight` giảm dần, tối đa 8.
- Khoảng trống: chỉ hàng `gap === 'gap'` rồi `'positioning'`; trong mỗi nhóm `have` tăng dần; tối đa 5.
- Target giống hệt nút + Collect hiện có (cùng `ref`) để gom tay sau đó không trùng.

- [ ] **Step 1: Viết test đỏ**

```ts
// thêm vào web/tests/build-start.test.ts
import { BUILD_LIMITS, pickBuildItems, type BuildInputs } from '@/lib/build-start';
import type { CompetitorRow, KeywordRow } from '@/lib/run-view';
import type { Complaint } from '@/lib/complaints';
import type { GapRowView } from '@/lib/feature-gap';

const RUN = { id: 7, seed: 'draw for kids', country: 'US' };
const kw = (term: string, play: number, ios: number, origin: KeywordRow['origin'] = 'play_suggest'): KeywordRow =>
  ({ id: Math.random(), term, origin, playCount: play, appstoreCount: ios, topPlay: null, topAppstore: null });
const app = (title: string, ratingsCount: number | null, store: CompetitorRow['store'] = 'play'): CompetitorRow => ({
  appId: Math.floor(Math.random() * 1e6), store, title, developer: 'Dev', iconUrl: null, url: `https://x/${title}`, price: 0, currency: null,
  rating: 4.2, ratingsCount, installsMin: null, updatedAt: null, releasedAt: null, keywordCount: 1, bestRank: 1, offersIap: null, iapRange: null, contentRating: null,
});
const complaint = (key: string, count: number, weight = 1) =>
  ({ phrase: key, key, count, byStore: { play: count, appstore: 0 }, type: 'bug', typeLabel: 'Lỗi', severity: { weight, label: '' }, apps: ['A'], quotes: [] }) as unknown as Complaint;
const gapRow = (key: string, gap: GapRowView['gap'], have: number) => ({ key, label: key, gap, have, unknown: 0, unstated: 0, cells: {} }) as unknown as GapRowView;
const empty: BuildInputs = { keywords: [], competitors: [], complaints: [], gapRows: [], gapApps: 0 };

describe('pickBuildItems', () => {
  it('keyword gốc đứng đầu, rồi keyword ít đối thủ nhất; tối đa 20', () => {
    const many = Array.from({ length: 30 }, (_, i) => kw(`k${i}`, 30 - i, 0));
    const out = pickBuildItems(RUN, { ...empty, keywords: [kw('draw for kids', 50, 50, 'seed'), ...many] });
    const kws = out.filter((t) => t.kind === 'keyword');
    expect(kws).toHaveLength(BUILD_LIMITS.keyword);
    expect(kws[0]).toMatchObject({ term: 'draw for kids', country: 'US', runId: 7 });
    expect(kws[1].term).toBe('k29');
  });
  it('không có dòng seed vẫn thêm keyword gốc', () => {
    expect(pickBuildItems(RUN, empty)[0]).toMatchObject({ kind: 'keyword', term: 'draw for kids' });
  });
  it('đối thủ: nhiều rating nhất, cả 2 store, ref = url như nút Collect', () => {
    const apps = [app('a', 10), app('b', null), app('c', 999, 'appstore'), ...Array.from({ length: 12 }, (_, i) => app(`z${i}`, 100 + i))];
    const comp = pickBuildItems(RUN, { ...empty, competitors: apps }).filter((t) => t.kind === 'competitor');
    expect(comp).toHaveLength(BUILD_LIMITS.competitor);
    expect(comp[0]).toMatchObject({ term: 'c', ref: 'https://x/c', sourceUrl: 'https://x/c' });
    expect(comp.some((t) => t.term === 'b')).toBe(false);
  });
  it('lời chê: số review × độ nặng; ref như ComplaintsBlock', () => {
    const out = pickBuildItems(RUN, { ...empty, complaints: [complaint('slow', 5), complaint('crash', 3, 3), complaint('ads', 4)] });
    const c = out.filter((t) => t.kind === 'complaint');
    expect(c.map((t) => t.ref)).toEqual(['draw for kids::c:crash', 'draw for kids::c:slow', 'draw for kids::c:ads']);
  });
  it('khoảng trống: gap trước positioning, ít app có trước; bỏ unsure / null; tối đa 5', () => {
    const rows = [gapRow('p1', 'positioning', 0), gapRow('g2', 'gap', 2), gapRow('u', 'unsure', 0), gapRow('n', null, 0), gapRow('g1', 'gap', 1),
      gapRow('g3', 'gap', 3), gapRow('g4', 'gap', 4), gapRow('g5', 'gap', 5)];
    const g = pickBuildItems(RUN, { ...empty, gapRows: rows, gapApps: 10 }).filter((t) => t.kind === 'gap');
    expect(g.map((t) => t.ref)).toEqual(['draw for kids::g1', 'draw for kids::g2', 'draw for kids::g3', 'draw for kids::g4', 'draw for kids::g5']);
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ**

Run: `cd web && npx vitest run tests/build-start.test.ts`
Expected: FAIL — `Cannot find module '@/lib/build-start'`

- [ ] **Step 3: Viết code**

```ts
// web/src/lib/build-start.ts
import type { Complaint } from './complaints';
import type { GapRowView } from './feature-gap';
import type { CompetitorRow, KeywordRow } from './run-view';

/**
 * Nút "Bắt đầu build" (Plan 2 · mục 13): chọn đồ gom từ 1 lượt Research.
 * Keyword: gốc trước, rồi ít đối thủ nhất · Đối thủ: nhiều rating nhất · Lời chê: số review × độ nặng ·
 * Khoảng trống: `gap` rồi `positioning`, ít app có trước. Target giống hệt nút + Collect (cùng `ref`) để gom tay sau không trùng.
 */
export const BUILD_LIMITS = { keyword: 20, competitor: 10, complaint: 8, gap: 5 } as const;
export type BuildRun = { id: number; seed: string; country: string };
export type BuildInputs = { keywords: KeywordRow[]; competitors: CompetitorRow[]; complaints: Complaint[]; gapRows: GapRowView[]; gapApps: number };

export function pickBuildItems(run: BuildRun, inp: BuildInputs): Record<string, unknown>[] {
  const base = { country: run.country, runId: run.id };
  const seedLower = run.seed.trim().toLowerCase();
  const others = inp.keywords
    .filter((k) => k.origin !== 'seed' && k.term.trim().toLowerCase() !== seedLower)
    .sort((a, b) => a.playCount + a.appstoreCount - (b.playCount + b.appstoreCount));
  const keywords = [run.seed, ...others.map((k) => k.term)].slice(0, BUILD_LIMITS.keyword)
    .map((term) => ({ kind: 'keyword', term, ...base }));

  const seen = new Set<string>();
  const competitors = [...inp.competitors]
    .sort((a, b) => (b.ratingsCount ?? 0) - (a.ratingsCount ?? 0))
    .filter((a) => (seen.has(a.url) ? false : (seen.add(a.url), true)))
    .slice(0, BUILD_LIMITS.competitor)
    .map((a) => ({
      kind: 'competitor', term: a.title, ref: a.url, sourceUrl: a.url, ...base,
      snapshot: { store: a.store, developer: a.developer, rating: a.rating, ratingsCount: a.ratingsCount, installsMin: a.installsMin, price: a.price, updatedAt: a.updatedAt },
    }));

  const complaints = [...inp.complaints]
    .sort((a, b) => b.count * b.severity.weight - a.count * a.severity.weight)
    .slice(0, BUILD_LIMITS.complaint)
    .map((c) => ({
      kind: 'complaint', term: `“${c.phrase}” — ${run.seed}`, ref: `${run.seed}::c:${c.key}`, ...base,
      snapshot: { phrase: c.phrase, type: c.typeLabel, reviews: c.count, apps: c.apps.length, quotes: c.quotes.slice(0, 3).map((q) => `${q.text} — ${q.app}`) },
    }));

  const order = { gap: 0, positioning: 1 } as const;
  const gaps = inp.gapRows
    .filter((r): r is GapRowView & { gap: 'gap' | 'positioning' } => r.gap === 'gap' || r.gap === 'positioning')
    .sort((a, b) => order[a.gap] - order[b.gap] || a.have - b.have)
    .slice(0, BUILD_LIMITS.gap)
    .map((r) => ({
      kind: 'gap', term: `${r.label} — ${run.seed}`, ref: `${run.seed}::${r.key}`, ...base,
      snapshot: { feature: r.label, have: r.have, apps: inp.gapApps, unknown: r.unknown, gap: r.gap },
    }));

  return [...keywords, ...competitors, ...complaints, ...gaps];
}
```

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `cd web && npx vitest run tests/build-start.test.ts`
Expected: PASS (6 test). Nếu `GapRowView['gap']` có giá trị khác `'gap' | 'positioning' | 'unsure' | null`, sửa test theo kiểu thật trong `web/src/lib/feature-gap.ts:137`.

- [ ] **Step 5: Commit**

```bash
git add web/src/lib/build-start.ts web/tests/build-start.test.ts
git commit -m "feat(web): pick keywords, competitors, complaints and gaps for a build project"
```

---

### Task 3: `buildFromRun` — tạo / mở project build và gom

**Files:**
- Modify: `web/src/lib/build-start.ts`
- Test: `web/tests/build-start.test.ts`

**Interfaces:**
- Consumes: `huntFromRun(db, runId)` (`@/lib/hunt`), `addItems`, `getProject`, `updateProject`, `log`, `ProjectError` (`@/lib/projects`), `getRunView` (`@/lib/run-view`), `cachedReviews`, `complaintReport` (`@/lib/complaint-report`), `gapMatrix` (`@/lib/gap`).
- Produces:
```ts
export const BUILD_LOG = 'bắt đầu build';
export type BuildResult = { id: number; reused: boolean; added: number[]; counts: Record<'keyword' | 'competitor' | 'complaint' | 'gap', number> };
export async function gatherBuildInputs(db: Db, view: RunView): Promise<BuildInputs>;
export async function buildFromRun(db: Db, runId: number, gather?: (db: Db, view: RunView) => Promise<BuildInputs>): Promise<BuildResult>;
export function buildRunOf(db: Db, runId: number): number | null; // id project build của lượt Research này (chưa lưu trữ), không có → null
```

Hành vi:
1. `huntFromRun` (tự kiểm "chưa tra xong" / "không có dữ liệu" / 404, tự trả phiên cũ).
2. Project đã có log `BUILD_LOG` → trả `{ id, reused: true, added: [], counts: 0 hết }`, không gom lại.
3. Gom bằng `addItems(db, id, targets)`; đối thủ mới thêm đổi `status = 'ứng viên'` (bước 2 tab Build: anh đổi thành **giữ** = chọn để bắt chước).
4. `updateProject(db, id, { status: 'đang build' })`, `log(db, id, BUILD_LOG, { by: 'Bạn', runId, ids: added })`.
5. `gatherBuildInputs`: lời chê từ `complaintReport(db, view, cachedReviews(db, view))`; khoảng trống từ `gapMatrix` với fetcher **ném lỗi** (`offline`) → chỉ dùng cache 7 ngày, app chưa cache thành cột `?`. Không gọi mạng.

- [ ] **Step 1: Viết test đỏ**

```ts
// thêm vào web/tests/build-start.test.ts
import { projectItems, runs, sourceJobs } from '@/db/schema';
import { eq } from 'drizzle-orm';
import type { Db } from '@/db/client';
import { BUILD_LOG, buildFromRun, buildRunOf } from '@/lib/build-start';
import { undoItems } from '@/lib/projects';

function doneRun(db: Db, seed: string, status: 'done' | 'running' = 'done') {
  const runId = db.insert(runs).values({ seed, country: 'US', createdAt: new Date().toISOString() }).returning().get().id;
  for (const source of ['playstore', 'appstore', 'trends'] as const) db.insert(sourceJobs).values({ runId, source, status }).run();
  return runId;
}
const fake = (inp: Partial<BuildInputs>) => async () => ({ ...empty, ...inp });

describe('buildFromRun', () => {
  it('tạo project đang build, gom đủ, đối thủ là ứng viên', async () => {
    const db = createDb(':memory:');
    const runId = doneRun(db, 'draw for kids');
    const r = await buildFromRun(db, runId, fake({ keywords: [kw('kids drawing', 1, 1)], competitors: [app('A', 5), app('B', 9)], complaints: [complaint('slow', 4)], gapRows: [gapRow('g1', 'gap', 0)], gapApps: 4 }));
    expect(r.reused).toBe(false);
    expect(r.counts).toEqual({ keyword: 2, competitor: 2, complaint: 1, gap: 1 });
    const p = getProject(db, r.id);
    expect(p.status).toBe('đang build');
    expect(p.all.filter((i) => i.kind === 'competitor').every((i) => i.status === 'ứng viên')).toBe(true);
    expect(p.log.some((l) => l.kind === BUILD_LOG)).toBe(true);
    expect(buildRunOf(db, runId)).toBe(r.id);
  });
  it('bấm lần 2 → mở lại, không gom thêm', async () => {
    const db = createDb(':memory:');
    const runId = doneRun(db, 'draw for kids');
    const a = await buildFromRun(db, runId, fake({ competitors: [app('A', 5)] }));
    const b = await buildFromRun(db, runId, fake({ competitors: [app('A', 5), app('C', 1)] }));
    expect(b).toMatchObject({ id: a.id, reused: true, added: [] });
    expect(db.select().from(projectItems).where(eq(projectItems.projectId, a.id)).all()).toHaveLength(2);
  });
  it('Hoàn tác xoá đúng đồ vừa gom (giữ keyword gốc của phiên)', async () => {
    const db = createDb(':memory:');
    const r = await buildFromRun(db, doneRun(db, 'draw for kids'), fake({ competitors: [app('A', 5)] }));
    undoItems(db, r.id, r.added);
    expect(getProject(db, r.id).all.map((i) => i.kind)).toEqual(['keyword']);
  });
  it('chưa tra xong → từ chối', async () => {
    const db = createDb(':memory:');
    await expect(buildFromRun(db, doneRun(db, 'x', 'running'), fake({}))).rejects.toThrow(/chưa tra xong/);
  });
  it('gatherBuildInputs mặc định không gọi mạng (run không có app → rỗng)', async () => {
    const db = createDb(':memory:');
    const r = await buildFromRun(db, doneRun(db, 'offline test'));
    expect(r.counts).toEqual({ keyword: 1, competitor: 0, complaint: 0, gap: 0 });
  });
});
```

Ghi chú: `huntFromRun` đã thêm keyword gốc (trạng thái `giữ`); `addItems` gặp trùng thì không thêm dòng mới → keyword gốc **không** nằm trong `added`, nên Hoàn tác giữ lại nó. `counts.keyword` đếm cả dòng trùng (đồ có trong project sau khi gom).

- [ ] **Step 2: Chạy, thấy đỏ**

Run: `cd web && npx vitest run tests/build-start.test.ts`
Expected: FAIL — `buildFromRun is not exported`

- [ ] **Step 3: Viết code** (nối vào cuối `web/src/lib/build-start.ts`, thêm import lên đầu file)

```ts
import { and, eq, isNull } from 'drizzle-orm';
import type { Db } from '@/db/client';
import { projectItems, projectLog, projects } from '@/db/schema';
import { cachedReviews, complaintReport } from './complaint-report';
import { gapMatrix } from './gap';
import { huntFromRun } from './hunt';
import { addItems, getProject, log, updateProject } from './projects';
import { getRunView, type RunView } from './run-view';
import { tr } from '@/lib/i18n';

export const BUILD_LOG = 'bắt đầu build';
type Kind = 'keyword' | 'competitor' | 'complaint' | 'gap';
export type BuildResult = { id: number; reused: boolean; added: number[]; counts: Record<Kind, number> };
const ZERO: Record<Kind, number> = { keyword: 0, competitor: 0, complaint: 0, gap: 0 };
const offline = async (): Promise<never> => { throw new Error('offline'); };

/** Chỉ đọc cache (review 1–3★, mô tả store, IAP) — bấm nút không gọi mạng, không chờ. */
export async function gatherBuildInputs(db: Db, view: RunView): Promise<BuildInputs> {
  const complaints = complaintReport(db, view, cachedReviews(db, view)).complaints;
  const { matrix } = await gapMatrix(db, view, AbortSignal.timeout(5_000), { listing: offline, iap: offline });
  // 0 app → mọi hàng thành "không ai quảng cáo" (positioning) giả → bỏ hết
  const gapRows = matrix.apps.length ? matrix.rows : [];
  return { keywords: view.keywords, competitors: view.competitors, complaints, gapRows, gapApps: matrix.apps.length };
}

/** Project build của 1 lượt Research (chưa lưu trữ) — để nút đổi thành "Mở project build". */
export function buildRunOf(db: Db, runId: number): number | null {
  const rows = db.select({ id: projects.id, detail: projectLog.detail }).from(projectLog).innerJoin(projects, eq(projects.id, projectLog.projectId))
    .where(and(eq(projectLog.kind, BUILD_LOG), isNull(projects.archivedAt))).all();
  return rows.find((r) => (r.detail as { runId?: number }).runId === runId)?.id ?? null;
}

export async function buildFromRun(db: Db, runId: number, gather: (db: Db, view: RunView) => Promise<BuildInputs> = gatherBuildInputs): Promise<BuildResult> {
  const { id } = huntFromRun(db, runId);
  if (getProject(db, id).log.some((l) => l.kind === BUILD_LOG)) return { id, reused: true, added: [], counts: { ...ZERO } };
  const view = getRunView(db, runId);
  if (!view) throw new Error(tr('Không tìm thấy lượt Research này'));
  const targets = pickBuildItems(view.run, await gather(db, view));
  const { added, existing } = addItems(db, id, targets);
  const counts = { ...ZERO };
  for (const i of [...added, ...existing]) if (i.kind in counts) counts[i.kind as Kind] += 1;
  const newComp = added.filter((i) => i.kind === 'competitor').map((i) => i.id);
  for (const itemId of newComp) db.update(projectItems).set({ status: 'ứng viên' }).where(eq(projectItems.id, itemId)).run();
  updateProject(db, id, { status: 'đang build' });
  log(db, id, BUILD_LOG, { by: 'Bạn', runId, ids: added.map((i) => i.id) });
  return { id, reused: false, added: added.map((i) => i.id), counts };
}
```

Kiểm 2 điều trước khi chạy:
- `getProject(db, id).log` có `kind` (đã có: `ProjectView.log: LogRow[]`).
- `huntFromRun` ném `ProjectError` với chữ "chưa tra xong" (đã có ở `web/src/lib/hunt.ts:91`).
- `tr('Không tìm thấy lượt Research này')` đã có bản tiếng Anh (dùng ở `hunt.ts:89`).

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `cd web && npx vitest run tests/build-start.test.ts tests/hunt-autopilot.test.ts`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add web/src/lib/build-start.ts web/tests/build-start.test.ts
git commit -m "feat(web): start a build project from a research run with cached data only"
```

---

### Task 4: API — `POST /api/build/from-run`, gộp nút Brief + Spec + Plan

**Files:**
- Modify: `web/src/server/app.ts` (gần các route `/projects`, ~dòng 920)
- Modify: `web/src/server/hunt-api.ts:76-84`
- Test: `web/tests/build-start.test.ts`

**Interfaces:**
- Consumes: `buildFromRun`, `buildRunOf` (Task 3).
- Produces:
  - `POST /api/build/from-run` body `{ runId }` → `BuildResult` (200) · 400 chưa tra xong · 404 không có.
  - `GET /api/build/of-run/:runId` → `{ id: number | null }`.
  - `POST /api/hunt/from-run` (nút Brief + Spec + Plan cũ) → vẫn `{ id }`, nhưng đi qua `buildFromRun` nên project cũng được gom + `đang build`.

- [ ] **Step 1: Viết test đỏ**

```ts
// thêm vào web/tests/build-start.test.ts
import { createApi } from '@/server/app';
import type { ResearchDeps } from '@/lib/run-research';

describe('API build', () => {
  const setup = () => {
    const noop = async () => {};
    const deps: ResearchDeps = { db: createDb(':memory:'), suggest: async () => [], collectors: { playstore: noop, appstore: noop, trends: noop } };
    const app = createApi(() => deps);
    const call = (method: string, path: string, body?: unknown) => app.request(path, { method, headers: { host: '127.0.0.1:3200', 'content-type': 'application/json' }, body: body === undefined ? undefined : JSON.stringify(body) });
    return { db: deps.db, call };
  };
  it('from-run tạo project; of-run trả đúng id; gọi lại reused', async () => {
    const { db, call } = setup();
    const runId = doneRun(db, 'draw for kids');
    expect(await (await call('GET', `/api/build/of-run/${runId}`)).json()).toEqual({ id: null });
    const a = await (await call('POST', '/api/build/from-run', { runId })).json();
    expect(a).toMatchObject({ reused: false, counts: { keyword: 1 } });
    expect(await (await call('GET', `/api/build/of-run/${runId}`)).json()).toEqual({ id: a.id });
    expect(await (await call('POST', '/api/build/from-run', { runId })).json()).toMatchObject({ id: a.id, reused: true });
  });
  it('lỗi rõ: chưa tra xong 400, không có 404, runId sai 400', async () => {
    const { db, call } = setup();
    expect((await call('POST', '/api/build/from-run', { runId: doneRun(db, 'x', 'running') })).status).toBe(400);
    expect((await call('POST', '/api/build/from-run', { runId: 99999 })).status).toBe(404);
    expect((await call('POST', '/api/build/from-run', { runId: 'abc' })).status).toBe(400);
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ**

Run: `cd web && npx vitest run tests/build-start.test.ts`
Expected: FAIL — status 404 ở `/api/build/of-run/…`

- [ ] **Step 3: Viết code**

`web/src/server/app.ts` — import cạnh các import `@/lib/projects`:
```ts
import { buildFromRun, buildRunOf } from '@/lib/build-start';
```
Thêm ngay sau dòng `api.post('/projects/:id/items', …)` (giữ nhóm route project):
```ts
  // Plan 2 · mục 13: nút Bắt đầu build trên trang Research — không gọi AI, không gọi mạng, Free dùng được
  api.get('/build/of-run/:runId', (c) => projectCall(c, false, () => ({ id: buildRunOf(db(), projectId(c.req.param('runId'))) })));
  api.post('/build/from-run', (c) => projectCall(c, true, (b) => { projectRoom(); return buildFromRun(db(), projectId(String(b.runId))); }));
```
(`projectId` ném `ProjectError(400)` khi không phải số nguyên dương; `projectCall` đổi `ProjectError` thành mã lỗi đúng. Đọc `projectId` + `projectRoom` ở `app.ts` trước khi dùng để chắc chữ ký; `projectRoom()` là giới hạn số project của bản Free — nếu nó chặn Free tạo project thứ N thì giữ nguyên luật đó.)

`web/src/server/hunt-api.ts:76-84` — đổi thân route:
```ts
  api.post('/from-run', (c) => call(c, true, async (b) => {
    const runId = idOf(String(b.runId));
    needPro();
    const busy = auto.running();
    if (busy !== null) throw new ProjectError(tr(AUTO_BUSY), 409);
    const { id } = await buildFromRun(o.db(), runId);
    auto.start(id, { until: 'plan', from: 'brief' });
    return { id };
  }));
```
và import `import { buildFromRun } from '@/lib/build-start';` (bỏ `huntFromRun` khỏi import nếu không còn dùng).

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `cd web && npx vitest run tests/build-start.test.ts tests/hunt-autopilot.test.ts tests/hunt.test.ts tests/collect.test.ts`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add web/src/server/app.ts web/src/server/hunt-api.ts web/tests/build-start.test.ts
git commit -m "feat(web): add build from-run api and route plan docs button through it"
```

---

### Task 5: Bộ build — `saveBuildKit` + `POST /api/projects/:id/build-kit`

**Files:**
- Create: `web/src/lib/export/build-kit.ts`
- Modify: `web/src/server/app.ts` (cạnh `/projects/:id/docs/save`, ~dòng 1032)
- Test: `web/tests/build-kit.test.ts`

**Interfaces:**
- Consumes: `saveHuntDocs`, `DocError` (`@/lib/export/hunt-docs`), `keywordsCsv`, `competitorsCsv`, `fileSlug` (`@/lib/project-files`), `getProject` (`@/lib/projects`).
- Produces:
```ts
export function complaintsMd(view: ProjectView): string;
export function startMd(name: string, docs: string[]): string;
export function saveBuildKit(db: Db, projectId: number, aiDir: string, now?: Date): { dir: string; files: string[]; missingDocs: boolean };
```
- Route: `POST /api/projects/:id/build-kit` → `{ dir, files, missingDocs }` (không khoá PRO).

Nội dung `START.md` (tiếng Việt, cố định — AI đọc được cả tiếng Việt):
```md
# Bắt đầu build — <tên project>

Thư mục này do ShotMatic xuất. Đọc theo thứ tự:

1. brief.md — khách là ai, vấn đề, vì sao làm
2. spec.md — tính năng MVP (chỉ làm đúng những gì ghi ở đây)
3. plan.md — các bước làm
4. competitors.csv — đối thủ (cột trạng thái "giữ" = app chọn để bắt chước)
5. complaints.md — lời chê của người dùng đối thủ + khoảng trống tính năng
6. keywords.csv — keyword cho tên app / mô tả store

Việc của bạn: dựng MVP theo plan.md. Không thêm tính năng ngoài spec.md. Số liệu trong các file có nguồn; không tự bịa số.
```
Thiếu `brief.md`/`spec.md`/`plan.md` → bỏ dòng đó và thêm dòng `> Chưa có Brief / Spec / Plan — viết ở tab Build trong ShotMatic rồi xuất lại.`

- [ ] **Step 1: Viết test đỏ**

```ts
// web/tests/build-kit.test.ts
import { existsSync, mkdtempSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { createDb } from '@/db/client';
import { addItems, createProject, getProject, log } from '@/lib/projects';
import { complaintsMd, saveBuildKit, startMd } from '@/lib/export/build-kit';

function setup() {
  const db = createDb(':memory:');
  const p = createProject(db, 'draw for kids');
  addItems(db, p.id, [
    { kind: 'keyword', term: 'draw for kids', country: 'US' },
    { kind: 'competitor', term: 'Kids Color', ref: 'https://play/x', country: 'US', sourceUrl: 'https://play/x' },
    { kind: 'complaint', term: '“too many ads” — draw for kids', ref: 'draw for kids::c:ads', country: 'US', snapshot: { phrase: 'too many ads', reviews: 12, quotes: ['ads every 10s — Kids Color'] } },
    { kind: 'gap', term: 'Offline mode — draw for kids', ref: 'draw for kids::offline', country: 'US', snapshot: { feature: 'Offline mode', have: 1, apps: 8 } },
  ]);
  return { db, id: p.id, dir: mkdtempSync(join(tmpdir(), 'kit-')) };
}

describe('bộ build', () => {
  it('chưa có tài liệu: vẫn ghi CSV + complaints.md + START.md, báo thiếu', () => {
    const { db, id, dir } = setup();
    const r = saveBuildKit(db, id, dir);
    expect(r.missingDocs).toBe(true);
    for (const f of ['keywords.csv', 'competitors.csv', 'complaints.md', 'START.md']) expect(existsSync(join(r.dir, f))).toBe(true);
    expect(readFileSync(join(r.dir, 'START.md'), 'utf8')).toMatch(/Chưa có Brief \/ Spec \/ Plan/);
  });
  it('có Brief: ghi brief.md, START.md trỏ tới nó', () => {
    const { db, id, dir } = setup();
    log(db, id, 'AI ghi chú', { by: 'AI · Claude Code', text: 'BRIEF: ## Vấn đề\nTrẻ muốn vẽ' });
    const r = saveBuildKit(db, id, dir);
    expect(r.missingDocs).toBe(false);
    expect(existsSync(join(r.dir, 'brief.md'))).toBe(true);
    expect(readFileSync(join(r.dir, 'START.md'), 'utf8')).toMatch(/1\. brief\.md/);
  });
  it('complaints.md có lời chê + trích + khoảng trống', () => {
    const { db, id } = setup();
    const md = complaintsMd(getProject(db, id));
    expect(md).toMatch(/too many ads/);
    expect(md).toMatch(/12 review/);
    expect(md).toMatch(/ads every 10s — Kids Color/);
    expect(md).toMatch(/Offline mode · 1\/8 app có/);
  });
  it('startMd chỉ liệt kê tài liệu có thật', () => {
    expect(startMd('X', ['plan'])).not.toMatch(/brief\.md/);
    expect(startMd('X', ['plan'])).toMatch(/plan\.md/);
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ**

Run: `cd web && npx vitest run tests/build-kit.test.ts`
Expected: FAIL — `Cannot find module '@/lib/export/build-kit'`

- [ ] **Step 3: Viết code**

```ts
// web/src/lib/export/build-kit.ts
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import type { Db } from '@/db/client';
import { competitorsCsv, fileSlug, keywordsCsv } from '@/lib/project-files';
import { getProject, type ProjectView } from '@/lib/projects';
import { DocError, saveHuntDocs } from './hunt-docs';

/** Bộ build (Plan 2 · mục 13): Brief/Spec/Plan + CSV + lời chê + START.md trong `<thư mục AI>/briefs/<tên>/` cho Claude Code / Codex. */
const DOC_LINES: Record<string, string> = {
  brief: 'brief.md — khách là ai, vấn đề, vì sao làm',
  spec: 'spec.md — tính năng MVP (chỉ làm đúng những gì ghi ở đây)',
  plan: 'plan.md — các bước làm',
};
const DATA_LINES = [
  'competitors.csv — đối thủ (cột trạng thái "giữ" = app chọn để bắt chước)',
  'complaints.md — lời chê của người dùng đối thủ + khoảng trống tính năng',
  'keywords.csv — keyword cho tên app / mô tả store',
];

export function startMd(name: string, docs: string[]): string {
  const lines = [...(['brief', 'spec', 'plan'] as const).filter((d) => docs.includes(d)).map((d) => DOC_LINES[d]), ...DATA_LINES];
  const missing = docs.length < 3 ? '\n> Chưa có Brief / Spec / Plan — viết ở tab Build trong ShotMatic rồi xuất lại.\n' : '';
  return `# Bắt đầu build — ${name}\n\nThư mục này do ShotMatic xuất. Đọc theo thứ tự:\n\n${lines.map((l, i) => `${i + 1}. ${l}`).join('\n')}\n${missing}
Việc của bạn: dựng MVP theo plan.md. Không thêm tính năng ngoài spec.md. Số liệu trong các file có nguồn; không tự bịa số.\n`;
}

type Snap = { phrase?: string; reviews?: number; quotes?: string[]; feature?: string; have?: number; apps?: number };
export function complaintsMd(view: ProjectView): string {
  const live = view.all.filter((i) => i.status !== 'loại');
  const complaints = live.filter((i) => i.kind === 'complaint').map((i) => {
    const s = (i.snapshot ?? {}) as Snap;
    const quotes = (s.quotes ?? []).map((q) => `  - > ${q}`).join('\n');
    return `- **${s.phrase ?? i.term}** · ${s.reviews ?? '?'} review${quotes ? `\n${quotes}` : ''}`;
  });
  const gaps = live.filter((i) => i.kind === 'gap').map((i) => {
    const s = (i.snapshot ?? {}) as Snap;
    return `- ${s.feature ?? i.term} · ${s.have ?? '?'}/${s.apps ?? '?'} app có`;
  });
  return `# Lời chê + khoảng trống — ${view.name}\n\n## Lời chê (review 1–3★ của đối thủ)\n\n${complaints.join('\n') || '_Chưa gom lời chê._'}\n
## Khoảng trống tính năng\n\n${gaps.join('\n') || '_Chưa gom khoảng trống._'}\n`;
}

export function saveBuildKit(db: Db, projectId: number, aiDir: string, now = new Date()): { dir: string; files: string[]; missingDocs: boolean } {
  const view = getProject(db, projectId);
  const dir = join(aiDir, 'briefs', fileSlug(view.name));
  let docFiles: string[] = [];
  try { docFiles = saveHuntDocs(db, projectId, aiDir, now).files; } catch (e) { if (!(e instanceof DocError)) throw e; }
  mkdirSync(dir, { recursive: true });
  const docs = (['brief', 'spec', 'plan'] as const).filter((d) => existsSync(join(dir, `${d}.md`)) && docFiles.some((f) => f.endsWith(`${d}.md`)));
  const out: [string, string][] = [
    ['keywords.csv', keywordsCsv(db, projectId)],
    ['competitors.csv', competitorsCsv(db, projectId)],
    ['complaints.md', complaintsMd(view)],
    ['START.md', startMd(view.name, docs)],
  ];
  for (const [f, body] of out) writeFileSync(join(dir, f), body);
  return { dir, files: [...docFiles, ...out.map(([f]) => join(dir, f))], missingDocs: docs.length < 3 };
}
```

`web/src/server/app.ts` — import `import { saveBuildKit } from '@/lib/export/build-kit';`, thêm ngay sau route `/projects/:id/docs/save`:
```ts
  // Plan 2 · mục 13: xuất bộ build (Brief/Spec/Plan + CSV + lời chê + START.md) vào thư mục AI — không khoá PRO
  api.post('/projects/:id/build-kit', (c) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    return projectFile(c, (id) => Response.json(saveBuildKit(db(), id, chat?.dir ?? aiDir())), false);
  });
```

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `cd web && npx vitest run tests/build-kit.test.ts tests/hunt-docs.test.ts tests/export.test.ts`
Expected: PASS. Nếu `competitorsCsv` chưa có cột trạng thái item, thêm cột `trạng thái` (giá trị `i.status`) vào cuối và sửa test `export.test.ts` tương ứng — START.md dựa vào cột này.

- [ ] **Step 5: Commit**

```bash
git add web/src/lib/export/build-kit.ts web/src/server/app.ts web/tests/build-kit.test.ts
git commit -m "feat(web): export build kit with docs, csv, complaints and START.md"
```

---

### Task 6: Nút ▶ Bắt đầu build trên trang Research

**Files:**
- Create: `web/src/components/StartBuildButton.tsx`
- Modify: `web/src/components/RunHeader.tsx:122-131` (hàng nút đầu trang) và `:150-153` (thanh dính)
- Modify: `web/src/locales/en-text-build.ts`

**Interfaces:**
- Consumes: `GET /api/build/of-run/:runId`, `POST /api/build/from-run` (Task 4); `answer.decision` của `RunHeader` (`'BUILD' | 'TEST THÊM' | 'BỎ' | null`).
- Produces: `<StartBuildButton runId ready decision compact? />`; điều hướng tới `/projects/:id?tab=build&added=<ids>`.

Hành vi:
- `ready = false` (còn job chưa xong) → nút xám, chữ "Chờ tra xong".
- Đã có project build → nút viền "Mở project build" (link).
- `decision === 'BUILD'` → `variant="primary"`; khác → viền; bấm khi `TEST THÊM`/`BỎ` → `window.confirm(tr('Gợi ý đang là {d}, vẫn bắt đầu build?', { d }))`.
- `IS_DEMO` → không hiện.

- [ ] **Step 1: Viết component**

```tsx
// web/src/components/StartBuildButton.tsx
import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router';
import { Button } from './Button';
import { IS_DEMO } from '@/demo/demo-config';
import { tr } from '@/lib/i18n';

/** Nút "▶ Bắt đầu build" (Plan 2 · mục 13): tạo / mở project build của lượt Research này. Không gọi AI. */
export function StartBuildButton({ runId, ready, decision, compact = false }: { runId: number; ready: boolean; decision: string | null; compact?: boolean }) {
  const nav = useNavigate();
  const [have, setHave] = useState<number | null | undefined>(undefined);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    let on = true;
    fetch(`/api/build/of-run/${runId}`).then((r) => r.json()).then((j: { id: number | null }) => { if (on) setHave(j.id); }, () => { if (on) setHave(null); });
    return () => { on = false; };
  }, [runId]);
  if (IS_DEMO) return null;
  const size = compact ? '!min-h-9 !py-1' : '!min-h-10';
  if (have) return <Link to={`/projects/${have}?tab=build`} className={`ui-button ui-button--secondary shrink-0 ${size}`}>{tr('Mở project build')}</Link>;
  const go = async () => {
    if (decision && decision !== 'BUILD' && !window.confirm(tr('Gợi ý đang là {d}, vẫn bắt đầu build?', { d: tr(decision) }))) return;
    setBusy(true);
    setError(null);
    try {
      const res = await fetch('/api/build/from-run', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ runId }) });
      const j = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(j.error || tr('Lỗi {n}', { n: res.status }));
      nav(`/projects/${j.id}?tab=build${j.added?.length ? `&added=${j.added.join(',')}` : ''}`);
    } catch (e) {
      setError((e as Error).message);
      setBusy(false);
    }
  };
  return (
    <>
      <Button variant={decision === 'BUILD' ? 'primary' : undefined} loading={busy} disabled={!ready || have === undefined} className={`shrink-0 ${size}`}
        title={ready ? tr('Tạo project, gom sẵn keyword · đối thủ · lời chê · khoảng trống') : tr('Chờ tra xong')} onClick={() => void go()}>
        {ready ? tr('▶ Bắt đầu build') : tr('Chờ tra xong')}
      </Button>
      {error && <span role="alert" className="text-sm text-rose-600">{error}</span>}
    </>
  );
}
```

Trước khi dùng: mở `web/src/components/Button.tsx` xem tên `variant` thật (nếu không có `'primary'`, dùng variant chính đang dùng cho nút màu chính, vd `'solid'`).

- [ ] **Step 2: Gắn vào RunHeader**

Trong hàng nút đầu trang (`<div className="ml-auto flex flex-wrap items-center gap-3">`), đặt **trước** nút "Chấm điểm":
```tsx
<StartBuildButton runId={view.run.id} ready={!view.jobs.some((j) => j.status === 'pending' || j.status === 'running')} decision={free ? null : answer?.decision ?? null} />
```
Trong thanh dính (`<div className="ml-auto flex shrink-0 items-center gap-2">`), đặt trước nút "Chấm điểm":
```tsx
<StartBuildButton compact runId={view.run.id} ready={!view.jobs.some((j) => j.status === 'pending' || j.status === 'running')} decision={free ? null : answer?.decision ?? null} />
```
Import `import { StartBuildButton } from './StartBuildButton';`.

- [ ] **Step 3: Thêm chữ tiếng Anh** vào `buildEnText`:
```ts
  'Mở project build': 'Open build project',
  'Gợi ý đang là {d}, vẫn bắt đầu build?': 'The suggestion is {d}. Start building anyway?',
  'Tạo project, gom sẵn keyword · đối thủ · lời chê · khoảng trống': 'Create a project with keywords · competitors · complaints · gaps already collected',
  '▶ Bắt đầu build': '▶ Start building',
  'Chờ tra xong': 'Wait for research to finish',
```
(`'Lỗi {n}'` đã có — kiểm bằng `grep -n "'Lỗi {n}'" web/src/locales/*.ts`.)

- [ ] **Step 4: Kiểm**

Run: `cd web && npx tsc --noEmit -p . && npx vitest run tests/i18n-text.test.ts`
Expected: không lỗi kiểu, PASS.

- [ ] **Step 5: Commit**

```bash
git add web/src/components/StartBuildButton.tsx web/src/components/RunHeader.tsx web/src/locales/en-text-build.ts
git commit -m "feat(web): add start building button to research header"
```

---

### Task 7: Tab Build trong project

**Files:**
- Create: `web/src/components/BuildTab.tsx`
- Modify: `web/src/client/ProjectPage.tsx:16-17` (kiểu Tab), `:26` (tab mặc định), `:150-158` (danh sách tab), thêm khối render
- Modify: `web/src/locales/en-text-build.ts`

**Interfaces:**
- Consumes: `ProjectView` (`view.all`, `view.kind`, `view.status`, `view.nextStep`, `view.nextDue`), `GET /api/projects/:id/docs` → `Record<'BRIEF'|'SPEC'|'PLAN', string|null>`, `POST /api/hunt/:id/autopilot/start { until: 'plan', from: 'brief' }`, `POST /api/projects/:id/build-kit`, `projectsApi.undo` (kiểm tên thật ở `web/src/lib/projects-client.ts`; route `POST /api/projects/:id/items/undo { ids }`).
- Produces: `<BuildTab view onTab onChange />`.

Bố cục (1 cột, 5 hàng `<ol>`; mỗi hàng: số tròn / ✓ · tiêu đề · 1 dòng phụ · nút bên phải `shrink-0`):
1. **Dữ liệu đã gom** — "20 keyword · 10 đối thủ · 8 lời chê · 5 khoảng trống" (mỗi số là nút sang tab tương ứng). ✓ khi tổng > 1.
2. **Đối thủ để bắt chước** — liệt kê tên đối thủ trạng thái `giữ` (truncate + title); chưa có → "Chọn 1–3 app: tab Đối thủ → đổi trạng thái thành giữ" + nút "Chọn đối thủ" (sang tab competitors). ✓ khi ≥ 1.
3. **Brief + Spec + Plan** — 3 chip BRIEF/SPEC/PLAN (xanh nếu có ngày). Nút "✦ Viết Brief + Spec + Plan" (gọi autopilot rồi `navigate('/hunt/:id')`) khi `view.kind === 'hunt'`; có đủ → nút "Xem trong phiên AI" (link `/hunt/:id`). Lỗi 402 → hiện link nâng PRO (`proHref('agent')`). ✓ khi đủ 3.
4. **Xuất bộ build** — nút "Xuất bộ build" → hiện đường dẫn thư mục (`wrap-anywhere`), nút "Copy lệnh" (copy `cd "<dir>" && claude`), dòng vàng nếu `missingDocs`. ✓ sau khi xuất trong phiên.
5. **Bước tiếp theo** — hiện `view.nextStep` + `view.nextDue`, chưa có → "Ghi ở tab Tổng quan" + nút sang overview.

Thanh báo đầu tab khi URL có `added=…`: "Đã gom {n} thứ vào project" + nút **Hoàn tác** (gọi undo với các id, rồi xoá `added` khỏi URL, `onChange()`).

- [ ] **Step 1: Viết `BuildTab.tsx`** theo bố cục trên. Dùng `bg-surface`, `zinc-*`, `min-w-0` cho cột chữ, `shrink-0` cho nút; không lưới nhiều cột.

```tsx
// web/src/components/BuildTab.tsx
import { useEffect, useState, type ReactNode } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router';
import { Button } from './Button';
import { tr } from '@/lib/i18n';
import { proHref } from '@/lib/pro-spots';
import type { ItemKind, ProjectView } from '@/lib/projects-client';

type Tab = 'overview' | 'keywords' | 'competitors' | 'complaints' | 'gaps';
type Docs = Record<'BRIEF' | 'SPEC' | 'PLAN', string | null>;
const post = (url: string, body: unknown = {}) => fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });

function Step({ n, done, title, sub, action }: { n: number; done: boolean; title: string; sub: ReactNode; action?: ReactNode }) {
  return (
    <li className="flex flex-wrap items-center gap-x-4 gap-y-2 py-4 first:pt-0 last:pb-0">
      <span className={`grid h-9 w-9 shrink-0 place-items-center rounded-full text-sm font-semibold ${done ? 'bg-emerald-100 text-emerald-700' : 'bg-zinc-100 text-zinc-600'}`} aria-hidden>{done ? '✓' : n}</span>
      <div className="min-w-0 flex-1 basis-60">
        <h3 className="text-base font-semibold">{title}</h3>
        <div className="text-sm text-zinc-500">{sub}</div>
      </div>
      {action && <div className="flex shrink-0 flex-wrap items-center gap-2">{action}</div>}
    </li>
  );
}

/** Tab Build (Plan 2 · mục 13): 5 bước từ dữ liệu đã gom tới bộ build cho Claude Code. */
export function BuildTab({ view, onTab, onChange }: { view: ProjectView; onTab: (t: Tab) => void; onChange: () => void }) {
  const nav = useNavigate();
  const [params, setParams] = useSearchParams();
  const added = (params.get('added') ?? '').split(',').map(Number).filter((x) => Number.isInteger(x) && x > 0);
  const [docs, setDocs] = useState<Docs | null>(null);
  const [kit, setKit] = useState<{ dir: string; missingDocs: boolean } | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<ReactNode>(null);
  const [copied, setCopied] = useState(false);
  useEffect(() => { fetch(`/api/projects/${view.id}/docs`).then((r) => (r.ok ? r.json() : null)).then(setDocs, () => setDocs(null)); }, [view.id]);

  const live = view.all.filter((i) => i.status !== 'loại');
  const n = (k: ItemKind[]) => live.filter((i) => k.includes(i.kind)).length;
  const picked = live.filter((i) => i.kind === 'competitor' && i.status === 'giữ');
  const docsDone = !!docs && !!docs.BRIEF && !!docs.SPEC && !!docs.PLAN;

  const run = async (key: string, fn: () => Promise<void>) => {
    setBusy(key); setError(null);
    try { await fn(); } catch (e) { setError((e as Error).message); }
    setBusy(null);
  };
  const undo = () => run('undo', async () => {
    const r = await post(`/api/projects/${view.id}/items/undo`, { ids: added });
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).error ?? tr('Lỗi {n}', { n: r.status }));
    params.delete('added'); setParams(params, { replace: true }); onChange();
  });
  const write = () => run('docs', async () => {
    const r = await post(`/api/hunt/${view.id}/autopilot/start`, { until: 'plan', from: 'brief' });
    if (r.status === 402) { setError(<Link className="underline" to={proHref('agent')}>{tr('Viết Brief + Spec + Plan cần PRO')}</Link>); return; }
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).error ?? tr('Lỗi {n}', { n: r.status }));
    nav(`/hunt/${view.id}`);
  });
  const exportKit = () => run('kit', async () => {
    const r = await post(`/api/projects/${view.id}/build-kit`);
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error ?? tr('Lỗi {n}', { n: r.status }));
    setKit({ dir: j.dir, missingDocs: j.missingDocs });
  });
  const copy = async (dir: string) => { await navigator.clipboard.writeText(`cd "${dir}" && claude`); setCopied(true); setTimeout(() => setCopied(false), 1500); };
  const num = (k: ItemKind[], label: string, t: Tab) => <button type="button" className="underline-offset-2 hover:underline" onClick={() => onTab(t)}>{tr(label, { n: n(k) })}</button>;

  return (
    <div className="space-y-4">
      {added.length > 0 && (
        <div className="flex flex-wrap items-center gap-3 rounded-xl border border-blue-200 bg-blue-50 px-4 py-3 text-sm text-blue-900">
          <span className="min-w-0 flex-1">{tr('Đã gom {n} thứ vào project', { n: added.length })}</span>
          <Button loading={busy === 'undo'} onClick={() => void undo()} className="shrink-0">{tr('Hoàn tác')}</Button>
        </div>
      )}
      {error && <p role="alert" className="text-sm text-rose-600">{error}</p>}
      <ol className="divide-y divide-zinc-100 rounded-2xl border border-zinc-200 bg-surface p-5">
        <Step n={1} done={live.length > 1} title={tr('Dữ liệu đã gom')}
          sub={<span className="flex flex-wrap gap-x-2">{num(['keyword', 'niche'], '{n} keyword', 'keywords')}·{num(['competitor'], '{n} đối thủ', 'competitors')}·{num(['complaint'], '{n} lời chê', 'complaints')}·{num(['gap'], '{n} khoảng trống', 'gaps')}</span>} />
        <Step n={2} done={picked.length > 0} title={tr('Đối thủ để bắt chước')}
          sub={picked.length ? <span className="block truncate" title={picked.map((i) => i.term).join(', ')}>{picked.map((i) => i.term).join(' · ')}</span> : tr('Chọn 1–3 app: tab Đối thủ → đổi trạng thái thành giữ')}
          action={<Button onClick={() => onTab('competitors')}>{picked.length ? tr('Đổi') : tr('Chọn đối thủ')}</Button>} />
        <Step n={3} done={docsDone} title="Brief + Spec + Plan"
          sub={<span className="flex flex-wrap gap-1.5">{(['BRIEF', 'SPEC', 'PLAN'] as const).map((d) => <span key={d} className={`rounded-md border px-1.5 py-0.5 font-mono text-xs ${docs?.[d] ? 'border-emerald-300 text-emerald-700' : 'border-zinc-300 text-zinc-500'}`}>{d}</span>)}</span>}
          action={view.kind === 'hunt' ? (docsDone
            ? <Link to={`/hunt/${view.id}`} className="ui-button ui-button--secondary">{tr('Xem trong phiên AI')}</Link>
            : <Button variant="ai" loading={busy === 'docs'} onClick={() => void write()}>{tr('✦ Viết Brief + Spec + Plan')}</Button>) : undefined} />
        <Step n={4} done={!!kit} title={tr('Xuất bộ build')}
          sub={kit ? <span className="block wrap-anywhere">{kit.dir}{kit.missingDocs && <span className="block text-amber-700">{tr('Chưa có đủ Brief / Spec / Plan — bộ build mới có CSV + lời chê')}</span>}</span> : tr('Ghi Brief / Spec / Plan + CSV + lời chê + START.md vào thư mục AI')}
          action={<>
            <Button loading={busy === 'kit'} onClick={() => void exportKit()}>{kit ? tr('Xuất lại') : tr('Xuất bộ build')}</Button>
            {kit && <Button onClick={() => void copy(kit.dir)}>{copied ? tr('Đã copy') : tr('Copy lệnh')}</Button>}
          </>} />
        <Step n={5} done={!!view.nextStep} title={tr('Bước tiếp theo')}
          sub={view.nextStep ? `${view.nextStep}${view.nextDue ? tr(' · hẹn {date}', { date: view.nextDue }) : ''}` : tr('Ghi ở tab Tổng quan')}
          action={<Button onClick={() => onTab('overview')}>{tr('Sửa')}</Button>} />
      </ol>
    </div>
  );
}
```

Trước khi dùng, kiểm 3 tên thật: `variant="ai"` của `Button` (đã dùng ở `PlanDocsButton.tsx`), `proHref('agent')` (đã dùng ở `PlanDocsButton.tsx`), `view.kind` có trong `ProjectView` (cột `kind` của bảng `projects`). Lớp `wrap-anywhere` đã dùng trong repo (luật Layout).

- [ ] **Step 2: Gắn vào ProjectPage**

```ts
type Tab = 'build' | 'overview' | 'keywords' | 'competitors' | 'complaints' | 'gaps' | 'tracking' | 'notes';
const TABS: Tab[] = ['build', 'overview', 'keywords', 'competitors', 'complaints', 'gaps', 'tracking', 'notes'];
```
Tab mặc định: `'build'` khi `view?.status === 'đang build'`, ngược lại `'overview'`:
```ts
const asked = params.get('tab') as Tab | null;
const tab = (asked && TABS.includes(asked) ? asked : view?.status === 'đang build' ? 'build' : 'overview') as Tab;
const setTab = (t: Tab) => setParams(t === 'overview' ? {} : { tab: t }, { replace: true });
```
(dời 2 dòng này xuống dưới chỗ khai báo `view`.) Trong `<Tabs items=…>` thêm đầu mảng khi `view.status === 'đang build' || tab === 'build'`:
```ts
...(view.status === 'đang build' || tab === 'build' ? [{ value: 'build' as const, label: tr('Build') }] : []),
```
và khối render:
```tsx
{tab === 'build' && <BuildTab view={view} onTab={setTab} onChange={() => void load()} />}
```

- [ ] **Step 3: Thêm chữ tiếng Anh** vào `buildEnText`:
```ts
  'Viết Brief + Spec + Plan cần PRO': 'Writing Brief + Spec + Plan needs PRO',
  'Đã gom {n} thứ vào project': 'Collected {n} items into the project',
  'Hoàn tác': 'Undo',
  'Dữ liệu đã gom': 'Collected data',
  '{n} keyword': '{n} keywords',
  '{n} đối thủ': '{n} competitors',
  '{n} lời chê': '{n} complaints',
  '{n} khoảng trống': '{n} gaps',
  'Đối thủ để bắt chước': 'Competitors to copy',
  'Chọn 1–3 app: tab Đối thủ → đổi trạng thái thành giữ': 'Pick 1–3 apps: Competitors tab → set status to keep',
  'Đổi': 'Change',
  'Chọn đối thủ': 'Pick competitors',
  'Xem trong phiên AI': 'Open in AI session',
  '✦ Viết Brief + Spec + Plan': '✦ Write Brief + Spec + Plan',
  'Xuất bộ build': 'Export build kit',
  'Chưa có đủ Brief / Spec / Plan — bộ build mới có CSV + lời chê': 'Brief / Spec / Plan not complete — the kit only has CSV + complaints',
  'Ghi Brief / Spec / Plan + CSV + lời chê + START.md vào thư mục AI': 'Writes Brief / Spec / Plan + CSV + complaints + START.md to the AI folder',
  'Xuất lại': 'Export again',
  'Đã copy': 'Copied',
  'Copy lệnh': 'Copy command',
  'Bước tiếp theo': 'Next step',
  'Ghi ở tab Tổng quan': 'Set it in the Overview tab',
  'Sửa': 'Edit',
  'Build': 'Build',
```
Chữ nào đã có sẵn trong file locale khác (vd `'Hoàn tác'`, `'Sửa'`, `' · hẹn {date}'`, `'Lỗi {n}'`) thì **bỏ** khỏi `buildEnText` để không trùng khoá — kiểm bằng `grep -rn "'Hoàn tác':" web/src/locales`.

- [ ] **Step 4: Kiểm**

Run: `cd web && npx tsc --noEmit -p . && npx vitest run tests/i18n-text.test.ts`
Expected: không lỗi, PASS.

- [ ] **Step 5: Commit**

```bash
git add web/src/components/BuildTab.tsx web/src/client/ProjectPage.tsx web/src/locales/en-text-build.ts
git commit -m "feat(web): add build tab with five steps to project page"
```

---

### Task 8: Chạy thật, soát layout, tài liệu

**Files:**
- Modify: `docs/web/phase-plan2-13-bat-dau-build.md` (chip trạng thái + mục "Chạy thật lần đầu" + sửa luật chọn keyword)
- Modify: `docs/web/index.md` (chip mục 13)
- Modify: `CHANGELOG.md` (1 dòng Web dưới `[Unreleased]`)

- [ ] **Step 1: Kiểm toàn repo**

Run: `npm run check` (ở gốc repo)
Expected: xanh hết.

- [ ] **Step 2: Chạy thật** — bật dev server (preview_start theo `.claude/launch.json`), tra "draw for kids" · US, chờ xong:
  - Bấm **▶ Bắt đầu build** → sang tab Build, thanh "Đã gom N thứ", số ở bước 1 khớp tab.
  - Quay lại Research → nút đã thành **Mở project build**.
  - Bấm Hoàn tác → còn đúng keyword gốc.
  - Bấm lại từ đầu trên 1 niche khác, đổi 2 đối thủ thành **giữ** → bước 2 ✓.
  - **Xuất bộ build** → mở thư mục, có `keywords.csv`, `competitors.csv`, `complaints.md`, `START.md`.

- [ ] **Step 3: Soát layout** — trang Research (đầu trang + thanh dính) và tab Build ở **960px** và **1340px**, sáng + tối, English + tiếng Việt, project tên dài (đặt tên ~80 ký tự): không cuộn ngang cả trang, nút không bị đẩy ra khỏi hàng. Screenshot và Read từng ảnh.

- [ ] **Step 4: Cập nhật tài liệu**
  - Spec: chip → `<span class="chip chip--done">Anh duyệt 2026-11-14 · đã code</span>`; sửa dòng Keyword trong bảng gom thành "keyword gốc + keyword gợi ý ít đối thủ nhất" (code dùng luật này vì trang Research không có bản đồ niche); bước 2 tab Build: "đổi trạng thái đối thủ thành **giữ** (đối thủ mới gom là **ứng viên**)" thay cho nút ☆; ghi đúng: lời chê / khoảng trống chỉ lấy từ cache (niche chưa mở khối Lời chê / Khoảng trống thì 0); thêm mục `## Chạy thật lần đầu (ngày)` với số đếm thật đo được ở Step 2.
  - `docs/web/index.md`: chip mục 13 → `chip--done` "Làm 2026-11-14 · đã code".
  - `CHANGELOG.md` dưới `[Unreleased]`: `- Web: nút ▶ Bắt đầu build trên trang Research → project đang build đã gom sẵn + tab Build 5 bước + xuất bộ build (START.md) cho Claude Code.`

Run: `npm run docs:build`
Expected: xanh.

- [ ] **Step 5: Commit**

```bash
git add docs/web/phase-plan2-13-bat-dau-build.md docs/web/index.md mkdocs.yml docs/superpowers/plans/2026-11-14-plan2-13-bat-dau-build.md
git commit -m "docs(web): mark start building as coded with first real run"
```
`CHANGELOG.md` đang có thay đổi của việc khác chưa commit → dùng `git add -p CHANGELOG.md` chỉ chọn dòng của mục này.
