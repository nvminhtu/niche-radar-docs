# Plan 2 · mục 23 — Trang YouTube gom 3 nhóm + chạy nhiều lượt — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Trang YouTube chỉ còn 3 thẻ nhóm (Tìm ngách · Săn kênh · Soi kênh) có chip chế độ. Ô nhập nhận nhiều dòng. Mọi lượt YouTube vào 1 hàng chờ ở máy chủ, chạy tối đa 3 luồng cùng lúc, và hiện thành dải chip bấm mở được.

**Architecture:** Sổ việc trong bộ nhớ `web/src/lib/social-jobs.ts` có thêm trạng thái `queued` / `cancelled`, khoá chống trùng (`dedupe`) và việc cha (`parent`). Module mới `web/src/lib/yt-queue.ts` giữ 1 bể luồng chung cho YouTube; API `/api/social/*` và MCP `/api/mcp/youtube/*` cùng đẩy việc vào đó. Trang web không tự lặp request nữa: gửi cả danh sách 1 lần (`/youtube/batch`, `/youtube/gather`), rồi đọc trạng thái qua `/api/activity` đang hỏi mỗi 4 giây.

**Tech Stack:** TypeScript · Hono (máy chủ) · React 19 + Tailwind v4 · Vitest (`renderToStaticMarkup` cho UI) · youtubei.js.

**Spec:** [`docs/web/phase-plan2-23-youtube-gom-nhom-chay-nhieu.md`](../../web/phase-plan2-23-youtube-gom-nhom-chay-nhieu.md)

## Global Constraints

- Mọi chữ trên UI bằng tiếng Việt qua `tr()` / `tx()`. Mỗi chữ mới phải có bản tiếng Anh trong `web/src/locales/en-text-yt-queue.ts`, gộp vào `web/src/locales/en-text.ts`.
- Không đổi khoá chế độ: `niche` · `hunt` · `trend` · `channel` · `compare`. Không đổi `localStorage` `niche-radar.youtubeMode`.
- Tối đa / lần: Tìm ý tưởng **10** keyword · Săn kênh nhỏ **5** chủ đề · Soi từng kênh **10** link · So kênh **2–3** link (giữ `COMPARE_MIN` / `COMPARE_MAX`).
- Số luồng: `YT_CONCURRENCY`, mặc định **3**, chỉ nhận số nguyên 1–8. Số này **chưa đo**, Task 8 sẽ đo rồi chốt.
- Việc đang chạy thì không huỷ được. Chỉ huỷ được việc còn `queued`.
- Hai lượt giống hệt nhau (cùng chế độ + đầu vào, không tính `force`) mà lượt trước chưa xong → trả mã việc của lượt trước, không chạy lại.
- Amazon và Google Maps **giữ nguyên** khoá 409 theo tab.
- Layout theo `CLAUDE.md` của repo: đứng được từ 960px tới 1920px, chữ dài `truncate` + `title`, con flex có `min-w-0`, chip/nút có `shrink-0`, mặt thẻ `bg-surface`, xám dùng `zinc-*`. Soát cả sáng lẫn tối.
- Không hiện số phase / số mục trên UI.
- Trước khi xong: `npm run check` ở gốc repo xanh, `npm run docs:build` xanh.
- **Commit:** chỉ commit khi anh Tu cho phép. Working tree đang có sửa đổi của session khác trong các file dùng chung (`SocialPage.tsx`, `social-api.ts`…), nên khi commit chỉ `git add` đúng file của task, và `git add -p` với file dùng chung.

## File Structure

| File | Việc | Trách nhiệm |
|---|---|---|
| `web/src/lib/social-jobs.ts` | Sửa | Sổ việc: thêm `state`, `dedupe`, `parent`, hàm `socialJobQueue` / `socialJobRun` / `socialJobCancel` / `socialJobInFlight` |
| `web/src/lib/yt-queue.ts` | Tạo | Bể luồng YouTube chung: `enqueue` / `wait` / `cancel`, `ytDedupe`, `YT_BATCH_MAX`, `ytConcurrency` |
| `web/src/lib/activity.ts` | Sửa | Việc `queued` lên Buồng lái với `status: 'pending'` |
| `web/src/server/social-api.ts` | Sửa | `/search` YouTube đi qua hàng chờ (bỏ 409), thêm `/youtube/batch`, `/youtube/gather`, `/jobs/:key/cancel` |
| `web/src/server/mcp-write-api.ts` | Sửa | `ytStart` đi qua hàng chờ, bỏ lỗi 429 |
| `web/src/lib/youtube-groups.ts` | Tạo | `YoutubeMode`, `YoutubeGroup`, `YT_GROUPS`, `groupOf`, `groupCounts` |
| `web/src/lib/multi-input.ts` | Tạo | `splitItems`, `looksLikeChannel` (dùng được cả máy chủ lẫn trang) |
| `web/src/lib/queue-chips.ts` | Tạo | `queueChips`, `gatherProgress`: biến danh sách việc thành chip |
| `web/src/client/YoutubeEntry.tsx` | Sửa | 3 thẻ nhóm + hàng chip chế độ, tách thanh dính thành `ModeSticky` |
| `web/src/components/MultiLineInput.tsx` | Tạo | Ô nhập nhiều dòng: Enter để chạy, Shift+Enter để xuống dòng, cao 1–6 dòng |
| `web/src/client/QueueStrip.tsx` | Tạo | Dải chip hàng chờ |
| `web/src/client/SocialPage.tsx` | Sửa | `SourcePanel` đếm việc theo nhóm; `ModePanel` gọi batch / gather, hiện `QueueStrip`, tự mở việc xong đầu tiên |
| `web/src/client/YoutubeHunt.tsx` · `YoutubeChannel.tsx` | Sửa | Form dùng `MultiLineInput`, gọi `onBatch` |
| `web/src/locales/en-text-yt-queue.ts` | Tạo | Bản tiếng Anh cho chữ mới |
| `web/tests/yt-queue.test.ts` · `youtube-groups.test.ts` · `multi-input.test.ts` · `queue-chips.test.ts` · `queue-strip.test.ts` · `youtube-batch-api.test.ts` | Tạo | Test |
| `web/tests/social-jobs.test.ts` · `youtube-agent.test.ts` | Sửa | Theo luật mới (không còn 429 ở MCP) |

---

### Task 1: Sổ việc có trạng thái chờ + bể luồng YouTube

**Files:**
- Modify: `web/src/lib/social-jobs.ts`
- Create: `web/src/lib/yt-queue.ts`
- Test: `web/tests/yt-queue.test.ts`, `web/tests/social-jobs.test.ts`

**Interfaces:**
- Produces:
  - `type SocialJobState = 'queued' | 'running' | 'done' | 'error' | 'cancelled'`
  - `SocialJob` thêm `state: SocialJobState; dedupe: string | null; parent: string | null`
  - `socialJobQueue(area: SocialArea, mode: string, label: string, o?: { dedupe?: string | null; parent?: string | null }, now?: number): string`
  - `socialJobRun(key: string, now?: number): void`
  - `socialJobCancel(key: string, now?: number): boolean`
  - `socialJobInFlight(area: SocialArea, dedupe: string): SocialJob | null`
  - `yt-queue.ts`: `type YtRunResult = { id: number; cached?: boolean }`, `type YtTask`, `class YtCancelled`, `createYtQueue(limit)`, `ytQueue()`, `resetYtQueue(limit?)`, `ytConcurrency(env?)`, `ytDedupe(mode, req)`, `YT_BATCH_MAX`, `type YtBatchMode`

- [ ] **Step 1: Viết test hỏng cho sổ việc**

Thêm vào cuối `describe` trong `web/tests/social-jobs.test.ts`. Sửa dòng import cho có thêm `socialJobQueue, socialJobRun, socialJobCancel, socialJobInFlight`.

```ts
  it('mục 23: việc chờ → chạy → xong; huỷ chỉ được khi còn chờ; tìm việc trùng đang bay', () => {
    const k = socialJobQueue('youtube', 'niche', 'yoga', { dedupe: 'niche:yoga' }, 1000);
    expect(listSocialJobs(1500)[0]).toMatchObject({ key: k, state: 'queued', finishedAt: null, dedupe: 'niche:yoga', parent: null });
    expect(socialJobInFlight('youtube', 'niche:yoga')?.key).toBe(k);
    socialJobRun(k, 2000);
    expect(listSocialJobs(2500)[0]).toMatchObject({ state: 'running', startedAt: 2000 });
    expect(socialJobCancel(k)).toBe(false);
    socialJobEnd(k, { resultId: 5 }, 3000);
    expect(listSocialJobs(3500)[0]).toMatchObject({ state: 'done', resultId: 5 });
    expect(socialJobInFlight('youtube', 'niche:yoga')).toBeNull();
    const q = socialJobQueue('youtube', 'hunt', 'cooking', { parent: 'social:99' }, 4000);
    expect(socialJobCancel(q, 4100)).toBe(true);
    expect(listSocialJobs(4200).find((j) => j.key === q)).toMatchObject({ state: 'cancelled', finishedAt: 4100, parent: 'social:99' });
  });
  it('mục 23: socialJobStart vẫn là việc đang chạy, lỗi → state error', () => {
    const k = socialJobStart('maps', 'maps', 'x');
    expect(listSocialJobs()[0]).toMatchObject({ state: 'running', dedupe: null, parent: null });
    socialJobEnd(k, { error: 'hỏng' });
    expect(listSocialJobs()[0]).toMatchObject({ state: 'error', error: 'hỏng' });
  });
```

- [ ] **Step 2: Chạy test, phải hỏng**

Run (ở `web/`): `npx vitest run tests/social-jobs.test.ts`
Expected: FAIL, `socialJobQueue is not a function`.

- [ ] **Step 3: Sửa `web/src/lib/social-jobs.ts`**

Thay khối type + `DONE_MAX` + `socialJobStart` + `socialJobEnd` bằng:

```ts
/** 2026-11-15 (mục 23): YouTube có hàng chờ — việc vào sổ ở `queued`, bể luồng (`yt-queue.ts`) chuyển sang `running`. */
export type SocialJobState = 'queued' | 'running' | 'done' | 'error' | 'cancelled';
export type SocialJob = {
  key: string;
  area: SocialArea;
  /** youtube: niche · hunt · trend · channel · compare · amazon: all · books · hunt · book · maps: maps */
  mode: string;
  label: string;
  state: SocialJobState;
  /** lúc vào hàng chờ; khi bắt đầu chạy thì đổi thành lúc bắt đầu */
  startedAt: number;
  finishedAt: number | null;
  /** id lượt tra đã lưu — mở được ở /<area>/<id> */
  resultId: number | null;
  error: string | null;
  /** khoá chống chạy trùng: cùng khoá mà việc trước chưa xong thì không chạy lại */
  dedupe: string | null;
  /** việc gộp (Đang trend nhiều nước · So kênh) mà việc này thuộc về */
  parent: string | null;
};

/** Giữ việc vừa xong trong chừng này phút để Buồng lái báo “vừa xong”. */
export const SOCIAL_DONE_KEEP_MS = 30 * 60_000;
/** 1 lần bấm có thể ra 10 việc → giữ đủ cho vài lần bấm */
const DONE_MAX = 60;

const jobs = new Map<string, SocialJob>();
let seq = 0;

const add = (area: SocialArea, mode: string, label: string, state: SocialJobState, o: { dedupe?: string | null; parent?: string | null }, now: number) => {
  const key = `social:${++seq}`;
  jobs.set(key, { key, area, mode, label, state, startedAt: now, finishedAt: null, resultId: null, error: null, dedupe: o.dedupe ?? null, parent: o.parent ?? null });
  return key;
};

/** Việc chạy ngay (Amazon · Maps · việc gộp). */
export function socialJobStart(area: SocialArea, mode: string, label: string, now = Date.now()): string {
  return add(area, mode, label, 'running', {}, now);
}

/** Việc vào hàng chờ, chưa chạy. */
export function socialJobQueue(area: SocialArea, mode: string, label: string, o: { dedupe?: string | null; parent?: string | null } = {}, now = Date.now()): string {
  return add(area, mode, label, 'queued', o, now);
}

/** Bể luồng lấy việc ra chạy. */
export function socialJobRun(key: string, now = Date.now()) {
  const j = jobs.get(key);
  if (j?.state === 'queued') jobs.set(key, { ...j, state: 'running', startedAt: now });
}

/** Huỷ việc còn chờ. Việc đang chạy / đã xong → false. */
export function socialJobCancel(key: string, now = Date.now()): boolean {
  const j = jobs.get(key);
  if (j?.state !== 'queued') return false;
  jobs.set(key, { ...j, state: 'cancelled', finishedAt: now });
  return true;
}

/** Việc chưa xong có cùng khoá chống trùng. */
export const socialJobInFlight = (area: SocialArea, dedupe: string): SocialJob | null =>
  [...jobs.values()].find((j) => j.area === area && j.dedupe === dedupe && j.finishedAt === null) ?? null;

export function socialJobEnd(key: string, r: { resultId?: number | null; error?: string | null }, now = Date.now()) {
  const j = jobs.get(key);
  if (!j) return;
  jobs.set(key, { ...j, state: r.error ? 'error' : 'done', finishedAt: now, resultId: r.resultId ?? null, error: r.error ?? null });
  const done = [...jobs.values()].filter((x) => x.finishedAt !== null).sort((a, b) => b.finishedAt! - a.finishedAt!);
  for (const x of done.slice(DONE_MAX)) jobs.delete(x.key);
}
```

Giữ nguyên `listSocialJobs`, `resetSocialJobs`, `socialJob`, `socialAreaBusy`, `socialJobOf`.

- [ ] **Step 4: Chạy test sổ việc, phải xanh**

Run: `npx vitest run tests/social-jobs.test.ts`
Expected: PASS hết, kể cả test cũ.

- [ ] **Step 5: Viết test hỏng cho bể luồng**

Tạo `web/tests/yt-queue.test.ts`:

```ts
import { beforeEach, describe, expect, it } from 'vitest';
import { listSocialJobs, resetSocialJobs } from '@/lib/social-jobs';
import { createYtQueue, YtCancelled, ytConcurrency, ytDedupe } from '@/lib/yt-queue';

const gate = () => { let open!: () => void; const p = new Promise<void>((r) => { open = r; }); return { p, open }; };
const flush = () => new Promise((r) => setTimeout(r, 0));
const states = () => listSocialJobs().map((j) => j.state).sort();

beforeEach(() => resetSocialJobs());

describe('yt-queue · bể luồng YouTube (mục 23)', () => {
  it('5 việc, giới hạn 3 → 3 chạy + 2 chờ; xong 1 thì việc chờ đầu tiên chạy', async () => {
    const q = createYtQueue(3);
    const gates = Array.from({ length: 5 }, gate);
    const keys = gates.map((g, i) => q.enqueue({ mode: 'niche', label: `k${i}`, dedupe: `niche:k${i}`, run: async () => { await g.p; return { id: i + 1 }; } }));
    await flush();
    expect(states()).toEqual(['queued', 'queued', 'running', 'running', 'running']);
    gates[0].open();
    await expect(q.wait(keys[0])).resolves.toEqual({ id: 1 });
    await flush();
    expect(states()).toEqual(['done', 'queued', 'running', 'running', 'running']);
    gates.forEach((g) => g.open());
    await Promise.all(keys.map((k) => q.wait(k)));
    expect(states()).toEqual(['done', 'done', 'done', 'done', 'done']);
  });
  it('lượt trùng còn đang bay → trả mã việc cũ, không chạy 2 lần', async () => {
    const q = createYtQueue(3);
    const g = gate();
    let calls = 0;
    const run = async () => { calls++; await g.p; return { id: 9 }; };
    const a = q.enqueue({ mode: 'channel', label: '@a', dedupe: 'channel:@a', run });
    const b = q.enqueue({ mode: 'channel', label: '@a', dedupe: 'channel:@a', run });
    expect(b).toBe(a);
    g.open();
    await q.wait(a);
    expect(calls).toBe(1);
  });
  it('huỷ việc chờ → cancelled, wait báo YtCancelled; việc đang chạy không huỷ được', async () => {
    const q = createYtQueue(1);
    const g = gate();
    const a = q.enqueue({ mode: 'niche', label: 'a', dedupe: 'a', run: async () => { await g.p; return { id: 1 }; } });
    const b = q.enqueue({ mode: 'niche', label: 'b', dedupe: 'b', run: async () => ({ id: 2 }) });
    await flush();
    expect(q.cancel(a)).toBe(false);
    expect(q.cancel(b)).toBe(true);
    await expect(q.wait(b)).rejects.toBeInstanceOf(YtCancelled);
    g.open();
    await q.wait(a);
    expect(listSocialJobs().find((j) => j.key === b)?.state).toBe('cancelled');
  });
  it('việc lỗi → state error, wait trả đúng lỗi gốc (để API đổi ra 404 / 400)', async () => {
    class Boom extends Error {}
    const q = createYtQueue(2);
    const k = q.enqueue({ mode: 'channel', label: 'x', dedupe: 'x', run: async () => { throw new Boom('không có kênh'); } });
    await expect(q.wait(k)).rejects.toBeInstanceOf(Boom);
    expect(listSocialJobs()[0]).toMatchObject({ state: 'error', error: 'không có kênh' });
  });
  it('ytConcurrency: 1–8, sai thì về 3', () => {
    expect(ytConcurrency(undefined)).toBe(3);
    expect(ytConcurrency('5')).toBe(5);
    expect(ytConcurrency('0')).toBe(3);
    expect(ytConcurrency('9')).toBe(3);
    expect(ytConcurrency('abc')).toBe(3);
  });
  it('ytDedupe: bỏ force, không phụ thuộc thứ tự khoá', () => {
    expect(ytDedupe('niche', { keyword: 'yoga', country: 'us', force: true })).toBe(ytDedupe('niche', { country: 'us', keyword: 'yoga' }));
    expect(ytDedupe('niche', { keyword: 'yoga', country: 'us' })).not.toBe(ytDedupe('niche', { keyword: 'yoga', country: 'vn' }));
  });
});
```

- [ ] **Step 6: Chạy, phải hỏng**

Run: `npx vitest run tests/yt-queue.test.ts`
Expected: FAIL, `Cannot find module '@/lib/yt-queue'`.

- [ ] **Step 7: Tạo `web/src/lib/yt-queue.ts`**

```ts
// Hàng chờ YouTube (Plan 2 · mục 23, 2026-11-15): mọi lượt YouTube (trang web + AI qua MCP) vào 1 bể luồng chung,
// chạy tối đa `limit` việc cùng lúc, việc dư chờ theo thứ tự bấm. Trạng thái ghi vào sổ social-jobs để Buồng lái + dải chip thấy.
// Bộ giới hạn tốc độ của từng collector (createLimiter ở cấp module) vẫn dùng chung cho mọi luồng.
import { tr } from '@/lib/i18n';
import { socialJob, socialJobCancel, socialJobEnd, socialJobInFlight, socialJobQueue, socialJobRun } from '@/lib/social-jobs';

export type YtRunResult = { id: number; cached?: boolean };
export type YtTask = { mode: string; label: string; dedupe: string; parent?: string | null; run: () => Promise<YtRunResult> };

/** Chưa đo (2026-11-15): số an toàn tự chọn, Task 8 đo 1 · 3 · 5 luồng rồi chốt. */
export const YT_CONCURRENCY_DEFAULT = 3;
/** Tối đa / 1 lần bấm (spec mục 23.2). */
export const YT_BATCH_MAX = { niche: 10, hunt: 5, channel: 10 } as const;
export type YtBatchMode = keyof typeof YT_BATCH_MAX;
export const isYtBatchMode = (v: unknown): v is YtBatchMode => typeof v === 'string' && v in YT_BATCH_MAX;

export function ytConcurrency(env: string | undefined = process.env.YT_CONCURRENCY): number {
  const n = Number(env);
  return Number.isInteger(n) && n >= 1 && n <= 8 ? n : YT_CONCURRENCY_DEFAULT;
}

/** Khoá chống trùng: chế độ + đầu vào, bỏ `force`, khoá xếp theo thứ tự chữ. */
export function ytDedupe(mode: string, req: Record<string, unknown>): string {
  const keys = Object.keys(req).filter((k) => k !== 'force' && req[k] !== undefined).sort();
  return `${mode}:${JSON.stringify(keys.map((k) => [k, req[k]]))}`;
}

export class YtCancelled extends Error {}

/** Giữ promise kết quả thêm 1 phút sau khi xong để request đến muộn vẫn đọc được. */
const KEEP_SETTLED_MS = 60_000;

export function createYtQueue(limit: number) {
  const waiting: { key: string; run: () => Promise<YtRunResult> }[] = [];
  const settled = new Map<string, Promise<YtRunResult>>();
  const resolvers = new Map<string, { ok: (r: YtRunResult) => void; fail: (e: unknown) => void }>();
  let active = 0;
  const forget = (key: string) => { const t = setTimeout(() => settled.delete(key), KEEP_SETTLED_MS); t.unref?.(); };
  const pump = () => {
    while (active < limit && waiting.length) {
      const w = waiting.shift()!;
      if (socialJob(w.key)?.state !== 'queued') continue; // đã huỷ
      active++;
      socialJobRun(w.key);
      const r = resolvers.get(w.key)!;
      Promise.resolve().then(w.run).then(
        (res) => { socialJobEnd(w.key, { resultId: res.id }); r.ok(res); },
        (e) => { socialJobEnd(w.key, { error: (e as Error).message }); r.fail(e); },
      ).finally(() => { active--; resolvers.delete(w.key); forget(w.key); pump(); });
    }
  };
  return {
    /** Đẩy việc vào hàng chờ → mã việc. Lượt trùng còn đang bay → mã việc cũ. */
    enqueue(t: YtTask): string {
      const same = socialJobInFlight('youtube', t.dedupe);
      if (same && settled.has(same.key)) return same.key;
      const key = socialJobQueue('youtube', t.mode, t.label, { dedupe: t.dedupe, parent: t.parent ?? null });
      const p = new Promise<YtRunResult>((ok, fail) => { resolvers.set(key, { ok, fail }); });
      p.catch(() => {}); // không ai chờ thì không thành unhandled rejection
      settled.set(key, p);
      waiting.push({ key, run: t.run });
      pump();
      return key;
    },
    /** Chờ việc xong → kết quả; lỗi → ném đúng lỗi gốc; huỷ → YtCancelled. */
    wait(key: string): Promise<YtRunResult> {
      return settled.get(key) ?? Promise.reject(new Error(tr('Không còn việc {job}', { job: key })));
    },
    /** Huỷ việc còn chờ. */
    cancel(key: string): boolean {
      if (!socialJobCancel(key)) return false;
      resolvers.get(key)?.fail(new YtCancelled(tr('Đã huỷ')));
      resolvers.delete(key);
      forget(key);
      return true;
    },
    stats: () => ({ active, limit }),
  };
}

export type YtQueue = ReturnType<typeof createYtQueue>;
let shared: YtQueue | null = null;
/** Bể luồng dùng chung cho cả máy chủ (social-api + mcp-write-api). */
export const ytQueue = (): YtQueue => (shared ??= createYtQueue(ytConcurrency()));
/** Test: tạo lại bể (đổi giới hạn). */
export function resetYtQueue(limit?: number) { shared = limit ? createYtQueue(limit) : null; }
```

- [ ] **Step 8: Chạy cả 2 file test, phải xanh**

Run: `npx vitest run tests/yt-queue.test.ts tests/social-jobs.test.ts`
Expected: PASS.

- [ ] **Step 9: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/src/lib/social-jobs.ts web/src/lib/yt-queue.ts web/tests/yt-queue.test.ts web/tests/social-jobs.test.ts
git commit -m "feat(web): hàng chờ YouTube chung, chạy tối đa 3 luồng (mục 23)"
```

---

### Task 2: API máy chủ đi qua hàng chờ (search · batch · gather · cancel) + Buồng lái

**Files:**
- Modify: `web/src/server/social-api.ts` (handler `/search` ở khoảng dòng 352–363, thêm route trước `return api;`)
- Modify: `web/src/lib/activity.ts:64-67`
- Create: `web/src/lib/multi-input.ts`
- Test: `web/tests/youtube-batch-api.test.ts`, `web/tests/multi-input.test.ts`

**Interfaces:**
- Consumes: `ytQueue`, `ytDedupe`, `YT_BATCH_MAX`, `isYtBatchMode`, `YtCancelled` (Task 1); `runHuntAll` từ `@/lib/youtube-agent`; `saveTrendMulti`, `saveChannelCompare`, `runSocial` từ `@/lib/social`.
- Produces:
  - `splitItems(text: string, max: number): { items: string[]; over: number }`
  - `looksLikeChannel(s: string): boolean`
  - `POST /api/social/youtube/batch` body `{ mode: 'niche'|'hunt'|'channel'; items: string[]; country?: string; period?: TrendPeriod; force?: boolean; settings?: unknown }` → `{ jobs: { item: string; key: string }[]; errors: { item: string; error: string }[] }`
  - `POST /api/social/youtube/gather` body `{ kind: 'trend'; countries: string[]; period?: TrendPeriod; force?: boolean }` hoặc `{ kind: 'compare'; channels: string[]; country?: string; mine?: number | null; force?: boolean }` → `{ key: string; children: string[] }`
  - `POST /api/social/jobs/:key/cancel` → `{ cancelled: boolean }`
  - `/api/social/search` với `source: 'youtube'`: không còn 409, chờ trong hàng rồi trả `{ id, cached }` như cũ.
  - Activity: việc `queued` → `ActivityJob.status === 'pending'`.

- [ ] **Step 1: Test hỏng cho `multi-input`**

Tạo `web/tests/multi-input.test.ts`:

```ts
import { describe, expect, it } from 'vitest';
import { looksLikeChannel, splitItems } from '@/lib/multi-input';

describe('splitItems (mục 23.2)', () => {
  it('tách theo dòng và dấu phẩy, bỏ trống / quá ngắn / trùng (không phân biệt hoa thường)', () => {
    expect(splitItems('yoga\n habit  tracker ,Yoga\n\nx\nbudget app', 10)).toEqual({ items: ['yoga', 'habit tracker', 'budget app'], over: 0 });
  });
  it('quá giới hạn → cắt, báo số dư', () => {
    expect(splitItems('a1\na2\na3\na4', 2)).toEqual({ items: ['a1', 'a2'], over: 2 });
  });
});

describe('looksLikeChannel', () => {
  it('nhận link kênh, link video, @tên, channel ID', () => {
    for (const s of ['https://www.youtube.com/@abc', 'youtube.com/channel/UC1234567890123456789012', 'https://youtu.be/dQw4w9WgXcQ', '@abc', 'UC1234567890123456789012']) expect(looksLikeChannel(s)).toBe(true);
  });
  it('chữ thường không phải kênh', () => {
    expect(looksLikeChannel('habit tracker')).toBe(false);
  });
});
```

- [ ] **Step 2: Chạy, phải hỏng**

Run: `npx vitest run tests/multi-input.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Tạo `web/src/lib/multi-input.ts`**

```ts
// Ô nhập nhiều dòng (Plan 2 · mục 23.2): dùng chung cho trang (báo trước) và máy chủ (kiểm lại).

/** Mỗi dòng (hoặc phần cách bằng dấu phẩy) là 1 mục; bỏ mục < 2 ký tự và mục trùng; cắt ở `max`. */
export function splitItems(text: string, max: number): { items: string[]; over: number } {
  const seen = new Set<string>();
  const all: string[] = [];
  for (const raw of text.split(/[\n,]+/)) {
    const s = raw.trim().replace(/\s+/g, ' ');
    if (s.length < 2) continue;
    const k = s.toLowerCase();
    if (seen.has(k)) continue;
    seen.add(k);
    all.push(s);
  }
  return { items: all.slice(0, max), over: Math.max(0, all.length - max) };
}

/** Link kênh / link video / @tên / channel ID — cùng các dạng mà Soi kênh nhận. */
export const looksLikeChannel = (s: string) => /youtube\.com\/|youtu\.be\/|^@[\w.-]{2,}$|^UC[\w-]{22}$/i.test(s.trim());
```

- [ ] **Step 4: Chạy, phải xanh**

Run: `npx vitest run tests/multi-input.test.ts`
Expected: PASS.

- [ ] **Step 5: Test hỏng cho API**

Tạo `web/tests/youtube-batch-api.test.ts`. Deps giả của YouTube: theo đúng kiểu `SocialDeps` mà `web/tests/youtube-agent.test.ts` đang dựng (hàm `setup` + `huntClient`). Đọc file đó và chép phần dựng deps YouTube niche (client gợi ý + tìm video) sang đây, đặt tên `ytDeps(gate?: Promise<void>)`: mỗi lần tra keyword đều `await gate` trước khi trả dữ liệu giả.

```ts
import { beforeEach, describe, expect, it } from 'vitest';
import { createDb } from '@/db/client';
import { listActivity } from '@/lib/activity';
import { listSocialJobs, resetSocialJobs } from '@/lib/social-jobs';
import { resetYtQueue } from '@/lib/yt-queue';
import { socialApi } from '@/server/social-api';
import { ytDeps } from './helpers/yt-deps';

const headers = { host: '127.0.0.1:3200', 'content-type': 'application/json' };
const mk = (deps = ytDeps()) => {
  const db = createDb(':memory:');
  const api = socialApi({ db: () => db, deps });
  const post = async (path: string, body: unknown) => { const r = await api.request(path, { method: 'POST', headers, body: JSON.stringify(body) }); return { status: r.status, body: await r.json() }; };
  return { db, post };
};
const gate = () => { let open!: () => void; const p = new Promise<void>((r) => { open = r; }); return { p, open }; };
const flush = () => new Promise((r) => setTimeout(r, 0));

beforeEach(() => { resetSocialJobs(); resetYtQueue(3); });

describe('API hàng chờ YouTube (mục 23)', () => {
  it('batch 5 keyword → 5 mã việc, 3 chạy + 2 chờ, Buồng lái thấy 2 việc pending', async () => {
    const g = gate();
    const { db, post } = mk(ytDeps(g.p));
    const r = await post('/youtube/batch', { mode: 'niche', items: ['yoga', 'cooking', 'budget', 'habit', 'piano'], country: 'us' });
    expect(r.status).toBe(200);
    expect(r.body.jobs).toHaveLength(5);
    expect(r.body.errors).toEqual([]);
    await flush();
    const act = listActivity(db, Date.now(), [], listSocialJobs());
    expect(act.jobs.filter((j) => j.status === 'running')).toHaveLength(3);
    expect(act.jobs.filter((j) => j.status === 'pending')).toHaveLength(2);
    g.open();
  });
  it('batch quá giới hạn → cắt ở 10 keyword; mục quá dài vào errors', async () => {
    const { post } = mk();
    const items = [...Array.from({ length: 12 }, (_, i) => `kw${i}`), 'x'.repeat(81)];
    const r = await post('/youtube/batch', { mode: 'niche', items, country: 'us' });
    expect(r.body.jobs).toHaveLength(10);
  });
  it('batch chế độ lạ / nước lạ → 400', async () => {
    const { post } = mk();
    expect((await post('/youtube/batch', { mode: 'trend', items: ['a1'] })).status).toBe(400);
    expect((await post('/youtube/batch', { mode: 'niche', items: ['a1'], country: 'zz' })).status).toBe(400);
  });
  it('/search YouTube cùng tab chạy song song được (không còn 409)', async () => {
    const g = gate();
    const { post } = mk(ytDeps(g.p));
    const a = post('/search', { source: 'youtube', keyword: 'yoga' });
    const b = post('/search', { source: 'youtube', keyword: 'cooking' });
    await flush();
    g.open();
    const [ra, rb] = await Promise.all([a, b]);
    expect(ra.status).toBe(200);
    expect(rb.status).toBe(200);
    expect(ra.body.id).not.toBe(rb.body.id);
  });
  it('huỷ việc đang chờ', async () => {
    resetYtQueue(1);
    const g = gate();
    const { post } = mk(ytDeps(g.p));
    const r = await post('/youtube/batch', { mode: 'niche', items: ['yoga', 'cooking'], country: 'us' });
    await flush();
    expect((await post(`/jobs/${r.body.jobs[0].key}/cancel`, {})).body).toEqual({ cancelled: false });
    expect((await post(`/jobs/${r.body.jobs[1].key}/cancel`, {})).body).toEqual({ cancelled: true });
    g.open();
  });
  it('gather trend 2 nước → việc cha xong với id lượt gộp', async () => {
    const { post } = mk();
    const r = await post('/youtube/gather', { kind: 'trend', countries: ['us', 'vn'], period: 'week' });
    expect(r.body.children).toHaveLength(2);
    for (let i = 0; i < 50 && listSocialJobs().find((j) => j.key === r.body.key)?.finishedAt == null; i++) await new Promise((x) => setTimeout(x, 10));
    const parent = listSocialJobs().find((j) => j.key === r.body.key);
    expect(parent).toMatchObject({ state: 'done', mode: 'trend' });
    expect(parent?.resultId).toBeGreaterThan(0);
    expect(listSocialJobs().filter((j) => j.parent === r.body.key)).toHaveLength(2);
  });
});
```

Tạo `web/tests/helpers/yt-deps.ts` chứa `export function ytDeps(gate?: Promise<void>): SocialDeps`. Phần này chép từ deps YouTube giả của `youtube-agent.test.ts`. Có thêm deps cho kênh trend (`trend: true`), vì test gather cần chúng: đọc `web/tests/social.test.ts`, tìm deps giả của lượt `trend: true` rồi chép vào. Mỗi hàm giả gọi `await gate` (nếu có) trước khi trả.

- [ ] **Step 6: Chạy, phải hỏng**

Run: `npx vitest run tests/youtube-batch-api.test.ts`
Expected: FAIL. `/youtube/batch` trả 404, và test `/search` song song nhận 409.

- [ ] **Step 7: Sửa `web/src/server/social-api.ts`**

Thêm import ở đầu file:

```ts
import { isYtBatchMode, YT_BATCH_MAX, YtCancelled, ytDedupe, ytQueue, type YtRunResult } from '@/lib/yt-queue';
import { splitItems } from '@/lib/multi-input';
import { runHuntAll } from '@/lib/youtube-agent';
```

Thay khối cuối handler `/search` (từ `// AI qua MCP cũng chạy YouTube` tới `} finally { running.delete(lock); }`) bằng:

```ts
    const { area, mode, label } = socialJobOf(req);
    const mapErr = (e: unknown) => {
      if (e instanceof ChannelNotFound) return c.json({ error: e.message }, 404);
      if (e instanceof HuntInputError) return c.json({ error: e.message }, 400);
      if (e instanceof YtCancelled) return c.json({ error: e.message }, 409);
      throw e;
    };
    // YouTube (mục 23): vào hàng chờ chung, chạy song song cả trong 1 tab; request chờ tới khi xong rồi trả như cũ
    if (area === 'youtube') {
      const q = ytQueue();
      const key = q.enqueue({ mode, label, dedupe: ytDedupe(mode, req as Record<string, unknown>), run: () => runSocial(o.db(), req, o.deps) as Promise<YtRunResult> });
      try { return c.json(await q.wait(key)); } catch (e) { return mapErr(e); }
    }
    // Amazon · Maps: giữ khoá 1 lượt / tab
    const lock = `${area}.${mode}`;
    if (running.has(lock) || socialAreaBusy(area, mode)) return c.json({ error: tr('Tab này đang chạy — đợi lượt trước xong') }, 409);
    running.add(lock);
    try {
      return c.json(await tracked(area, mode, label, () => runSocial(o.db(), req, o.deps)));
    } catch (e) { return mapErr(e); } finally { running.delete(lock); }
  });
```

Thêm 3 route mới ngay trước `return api;`:

```ts
  // ── Hàng chờ YouTube (Plan 2 · mục 23) ──────────────────────────────────────────────────────────────────────────
  // Nhiều keyword / chủ đề / kênh 1 lần: mỗi mục 1 việc trong hàng chờ, trả mã việc ngay (không chờ chạy xong).
  api.post('/youtube/batch', async (c: Context) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const b = await c.req.json().catch(() => null) as Record<string, unknown> | null;
    if (!b || !isYtBatchMode(b.mode)) return c.json({ error: tr('mode phải là niche · hunt · channel') }, 400);
    const mode = b.mode;
    const country = b.country ?? 'us';
    if (!isYtCountry(country)) return c.json({ error: tr('Nước YouTube không hỗ trợ') }, 400);
    const period = b.period ?? 'month';
    if (mode === 'hunt' && !isTrendPeriod(period)) return c.json({ error: tr('Kỳ phải là tuần · tháng · năm') }, 400);
    const raw = Array.isArray(b.items) ? b.items.filter((x): x is string => typeof x === 'string') : [];
    const { items } = splitItems(raw.join('\n'), YT_BATCH_MAX[mode]);
    if (!items.length) return c.json({ error: tr('Gõ ít nhất 1 mục') }, 400);
    const force = b.force === true;
    const maxLen = mode === 'channel' ? 300 : 80;
    // nhiều chủ đề săn → mỗi lượt tự chạy hết 3 bước; 1 chủ đề → chỉ bước 1, người dùng tự bấm bước 2 / 3 như cũ
    const auto = mode === 'hunt' && items.length > 1;
    const q = ytQueue();
    const jobs: { item: string; key: string }[] = [];
    const errors: { item: string; error: string }[] = [];
    for (const item of items) {
      if (item.length > maxLen) { errors.push({ item: item.slice(0, 80), error: tr('Quá dài') }); continue; }
      const req: Parameters<typeof runSocial>[1] = mode === 'niche' ? { source: 'youtube', keyword: item, country, force }
        : mode === 'channel' ? { source: 'youtube', channel: item, country, force }
        : { source: 'youtube', hunt: item, country, period: period as TrendPeriod, force, settings: huntSettings(b.settings) };
      const run = auto ? () => runHuntAll(o.db(), { topic: item, country, period: period as TrendPeriod }, o.deps) : () => runSocial(o.db(), req, o.deps) as Promise<YtRunResult>;
      const dedupe = ytDedupe(mode, { ...(req as Record<string, unknown>), auto });
      jobs.push({ item, key: q.enqueue({ mode, label: item, dedupe, run }) });
    }
    return c.json({ jobs, errors });
  });
  // Việc gộp: Đang trend nhiều nước · So kênh. Máy chủ đẩy từng nước / kênh vào hàng chờ rồi tự gộp khi xong hết,
  // nên rời trang vẫn gộp được (trước 2026-11-15 trình duyệt tự lặp).
  api.post('/youtube/gather', async (c: Context) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const b = await c.req.json().catch(() => null) as Record<string, unknown> | null;
    const force = b?.force === true;
    const q = ytQueue();
    if (b?.kind === 'trend') {
      const countries = Array.isArray(b.countries) ? [...new Set(b.countries.filter(isYtCountry))] : [];
      if (!countries.length || countries.length > Object.keys(YT_COUNTRIES).length) return c.json({ error: tr('Chọn ít nhất 1 nước') }, 400);
      const period = b.period ?? 'week';
      if (!isTrendPeriod(period)) return c.json({ error: tr('Kỳ phải là tuần · tháng · năm') }, 400);
      const parent = socialJobStart('youtube', 'trend', `${countries.map((x) => x.toUpperCase()).join(', ')} · ${period}`);
      const children = countries.map((country) => {
        const req = { source: 'youtube' as const, trend: true as const, country, period, force };
        return q.enqueue({ mode: 'trend', label: `${country.toUpperCase()} · ${period}`, parent, dedupe: ytDedupe('trend', req), run: () => runSocial(o.db(), req, o.deps) as Promise<YtRunResult> });
      });
      void gatherThen(parent, children, countries.map((x) => x.toUpperCase()), (ids, errors) => saveTrendMulti(o.db(), ids, errors));
      return c.json({ key: parent, children });
    }
    if (b?.kind === 'compare') {
      const channels = Array.isArray(b.channels) ? b.channels.filter((x): x is string => typeof x === 'string').map((x) => x.trim()).filter((x) => x.length >= 2 && x.length <= 300) : [];
      if (channels.length < COMPARE_MIN || channels.length > COMPARE_MAX) return c.json({ error: tr('So {min}–{max} kênh', { min: COMPARE_MIN, max: COMPARE_MAX }) }, 400);
      const country = b.country ?? 'us';
      if (!isYtCountry(country)) return c.json({ error: tr('Nước YouTube không hỗ trợ') }, 400);
      const mineAt = Number.isInteger(b.mine) && (b.mine as number) >= 0 && (b.mine as number) < channels.length ? b.mine as number : null;
      const parent = socialJobStart('youtube', 'compare', channels.join(' · '));
      const children = channels.map((channel) => {
        const req = { source: 'youtube' as const, channel, country, force, compare: true };
        return q.enqueue({ mode: 'compare', label: channel, parent, dedupe: ytDedupe('compare', req), run: () => runSocial(o.db(), req, o.deps) as Promise<YtRunResult> });
      });
      void gatherThen(parent, children, channels, (ids, errors, byChild) => {
        const myId = mineAt === null ? null : byChild[mineAt];
        const uniq = [...new Set(ids)];
        if (uniq.length < COMPARE_MIN) throw Error(tr('Cần ít nhất 2 kênh soi được để so'));
        return saveChannelCompare(o.db(), uniq, myId == null ? null : uniq.indexOf(myId), errors, { trends: o.deps?.trends });
      });
      return c.json({ key: parent, children });
    }
    return c.json({ error: tr('kind phải là trend · compare') }, 400);
  });
  /** Chờ mọi việc con xong → gọi `save` với id lượt thành công + lỗi từng mục → ghi id lượt gộp vào việc cha. */
  async function gatherThen(parent: string, children: string[], names: string[], save: (ids: number[], errors: string[], byChild: (number | null)[]) => number | Promise<number>) {
    const res = await Promise.allSettled(children.map((k) => ytQueue().wait(k)));
    const byChild = res.map((r) => (r.status === 'fulfilled' ? r.value.id : null));
    const ids = byChild.filter((x): x is number => x !== null);
    const errors = res.flatMap((r, i) => (r.status === 'rejected' ? [`${names[i]}: ${(r.reason as Error).message}`] : []));
    try {
      if (!ids.length) throw Error(tr('Không mục nào tra được'));
      socialJobEnd(parent, { resultId: await save(ids, errors, byChild) });
    } catch (e) { socialJobEnd(parent, { error: (e as Error).message }); }
  }
  api.post('/jobs/:key/cancel', (c: Context) => {
    const blocked = guardJsonPost(c.req.raw);
    if (blocked) return blocked;
    const key = c.req.param('key');
    if (!/^social:\d+$/.test(key)) return c.json({ error: tr('Mã việc không đúng') }, 400);
    return c.json({ cancelled: ytQueue().cancel(key) });
  });
```

Kiểm 2 điều khi gõ code:
- `req` của trend / compare phải đúng kiểu `Parameters<typeof runSocial>[1]`. Nếu TypeScript không nhận object literal ở trên thì khai báo `const req: Parameters<typeof runSocial>[1] = { … }`.
- `socialJobStart` / `socialJobEnd` đã được import sẵn ở đầu file.

- [ ] **Step 8: Sửa `web/src/lib/activity.ts:64-67`**

```ts
  const active = [...activeJobs(db, chats), ...social.filter((j) => j.finishedAt === null).map((j): ActivityJob => ({
    key: j.key, kind: 'social', status: j.state === 'queued' ? 'pending' : 'running', label: j.label, source: null, runId: null, exploreId: null, tool: null,
    startedAt: new Date(j.startedAt).toISOString(), href: `/${j.area}`, hunts: [], area: j.area, mode: j.mode,
  }))];
```

- [ ] **Step 9: Chạy test API + test cũ của social, phải xanh**

Run: `npx vitest run tests/youtube-batch-api.test.ts tests/multi-input.test.ts tests/social-jobs.test.ts tests/social.test.ts`
Expected: PASS. Test `khoá theo tab … 409` trong `social-jobs.test.ts` dùng Maps nên vẫn xanh.

- [ ] **Step 10: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/src/lib/multi-input.ts web/src/lib/activity.ts web/tests/multi-input.test.ts web/tests/youtube-batch-api.test.ts web/tests/helpers/yt-deps.ts
git add -p web/src/server/social-api.ts
git commit -m "feat(web): API batch / gather / huỷ cho hàng chờ YouTube, bỏ 409 ở YouTube (mục 23)"
```

---

### Task 3: AI qua MCP dùng chung hàng chờ

**Files:**
- Modify: `web/src/server/mcp-write-api.ts:285-322`
- Test: `web/tests/youtube-agent.test.ts:126-143`

**Interfaces:**
- Consumes: `ytQueue`, `ytDedupe` (Task 1).
- Produces: `youtube_job` có thêm `status: 'queued'` kèm `next`.

- [ ] **Step 1: Sửa test cho luật mới (test sẽ hỏng)**

Trong `web/tests/youtube-agent.test.ts`, thêm `import { resetYtQueue } from '../src/lib/yt-queue';`, rồi thay test `'chạy lâu → trả job; trong lúc chạy YouTube bị khoá; …'` bằng:

```ts
  it('chạy lâu → trả job; lượt dư xếp hàng (không 429); youtube_job hỏi lại tới khi xong', async () => {
    resetYtQueue(1);
    let open!: () => void;
    const gate = new Promise<void>((r) => { open = r; });
    const { post } = setup({ social: { hunt: huntClient(gate) }, wait: 20 });
    const r = await post('/youtube/hunt', { topic: 'kinh tế', country: 'vn' });
    expect(r.body).toMatchObject({ status: 'running' });
    expect(r.body.job).toMatch(/^social:\d+$/);
    const second = await post('/youtube/hunt', { topic: 'nấu ăn', country: 'vn' });
    expect(second.status).toBe(200);
    expect(second.body).toMatchObject({ status: 'queued' });
    expect((await post('/youtube/job', { job: r.body.job })).body.status).toBe('running');
    open();
    await new Promise((x) => setTimeout(x, 80));
    expect((await post('/youtube/job', { job: r.body.job })).body.status).toBe('done');
    resetYtQueue();
  });
```

Thêm `resetYtQueue();` vào `beforeEach` của file (cạnh `resetSocialJobs()`). Nếu import `socialAreaBusy` không còn dùng nữa thì xoá khỏi import.

- [ ] **Step 2: Chạy, phải hỏng**

Run: `npx vitest run tests/youtube-agent.test.ts`
Expected: FAIL, lượt săn thứ 2 vẫn trả 429.

- [ ] **Step 3: Sửa `web/src/server/mcp-write-api.ts`**

Import: bỏ `socialAreaBusy, socialJobEnd, socialJobStart` khỏi import `social-jobs` (giữ `socialJob`), thêm `import { ytDedupe, ytQueue, type YtRunResult } from '@/lib/yt-queue';`.

Trong `ytResult`, thay nhánh `if (j.finishedAt === null) { … }` bằng:

```ts
    if (j.state === 'queued') {
      return { job: key, status: 'queued', next: tr('Đang chờ tới lượt trong hàng chờ YouTube — gọi youtube_job { job: "{job}" } sau ~30 giây', { job: key }) };
    }
    if (j.finishedAt === null) {
      return { job: key, status: 'running', seconds: Math.round((now() - j.startedAt) / 1000), next: tr('Đang tra YouTube (~1–2 phút) — gọi youtube_job { job: "{job}" } sau ~30 giây', { job: key }) };
    }
    if (j.state === 'cancelled') return { job: key, status: 'error', error: tr('Đã huỷ') };
```

Thay `ytStart`:

```ts
  // mục 23: chung hàng chờ với trang web — lượt dư xếp hàng thay vì báo 429
  const ytStart = async (mode: string, label: string, top: number, dedupe: Record<string, unknown>, fn: () => Promise<{ id: number }>) => {
    const q = ytQueue();
    const key = q.enqueue({ mode, label, dedupe: ytDedupe(mode, dedupe), run: fn as () => Promise<YtRunResult> });
    await Promise.race([q.wait(key).catch(() => undefined), new Promise((r) => setTimeout(r, ytWait))]);
    return ytResult(key, top);
  };
```

Sửa 3 chỗ gọi:

```ts
    return ytStart('niche', keyword, topOf(b.top, 10), { keyword, country }, () => runSocial(o.db(), { source: 'youtube', keyword, country }, o.social));
```
```ts
    return ytStart('hunt', topic, topOf(b.top, 3), { topic, country, period, auto: true }, () => runHuntAll(o.db(), { topic, country, period }, o.social));
```
```ts
    return ytStart('channel', channel, topOf(b.top, 10), { channel, country }, () => runSocial(o.db(), { source: 'youtube', channel, country }, o.social));
```

Sửa câu chú thích phía trên khối (dòng "trang YouTube bị khoá như khi tự bấm") thành "chung hàng chờ với trang YouTube (mục 23)".

- [ ] **Step 4: Chạy, phải xanh**

Run: `npx vitest run tests/youtube-agent.test.ts tests/youtube-mcp.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit (chỉ khi anh Tu cho phép)**

```bash
git add -p web/src/server/mcp-write-api.ts web/tests/youtube-agent.test.ts
git commit -m "feat(web): MCP YouTube dùng chung hàng chờ, lượt dư báo queued thay vì 429 (mục 23)"
```

---

### Task 4: Gom 3 nhóm + chip chế độ trên trang

**Files:**
- Create: `web/src/lib/youtube-groups.ts`
- Modify: `web/src/client/YoutubeEntry.tsx`
- Modify: `web/src/client/SocialPage.tsx:157-171` (đếm việc, truyền `counts`)
- Create: `web/src/locales/en-text-yt-queue.ts`; Modify: `web/src/locales/en-text.ts`
- Test: `web/tests/youtube-groups.test.ts`

**Interfaces:**
- Consumes: `SocialJob` (Task 1).
- Produces:
  - `type YoutubeMode = 'niche' | 'hunt' | 'trend' | 'channel' | 'compare'` (dời từ `YoutubeEntry.tsx` sang lib, `YoutubeEntry.tsx` re-export)
  - `type YoutubeGroup = 'find' | 'hunt' | 'inspect'`
  - `YT_GROUPS: { group: YoutubeGroup; modes: YoutubeMode[] }[]`
  - `groupOf(m: YoutubeMode): YoutubeGroup`
  - `modeCounts(jobs: SocialJob[]): Partial<Record<YoutubeMode, { running: number; queued: number }>>` (chỉ việc YouTube, không tính việc con)
  - `YoutubeEntry` props: `{ value: YoutubeMode; onChange: (m: YoutubeMode) => void; running?: Partial<Record<YoutubeMode, number>>; counts?: Partial<Record<YoutubeMode, { running: number; queued: number }>> }`

- [ ] **Step 1: Test hỏng**

Tạo `web/tests/youtube-groups.test.ts`:

```ts
// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { createElement as h } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { groupOf, modeCounts, YT_GROUPS } from '@/lib/youtube-groups';
import { YoutubeEntry } from '@/client/YoutubeEntry';
import type { SocialJob } from '@/lib/social-jobs';

const job = (p: Partial<SocialJob>): SocialJob => ({ key: 'social:1', area: 'youtube', mode: 'niche', label: 'x', state: 'running', startedAt: 0, finishedAt: null, resultId: null, error: null, dedupe: null, parent: null, ...p });

describe('youtube-groups (mục 23.1)', () => {
  it('5 chế độ nằm trong đúng 3 nhóm, mỗi chế độ 1 nhóm', () => {
    expect(YT_GROUPS.map((g) => g.group)).toEqual(['find', 'hunt', 'inspect']);
    expect(YT_GROUPS.flatMap((g) => g.modes).sort()).toEqual(['channel', 'compare', 'hunt', 'niche', 'trend']);
    expect(groupOf('trend')).toBe('find');
    expect(groupOf('compare')).toBe('inspect');
  });
  it('modeCounts: đếm chạy / chờ theo chế độ, bỏ việc xong, việc con, việc nguồn khác', () => {
    const c = modeCounts([
      job({ key: 'a', mode: 'niche' }), job({ key: 'b', mode: 'niche', state: 'queued' }), job({ key: 'c', mode: 'niche', state: 'done', finishedAt: 1 }),
      job({ key: 'd', mode: 'trend', parent: 'p' }), job({ key: 'e', area: 'amazon', mode: 'hunt' }),
    ]);
    expect(c).toEqual({ niche: { running: 1, queued: 1 } });
  });
  it('render: 3 thẻ nhóm + chip chế độ của nhóm đang chọn, nhóm có việc ghi số đang chạy', () => {
    const html = renderToStaticMarkup(h(YoutubeEntry, { value: 'channel', onChange: () => {}, counts: { niche: { running: 2, queued: 1 } } }));
    expect(html.match(/data-yt-group=/g)).toHaveLength(3);
    expect(html).toContain('Soi từng kênh');
    expect(html).toContain('So kênh');
    expect(html).not.toContain('data-yt-mode="niche"');
    expect(html).toContain('2 đang chạy');
  });
});
```

- [ ] **Step 2: Chạy, phải hỏng**

Run: `npx vitest run tests/youtube-groups.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Tạo `web/src/lib/youtube-groups.ts`**

```ts
// Trang YouTube gom 3 nhóm theo việc (Plan 2 · mục 23.1). Khoá chế độ giữ nguyên; nhóm suy ra từ chế độ.
import type { SocialJob } from '@/lib/social-jobs';

export type YoutubeMode = 'niche' | 'hunt' | 'trend' | 'channel' | 'compare';
export type YoutubeGroup = 'find' | 'hunt' | 'inspect';

/** Mục 15 (Theo dõi ngách) và mục 21 (Keyword đang tìm) sau này chỉ thêm chế độ vào đây. */
export const YT_GROUPS: { group: YoutubeGroup; modes: YoutubeMode[] }[] = [
  { group: 'find', modes: ['niche', 'trend'] },
  { group: 'hunt', modes: ['hunt'] },
  { group: 'inspect', modes: ['channel', 'compare'] },
];

export const groupOf = (m: YoutubeMode): YoutubeGroup => YT_GROUPS.find((g) => g.modes.includes(m))?.group ?? 'find';

export type ModeCount = { running: number; queued: number };
/** Việc YouTube chưa xong theo chế độ (bỏ việc con của việc gộp: thẻ chỉ đếm 1 lượt gộp). */
export function modeCounts(jobs: readonly SocialJob[]): Partial<Record<YoutubeMode, ModeCount>> {
  const out: Partial<Record<YoutubeMode, ModeCount>> = {};
  for (const j of jobs) {
    if (j.area !== 'youtube' || j.finishedAt !== null || j.parent !== null) continue;
    const c = (out[j.mode as YoutubeMode] ??= { running: 0, queued: 0 });
    if (j.state === 'queued') c.queued++; else c.running++;
  }
  return out;
}
```

- [ ] **Step 4: Sửa `web/src/client/YoutubeEntry.tsx`**

4a. Đầu file: thay `export type YoutubeMode = …;` bằng

```ts
import { groupOf, YT_GROUPS, type ModeCount, type YoutubeGroup, type YoutubeMode } from '@/lib/youtube-groups';
export type { YoutubeMode } from '@/lib/youtube-groups';
```

4b. Trong `ENTRIES`, đổi thẻ `channel`:

```ts
  { mode: 'channel', title: tx('Soi từng kênh'), what: tx('Dán 1 hoặc nhiều link kênh (mỗi dòng 1 kênh): dùng keyword gì, đứng thứ mấy khi tìm, kênh cày nhóm nội dung nào, từng video nên học hay tránh.'), icon: 'channel' },
```

4c. Thêm bảng nhóm ngay sau `ENTRIES`:

```ts
const GROUP_META: Record<YoutubeGroup, { title: string; icon: Icon }> = {
  find: { title: tx('Tìm ngách'), icon: 'idea' },
  hunt: { title: tx('Săn kênh'), icon: 'hunt' },
  inspect: { title: tx('Soi kênh'), icon: 'channel' },
};
```

4d. Tách thanh dính ra hàm riêng, để cả `EntryCards` (KDP) lẫn nhóm YouTube dùng chung. Cắt nguyên khối `{cur && <div className="mode-sticky !mt-0" …>…</div>}` trong `EntryCards` vào component mới, chỉ đổi phần trước tên chế độ: thêm nấc nhóm `crumb` khi có.

```tsx
function ModeSticky({ stuck, onJump, page, crumb, icon, title, subject, since, now }: {
  stuck: boolean; onJump: () => void; page: { icon: PageIconName; name: string }; crumb?: string; icon: Icon; title: string;
  subject: StickySubject | null; since: number | undefined; now: number;
}) {
  return (
    <div className="mode-sticky !mt-0" aria-hidden={!stuck}>
      <button type="button" tabIndex={stuck ? 0 : -1} onClick={onJump} title={tr('Đổi chế độ')} data-on={stuck || undefined}
        className="mode-sticky-bar relative flex max-w-full items-center gap-2.5 overflow-hidden rounded-full border border-zinc-200 bg-surface py-1.5 pl-2 pr-4 text-left shadow-md">
        <span className="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-zinc-100"><PageGlyph name={page.icon} className="h-5 w-5" /></span>
        <span className="shrink-0 text-xs font-medium text-zinc-500">{page.name}</span>
        {crumb && <><span aria-hidden className="text-zinc-300">/</span><span className="shrink-0 text-xs font-medium text-zinc-500">{tr(crumb)}</span></>}
        <span aria-hidden className="text-zinc-300">/</span>
        <svg aria-hidden viewBox="0 0 24 24" className="h-4 w-4 shrink-0 text-[var(--accent)]" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">{ICON[icon]}</svg>
        <span className={`truncate text-sm font-semibold text-[var(--accent)] ${subject ? 'shrink-0' : 'min-w-0'}`}>{tr(title)}</span>
        {subject && <>
          <span aria-hidden className="text-zinc-300">/</span>
          {subject.image && <img src={subject.image} alt="" referrerPolicy="no-referrer" className="h-7 w-7 shrink-0 rounded-full object-cover" />}
          <span className="min-w-0 max-w-64 truncate text-sm font-semibold text-zinc-900">{subject.name}</span>
        </>}
        {since !== undefined && <span className="flex shrink-0 items-center gap-1 text-xs font-medium text-[var(--accent)]">
          <span className="progress-spinner !h-3 !w-3" aria-hidden />{mmss(now - since)}</span>}
        <svg aria-hidden viewBox="0 0 24 24" className="h-3.5 w-3.5 shrink-0 text-zinc-400" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m18 15-6-6-6 6" /></svg>
        {since !== undefined && <span className="tab-running-bar !h-[3px]" aria-hidden><span /></span>}
      </button>
    </div>
  );
}
```

Trong `EntryCards`, chỗ cũ thay bằng:

```tsx
    {cur && <ModeSticky stuck={stuck} onJump={() => grid.current?.scrollIntoView({ behavior: 'smooth', block: 'center' })} page={page}
      icon={cur.icon} title={cur.title} subject={subject} since={curSince} now={now} />}
```

4e. Viết lại `YoutubeEntry`, không dùng `EntryCards` nữa:

```tsx
/** 2026-11-15 (mục 23.1): 3 thẻ nhóm theo việc + hàng chip chế độ của nhóm đang chọn. Bấm thẻ nhóm → về chế độ dùng gần nhất của nhóm đó. */
export function YoutubeEntry({ value, onChange, running = {}, counts = {} }: {
  value: YoutubeMode; onChange: (m: YoutubeMode) => void; running?: Partial<Record<YoutubeMode, number>>; counts?: Partial<Record<YoutubeMode, ModeCount>>;
}) {
  const group = groupOf(value);
  const last = useRef<Partial<Record<YoutubeGroup, YoutubeMode>>>({});
  last.current[group] = value;
  const cur = ENTRIES.find((e) => e.mode === value)!;
  const now = useNow(Object.keys(running).length > 0);
  const grid = useRef<HTMLDivElement>(null);
  const stuck = useScrolledPast(grid);
  const subject = useStickySubject(value);
  const sum = (modes: YoutubeMode[]) => modes.reduce((n, m) => n + (counts[m]?.running ?? 0) + (counts[m]?.queued ?? 0), 0);
  const groupSince = (modes: YoutubeMode[]) => modes.map((m) => running[m]).filter((x): x is number => x !== undefined).sort((a, b) => a - b)[0];
  const modes = YT_GROUPS.find((g) => g.group === group)!.modes;
  return (<>
    <div className="@container space-y-3">
      <div ref={grid} role="radiogroup" aria-label={tr('Bạn muốn làm gì trên YouTube')} className="grid grid-cols-[repeat(3,minmax(0,1fr))] gap-3">
        {YT_GROUPS.map((g) => {
          const on = g.group === group;
          const meta = GROUP_META[g.group];
          const n = sum(g.modes);
          const since = groupSince(g.modes);
          return (
            <button key={g.group} type="button" role="radio" aria-checked={on} data-yt-group={g.group}
              onClick={() => onChange(last.current[g.group] ?? g.modes[0])}
              className={`relative flex min-w-0 items-center gap-3 overflow-hidden rounded-2xl border-2 px-4 py-3.5 text-left transition-colors ${on ? 'border-[var(--accent)] bg-[var(--accent-soft)]' : 'border-zinc-200 bg-surface hover:border-zinc-400'}`}>
              <span aria-hidden className={`grid h-12 w-12 shrink-0 place-items-center rounded-2xl ${on ? 'bg-[var(--accent-solid)] text-white' : 'bg-zinc-100 text-zinc-700'}`}>
                <svg viewBox="0 0 24 24" className="h-7 w-7" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">{ICON[meta.icon]}</svg>
              </span>
              <span className="min-w-0 flex-1">
                <span className={`block truncate text-base font-semibold leading-snug ${on ? 'text-[var(--accent)]' : 'text-zinc-900'}`}>{tr(meta.title)}</span>
                {n > 0 && <span className="mt-0.5 flex items-center gap-1.5 text-xs font-medium text-[var(--accent)]">
                  <span className="progress-spinner !h-3 !w-3" aria-hidden />{tr('{n} đang chạy', { n })}</span>}
              </span>
              {since !== undefined && <span className="tab-running-bar" aria-hidden><span /></span>}
            </button>
          );
        })}
      </div>
      <div role="radiogroup" aria-label={tr('Chế độ')} className="flex flex-wrap items-center gap-2">
        {modes.map((m) => {
          const e = ENTRIES.find((x) => x.mode === m)!;
          const on = m === value;
          const n = (counts[m]?.running ?? 0) + (counts[m]?.queued ?? 0);
          return (
            <button key={m} type="button" role="radio" aria-checked={on} data-yt-mode={m} title={tr(e.what)} onClick={() => onChange(m)}
              className={`inline-flex shrink-0 items-center gap-1.5 rounded-full border px-3 py-1.5 text-sm font-medium ${on ? 'border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--accent)]' : 'border-zinc-200 bg-surface text-zinc-700 hover:border-zinc-400'}`}>
              <svg aria-hidden viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">{ICON[e.icon]}</svg>
              {tr(e.title)}
              {n > 0 && <span className="rounded-full bg-[var(--accent-solid)] px-1.5 text-xs text-white">{n}</span>}
            </button>
          );
        })}
      </div>
      <p role="status" className="flex min-w-0 items-start gap-2 px-1 text-sm text-zinc-600">
        <span aria-hidden className="mt-1.5 h-2 w-2 shrink-0 rounded-full bg-[var(--accent)]" /><span className="min-w-0">{tr(cur.what)}</span>
      </p>
    </div>
    <ModeSticky stuck={stuck} onJump={() => grid.current?.scrollIntoView({ behavior: 'smooth', block: 'center' })} page={{ icon: 'youtube', name: 'YouTube' }}
      crumb={GROUP_META[group].title} icon={cur.icon} title={cur.title} subject={subject} since={running[value]} now={now} />
  </>);
}
```

- [ ] **Step 5: Sửa `web/src/client/SocialPage.tsx` (SourcePanel)**

Thêm import `import { modeCounts } from '@/lib/youtube-groups';`. Thay dòng `for (const j of activity?.social ?? []) …` bằng:

```ts
  // chỉ việc đang chạy thật (việc còn chờ không có vạch chạy); việc con của lượt gộp không tính riêng
  for (const j of activity?.social ?? []) if (j.area === api && j.state === 'running' && j.parent === null && modes.includes(j.mode)) running[j.mode] ??= j.startedAt;
  const counts = page === 'youtube' ? modeCounts(activity?.social ?? []) : {};
```

và dòng render:

```tsx
      {page === 'youtube' && <YoutubeEntry value={mode as YoutubeMode} onChange={switchMode} running={running} counts={counts} />}
```

- [ ] **Step 6: Bản tiếng Anh**

Tạo `web/src/locales/en-text-yt-queue.ts`:

```ts
/**
 * Bản tiếng Anh cho trang YouTube gom 3 nhóm + hàng chờ (Plan 2 · mục 23, 2026-11-15).
 * Gộp vào `enText` (en-text.ts). Khoá = đúng chữ tiếng Việt trong code.
 */
export const ytQueueEnText: Record<string, string> = {
  'Tìm ngách': 'Find a niche',
  'Săn kênh': 'Hunt channels',
  'Soi kênh': 'Inspect channels',
  'Soi từng kênh': 'Inspect each channel',
  'Dán 1 hoặc nhiều link kênh (mỗi dòng 1 kênh): dùng keyword gì, đứng thứ mấy khi tìm, kênh cày nhóm nội dung nào, từng video nên học hay tránh.': 'Paste one or more channel links (one per line): which keywords they use, where they rank in search, which content groups they grind, which videos to learn from or avoid.',
  '{n} đang chạy': '{n} running',
  'Chế độ': 'Mode',
  'Đã huỷ': 'Cancelled',
  'Không còn việc {job}': 'Job {job} is gone',
  'mode phải là niche · hunt · channel': 'mode must be niche · hunt · channel',
  'Gõ ít nhất 1 mục': 'Type at least 1 item',
  'Quá dài': 'Too long',
  'Chọn ít nhất 1 nước': 'Pick at least 1 country',
  'Không mục nào tra được': 'No item could be looked up',
  'kind phải là trend · compare': 'kind must be trend · compare',
  'Mã việc không đúng': 'Invalid job code',
  'Đang chờ tới lượt trong hàng chờ YouTube — gọi youtube_job { job: "{job}" } sau ~30 giây': 'Waiting in the YouTube queue — call youtube_job { job: "{job}" } in ~30 seconds',
};
```

Mở `web/src/locales/en-text.ts`, thêm `ytQueueEnText` đúng như cách `channelCompareEnText` đang được import và spread vào `enText`. Task 5 và 6 sẽ thêm chữ mới vào cùng file này.

- [ ] **Step 7: Chạy test nhóm + i18n, phải xanh**

Run: `npx vitest run tests/youtube-groups.test.ts tests/i18n-text.test.ts tests/i18n.test.ts`
Expected: PASS. Nếu `i18n-text.test.ts` báo thiếu bản dịch thì thêm đúng chữ nó in ra vào `en-text-yt-queue.ts`.

- [ ] **Step 8: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/src/lib/youtube-groups.ts web/src/locales/en-text-yt-queue.ts web/tests/youtube-groups.test.ts
git add -p web/src/client/YoutubeEntry.tsx web/src/client/SocialPage.tsx web/src/locales/en-text.ts
git commit -m "feat(web): trang YouTube gom 3 nhóm + chip chế độ (mục 23.1)"
```

---

### Task 5: Dải chip hàng chờ

**Files:**
- Create: `web/src/lib/queue-chips.ts`
- Create: `web/src/client/QueueStrip.tsx`
- Modify: `web/src/locales/en-text-yt-queue.ts`
- Test: `web/tests/queue-chips.test.ts`, `web/tests/queue-strip.test.ts`

**Interfaces:**
- Consumes: `SocialJob`, `SocialJobState` (Task 1).
- Produces:
  - `type QueueChip = { key: string; label: string; state: SocialJobState; resultId: number | null; error: string | null; startedAt: number; position: number | null; children: { done: number; total: number } | null }`
  - `queueChips(jobs: readonly SocialJob[], mode: string, dismissed: ReadonlySet<string>, cap?: number): { chips: QueueChip[]; other: number }`
  - `gatherProgress(jobs: readonly SocialJob[], parent: string): { done: number; total: number; current: string | null; failed: string[] } | null` (cùng dạng với `MultiProgress` / `CompareProgress`)
  - `QueueStrip` props `{ chips: QueueChip[]; other: number; openId: number | null; onOpen: (resultId: number) => void; onCancel: (key: string) => void; onDismiss: (key: string) => void }`

- [ ] **Step 1: Test hỏng cho hàm thuần**

Tạo `web/tests/queue-chips.test.ts`:

```ts
import { describe, expect, it } from 'vitest';
import { gatherProgress, queueChips } from '@/lib/queue-chips';
import type { SocialJob } from '@/lib/social-jobs';

let n = 0;
const job = (p: Partial<SocialJob>): SocialJob => ({ key: `social:${++n}`, area: 'youtube', mode: 'niche', label: 'x', state: 'running', startedAt: 0, finishedAt: null, resultId: null, error: null, dedupe: null, parent: null, ...p });

describe('queueChips (mục 23.3)', () => {
  it('việc chưa xong trước (theo lúc vào), rồi việc xong mới nhất; số thứ tự chờ tính trên cả YouTube', () => {
    const other = job({ mode: 'channel', state: 'queued', startedAt: 1 });
    const a = job({ state: 'done', finishedAt: 50, resultId: 3, startedAt: 2 });
    const b = job({ state: 'queued', startedAt: 5 });
    const c = job({ state: 'running', startedAt: 4 });
    const r = queueChips([a, b, c, other], 'niche', new Set());
    expect(r.chips.map((x) => x.key)).toEqual([c.key, b.key, a.key]);
    expect(r.chips[1].position).toBe(2);
    expect(r.other).toBe(1);
  });
  it('bỏ việc đã đóng, việc huỷ, việc con; giữ tối đa `cap` chip đã xong', () => {
    const done = Array.from({ length: 10 }, (_, i) => job({ state: 'done', finishedAt: i, resultId: i + 1 }));
    const gone = job({ state: 'done', finishedAt: 99 });
    const cancelled = job({ state: 'cancelled', finishedAt: 98 });
    const child = job({ parent: 'social:500' });
    const r = queueChips([...done, gone, cancelled, child], 'niche', new Set([gone.key]), 8);
    expect(r.chips).toHaveLength(8);
    expect(r.chips[0].resultId).toBe(10);
  });
  it('việc gộp có đếm việc con', () => {
    const p = job({ mode: 'trend', key: 'social:900' });
    const kids = [job({ mode: 'trend', parent: 'social:900', state: 'done', finishedAt: 1, label: 'US · week' }), job({ mode: 'trend', parent: 'social:900', label: 'VN · week' }), job({ mode: 'trend', parent: 'social:900', state: 'error', finishedAt: 2, label: 'JP · week' })];
    expect(queueChips([p, ...kids], 'trend', new Set()).chips[0].children).toEqual({ done: 2, total: 3 });
    expect(gatherProgress([p, ...kids], 'social:900')).toEqual({ done: 2, total: 3, current: 'VN · week', failed: ['JP · week'] });
    expect(gatherProgress([], 'social:1')).toBeNull();
  });
});
```

- [ ] **Step 2: Chạy, phải hỏng**

Run: `npx vitest run tests/queue-chips.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Tạo `web/src/lib/queue-chips.ts`**

```ts
// Dải chip hàng chờ trang YouTube (Plan 2 · mục 23.3): biến sổ việc thành chip của 1 chế độ.
import type { SocialJob, SocialJobState } from '@/lib/social-jobs';

export type QueueChip = {
  key: string; label: string; state: SocialJobState; resultId: number | null; error: string | null; startedAt: number;
  /** thứ tự trong hàng chờ YouTube (1 = tới lượt kế), chỉ có khi đang chờ */
  position: number | null;
  /** việc gộp: số việc con đã xong / tổng */
  children: { done: number; total: number } | null;
};

/** Mặc định giữ 8 chip đã xong; việc chưa xong luôn hiện. */
export const QUEUE_DONE_CAP = 8;

export function queueChips(jobs: readonly SocialJob[], mode: string, dismissed: ReadonlySet<string>, cap = QUEUE_DONE_CAP): { chips: QueueChip[]; other: number } {
  const yt = jobs.filter((j) => j.area === 'youtube');
  const queued = yt.filter((j) => j.state === 'queued').sort((a, b) => a.startedAt - b.startedAt);
  const top = yt.filter((j) => j.parent === null && j.state !== 'cancelled' && !dismissed.has(j.key));
  const mine = top.filter((j) => j.mode === mode);
  const toChip = (j: SocialJob): QueueChip => {
    const kids = yt.filter((k) => k.parent === j.key);
    return {
      key: j.key, label: j.label, state: j.state, resultId: j.resultId, error: j.error, startedAt: j.startedAt,
      position: j.state === 'queued' ? queued.findIndex((q) => q.key === j.key) + 1 : null,
      children: kids.length ? { done: kids.filter((k) => k.finishedAt !== null).length, total: kids.length } : null,
    };
  };
  const live = mine.filter((j) => j.finishedAt === null).sort((a, b) => a.startedAt - b.startedAt);
  const done = mine.filter((j) => j.finishedAt !== null).sort((a, b) => b.finishedAt! - a.finishedAt!).slice(0, cap);
  const other = top.filter((j) => j.mode !== mode && j.finishedAt === null).length;
  return { chips: [...live, ...done].map(toChip), other };
}

/** Tiến độ việc gộp, cùng dạng `MultiProgress` (YoutubeTrend) / `CompareProgress` (YoutubeCompare). */
export function gatherProgress(jobs: readonly SocialJob[], parent: string): { done: number; total: number; current: string | null; failed: string[] } | null {
  const kids = jobs.filter((j) => j.parent === parent);
  if (!kids.length) return null;
  return {
    done: kids.filter((k) => k.finishedAt !== null).length,
    total: kids.length,
    current: kids.find((k) => k.state === 'running')?.label ?? null,
    failed: kids.filter((k) => k.state === 'error').map((k) => k.label),
  };
}
```

- [ ] **Step 4: Chạy, phải xanh**

Run: `npx vitest run tests/queue-chips.test.ts`
Expected: PASS.

- [ ] **Step 5: Test hỏng cho component**

Tạo `web/tests/queue-strip.test.ts`:

```ts
// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { createElement as h } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { QueueStrip } from '@/client/QueueStrip';
import type { QueueChip } from '@/lib/queue-chips';

const chip = (p: Partial<QueueChip>): QueueChip => ({ key: 'social:1', label: 'yoga', state: 'running', resultId: null, error: null, startedAt: Date.now(), position: null, children: null, ...p });
const noop = () => {};

describe('QueueStrip', () => {
  it('không có chip → không vẽ gì', () => {
    expect(renderToStaticMarkup(h(QueueStrip, { chips: [], other: 0, openId: null, onOpen: noop, onCancel: noop, onDismiss: noop }))).toBe('');
  });
  it('vẽ đủ 4 trạng thái, chip đang mở được đánh dấu, đếm việc ở chế độ khác', () => {
    const html = renderToStaticMarkup(h(QueueStrip, {
      chips: [chip({ key: 'a' }), chip({ key: 'b', state: 'queued', position: 2, label: 'cooking' }), chip({ key: 'c', state: 'done', resultId: 7, label: 'budget' }), chip({ key: 'd', state: 'error', error: 'hỏng', label: 'piano' })],
      other: 3, openId: 7, onOpen: noop, onCancel: noop, onDismiss: noop,
    }));
    expect(html.match(/data-queue-chip=/g)).toHaveLength(4);
    expect(html).toContain('data-state="queued"');
    expect(html).toContain('#2');
    expect(html).toContain('aria-current="true"');
    expect(html).toContain('title="hỏng"');
    expect(html).toContain('+3 ở chế độ khác');
  });
});
```

- [ ] **Step 6: Chạy, phải hỏng**

Run: `npx vitest run tests/queue-strip.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 7: Tạo `web/src/client/QueueStrip.tsx`**

```tsx
// Dải chip hàng chờ trang YouTube (Plan 2 · mục 23.3): mỗi lượt 1 chip; bấm chip đã xong → mở kết quả ngay bên dưới (như tab con).
import { tr } from '@/lib/i18n';
import { mmss, useNow } from '@/components/progress-hooks';
import type { QueueChip } from '@/lib/queue-chips';

export function QueueStrip({ chips, other, openId, onOpen, onCancel, onDismiss }: {
  chips: QueueChip[]; other: number; openId: number | null;
  onOpen: (resultId: number) => void; onCancel: (key: string) => void; onDismiss: (key: string) => void;
}) {
  const now = useNow(chips.some((c) => c.state === 'running'));
  if (!chips.length && !other) return null;
  return (
    <div role="list" aria-label={tr('Hàng chờ')} className="flex flex-wrap items-center gap-2">
      {chips.map((c) => {
        const on = c.resultId !== null && c.resultId === openId;
        const canOpen = c.state === 'done' && c.resultId !== null;
        const tone = c.state === 'error' ? 'border-rose-200 bg-rose-50 text-rose-700'
          : on ? 'border-[var(--accent)] bg-[var(--accent-soft)] text-[var(--accent)]'
          : c.state === 'queued' ? 'border-dashed border-zinc-300 bg-surface text-zinc-500' : 'border-zinc-200 bg-surface text-zinc-700';
        return (
          <span key={c.key} role="listitem" data-queue-chip={c.key} data-state={c.state}
            className={`inline-flex max-w-64 min-w-0 items-center gap-1.5 rounded-full border py-1 pl-2.5 pr-1 text-sm ${tone}`}>
            <button type="button" disabled={!canOpen} aria-current={on || undefined} onClick={() => canOpen && onOpen(c.resultId!)}
              title={c.state === 'error' ? c.error ?? '' : c.label} className="flex min-w-0 items-center gap-1.5 disabled:cursor-default">
              {c.state === 'running' && <span className="progress-spinner !h-3 !w-3 shrink-0" aria-hidden />}
              {c.state === 'queued' && <span aria-hidden className="shrink-0">⏳</span>}
              {c.state === 'done' && <span aria-hidden className="shrink-0 text-emerald-600">✓</span>}
              {c.state === 'error' && <span aria-hidden className="shrink-0">⚠</span>}
              <span className="min-w-0 truncate font-medium">{c.label}</span>
              {c.state === 'queued' && c.position !== null && <span className="shrink-0 text-xs">#{c.position}</span>}
              {c.state === 'running' && <span className="shrink-0 text-xs tabular-nums">{c.children ? `${c.children.done}/${c.children.total} · ` : ''}{mmss(now - c.startedAt)}</span>}
            </button>
            <button type="button" onClick={() => (c.state === 'queued' ? onCancel(c.key) : onDismiss(c.key))} disabled={c.state === 'running'}
              aria-label={c.state === 'queued' ? tr('Huỷ lượt này') : tr('Đóng chip')} title={c.state === 'queued' ? tr('Huỷ lượt này') : tr('Đóng chip')}
              className="grid h-5 w-5 shrink-0 place-items-center rounded-full text-zinc-400 hover:bg-zinc-100 hover:text-zinc-700 disabled:invisible">×</button>
          </span>
        );
      })}
      {other > 0 && <span className="shrink-0 text-xs text-zinc-500">{tr('+{n} ở chế độ khác', { n: other })}</span>}
    </div>
  );
}
```

Thêm vào `en-text-yt-queue.ts`:

```ts
  'Hàng chờ': 'Queue',
  'Huỷ lượt này': 'Cancel this run',
  'Đóng chip': 'Close chip',
  '+{n} ở chế độ khác': '+{n} in other modes',
```

- [ ] **Step 8: Chạy, phải xanh**

Run: `npx vitest run tests/queue-strip.test.ts tests/queue-chips.test.ts tests/i18n-text.test.ts`
Expected: PASS.

- [ ] **Step 9: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/src/lib/queue-chips.ts web/src/client/QueueStrip.tsx web/tests/queue-chips.test.ts web/tests/queue-strip.test.ts web/src/locales/en-text-yt-queue.ts
git commit -m "feat(web): dải chip hàng chờ YouTube (mục 23.3)"
```

---

### Task 6: Ô nhập nhiều dòng + nối form với batch / dải chip

**Files:**
- Create: `web/src/components/MultiLineInput.tsx`
- Modify: `web/src/client/SocialPage.tsx` (`ModePanel` + `KeywordForm`)
- Modify: `web/src/client/YoutubeHunt.tsx:97-130` (`HuntForm`)
- Modify: `web/src/client/YoutubeChannel.tsx:48-69` (`ChannelForm`)
- Modify: `web/src/locales/en-text-yt-queue.ts`
- Test: `web/tests/multi-line-input.test.ts`

**Interfaces:**
- Consumes: `splitItems`, `looksLikeChannel` (Task 2); `queueChips`, `QueueStrip` (Task 5); `/api/social/youtube/batch`, `/api/social/jobs/:key/cancel` (Task 2); `YT_BATCH_MAX` (Task 1).
- Produces:
  - `MultiLineInput` props `{ value: string; onChange: (v: string) => void; onSubmit: () => void; placeholder: string; label: string; maxLength: number }`
  - Kiểu callback form: `type OnBatch = (items: string[], opts: Record<string, unknown>) => void`
  - `HuntForm` / `ChannelForm` thêm prop `onBatch: OnBatch` (bỏ dùng `onRun` cho lượt mới; `onRun` giữ cho chỗ khác gọi)

- [ ] **Step 1: Test hỏng**

Tạo `web/tests/multi-line-input.test.ts`:

```ts
// @vitest-environment node
import { describe, expect, it } from 'vitest';
import { createElement as h } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { MultiLineInput } from '@/components/MultiLineInput';

const r = (value: string) => renderToStaticMarkup(h(MultiLineInput, { value, onChange: () => {}, onSubmit: () => {}, placeholder: 'vd', label: 'Keyword', maxLength: 2000 }));

describe('MultiLineInput', () => {
  it('cao theo số dòng, tối thiểu 1, tối đa 6', () => {
    expect(r('a')).toContain('rows="1"');
    expect(r('a\nb\nc')).toContain('rows="3"');
    expect(r(Array.from({ length: 9 }, () => 'x').join('\n'))).toContain('rows="6"');
  });
});
```

- [ ] **Step 2: Chạy, phải hỏng**

Run: `npx vitest run tests/multi-line-input.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Tạo `web/src/components/MultiLineInput.tsx`**

```tsx
// Ô nhập nhiều dòng (Plan 2 · mục 23.2): mỗi dòng 1 mục. Enter = chạy (như ô 1 dòng cũ), Shift+Enter = xuống dòng; dán danh sách thì giữ nguyên các dòng.
import { input } from '@/client/social-ui';

export function MultiLineInput({ value, onChange, onSubmit, placeholder, label, maxLength }: {
  value: string; onChange: (v: string) => void; onSubmit: () => void; placeholder: string; label: string; maxLength: number;
}) {
  const rows = Math.min(6, Math.max(1, value.split('\n').length));
  return (
    <textarea rows={rows} value={value} placeholder={placeholder} aria-label={label} maxLength={maxLength}
      onChange={(e) => onChange(e.target.value)}
      onKeyDown={(e) => {
        // bộ gõ tiếng Việt đang ghép chữ thì Enter là chốt chữ, không phải chạy
        if (e.key === 'Enter' && !e.shiftKey && !e.nativeEvent.isComposing) { e.preventDefault(); onSubmit(); }
      }}
      className={`${input} min-w-0 resize-none leading-6`} />
  );
}
```

Nếu `@/client/social-ui` không export `input` từ đường dẫn này (lỗi import vòng) thì chép chuỗi class `input` vào file này làm hằng riêng.

- [ ] **Step 4: Chạy, phải xanh**

Run: `npx vitest run tests/multi-line-input.test.ts`
Expected: PASS.

- [ ] **Step 5: `ChannelForm` (`web/src/client/YoutubeChannel.tsx`)**

```tsx
export function ChannelForm({ busy, onRun, onBatch, countries }: { busy: boolean; onRun: (b: Record<string, unknown>) => void; onBatch?: (items: string[], opts: Record<string, unknown>) => void; countries: string[] }) {
  const [text, setText] = useState('');
  const [country, setCountry] = useState('us');
  const [force, setForce] = useState(false);
  const options: CountryOption[] = countries.map((code) => ({ code, label: countryName(code) }));
  const { items, over } = splitItems(text, YT_BATCH_MAX.channel);
  const bad = items.filter((s) => !looksLikeChannel(s));
  const good = items.filter(looksLikeChannel);
  const go = () => {
    if (!good.length) return;
    if (onBatch) onBatch(good, { country, force }); else onRun({ channel: good[0], country, force });
    setText(bad.join('\n')); // giữ lại dòng sai để sửa
  };
  return (
    <form onSubmit={(e: FormEvent) => { e.preventDefault(); go(); }} className={card} aria-labelledby="yt-channel-form">
      <div className="space-y-1">
        <h2 id="yt-channel-form" className="text-lg font-semibold">{tr('Soi từng kênh YouTube')}</h2>
        <p className="flex items-center gap-1.5 text-sm text-zinc-600">{tr('Dán link kênh hoặc @tên, mỗi dòng 1 kênh (tối đa {n}) · ~30 giây / kênh · không cần key', { n: YT_BATCH_MAX.channel })}
          <Hint text={tr('Dán link kênh, link 1 video của kênh, hoặc gõ @tên. Máy đọc 90 video gần nhất, rút keyword từ tiêu đề rồi tìm từng keyword trên YouTube để xem kênh đứng thứ mấy. Không cần key, ~30 giây. Kết quả giữ 7 ngày.')} /></p>
      </div>
      <div className="flex flex-wrap items-start gap-2">
        <MultiLineInput value={text} onChange={setText} onSubmit={go} placeholder={tr('vd. youtube.com/@tenkenh')} label={tr('Link kênh YouTube hoặc @tên')} maxLength={3000} />
        <CountryPicker value={country} onChange={setCountry} options={options} ariaLabel={tr('Nước dùng để tìm keyword')} short className="py-2" />
        <label className="flex shrink-0 items-center gap-1.5 py-2 text-sm text-zinc-600"><input type="checkbox" checked={force} onChange={(e) => setForce(e.target.checked)} />{tr('Tra mới, bỏ kết quả đã lưu')}</label>
        <Button type="submit" variant="primary" loading={busy} loadingLabel={tr('Đang soi…')} disabled={!good.length} className="shrink-0">
          {good.length > 1 ? tr('Soi {n} kênh', { n: good.length }) : tr('Soi kênh')}</Button>
      </div>
      {(bad.length > 0 || over > 0) && <p role="alert" className="text-sm text-rose-700">
        {bad.length > 0 && tr('Không phải link kênh: {x}', { x: bad.join(', ') })}{bad.length > 0 && over > 0 && ' · '}
        {over > 0 && tr('Bỏ {n} dòng dư (tối đa {max})', { n: over, max: YT_BATCH_MAX.channel })}</p>}
    </form>
  );
}
```

Import thêm: `MultiLineInput` từ `@/components/MultiLineInput`, `splitItems, looksLikeChannel` từ `@/lib/multi-input`, `YT_BATCH_MAX` từ `@/lib/yt-queue`.

**Lưu ý:** `yt-queue.ts` import `social-jobs` (chỉ có code thuần, không có gì của máy chủ), nên bundle trang vẫn chạy. Nếu Vite báo `process is not defined` vì `ytConcurrency` đọc `process.env` thì đổi thành `typeof process === 'undefined' ? undefined : process.env.YT_CONCURRENCY`.

- [ ] **Step 6: `HuntForm` (`web/src/client/YoutubeHunt.tsx`)**

Đổi chữ ký thành `{ busy, onRun, onBatch, countries }`, trong đó `onBatch?: (items: string[], opts: Record<string, unknown>) => void`. Thay `topic` / `setTopic` bằng `text` / `setText`, rồi:

```tsx
  const { items, over } = splitItems(text, YT_BATCH_MAX.hunt);
  const go = () => {
    if (!items.length) return;
    if (onBatch) onBatch(items, { country, period, force, settings }); else onRun({ hunt: items[0], country, period, force, settings });
    setText('');
  };
  const submit = (e: FormEvent) => { e.preventDefault(); go(); };
```

Thay `<input className={input} value={topic} … />` bằng:

```tsx
        <MultiLineInput value={text} onChange={setText} onSubmit={go} placeholder={tr('vd. kinh tế, personal finance')} label={tr('Chủ đề')} maxLength={1000} />
```

Đổi hàng nút thành `flex flex-wrap items-start gap-2`. Nút chạy ghi `items.length > 1 ? tr('Săn {n} chủ đề', { n: items.length }) : <chữ cũ>`. Dưới ô nhập thêm:

```tsx
      {items.length > 1 && <p className="text-sm text-zinc-600">{tr('Nhiều chủ đề: mỗi chủ đề tự chạy đủ 3 bước, theo ngưỡng lọc trong Tuỳ chọn')}</p>}
      {over > 0 && <p role="alert" className="text-sm text-rose-700">{tr('Bỏ {n} dòng dư (tối đa {max})', { n: over, max: YT_BATCH_MAX.hunt })}</p>}
```

Placeholder cũ `'vd. kinh tế, personal finance'` có dấu phẩy, mà nay dấu phẩy sẽ tách thành 2 chủ đề. Đổi placeholder thành `tr('vd. personal finance (mỗi dòng 1 chủ đề)')` và thêm khoá mới này vào `en-text-yt-queue.ts`.

- [ ] **Step 7: `KeywordForm` (`web/src/client/SocialPage.tsx`), chỉ khi `source === 'youtube'`**

Thêm prop `onBatch?: (items: string[], opts: Record<string, unknown>) => void`. Khi có `onBatch`:
- Thay ô `<input ref={box} …>` bằng `MultiLineInput`. Ô của Amazon giữ nguyên.
- Lúc chạy: `const { items, over } = splitItems(keyword, YT_BATCH_MAX.niche); onBatch(items, { country: market, force }); setKeyword('');`
- Nút: `items.length > 1 ? tr('Tra {n} keyword', { n: items.length }) : tr('Tra')`
- `over > 0` → câu báo đỏ như ở Step 5.

`prefill` (bấm keyword từ kết quả) vẫn chỉ điền chữ vào ô, giữ như cũ. `box` ref đang dùng để focus khi prefill: nếu `MultiLineInput` không nhận ref thì bọc nó bằng `forwardRef` trong Step 3.

- [ ] **Step 8: `ModePanel` (`web/src/client/SocialPage.tsx`)**

Thêm vào thân `ModePanel`, ngay sau `const markets = …`:

```ts
  // ── Hàng chờ YouTube (mục 23): lượt mới đi /youtube/batch, dải chip đọc sổ việc qua /api/activity ──────────────
  const ytQueued = page === 'youtube' && (mode === 'niche' || mode === 'hunt' || mode === 'channel');
  const [dismissed, setDismissed] = useState<Set<string>>(() => new Set());
  const [notice, setNotice] = useState<string | null>(null);
  const myBatch = useRef<Set<string>>(new Set());
  const autoOpened = useRef(true);
  const { chips, other } = page === 'youtube' ? queueChips(activity?.social ?? [], mode, dismissed) : { chips: [], other: 0 };
  async function runBatch(items: string[], opts: Record<string, unknown>) {
    setError(null);
    try {
      const r = await postJson<{ jobs: { item: string; key: string }[]; errors: { item: string; error: string }[] }>('/api/social/youtube/batch', { mode, items, ...opts });
      myBatch.current = new Set(r.jobs.map((j) => j.key));
      autoOpened.current = false;
      setNotice(tr('Đã thêm {n} lượt vào hàng chờ', { n: r.jobs.length }));
      if (r.errors.length) setError(r.errors.map((e) => `${e.item}: ${e.error}`).join(' · '));
    } catch (e) { setError((e as Error).message); }
  }
  async function cancelJob(key: string) {
    try { await postJson(`/api/social/jobs/${encodeURIComponent(key)}/cancel`, {}); } catch (e) { setError((e as Error).message); }
  }
  // việc của chế độ này xong → tải lại lịch sử; việc xong ĐẦU TIÊN của lượt mình vừa bấm → tự mở (việc sau không tự nhảy)
  const seenDone = useRef<Set<string>>(new Set());
  useEffect(() => {
    if (page !== 'youtube') return;
    const fresh = chips.filter((c) => c.state === 'done' && !seenDone.current.has(c.key));
    if (!fresh.length) return;
    fresh.forEach((c) => seenDone.current.add(c.key));
    const first = autoOpened.current ? null : fresh.find((c) => myBatch.current.has(c.key) && c.resultId !== null);
    if (first) { autoOpened.current = true; setNotice(null); }
    void load().then(() => { setBoardKey((n) => n + 1); if (first) open(first.resultId!); });
    // eslint-disable-next-line react-hooks/exhaustive-deps -- chỉ theo các chip vừa xong
  }, [chips.map((c) => `${c.key}:${c.state}`).join('|')]);
```

Lần đầu render, các chip đã xong từ trước cũng lọt vào `fresh`. Chúng chỉ làm `load()` chạy thêm 1 lần, không tự mở, vì `autoOpened.current` khởi đầu là `true`. Chấp nhận được.

Sửa khoá form và khung chờ cho các chế độ có hàng chờ:

```ts
  const locked = ytQueued ? false : busy || !!serverJob;
```

Dòng `{runningCard}` trong JSX đổi thành `{!ytQueued && runningCard}`. Ngay dưới nó thêm:

```tsx
      {page === 'youtube' && <QueueStrip chips={chips} other={other} openId={shownId} onOpen={open} onCancel={(k) => void cancelJob(k)} onDismiss={(k) => setDismissed((s) => new Set(s).add(k))} />}
      {notice && ytQueued && <p role="status" className="text-sm text-zinc-600">{notice}</p>}
```

Effect `watched` cũ (mở lượt máy chủ vừa xong) chỉ chạy khi `!ytQueued`: thêm `if (ytQueued) return;` ở đầu thân effect.

Truyền `onBatch` vào 3 form:

```tsx
        {page === 'youtube' && mode === 'hunt' && <HuntForm busy={busy} onRun={run} onBatch={runBatch} countries={ytCountries} />}
        {page === 'youtube' && mode === 'channel' && <ChannelForm busy={busy} onRun={run} onBatch={runBatch} countries={ytCountries} />}
```

`KeywordForm` của `niche` thêm `onBatch={runBatch}`. Nút "Soi kênh" trong bảng kênh (`onAuditChannel`) đổi `runRef.current(ask)` thành `void runBatch([String(ask.channel)], { country: ask.country, force: false })` để vào chung hàng chờ. Trước khi đổi, đọc kiểu `ask` trong `YoutubeChannel.tsx` để lấy đúng tên trường.

Import thêm: `QueueStrip` từ `./QueueStrip`, `queueChips` từ `@/lib/queue-chips`, `splitItems` từ `@/lib/multi-input`, `YT_BATCH_MAX` từ `@/lib/yt-queue`, `MultiLineInput` từ `@/components/MultiLineInput`.

Thêm vào `en-text-yt-queue.ts` đủ các chữ mới:

```ts
  'Soi từng kênh YouTube': 'Inspect YouTube channels',
  'Dán link kênh hoặc @tên, mỗi dòng 1 kênh (tối đa {n}) · ~30 giây / kênh · không cần key': 'Paste channel links or @names, one per line (max {n}) · ~30 seconds / channel · no key needed',
  'Soi {n} kênh': 'Inspect {n} channels',
  'Không phải link kênh: {x}': 'Not a channel link: {x}',
  'Bỏ {n} dòng dư (tối đa {max})': 'Dropped {n} extra lines (max {max})',
  'Săn {n} chủ đề': 'Hunt {n} topics',
  'Nhiều chủ đề: mỗi chủ đề tự chạy đủ 3 bước, theo ngưỡng lọc trong Tuỳ chọn': 'Several topics: each runs all 3 steps on its own, using the filters in Options',
  'vd. personal finance (mỗi dòng 1 chủ đề)': 'e.g. personal finance (one topic per line)',
  'Tra {n} keyword': 'Look up {n} keywords',
  'Đã thêm {n} lượt vào hàng chờ': 'Added {n} runs to the queue',
```

- [ ] **Step 9: Typecheck + lint + test toàn bộ**

Run (ở gốc repo): `npm run check`
Expected: xanh. Lỗi kiểu ở chỗ gọi `HuntForm` / `ChannelForm` / `KeywordForm` thì sửa theo chữ ký mới.

- [ ] **Step 10: Xem tận mắt**

Mở preview dev server (`preview_start`, tên server trong `.claude/launch.json` của repo; chưa có thì thêm cấu hình chạy `npm --prefix web run dev`). Vào `/youtube` rồi kiểm:
1. 3 thẻ nhóm. Bấm Soi kênh thì thấy 2 chip Soi từng kênh / So kênh.
2. Tìm ý tưởng: dán 4 keyword (mỗi dòng 1) rồi Enter. Dải chip hiện 3 chip đang chạy + 1 chip ⏳ #1. Lượt xong đầu tiên tự mở. Bấm chip khác thì đổi kết quả.
3. Huỷ chip đang chờ thì chip biến mất.
4. Chuyển sang Soi từng kênh trong lúc Tìm ý tưởng đang chạy: thẻ Tìm ngách ghi "n đang chạy".

Chụp ở 960px và 1340px, cả sáng lẫn tối (Cài đặt → Appearance), cả English lẫn tiếng Việt. Read lại ảnh. Không được có cuộn ngang cả trang, và chip có chữ dài phải `truncate`.

- [ ] **Step 11: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/src/components/MultiLineInput.tsx web/tests/multi-line-input.test.ts web/src/locales/en-text-yt-queue.ts
git add -p web/src/client/SocialPage.tsx web/src/client/YoutubeHunt.tsx web/src/client/YoutubeChannel.tsx
git commit -m "feat(web): gõ nhiều keyword / chủ đề / kênh 1 lần, mở kết quả bằng chip (mục 23.2)"
```

---

### Task 7: Đang trend nhiều nước + So kênh gộp ở máy chủ

**Files:**
- Modify: `web/src/client/SocialPage.tsx` (`runMulti`, `runCompare` trong `ModePanel`, khoảng dòng 234–292)

**Interfaces:**
- Consumes: `POST /api/social/youtube/gather` (Task 2), `gatherProgress` (Task 5), `myBatch` / `autoOpened` (Task 6).
- Produces: không đổi props của `TrendForm` / `CompareForm`. `progress` vẫn là `MultiProgress` / `CompareProgress`, giờ lấy từ sổ việc.

- [ ] **Step 1: Thay `runMulti` + `runCompare`**

Xoá thân 2 hàm cũ và 2 `useState` `progress` / `cmpProgress`. Thay bằng:

```ts
  // mục 23: máy chủ đẩy từng nước / kênh vào hàng chờ rồi tự gộp; trang chỉ nhớ mã việc cha để vẽ tiến độ + tự mở khi xong
  const [gatherKey, setGatherKey] = useState<string | null>(null);
  const gp = gatherKey ? gatherProgress(activity?.social ?? [], gatherKey) : null;
  const progress = mode === 'trend' ? gp : null;
  const cmpProgress = mode === 'compare' ? gp : null;
  async function gather(body: Record<string, unknown>) {
    setError(null);
    try {
      const r = await postJson<{ key: string; children: string[] }>('/api/social/youtube/gather', body);
      setGatherKey(r.key);
      myBatch.current = new Set([r.key]);
      autoOpened.current = false;
    } catch (e) { setError((e as Error).message); }
  }
  const runMulti = (countries: string[], period: TrendPeriod, force: boolean) => gather({ kind: 'trend', countries, period, force });
  const runCompare = (inputs: string[], country: string, mineAt: number | null, force: boolean) => gather({ kind: 'compare', channels: inputs, country, mine: mineAt, force });
  // việc cha báo lỗi → hiện lỗi; xong → effect chip (Task 6) tự mở
  const gatherJob = gatherKey ? activity?.social?.find((j) => j.key === gatherKey) : undefined;
  useEffect(() => {
    if (gatherJob?.state === 'error') setError(gatherJob.error);
    if (gatherJob && gatherJob.finishedAt !== null) setGatherKey(null);
  }, [gatherJob?.state]); // eslint-disable-line react-hooks/exhaustive-deps
```

`gatherKey` bị xoá ngay khi việc cha xong, nhưng effect chip của Task 6 chạy trên `chips` nên vẫn thấy việc cha `done` trong `myBatch`. Để chắc chắn việc tự mở xảy ra trước, đặt khối này **sau** effect chip trong mã nguồn.

Nhánh `trend` / `compare` cũng thuộc hàng chờ. Đổi `ytQueued` ở Task 6 thành `page === 'youtube'`, để `runningCard` cũ và effect `watched` không chạy ở mọi chế độ YouTube. Nút Tra 1 nước của Đang trend (`onRun={run}`) vẫn gọi `/search`. `/search` giờ đi qua hàng chờ, chip vẫn hiện, còn `run()` tự mở kết quả khi request trả về như cũ.

Đổi `TrendForm busy={busy}` thành `busy={!!progress}` và `CompareForm busy={busy}` thành `busy={!!cmpProgress}`.

- [ ] **Step 2: Typecheck + test**

Run (ở gốc repo): `npm run check`
Expected: xanh.

- [ ] **Step 3: Xem tận mắt**

Ở preview:
1. Đang trend: chọn 3 nước rồi chạy. Thanh tiến độ của form đếm 1/3 → 3/3, dải chip có 1 chip "US, VN, JP · week" ghi `2/3 · 0:41`. Xong thì tự mở bảng gộp.
2. Chạy lại rồi rời sang trang khác, đợi khoảng 2 phút, quay lại: chip ✓ có sẵn, bấm vào mở được bảng gộp.
3. So kênh: dán 2 link, đánh dấu Kênh của tôi, chạy. Xong thì mở bảng so, và kênh của tôi được đánh dấu đúng.

- [ ] **Step 4: Commit (chỉ khi anh Tu cho phép)**

```bash
git add -p web/src/client/SocialPage.tsx
git commit -m "feat(web): Đang trend nhiều nước + So kênh gộp ở máy chủ, rời trang vẫn gộp (mục 23)"
```

---

### Task 8: Đo số luồng thật + chốt mặc định

**Files:**
- Create: `web/scripts/yt-concurrency-probe.ts`
- Modify: `docs/web/phase-plan2-23-youtube-gom-nhom-chay-nhieu.md` (mục "Đã đo / chưa đo")
- Modify (nếu số đo bảo đổi): `web/src/lib/yt-queue.ts` `YT_CONCURRENCY_DEFAULT`

- [ ] **Step 1: Viết script đo**

```ts
// Đo hàng chờ YouTube (Plan 2 · mục 23): 5 keyword thật với 1 · 3 · 5 luồng, ghi tổng thời gian + số lỗi.
// Chạy: cd web && npx tsx scripts/yt-concurrency-probe.ts
import { createDb } from '@/db/client';
import { runSocial } from '@/lib/social';
import { createYtQueue } from '@/lib/yt-queue';

const KEYWORDS = ['sourdough bread', 'budget planner', 'piano for beginners', 'home workout', 'excel tips'];

for (const limit of [1, 3, 5]) {
  const db = createDb(':memory:');
  const q = createYtQueue(limit);
  const t0 = Date.now();
  const keys = KEYWORDS.map((k) => q.enqueue({ mode: 'niche', label: k, dedupe: `${limit}:${k}`, run: () => runSocial(db, { source: 'youtube', keyword: k, country: 'us', force: true }) }));
  const res = await Promise.allSettled(keys.map((k) => q.wait(k)));
  const errors = res.filter((r) => r.status === 'rejected').map((r) => String((r as PromiseRejectedResult).reason?.message ?? r));
  console.log(JSON.stringify({ limit, seconds: Math.round((Date.now() - t0) / 1000), ok: res.length - errors.length, errors }));
}
```

Nếu `tsx` không đọc được alias `@/` thì chạy bằng cách mà `scripts/dev.ts` đang dùng (đọc file đó trước), hoặc đổi import sang đường dẫn tương đối `../src/...`.

- [ ] **Step 2: Chạy thật (mạng thật, khoảng 5–10 phút)**

Run (ở `web/`, chạy nền vì có thể quá 2 phút): `npx tsx scripts/yt-concurrency-probe.ts`
Expected: 3 dòng JSON. Ghi nguyên số.

- [ ] **Step 3: Chốt và ghi vào spec**

Trong `docs/web/phase-plan2-23-youtube-gom-nhom-chay-nhieu.md`, thay gạch đầu dòng "**Chưa đo:** …" bằng bảng đo thật, ghi ngày đo:

```markdown
**Đo 2026-11-xx** (5 keyword US, `force`, máy dev, `web/scripts/yt-concurrency-probe.ts`):

| Luồng | Tổng thời gian | Lượt ok | Lỗi |
|---|---|---|---|
| 1 | … giây | …/5 | … |
| 3 | … giây | …/5 | … |
| 5 | … giây | …/5 | … |
```

Luật chốt: lấy số luồng lớn nhất mà **không có lỗi** và nhanh hơn số luồng nhỏ hơn liền trước ít nhất 20%. Nếu 3 luồng có lỗi thì hạ `YT_CONCURRENCY_DEFAULT` xuống 2 và đo lại 2 luồng. Đổi chip đầu trang spec thành `Code xong 2026-11-xx · đã đo`.

- [ ] **Step 4: Commit (chỉ khi anh Tu cho phép)**

```bash
git add web/scripts/yt-concurrency-probe.ts docs/web/phase-plan2-23-youtube-gom-nhom-chay-nhieu.md web/src/lib/yt-queue.ts
git commit -m "docs(web): đo hàng chờ YouTube 1 · 3 · 5 luồng, chốt mặc định (mục 23)"
```

---

### Task 9: Tài liệu + soát cuối

**Files:**
- Modify: `CHANGELOG.md` (dưới `[Unreleased]`)
- Modify: `docs/web/index.md` (chip của mục 23)
- Modify: `docs/cach-dung.md` (nếu có đoạn tả trang YouTube 5 thẻ)

- [ ] **Step 1: CHANGELOG**

Thêm dưới `[Unreleased]`:

```markdown
- **Web** · Trang YouTube gom 3 nhóm (Tìm ngách · Săn kênh · Soi kênh) có chip chế độ; gõ nhiều keyword / chủ đề / link kênh 1 lần; mọi lượt YouTube (trang + MCP) vào 1 hàng chờ máy chủ chạy tối đa `YT_CONCURRENCY` luồng (mặc định 3), có dải chip mở kết quả và huỷ lượt đang chờ; bỏ lỗi "Tab này đang chạy" ở YouTube (Plan 2 · mục 23).
```

- [ ] **Step 2: Trang mục lục + cách dùng**

Ở `docs/web/index.md`, đổi chip mục 23 từ `chip--todo` "Viết 2026-11-15 · chờ anh duyệt" sang trạng thái xong, giống chip của các mục đã code. Chạy `grep -n "Soi 1 kênh\|5 thẻ\|Tab này đang chạy" docs/cach-dung.md`, và sửa câu nào còn tả kiểu cũ.

- [ ] **Step 3: Kiểm cuối**

Run (ở gốc repo): `npm run check && npm run docs:build`
Expected: cả 2 xanh.

- [ ] **Step 4: Commit (chỉ khi anh Tu cho phép)**

```bash
git add CHANGELOG.md docs/web/index.md docs/cach-dung.md
git commit -m "docs: ghi mục 23 trang YouTube gom nhóm + hàng chờ"
```
