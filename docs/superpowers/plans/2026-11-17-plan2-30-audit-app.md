# Audit 1 app (Plan 2 mục 30) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Thẻ thứ 7 "Audit app" ở trang App: dán link app đã có → chip keyword gợi ý (sửa được) → điểm /100 gồm 4 phần + bảng hạng keyword + 3–5 việc nên sửa → nút Lấy đối thủ đẩy app đã tick sang So sánh app.

**Architecture:** Một file thuần `lib/app-audit-core.ts` (rút keyword, chấm điểm, việc nên sửa, gộp đối thủ) có test đầy đủ. Một file đọc trang store `lib/app-audit-listing.ts` (phần parse thuần + phần fetch). Một file chạy `lib/app-audit.ts` (đo hạng 3 luồng, lưu bảng `app_audits`, gộp đối thủ, upsert app để có id cho So sánh app). API riêng `server/audit-api.ts` gắn ở `/api/audit`. Giao diện `client/AppAudit.tsx` + 2 file con, gắn vào `HomePage` như Đào review.

**Tech Stack:** TypeScript, Hono, drizzle-orm + better-sqlite3, google-play-scraper, iTunes Search/Lookup API, React + Tailwind v4, vitest.

**Spec:** [docs/web/phase-plan2-30-audit-app.md](../../web/phase-plan2-30-audit-app.md)

## Global Constraints

- Mọi lệnh chạy ở `web/` trừ `npm run check` và `npm run docs:build` (gốc repo).
- Chữ giao diện viết tiếng Việt trong `tr()` / `tx()`, bản tiếng Anh thêm vào `web/src/locales/en-text-app-audit.ts` và gộp vào `en-text.ts`.
- Không hiện số mục / số phase trên UI.
- 1 nước mỗi lần chạy, 17 nước của `COUNTRIES`. Tối đa **20 keyword** mỗi lần chạy, gợi ý **15 chip**.
- Đo hạng: **top 50**, tối đa **3 luồng**, gặp `RATE_LIMITED` chờ 3 giây thử lại **1 lần**, vẫn lỗi → keyword đó `measured: false` ("chưa đo"), **không** tính là ngoài top.
- Điểm: Tên & phụ đề **30** · Mô tả **15** · Hình ảnh & rating **20** · Hạng keyword **35**. Mục / phần chưa đo **bỏ khỏi mẫu số**, không cho 0.
- Giới hạn ký tự: App Store tên 30, phụ đề 30 · Play tên 30, mô tả ngắn 80.
- App Store: iTunes Lookup không trả phụ đề và video → `subtitle: null`, `hasVideo: null` (chưa đo). Không đọc trang apps.apple.com ở bản này.
- Hạng của audit lưu trong `app_audits.data` (JSON), **không** ghi vào `keyword_hits` (tránh tạo lượt Research giả). Spec đã sửa theo.
- Layout: trang 1 cột, đứng được từ 960px, bảng bọc `overflow-x-auto`, chữ dài `truncate` + `title`, thẻ dùng `bg-surface`, màu xám `zinc-*`.
- Commit chỉ khi anh Tu cho phép. Các bước "Commit" bên dưới là điểm dừng gợi ý.

---

## File Structure

| File | Làm gì |
|---|---|
| Create `web/src/lib/app-audit-core.ts` | Kiểu dữ liệu, rút keyword, gộp chip, chấm 4 phần, việc nên sửa, gộp + xếp đối thủ. Thuần, chạy được cả client. |
| Create `web/src/lib/app-audit-listing.ts` | `parsePlayListing` / `parseItunesListing` (thuần) + `fetchListing` (mạng). |
| Create `web/src/lib/app-audit.ts` | `searchTop`, `rankTerms`, `suggestChips`, `runAudit`, `auditRivals`, `listAudits`, `ensureAppIds`. |
| Modify `web/src/db/schema.ts` + migration mới ở `web/drizzle/` | Bảng `app_audits`. |
| Create `web/src/server/audit-api.ts` | `POST /read` · `POST /run` · `POST /rivals` · `GET /list`. |
| Modify `web/src/server/app.ts` | `api.route('/audit', auditApi({ db }))`. |
| Create `web/src/client/AppAudit.tsx` | Ô nhập, chip, chạy, mở lại lần cũ. |
| Create `web/src/client/AuditResult.tsx` | Số lớn, 4 thanh, việc nên sửa, bảng hạng. |
| Create `web/src/client/AuditRivals.tsx` | Lấy đối thủ, tick, đẩy sang So sánh app, ô dán tay App Store. |
| Modify `web/src/client/YoutubeEntry.tsx`, `HomePage.tsx`, `AppInspect.tsx` | Mode `audit`, thẻ thứ 7, "7 việc", nút Audit app này. |
| Create `web/src/locales/en-text-app-audit.ts`, modify `en-text.ts`, `en-text-review-mining.ts` | Chữ tiếng Anh. |
| Create `web/tests/app-audit.test.ts` | Test core, listing, run, API. |

---

### Task 1: Lõi thuần — kiểu, rút keyword, gộp chip

**Files:**
- Create: `web/src/lib/app-audit-core.ts`
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Produces:
  - `type AuditStore = 'play' | 'appstore'`
  - `type Listing = { store; id: string; country: string; title: string; subtitle: string | null; description: string | null; screenshots: number | null; hasVideo: boolean | null; rating: number | null; ratingsCount: number | null; updatedAt: string | null; iconUrl: string | null; url: string; developer: string }`
  - `type RivalHit = { store: AuditStore; id: string; title: string; developer: string; iconUrl: string | null; url: string; rating: number | null; ratingsCount: number | null }`
  - `type RankRow = { term: string; measured: boolean; rank: number | null; top: RivalHit[] }` — `rank: null` + `measured: true` = ngoài top 50; `top` = 10 app đầu.
  - `type ChipSource = 'name' | 'suggest' | 'rival'`; `type Chip = { term: string; source: ChipSource }`
  - `const TOP_DEPTH = 50`, `MAX_TERMS = 20`, `MAX_CHIPS = 15`, `LIMITS`
  - `tokens(s: string): string[]`, `ownPhrases(l: Listing, max?: number): string[]`, `mergeChips(groups: Chip[][], max?: number): Chip[]`, `inName(l: Listing, term: string): boolean`

- [ ] **Step 1: Viết test hỏng**

```ts
// web/tests/app-audit.test.ts
import { describe, expect, it } from 'vitest';
import { inName, mergeChips, ownPhrases, tokens, type Listing } from '@/lib/app-audit-core';

const listing = (o: Partial<Listing> = {}): Listing => ({
  store: 'play', id: 'com.habit.app', country: 'US', title: 'Habit Tracker: Daily Routine', subtitle: 'Build good habits, track goals and streaks',
  description: 'Habit tracker for daily routine.\nTrack goals.\nStay on streak.\n' + 'x'.repeat(1200), screenshots: 8, hasVideo: true,
  rating: 4.6, ratingsCount: 12000, updatedAt: '2026-11-01T00:00:00.000Z', iconUrl: null, url: 'https://play.google.com/store/apps/details?id=com.habit.app',
  developer: 'Lumen Labs', ...o,
});

describe('tokens', () => {
  it('chữ thường, bỏ dấu câu và stop word', () => {
    expect(tokens('Habit Tracker: the Daily & Routine for you!')).toEqual(['habit', 'tracker', 'daily', 'routine']);
  });
});

describe('ownPhrases', () => {
  it('cụm 2 chữ trước, rồi 3 chữ, rồi 1 chữ; không vượt qua dấu tách; bỏ chữ trong tên nhà phát triển', () => {
    const p = ownPhrases(listing());
    expect(p.slice(0, 2)).toEqual(['habit tracker', 'daily routine']);
    expect(p).toContain('good habits');
    expect(p).not.toContain('tracker daily'); // dấu ":" tách 2 đoạn
    expect(p.every((x) => !x.split(' ').includes('labs'))).toBe(true);
    expect(p.length).toBeLessThanOrEqual(10);
  });
  it('không có phụ đề vẫn chạy', () => {
    expect(ownPhrases(listing({ subtitle: null }))).toContain('habit tracker');
  });
});

describe('mergeChips', () => {
  it('bỏ trùng giữa các nguồn, giữ nguồn đầu tiên, cắt ở max', () => {
    const out = mergeChips([[{ term: 'habit tracker', source: 'name' }], [{ term: 'Habit Tracker', source: 'suggest' }, { term: 'habit app', source: 'suggest' }]], 2);
    expect(out).toEqual([{ term: 'habit tracker', source: 'name' }, { term: 'habit app', source: 'suggest' }]);
  });
});

describe('inName', () => {
  it('tìm trong tên + phụ đề theo token, không phân biệt hoa thường', () => {
    expect(inName(listing(), 'Daily Routine')).toBe(true);
    expect(inName(listing(), 'streaks')).toBe(true);
    expect(inName(listing(), 'mood journal')).toBe(false);
  });
});
```

- [ ] **Step 2: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — `Cannot find module '@/lib/app-audit-core'`

- [ ] **Step 3: Viết code tối thiểu**

```ts
// web/src/lib/app-audit-core.ts
/**
 * Plan 2 mục 30 · Audit 1 app — phần thuần (client + server): kiểu dữ liệu, rút keyword, chấm điểm, việc nên sửa, gộp đối thủ.
 * Ngưỡng là QUY ƯỚC ShotMatic (2026-11-17), không phải số store công bố.
 */
export type AuditStore = 'play' | 'appstore';
export type Listing = {
  store: AuditStore; id: string; country: string;
  title: string;
  /** Play: mô tả ngắn · App Store: null (iTunes Lookup không trả phụ đề) */
  subtitle: string | null;
  description: string | null;
  screenshots: number | null;
  /** App Store: null (iTunes Lookup không trả video) */
  hasVideo: boolean | null;
  rating: number | null; ratingsCount: number | null; updatedAt: string | null;
  iconUrl: string | null; url: string; developer: string;
};
export type RivalHit = { store: AuditStore; id: string; title: string; developer: string; iconUrl: string | null; url: string; rating: number | null; ratingsCount: number | null };
/** measured=false: store lỗi, chưa đo · measured=true + rank=null: ngoài top 50 · top: 10 app đầu */
export type RankRow = { term: string; measured: boolean; rank: number | null; top: RivalHit[] };
export type ChipSource = 'name' | 'suggest' | 'rival';
export type Chip = { term: string; source: ChipSource };

export const TOP_DEPTH = 50;
export const MAX_TERMS = 20;
export const MAX_CHIPS = 15;
export const LIMITS: Record<AuditStore, { title: number; subtitle: number }> = { play: { title: 30, subtitle: 80 }, appstore: { title: 30, subtitle: 30 } };

const STOP = new Set(['a', 'an', 'and', 'the', 'for', 'of', 'to', 'in', 'on', 'with', 'by', 'your', 'you', 'my', 'app', 'apps', 'free', 'pro', 'best', 'new', 'is', 'it', 'at', 'or', 'from', 'plus', 'lite']);
const SEP = /[:|\-–—,&/·•()[\]!?.]+/;

export function tokens(s: string): string[] {
  return s.toLowerCase().split(/[^\p{L}\p{N}']+/u).map((w) => w.replace(/^'+|'+$/g, '')).filter((w) => w && !STOP.has(w));
}

/** Cụm 1–3 chữ từ tên + phụ đề, không vượt dấu tách, bỏ chữ của tên nhà phát triển (thương hiệu). Thứ tự: 2 chữ → 3 chữ → 1 chữ. */
export function ownPhrases(l: Listing, max = 10): string[] {
  const brand = new Set(tokens(l.developer));
  const segs = [l.title, l.subtitle ?? ''].flatMap((s) => s.split(SEP)).map((s) => tokens(s).filter((w) => !brand.has(w))).filter((t) => t.length);
  const by = (n: number) => segs.flatMap((t) => t.slice(0, t.length - n + 1).map((_, i) => t.slice(i, i + n).join(' ')));
  return [...new Set([...by(2), ...by(3), ...by(1).filter((w) => w.length >= 4)])].slice(0, max);
}

export function mergeChips(groups: Chip[][], max = MAX_CHIPS): Chip[] {
  const seen = new Set<string>();
  const out: Chip[] = [];
  for (const c of groups.flat()) {
    const term = c.term.trim().toLowerCase().replace(/\s+/g, ' ');
    if (!term || seen.has(term)) continue;
    seen.add(term);
    out.push({ term, source: c.source });
    if (out.length >= max) break;
  }
  return out;
}

/** Mọi token của keyword đều có trong tên + phụ đề. */
export function inName(l: Listing, term: string): boolean {
  const have = new Set(tokens(`${l.title} ${l.subtitle ?? ''}`).map(stem));
  const need = tokens(term).map(stem);
  return need.length > 0 && need.every((w) => have.has(w));
}
const stem = (w: string) => (w.length > 3 && w.endsWith('s') ? w.slice(0, -1) : w);
```

- [ ] **Step 4: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS (4 describe). Nếu `ownPhrases` không mở đầu bằng `['habit tracker','daily routine']`, xem lại thứ tự đoạn: tên trước phụ đề, trong tên đoạn trước ":" trước. Tên nhà phát triển trong fixture là `Lumen Labs` để chữ thương hiệu không trùng keyword.

- [ ] **Step 5: Commit (khi anh cho phép)**

```bash
git add web/src/lib/app-audit-core.ts web/tests/app-audit.test.ts
git commit -m "feat(web): audit app core — keyword phrases and chips (mục 30)"
```

---

### Task 2: Lõi thuần — chấm điểm 4 phần + việc nên sửa

**Files:**
- Modify: `web/src/lib/app-audit-core.ts`
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Consumes: `Listing`, `RankRow`, `LIMITS`, `inName`, `tokens` (Task 1)
- Produces:
  - `type PartKey = 'name' | 'description' | 'visuals' | 'ranks'`; `const WEIGHTS: Record<PartKey, number> = { name: 30, description: 15, visuals: 20, ranks: 35 }`
  - `type Item = { key: ItemKey; part: PartKey; max: number; got: number | null; params: Record<string, string | number> }`
  - `type ItemKey = 'titleFill' | 'subtitleFill' | 'termInName' | 'noRepeat' | 'descLength' | 'termEarly' | 'shots' | 'video' | 'rating' | 'fresh' | 'ranks'`
  - `type Part = { key: PartKey; weight: number; score: number | null }`
  - `type AuditScore = { total: number | null; parts: Part[]; items: Item[]; top10: number; top50: number; measured: number }`
  - `type Fix = { key: ItemKey; gain: number; params: Record<string, string | number> }`
  - `scoreAudit(l: Listing, ranks: RankRow[], now?: Date): AuditScore`
  - `fixList(s: AuditScore, max?: number): Fix[]`

- [ ] **Step 1: Viết test hỏng** (thêm vào cuối `web/tests/app-audit.test.ts`, sửa dòng import đầu file cho đủ tên)

```ts
import { fixList, scoreAudit, WEIGHTS, type RankRow } from '@/lib/app-audit-core';

const row = (term: string, rank: number | null, measured = true): RankRow => ({ term, rank, measured, top: [] });
const NOW = new Date('2026-11-17T00:00:00Z');

describe('scoreAudit', () => {
  it('trang tốt + hạng tốt → điểm cao, đủ 4 phần', () => {
    const s = scoreAudit(listing(), [row('habit tracker', 3), row('daily routine', 8), row('streaks', 20)], NOW);
    expect(s.parts.map((p) => p.key)).toEqual(['name', 'description', 'visuals', 'ranks']);
    expect(s.parts.every((p) => p.score !== null)).toBe(true);
    expect(s.top10).toBe(2);
    expect(s.measured).toBe(3);
    expect(s.total).toBeGreaterThanOrEqual(75);
  });
  it('trang thiếu → điểm thấp hơn hẳn', () => {
    const bad = listing({ title: 'Habit', subtitle: 'Habit habit', description: 'short', screenshots: 2, hasVideo: false, rating: 3.6, updatedAt: '2026-01-01T00:00:00Z' });
    const good = scoreAudit(listing(), [row('habit tracker', 3)], NOW).total!;
    expect(scoreAudit(bad, [row('habit tracker', 45)], NOW).total!).toBeLessThan(good - 30);
  });
  it('chưa đo không kéo điểm về 0: App Store không có phụ đề / video', () => {
    const ios = listing({ store: 'appstore', subtitle: null, hasVideo: null });
    const s = scoreAudit(ios, [row('habit tracker', 3)], NOW);
    expect(s.items.find((i) => i.key === 'subtitleFill')!.got).toBeNull();
    expect(s.items.find((i) => i.key === 'video')!.got).toBeNull();
    expect(s.parts.find((p) => p.key === 'name')!.score).toBe(WEIGHTS.name); // chỉ còn titleFill đo được, đủ điểm
    expect(s.total).toBeGreaterThanOrEqual(70);
  });
  it('mọi keyword chưa đo → phần hạng = null, tổng vẫn có từ 3 phần còn lại', () => {
    const s = scoreAudit(listing(), [row('habit tracker', null, false)], NOW);
    expect(s.parts.find((p) => p.key === 'ranks')!.score).toBeNull();
    expect(s.measured).toBe(0);
    expect(s.total).not.toBeNull();
  });
  it('không có gì đo được → total null', () => {
    const empty = listing({ title: '', subtitle: null, description: null, screenshots: null, hasVideo: null, rating: null, updatedAt: null });
    expect(scoreAudit(empty, [], NOW).total).toBeNull();
  });
});

describe('fixList', () => {
  it('xếp theo điểm lấy lại được, tối đa 5, có số trong params', () => {
    const bad = listing({ title: 'Habit', subtitle: 'Habit habit', description: 'short', screenshots: 2, rating: 3.6, updatedAt: '2026-01-01T00:00:00Z' });
    const f = fixList(scoreAudit(bad, [row('mood journal', 38), row('habit tracker', null)], NOW));
    expect(f.length).toBeLessThanOrEqual(5);
    expect(f.length).toBeGreaterThanOrEqual(3);
    for (let i = 1; i < f.length; i++) expect(f[i - 1].gain).toBeGreaterThanOrEqual(f[i].gain);
    expect(f.find((x) => x.key === 'termInName')?.params).toEqual({ term: 'mood journal', rank: 38 });
  });
  it('không đưa mục chưa đo vào việc nên sửa', () => {
    const ios = listing({ store: 'appstore', subtitle: null, hasVideo: null });
    expect(fixList(scoreAudit(ios, [], NOW)).some((x) => x.key === 'video' || x.key === 'subtitleFill')).toBe(false);
  });
});
```

- [ ] **Step 2: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — `scoreAudit is not a function` / không export.

- [ ] **Step 3: Viết code** (thêm vào cuối `app-audit-core.ts`)

```ts
export type PartKey = 'name' | 'description' | 'visuals' | 'ranks';
export const WEIGHTS: Record<PartKey, number> = { name: 30, description: 15, visuals: 20, ranks: 35 };
export type ItemKey = 'titleFill' | 'subtitleFill' | 'termInName' | 'noRepeat' | 'descLength' | 'termEarly' | 'shots' | 'video' | 'rating' | 'fresh' | 'ranks';
export type Item = { key: ItemKey; part: PartKey; max: number; got: number | null; params: Record<string, string | number> };
export type Part = { key: PartKey; weight: number; score: number | null };
export type AuditScore = { total: number | null; parts: Part[]; items: Item[]; top10: number; top50: number; measured: number };
export type Fix = { key: ItemKey; gain: number; params: Record<string, string | number> };

/** Tỉ lệ 0–1, đầy khi đạt `full`. */
const fill = (v: number, full: number) => Math.max(0, Math.min(1, v / full));
const days = (iso: string | null, now: Date) => (iso ? Math.max(0, Math.floor((now.getTime() - Date.parse(iso)) / 86_400_000)) : null);

export function scoreAudit(l: Listing, ranks: RankRow[], now = new Date()): AuditScore {
  const lim = LIMITS[l.store];
  const done = ranks.filter((r) => r.measured);
  const top10 = done.filter((r) => r.rank !== null && r.rank <= 10).length;
  const top50 = done.filter((r) => r.rank !== null).length;
  // keyword gần top 10 nhất (hạng 11–50) — đưa vào tên là dễ lên nhất
  const near = done.filter((r) => r.rank !== null && r.rank > 10).sort((a, b) => a.rank! - b.rank!)[0] ?? null;
  // keyword chính = 3 keyword hạng tốt nhất
  const main = done.filter((r) => r.rank !== null).sort((a, b) => a.rank! - b.rank!).slice(0, 3);
  const repeats = l.subtitle ? [...new Set(tokens(l.title))].filter((w) => tokens(l.subtitle!).includes(w)) : [];
  const head = l.description ? l.description.split(/\n+/).slice(0, 3).join(' ') : null;
  const early = head !== null && main.length ? main.find((r) => tokens(r.term).every((w) => tokens(head).includes(w))) ?? null : null;
  const age = days(l.updatedAt, now);

  const items: Item[] = [
    { key: 'titleFill', part: 'name', max: 10, got: l.title ? 10 * fill(l.title.length, lim.title * 0.7) : null, params: { used: l.title.length, limit: lim.title } },
    { key: 'subtitleFill', part: 'name', max: 8, got: l.subtitle === null ? null : 8 * fill(l.subtitle.length, lim.subtitle * 0.7), params: { used: l.subtitle?.length ?? 0, limit: lim.subtitle } },
    { key: 'termInName', part: 'name', max: 8, got: near ? (inName(l, near.term) ? 8 : 0) : null, params: near ? { term: near.term, rank: near.rank! } : {} },
    { key: 'noRepeat', part: 'name', max: 4, got: l.subtitle === null ? null : Math.max(0, 4 - 2 * repeats.length), params: { words: repeats.join(', ') } },
    { key: 'descLength', part: 'description', max: 8, got: l.description === null ? null : 8 * fill(l.description.length, 1000), params: { chars: l.description?.length ?? 0 } },
    { key: 'termEarly', part: 'description', max: 7, got: head === null || !main.length ? null : early ? 7 : 0, params: main[0] ? { term: main[0].term } : {} },
    { key: 'shots', part: 'visuals', max: 6, got: l.screenshots === null ? null : 6 * fill(l.screenshots, 6), params: { n: l.screenshots ?? 0 } },
    { key: 'video', part: 'visuals', max: 3, got: l.hasVideo === null ? null : l.hasVideo ? 3 : 0, params: {} },
    { key: 'rating', part: 'visuals', max: 6, got: l.rating === null ? null : 6 * fill(l.rating - 3.5, 1), params: { rating: l.rating ?? 0 } },
    { key: 'fresh', part: 'visuals', max: 5, got: age === null ? null : age <= 30 ? 5 : age <= 90 ? 3 : age <= 180 ? 1 : 0, params: { days: age ?? 0 } },
    { key: 'ranks', part: 'ranks', max: 35, got: done.length ? 35 * (0.7 * top10 + 0.3 * top50) / done.length : null, params: { top10, top50, measured: done.length } },
  ];
  const parts: Part[] = (Object.keys(WEIGHTS) as PartKey[]).map((key) => {
    const m = items.filter((i) => i.part === key && i.got !== null);
    const max = m.reduce((a, i) => a + i.max, 0);
    return { key, weight: WEIGHTS[key], score: max ? Math.round((m.reduce((a, i) => a + i.got!, 0) / max) * WEIGHTS[key]) : null };
  });
  const m = parts.filter((p) => p.score !== null);
  const w = m.reduce((a, p) => a + p.weight, 0);
  return { total: w ? Math.round((m.reduce((a, p) => a + p.score!, 0) / w) * 100) : null, parts, items, top10, top50, measured: done.length };
}

/** Việc nên sửa: mục đã đo còn thiếu điểm, quy ra điểm /100 lấy lại được, lớn nhất trước. */
export function fixList(s: AuditScore, max = 5): Fix[] {
  const partMax = new Map<PartKey, number>();
  for (const i of s.items) if (i.got !== null) partMax.set(i.part, (partMax.get(i.part) ?? 0) + i.max);
  const w = s.parts.filter((p) => p.score !== null).reduce((a, p) => a + p.weight, 0);
  return s.items
    .filter((i) => i.got !== null && i.max - i.got! >= 0.5)
    .map((i) => ({ key: i.key, params: i.params, gain: Math.round(((i.max - i.got!) / partMax.get(i.part)!) * WEIGHTS[i.part] / w * 100) }))
    .filter((f) => f.gain > 0)
    .sort((a, b) => b.gain - a.gain)
    .slice(0, max);
}
```

- [ ] **Step 4: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS. Tính tay để đối chiếu: trang tốt = 28 + 15 + 20 + 27 = **90**; trang thiếu = 6 + 0 + 3 + 11 = **20**.

- [ ] **Step 5: Commit (khi anh cho phép)**

```bash
git add web/src/lib/app-audit-core.ts web/tests/app-audit.test.ts
git commit -m "feat(web): audit app score parts and fix list (mục 30)"
```

---

### Task 3: Lõi thuần — gộp đối thủ + chip từ đối thủ

**Files:**
- Modify: `web/src/lib/app-audit-core.ts`
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Consumes: `RankRow`, `RivalHit`, `Chip`, `tokens`, `ownPhrases`, `inName` (Task 1)
- Produces:
  - `type RivalSource = 'above' | 'similar'`
  - `type RivalRow = { app: RivalHit; overlap: number; sources: RivalSource[] }`
  - `mergeRivals(self: { store: AuditStore; id: string }, ranks: RankRow[], similar: RivalHit[], max?: number): RivalRow[]`
  - `rivalChips(own: Listing, rivals: RivalHit[]): Chip[]`

- [ ] **Step 1: Viết test hỏng**

```ts
import { mergeRivals, rivalChips, type RivalHit } from '@/lib/app-audit-core';

const hit = (id: string, title = id, ratingsCount = 100): RivalHit => ({ store: 'play', id, title, developer: 'D', iconUrl: null, url: `u/${id}`, rating: 4.2, ratingsCount });

describe('mergeRivals', () => {
  const self = { store: 'play' as const, id: 'com.habit.app' };
  const ranks: RankRow[] = [
    { term: 'habit tracker', measured: true, rank: 14, top: [hit('a'), hit('b'), hit('com.habit.app')] },
    { term: 'daily routine', measured: true, rank: null, top: [hit('a'), hit('c')] },
    { term: 'streaks', measured: true, rank: 2, top: [hit('d'), hit('com.habit.app')] },
    { term: 'mood', measured: false, rank: null, top: [] },
  ];
  it('app đứng trên ở keyword mình thua (ngoài top 10), bỏ chính mình, xếp theo số keyword trùng', () => {
    const r = mergeRivals(self, ranks, []);
    expect(r.map((x) => x.app.id)).toEqual(['a', 'b', 'c']);
    expect(r[0]).toMatchObject({ overlap: 2, sources: ['above'] });
  });
  it('gộp app tương tự, đếm trùng trên mọi keyword đã đo', () => {
    const r = mergeRivals(self, ranks, [hit('d', 'D app', 5000), hit('a')]);
    expect(r.find((x) => x.app.id === 'a')!.sources).toEqual(['above', 'similar']);
    expect(r.find((x) => x.app.id === 'd')).toMatchObject({ overlap: 1, sources: ['similar'] });
  });
  it('cắt ở max', () => {
    expect(mergeRivals(self, ranks, [], 2)).toHaveLength(2);
  });
});

describe('rivalChips', () => {
  it('cụm 2 chữ có trong tên ≥ 2 đối thủ mà tên mình chưa có', () => {
    const own = listing();
    const chips = rivalChips(own, [hit('a', 'Mood Journal: Habit Tracker'), hit('b', 'Mood Journal & Diary'), hit('c', 'Sleep Sounds')]);
    expect(chips).toEqual([{ term: 'mood journal', source: 'rival' }]);
  });
});
```

- [ ] **Step 2: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — `mergeRivals` không export.

- [ ] **Step 3: Viết code** (thêm vào cuối `app-audit-core.ts`)

```ts
export type RivalSource = 'above' | 'similar';
export type RivalRow = { app: RivalHit; overlap: number; sources: RivalSource[] };

export function mergeRivals(self: { store: AuditStore; id: string }, ranks: RankRow[], similar: RivalHit[], max = 20): RivalRow[] {
  const key = (a: { store: string; id: string }) => `${a.store}:${a.id}`;
  const me = key(self);
  const rows = new Map<string, RivalRow>();
  const add = (a: RivalHit, src: RivalSource) => {
    if (key(a) === me) return;
    const r = rows.get(key(a)) ?? { app: a, overlap: 0, sources: [] };
    if (!r.sources.includes(src)) r.sources.push(src);
    rows.set(key(a), r);
  };
  const done = ranks.filter((r) => r.measured);
  for (const r of done) if (r.rank === null || r.rank > 10) for (const a of r.top) add(a, 'above');
  for (const a of similar) add(a, 'similar');
  for (const r of rows.values()) r.overlap = done.filter((x) => x.top.some((a) => key(a) === key(r.app))).length;
  return [...rows.values()].sort((a, b) => b.overlap - a.overlap || (b.app.ratingsCount ?? 0) - (a.app.ratingsCount ?? 0)).slice(0, max);
}

/** Cụm 2 chữ xuất hiện trong tên ≥ 2 đối thủ mà tên + phụ đề của mình chưa có. */
export function rivalChips(own: Listing, rivals: RivalHit[]): Chip[] {
  const count = new Map<string, number>();
  for (const a of rivals) {
    const set = new Set(a.title.split(SEP).flatMap((s) => { const t = tokens(s); return t.slice(0, -1).map((_, i) => `${t[i]} ${t[i + 1]}`); }));
    for (const p of set) count.set(p, (count.get(p) ?? 0) + 1);
  }
  return [...count].filter(([p, n]) => n >= 2 && !inName(own, p)).sort((a, b) => b[1] - a[1]).map(([term]) => ({ term, source: 'rival' as const }));
}
```

- [ ] **Step 4: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS. Ghi chú: ở test đầu `d` không vào vì `streaks` mình hạng 2 (≤ 10) → không phải keyword thua.

- [ ] **Step 5: Commit (khi anh cho phép)**

```bash
git add web/src/lib/app-audit-core.ts web/tests/app-audit.test.ts
git commit -m "feat(web): audit app rivals merge and rival chips (mục 30)"
```

---

### Task 4: Đọc trang store (listing)

**Files:**
- Create: `web/src/lib/app-audit-listing.ts`
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Consumes: `Listing` (Task 1); `AppRef` từ `@/lib/app-inspect-core`; `playLimit` từ `@/collectors/playstore`; `appleWebLimit` từ `@/collectors/appstore-web`; `CollectorError` từ `@/lib/errors`; `tr` từ `@/lib/i18n`
- Produces:
  - `parsePlayListing(raw: any, country: string): Listing`
  - `parseItunesListing(raw: any, country: string): Listing`
  - `type FetchListing = (ref: AppRef & { country: string }, signal: AbortSignal) => Promise<Listing>`
  - `const fetchListing: FetchListing`

- [ ] **Step 1: Viết test hỏng**

```ts
import { parseItunesListing, parsePlayListing } from '@/lib/app-audit-listing';

describe('parsePlayListing', () => {
  it('lấy tên, mô tả ngắn, mô tả, số ảnh, video', () => {
    const l = parsePlayListing({ appId: 'com.x.y', title: 'X', summary: 'Short', description: 'Long', screenshots: ['a', 'b'], video: 'https://yt/v',
      score: 4.1, ratings: 900, updated: 1763337600000, icon: 'i', url: 'u', developer: 'Dev' }, 'us');
    expect(l).toMatchObject({ store: 'play', id: 'com.x.y', country: 'US', subtitle: 'Short', description: 'Long', screenshots: 2, hasVideo: true, rating: 4.1, ratingsCount: 900 });
    expect(l.updatedAt).toBe(new Date(1763337600000).toISOString());
  });
  it('thiếu video → false, thiếu ảnh → 0', () => {
    expect(parsePlayListing({ appId: 'com.x.y', title: 'X', url: 'u' }, 'US')).toMatchObject({ hasVideo: false, screenshots: 0, subtitle: null });
  });
});

describe('parseItunesListing', () => {
  it('phụ đề + video = null (chưa đo), ảnh = iPhone + iPad', () => {
    const l = parseItunesListing({ trackId: 123, trackName: 'Y', description: 'D', screenshotUrls: ['a', 'b', 'c'], ipadScreenshotUrls: ['d'],
      averageUserRating: 4.7, userRatingCount: 50, currentVersionReleaseDate: '2026-10-01T00:00:00Z', artworkUrl512: 'i', trackViewUrl: 'u', artistName: 'Dev' }, 'US');
    expect(l).toMatchObject({ store: 'appstore', id: '123', subtitle: null, hasVideo: null, screenshots: 3, rating: 4.7, ratingsCount: 50, updatedAt: '2026-10-01T00:00:00Z' });
  });
});
```

Ghi chú: `screenshots` App Store chỉ đếm ảnh iPhone (`screenshotUrls`) vì đó là thứ người dùng iPhone thấy khi tìm.

- [ ] **Step 2: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — không tìm thấy module `@/lib/app-audit-listing`.

- [ ] **Step 3: Viết code**

```ts
// web/src/lib/app-audit-listing.ts
/** Plan 2 mục 30 · Audit 1 app — đọc trang store: tên, phụ đề, mô tả, ảnh, video, sao, ngày cập nhật. */
import gplay from 'google-play-scraper';
import type { AppRef } from './app-inspect-core';
import type { Listing } from './app-audit-core';
import { playLimit } from '@/collectors/playstore';
import { appleWebLimit } from '@/collectors/appstore-web';
import { CollectorError } from '@/lib/errors';
import { tr } from '@/lib/i18n';

const iso = (v: unknown): string | null => {
  if (typeof v === 'number' && Number.isFinite(v)) return new Date(v).toISOString();
  if (typeof v === 'string' && !Number.isNaN(Date.parse(v))) return v;
  return null;
};
const str = (v: unknown) => (typeof v === 'string' && v.trim() ? v : null);
const num = (v: unknown) => (typeof v === 'number' && Number.isFinite(v) ? v : null);

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function parsePlayListing(raw: any, country: string): Listing {
  return {
    store: 'play', id: String(raw.appId), country: country.toUpperCase(), title: String(raw.title ?? ''),
    subtitle: str(raw.summary), description: str(raw.description),
    screenshots: Array.isArray(raw.screenshots) ? raw.screenshots.length : 0, hasVideo: !!str(raw.video),
    rating: num(raw.score), ratingsCount: num(raw.ratings), updatedAt: iso(raw.updated),
    iconUrl: str(raw.icon), url: String(raw.url ?? `https://play.google.com/store/apps/details?id=${raw.appId}`), developer: String(raw.developer ?? ''),
  };
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function parseItunesListing(raw: any, country: string): Listing {
  return {
    store: 'appstore', id: String(raw.trackId), country: country.toUpperCase(), title: String(raw.trackName ?? ''),
    subtitle: null, description: str(raw.description),
    screenshots: Array.isArray(raw.screenshotUrls) ? raw.screenshotUrls.length : null, hasVideo: null,
    rating: num(raw.averageUserRating), ratingsCount: num(raw.userRatingCount), updatedAt: iso(raw.currentVersionReleaseDate),
    iconUrl: str(raw.artworkUrl512) ?? str(raw.artworkUrl100), url: String(raw.trackViewUrl ?? ''), developer: String(raw.artistName ?? ''),
  };
}

export type FetchListing = (ref: AppRef & { country: string }, signal: AbortSignal) => Promise<Listing>;

export const fetchListing: FetchListing = (ref, signal) => ref.store === 'play'
  ? playLimit(async () => {
    signal.throwIfAborted();
    try {
      const raw = await gplay.app({ appId: ref.id, country: ref.country.toLowerCase(), lang: 'en',
        requestOptions: { timeout: { request: 20_000 }, retry: { limit: 0 }, signal: AbortSignal.any([signal, AbortSignal.timeout(20_000)]) } });
      return parsePlayListing(raw, ref.country);
    } catch (e) {
      if (/404|not found/i.test(String((e as Error)?.message))) throw new CollectorError('PARSE', tr('Google Play không có app này ở nước đã chọn'));
      throw e;
    }
  })
  : appleWebLimit(async () => {
    signal.throwIfAborted();
    const res = await fetch(`https://itunes.apple.com/lookup?id=${ref.id}&country=${ref.country.toLowerCase()}`, { signal: AbortSignal.any([signal, AbortSignal.timeout(20_000)]) });
    if (res.status === 403 || res.status === 429) throw new CollectorError('RATE_LIMITED', `iTunes lookup ${res.status}`);
    if (!res.ok) throw new CollectorError('NETWORK', `iTunes lookup ${res.status}`);
    const json = await res.json() as { results?: unknown[] };
    if (!json.results?.length) throw new CollectorError('PARSE', tr('App Store không có app này ở nước đã chọn'));
    return parseItunesListing(json.results[0], ref.country);
  });
```

- [ ] **Step 4: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit (khi anh cho phép)**

```bash
git add web/src/lib/app-audit-listing.ts web/tests/app-audit.test.ts
git commit -m "feat(web): audit app store listing reader (mục 30)"
```

---

### Task 5: Bảng `app_audits` + đo hạng + chạy audit + đối thủ

**Files:**
- Modify: `web/src/db/schema.ts` (thêm bảng ở cuối, cạnh `reviewMineApps`)
- Create: migration qua `npm run db:generate` (ra `web/drizzle/0030_*.sql`)
- Create: `web/src/lib/app-audit.ts`
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Consumes: Task 1–4; `createSuggest`, `fetchSuggest`, `type FetchSuggest` từ `@/collectors/suggest`; `playRelated` từ `@/lib/app-related`; `fetchItunes`, `normalizeItunesApp` từ `@/collectors/appstore`; `playLimit`; `CollectorError`; bảng `apps`.
- Produces:
  - bảng `appAudits` (`app_audits`): `id` int pk auto · `store` text · `storeAppId` text · `country` text · `title` text · `iconUrl` text null · `score` int null · `createdAt` int · `data` text JSON
  - `type SearchTop = (store: AuditStore, term: string, country: string, signal: AbortSignal) => Promise<RivalHit[]>`; `const searchTop: SearchTop`
  - `rankTerms(l: Listing, terms: string[], signal: AbortSignal, search?: SearchTop, onDone?: (n: number) => void, waitMs?: number): Promise<RankRow[]>`
  - `suggestChips(db: Db, l: Listing, signal: AbortSignal, fetcher?: FetchSuggest): Promise<Chip[]>`
  - `type AuditView = { id: number; listing: Listing; ranks: RankRow[]; score: AuditScore; fixes: Fix[]; createdAt: string }`
  - `type AuditDeps = { listing?: FetchListing; search?: SearchTop; suggest?: FetchSuggest; similar?: (l: Listing, signal: AbortSignal) => Promise<RivalHit[]> }`
  - `runAudit(db: Db, input: { ref: AppRef & { country: string }; terms: string[] }, signal: AbortSignal, deps?: AuditDeps, now?: Date): Promise<AuditView>`
  - `getAudit(db: Db, id: number): AuditView | null`
  - `listAudits(db: Db, limit?: number): { id: number; store: AuditStore; storeAppId: string; country: string; title: string; iconUrl: string | null; score: number | null; createdAt: string }[]`
  - `ensureAppIds(db: Db, hits: RivalHit[]): Map<string, number>` (khoá `store:id`)
  - `auditRivals(db: Db, id: number, signal: AbortSignal, deps?: AuditDeps, pasted?: RivalHit[]): Promise<{ selfDbId: number; rivals: (RivalRow & { dbId: number })[]; chips: Chip[] } | null>`

- [ ] **Step 1: Thêm bảng vào schema + sinh migration**

```ts
// web/src/db/schema.ts — cuối file
/** Plan 2 mục 30 · Audit 1 app: mỗi lần chạy 1 dòng; `data` = AuditView (không có id) dạng JSON. Hạng KHÔNG ghi vào keyword_hits. */
export const appAudits = sqliteTable('app_audits', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  store: text('store').notNull(), storeAppId: text('store_app_id').notNull(), country: text('country').notNull(),
  title: text('title').notNull(), iconUrl: text('icon_url'), score: integer('score'),
  createdAt: integer('created_at').notNull(), data: text('data').notNull(),
});
```

Run: `npm run db:generate`
Expected: file mới `web/drizzle/0030_<tên>.sql` có `CREATE TABLE \`app_audits\``. Không sửa tay file sinh ra.

- [ ] **Step 2: Viết test hỏng**

```ts
import { createDb } from '@/db/client';
import { auditRivals, ensureAppIds, getAudit, listAudits, rankTerms, runAudit, suggestChips, type SearchTop } from '@/lib/app-audit';
import { CollectorError } from '@/lib/errors';

const sig = () => new AbortController().signal;
const fakeSearch = (map: Record<string, string[]>, fail: Record<string, number> = {}): SearchTop => async (_s, term) => {
  if (fail[term]) { fail[term]--; throw new CollectorError('RATE_LIMITED', '429'); }
  return (map[term] ?? []).map((id) => hit(id));
};

describe('rankTerms', () => {
  it('hạng = vị trí 1-based; không có = ngoài top; 429 hai lần = chưa đo; 429 một lần = thử lại được', async () => {
    const l = listing();
    const s = fakeSearch({ a: ['x', 'com.habit.app'], b: ['x'], c: ['com.habit.app'], d: ['com.habit.app'] }, { c: 2, d: 1 });
    const r = await rankTerms(l, ['a', 'b', 'c', 'd'], sig(), s, undefined, 0);
    expect(r.map((x) => [x.term, x.measured, x.rank])).toEqual([['a', true, 2], ['b', true, null], ['c', false, null], ['d', true, 1]]);
    expect(r[0].top.map((x) => x.id)).toEqual(['x', 'com.habit.app']);
  });
  it('cắt ở 20 keyword', async () => {
    const terms = Array.from({ length: 25 }, (_, i) => `t${i}`);
    expect(await rankTerms(listing(), terms, sig(), fakeSearch({}), undefined, 0)).toHaveLength(20);
  });
});

describe('suggestChips', () => {
  it('chip từ tên trước, rồi gợi ý store; tối đa 15', async () => {
    const db = createDb(':memory:');
    const chips = await suggestChips(db, listing(), sig(), async (term) => [`${term} app`, `${term} free`]);
    expect(chips[0]).toEqual({ term: 'habit tracker', source: 'name' });
    expect(chips.some((c) => c.source === 'suggest')).toBe(true);
    expect(chips.length).toBeLessThanOrEqual(15);
  });
  it('gợi ý store lỗi vẫn trả chip từ tên', async () => {
    const db = createDb(':memory:');
    const chips = await suggestChips(db, listing(), sig(), async () => { throw new Error('down'); });
    expect(chips.length).toBeGreaterThan(0);
    expect(chips.every((c) => c.source === 'name')).toBe(true);
  });
});

describe('runAudit + getAudit + listAudits + auditRivals', () => {
  const deps = {
    listing: async () => listing(),
    search: fakeSearch({ 'habit tracker': ['a', 'b', 'com.habit.app'], 'daily routine': ['a', 'c'] }),
    similar: async () => [hit('s1', 'Similar One', 9000)],
  };
  it('lưu 1 dòng, đọc lại đúng, đối thủ có id DB để So sánh app', async () => {
    const db = createDb(':memory:');
    const v = await runAudit(db, { ref: { store: 'play', id: 'com.habit.app', country: 'US' }, terms: ['habit tracker', 'daily routine'] }, sig(), deps, new Date('2026-11-17T00:00:00Z'));
    expect(v.id).toBeGreaterThan(0);
    expect(v.ranks.map((r) => r.rank)).toEqual([3, null]);
    expect(v.score.total).not.toBeNull();
    expect(getAudit(db, v.id)).toEqual(v);
    expect(listAudits(db)[0]).toMatchObject({ id: v.id, title: 'Habit Tracker: Daily Routine', score: v.score.total });
    const r = await auditRivals(db, v.id, sig(), deps);
    expect(r!.rivals.map((x) => x.app.id)).toEqual(['a', 'c', 's1']);
    expect(r!.rivals.every((x) => x.dbId > 0)).toBe(true);
    expect(r!.selfDbId).toBeGreaterThan(0);
  });
  it('id lạ → null', async () => {
    expect(await auditRivals(createDb(':memory:'), 999, sig(), deps)).toBeNull();
  });
  it('ensureAppIds gọi 2 lần không nhân đôi app', () => {
    const db = createDb(':memory:');
    const a = ensureAppIds(db, [hit('a')]);
    const b = ensureAppIds(db, [hit('a', 'A renamed')]);
    expect(a.get('play:a')).toBe(b.get('play:a'));
  });
});
```

- [ ] **Step 3: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — không tìm thấy module `@/lib/app-audit`.

- [ ] **Step 4: Viết code**

```ts
// web/src/lib/app-audit.ts
/**
 * Plan 2 mục 30 · Audit 1 app — máy chủ: đọc trang store, gợi ý chip, đo hạng top 50 (3 luồng, thử lại 1 lần khi 429),
 * chấm điểm, lưu bảng app_audits, gộp đối thủ + upsert app để So sánh app dùng id DB.
 */
import gplay from 'google-play-scraper';
import { desc, eq } from 'drizzle-orm';
import type { Db } from '@/db/client';
import { appAudits, apps } from '@/db/schema';
import { fetchItunes, normalizeItunesApp } from '@/collectors/appstore';
import { playLimit } from '@/collectors/playstore';
import { createSuggest, fetchSuggest, type FetchSuggest } from '@/collectors/suggest';
import { CollectorError } from '@/lib/errors';
import { playRelated } from './app-related';
import type { AppRef } from './app-inspect-core';
import { fetchListing, type FetchListing } from './app-audit-listing';
import {
  fixList, MAX_CHIPS, MAX_TERMS, mergeChips, mergeRivals, ownPhrases, rivalChips, scoreAudit, TOP_DEPTH,
  type AuditScore, type AuditStore, type Chip, type Fix, type Listing, type RankRow, type RivalHit, type RivalRow,
} from './app-audit-core';

export type SearchTop = (store: AuditStore, term: string, country: string, signal: AbortSignal) => Promise<RivalHit[]>;

export const searchTop: SearchTop = async (store, term, country, signal) => {
  if (store === 'play') return playLimit(async () => {
    signal.throwIfAborted();
    const raw = await gplay.search({ term, num: TOP_DEPTH, country: country.toLowerCase(), lang: 'en',
      requestOptions: { timeout: { request: 20_000 }, retry: { limit: 0 }, signal: AbortSignal.any([signal, AbortSignal.timeout(20_000)]) } });
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    return (Array.isArray(raw) ? raw : []).slice(0, TOP_DEPTH).map((a: any) => ({ store: 'play' as const, id: a.appId, title: a.title, developer: a.developer ?? '',
      iconUrl: a.icon ?? null, url: a.url ?? `https://play.google.com/store/apps/details?id=${a.appId}`, rating: typeof a.score === 'number' ? a.score : null, ratingsCount: null }));
  });
  const rows = await fetchItunes(term, country, signal, TOP_DEPTH);
  return rows.slice(0, TOP_DEPTH).map((r) => {
    const a = normalizeItunesApp(r);
    return { store: 'appstore' as const, id: a.storeAppId, title: a.title, developer: a.developer, iconUrl: a.iconUrl, url: a.url, rating: a.rating, ratingsCount: a.ratingsCount };
  });
};

const sleep = (ms: number, signal: AbortSignal) => new Promise<void>((ok, no) => {
  const t = setTimeout(ok, ms);
  signal.addEventListener('abort', () => { clearTimeout(t); no(signal.reason); }, { once: true });
});

/** Đo hạng từng keyword (tối đa 20), 3 luồng. 429 → chờ `waitMs` thử lại 1 lần; vẫn lỗi / lỗi khác → measured=false. */
export async function rankTerms(l: Listing, terms: string[], signal: AbortSignal, search: SearchTop = searchTop, onDone?: (n: number) => void, waitMs = 3000): Promise<RankRow[]> {
  const list = terms.slice(0, MAX_TERMS);
  const out: RankRow[] = new Array(list.length);
  let next = 0;
  let done = 0;
  const one = async (term: string): Promise<RankRow> => {
    for (let attempt = 0; attempt < 2; attempt++) {
      try {
        const hits = await search(l.store, term, l.country, signal);
        const i = hits.findIndex((h) => h.id === l.id);
        return { term, measured: true, rank: i >= 0 ? i + 1 : null, top: hits.slice(0, 10) };
      } catch (e) {
        signal.throwIfAborted();
        if (attempt === 0 && e instanceof CollectorError && e.code === 'RATE_LIMITED') { await sleep(waitMs, signal); continue; }
        break;
      }
    }
    return { term, measured: false, rank: null, top: [] };
  };
  const worker = async () => {
    while (next < list.length) {
      const i = next++;
      out[i] = await one(list[i]);
      onDone?.(++done);
    }
  };
  await Promise.all([worker(), worker(), worker()]);
  return out;
}

/** Chip: cụm từ tên + phụ đề, rồi gợi ý store của 2 cụm đầu. Gợi ý lỗi → chỉ còn chip từ tên. */
export async function suggestChips(db: Db, l: Listing, signal: AbortSignal, fetcher: FetchSuggest = fetchSuggest): Promise<Chip[]> {
  const own = ownPhrases(l);
  const suggest = createSuggest(db, fetcher);
  const source = l.store === 'play' ? 'play_suggest' as const : 'appstore_hint' as const;
  const found: Chip[] = [];
  for (const seed of own.slice(0, 2)) {
    try { found.push(...(await suggest(seed, l.country, source, signal)).map((term) => ({ term, source: 'suggest' as const }))); }
    catch { signal.throwIfAborted(); }
  }
  return mergeChips([own.map((term) => ({ term, source: 'name' as const })), found], MAX_CHIPS);
}

export type AuditView = { id: number; listing: Listing; ranks: RankRow[]; score: AuditScore; fixes: Fix[]; createdAt: string };
export type AuditDeps = { listing?: FetchListing; search?: SearchTop; suggest?: FetchSuggest; similar?: (l: Listing, signal: AbortSignal) => Promise<RivalHit[]> };

export async function runAudit(db: Db, input: { ref: AppRef & { country: string }; terms: string[] }, signal: AbortSignal, deps: AuditDeps = {}, now = new Date(), onDone?: (n: number) => void): Promise<AuditView> {
  const listing = await (deps.listing ?? fetchListing)(input.ref, signal);
  const terms = [...new Set(input.terms.map((t) => t.trim().toLowerCase()).filter(Boolean))];
  const ranks = await rankTerms(listing, terms, signal, deps.search ?? searchTop, onDone);
  const score = scoreAudit(listing, ranks, now);
  const body = { listing, ranks, score, fixes: fixList(score), createdAt: now.toISOString() };
  const id = db.insert(appAudits).values({ store: listing.store, storeAppId: listing.id, country: listing.country, title: listing.title, iconUrl: listing.iconUrl,
    score: score.total, createdAt: now.getTime(), data: JSON.stringify(body) }).returning({ id: appAudits.id }).get().id;
  return { id, ...body };
}

export function getAudit(db: Db, id: number): AuditView | null {
  const r = db.select().from(appAudits).where(eq(appAudits.id, id)).get();
  return r ? { id: r.id, ...(JSON.parse(r.data) as Omit<AuditView, 'id'>) } : null;
}

export function listAudits(db: Db, limit = 20) {
  return db.select({ id: appAudits.id, store: appAudits.store, storeAppId: appAudits.storeAppId, country: appAudits.country, title: appAudits.title,
    iconUrl: appAudits.iconUrl, score: appAudits.score, createdAt: appAudits.createdAt }).from(appAudits).orderBy(desc(appAudits.id)).limit(limit).all()
    .map((r) => ({ ...r, store: r.store as AuditStore, createdAt: new Date(r.createdAt).toISOString() }));
}

/** Upsert app tối thiểu (tên, studio, icon, link) → id DB. Có rồi thì giữ dòng cũ, chỉ cập nhật tên / icon. */
export function ensureAppIds(db: Db, hits: RivalHit[]): Map<string, number> {
  const ids = new Map<string, number>();
  db.transaction((tx) => {
    for (const h of hits) {
      const k = `${h.store}:${h.id}`;
      if (ids.has(k)) continue;
      const details = { title: h.title, developer: h.developer, iconUrl: h.iconUrl, url: h.url };
      ids.set(k, tx.insert(apps).values({ store: h.store, storeAppId: h.id, ...details })
        .onConflictDoUpdate({ target: [apps.store, apps.storeAppId], set: details }).returning({ id: apps.id }).get().id);
    }
  });
  return ids;
}

const playSimilar = async (l: Listing, signal: AbortSignal): Promise<RivalHit[]> => {
  if (l.store !== 'play') return [];
  const v = await playRelated(l.id, l.country, signal);
  return (v.similar?.apps ?? []).map((a) => ({ store: a.store, id: a.id, title: a.title, developer: a.developer, iconUrl: a.iconUrl, url: a.url, rating: a.rating, ratingsCount: a.ratingsCount }));
};

/** Đối thủ = app đứng trên mình + app tương tự (Play tự đọc; App Store = `pasted` từ ô dán tay). */
export async function auditRivals(db: Db, id: number, signal: AbortSignal, deps: AuditDeps = {}, pasted: RivalHit[] = []) {
  const v = getAudit(db, id);
  if (!v) return null;
  let similar: RivalHit[] = [];
  try { similar = await (deps.similar ?? playSimilar)(v.listing, signal); } catch { signal.throwIfAborted(); }
  const rows = mergeRivals({ store: v.listing.store, id: v.listing.id }, v.ranks, [...similar, ...pasted]);
  const self: RivalHit = { store: v.listing.store, id: v.listing.id, title: v.listing.title, developer: v.listing.developer, iconUrl: v.listing.iconUrl, url: v.listing.url, rating: v.listing.rating, ratingsCount: v.listing.ratingsCount };
  const ids = ensureAppIds(db, [self, ...rows.map((r) => r.app)]);
  return {
    selfDbId: ids.get(`${self.store}:${self.id}`)!,
    rivals: rows.map((r) => ({ ...r, dbId: ids.get(`${r.app.store}:${r.app.id}`)! })),
    chips: rivalChips(v.listing, rows.map((r) => r.app)),
  };
}
```

Ghi chú: `CollectorError` có `code: ErrorCode` (`web/src/lib/errors.ts`). Bảng `apps` có cột `developer` NOT NULL — `RivalHit.developer` luôn là chuỗi nên ổn.

- [ ] **Step 5: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS. Thứ tự đối thủ ở test chính: `habit tracker` mình hạng 3 (≤ 10, không thua) nên `b` không vào; `daily routine` ngoài top → `a`, `c`; `a` trùng 2 keyword, `c` 1, `s1` 0 → `['a','c','s1']`.

- [ ] **Step 6: Commit (khi anh cho phép)**

```bash
git add web/src/db/schema.ts web/drizzle web/src/lib/app-audit.ts web/tests/app-audit.test.ts
git commit -m "feat(web): run app audit — ranks, save, rivals with db ids (mục 30)"
```

---

### Task 6: API `/api/audit`

**Files:**
- Create: `web/src/server/audit-api.ts`
- Modify: `web/src/server/app.ts` (import + `api.route('/audit', auditApi({ db }))` cạnh dòng `api.route('/reviews', reviewsApi({ db }))`)
- Test: `web/tests/app-audit.test.ts`

**Interfaces:**
- Consumes: Task 5 (`runAudit`, `getAudit`, `listAudits`, `auditRivals`, `suggestChips`, `AuditDeps`); `fetchListing`; `parseAppLink`; `guardJsonPost` từ `@/lib/api-guard`; `COUNTRIES` từ `@/lib/countries`; `pastedSimilar` từ `@/lib/app-related`
- Produces (HTTP):
  - `POST /api/audit/read` `{ link, country }` → `{ listing: Listing; chips: Chip[] }`
  - `POST /api/audit/run` `{ link, country, terms: string[] }` → `AuditView`
  - `POST /api/audit/rivals` `{ id: number; pasted?: string }` → `{ selfDbId; rivals; chips }`
  - `GET /api/audit/list` → `{ audits: ReturnType<typeof listAudits> }`
  - `GET /api/audit/:id` → `AuditView`
  - `auditApi(o: { db: () => Db; deps?: AuditDeps }): Hono`

- [ ] **Step 1: Viết test hỏng**

```ts
import { auditApi } from '@/server/audit-api';

describe('auditApi', () => {
  const deps = { listing: async () => listing(), search: fakeSearch({ 'habit tracker': ['a'] }), suggest: async () => [], similar: async () => [] };
  const make = () => { const db = createDb(':memory:'); return auditApi({ db: () => db, deps }); };
  const post = (api: ReturnType<typeof auditApi>, p: string, b: unknown) => api.request(p, { method: 'POST',
    headers: { 'Content-Type': 'application/json', Origin: 'http://127.0.0.1:3200', Host: '127.0.0.1:3200' }, body: JSON.stringify(b) });

  it('link sai / nước sai / không keyword → 400', async () => {
    const api = make();
    expect((await post(api, '/read', { link: 'hello' })).status).toBe(400);
    expect((await post(api, '/read', { link: 'com.habit.app', country: 'ZZ' })).status).toBe(400);
    expect((await post(api, '/run', { link: 'com.habit.app', terms: [] })).status).toBe(400);
  });
  it('read → chip · run → lưu · list + get + rivals', async () => {
    const api = make();
    const r = await (await post(api, '/read', { link: 'com.habit.app', country: 'US' })).json();
    expect(r.chips[0].term).toBe('habit tracker');
    const v = await (await post(api, '/run', { link: 'com.habit.app', country: 'US', terms: ['habit tracker'] })).json();
    expect(v.ranks[0].rank).toBeNull(); // ngoài top → a đứng trên mình
    expect((await (await api.request('/list')).json()).audits).toHaveLength(1);
    expect((await (await api.request(`/${v.id}`)).json()).id).toBe(v.id);
    const riv = await (await post(api, '/rivals', { id: v.id })).json();
    expect(riv.rivals.map((x: { app: { id: string } }) => x.app.id)).toEqual(['a']);
    expect((await post(api, '/rivals', { id: 999 })).status).toBe(404);
  });
});
```

- [ ] **Step 2: Chạy test, phải hỏng**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: FAIL — không tìm thấy `@/server/audit-api`.

- [ ] **Step 3: Viết code**

```ts
// web/src/server/audit-api.ts
import { Hono } from 'hono';
import type { Db } from '@/db/client';
import { guardJsonPost } from '@/lib/api-guard';
import { tr } from '@/lib/i18n';
import { COUNTRIES } from '@/lib/countries';
import { parseAppLink } from '@/lib/app-inspect-core';
import { fetchListing } from '@/lib/app-audit-listing';
import { pastedSimilar } from '@/lib/app-related';
import { MAX_TERMS, type RivalHit } from '@/lib/app-audit-core';
import { auditRivals, getAudit, listAudits, runAudit, suggestChips, type AuditDeps } from '@/lib/app-audit';

/** Plan 2 mục 30 · Audit 1 app: /api/audit/* */
export function auditApi(o: { db: () => Db; deps?: AuditDeps }) {
  const api = new Hono();
  const body = async (req: Request) => {
    const b = await req.json().catch(() => null);
    return b && typeof b === 'object' && !Array.isArray(b) ? b as Record<string, unknown> : null;
  };
  const err = (e: unknown, signal: AbortSignal) => Response.json({ error: signal.aborted ? tr('Đã dừng') : e instanceof Error ? e.message : String(e) }, { status: 502 });
  /** link + nước → ref, hoặc lỗi 400 */
  const refOf = (b: Record<string, unknown> | null) => {
    const ref = typeof b?.link === 'string' ? parseAppLink(b.link) : null;
    if (!ref) return { error: tr('Không đọc được link — dán link App Store / Google Play của 1 app') };
    const country = ref.country ?? (typeof b?.country === 'string' ? b.country.toUpperCase() : 'US');
    if (!COUNTRIES.some((c) => c.code === country)) return { error: tr('Nước không hỗ trợ: {country}', { country }) };
    return { ref: { ...ref, country } };
  };

  api.get('/list', (c) => c.json({ audits: listAudits(o.db()) }));

  api.post('/read', async (c) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const r = refOf(await body(c.req.raw));
    if (!r.ref) return c.json({ error: r.error }, 400);
    const signal = AbortSignal.any([c.req.raw.signal, AbortSignal.timeout(60_000)]);
    try {
      const listing = await (o.deps?.listing ?? fetchListing)(r.ref, signal);
      return c.json({ listing, chips: await suggestChips(o.db(), listing, signal, o.deps?.suggest) });
    } catch (e) { return err(e, signal); }
  });

  api.post('/run', async (c) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const b = await body(c.req.raw);
    const r = refOf(b);
    if (!r.ref) return c.json({ error: r.error }, 400);
    const terms = Array.isArray(b?.terms) ? b.terms.filter((x): x is string => typeof x === 'string' && !!x.trim()).slice(0, MAX_TERMS) : [];
    if (!terms.length) return c.json({ error: tr('Chọn ít nhất 1 keyword') }, 400);
    const signal = AbortSignal.any([c.req.raw.signal, AbortSignal.timeout(180_000)]);
    try { return c.json(await runAudit(o.db(), { ref: r.ref, terms }, signal, o.deps)); }
    catch (e) { return err(e, signal); }
  });

  api.post('/rivals', async (c) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const b = await body(c.req.raw);
    const id = Number(b?.id);
    const v = Number.isInteger(id) ? getAudit(o.db(), id) : null;
    if (!v) return c.json({ error: tr('Không thấy lần audit này') }, 404);
    const signal = AbortSignal.any([c.req.raw.signal, AbortSignal.timeout(90_000)]);
    try {
      let pasted: RivalHit[] = [];
      const text = typeof b?.pasted === 'string' ? b.pasted.slice(0, 20_000) : '';
      if (text.trim() && v.listing.store === 'appstore') {
        const p = await pastedSimilar(v.listing.id, v.listing.country, text, signal);
        pasted = p.apps.map((a) => ({ store: a.store, id: a.id, title: a.title, developer: a.developer, iconUrl: a.iconUrl, url: a.url, rating: a.rating, ratingsCount: a.ratingsCount }));
      }
      return c.json(await auditRivals(o.db(), id, signal, o.deps, pasted));
    } catch (e) { return err(e, signal); }
  });

  api.get('/:id', (c) => {
    const v = getAudit(o.db(), Number(c.req.param('id')));
    return v ? c.json(v) : c.json({ error: tr('Không thấy lần audit này') }, 404);
  });

  return api;
}
```

Trong `web/src/server/app.ts`:

```ts
import { auditApi } from './audit-api';
// … cạnh api.route('/reviews', reviewsApi({ db }));
api.route('/audit', auditApi({ db }));
```

- [ ] **Step 4: Chạy test, phải qua**

Run: `npx vitest run tests/app-audit.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit (khi anh cho phép)**

```bash
git add web/src/server/audit-api.ts web/src/server/app.ts web/tests/app-audit.test.ts
git commit -m "feat(web): /api/audit read, run, rivals, list (mục 30)"
```

---

### Task 7: Giao diện — thẻ thứ 7, ô nhập, chip, kết quả, đối thủ

**Files:**
- Modify: `web/src/client/YoutubeEntry.tsx` (`AppMode` + `APP_ENTRIES` + icon `audit`)
- Modify: `web/src/client/HomePage.tsx` (`MODES`, panel, "7 việc")
- Modify: `web/src/client/AppInspect.tsx` (nút Audit app này)
- Create: `web/src/client/AppAudit.tsx`, `web/src/client/AuditResult.tsx`, `web/src/client/AuditRivals.tsx`
- Create: `web/src/locales/en-text-app-audit.ts`; Modify: `web/src/locales/en-text.ts`, `web/src/locales/en-text-review-mining.ts`

**Interfaces:**
- Consumes: API Task 6; kiểu `Listing`, `Chip`, `AuditView` (import type từ `@/lib/app-audit-core` và `@/lib/app-audit` — chỉ `import type`, không kéo code máy chủ vào client); `COUNTRIES`; `InfoTip`
- Produces: `export function AppAudit({ onRunning }: { onRunning: (since: number | null) => void })`; `export function AuditResult({ v }: { v: AuditView })`; `export function AuditRivals({ v }: { v: AuditView })`; `export function fixText(f: Fix): string`

- [ ] **Step 1: Gắn mode + thẻ**

`web/src/client/YoutubeEntry.tsx`:

```ts
export type AppMode = 'research' | 'explore' | 'hunt' | 'app' | 'reviews' | 'compare' | 'audit';
// thêm cuối APP_ENTRIES:
  { mode: 'audit', title: tx('Audit app của bạn'), what: tx('Dán link app bạn đã có trên store: chấm trang store + hạng keyword /100, thấy việc nên sửa trước, kéo đối thủ sang So sánh app.'), icon: 'audit' },
```

Thêm `'audit'` vào kiểu `Icon` và vào `ICON`:

```tsx
  audit: <><rect x="5" y="3" width="14" height="18" rx="2" /><path d="M9 3v2h6V3" /><path d="M8.5 13l2.5 2.5 4.5-5" /></>,
```

`web/src/client/HomePage.tsx`:

```tsx
const MODES: AppMode[] = ['research', 'explore', 'hunt', 'app', 'reviews', 'compare', 'audit'];
// header: tr('6 việc bên dưới chạy không cần AI') → tr('7 việc bên dưới chạy không cần AI')
// sau panel compare:
      {opened.has('audit') && <div hidden={mode !== 'audit'}><AppAudit onRunning={(since) => report('audit', since)} /></div>}
```

`web/src/client/AppInspect.tsx` — cạnh link "So sánh với đối thủ" (dòng ~158):

```tsx
        <Link to={`/?mode=audit&link=${encodeURIComponent(v.app.url)}&country=${v.country}`} className="ui-button ui-button--secondary !min-h-9 !py-1 text-sm">{tr('Audit app này')}</Link>
```

(`v` là biến view đang dùng ở chỗ đó; nếu tên khác, dùng đúng biến đang giữ `AppInspectView`.)

- [ ] **Step 2: Viết `AppAudit.tsx`** (form + chip + chạy + lần cũ)

```tsx
// web/src/client/AppAudit.tsx
import { useEffect, useRef, useState } from 'react';
import { useSearchParams } from 'react-router';
import { tr } from '@/lib/i18n';
import { COUNTRIES } from '@/lib/countries';
import { parseAppLink } from '@/lib/app-inspect-core';
import { MAX_TERMS, type Chip, type Listing } from '@/lib/app-audit-core';
import type { AuditView } from '@/lib/app-audit';
import { InfoTip } from '@/components/InfoTip';
import { AuditResult } from './AuditResult';
import { AuditRivals } from './AuditRivals';

type Past = { id: number; title: string; iconUrl: string | null; country: string; score: number | null; createdAt: string };
const DOT: Record<Chip['source'], string> = { name: 'bg-blue-500', suggest: 'bg-emerald-500', rival: 'bg-amber-500' };

async function postJson<T>(url: string, body: unknown, signal?: AbortSignal): Promise<T> {
  const res = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal });
  const j = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(j.error ?? `HTTP ${res.status}`);
  return j as T;
}

/** Plan 2 mục 30 · Audit 1 app: dán link → chip → chạy → điểm + việc nên sửa → lấy đối thủ. */
export function AppAudit({ onRunning }: { onRunning: (since: number | null) => void }) {
  const [params] = useSearchParams();
  const [link, setLink] = useState('');
  const [country, setCountry] = useState('US');
  const [listing, setListing] = useState<Listing | null>(null);
  const [chips, setChips] = useState<Chip[]>([]);
  const [off, setOff] = useState<Set<string>>(new Set());
  const [extra, setExtra] = useState('');
  const [view, setView] = useState<AuditView | null>(null);
  const [past, setPast] = useState<Past[]>([]);
  const [busy, setBusy] = useState<'read' | 'run' | null>(null);
  const [error, setError] = useState('');
  const stop = useRef<AbortController | null>(null);

  const loadPast = () => fetch('/api/audit/list').then((r) => r.json()).then((j) => setPast(j.audits ?? []), () => undefined);
  useEffect(() => { loadPast(); }, []);
  // mở thẳng từ Soi 1 app: ?mode=audit&link=…&country=…
  useEffect(() => {
    const l = params.get('link');
    if (params.get('mode') !== 'audit' || !l || !parseAppLink(l)) return;
    setLink(l);
    const cc = (params.get('country') ?? 'US').toUpperCase();
    setCountry(cc);
    void read(l, cc);
  }, [params]); // eslint-disable-line react-hooks/exhaustive-deps

  const read = async (l = link, cc = country) => {
    setBusy('read'); setError(''); setView(null);
    try {
      const r = await postJson<{ listing: Listing; chips: Chip[] }>('/api/audit/read', { link: l, country: cc });
      setListing(r.listing); setChips(r.chips); setOff(new Set());
    } catch (e) { setError((e as Error).message); } finally { setBusy(null); }
  };
  const terms = chips.filter((c) => !off.has(c.term)).map((c) => c.term).slice(0, MAX_TERMS);
  const run = async () => {
    stop.current = new AbortController();
    setBusy('run'); setError(''); onRunning(Date.now());
    try { setView(await postJson<AuditView>('/api/audit/run', { link, country, terms }, stop.current.signal)); loadPast(); }
    catch (e) { setError(stop.current.signal.aborted ? tr('Đã dừng') : (e as Error).message); }
    finally { setBusy(null); onRunning(null); }
  };
  const addChip = () => {
    const t = extra.trim().toLowerCase();
    if (t && !chips.some((c) => c.term === t)) setChips([...chips, { term: t, source: 'name' }]);
    setExtra('');
  };
  const open = (id: number) => fetch(`/api/audit/${id}`).then((r) => r.json()).then((v: AuditView) => { setView(v); setListing(v.listing); setLink(v.listing.url); setCountry(v.listing.country); });

  return (
    <div className="space-y-4">
      <section className="space-y-3 rounded-2xl border border-zinc-200 bg-surface p-5">
        <h2 className="flex items-center gap-2 text-lg font-semibold">{tr('Audit app của bạn')}
          <InfoTip text={tr('Đọc trang store của app (tên, phụ đề, mô tả, ảnh, sao, ngày cập nhật) rồi tìm từng keyword trên store đúng nước đã chọn, lấy top 50. Điểm là quy ước của ShotMatic, không phải số store công bố. Phần store không trả dữ liệu ghi "chưa đo" và không tính vào điểm.')} /></h2>
        <div className="flex min-w-0 flex-wrap gap-2">
          <input value={link} onChange={(e) => setLink(e.target.value)} placeholder={tr('Link app của bạn trên Google Play hoặc App Store')}
            className="ui-input min-w-0 flex-1" onKeyDown={(e) => e.key === 'Enter' && read()} />
          <select value={country} onChange={(e) => setCountry(e.target.value)} className="ui-input shrink-0">
            {COUNTRIES.map((c) => <option key={c.code} value={c.code}>{c.code}</option>)}
          </select>
          <button className="ui-button shrink-0" disabled={!parseAppLink(link) || !!busy} onClick={() => read()}>{busy === 'read' ? tr('Đang đọc…') : tr('Đọc app')}</button>
        </div>
        {listing && (
          <div className="space-y-2">
            <div className="flex min-w-0 items-center gap-3">
              {listing.iconUrl && <img src={listing.iconUrl} alt="" className="size-10 shrink-0 rounded-xl" />}
              <div className="min-w-0"><p className="truncate font-medium" title={listing.title}>{listing.title}</p>
                <p className="truncate text-sm text-zinc-500" title={listing.subtitle ?? ''}>{listing.subtitle ?? tr('Phụ đề: chưa đo')}</p></div>
            </div>
            <p className="text-sm text-zinc-600">{tr('Keyword sẽ tra · bỏ bằng ×, thêm bằng ô bên dưới · tối đa {n}', { n: MAX_TERMS })}</p>
            <div className="flex flex-wrap gap-2">
              {chips.map((c) => (
                <span key={c.term} className={`chip inline-flex max-w-full items-center gap-1.5 ${off.has(c.term) ? 'opacity-40 line-through' : ''}`}>
                  <span className={`size-2 shrink-0 rounded-full ${DOT[c.source]}`} aria-hidden />
                  <span className="truncate" title={c.term}>{c.term}</span>
                  <button className="shrink-0 text-zinc-500" aria-label={tr('Bỏ')} onClick={() => setOff((s) => { const n = new Set(s); if (n.has(c.term)) n.delete(c.term); else n.add(c.term); return n; })}>×</button>
                </span>
              ))}
            </div>
            <div className="flex min-w-0 flex-wrap gap-2">
              <input value={extra} onChange={(e) => setExtra(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && addChip()} placeholder={tr('Thêm keyword rồi Enter')} className="ui-input min-w-0 flex-1" />
              {busy === 'run'
                ? <button className="ui-button ui-button--secondary shrink-0" onClick={() => stop.current?.abort()}>{tr('Dừng')}</button>
                : <button className="ui-button shrink-0" disabled={!terms.length || !!busy} onClick={run}>{tr('Chạy audit · {n} keyword', { n: terms.length })}</button>}
            </div>
            {busy === 'run' && <p className="text-sm text-zinc-500">{tr('Đang tìm từng keyword trên store, khoảng 30–60 giây…')}</p>}
          </div>
        )}
        {error && <p className="text-sm text-red-600">{error}</p>}
        {past.length > 0 && !view && (
          <div className="space-y-1">
            <p className="text-sm text-zinc-600">{tr('Lần audit trước')}</p>
            <div className="flex flex-wrap gap-2">
              {past.map((p) => (
                <button key={p.id} onClick={() => open(p.id)} className="chip inline-flex max-w-full items-center gap-1.5">
                  {p.iconUrl && <img src={p.iconUrl} alt="" className="size-4 shrink-0 rounded" />}
                  <span className="truncate" title={p.title}>{p.title}</span>
                  <span className="shrink-0 text-zinc-500">{p.country} · {p.score ?? '—'}</span>
                </button>
              ))}
            </div>
          </div>
        )}
      </section>
      {view && <AuditResult v={view} />}
      {view && <AuditRivals v={view} onChips={(more) => setChips((c) => [...c, ...more.filter((m) => !c.some((x) => x.term === m.term))])} />}
    </div>
  );
}
```

Ghi chú: class `ui-input`, `ui-button`, `chip` lấy theo `globals.css`. Nếu `chip` không có, dùng class mà `ReviewMining.tsx` đang dùng cho chip nước.

- [ ] **Step 3: Viết `AuditResult.tsx`**

```tsx
// web/src/client/AuditResult.tsx
import { tr } from '@/lib/i18n';
import type { Fix, PartKey } from '@/lib/app-audit-core';
import type { AuditView } from '@/lib/app-audit';
import { InfoTip } from '@/components/InfoTip';

const PART: Record<PartKey, string> = { name: 'Tên & phụ đề', description: 'Mô tả', visuals: 'Hình ảnh & rating', ranks: 'Hạng keyword' };
const PART_TIP: Record<PartKey, string> = {
  name: 'Dùng bao nhiêu % giới hạn ký tự (đủ khi ≥ 70%) · keyword gần top 10 nhất (hạng 11–50) đã có trong tên chưa · tên và phụ đề có lặp chữ không.',
  description: 'Đủ 1.000 ký tự chưa · keyword hạng tốt nhất có trong 3 dòng đầu không.',
  visuals: 'Số ảnh (đủ khi ≥ 6) · có video không · sao (3,5 → 0, 4,5 → đủ) · cập nhật trong 30 / 90 / 180 ngày.',
  ranks: '70% theo tỉ lệ keyword vào top 10, 30% theo tỉ lệ vào top 50. Keyword chưa đo không tính.',
};

export function fixText(f: Fix): string {
  const p = f.params;
  switch (f.key) {
    case 'titleFill': return tr('Tên mới dùng {used}/{limit} ký tự — thêm keyword vào tên.', p);
    case 'subtitleFill': return tr('Phụ đề mới dùng {used}/{limit} ký tự.', p);
    case 'termInName': return tr('Keyword "{term}" bạn đứng hạng {rank}, nhưng tên và phụ đề chưa có chữ này.', p);
    case 'noRepeat': return tr('Tên và phụ đề lặp chữ: {words} — lặp không giúp lên hạng, đổi sang keyword khác.', p);
    case 'descLength': return tr('Mô tả mới {chars} ký tự — viết dài hơn, đủ khoảng 1.000.', p);
    case 'termEarly': return tr('Đưa keyword "{term}" vào 3 dòng đầu của mô tả.', p);
    case 'shots': return tr('Mới có {n} ảnh chụp màn hình — nên có ít nhất 6.', p);
    case 'video': return tr('Chưa có video giới thiệu.');
    case 'rating': return tr('Sao đang {rating} — xin đánh giá từ người dùng hài lòng, sửa lỗi bị chê nhiều nhất.', p);
    case 'fresh': return tr('Cập nhật lần cuối {days} ngày trước — ra bản mới.', p);
    case 'ranks': return tr('Chỉ {top10}/{measured} keyword vào top 10 — xem bảng hạng bên dưới để chọn keyword đưa vào tên.', p);
  }
}

const dot = (rank: number | null, measured: boolean) => (!measured ? 'bg-zinc-300' : rank === null ? 'bg-zinc-400' : rank <= 10 ? 'bg-emerald-500' : 'bg-amber-500');

export function AuditResult({ v }: { v: AuditView }) {
  const s = v.score;
  return (
    <section className="space-y-5 rounded-2xl border border-zinc-200 bg-surface p-5">
      <div className="flex min-w-0 items-end gap-4">
        <p className="shrink-0 text-5xl font-semibold">{s.total ?? '—'}<span className="text-xl text-zinc-500">/100</span></p>
        <p className="min-w-0 pb-1 text-zinc-700">{tr('{top10}/{measured} keyword vào top 10 · {top50}/{measured} vào top 50', { top10: s.top10, top50: s.top50, measured: s.measured })}</p>
      </div>
      <div className="space-y-2">
        {s.parts.map((p) => (
          <div key={p.key} className="space-y-1">
            <div className="flex min-w-0 items-center justify-between gap-2 text-sm">
              <span className="flex min-w-0 items-center gap-1.5">{tr(PART[p.key])}<InfoTip text={tr(PART_TIP[p.key])} /></span>
              <span className="shrink-0 whitespace-nowrap text-zinc-600">{p.score === null ? tr('chưa đo') : `${p.score}/${p.weight}`}</span>
            </div>
            <div className="h-2 rounded-full bg-zinc-100"><div className="h-2 rounded-full bg-[var(--accent-solid)]" style={{ width: `${p.score === null ? 0 : (p.score / p.weight) * 100}%` }} /></div>
          </div>
        ))}
      </div>
      {v.fixes.length > 0 && (
        <div className="space-y-2">
          <h3 className="font-semibold">{tr('Nên sửa trước')}</h3>
          <ol className="space-y-1.5">
            {v.fixes.map((f, i) => (
              <li key={f.key} className="flex min-w-0 gap-2 text-sm">
                <span className="shrink-0 font-semibold text-zinc-500">{i + 1}.</span>
                <span className="min-w-0 flex-1">{fixText(f)}</span>
                <span className="shrink-0 whitespace-nowrap text-emerald-700">+{f.gain}</span>
              </li>
            ))}
          </ol>
        </div>
      )}
      <div className="space-y-2">
        <h3 className="font-semibold">{tr('Hạng keyword')}</h3>
        <div className="overflow-x-auto">
          <table className="w-full table-fixed text-sm">
            <colgroup><col className="w-[40%]" /><col className="w-24" /><col /></colgroup>
            <thead><tr className="text-left text-zinc-500"><th className="py-1">{tr('Keyword')}</th><th className="py-1 text-right">{tr('Hạng')}</th><th className="py-1 pl-4">{tr('3 app đầu')}</th></tr></thead>
            <tbody>
              {v.ranks.map((r) => (
                <tr key={r.term} className="border-t border-zinc-100">
                  <td className="truncate py-1.5" title={r.term}>{r.term}</td>
                  <td className="whitespace-nowrap py-1.5 text-right"><span className={`mr-1.5 inline-block size-2 rounded-full ${dot(r.rank, r.measured)}`} />
                    {!r.measured ? tr('chưa đo') : r.rank === null ? tr('ngoài 50') : `#${r.rank}`}</td>
                  <td className="py-1.5 pl-4"><div className="flex min-w-0 gap-1.5">
                    {r.top.slice(0, 3).map((a) => a.iconUrl
                      ? <img key={a.id} src={a.iconUrl} alt={a.title} title={a.title} className="size-6 shrink-0 rounded-md" />
                      : <span key={a.id} className="truncate" title={a.title}>{a.title}</span>)}
                  </div></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
```

`tr(text, params)` nhận object số / chuỗi: nếu chữ ký `tr` chỉ nhận `Record<string, string | number>` thì `f.params` đã đúng kiểu.

- [ ] **Step 4: Viết `AuditRivals.tsx`**

```tsx
// web/src/client/AuditRivals.tsx
import { useState } from 'react';
import { Link } from 'react-router';
import { CC_MAX } from '@/lib/competitor-compare-core';
import { tr } from '@/lib/i18n';
import type { Chip, RivalRow } from '@/lib/app-audit-core';
import type { AuditView } from '@/lib/app-audit';

type Rivals = { selfDbId: number; rivals: (RivalRow & { dbId: number })[]; chips: Chip[] };
/** So sánh app nhận tối đa CC_MAX (= 4) app: mình + 3 đối thủ. */
const PICK_MAX = CC_MAX - 1;

export function AuditRivals({ v, onChips }: { v: AuditView; onChips: (c: Chip[]) => void }) {
  const [data, setData] = useState<Rivals | null>(null);
  const [pick, setPick] = useState<Set<number>>(new Set());
  const [pasted, setPasted] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const load = async () => {
    setBusy(true); setError('');
    try {
      const res = await fetch('/api/audit/rivals', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id: v.id, pasted }) });
      const j = await res.json();
      if (!res.ok) throw new Error(j.error);
      setData(j); setPick(new Set(j.rivals.slice(0, PICK_MAX).map((r: { dbId: number }) => r.dbId))); onChips(j.chips);
    } catch (e) { setError((e as Error).message); } finally { setBusy(false); }
  };
  const toggle = (id: number) => setPick((s) => { const n = new Set(s); if (n.has(id)) n.delete(id); else if (n.size < PICK_MAX) n.add(id); return n; });
  const compareUrl = data ? `/?mode=compare&apps=${[data.selfDbId, ...pick].join(',')}&country=${v.listing.country}` : '';

  return (
    <section className="space-y-3 rounded-2xl border border-zinc-200 bg-surface p-5">
      <div className="flex min-w-0 flex-wrap items-center justify-between gap-2">
        <h3 className="font-semibold">{tr('Đối thủ')}</h3>
        <button className="ui-button ui-button--secondary shrink-0" disabled={busy} onClick={load}>{busy ? tr('Đang lấy…') : tr('Lấy đối thủ')}</button>
      </div>
      {v.listing.store === 'appstore' && (
        <textarea value={pasted} onChange={(e) => setPasted(e.target.value)} rows={2} className="ui-input w-full"
          placeholder={tr('App Store không có danh sách app tương tự — dán link hoặc bôi đen khối "You Might Also Like" vào đây (tuỳ chọn)')} />
      )}
      {error && <p className="text-sm text-red-600">{error}</p>}
      {data && (
        <>
          <ul className="space-y-1.5">
            {data.rivals.map((r) => (
              <li key={r.dbId}>
                <label className="flex min-w-0 cursor-pointer items-center gap-3 text-sm">
                  <input type="checkbox" className="shrink-0" checked={pick.has(r.dbId)} onChange={() => toggle(r.dbId)} />
                  {r.app.iconUrl && <img src={r.app.iconUrl} alt="" className="size-7 shrink-0 rounded-lg" />}
                  <span className="min-w-0 flex-1 truncate" title={r.app.title}>{r.app.title}</span>
                  <span className="shrink-0 whitespace-nowrap text-zinc-600">{tr('{n} keyword trùng', { n: r.overlap })}</span>
                  <span className="shrink-0 whitespace-nowrap text-zinc-500">{r.app.rating?.toFixed(1) ?? '—'}★</span>
                  <span className="shrink-0 whitespace-nowrap text-xs text-zinc-500">{r.sources.map((s) => (s === 'above' ? tr('đứng trên') : tr('tương tự'))).join(' · ')}</span>
                </label>
              </li>
            ))}
          </ul>
          <Link to={compareUrl} className={`ui-button ${pick.size ? '' : 'pointer-events-none opacity-50'}`}>{tr('Đẩy sang So sánh app · {n} app', { n: pick.size + 1 })}</Link>
        </>
      )}
    </section>
  );
}
```

Ghi chú: trang So sánh app (`CompareCompetitorsPage.tsx`) đọc `apps` (id DB) và cắt ở `CC_MAX` = 4 (`lib/competitor-compare-core.ts`), nên tick tối đa 3 đối thủ. Spec đã sửa "3–5" thành "tối đa 3".

- [ ] **Step 5: Chữ tiếng Anh**

`web/src/locales/en-text-review-mining.ts`: đổi khoá `"6 việc bên dưới chạy không cần AI"` thành `"7 việc bên dưới chạy không cần AI": "The 7 tasks below run without AI"`.

Tạo `web/src/locales/en-text-app-audit.ts` với **mọi** chuỗi `tr()` / `tx()` mới ở Step 1–4 (gom bằng `grep -ohE "t[rx]\('[^']+'" web/src/client/AppAudit.tsx web/src/client/AuditResult.tsx web/src/client/AuditRivals.tsx` + 2 chuỗi thẻ ở `YoutubeEntry.tsx` + `'Audit app này'` + các chuỗi lỗi ở `audit-api.ts`):

```ts
/** Bản tiếng Anh cho Audit 1 app (Plan 2 · mục 30, 2026-11-17). Gộp vào `enText` (en-text.ts). */
export const appAuditEnText: Record<string, string> = {
  "Audit app của bạn": "Audit my app",
  "Dán link app bạn đã có trên store: chấm trang store + hạng keyword /100, thấy việc nên sửa trước, kéo đối thủ sang So sánh app.": "Paste your live app: score its store page and keyword ranks /100, see what to fix first, pull rivals into Compare.",
  "Audit app này": "Audit this app",
  "Link app của bạn trên Google Play hoặc App Store": "Your app link on Google Play or the App Store",
  "Đọc app": "Read app",
  "Đang đọc…": "Reading…",
  "Phụ đề: chưa đo": "Subtitle: not measured",
  "Keyword sẽ tra · bỏ bằng ×, thêm bằng ô bên dưới · tối đa {n}": "Keywords to check · remove with ×, add below · up to {n}",
  "Bỏ": "Remove",
  "Thêm keyword rồi Enter": "Add a keyword, then Enter",
  "Dừng": "Stop",
  "Chạy audit · {n} keyword": "Run audit · {n} keywords",
  "Đang tìm từng keyword trên store, khoảng 30–60 giây…": "Searching each keyword on the store, about 30–60 seconds…",
  "Lần audit trước": "Past audits",
  "Đọc trang store của app (tên, phụ đề, mô tả, ảnh, sao, ngày cập nhật) rồi tìm từng keyword trên store đúng nước đã chọn, lấy top 50. Điểm là quy ước của ShotMatic, không phải số store công bố. Phần store không trả dữ liệu ghi \"chưa đo\" và không tính vào điểm.": "Reads your store page (name, subtitle, description, screenshots, rating, last update), then searches each keyword in the chosen country's store, top 50. The score is ShotMatic's own rule, not a store number. Anything the store doesn't return shows \"not measured\" and isn't counted.",
  "Tên & phụ đề": "Name & subtitle",
  "Mô tả": "Description",
  "Hình ảnh & rating": "Visuals & rating",
  "Hạng keyword": "Keyword ranks",
  "chưa đo": "not measured",
  "ngoài 50": "not in top 50",
  "Nên sửa trước": "Fix first",
  "Keyword": "Keyword",
  "Hạng": "Rank",
  "3 app đầu": "Top 3 apps",
  "{top10}/{measured} keyword vào top 10 · {top50}/{measured} vào top 50": "{top10}/{measured} keywords in the top 10 · {top50}/{measured} in the top 50",
  "Tên mới dùng {used}/{limit} ký tự — thêm keyword vào tên.": "Name uses only {used}/{limit} characters — add a keyword to it.",
  "Phụ đề mới dùng {used}/{limit} ký tự.": "Subtitle uses only {used}/{limit} characters.",
  "Keyword \"{term}\" bạn đứng hạng {rank}, nhưng tên và phụ đề chưa có chữ này.": "You rank #{rank} for \"{term}\", but your name and subtitle don't contain it.",
  "Tên và phụ đề lặp chữ: {words} — lặp không giúp lên hạng, đổi sang keyword khác.": "Name and subtitle repeat: {words} — repeats don't help ranking, use another keyword.",
  "Mô tả mới {chars} ký tự — viết dài hơn, đủ khoảng 1.000.": "Description is only {chars} characters — aim for about 1,000.",
  "Đưa keyword \"{term}\" vào 3 dòng đầu của mô tả.": "Put \"{term}\" in the first 3 lines of the description.",
  "Mới có {n} ảnh chụp màn hình — nên có ít nhất 6.": "Only {n} screenshots — use at least 6.",
  "Chưa có video giới thiệu.": "No preview video yet.",
  "Sao đang {rating} — xin đánh giá từ người dùng hài lòng, sửa lỗi bị chê nhiều nhất.": "Rating is {rating} — ask happy users to rate, fix the most-complained bug.",
  "Cập nhật lần cuối {days} ngày trước — ra bản mới.": "Last updated {days} days ago — ship an update.",
  "Chỉ {top10}/{measured} keyword vào top 10 — xem bảng hạng bên dưới để chọn keyword đưa vào tên.": "Only {top10}/{measured} keywords in the top 10 — use the rank table below to pick keywords for your name.",
  "Dùng bao nhiêu % giới hạn ký tự (đủ khi ≥ 70%) · keyword gần top 10 nhất (hạng 11–50) đã có trong tên chưa · tên và phụ đề có lặp chữ không.": "Share of the character limit used (full at ≥ 70%) · is your nearest-to-top-10 keyword (rank 11–50) in the name · do name and subtitle repeat words.",
  "Đủ 1.000 ký tự chưa · keyword hạng tốt nhất có trong 3 dòng đầu không.": "Reaches 1,000 characters · is your best-ranked keyword in the first 3 lines.",
  "Số ảnh (đủ khi ≥ 6) · có video không · sao (3,5 → 0, 4,5 → đủ) · cập nhật trong 30 / 90 / 180 ngày.": "Screenshots (full at ≥ 6) · has a video · rating (3.5 → 0, 4.5 → full) · updated within 30 / 90 / 180 days.",
  "70% theo tỉ lệ keyword vào top 10, 30% theo tỉ lệ vào top 50. Keyword chưa đo không tính.": "70% from the share of keywords in the top 10, 30% from the share in the top 50. Unmeasured keywords don't count.",
  "Đối thủ": "Rivals",
  "Lấy đối thủ": "Fetch rivals",
  "Đang lấy…": "Fetching…",
  "App Store không có danh sách app tương tự — dán link hoặc bôi đen khối \"You Might Also Like\" vào đây (tuỳ chọn)": "The App Store has no similar-apps list — paste links or the \"You Might Also Like\" block here (optional)",
  "{n} keyword trùng": "{n} shared keywords",
  "đứng trên": "ranks above",
  "tương tự": "similar",
  "Đẩy sang So sánh app · {n} app": "Send to Compare apps · {n} apps",
  "Chọn ít nhất 1 keyword": "Pick at least 1 keyword",
  "Không thấy lần audit này": "Audit not found",
};
```

`web/src/locales/en-text.ts`: `import { appAuditEnText } from './en-text-app-audit';` và thêm `...appAuditEnText,` cạnh `...reviewMiningEnText,`.

- [ ] **Step 6: Kiểm kiểu + lint + test**

Run (gốc repo): `npm run check`
Expected: typecheck, lint, test đều xanh. Lỗi kiểu hay gặp: `tr(text, f.params)` — nếu `tr` đòi `Record<string, string | number>` mà `params` là `{}` rỗng thì vẫn hợp.

- [ ] **Step 7: Xem tận mắt** (theo CLAUDE.md "Soát trước khi xong")

1. `preview_start` tên `niche-radar`, mở `/?mode=audit`.
2. Dán 1 app Play thật (vd `com.habitnow`… lấy link Play thật của 1 app habit tracker) ở US → Đọc app → Chạy audit. Kết quả có số, 4 thanh, việc nên sửa, bảng hạng; ô nào thiếu ghi "chưa đo".
3. Lặp với 1 app App Store thật: phụ đề ghi "chưa đo", thanh Tên & phụ đề vẫn có số.
4. Bấm Lấy đối thủ → tick 3 app (ô thứ 4 không tick được) → Đẩy sang So sánh app: trang So sánh mở đúng 4 app.
5. Soi ở 960px và 1340px, English lẫn tiếng Việt, sáng lẫn tối: 1 cột, không cuộn ngang cả trang (`document.documentElement.scrollWidth === innerWidth`), tên app dài bị cắt có `title`.
6. Soi 1 app → nút Audit app này mở thẳng tab audit đã đọc sẵn app.

- [ ] **Step 8: Commit (khi anh cho phép)**

```bash
git add web/src/client web/src/locales
git commit -m "feat(web): audit app tab — chips, score, fixes, rivals to compare (mục 30)"
```

---

### Task 8: Tài liệu + CHANGELOG

**Files:**
- Modify: `docs/web/phase-plan2-30-audit-app.md` (chip trạng thái → "Code … · chờ anh soát", ghi số đo thật: thời gian chạy 15 keyword ở Play / App Store, số lần gặp 429)
- Modify: `docs/web/index.md` (chip mục 30)
- Modify: `CHANGELOG.md` (dòng **Web** dưới `[Unreleased]`: tên file, bảng `app_audits`, API `/api/audit/*`)

- [ ] **Step 1: Sửa 3 file trên với số đo thật lấy từ Task 7 Step 7** (không có số thì ghi "chưa đo").
- [ ] **Step 2:** Run (gốc repo): `npm run docs:build` → Expected: build xong, không `Aborted`.
- [ ] **Step 3: Commit (khi anh cho phép)**

```bash
git add docs CHANGELOG.md
git commit -m "docs(web): mục 30 audit app — code status and measured times"
```
