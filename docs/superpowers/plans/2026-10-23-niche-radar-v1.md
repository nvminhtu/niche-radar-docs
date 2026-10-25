# niche-radar v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Web tool local: gõ một niche → tra Google Play, App Store, Google Trends, Reddit → lưu SQLite → dashboard dữ liệu thô + số liệu thống kê.

**Architecture:** Một app Next.js 15 (App Router). `POST /api/research` tạo run rồi chạy nền 4 collector song song trong cùng process Node; mỗi collector là một module độc lập ghi thẳng vào SQLite và cập nhật `source_jobs`. Trang `/r/[id]` hỏi `GET /api/research/[id]` mỗi 2 giây; `getRunView()` gom toàn bộ dữ liệu + số liệu thống kê thành một object cho UI.

**Tech Stack:** Next.js 15.5 · TypeScript · Tailwind · better-sqlite3 + Drizzle ORM (drizzle-kit migrations) · Recharts 3 · google-play-scraper 10 · google-trends-api 4 · Vitest 3 · tsx.

**Spec:** `docs/superpowers/specs/2026-10-23-niche-radar-design.md`

## Global Constraints

- Repo: `niche-radar`, nhánh `main`. Mọi lệnh chạy từ thư mục này.
- Node 22. Cổng dev **3200** (`npm run dev`).
- DB: file `data/niche.db` (gitignore); ghi đè bằng env `NICHE_DB`. Test dùng `:memory:`.
- 4 nguồn, tên cố định: `playstore`, `appstore`, `trends`, `reddit`. Store trong bảng `apps`: `play`, `appstore`.
- Trạng thái job: `pending` → `running` → `done` | `error`.
- Mã lỗi: `RATE_LIMITED`, `NETWORK`, `MISSING_KEYS`, `PARSE`, `UNKNOWN`.
- Nhịp gọi: Play ≤ 1 req/s · iTunes ≤ 20 req/phút (1 req / 3s) · Reddit ≤ 1 req/s · Trends retry 3 lần chờ 2s → 5s → 10s với `RATE_LIMITED`/`NETWORK`.
- Mỗi keyword lấy top **30** app mỗi store. Keyword = seed + tối đa **5** gợi ý Play autocomplete. Trends chỉ tra seed, 12 tháng.
- Cache **24 giờ** theo `seed` + `country`; `force: true` bỏ qua cache.
- Seed và keyword lưu dạng `trim().toLowerCase()`. Country lưu dạng chữ hoa (`US`).
- Nước hỗ trợ: `US, GB, VN, DE, JP`, mặc định `US`.
- Pattern bài xin app (không phân biệt hoa thường): `is there an app`, `looking for an app`, `app that`, `alternative to`, `recommend an app`.
- Key Reddit trong `.env.local`: `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`.
- Ngày giờ lưu dạng chuỗi ISO 8601 (UTC).
- Ghi DB của một collector nằm trong một transaction.
- Lệch nhỏ so với spec, có chủ ý: `CollectContext` có thêm `db` và `seed`. Lúc khởi động, job còn `pending` **hoặc** `running` đều chuyển sang `error`/`UNKNOWN`/`interrupted` (job `pending` mồ côi cũng sẽ treo mãi).

## File Structure

```
niche-radar/
├── .claude/launch.json             preview config (cổng 3200)
├── drizzle.config.ts               drizzle-kit → thư mục drizzle/
├── drizzle/                        SQL migration sinh tự động (commit)
├── next.config.ts                  serverExternalPackages: better-sqlite3
├── vitest.config.ts
├── scripts/smoke.ts                gọi thật 4 nguồn, in số dòng
├── src/
│   ├── types/vendor.d.ts           khai module không có type
│   ├── db/schema.ts                bảng Drizzle + SOURCES
│   ├── db/client.ts                createDb, getDb, markInterrupted
│   ├── lib/errors.ts               CollectorError, toCollectorError
│   ├── lib/rate-limit.ts           createLimiter, withRetry, sleep
│   ├── lib/stats.ts                hàm thống kê thuần
│   ├── lib/countries.ts            COUNTRIES
│   ├── lib/format.ts               định dạng số/ngày cho UI
│   ├── lib/run-research.ts         orchestrator: run, keyword, cache, retry
│   ├── lib/run-view.ts             getRunView, listRuns, kiểu dữ liệu cho UI
│   ├── lib/deps.ts                 nối collector thật vào orchestrator
│   ├── collectors/types.ts         Collector, CollectContext, StoreApp, StoreHit
│   ├── collectors/store-apps.ts    saveStoreHits (dùng chung 2 store)
│   ├── collectors/playstore.ts
│   ├── collectors/appstore.ts
│   ├── collectors/trends.ts
│   ├── collectors/reddit.ts
│   ├── app/layout.tsx  app/page.tsx  app/r/[id]/page.tsx
│   ├── app/api/research/route.ts
│   ├── app/api/research/[id]/route.ts
│   ├── app/api/research/[id]/retry/route.ts
│   └── components/                 SearchForm, RunHistory, SourceChip, RunDashboard,
│                                   RunHeader, SourceBlock, StatTiles, KeywordTable,
│                                   CompetitorBlock, TrendsBlock, RedditBlock, charts/*
└── tests/                          *.test.ts + fixtures/<source>/*.json
```

---

### Task 1: Scaffold Next.js + Vitest + dependency

**Files:**
- Create: toàn bộ khung Next.js (từ `create-next-app`), `next.config.ts`, `vitest.config.ts`, `web/src/types/vendor.d.ts`, `.claude/launch.json`, `web/tests/sanity.test.ts`
- Modify: `.gitignore`, `package.json`

**Interfaces:**
- Produces: alias `@/` → `web/src/`; script `dev`, `build`, `start`, `test`, `smoke`, `db:generate`.

- [ ] **Step 1: Sinh khung Next.js vào thư mục tạm rồi chép vào repo** (repo đã có `docs/`, `.git` nên không sinh thẳng được)

```bash
cd Niche-Research
npx --yes create-next-app@15.5.28 nr-tmp --ts --tailwind --eslint --app --src-dir --use-npm --no-turbopack --import-alias "@/*" --yes
rsync -a --exclude .git --exclude .gitignore --exclude README.md nr-tmp/ niche-radar/
rm -rf nr-tmp
cd niche-radar
```

Expected: `niche-radar/` có `package.json`, `src/app/page.tsx`, `next.config.ts`.

- [ ] **Step 2: Cài dependency**

```bash
npm install better-sqlite3@13.0.3 drizzle-orm@0.45.4 google-play-scraper@10.1.4 google-trends-api@4.9.2 recharts@3.10.1
npm install -D drizzle-kit@0.31.11 vitest@5.0.5 tsx @types/better-sqlite3
```

Expected: không có lỗi build native của better-sqlite3.

- [ ] **Step 3: Ghi `next.config.ts`**

```ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  serverExternalPackages: ['better-sqlite3'],
};

export default nextConfig;
```

- [ ] **Step 4: Ghi `vitest.config.ts`**

```ts
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: { environment: 'node', include: ['tests/**/*.test.ts'] },
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
});
```

- [ ] **Step 5: Ghi `web/src/types/vendor.d.ts`** (2 thư viện không kèm type)

```ts
declare module 'google-play-scraper';
declare module 'google-trends-api';
```

- [ ] **Step 6: Sửa `scripts` trong `package.json`** (giữ nguyên `lint` do create-next-app tạo)

```json
"scripts": {
  "dev": "next dev -p 3200",
  "build": "next build",
  "start": "next start -p 3200",
  "lint": "next lint",
  "test": "vitest run",
  "smoke": "tsx scripts/smoke.ts",
  "db:generate": "drizzle-kit generate"
}
```

- [ ] **Step 7: Thay `.gitignore`**

```
node_modules/
.next/
next-env.d.ts
data/
.env*.local
.DS_Store
*.tsbuildinfo
```

- [ ] **Step 8: Ghi `.claude/launch.json`**

```json
{
  "version": "0.0.1",
  "configurations": [
    { "name": "niche-radar", "runtimeExecutable": "npm", "runtimeArgs": ["run", "dev"], "port": 3200 }
  ]
}
```

- [ ] **Step 9: Test sanity** — ghi `web/tests/sanity.test.ts`

```ts
import { describe, expect, it } from 'vitest';

describe('toolchain', () => {
  it('runs vitest', () => {
    expect(1 + 1).toBe(2);
  });
});
```

- [ ] **Step 10: Chạy test + build**

Run: `npm test && npm run build`
Expected: `1 passed`; build xong không lỗi.

- [ ] **Step 11: Commit**

```bash
git add -A
git commit -m "chore: scaffold Next.js 15 + Vitest + dependency"
```

---

### Task 2: Database schema + client

**Files:**
- Create: `web/src/db/schema.ts`, `web/src/db/client.ts`, `drizzle.config.ts`, `web/drizzle/*` (sinh tự động)
- Test: `web/tests/db.test.ts`

**Interfaces:**
- Produces:
  - `SOURCES: readonly ['playstore','appstore','trends','reddit']`, `type Source`
  - bảng Drizzle: `runs`, `keywords`, `sourceJobs`, `apps`, `appSnapshots`, `keywordHits`, `trendPoints`, `trendRelated`, `redditPosts`
  - `type Db`, `createDb(file: string): Db`, `getDb(): Db`, `markInterrupted(db: Db): number`

- [ ] **Step 1: Ghi `web/src/db/schema.ts`**

```ts
import { integer, primaryKey, real, sqliteTable, text, uniqueIndex } from 'drizzle-orm/sqlite-core';

export const SOURCES = ['playstore', 'appstore', 'trends', 'reddit'] as const;
export type Source = (typeof SOURCES)[number];
export const JOB_STATUSES = ['pending', 'running', 'done', 'error'] as const;
export type JobStatus = (typeof JOB_STATUSES)[number];
export const STORES = ['play', 'appstore'] as const;
export type Store = (typeof STORES)[number];

export const runs = sqliteTable('runs', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  seed: text('seed').notNull(),
  country: text('country').notNull(),
  createdAt: text('created_at').notNull(),
});

export const keywords = sqliteTable('keywords', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
  term: text('term').notNull(),
  origin: text('origin', { enum: ['seed', 'play_suggest'] }).notNull(),
});

export const sourceJobs = sqliteTable(
  'source_jobs',
  {
    runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
    source: text('source', { enum: SOURCES }).notNull(),
    status: text('status', { enum: JOB_STATUSES }).notNull(),
    errorCode: text('error_code'),
    errorMessage: text('error_message'),
    startedAt: text('started_at'),
    finishedAt: text('finished_at'),
  },
  (t) => [primaryKey({ columns: [t.runId, t.source] })],
);

export const apps = sqliteTable(
  'apps',
  {
    id: integer('id').primaryKey({ autoIncrement: true }),
    store: text('store', { enum: STORES }).notNull(),
    storeAppId: text('store_app_id').notNull(),
    title: text('title').notNull(),
    developer: text('developer').notNull(),
    iconUrl: text('icon_url'),
    url: text('url').notNull(),
    genre: text('genre'),
    price: real('price').notNull().default(0),
    releasedAt: text('released_at'),
  },
  (t) => [uniqueIndex('apps_store_app_uq').on(t.store, t.storeAppId)],
);

export const appSnapshots = sqliteTable(
  'app_snapshots',
  {
    appId: integer('app_id').notNull().references(() => apps.id),
    runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
    rating: real('rating'),
    ratingsCount: integer('ratings_count'),
    installsMin: integer('installs_min'),
    updatedAt: text('updated_at'),
  },
  (t) => [primaryKey({ columns: [t.appId, t.runId] })],
);

export const keywordHits = sqliteTable(
  'keyword_hits',
  {
    keywordId: integer('keyword_id').notNull().references(() => keywords.id, { onDelete: 'cascade' }),
    appId: integer('app_id').notNull().references(() => apps.id),
    rank: integer('rank').notNull(),
  },
  (t) => [primaryKey({ columns: [t.keywordId, t.appId] })],
);

export const trendPoints = sqliteTable(
  'trend_points',
  {
    runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
    date: text('date').notNull(),
    value: integer('value').notNull(),
  },
  (t) => [primaryKey({ columns: [t.runId, t.date] })],
);

export const trendRelated = sqliteTable('trend_related', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
  query: text('query').notNull(),
  value: integer('value').notNull(),
  kind: text('kind', { enum: ['top', 'rising'] }).notNull(),
});

export const redditPosts = sqliteTable(
  'reddit_posts',
  {
    runId: integer('run_id').notNull().references(() => runs.id, { onDelete: 'cascade' }),
    keywordId: integer('keyword_id').notNull().references(() => keywords.id, { onDelete: 'cascade' }),
    postId: text('post_id').notNull(),
    subreddit: text('subreddit').notNull(),
    title: text('title').notNull(),
    url: text('url').notNull(),
    score: integer('score').notNull(),
    numComments: integer('num_comments').notNull(),
    createdAt: text('created_at').notNull(),
    isAppRequest: integer('is_app_request', { mode: 'boolean' }).notNull(),
  },
  (t) => [primaryKey({ columns: [t.runId, t.postId] })],
);
```

- [ ] **Step 2: Ghi `drizzle.config.ts` và sinh migration**

```ts
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  dialect: 'sqlite',
  schema: './src/db/schema.ts',
  out: './drizzle',
});
```

Run: `npm run db:generate`
Expected: thư mục `web/drizzle/` có `0000_*.sql` + `meta/`.

- [ ] **Step 3: Viết test fail** — `web/tests/db.test.ts`

```ts
import { eq } from 'drizzle-orm';
import { describe, expect, it } from 'vitest';
import { createDb, markInterrupted } from '@/db/client';
import { keywords, runs, sourceJobs } from '@/db/schema';

function seedRun(db: ReturnType<typeof createDb>) {
  const run = db.insert(runs).values({ seed: 'habit tracker', country: 'US', createdAt: new Date().toISOString() })
    .returning({ id: runs.id }).get();
  return run.id;
}

describe('db client', () => {
  it('migrates an in-memory database', () => {
    const db = createDb(':memory:');
    expect(seedRun(db)).toBe(1);
  });

  it('marks pending and running jobs as interrupted', () => {
    const db = createDb(':memory:');
    const runId = seedRun(db);
    db.insert(sourceJobs).values([
      { runId, source: 'playstore', status: 'running' },
      { runId, source: 'appstore', status: 'pending' },
      { runId, source: 'trends', status: 'done' },
    ]).run();
    expect(markInterrupted(db)).toBe(2);
    const rows = db.select().from(sourceJobs).where(eq(sourceJobs.runId, runId)).all();
    const play = rows.find((r) => r.source === 'playstore')!;
    expect(play.status).toBe('error');
    expect(play.errorCode).toBe('UNKNOWN');
    expect(play.errorMessage).toBe('interrupted');
    expect(rows.find((r) => r.source === 'trends')!.status).toBe('done');
  });

  it('cascades keyword deletes with their run', () => {
    const db = createDb(':memory:');
    const runId = seedRun(db);
    db.insert(keywords).values({ runId, term: 'habit tracker', origin: 'seed' }).run();
    db.delete(runs).where(eq(runs.id, runId)).run();
    expect(db.select().from(keywords).all()).toHaveLength(0);
  });
});
```

- [ ] **Step 4: Chạy để thấy fail**

Run: `npx vitest run tests/db.test.ts`
Expected: FAIL, `Cannot find module '@/db/client'` hoặc tương đương.

- [ ] **Step 5: Ghi `web/src/db/client.ts`**

```ts
import { mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import Database from 'better-sqlite3';
import { inArray } from 'drizzle-orm';
import { type BetterSQLite3Database, drizzle } from 'drizzle-orm/better-sqlite3';
import { migrate } from 'drizzle-orm/better-sqlite3/migrator';
import * as schema from './schema';

export type Db = BetterSQLite3Database<typeof schema>;

export function createDb(file: string): Db {
  if (file !== ':memory:') mkdirSync(dirname(file), { recursive: true });
  const sqlite = new Database(file);
  sqlite.pragma('journal_mode = WAL');
  sqlite.pragma('foreign_keys = ON');
  const db = drizzle(sqlite, { schema });
  migrate(db, { migrationsFolder: join(process.cwd(), 'drizzle') });
  return db;
}

/** Job bị bỏ dở khi process trước chết: không ai chạy tiếp nữa, đánh dấu lỗi. */
export function markInterrupted(db: Db): number {
  return db
    .update(schema.sourceJobs)
    .set({ status: 'error', errorCode: 'UNKNOWN', errorMessage: 'interrupted', finishedAt: new Date().toISOString() })
    .where(inArray(schema.sourceJobs.status, ['pending', 'running']))
    .run().changes;
}

// Giữ một kết nối cho cả process; globalThis để HMR của next dev không mở lại DB.
const holder = globalThis as unknown as { __nicheDb?: Db };

export function getDb(): Db {
  if (!holder.__nicheDb) {
    holder.__nicheDb = createDb(process.env.NICHE_DB ?? join(process.cwd(), 'data', 'niche.db'));
    markInterrupted(holder.__nicheDb);
  }
  return holder.__nicheDb;
}
```

- [ ] **Step 6: Chạy test**

Run: `npx vitest run tests/db.test.ts`
Expected: PASS 3 test.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat(db): schema SQLite + client có migration và đánh dấu job bị ngắt"
```

---

### Task 3: Lỗi, rate limit, retry

**Files:**
- Create: `web/src/lib/errors.ts`, `web/src/lib/rate-limit.ts`
- Test: `web/tests/errors.test.ts`, `web/tests/rate-limit.test.ts`

**Interfaces:**
- Produces:
  - `type ErrorCode`, `class CollectorError(code: ErrorCode, message: string)` có `.code`
  - `toCollectorError(err: unknown): CollectorError`
  - `sleep(ms: number): Promise<void>`
  - `createLimiter(minIntervalMs: number): <T>(fn: () => Promise<T>) => Promise<T>`
  - `withRetry<T>(fn: () => Promise<T>, delays: number[], shouldRetry: (e: unknown) => boolean): Promise<T>`

- [ ] **Step 1: Viết test fail** — `web/tests/errors.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { CollectorError, toCollectorError } from '@/lib/errors';

describe('toCollectorError', () => {
  it('keeps a CollectorError as is', () => {
    const e = new CollectorError('MISSING_KEYS', 'x');
    expect(toCollectorError(e)).toBe(e);
  });
  it('maps 429 messages to RATE_LIMITED', () => {
    expect(toCollectorError(new Error('Request failed with status 429')).code).toBe('RATE_LIMITED');
  });
  it('maps network failures to NETWORK', () => {
    expect(toCollectorError(new Error('fetch failed')).code).toBe('NETWORK');
    expect(toCollectorError(new Error('getaddrinfo ENOTFOUND x')).code).toBe('NETWORK');
  });
  it('maps SyntaxError to PARSE', () => {
    expect(toCollectorError(new SyntaxError('Unexpected token <')).code).toBe('PARSE');
  });
  it('falls back to UNKNOWN', () => {
    expect(toCollectorError('boom').code).toBe('UNKNOWN');
  });
});
```

`web/tests/rate-limit.test.ts`

```ts
import { describe, expect, it, vi } from 'vitest';
import { createLimiter, withRetry } from '@/lib/rate-limit';

describe('createLimiter', () => {
  it('spaces calls by the minimum interval', async () => {
    const limit = createLimiter(50);
    const times: number[] = [];
    await Promise.all([1, 2, 3].map(() => limit(async () => { times.push(Date.now()); })));
    expect(times[1] - times[0]).toBeGreaterThanOrEqual(45);
    expect(times[2] - times[1]).toBeGreaterThanOrEqual(45);
  });
});

describe('withRetry', () => {
  it('retries until success', async () => {
    const fn = vi.fn().mockRejectedValueOnce(new Error('a')).mockRejectedValueOnce(new Error('b')).mockResolvedValue('ok');
    await expect(withRetry(fn, [1, 1, 1], () => true)).resolves.toBe('ok');
    expect(fn).toHaveBeenCalledTimes(3);
  });
  it('does not retry when shouldRetry is false', async () => {
    const fn = vi.fn().mockRejectedValue(new Error('fatal'));
    await expect(withRetry(fn, [1, 1], () => false)).rejects.toThrow('fatal');
    expect(fn).toHaveBeenCalledTimes(1);
  });
  it('throws the last error after delays run out', async () => {
    const fn = vi.fn().mockRejectedValue(new Error('still down'));
    await expect(withRetry(fn, [1, 1], () => true)).rejects.toThrow('still down');
    expect(fn).toHaveBeenCalledTimes(3);
  });
});
```

- [ ] **Step 2: Chạy để thấy fail**

Run: `npx vitest run tests/errors.test.ts tests/rate-limit.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Ghi `web/src/lib/errors.ts`**

```ts
export type ErrorCode = 'RATE_LIMITED' | 'NETWORK' | 'MISSING_KEYS' | 'PARSE' | 'UNKNOWN';

export class CollectorError extends Error {
  constructor(public code: ErrorCode, message: string) {
    super(message);
    this.name = 'CollectorError';
  }
}

export function toCollectorError(err: unknown): CollectorError {
  if (err instanceof CollectorError) return err;
  const message = err instanceof Error ? err.message : String(err);
  if (/\b429\b|too many requests/i.test(message)) return new CollectorError('RATE_LIMITED', message);
  if (/fetch failed|ENOTFOUND|ECONNRESET|ETIMEDOUT|ECONNREFUSED|socket hang up/i.test(message)) {
    return new CollectorError('NETWORK', message);
  }
  if (err instanceof SyntaxError) return new CollectorError('PARSE', message);
  return new CollectorError('UNKNOWN', message);
}
```

- [ ] **Step 4: Ghi `web/src/lib/rate-limit.ts`**

```ts
export const sleep = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms));

/** Xếp lịch để hai lần gọi cách nhau ít nhất minIntervalMs, kể cả khi gọi song song. */
export function createLimiter(minIntervalMs: number) {
  let nextSlot = 0;
  return async function schedule<T>(fn: () => Promise<T>): Promise<T> {
    const now = Date.now();
    const at = Math.max(now, nextSlot);
    nextSlot = at + minIntervalMs;
    if (at > now) await sleep(at - now);
    return fn();
  };
}

export async function withRetry<T>(
  fn: () => Promise<T>,
  delays: number[],
  shouldRetry: (e: unknown) => boolean,
): Promise<T> {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (e) {
      if (attempt >= delays.length || !shouldRetry(e)) throw e;
      await sleep(delays[attempt]);
    }
  }
}
```

- [ ] **Step 5: Chạy test**

Run: `npx vitest run tests/errors.test.ts tests/rate-limit.test.ts`
Expected: PASS 9 test.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(lib): CollectorError, rate limiter, retry"
```

---

### Task 4: Hàm thống kê thuần

**Files:**
- Create: `web/src/lib/stats.ts`
- Test: `web/tests/stats.test.ts`

**Interfaces:**
- Produces:
  - `median(xs: number[]): number | null`
  - `INSTALL_BUCKETS: string[]`, `installBucket(n: number): string`
  - `AGE_BUCKETS: string[]`, `daysSince(iso: string, now: Date): number`, `ageBucket(iso: string, now: Date): string`
  - `countBy<T>(items: T[], key: (t: T) => string, order?: string[]): { key: string; count: number }[]`
  - `monthKey(iso: string): string` (dạng `YYYY-MM`), `lastMonths(now: Date, n: number): string[]`

- [ ] **Step 1: Viết test fail** — `web/tests/stats.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { ageBucket, countBy, daysSince, installBucket, lastMonths, median, monthKey } from '@/lib/stats';

const NOW = new Date('2026-10-23T00:00:00Z');

describe('stats', () => {
  it('median', () => {
    expect(median([3, 1, 2])).toBe(2);
    expect(median([1, 2, 3, 4])).toBe(2.5);
    expect(median([])).toBeNull();
  });

  it('installBucket', () => {
    expect(installBucket(999)).toBe('<1K');
    expect(installBucket(1_000)).toBe('1K–10K');
    expect(installBucket(50_000)).toBe('10K–100K');
    expect(installBucket(100_000)).toBe('100K–1M');
    expect(installBucket(1_000_000)).toBe('1M+');
  });

  it('daysSince and ageBucket', () => {
    expect(daysSince('2026-10-13T00:00:00Z', NOW)).toBe(10);
    expect(ageBucket('2026-09-01T00:00:00Z', NOW)).toBe('<3 tháng');
    expect(ageBucket('2026-03-01T00:00:00Z', NOW)).toBe('3–12 tháng');
    expect(ageBucket('2025-06-01T00:00:00Z', NOW)).toBe('1–2 năm');
    expect(ageBucket('2023-01-01T00:00:00Z', NOW)).toBe('>2 năm');
  });

  it('countBy keeps the given order and fills zeros', () => {
    expect(countBy(['b', 'a', 'b'], (x) => x, ['a', 'b', 'c'])).toEqual([
      { key: 'a', count: 1 }, { key: 'b', count: 2 }, { key: 'c', count: 0 },
    ]);
  });

  it('countBy without order sorts by count desc then key', () => {
    expect(countBy(['x', 'y', 'y', 'z'], (v) => v)).toEqual([
      { key: 'y', count: 2 }, { key: 'x', count: 1 }, { key: 'z', count: 1 },
    ]);
  });

  it('monthKey and lastMonths', () => {
    expect(monthKey('2026-03-15T10:00:00Z')).toBe('2026-03');
    expect(lastMonths(NOW, 3)).toEqual(['2026-08', '2026-09', '2026-10']);
  });
});
```

- [ ] **Step 2: Chạy để thấy fail**

Run: `npx vitest run tests/stats.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Ghi `web/src/lib/stats.ts`**

```ts
const DAY_MS = 86_400_000;

export function median(xs: number[]): number | null {
  if (xs.length === 0) return null;
  const s = [...xs].sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

export const INSTALL_BUCKETS = ['<1K', '1K–10K', '10K–100K', '100K–1M', '1M+'];

export function installBucket(n: number): string {
  if (n < 1_000) return '<1K';
  if (n < 10_000) return '1K–10K';
  if (n < 100_000) return '10K–100K';
  if (n < 1_000_000) return '100K–1M';
  return '1M+';
}

export const AGE_BUCKETS = ['<3 tháng', '3–12 tháng', '1–2 năm', '>2 năm'];

export function daysSince(iso: string, now: Date): number {
  return Math.floor((now.getTime() - new Date(iso).getTime()) / DAY_MS);
}

export function ageBucket(iso: string, now: Date): string {
  const d = daysSince(iso, now);
  if (d < 91) return '<3 tháng';
  if (d < 365) return '3–12 tháng';
  if (d < 730) return '1–2 năm';
  return '>2 năm';
}

export function countBy<T>(items: T[], key: (t: T) => string, order?: string[]) {
  const counts = new Map<string, number>();
  for (const item of items) counts.set(key(item), (counts.get(key(item)) ?? 0) + 1);
  if (order) return order.map((k) => ({ key: k, count: counts.get(k) ?? 0 }));
  return [...counts.entries()]
    .map(([k, count]) => ({ key: k, count }))
    .sort((a, b) => b.count - a.count || a.key.localeCompare(b.key));
}

export const monthKey = (iso: string) => iso.slice(0, 7);

export function lastMonths(now: Date, n: number): string[] {
  const out: string[] = [];
  for (let i = n - 1; i >= 0; i--) {
    out.push(new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth() - i, 1)).toISOString().slice(0, 7));
  }
  return out;
}
```

- [ ] **Step 4: Chạy test**

Run: `npx vitest run tests/stats.test.ts`
Expected: PASS 6 test.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(lib): hàm thống kê (median, mốc số cài, tuổi update, đếm theo tháng)"
```

---

### Task 5: Kiểu collector chung + Google Play collector

**Files:**
- Create: `web/src/collectors/types.ts`, `web/src/collectors/store-apps.ts`, `web/src/collectors/playstore.ts`
- Test: `web/tests/playstore.test.ts`, `web/tests/store-apps.test.ts`, `web/tests/fixtures/playstore/app.json`

**Interfaces:**
- Consumes: `Db`, bảng `apps`/`appSnapshots`/`keywordHits` (Task 2); `createLimiter` (Task 3)
- Produces:
  - `type CollectContext = { db: Db; runId: number; seed: string; country: string; keywords: { id: number; term: string }[] }`
  - `type Collector = (ctx: CollectContext) => Promise<void>`
  - `type StoreApp`, `type StoreHit = { keywordId: number; rank: number; app: StoreApp }`
  - `saveStoreHits(db: Db, runId: number, hits: StoreHit[]): void`
  - `normalizePlayApp(raw: any): StoreApp`, `suggestPlayKeywords(seed: string, country: string, max?: number): Promise<string[]>`, `collectPlaystore: Collector`

- [ ] **Step 1: Ghi `web/src/collectors/types.ts`**

```ts
import type { Db } from '@/db/client';
import type { Store } from '@/db/schema';

export type CollectContext = {
  db: Db;
  runId: number;
  seed: string;
  country: string; // chữ hoa, ví dụ 'US'
  keywords: { id: number; term: string }[];
};

/** Tự ghi DB trong một transaction; ném lỗi khi thất bại. */
export type Collector = (ctx: CollectContext) => Promise<void>;

export type StoreApp = {
  store: Store;
  storeAppId: string;
  title: string;
  developer: string;
  iconUrl: string | null;
  url: string;
  genre: string | null;
  price: number;
  releasedAt: string | null;
  rating: number | null;
  ratingsCount: number | null;
  installsMin: number | null;
  updatedAt: string | null;
};

export type StoreHit = { keywordId: number; rank: number; app: StoreApp };
```

- [ ] **Step 2: Ghi fixture `web/tests/fixtures/playstore/app.json`** (rút gọn từ kết quả `gplay.app()`; thay bằng bản ghi thật khi chạy smoke ở Task 15 nếu khác)

```json
{
  "appId": "com.habit.tracker",
  "title": "Habit Tracker",
  "developer": "Habit Labs",
  "icon": "https://play-lh.googleusercontent.com/icon.png",
  "url": "https://play.google.com/store/apps/details?id=com.habit.tracker&hl=en&gl=us",
  "genre": "Productivity",
  "price": 0,
  "free": true,
  "score": 4.6,
  "ratings": 125000,
  "minInstalls": 1000000,
  "installs": "1,000,000+",
  "released": "Mar 4, 2019",
  "updated": 1758844800000
}
```

- [ ] **Step 3: Viết test fail** — `web/tests/playstore.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { normalizePlayApp } from '@/collectors/playstore';
import raw from './fixtures/playstore/app.json';

describe('normalizePlayApp', () => {
  it('maps a gplay.app() result to a StoreApp', () => {
    expect(normalizePlayApp(raw)).toEqual({
      store: 'play',
      storeAppId: 'com.habit.tracker',
      title: 'Habit Tracker',
      developer: 'Habit Labs',
      iconUrl: 'https://play-lh.googleusercontent.com/icon.png',
      url: 'https://play.google.com/store/apps/details?id=com.habit.tracker&hl=en&gl=us',
      genre: 'Productivity',
      price: 0,
      releasedAt: new Date('Mar 4, 2019').toISOString(),
      rating: 4.6,
      ratingsCount: 125000,
      installsMin: 1000000,
      updatedAt: new Date(1758844800000).toISOString(),
    });
  });

  it('tolerates missing optional fields', () => {
    const app = normalizePlayApp({ appId: 'x', title: 'X', url: 'u', released: 'not a date' });
    expect(app.developer).toBe('');
    expect(app.releasedAt).toBeNull();
    expect(app.updatedAt).toBeNull();
    expect(app.installsMin).toBeNull();
  });
});
```

`web/tests/store-apps.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import type { StoreApp } from '@/collectors/types';
import { saveStoreHits } from '@/collectors/store-apps';
import { createDb } from '@/db/client';
import { appSnapshots, apps, keywordHits, keywords, runs } from '@/db/schema';

const app = (over: Partial<StoreApp> = {}): StoreApp => ({
  store: 'play', storeAppId: 'a1', title: 'A1', developer: 'Dev', iconUrl: null, url: 'u', genre: null,
  price: 0, releasedAt: null, rating: 4.5, ratingsCount: 10, installsMin: 1000, updatedAt: null, ...over,
});

function setup() {
  const db = createDb(':memory:');
  const runId = db.insert(runs).values({ seed: 's', country: 'US', createdAt: 'now' }).returning({ id: runs.id }).get().id;
  const [k1, k2] = db.insert(keywords).values([
    { runId, term: 's', origin: 'seed' }, { runId, term: 's2', origin: 'play_suggest' },
  ]).returning({ id: keywords.id }).all();
  return { db, runId, k1: k1.id, k2: k2.id };
}

describe('saveStoreHits', () => {
  it('stores one app row and one snapshot for an app found by two keywords', () => {
    const { db, runId, k1, k2 } = setup();
    saveStoreHits(db, runId, [{ keywordId: k1, rank: 1, app: app() }, { keywordId: k2, rank: 3, app: app() }]);
    expect(db.select().from(apps).all()).toHaveLength(1);
    expect(db.select().from(appSnapshots).all()).toHaveLength(1);
    expect(db.select().from(keywordHits).all().map((h) => h.rank).sort()).toEqual([1, 3]);
  });

  it('updates app details on a later run', () => {
    const { db, runId, k1 } = setup();
    saveStoreHits(db, runId, [{ keywordId: k1, rank: 1, app: app() }]);
    const run2 = db.insert(runs).values({ seed: 's', country: 'US', createdAt: 'now' }).returning({ id: runs.id }).get().id;
    const k = db.insert(keywords).values({ runId: run2, term: 's', origin: 'seed' }).returning({ id: keywords.id }).get().id;
    saveStoreHits(db, run2, [{ keywordId: k, rank: 1, app: app({ title: 'A1 renamed', ratingsCount: 20 }) }]);
    expect(db.select().from(apps).all().map((a) => a.title)).toEqual(['A1 renamed']);
    expect(db.select().from(appSnapshots).all().map((s) => s.ratingsCount).sort()).toEqual([10, 20]);
  });
});
```

- [ ] **Step 4: Chạy để thấy fail**

Run: `npx vitest run tests/playstore.test.ts tests/store-apps.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 5: Ghi `web/src/collectors/store-apps.ts`**

```ts
import type { Db } from '@/db/client';
import { appSnapshots, apps, keywordHits } from '@/db/schema';
import type { StoreHit } from './types';

export function saveStoreHits(db: Db, runId: number, hits: StoreHit[]): void {
  db.transaction((tx) => {
    const idByKey = new Map<string, number>();
    for (const { keywordId, rank, app } of hits) {
      const key = `${app.store}:${app.storeAppId}`;
      let appId = idByKey.get(key);
      if (appId === undefined) {
        const details = {
          title: app.title, developer: app.developer, iconUrl: app.iconUrl, url: app.url,
          genre: app.genre, price: app.price, releasedAt: app.releasedAt,
        };
        appId = tx.insert(apps).values({ store: app.store, storeAppId: app.storeAppId, ...details })
          .onConflictDoUpdate({ target: [apps.store, apps.storeAppId], set: details })
          .returning({ id: apps.id }).get().id;
        idByKey.set(key, appId);
        tx.insert(appSnapshots).values({
          appId, runId, rating: app.rating, ratingsCount: app.ratingsCount,
          installsMin: app.installsMin, updatedAt: app.updatedAt,
        }).onConflictDoNothing().run();
      }
      tx.insert(keywordHits).values({ keywordId, appId, rank }).onConflictDoNothing().run();
    }
  });
}
```

- [ ] **Step 6: Ghi `web/src/collectors/playstore.ts`**

```ts
import gplay from 'google-play-scraper';
import { createLimiter } from '@/lib/rate-limit';
import { saveStoreHits } from './store-apps';
import type { Collector, StoreApp, StoreHit } from './types';

const limit = createLimiter(1000);
const PER_KEYWORD = 30;

function toIso(value: unknown): string | null {
  if (value === null || value === undefined || value === '') return null;
  const d = new Date(value as string | number);
  return Number.isNaN(d.getTime()) ? null : d.toISOString();
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function normalizePlayApp(raw: any): StoreApp {
  return {
    store: 'play',
    storeAppId: raw.appId,
    title: raw.title,
    developer: raw.developer ?? '',
    iconUrl: raw.icon ?? null,
    url: raw.url,
    genre: raw.genre ?? null,
    price: Number(raw.price ?? 0),
    releasedAt: toIso(raw.released),
    rating: raw.score ?? null,
    ratingsCount: raw.ratings ?? null,
    installsMin: raw.minInstalls ?? null,
    updatedAt: toIso(raw.updated),
  };
}

export async function suggestPlayKeywords(seed: string, country: string, max = 5): Promise<string[]> {
  const list: string[] = await limit(() => gplay.suggest({ term: seed, country: country.toLowerCase(), lang: 'en' }));
  const s = seed.trim().toLowerCase();
  return [...new Set(list.map((x) => x.trim().toLowerCase()))].filter((x) => x && x !== s).slice(0, max);
}

export const collectPlaystore: Collector = async ({ db, runId, keywords, country }) => {
  const gl = country.toLowerCase();
  const idsByKeyword = new Map<number, string[]>();
  for (const k of keywords) {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const found: any[] = await limit(() => gplay.search({ term: k.term, num: PER_KEYWORD, country: gl, lang: 'en' }));
    idsByKeyword.set(k.id, found.map((a) => a.appId));
  }

  // search() không trả số cài/số rating/ngày update → phải gọi app() cho từng app (không trùng).
  const details = new Map<string, StoreApp>();
  for (const appId of new Set([...idsByKeyword.values()].flat())) {
    try {
      details.set(appId, normalizePlayApp(await limit(() => gplay.app({ appId, country: gl, lang: 'en' }))));
    } catch {
      // app bị gỡ hoặc khoá vùng: bỏ qua, không làm hỏng cả nguồn
    }
  }

  const hits: StoreHit[] = [];
  for (const [keywordId, ids] of idsByKeyword) {
    ids.forEach((id, i) => {
      const app = details.get(id);
      if (app) hits.push({ keywordId, rank: i + 1, app });
    });
  }
  saveStoreHits(db, runId, hits);
};
```

- [ ] **Step 7: Chạy test**

Run: `npx vitest run tests/playstore.test.ts tests/store-apps.test.ts`
Expected: PASS 4 test. (Nếu TS báo không import được JSON, thêm `"resolveJsonModule": true` vào `tsconfig.json` — create-next-app thường đã bật.)

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(collector): Google Play + lưu app dùng chung cho 2 store"
```

---

### Task 6: App Store collector

**Files:**
- Create: `web/src/collectors/appstore.ts`
- Test: `web/tests/appstore.test.ts`, `web/tests/fixtures/appstore/search.json`

**Interfaces:**
- Consumes: `Collector`, `StoreApp`, `StoreHit`, `saveStoreHits` (Task 5); `createLimiter` (Task 3); `CollectorError` (Task 3)
- Produces: `normalizeItunesApp(raw: any): StoreApp`, `fetchItunes(term: string, country: string): Promise<any[]>`, `collectAppstore: Collector`

- [ ] **Step 1: Ghi fixture `web/tests/fixtures/appstore/search.json`**

```json
{
  "resultCount": 1,
  "results": [
    {
      "trackId": 1234567890,
      "trackName": "Streaks",
      "artistName": "Crunchy Bagel",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/icon100.png",
      "trackViewUrl": "https://apps.apple.com/us/app/streaks/id1234567890",
      "primaryGenreName": "Health & Fitness",
      "price": 5.99,
      "averageUserRating": 4.8,
      "userRatingCount": 41000,
      "releaseDate": "2015-12-03T08:00:00Z",
      "currentVersionReleaseDate": "2026-09-20T16:00:00Z"
    }
  ]
}
```

- [ ] **Step 2: Viết test fail** — `web/tests/appstore.test.ts`

```ts
import { afterEach, describe, expect, it, vi } from 'vitest';
import { fetchItunes, normalizeItunesApp } from '@/collectors/appstore';
import fixture from './fixtures/appstore/search.json';

afterEach(() => vi.unstubAllGlobals());

describe('normalizeItunesApp', () => {
  it('maps an iTunes result to a StoreApp without installs', () => {
    expect(normalizeItunesApp(fixture.results[0])).toEqual({
      store: 'appstore',
      storeAppId: '1234567890',
      title: 'Streaks',
      developer: 'Crunchy Bagel',
      iconUrl: 'https://is1-ssl.mzstatic.com/icon100.png',
      url: 'https://apps.apple.com/us/app/streaks/id1234567890',
      genre: 'Health & Fitness',
      price: 5.99,
      releasedAt: '2015-12-03T08:00:00Z',
      rating: 4.8,
      ratingsCount: 41000,
      installsMin: null,
      updatedAt: '2026-09-20T16:00:00Z',
    });
  });
});

describe('fetchItunes', () => {
  it('builds the search URL with lowercase country', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(fixture), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const rows = await fetchItunes('habit tracker', 'US');
    expect(rows).toHaveLength(1);
    const url = new URL(fetchMock.mock.calls[0][0]);
    expect(url.searchParams.get('term')).toBe('habit tracker');
    expect(url.searchParams.get('country')).toBe('us');
    expect(url.searchParams.get('entity')).toBe('software');
    expect(url.searchParams.get('limit')).toBe('30');
  });

  it('maps 403 to RATE_LIMITED', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response('', { status: 403 })));
    await expect(fetchItunes('x', 'US')).rejects.toMatchObject({ code: 'RATE_LIMITED' });
  });
});
```

- [ ] **Step 3: Chạy để thấy fail**

Run: `npx vitest run tests/appstore.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 4: Ghi `web/src/collectors/appstore.ts`**

```ts
import { CollectorError } from '@/lib/errors';
import { createLimiter } from '@/lib/rate-limit';
import { saveStoreHits } from './store-apps';
import type { Collector, StoreApp, StoreHit } from './types';

const limit = createLimiter(3000); // iTunes Search API ≈ 20 req/phút

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function normalizeItunesApp(r: any): StoreApp {
  return {
    store: 'appstore',
    storeAppId: String(r.trackId),
    title: r.trackName,
    developer: r.artistName ?? '',
    iconUrl: r.artworkUrl100 ?? null,
    url: r.trackViewUrl,
    genre: r.primaryGenreName ?? null,
    price: Number(r.price ?? 0),
    releasedAt: r.releaseDate ?? null,
    rating: r.averageUserRating ?? null,
    ratingsCount: r.userRatingCount ?? null,
    installsMin: null, // App Store không công khai số cài
    updatedAt: r.currentVersionReleaseDate ?? null,
  };
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export async function fetchItunes(term: string, country: string): Promise<any[]> {
  const params = new URLSearchParams({ term, country: country.toLowerCase(), entity: 'software', limit: '30' });
  const res = await fetch(`https://itunes.apple.com/search?${params}`);
  if (res.status === 403 || res.status === 429) throw new CollectorError('RATE_LIMITED', `iTunes ${res.status}`);
  if (!res.ok) throw new CollectorError('NETWORK', `iTunes ${res.status}`);
  const json = await res.json();
  return json.results ?? [];
}

export const collectAppstore: Collector = async ({ db, runId, keywords, country }) => {
  const hits: StoreHit[] = [];
  for (const k of keywords) {
    const rows = await limit(() => fetchItunes(k.term, country));
    rows.forEach((r, i) => hits.push({ keywordId: k.id, rank: i + 1, app: normalizeItunesApp(r) }));
  }
  saveStoreHits(db, runId, hits);
};
```

- [ ] **Step 5: Chạy test**

Run: `npx vitest run tests/appstore.test.ts`
Expected: PASS 3 test.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(collector): App Store qua iTunes Search API"
```

---

### Task 7: Google Trends collector

**Files:**
- Create: `web/src/collectors/trends.ts`
- Test: `web/tests/trends.test.ts`, `web/tests/fixtures/trends/interest.json`, `web/tests/fixtures/trends/related.json`

**Interfaces:**
- Consumes: `Collector` (Task 5); `CollectorError`, `toCollectorError`, `withRetry` (Task 3); bảng `trendPoints`, `trendRelated` (Task 2)
- Produces: `parseTrendsJson(text: string): any`, `normalizeInterest(json: any): { date: string; value: number }[]`, `normalizeRelated(json: any): { query: string; value: number; kind: 'top' | 'rising' }[]`, `collectTrends: Collector`

- [ ] **Step 1: Ghi fixture**

`web/tests/fixtures/trends/interest.json`

```json
{
  "default": {
    "timelineData": [
      { "time": "1730505600", "formattedTime": "Nov 2, 2024", "value": [62] },
      { "time": "1731110400", "formattedTime": "Nov 9, 2024", "value": [71] }
    ]
  }
}
```

`web/tests/fixtures/trends/related.json`

```json
{
  "default": {
    "rankedList": [
      { "rankedKeyword": [{ "query": "habit tracker app", "value": 100 }, { "query": "best habit tracker", "value": 40 }] },
      { "rankedKeyword": [{ "query": "habit tracker notion", "value": 250 }] }
    ]
  }
}
```

- [ ] **Step 2: Viết test fail** — `web/tests/trends.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { normalizeInterest, normalizeRelated, parseTrendsJson } from '@/collectors/trends';
import interest from './fixtures/trends/interest.json';
import related from './fixtures/trends/related.json';

describe('trends', () => {
  it('normalizes interest over time to daily dates', () => {
    expect(normalizeInterest(interest)).toEqual([
      { date: '2024-11-02', value: 62 },
      { date: '2024-11-09', value: 71 },
    ]);
  });

  it('normalizes related queries into top and rising', () => {
    expect(normalizeRelated(related)).toEqual([
      { query: 'habit tracker app', value: 100, kind: 'top' },
      { query: 'best habit tracker', value: 40, kind: 'top' },
      { query: 'habit tracker notion', value: 250, kind: 'rising' },
    ]);
  });

  it('treats an HTML response as RATE_LIMITED', () => {
    expect(() => parseTrendsJson('<!DOCTYPE html><html>429</html>')).toThrowError(
      expect.objectContaining({ code: 'RATE_LIMITED' }),
    );
  });

  it('treats broken JSON as PARSE', () => {
    expect(() => parseTrendsJson('{"default":')).toThrowError(expect.objectContaining({ code: 'PARSE' }));
  });
});
```

- [ ] **Step 3: Chạy để thấy fail**

Run: `npx vitest run tests/trends.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 4: Ghi `web/src/collectors/trends.ts`**

```ts
import googleTrends from 'google-trends-api';
import { trendPoints, trendRelated } from '@/db/schema';
import { CollectorError, toCollectorError } from '@/lib/errors';
import { withRetry } from '@/lib/rate-limit';
import type { Collector } from './types';

const RETRY_DELAYS = [2000, 5000, 10000];
const RELATED_LIMIT = 25;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function parseTrendsJson(text: string): any {
  // Google trả trang HTML (thường là 429) thay vì JSON khi chặn
  if (text.trimStart().startsWith('<')) throw new CollectorError('RATE_LIMITED', 'Google Trends trả về HTML (bị chặn tạm thời)');
  try {
    return JSON.parse(text);
  } catch (e) {
    throw new CollectorError('PARSE', `Google Trends JSON lỗi: ${(e as Error).message}`);
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function normalizeInterest(json: any): { date: string; value: number }[] {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  return (json.default?.timelineData ?? []).map((p: any) => ({
    date: new Date(Number(p.time) * 1000).toISOString().slice(0, 10),
    value: Number(p.value?.[0] ?? 0),
  }));
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function normalizeRelated(json: any): { query: string; value: number; kind: 'top' | 'rising' }[] {
  const [top, rising] = json.default?.rankedList ?? [];
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const pick = (list: any, kind: 'top' | 'rising') =>
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (list?.rankedKeyword ?? []).slice(0, RELATED_LIMIT).map((k: any) => ({ query: k.query, value: Number(k.value), kind }));
  return [...pick(top, 'top'), ...pick(rising, 'rising')];
}

function retryable(e: unknown): boolean {
  const code = toCollectorError(e).code;
  return code === 'RATE_LIMITED' || code === 'NETWORK';
}

const call = (fn: () => Promise<string>) => withRetry(async () => parseTrendsJson(await fn()), RETRY_DELAYS, retryable);

export const collectTrends: Collector = async ({ db, runId, seed, country }) => {
  const opts = { keyword: seed, geo: country.toUpperCase(), startTime: new Date(Date.now() - 365 * 86_400_000) };
  const interest = normalizeInterest(await call(() => googleTrends.interestOverTime(opts)));
  const related = normalizeRelated(await call(() => googleTrends.relatedQueries(opts)));
  db.transaction((tx) => {
    if (interest.length) tx.insert(trendPoints).values(interest.map((p) => ({ runId, ...p }))).onConflictDoNothing().run();
    if (related.length) tx.insert(trendRelated).values(related.map((r) => ({ runId, ...r }))).run();
  });
};
```

- [ ] **Step 5: Chạy test**

Run: `npx vitest run tests/trends.test.ts`
Expected: PASS 4 test.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(collector): Google Trends có retry và nhận diện bị chặn"
```

---

### Task 8: Reddit collector

**Files:**
- Create: `web/src/collectors/reddit.ts`, `.env.example`
- Test: `web/tests/reddit.test.ts`, `web/tests/fixtures/reddit/search.json`

**Interfaces:**
- Consumes: `Collector` (Task 5); `CollectorError` (Task 3); `createLimiter` (Task 3); bảng `redditPosts` (Task 2)
- Produces:
  - `isAppRequest(title: string, body: string): boolean`
  - `type RedditPostRow = { postId; subreddit; title; url; score; numComments; createdAt; isAppRequest }`
  - `normalizeRedditListing(json: any): RedditPostRow[]`
  - `mergeKeywordPosts(perKeyword: { keywordId: number; posts: RedditPostRow[] }[]): (RedditPostRow & { keywordId: number })[]`
  - `readRedditEnv(env?: NodeJS.ProcessEnv): { clientId: string; clientSecret: string; userAgent: string }`
  - `collectReddit: Collector`

- [ ] **Step 1: Ghi fixture `web/tests/fixtures/reddit/search.json`**

```json
{
  "data": {
    "children": [
      {
        "data": {
          "id": "abc123",
          "subreddit": "productivity",
          "title": "Is there an app that tracks habits without a subscription?",
          "selftext": "",
          "permalink": "/r/productivity/comments/abc123/is_there_an_app/",
          "score": 154,
          "num_comments": 87,
          "created_utc": 1759276800
        }
      },
      {
        "data": {
          "id": "def456",
          "subreddit": "getdisciplined",
          "title": "My 90 day habit streak",
          "selftext": "Sharing my progress",
          "permalink": "/r/getdisciplined/comments/def456/my_90_day/",
          "score": 30,
          "num_comments": 4,
          "created_utc": 1756684800
        }
      }
    ]
  }
}
```

- [ ] **Step 2: Viết test fail** — `web/tests/reddit.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { isAppRequest, mergeKeywordPosts, normalizeRedditListing, readRedditEnv } from '@/collectors/reddit';
import listing from './fixtures/reddit/search.json';

describe('reddit', () => {
  it('detects app-request posts', () => {
    expect(isAppRequest('Is there an app for this?', '')).toBe(true);
    expect(isAppRequest('Need help', 'any ALTERNATIVE TO Habitica?')).toBe(true);
    expect(isAppRequest('My streak', 'day 90')).toBe(false);
  });

  it('normalizes a search listing', () => {
    const rows = normalizeRedditListing(listing);
    expect(rows[0]).toEqual({
      postId: 'abc123',
      subreddit: 'productivity',
      title: 'Is there an app that tracks habits without a subscription?',
      url: 'https://www.reddit.com/r/productivity/comments/abc123/is_there_an_app/',
      score: 154,
      numComments: 87,
      createdAt: '2025-10-01T00:00:00.000Z',
      isAppRequest: true,
    });
    expect(rows[1].isAppRequest).toBe(false);
  });

  it('keeps a post once, under the first keyword that found it', () => {
    const rows = normalizeRedditListing(listing);
    const merged = mergeKeywordPosts([
      { keywordId: 1, posts: [rows[0]] },
      { keywordId: 2, posts: [rows[0], rows[1]] },
    ]);
    expect(merged.map((p) => [p.postId, p.keywordId])).toEqual([['abc123', 1], ['def456', 2]]);
  });

  it('throws MISSING_KEYS when env is incomplete', () => {
    expect(() => readRedditEnv({ REDDIT_CLIENT_ID: 'x' })).toThrowError(expect.objectContaining({ code: 'MISSING_KEYS' }));
    expect(readRedditEnv({ REDDIT_CLIENT_ID: 'i', REDDIT_CLIENT_SECRET: 's', REDDIT_USER_AGENT: 'ua' }))
      .toEqual({ clientId: 'i', clientSecret: 's', userAgent: 'ua' });
  });
});
```

- [ ] **Step 3: Chạy để thấy fail**

Run: `npx vitest run tests/reddit.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 4: Ghi `web/src/collectors/reddit.ts`**

```ts
import { redditPosts } from '@/db/schema';
import { CollectorError } from '@/lib/errors';
import { createLimiter } from '@/lib/rate-limit';
import type { Collector } from './types';

const limit = createLimiter(1000);

const APP_REQUEST_PATTERNS = [/is there an app/i, /looking for an app/i, /app that/i, /alternative to/i, /recommend an app/i];

export function isAppRequest(title: string, body: string): boolean {
  const text = `${title}\n${body}`;
  return APP_REQUEST_PATTERNS.some((re) => re.test(text));
}

export type RedditPostRow = {
  postId: string;
  subreddit: string;
  title: string;
  url: string;
  score: number;
  numComments: number;
  createdAt: string;
  isAppRequest: boolean;
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function normalizeRedditListing(json: any): RedditPostRow[] {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  return (json.data?.children ?? []).map((c: any) => c.data).map((d: any) => ({
    postId: d.id,
    subreddit: d.subreddit,
    title: d.title,
    url: `https://www.reddit.com${d.permalink}`,
    score: d.score ?? 0,
    numComments: d.num_comments ?? 0,
    createdAt: new Date(d.created_utc * 1000).toISOString(),
    isAppRequest: isAppRequest(d.title ?? '', d.selftext ?? ''),
  }));
}

export function mergeKeywordPosts(perKeyword: { keywordId: number; posts: RedditPostRow[] }[]) {
  const seen = new Set<string>();
  const out: (RedditPostRow & { keywordId: number })[] = [];
  for (const { keywordId, posts } of perKeyword) {
    for (const p of posts) {
      if (seen.has(p.postId)) continue;
      seen.add(p.postId);
      out.push({ ...p, keywordId });
    }
  }
  return out;
}

export function readRedditEnv(env: NodeJS.ProcessEnv = process.env) {
  const clientId = env.REDDIT_CLIENT_ID;
  const clientSecret = env.REDDIT_CLIENT_SECRET;
  const userAgent = env.REDDIT_USER_AGENT;
  if (!clientId || !clientSecret || !userAgent) {
    throw new CollectorError('MISSING_KEYS', 'Thiếu REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET / REDDIT_USER_AGENT trong .env.local');
  }
  return { clientId, clientSecret, userAgent };
}

async function getToken(cfg: ReturnType<typeof readRedditEnv>): Promise<string> {
  const res = await fetch('https://www.reddit.com/api/v1/access_token', {
    method: 'POST',
    headers: {
      Authorization: `Basic ${Buffer.from(`${cfg.clientId}:${cfg.clientSecret}`).toString('base64')}`,
      'User-Agent': cfg.userAgent,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'grant_type=client_credentials',
  });
  if (res.status === 401) throw new CollectorError('MISSING_KEYS', 'Reddit từ chối key (401) — kiểm tra lại .env.local');
  if (!res.ok) throw new CollectorError('NETWORK', `Reddit token ${res.status}`);
  return (await res.json()).access_token;
}

async function searchReddit(token: string, userAgent: string, term: string): Promise<RedditPostRow[]> {
  const params = new URLSearchParams({ q: `"${term}"`, t: 'year', sort: 'relevance', limit: '100', type: 'link' });
  const res = await fetch(`https://oauth.reddit.com/search?${params}`, {
    headers: { Authorization: `Bearer ${token}`, 'User-Agent': userAgent },
  });
  if (res.status === 429) throw new CollectorError('RATE_LIMITED', 'Reddit 429');
  if (!res.ok) throw new CollectorError('NETWORK', `Reddit search ${res.status}`);
  return normalizeRedditListing(await res.json());
}

export const collectReddit: Collector = async ({ db, runId, keywords }) => {
  const cfg = readRedditEnv();
  const token = await limit(() => getToken(cfg));
  const perKeyword = [];
  for (const k of keywords) {
    perKeyword.push({ keywordId: k.id, posts: await limit(() => searchReddit(token, cfg.userAgent, k.term)) });
  }
  const rows = mergeKeywordPosts(perKeyword);
  db.transaction((tx) => {
    if (rows.length) tx.insert(redditPosts).values(rows.map((r) => ({ runId, ...r }))).run();
  });
};
```

- [ ] **Step 5: Ghi `.env.example`**

```
# Tạo app loại "script" tại https://www.reddit.com/prefs/apps, chép sang .env.local
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=niche-radar/0.1 by <reddit-username>
```

- [ ] **Step 6: Chạy test**

Run: `npx vitest run tests/reddit.test.ts`
Expected: PASS 4 test.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat(collector): Reddit OAuth, đánh dấu bài xin app"
```

---

### Task 9: Orchestrator — run, keyword, cache, retry

**Files:**
- Create: `web/src/lib/run-research.ts`
- Test: `web/tests/run-research.test.ts`

**Interfaces:**
- Consumes: `Db` + bảng (Task 2); `toCollectorError` (Task 3); `Collector` (Task 5); `saveStoreHits` (Task 5, chỉ trong test)
- Produces:
  - `type ResearchDeps = { db: Db; collectors: Record<Source, Collector>; suggest: (seed: string, country: string) => Promise<string[]>; now?: () => Date }`
  - `normalizeSeed(seed: string): string`
  - `startResearch(deps, seed: string, country: string, opts?: { force?: boolean }): { runId: number; done: Promise<void> }`
  - `retrySource(deps, runId: number, source: Source): Promise<void>`

- [ ] **Step 1: Viết test fail** — `web/tests/run-research.test.ts`

```ts
import { eq } from 'drizzle-orm';
import { describe, expect, it, vi } from 'vitest';
import { saveStoreHits } from '@/collectors/store-apps';
import type { Collector, StoreApp } from '@/collectors/types';
import { createDb } from '@/db/client';
import { keywordHits, keywords, sourceJobs, type Source } from '@/db/schema';
import { CollectorError } from '@/lib/errors';
import { type ResearchDeps, retrySource, startResearch } from '@/lib/run-research';

const app: StoreApp = {
  store: 'play', storeAppId: 'a1', title: 'A1', developer: 'D', iconUrl: null, url: 'u', genre: null,
  price: 0, releasedAt: null, rating: 4, ratingsCount: 5, installsMin: 100, updatedAt: null,
};

function makeDeps(over: Partial<Record<Source, Collector>> = {}): ResearchDeps & { calls: Record<Source, number> } {
  const calls = { playstore: 0, appstore: 0, trends: 0, reddit: 0 };
  const wrap = (s: Source, fn: Collector): Collector => async (ctx) => { calls[s]++; await fn(ctx); };
  const noop: Collector = async () => {};
  const play: Collector = async ({ db, runId, keywords: ks }) =>
    saveStoreHits(db, runId, [{ keywordId: ks[0].id, rank: 1, app }]);
  return {
    db: createDb(':memory:'),
    suggest: async () => ['habit tracker app', 'Habit Tracker'],
    collectors: {
      playstore: wrap('playstore', over.playstore ?? play),
      appstore: wrap('appstore', over.appstore ?? noop),
      trends: wrap('trends', over.trends ?? noop),
      reddit: wrap('reddit', over.reddit ?? noop),
    },
    calls,
  };
}

const jobsOf = (deps: ResearchDeps, runId: number) =>
  Object.fromEntries(deps.db.select().from(sourceJobs).where(eq(sourceJobs.runId, runId)).all().map((j) => [j.source, j]));

describe('startResearch', () => {
  it('creates keywords from seed + suggestions and finishes all jobs', async () => {
    const deps = makeDeps();
    const { runId, done } = startResearch(deps, '  Habit Tracker ', 'US');
    await done;
    const ks = deps.db.select().from(keywords).where(eq(keywords.runId, runId)).all();
    expect(ks.map((k) => [k.term, k.origin])).toEqual([['habit tracker', 'seed'], ['habit tracker app', 'play_suggest']]);
    expect(Object.values(jobsOf(deps, runId)).map((j) => j.status)).toEqual(['done', 'done', 'done', 'done']);
  });

  it('falls back to the seed only when suggest fails', async () => {
    const deps = makeDeps();
    deps.suggest = async () => { throw new Error('boom'); };
    const { runId, done } = startResearch(deps, 'habit tracker', 'US');
    await done;
    expect(deps.db.select().from(keywords).where(eq(keywords.runId, runId)).all()).toHaveLength(1);
  });

  it('isolates a failing source', async () => {
    const deps = makeDeps({ trends: async () => { throw new CollectorError('RATE_LIMITED', '429'); } });
    const { runId, done } = startResearch(deps, 'habit tracker', 'US');
    await done;
    const jobs = jobsOf(deps, runId);
    expect(jobs.trends.status).toBe('error');
    expect(jobs.trends.errorCode).toBe('RATE_LIMITED');
    expect(jobs.playstore.status).toBe('done');
  });

  it('copies cached data within 24h instead of calling the collector', async () => {
    const deps = makeDeps();
    await startResearch(deps, 'habit tracker', 'US').done;
    const second = startResearch(deps, 'habit tracker', 'US');
    await second.done;
    expect(deps.calls.playstore).toBe(1);
    const hits = deps.db.select().from(keywordHits)
      .innerJoin(keywords, eq(keywords.id, keywordHits.keywordId))
      .where(eq(keywords.runId, second.runId)).all();
    expect(hits).toHaveLength(1);
  });

  it('does not reuse a failed source from the cache', async () => {
    let fail = true;
    const deps = makeDeps({ trends: async () => { if (fail) throw new Error('x'); } });
    await startResearch(deps, 'habit tracker', 'US').done;
    fail = false;
    const { runId, done } = startResearch(deps, 'habit tracker', 'US');
    await done;
    expect(deps.calls.trends).toBe(2);
    expect(jobsOf(deps, runId).trends.status).toBe('done');
  });

  it('skips the cache with force', async () => {
    const deps = makeDeps();
    await startResearch(deps, 'habit tracker', 'US').done;
    await startResearch(deps, 'habit tracker', 'US', { force: true }).done;
    expect(deps.calls.playstore).toBe(2);
  });

  it('does not use a cache older than 24h', async () => {
    const deps = makeDeps();
    deps.now = () => new Date('2026-10-20T00:00:00Z');
    await startResearch(deps, 'habit tracker', 'US').done;
    deps.now = () => new Date('2026-10-22T00:00:00Z');
    await startResearch(deps, 'habit tracker', 'US').done;
    expect(deps.calls.playstore).toBe(2);
  });
});

describe('retrySource', () => {
  it('reruns one failed source', async () => {
    const reddit = vi.fn<Collector>().mockRejectedValueOnce(new CollectorError('NETWORK', 'down')).mockResolvedValue();
    const deps = makeDeps({ reddit });
    const { runId, done } = startResearch(deps, 'habit tracker', 'US');
    await done;
    expect(jobsOf(deps, runId).reddit.status).toBe('error');
    await retrySource(deps, runId, 'reddit');
    expect(jobsOf(deps, runId).reddit.status).toBe('done');
    expect(jobsOf(deps, runId).reddit.errorCode).toBeNull();
  });
});
```

- [ ] **Step 2: Chạy để thấy fail**

Run: `npx vitest run tests/run-research.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Ghi `web/src/lib/run-research.ts`**

```ts
import { and, desc, eq, gte, ne, sql } from 'drizzle-orm';
import type { Collector } from '@/collectors/types';
import type { Db } from '@/db/client';
import { keywords, runs, SOURCES, type Source, sourceJobs } from '@/db/schema';
import { toCollectorError } from '@/lib/errors';

export const CACHE_MS = 24 * 3600 * 1000;

export type ResearchDeps = {
  db: Db;
  collectors: Record<Source, Collector>;
  suggest: (seed: string, country: string) => Promise<string[]>;
  now?: () => Date;
};

type Kw = { id: number; term: string };

export const normalizeSeed = (seed: string) => seed.trim().toLowerCase();
const nowOf = (deps: ResearchDeps) => (deps.now ?? (() => new Date()))();
const storeOf = (source: Source) => (source === 'playstore' ? 'play' : 'appstore');

function setJob(db: Db, runId: number, source: Source, patch: Partial<typeof sourceJobs.$inferInsert>) {
  db.update(sourceJobs).set(patch).where(and(eq(sourceJobs.runId, runId), eq(sourceJobs.source, source))).run();
}

function findCacheRun(deps: ResearchDeps, seed: string, country: string, excludeRunId: number): number | undefined {
  const since = new Date(nowOf(deps).getTime() - CACHE_MS).toISOString();
  return deps.db.select({ id: runs.id }).from(runs)
    .where(and(eq(runs.seed, seed), eq(runs.country, country), gte(runs.createdAt, since), ne(runs.id, excludeRunId)))
    .orderBy(desc(runs.id)).limit(1).get()?.id;
}

function insertKeywords(db: Db, runId: number, rows: { term: string; origin: 'seed' | 'play_suggest' }[]): Kw[] {
  return db.insert(keywords).values(rows.map((r) => ({ runId, ...r })))
    .returning({ id: keywords.id, term: keywords.term }).all();
}

async function prepareKeywords(deps: ResearchDeps, runId: number, seed: string, country: string, cacheRunId?: number) {
  if (cacheRunId !== undefined) {
    const old = deps.db.select().from(keywords).where(eq(keywords.runId, cacheRunId)).orderBy(keywords.id).all();
    return insertKeywords(deps.db, runId, old.map((k) => ({ term: k.term, origin: k.origin })));
  }
  let suggestions: string[] = [];
  try {
    suggestions = await deps.suggest(seed, country);
  } catch {
    // autocomplete lỗi: vẫn chạy với seed
  }
  const terms = [...new Set(suggestions.map(normalizeSeed))].filter((t) => t && t !== seed).slice(0, 5);
  return insertKeywords(deps.db, runId, [
    { term: seed, origin: 'seed' },
    ...terms.map((term) => ({ term, origin: 'play_suggest' as const })),
  ]);
}

function clearSourceData(db: Db, runId: number, source: Source) {
  if (source === 'playstore' || source === 'appstore') {
    const store = storeOf(source);
    db.run(sql`DELETE FROM keyword_hits WHERE keyword_id IN (SELECT id FROM keywords WHERE run_id = ${runId})
      AND app_id IN (SELECT id FROM apps WHERE store = ${store})`);
    db.run(sql`DELETE FROM app_snapshots WHERE run_id = ${runId} AND app_id IN (SELECT id FROM apps WHERE store = ${store})`);
  } else if (source === 'trends') {
    db.run(sql`DELETE FROM trend_points WHERE run_id = ${runId}`);
    db.run(sql`DELETE FROM trend_related WHERE run_id = ${runId}`);
  } else {
    db.run(sql`DELETE FROM reddit_posts WHERE run_id = ${runId}`);
  }
}

/** Chép dữ liệu một nguồn từ run cũ sang run mới; keyword ghép theo term. */
function copySourceData(db: Db, from: number, to: number, source: Source) {
  db.transaction((tx) => {
    if (source === 'playstore' || source === 'appstore') {
      const store = storeOf(source);
      tx.run(sql`INSERT INTO keyword_hits (keyword_id, app_id, rank)
        SELECT kn.id, h.app_id, h.rank FROM keyword_hits h
        JOIN keywords ko ON ko.id = h.keyword_id AND ko.run_id = ${from}
        JOIN keywords kn ON kn.term = ko.term AND kn.run_id = ${to}
        JOIN apps a ON a.id = h.app_id AND a.store = ${store}`);
      tx.run(sql`INSERT INTO app_snapshots (app_id, run_id, rating, ratings_count, installs_min, updated_at)
        SELECT s.app_id, ${to}, s.rating, s.ratings_count, s.installs_min, s.updated_at FROM app_snapshots s
        JOIN apps a ON a.id = s.app_id AND a.store = ${store} WHERE s.run_id = ${from}`);
    } else if (source === 'trends') {
      tx.run(sql`INSERT INTO trend_points (run_id, date, value) SELECT ${to}, date, value FROM trend_points WHERE run_id = ${from}`);
      tx.run(sql`INSERT INTO trend_related (run_id, query, value, kind) SELECT ${to}, query, value, kind FROM trend_related WHERE run_id = ${from}`);
    } else {
      tx.run(sql`INSERT INTO reddit_posts (run_id, keyword_id, post_id, subreddit, title, url, score, num_comments, created_at, is_app_request)
        SELECT ${to}, kn.id, p.post_id, p.subreddit, p.title, p.url, p.score, p.num_comments, p.created_at, p.is_app_request
        FROM reddit_posts p
        JOIN keywords ko ON ko.id = p.keyword_id
        JOIN keywords kn ON kn.term = ko.term AND kn.run_id = ${to}
        WHERE p.run_id = ${from}`);
    }
  });
}

async function runSource(deps: ResearchDeps, runId: number, source: Source, kws: Kw[], cacheRunId?: number) {
  const { db } = deps;
  setJob(db, runId, source, { status: 'running', startedAt: nowOf(deps).toISOString(), errorCode: null, errorMessage: null });
  if (cacheRunId !== undefined) {
    const cached = db.select().from(sourceJobs)
      .where(and(eq(sourceJobs.runId, cacheRunId), eq(sourceJobs.source, source))).get();
    if (cached?.status === 'done') {
      copySourceData(db, cacheRunId, runId, source);
      setJob(db, runId, source, { status: 'done', finishedAt: nowOf(deps).toISOString() });
      return;
    }
  }
  const run = db.select().from(runs).where(eq(runs.id, runId)).get()!;
  try {
    await deps.collectors[source]({ db, runId, seed: run.seed, country: run.country, keywords: kws });
    setJob(db, runId, source, { status: 'done', finishedAt: nowOf(deps).toISOString() });
  } catch (e) {
    const err = toCollectorError(e);
    clearSourceData(db, runId, source);
    setJob(db, runId, source, {
      status: 'error', errorCode: err.code, errorMessage: err.message, finishedAt: nowOf(deps).toISOString(),
    });
  }
}

export function startResearch(deps: ResearchDeps, rawSeed: string, rawCountry: string, opts: { force?: boolean } = {}) {
  const { db } = deps;
  const seed = normalizeSeed(rawSeed);
  const country = rawCountry.toUpperCase();
  const runId = db.insert(runs).values({ seed, country, createdAt: nowOf(deps).toISOString() })
    .returning({ id: runs.id }).get().id;
  db.insert(sourceJobs).values(SOURCES.map((source) => ({ runId, source, status: 'pending' as const }))).run();

  const done = (async () => {
    try {
      const cacheRunId = opts.force ? undefined : findCacheRun(deps, seed, country, runId);
      const kws = await prepareKeywords(deps, runId, seed, country, cacheRunId);
      await Promise.allSettled(SOURCES.map((s) => runSource(deps, runId, s, kws, cacheRunId)));
    } catch (e) {
      // lỗi ngoài collector (DB...): không để job treo ở pending
      const err = toCollectorError(e);
      db.update(sourceJobs).set({ status: 'error', errorCode: err.code, errorMessage: err.message })
        .where(and(eq(sourceJobs.runId, runId), eq(sourceJobs.status, 'pending'))).run();
    }
  })();
  return { runId, done };
}

export async function retrySource(deps: ResearchDeps, runId: number, source: Source): Promise<void> {
  // Hai lệnh đồng bộ đầu tiên chạy trước khi hàm trả Promise → API trả về thì job đã là pending.
  clearSourceData(deps.db, runId, source);
  setJob(deps.db, runId, source, { status: 'pending', errorCode: null, errorMessage: null, finishedAt: null });
  const kws = deps.db.select({ id: keywords.id, term: keywords.term }).from(keywords)
    .where(eq(keywords.runId, runId)).orderBy(keywords.id).all();
  await runSource(deps, runId, source, kws);
}
```

- [ ] **Step 4: Chạy test**

Run: `npx vitest run tests/run-research.test.ts`
Expected: PASS 8 test.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(lib): orchestrator chạy 4 nguồn song song, cache 24h, thử lại từng nguồn"
```

---

### Task 10: run-view + API routes

**Files:**
- Create: `web/src/lib/run-view.ts`, `web/src/lib/countries.ts`, `web/src/lib/deps.ts`, `src/app/api/research/route.ts`, `src/app/api/research/[id]/route.ts`, `src/app/api/research/[id]/retry/route.ts`
- Test: `web/tests/run-view.test.ts`

**Interfaces:**
- Consumes: bảng (Task 2); hàm stats (Task 4); collectors (Task 5–8); `startResearch`, `retrySource`, `ResearchDeps` (Task 9)
- Produces (UI ở Task 11–14 dùng):
  - `COUNTRIES: { code: string; label: string }[]`, `isCountry(code: string): boolean`
  - `defaultDeps(): ResearchDeps`
  - kiểu `JobView`, `AppBrief`, `KeywordRow`, `CompetitorRow`, `Bucket`, `RunStats`, `RedditPostView`, `RunView`, `RunSummary`
  - `getRunView(db: Db, runId: number, now?: Date): RunView | null`
  - `listRuns(db: Db, limit: number): RunSummary[]`
  - `POST /api/research {seed, country, force?}` → `{ runId }` · `GET /api/research` → `RunSummary[]` · `GET /api/research/[id]` → `RunView` · `POST /api/research/[id]/retry {source}` → `{ ok: true }`

- [ ] **Step 1: Viết test fail** — `web/tests/run-view.test.ts`

```ts
import { describe, expect, it } from 'vitest';
import { saveStoreHits } from '@/collectors/store-apps';
import type { StoreApp } from '@/collectors/types';
import { createDb } from '@/db/client';
import { keywords, redditPosts, runs, sourceJobs, SOURCES, trendPoints, trendRelated } from '@/db/schema';
import { getRunView, listRuns } from '@/lib/run-view';

const NOW = new Date('2026-10-23T00:00:00Z');
const base: StoreApp = {
  store: 'play', storeAppId: 'p1', title: 'P1', developer: 'D', iconUrl: null, url: 'u', genre: null, price: 0,
  releasedAt: '2020-01-01T00:00:00Z', rating: 4, ratingsCount: 100, installsMin: 50_000, updatedAt: '2026-10-01T00:00:00Z',
};

function setup() {
  const db = createDb(':memory:');
  const runId = db.insert(runs).values({ seed: 'habit tracker', country: 'US', createdAt: NOW.toISOString() })
    .returning({ id: runs.id }).get().id;
  db.insert(sourceJobs).values(SOURCES.map((source) => ({ runId, source, status: 'done' as const }))).run();
  const [seed, sug] = db.insert(keywords).values([
    { runId, term: 'habit tracker', origin: 'seed' }, { runId, term: 'habit app', origin: 'play_suggest' },
  ]).returning({ id: keywords.id }).all();
  saveStoreHits(db, runId, [
    { keywordId: seed.id, rank: 1, app: base },
    { keywordId: seed.id, rank: 2, app: { ...base, storeAppId: 'p2', title: 'P2', rating: 3, ratingsCount: 10, installsMin: 500, updatedAt: '2024-01-01T00:00:00Z', releasedAt: '2025-05-01T00:00:00Z' } },
    { keywordId: sug.id, rank: 1, app: base },
    { keywordId: seed.id, rank: 1, app: { ...base, store: 'appstore', storeAppId: 'i1', title: 'I1', rating: 5, ratingsCount: 1000, installsMin: null } },
  ]);
  db.insert(trendPoints).values([{ runId, date: '2026-01-01', value: 40 }, { runId, date: '2026-01-08', value: 60 }]).run();
  db.insert(trendRelated).values([{ runId, query: 'habit app', value: 100, kind: 'top' }, { runId, query: 'habit ai', value: 300, kind: 'rising' }]).run();
  db.insert(redditPosts).values([
    { runId, keywordId: seed.id, postId: 'r1', subreddit: 'productivity', title: 't', url: 'u', score: 5, numComments: 1, createdAt: '2026-10-01T00:00:00Z', isAppRequest: false },
    { runId, keywordId: seed.id, postId: 'r2', subreddit: 'productivity', title: 't2', url: 'u', score: 1, numComments: 0, createdAt: '2026-09-01T00:00:00Z', isAppRequest: true },
  ]).run();
  return { db, runId };
}

describe('getRunView', () => {
  it('returns null for an unknown run', () => {
    expect(getRunView(createDb(':memory:'), 99, NOW)).toBeNull();
  });

  it('computes seed stats', () => {
    const { db, runId } = setup();
    const { stats } = getRunView(db, runId, NOW)!;
    expect(stats).toEqual({
      playCount: 2,
      appstoreCount: 1,
      maxInstalls: 50_000,
      medianRating: 4,
      topRatingsSum: { play: 110, appstore: 1000 },
      newestRelease: '2025-05-01T00:00:00Z',
      staleSharePct: 33,
      redditPosts: 2,
      redditAppRequests: 1,
      trendsAvg: 50,
    });
  });

  it('builds keyword rows with the top app per store', () => {
    const { db, runId } = setup();
    const rows = getRunView(db, runId, NOW)!.keywords;
    expect(rows.map((r) => [r.term, r.playCount, r.appstoreCount])).toEqual([['habit tracker', 2, 1], ['habit app', 1, 0]]);
    expect(rows[0].topPlay?.title).toBe('P1');
    expect(rows[1].topAppstore).toBeNull();
  });

  it('dedupes competitors and counts keywords', () => {
    const { db, runId } = setup();
    const view = getRunView(db, runId, NOW)!;
    expect(view.competitors).toHaveLength(3);
    expect(view.competitors.find((c) => c.title === 'P1')!.keywordCount).toBe(2);
    expect(view.charts.installs.find((b) => b.key === '10K–100K')!.count).toBe(1);
    expect(view.charts.updateAge.find((b) => b.key === '>2 năm')!.count).toBe(1); // P2 update 2024-01-01
  });

  it('prepares trends and reddit blocks', () => {
    const { db, runId } = setup();
    const view = getRunView(db, runId, NOW)!;
    expect(view.trends.rising).toEqual([{ query: 'habit ai', value: 300 }]);
    expect(view.reddit.byMonth).toHaveLength(12);
    expect(view.reddit.byMonth.at(-1)).toEqual({ key: '2026-10', count: 1 });
    expect(view.reddit.posts[0].postId).toBe('r2'); // bài xin app lên đầu
  });
});

describe('listRuns', () => {
  it('lists recent runs with job statuses', () => {
    const { db } = setup();
    const [r] = listRuns(db, 10);
    expect(r.seed).toBe('habit tracker');
    expect(r.jobs.map((j) => j.status)).toEqual(['done', 'done', 'done', 'done']);
  });
});
```

Con số kiểm tay: seed có P1 (play), P2 (play), I1 (appstore) → median rating của [4, 3, 5] = 4; top rating Play = 100 + 10 = 110; app có `updatedAt` > 365 ngày: chỉ P2 → 1/3 = 33%.

- [ ] **Step 2: Chạy để thấy fail**

Run: `npx vitest run tests/run-view.test.ts`
Expected: FAIL, không tìm thấy module.

- [ ] **Step 3: Ghi `web/src/lib/countries.ts`**

```ts
export const COUNTRIES = [
  { code: 'US', label: 'United States' },
  { code: 'GB', label: 'United Kingdom' },
  { code: 'VN', label: 'Việt Nam' },
  { code: 'DE', label: 'Germany' },
  { code: 'JP', label: 'Japan' },
];

export const isCountry = (code: string) => COUNTRIES.some((c) => c.code === code);
```

- [ ] **Step 4: Ghi `web/src/lib/run-view.ts`**

```ts
import { and, desc, eq, inArray } from 'drizzle-orm';
import type { Db } from '@/db/client';
import {
  appSnapshots, apps, type JobStatus, keywordHits, keywords, redditPosts, runs, SOURCES, type Source,
  sourceJobs, type Store, trendPoints, trendRelated,
} from '@/db/schema';
import { AGE_BUCKETS, INSTALL_BUCKETS, ageBucket, countBy, daysSince, installBucket, lastMonths, median, monthKey } from '@/lib/stats';

export type JobView = { source: Source; status: JobStatus; errorCode: string | null; errorMessage: string | null };
export type AppBrief = { title: string; url: string; ratingsCount: number | null; installsMin: number | null };
export type KeywordRow = {
  id: number; term: string; origin: 'seed' | 'play_suggest';
  playCount: number; appstoreCount: number; topPlay: AppBrief | null; topAppstore: AppBrief | null;
};
export type CompetitorRow = {
  appId: number; store: Store; title: string; developer: string; iconUrl: string | null; url: string; price: number;
  rating: number | null; ratingsCount: number | null; installsMin: number | null;
  updatedAt: string | null; releasedAt: string | null; keywordCount: number; bestRank: number;
};
export type Bucket = { key: string; count: number };
export type RunStats = {
  playCount: number; appstoreCount: number; maxInstalls: number | null; medianRating: number | null;
  topRatingsSum: { play: number; appstore: number }; newestRelease: string | null; staleSharePct: number | null;
  redditPosts: number; redditAppRequests: number; trendsAvg: number | null;
};
export type RedditPostView = {
  postId: string; subreddit: string; title: string; url: string; score: number; numComments: number;
  createdAt: string; isAppRequest: boolean; keyword: string;
};
export type RunView = {
  run: { id: number; seed: string; country: string; createdAt: string };
  jobs: JobView[];
  stats: RunStats;
  keywords: KeywordRow[];
  competitors: CompetitorRow[];
  charts: { installs: Bucket[]; updateAge: Bucket[] };
  trends: { points: { date: string; value: number }[]; top: { query: string; value: number }[]; rising: { query: string; value: number }[] };
  reddit: { posts: RedditPostView[]; byMonth: Bucket[]; bySubreddit: Bucket[] };
};
export type RunSummary = { id: number; seed: string; country: string; createdAt: string; jobs: { source: Source; status: JobStatus }[] };

type Hit = Omit<CompetitorRow, 'keywordCount' | 'bestRank'> & { keywordId: number; rank: number };

const brief = (h: Hit | undefined): AppBrief | null =>
  h ? { title: h.title, url: h.url, ratingsCount: h.ratingsCount, installsMin: h.installsMin } : null;
const byRank = (a: Hit, b: Hit) => a.rank - b.rank;

function jobViews(rows: (typeof sourceJobs.$inferSelect)[], runId: number): JobView[] {
  return SOURCES.map((source) => {
    const j = rows.find((r) => r.runId === runId && r.source === source);
    return { source, status: j?.status ?? 'pending', errorCode: j?.errorCode ?? null, errorMessage: j?.errorMessage ?? null };
  });
}

export function getRunView(db: Db, runId: number, now = new Date()): RunView | null {
  const run = db.select().from(runs).where(eq(runs.id, runId)).get();
  if (!run) return null;

  const jobs = jobViews(db.select().from(sourceJobs).where(eq(sourceJobs.runId, runId)).all(), runId);
  const kws = db.select().from(keywords).where(eq(keywords.runId, runId)).orderBy(keywords.id).all();
  const seedKw = kws.find((k) => k.origin === 'seed');

  const hits: Hit[] = db
    .select({
      keywordId: keywordHits.keywordId, rank: keywordHits.rank, appId: apps.id, store: apps.store, title: apps.title,
      developer: apps.developer, iconUrl: apps.iconUrl, url: apps.url, price: apps.price, releasedAt: apps.releasedAt,
      rating: appSnapshots.rating, ratingsCount: appSnapshots.ratingsCount, installsMin: appSnapshots.installsMin,
      updatedAt: appSnapshots.updatedAt,
    })
    .from(keywordHits)
    .innerJoin(keywords, eq(keywords.id, keywordHits.keywordId))
    .innerJoin(apps, eq(apps.id, keywordHits.appId))
    .leftJoin(appSnapshots, and(eq(appSnapshots.appId, apps.id), eq(appSnapshots.runId, runId)))
    .where(eq(keywords.runId, runId))
    .all();

  // Số liệu tổng: chỉ tính trên keyword seed
  const seedHits = hits.filter((h) => h.keywordId === seedKw?.id).sort(byRank);
  const seedPlay = seedHits.filter((h) => h.store === 'play');
  const seedIos = seedHits.filter((h) => h.store === 'appstore');
  const installs = seedPlay.map((h) => h.installsMin).filter((n): n is number => n !== null);
  const withUpdate = seedHits.filter((h) => h.updatedAt);
  const releases = seedHits.map((h) => h.releasedAt).filter((d): d is string => !!d).sort();
  const sumTop10 = (xs: Hit[]) => xs.slice(0, 10).reduce((s, h) => s + (h.ratingsCount ?? 0), 0);

  const points = db.select({ date: trendPoints.date, value: trendPoints.value }).from(trendPoints)
    .where(eq(trendPoints.runId, runId)).orderBy(trendPoints.date).all();
  const related = db.select().from(trendRelated).where(eq(trendRelated.runId, runId)).all();
  const relatedOf = (kind: 'top' | 'rising') => related.filter((r) => r.kind === kind)
    .sort((a, b) => b.value - a.value).map((r) => ({ query: r.query, value: r.value }));

  const termById = new Map(kws.map((k) => [k.id, k.term]));
  const posts: RedditPostView[] = db.select().from(redditPosts).where(eq(redditPosts.runId, runId)).all()
    .map((p) => ({
      postId: p.postId, subreddit: p.subreddit, title: p.title, url: p.url, score: p.score,
      numComments: p.numComments, createdAt: p.createdAt, isAppRequest: p.isAppRequest, keyword: termById.get(p.keywordId) ?? '',
    }))
    .sort((a, b) => Number(b.isAppRequest) - Number(a.isAppRequest) || b.score - a.score);
  const seedPosts = posts.filter((p) => p.keyword === seedKw?.term);

  const stats: RunStats = {
    playCount: seedPlay.length,
    appstoreCount: seedIos.length,
    maxInstalls: installs.length ? Math.max(...installs) : null,
    medianRating: median(seedHits.map((h) => h.rating).filter((r): r is number => r !== null && r > 0)),
    topRatingsSum: { play: sumTop10(seedPlay), appstore: sumTop10(seedIos) },
    newestRelease: releases.at(-1) ?? null,
    staleSharePct: withUpdate.length
      ? Math.round((withUpdate.filter((h) => daysSince(h.updatedAt!, now) > 365).length / withUpdate.length) * 100)
      : null,
    redditPosts: seedPosts.length,
    redditAppRequests: seedPosts.filter((p) => p.isAppRequest).length,
    trendsAvg: points.length ? Math.round(points.reduce((s, p) => s + p.value, 0) / points.length) : null,
  };

  const keywordRows: KeywordRow[] = kws.map((k) => {
    const mine = hits.filter((h) => h.keywordId === k.id).sort(byRank);
    const play = mine.filter((h) => h.store === 'play');
    const ios = mine.filter((h) => h.store === 'appstore');
    return {
      id: k.id, term: k.term, origin: k.origin, playCount: play.length, appstoreCount: ios.length,
      topPlay: brief(play[0]), topAppstore: brief(ios[0]),
    };
  });

  const byApp = new Map<number, CompetitorRow>();
  for (const h of hits) {
    const cur = byApp.get(h.appId);
    if (cur) {
      cur.keywordCount += 1;
      cur.bestRank = Math.min(cur.bestRank, h.rank);
    } else {
      const { keywordId: _k, rank, ...rest } = h;
      byApp.set(h.appId, { ...rest, keywordCount: 1, bestRank: rank });
    }
  }
  const competitors = [...byApp.values()].sort((a, b) => (b.ratingsCount ?? 0) - (a.ratingsCount ?? 0));

  return {
    run,
    jobs,
    stats,
    keywords: keywordRows,
    competitors,
    charts: {
      installs: countBy(competitors.filter((c) => c.store === 'play' && c.installsMin !== null), (c) => installBucket(c.installsMin!), INSTALL_BUCKETS),
      updateAge: countBy(competitors.filter((c) => c.updatedAt), (c) => ageBucket(c.updatedAt!, now), AGE_BUCKETS),
    },
    trends: { points, top: relatedOf('top'), rising: relatedOf('rising') },
    reddit: {
      posts,
      byMonth: countBy(posts, (p) => monthKey(p.createdAt), lastMonths(now, 12)),
      bySubreddit: countBy(posts, (p) => p.subreddit).slice(0, 10),
    },
  };
}

export function listRuns(db: Db, limit: number): RunSummary[] {
  const rs = db.select().from(runs).orderBy(desc(runs.id)).limit(limit).all();
  if (!rs.length) return [];
  const js = db.select().from(sourceJobs).where(inArray(sourceJobs.runId, rs.map((r) => r.id))).all();
  return rs.map((r) => ({ ...r, jobs: jobViews(js, r.id).map(({ source, status }) => ({ source, status })) }));
}
```

- [ ] **Step 5: Chạy test**

Run: `npx vitest run tests/run-view.test.ts`
Expected: PASS 6 test.

- [ ] **Step 6: Ghi `web/src/lib/deps.ts`**

```ts
import { collectAppstore } from '@/collectors/appstore';
import { collectPlaystore, suggestPlayKeywords } from '@/collectors/playstore';
import { collectReddit } from '@/collectors/reddit';
import { collectTrends } from '@/collectors/trends';
import { getDb } from '@/db/client';
import type { ResearchDeps } from '@/lib/run-research';

export function defaultDeps(): ResearchDeps {
  return {
    db: getDb(),
    suggest: (seed, country) => suggestPlayKeywords(seed, country),
    collectors: { playstore: collectPlaystore, appstore: collectAppstore, trends: collectTrends, reddit: collectReddit },
  };
}
```

- [ ] **Step 7: Ghi `src/app/api/research/route.ts`**

```ts
import { NextResponse } from 'next/server';
import { getDb } from '@/db/client';
import { isCountry } from '@/lib/countries';
import { defaultDeps } from '@/lib/deps';
import { startResearch } from '@/lib/run-research';
import { listRuns } from '@/lib/run-view';

export const runtime = 'nodejs';

export async function GET() {
  return NextResponse.json(listRuns(getDb(), 30));
}

export async function POST(req: Request) {
  const body = await req.json().catch(() => ({}));
  const seed = String(body.seed ?? '').trim();
  const country = String(body.country ?? 'US').toUpperCase();
  if (!seed || seed.length > 80) return NextResponse.json({ error: 'Niche phải có 1–80 ký tự' }, { status: 400 });
  if (!isCountry(country)) return NextResponse.json({ error: `Nước không hỗ trợ: ${country}` }, { status: 400 });
  const { runId, done } = startResearch(defaultDeps(), seed, country, { force: Boolean(body.force) });
  done.catch((e) => console.error('[research]', runId, e));
  return NextResponse.json({ runId });
}
```

- [ ] **Step 8: Ghi `src/app/api/research/[id]/route.ts`**

```ts
import { NextResponse } from 'next/server';
import { getDb } from '@/db/client';
import { getRunView } from '@/lib/run-view';

export const runtime = 'nodejs';

export async function GET(_req: Request, { params }: { params: Promise<{ id: string }> }) {
  const view = getRunView(getDb(), Number((await params).id));
  if (!view) return NextResponse.json({ error: 'Không tìm thấy run' }, { status: 404 });
  return NextResponse.json(view);
}
```

- [ ] **Step 9: Ghi `src/app/api/research/[id]/retry/route.ts`**

```ts
import { NextResponse } from 'next/server';
import { SOURCES, type Source } from '@/db/schema';
import { defaultDeps } from '@/lib/deps';
import { retrySource } from '@/lib/run-research';

export const runtime = 'nodejs';

export async function POST(req: Request, { params }: { params: Promise<{ id: string }> }) {
  const runId = Number((await params).id);
  const { source } = await req.json().catch(() => ({}));
  if (!SOURCES.includes(source)) return NextResponse.json({ error: 'source không hợp lệ' }, { status: 400 });
  retrySource(defaultDeps(), runId, source as Source).catch((e) => console.error('[retry]', runId, source, e));
  return NextResponse.json({ ok: true });
}
```

- [ ] **Step 10: Chạy toàn bộ test + build**

Run: `npm test && npm run build`
Expected: mọi test PASS; build xong, có route `/api/research`, `/api/research/[id]`, `/api/research/[id]/retry`.

- [ ] **Step 11: Commit**

```bash
git add -A
git commit -m "feat(api): getRunView + route tạo run, xem run, thử lại nguồn"
```

---

### Task 11: Trang chủ — ô search + lịch sử

**Files:**
- Create: `web/src/lib/format.ts`, `web/src/components/SourceChip.tsx`, `web/src/components/SearchForm.tsx`, `web/src/components/RunHistory.tsx`
- Modify: `src/app/layout.tsx`, `src/app/page.tsx`, `src/app/globals.css`

**Interfaces:**
- Consumes: `COUNTRIES` (Task 10), `listRuns`, `RunSummary`, `JobStatus` (Task 10), `POST /api/research`
- Produces: `fmtInt(n: number | null): string`, `fmtDate(iso: string | null): string`, `fmtRating(r: number | null): string`, `SOURCE_LABEL: Record<Source, string>`; component `<SourceChip source status />`

- [ ] **Step 1: Ghi `web/src/lib/format.ts`**

```ts
import type { Source } from '@/db/schema';

const compact = new Intl.NumberFormat('en', { notation: 'compact', maximumFractionDigits: 1 });

export const fmtInt = (n: number | null) => (n === null ? '—' : compact.format(n));
export const fmtDate = (iso: string | null) => (iso ? iso.slice(0, 10) : '—');
export const fmtRating = (r: number | null) => (r === null || r === 0 ? '—' : r.toFixed(1));

export const SOURCE_LABEL: Record<Source, string> = {
  playstore: 'Google Play',
  appstore: 'App Store',
  trends: 'Google Trends',
  reddit: 'Reddit',
};
```

- [ ] **Step 2: Ghi `web/src/components/SourceChip.tsx`**

```tsx
import type { JobStatus, Source } from '@/db/schema';
import { SOURCE_LABEL } from '@/lib/format';

const STYLE: Record<JobStatus, string> = {
  pending: 'bg-zinc-100 text-zinc-500',
  running: 'bg-sky-100 text-sky-700 animate-pulse',
  done: 'bg-emerald-100 text-emerald-700',
  error: 'bg-rose-100 text-rose-700',
};

export function SourceChip({ source, status }: { source: Source; status: JobStatus }) {
  return (
    <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${STYLE[status]}`}>
      {SOURCE_LABEL[source]}
    </span>
  );
}
```

- [ ] **Step 3: Ghi `web/src/components/SearchForm.tsx`**

```tsx
'use client';

import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { COUNTRIES } from '@/lib/countries';

export function SearchForm() {
  const router = useRouter();
  const [seed, setSeed] = useState('');
  const [country, setCountry] = useState('US');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);
    const res = await fetch('/api/research', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ seed, country }),
    });
    const json = await res.json();
    if (!res.ok) {
      setError(json.error ?? 'Lỗi không rõ');
      setBusy(false);
      return;
    }
    router.push(`/r/${json.runId}`);
  }

  return (
    <form onSubmit={submit} className="flex flex-col gap-3 sm:flex-row">
      <input
        value={seed}
        onChange={(e) => setSeed(e.target.value)}
        placeholder="Nhập niche, ví dụ: habit tracker"
        maxLength={80}
        required
        className="flex-1 rounded-lg border border-zinc-300 bg-white px-4 py-3 text-base outline-none focus:border-zinc-900"
      />
      <select
        value={country}
        onChange={(e) => setCountry(e.target.value)}
        className="rounded-lg border border-zinc-300 bg-white px-3 py-3"
      >
        {COUNTRIES.map((c) => <option key={c.code} value={c.code}>{c.code} · {c.label}</option>)}
      </select>
      <button
        disabled={busy}
        className="rounded-lg bg-zinc-900 px-6 py-3 font-medium text-white disabled:opacity-50"
      >
        {busy ? 'Đang tạo…' : 'Research'}
      </button>
      {error && <p className="text-sm text-rose-600 sm:basis-full">{error}</p>}
    </form>
  );
}
```

- [ ] **Step 4: Ghi `web/src/components/RunHistory.tsx`**

```tsx
import Link from 'next/link';
import type { RunSummary } from '@/lib/run-view';
import { SourceChip } from './SourceChip';

export function RunHistory({ runs }: { runs: RunSummary[] }) {
  if (!runs.length) return <p className="text-sm text-zinc-500">Chưa tra niche nào.</p>;
  return (
    <ul className="divide-y divide-zinc-200 rounded-xl border border-zinc-200 bg-white">
      {runs.map((r) => (
        <li key={r.id}>
          <Link href={`/r/${r.id}`} className="flex flex-wrap items-center gap-3 px-4 py-3 hover:bg-zinc-50">
            <span className="font-medium">{r.seed}</span>
            <span className="text-xs text-zinc-500">{r.country} · {r.createdAt.slice(0, 16).replace('T', ' ')}</span>
            <span className="ml-auto flex flex-wrap gap-1">
              {r.jobs.map((j) => <SourceChip key={j.source} source={j.source} status={j.status} />)}
            </span>
          </Link>
        </li>
      ))}
    </ul>
  );
}
```

- [ ] **Step 5: Thay `src/app/page.tsx`**

```tsx
import { RunHistory } from '@/components/RunHistory';
import { SearchForm } from '@/components/SearchForm';
import { getDb } from '@/db/client';
import { listRuns } from '@/lib/run-view';

export const dynamic = 'force-dynamic';

export default function Home() {
  const runs = listRuns(getDb(), 30);
  return (
    <main className="mx-auto max-w-4xl space-y-8 px-4 py-10">
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold">niche-radar</h1>
        <p className="text-sm text-zinc-600">Tra một niche trên Google Play, App Store, Google Trends và Reddit.</p>
      </header>
      <SearchForm />
      <section className="space-y-3">
        <h2 className="text-sm font-semibold uppercase tracking-wide text-zinc-500">Đã tra</h2>
        <RunHistory runs={runs} />
      </section>
    </main>
  );
}
```

- [ ] **Step 6: Sửa `src/app/layout.tsx`** — giữ phần font create-next-app sinh ra, chỉ đổi `metadata`, `lang` và class `body`

```tsx
export const metadata: Metadata = {
  title: 'niche-radar',
  description: 'Tra niche trên store, Trends và Reddit',
};
// trong RootLayout:
// <html lang="vi">
//   <body className={`${geistSans.variable} ${geistMono.variable} min-h-screen bg-zinc-50 text-zinc-900 antialiased`}>
```

- [ ] **Step 7: Bỏ khối dark mode mặc định trong `src/app/globals.css`** (v1 chỉ có giao diện sáng; nền đã đặt ở `body`). Xoá block `@media (prefers-color-scheme: dark) { :root { … } }`; giữ `@import "tailwindcss";` và phần còn lại.

- [ ] **Step 8: Kiểm trên trình duyệt**

Chạy preview `niche-radar` (`.claude/launch.json`), mở `http://localhost:3200`.
Expected: thấy tiêu đề, ô search, dropdown 5 nước, dòng "Chưa tra niche nào."; console không lỗi. Gõ `habit tracker` → bấm Research → chuyển sang `/r/1` (trang 404 là đúng ở bước này, Task 12 mới làm trang kết quả). Quay lại `/` → lịch sử có dòng `habit tracker` với 4 chip.

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "feat(ui): trang chủ — ô search, chọn nước, lịch sử run"
```

---

### Task 12: Trang kết quả — polling, header, số liệu, bảng keyword

**Files:**
- Create: `src/app/r/[id]/page.tsx`, `web/src/components/RunDashboard.tsx`, `web/src/components/RunHeader.tsx`, `web/src/components/SourceBlock.tsx`, `web/src/components/StatTiles.tsx`, `web/src/components/KeywordTable.tsx`

**Interfaces:**
- Consumes: `RunView`, `JobView`, `RunStats`, `KeywordRow` (Task 10); `fmtInt`, `fmtDate`, `fmtRating`, `SOURCE_LABEL`, `SourceChip` (Task 11); `GET /api/research/[id]`, `POST /api/research/[id]/retry`, `POST /api/research`
- Produces: `<SourceBlock title jobs onRetry>` (Task 13–14 dùng); `RunDashboard` có chỗ cắm `CompetitorBlock`, `TrendsBlock`, `RedditBlock`

- [ ] **Step 1: Ghi `src/app/r/[id]/page.tsx`**

```tsx
import { RunDashboard } from '@/components/RunDashboard';

export default async function RunPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return <RunDashboard runId={Number(id)} />;
}
```

- [ ] **Step 2: Ghi `web/src/components/SourceBlock.tsx`**

```tsx
'use client';

import type { Source } from '@/db/schema';
import { SOURCE_LABEL } from '@/lib/format';
import type { JobView } from '@/lib/run-view';

function ErrorBox({ job, onRetry }: { job: JobView; onRetry: () => void }) {
  return (
    <div className="mb-3 rounded-lg border border-rose-200 bg-rose-50 p-3 text-sm text-rose-800">
      <div className="flex items-start gap-3">
        <p className="flex-1">
          <b>{SOURCE_LABEL[job.source]}</b> lỗi <code>{job.errorCode}</code>: {job.errorMessage}
        </p>
        <button onClick={onRetry} className="rounded-md bg-rose-600 px-3 py-1 text-white">Thử lại</button>
      </div>
      {job.errorCode === 'MISSING_KEYS' && (
        <ol className="mt-2 list-decimal pl-5 text-rose-900">
          <li>Vào <a className="underline" href="https://www.reddit.com/prefs/apps" target="_blank" rel="noreferrer">reddit.com/prefs/apps</a> → “create another app…” → chọn loại <b>script</b>.</li>
          <li>Chép <code>.env.example</code> thành <code>.env.local</code>, điền client id (dưới tên app), secret, user agent.</li>
          <li>Khởi động lại <code>npm run dev</code> rồi bấm Thử lại.</li>
        </ol>
      )}
    </div>
  );
}

export function SourceBlock({ title, jobs, onRetry, children }: {
  title: string;
  jobs: JobView[];
  onRetry: (source: Source) => void;
  children: React.ReactNode;
}) {
  const busy = jobs.some((j) => j.status === 'pending' || j.status === 'running');
  const anyDone = jobs.some((j) => j.status === 'done');
  return (
    <section className="rounded-xl border border-zinc-200 bg-white p-5">
      <h2 className="mb-4 text-lg font-semibold">{title}</h2>
      {jobs.filter((j) => j.status === 'error').map((j) => (
        <ErrorBox key={j.source} job={j} onRetry={() => onRetry(j.source)} />
      ))}
      {anyDone && children}
      {busy && !anyDone && <div className="h-40 animate-pulse rounded-lg bg-zinc-100" />}
    </section>
  );
}
```

- [ ] **Step 3: Ghi `web/src/components/RunHeader.tsx`**

```tsx
'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useState } from 'react';
import type { RunView } from '@/lib/run-view';
import { SourceChip } from './SourceChip';

export function RunHeader({ view }: { view: RunView }) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  async function rerun() {
    setBusy(true);
    const res = await fetch('/api/research', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ seed: view.run.seed, country: view.run.country, force: true }),
    });
    const json = await res.json();
    router.push(`/r/${json.runId}`);
  }

  return (
    <header className="space-y-3">
      <Link href="/" className="text-sm text-zinc-500 hover:text-zinc-900">← Tra niche khác</Link>
      <div className="flex flex-wrap items-center gap-3">
        <h1 className="text-2xl font-semibold">{view.run.seed}</h1>
        <span className="text-sm text-zinc-500">{view.run.country} · {view.run.createdAt.slice(0, 16).replace('T', ' ')}</span>
        <button onClick={rerun} disabled={busy} className="ml-auto rounded-lg border border-zinc-300 px-3 py-1.5 text-sm disabled:opacity-50">
          {busy ? 'Đang tạo…' : 'Tra lại (bỏ cache)'}
        </button>
      </div>
      <div className="flex flex-wrap gap-1.5">
        {view.jobs.map((j) => <SourceChip key={j.source} source={j.source} status={j.status} />)}
      </div>
    </header>
  );
}
```

- [ ] **Step 4: Ghi `web/src/components/StatTiles.tsx`**

```tsx
import { fmtDate, fmtInt, fmtRating } from '@/lib/format';
import type { RunStats } from '@/lib/run-view';

function Tile({ label, value, hint }: { label: string; value: string; hint?: string }) {
  return (
    <div className="rounded-xl border border-zinc-200 bg-white p-4">
      <p className="text-xs text-zinc-500">{label}</p>
      <p className="mt-1 text-2xl font-semibold tabular-nums">{value}</p>
      {hint && <p className="mt-0.5 text-xs text-zinc-500">{hint}</p>}
    </div>
  );
}

export function StatTiles({ stats }: { stats: RunStats }) {
  return (
    <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
      <Tile label="App trên Google Play" value={String(stats.playCount)} hint="top 30, keyword gốc" />
      <Tile label="App trên App Store" value={String(stats.appstoreCount)} hint="top 30, keyword gốc" />
      <Tile label="Số cài cao nhất (Play)" value={fmtInt(stats.maxInstalls)} />
      <Tile label="Median rating" value={fmtRating(stats.medianRating)} hint="gộp 2 store" />
      <Tile label="Tổng rating top 10" value={`${fmtInt(stats.topRatingsSum.play)} / ${fmtInt(stats.topRatingsSum.appstore)}`} hint="Play / App Store" />
      <Tile label="App mới nhất ra mắt" value={fmtDate(stats.newestRelease)} />
      <Tile label="App bỏ bê > 1 năm" value={stats.staleSharePct === null ? '—' : `${stats.staleSharePct}%`} hint="không update > 365 ngày" />
      <Tile label="Bài Reddit 12 tháng" value={String(stats.redditPosts)} hint={`${stats.redditAppRequests} bài xin app`} />
      <Tile label="Google Trends TB 12 tháng" value={stats.trendsAvg === null ? '—' : String(stats.trendsAvg)} hint="thang 0–100" />
    </div>
  );
}
```

- [ ] **Step 5: Ghi `web/src/components/KeywordTable.tsx`**

```tsx
import { fmtInt } from '@/lib/format';
import type { AppBrief, KeywordRow } from '@/lib/run-view';

function Top({ app, installs }: { app: AppBrief | null; installs?: boolean }) {
  if (!app) return <span className="text-zinc-400">chưa có</span>;
  return (
    <a href={app.url} target="_blank" rel="noreferrer" className="hover:underline">
      {app.title}
      <span className="ml-1 text-xs text-zinc-500">
        {installs && app.installsMin !== null ? `${fmtInt(app.installsMin)}+ cài · ` : ''}{fmtInt(app.ratingsCount)} rating
      </span>
    </a>
  );
}

export function KeywordTable({ rows }: { rows: KeywordRow[] }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left text-sm">
        <thead className="text-xs uppercase text-zinc-500">
          <tr>
            <th className="py-2 pr-4">Keyword</th>
            <th className="py-2 pr-4 text-right">Play</th>
            <th className="py-2 pr-4 text-right">App Store</th>
            <th className="py-2 pr-4">Top 1 Play</th>
            <th className="py-2">Top 1 App Store</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-zinc-100">
          {rows.map((r) => (
            <tr key={r.id}>
              <td className="py-2 pr-4">
                {r.term}
                {r.origin === 'seed' && <span className="ml-2 rounded bg-zinc-900 px-1.5 py-0.5 text-[10px] text-white">gốc</span>}
              </td>
              <td className="py-2 pr-4 text-right tabular-nums">{r.playCount}</td>
              <td className="py-2 pr-4 text-right tabular-nums">{r.appstoreCount}</td>
              <td className="py-2 pr-4"><Top app={r.topPlay} installs /></td>
              <td className="py-2"><Top app={r.topAppstore} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

- [ ] **Step 6: Ghi `web/src/components/RunDashboard.tsx`** (Task 13–14 sẽ thay 3 chỗ `{/* … */}` bằng block thật)

```tsx
'use client';

import { useCallback, useEffect, useState } from 'react';
import type { Source } from '@/db/schema';
import type { RunView } from '@/lib/run-view';
import { KeywordTable } from './KeywordTable';
import { RunHeader } from './RunHeader';
import { SourceBlock } from './SourceBlock';
import { StatTiles } from './StatTiles';

const POLL_MS = 2000;
const isSettled = (v: RunView) => v.jobs.every((j) => j.status === 'done' || j.status === 'error');

export function RunDashboard({ runId }: { runId: number }) {
  const [view, setView] = useState<RunView | null>(null);
  const [notFound, setNotFound] = useState(false);
  const [polling, setPolling] = useState(true);

  const load = useCallback(async () => {
    const res = await fetch(`/api/research/${runId}`, { cache: 'no-store' });
    if (res.status === 404) {
      setNotFound(true);
      setPolling(false);
      return;
    }
    const next: RunView = await res.json();
    setView(next);
    if (isSettled(next)) setPolling(false);
  }, [runId]);

  useEffect(() => {
    load();
    if (!polling) return;
    const t = setInterval(load, POLL_MS);
    return () => clearInterval(t);
  }, [load, polling]);

  async function retry(source: Source) {
    await fetch(`/api/research/${runId}/retry`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source }),
    });
    setPolling(true);
  }

  if (notFound) return <main className="mx-auto max-w-6xl px-4 py-10">Không tìm thấy run #{runId}.</main>;
  if (!view) return <main className="mx-auto max-w-6xl px-4 py-10 text-zinc-500">Đang tải…</main>;

  const jobs = (...s: Source[]) => view.jobs.filter((j) => s.includes(j.source));

  return (
    <main className="mx-auto max-w-6xl space-y-6 px-4 py-8">
      <RunHeader view={view} />
      <StatTiles stats={view.stats} />
      <SourceBlock title="Keyword × Store — đã có ai làm chưa" jobs={jobs('playstore', 'appstore')} onRetry={retry}>
        <KeywordTable rows={view.keywords} />
      </SourceBlock>
      {/* CompetitorBlock — Task 13 */}
      {/* TrendsBlock — Task 14 */}
      {/* RedditBlock — Task 14 */}
    </main>
  );
}
```

- [ ] **Step 7: Kiểm trên trình duyệt**

Mở `http://localhost:3200`, tra `habit tracker` (US).
Expected:
- `/r/<id>` hiện header, 4 chip đổi màu dần (xám → xanh dương → xanh lá/đỏ).
- Hàng số liệu có số.
- Bảng keyword có dòng `habit tracker` (nhãn "gốc") + tối đa 5 dòng gợi ý.
- Chưa có `.env.local` → chip Reddit đỏ; số liệu Reddit = 0.
- Polling dừng khi 4 nguồn xong (tab Network không còn request mới).
- Bấm "Tra lại (bỏ cache)" → chuyển sang run mới.
- Console không lỗi.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(ui): trang kết quả — polling, header, số liệu, bảng keyword × store"
```

---

### Task 13: Khối đối thủ — bảng + 3 biểu đồ

**Files:**
- Create: `web/src/components/charts/BucketBar.tsx`, `web/src/components/charts/RatingScatter.tsx`, `web/src/components/CompetitorBlock.tsx`
- Modify: `web/src/components/RunDashboard.tsx`

**Interfaces:**
- Consumes: `CompetitorRow`, `Bucket` (Task 10); `fmtInt`, `fmtDate`, `fmtRating` (Task 11); `SourceBlock` (Task 12)
- Produces: `<BucketBar data color? horizontal? height? />` (Task 14 dùng lại)

- [ ] **Step 1: Ghi `web/src/components/charts/BucketBar.tsx`**

```tsx
'use client';

import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import type { Bucket } from '@/lib/run-view';

export function BucketBar({ data, color = '#18181b', horizontal = false, height = 220 }: {
  data: Bucket[];
  color?: string;
  horizontal?: boolean;
  height?: number;
}) {
  return (
    <ResponsiveContainer width="100%" height={height}>
      {horizontal ? (
        <BarChart data={data} layout="vertical" margin={{ left: 8, right: 16 }}>
          <CartesianGrid horizontal={false} stroke="#e4e4e7" />
          <XAxis type="number" allowDecimals={false} tick={{ fontSize: 12 }} />
          <YAxis type="category" dataKey="key" width={130} tick={{ fontSize: 12 }} />
          <Tooltip />
          <Bar dataKey="count" name="Số lượng" fill={color} radius={[0, 4, 4, 0]} />
        </BarChart>
      ) : (
        <BarChart data={data} margin={{ right: 8 }}>
          <CartesianGrid vertical={false} stroke="#e4e4e7" />
          <XAxis dataKey="key" tick={{ fontSize: 12 }} />
          <YAxis allowDecimals={false} width={32} tick={{ fontSize: 12 }} />
          <Tooltip />
          <Bar dataKey="count" name="Số lượng" fill={color} radius={[4, 4, 0, 0]} />
        </BarChart>
      )}
    </ResponsiveContainer>
  );
}
```

- [ ] **Step 2: Ghi `web/src/components/charts/RatingScatter.tsx`**

```tsx
'use client';

import { CartesianGrid, Legend, ResponsiveContainer, Scatter, ScatterChart, Tooltip, XAxis, YAxis } from 'recharts';
import { fmtInt } from '@/lib/format';
import type { CompetitorRow } from '@/lib/run-view';

export const STORE_COLOR = { play: '#059669', appstore: '#0284c7' } as const;

export function RatingScatter({ apps }: { apps: CompetitorRow[] }) {
  // trục log không vẽ được 0 → bỏ app chưa có rating
  const pts = apps.filter((a) => (a.ratingsCount ?? 0) > 0 && a.rating);
  const series = (store: 'play' | 'appstore') =>
    pts.filter((a) => a.store === store).map((a) => ({ x: a.ratingsCount, y: a.rating, title: a.title }));
  return (
    <ResponsiveContainer width="100%" height={280}>
      <ScatterChart margin={{ right: 16 }}>
        <CartesianGrid stroke="#e4e4e7" />
        <XAxis type="number" dataKey="x" name="Số rating" scale="log" domain={['auto', 'auto']}
          tickFormatter={(v) => fmtInt(v)} tick={{ fontSize: 12 }} />
        <YAxis type="number" dataKey="y" name="Rating" domain={[1, 5]} width={32} tick={{ fontSize: 12 }} />
        <Tooltip
          cursor={{ strokeDasharray: '3 3' }}
          content={({ payload }) => {
            const p = payload?.[0]?.payload;
            if (!p) return null;
            return (
              <div className="rounded border border-zinc-200 bg-white px-2 py-1 text-xs shadow">
                <b>{p.title}</b><br />{p.y.toFixed(1)}★ · {fmtInt(p.x)} rating
              </div>
            );
          }}
        />
        <Legend />
        <Scatter name="Google Play" data={series('play')} fill={STORE_COLOR.play} />
        <Scatter name="App Store" data={series('appstore')} fill={STORE_COLOR.appstore} />
      </ScatterChart>
    </ResponsiveContainer>
  );
}
```

- [ ] **Step 3: Ghi `web/src/components/CompetitorBlock.tsx`**

```tsx
'use client';

import { useMemo, useState } from 'react';
import { fmtDate, fmtInt, fmtRating } from '@/lib/format';
import type { Bucket, CompetitorRow } from '@/lib/run-view';
import { BucketBar } from './charts/BucketBar';
import { RatingScatter } from './charts/RatingScatter';

type SortKey = 'title' | 'rating' | 'ratingsCount' | 'installsMin' | 'updatedAt' | 'releasedAt' | 'price' | 'keywordCount';
const COLUMNS: { key: SortKey; label: string }[] = [
  { key: 'title', label: 'App' },
  { key: 'rating', label: 'Rating' },
  { key: 'ratingsCount', label: 'Số rating' },
  { key: 'installsMin', label: 'Số cài' },
  { key: 'updatedAt', label: 'Update cuối' },
  { key: 'releasedAt', label: 'Ra mắt' },
  { key: 'price', label: 'Giá' },
  { key: 'keywordCount', label: 'Số keyword' },
];

export function CompetitorBlock({ apps, installs, updateAge }: { apps: CompetitorRow[]; installs: Bucket[]; updateAge: Bucket[] }) {
  const [store, setStore] = useState<'all' | 'play' | 'appstore'>('all');
  const [sort, setSort] = useState<{ key: SortKey; dir: 1 | -1 }>({ key: 'ratingsCount', dir: -1 });

  const rows = useMemo(() => {
    const list = apps.filter((a) => store === 'all' || a.store === store);
    return [...list].sort((a, b) => {
      const va = a[sort.key];
      const vb = b[sort.key];
      if (va === null) return 1; // giá trị trống luôn xuống cuối
      if (vb === null) return -1;
      return (va < vb ? -1 : va > vb ? 1 : 0) * sort.dir;
    });
  }, [apps, store, sort]);

  const toggle = (key: SortKey) => setSort((s) => (s.key === key ? { key, dir: s.dir === 1 ? -1 : 1 } : { key, dir: -1 }));

  return (
    <div className="space-y-6">
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-3">
          <h3 className="mb-2 text-sm font-medium text-zinc-600">Rating × số rating (trục ngang log)</h3>
          <RatingScatter apps={apps} />
        </div>
        <div>
          <h3 className="mb-2 text-sm font-medium text-zinc-600">Phân bố số cài (Google Play)</h3>
          <BucketBar data={installs} color="#059669" />
        </div>
        <div className="lg:col-span-2">
          <h3 className="mb-2 text-sm font-medium text-zinc-600">Lần update cuối cách đây</h3>
          <BucketBar data={updateAge} color="#71717a" />
        </div>
      </div>

      <div className="flex gap-2 text-sm">
        {(['all', 'play', 'appstore'] as const).map((s) => (
          <button key={s} onClick={() => setStore(s)}
            className={`rounded-full px-3 py-1 ${store === s ? 'bg-zinc-900 text-white' : 'bg-zinc-100'}`}>
            {s === 'all' ? `Tất cả (${apps.length})` : s === 'play' ? 'Google Play' : 'App Store'}
          </button>
        ))}
      </div>

      <div className="max-h-[560px] overflow-auto">
        <table className="w-full text-left text-sm">
          <thead className="sticky top-0 bg-white text-xs uppercase text-zinc-500">
            <tr>
              {COLUMNS.map((c) => (
                <th key={c.key} className="cursor-pointer select-none py-2 pr-4" onClick={() => toggle(c.key)}>
                  {c.label}{sort.key === c.key ? (sort.dir === 1 ? ' ▲' : ' ▼') : ''}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-100">
            {rows.map((a) => (
              <tr key={a.appId}>
                <td className="py-2 pr-4">
                  <a href={a.url} target="_blank" rel="noreferrer" className="flex items-center gap-2 hover:underline">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    {a.iconUrl && <img src={a.iconUrl} alt="" className="h-7 w-7 rounded-md" />}
                    <span>
                      {a.title}
                      <span className="block text-xs text-zinc-500">
                        {a.store === 'play' ? 'Play' : 'App Store'} · {a.developer}
                      </span>
                    </span>
                  </a>
                </td>
                <td className="py-2 pr-4 tabular-nums">{fmtRating(a.rating)}</td>
                <td className="py-2 pr-4 tabular-nums">{fmtInt(a.ratingsCount)}</td>
                <td className="py-2 pr-4 tabular-nums">{a.installsMin === null ? '—' : `${fmtInt(a.installsMin)}+`}</td>
                <td className="py-2 pr-4">{fmtDate(a.updatedAt)}</td>
                <td className="py-2 pr-4">{fmtDate(a.releasedAt)}</td>
                <td className="py-2 pr-4">{a.price ? `$${a.price}` : 'Free'}</td>
                <td className="py-2 pr-4 tabular-nums">{a.keywordCount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Cắm vào `web/src/components/RunDashboard.tsx`** — thêm import và thay dòng `{/* CompetitorBlock — Task 13 */}`

```tsx
import { CompetitorBlock } from './CompetitorBlock';
```

```tsx
      <SourceBlock title={`Đối thủ (${view.competitors.length} app)`} jobs={jobs('playstore', 'appstore')} onRetry={retry}>
        <CompetitorBlock apps={view.competitors} installs={view.charts.installs} updateAge={view.charts.updateAge} />
      </SourceBlock>
```

- [ ] **Step 5: Kiểm trên trình duyệt**

Mở lại run `habit tracker`.
Expected:
- Scatter có 2 màu (xanh lá Play, xanh dương App Store), hover hiện tên app.
- 2 biểu đồ cột có số.
- Bảng lọc được theo store; bấm tiêu đề cột thì đổi chiều sắp xếp (ô trống nằm cuối).
- Icon app hiện; console không lỗi.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(ui): khối đối thủ — bảng lọc/sắp xếp + scatter rating, phân bố số cài, tuổi update"
```

---

### Task 14: Khối Trends + Reddit

**Files:**
- Create: `web/src/components/charts/TrendLine.tsx`, `web/src/components/TrendsBlock.tsx`, `web/src/components/RedditBlock.tsx`
- Modify: `web/src/components/RunDashboard.tsx`

**Interfaces:**
- Consumes: `RunView['trends']`, `RunView['reddit']`, `RedditPostView` (Task 10); `BucketBar` (Task 13); `fmtDate` (Task 11); `SourceBlock` (Task 12)

- [ ] **Step 1: Ghi `web/src/components/charts/TrendLine.tsx`**

```tsx
'use client';

import { CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

export function TrendLine({ points }: { points: { date: string; value: number }[] }) {
  return (
    <ResponsiveContainer width="100%" height={260}>
      <LineChart data={points} margin={{ right: 16 }}>
        <CartesianGrid vertical={false} stroke="#e4e4e7" />
        <XAxis dataKey="date" tickFormatter={(d: string) => d.slice(0, 7)} minTickGap={40} tick={{ fontSize: 12 }} />
        <YAxis domain={[0, 100]} width={32} tick={{ fontSize: 12 }} />
        <Tooltip />
        <Line type="monotone" dataKey="value" name="Độ quan tâm" stroke="#7c3aed" strokeWidth={2} dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
}
```

- [ ] **Step 2: Ghi `web/src/components/TrendsBlock.tsx`**

```tsx
import type { RunView } from '@/lib/run-view';
import { TrendLine } from './charts/TrendLine';

function QueryList({ title, items, suffix }: { title: string; items: { query: string; value: number }[]; suffix: string }) {
  return (
    <div>
      <h3 className="mb-2 text-sm font-medium text-zinc-600">{title}</h3>
      {items.length === 0 ? <p className="text-sm text-zinc-400">Không có dữ liệu</p> : (
        <ol className="space-y-1 text-sm">
          {items.slice(0, 10).map((q) => (
            <li key={q.query} className="flex justify-between gap-3">
              <span>{q.query}</span>
              <span className="tabular-nums text-zinc-500">{q.value}{suffix}</span>
            </li>
          ))}
        </ol>
      )}
    </div>
  );
}

export function TrendsBlock({ trends }: { trends: RunView['trends'] }) {
  return (
    <div className="grid gap-6 lg:grid-cols-3">
      <div className="lg:col-span-2">
        <h3 className="mb-2 text-sm font-medium text-zinc-600">Độ quan tâm 12 tháng (keyword gốc)</h3>
        {trends.points.length ? <TrendLine points={trends.points} /> : <p className="text-sm text-zinc-400">Không có dữ liệu</p>}
      </div>
      <div className="space-y-6">
        <QueryList title="Related queries — top" items={trends.top} suffix="" />
        <QueryList title="Related queries — rising" items={trends.rising} suffix="%" />
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Ghi `web/src/components/RedditBlock.tsx`**

```tsx
import { fmtDate } from '@/lib/format';
import type { RunView } from '@/lib/run-view';
import { BucketBar } from './charts/BucketBar';

export function RedditBlock({ reddit }: { reddit: RunView['reddit'] }) {
  return (
    <div className="space-y-6">
      <div className="grid gap-6 lg:grid-cols-2">
        <div>
          <h3 className="mb-2 text-sm font-medium text-zinc-600">Số bài theo tháng</h3>
          <BucketBar data={reddit.byMonth.map((b) => ({ ...b, key: b.key.slice(2) }))} color="#ea580c" />
        </div>
        <div>
          <h3 className="mb-2 text-sm font-medium text-zinc-600">Top subreddit</h3>
          <BucketBar data={reddit.bySubreddit.map((b) => ({ ...b, key: `r/${b.key}` }))} color="#ea580c" horizontal height={260} />
        </div>
      </div>
      <ul className="max-h-[520px] divide-y divide-zinc-100 overflow-auto text-sm">
        {reddit.posts.map((p) => (
          <li key={p.postId} className="py-2">
            <a href={p.url} target="_blank" rel="noreferrer" className="hover:underline">
              {p.isAppRequest && <span className="mr-2 rounded bg-orange-100 px-1.5 py-0.5 text-[10px] font-medium text-orange-800">xin app</span>}
              {p.title}
            </a>
            <p className="text-xs text-zinc-500">
              r/{p.subreddit} · {p.score} điểm · {p.numComments} comment · {fmtDate(p.createdAt)} · “{p.keyword}”
            </p>
          </li>
        ))}
        {reddit.posts.length === 0 && <li className="py-2 text-zinc-400">Không có bài nào trong 12 tháng.</li>}
      </ul>
    </div>
  );
}
```

- [ ] **Step 4: Cắm vào `web/src/components/RunDashboard.tsx`** — thêm import và thay 2 dòng `{/* TrendsBlock — Task 14 */}`, `{/* RedditBlock — Task 14 */}`

```tsx
import { RedditBlock } from './RedditBlock';
import { TrendsBlock } from './TrendsBlock';
```

```tsx
      <SourceBlock title="Google Trends" jobs={jobs('trends')} onRetry={retry}>
        <TrendsBlock trends={view.trends} />
      </SourceBlock>
      <SourceBlock title={`Reddit (${view.reddit.posts.length} bài)`} jobs={jobs('reddit')} onRetry={retry}>
        <RedditBlock reddit={view.reddit} />
      </SourceBlock>
```

- [ ] **Step 5: Kiểm trên trình duyệt**

Expected:
- **Trends:** có đường 12 tháng + 2 danh sách. Nếu Trends lỗi `RATE_LIMITED` → hộp đỏ có nút Thử lại; bấm thì chip chuyển xanh dương rồi xong/đỏ lại.
- **Reddit khi chưa có `.env.local`:** hộp đỏ `MISSING_KEYS` kèm 3 bước hướng dẫn.
- **Reddit sau khi điền key** và khởi động lại dev server → bấm Thử lại → có 2 biểu đồ cam + danh sách bài, bài "xin app" lên đầu.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(ui): khối Google Trends và Reddit"
```

---

### Task 15: Smoke script, README, kiểm toàn bộ

**Files:**
- Create: `web/scripts/smoke.ts`, `README.md`

**Interfaces:**
- Consumes: `createDb` (Task 2); collector thật + `suggestPlayKeywords` (Task 5–8); `startResearch` (Task 9); `getRunView` (Task 10)

- [ ] **Step 1: Ghi `web/scripts/smoke.ts`**

```ts
// Gọi thật 4 nguồn với một DB tạm, in kết quả. Chạy: npm run smoke -- "habit tracker" [US]
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { collectAppstore } from '@/collectors/appstore';
import { collectPlaystore, suggestPlayKeywords } from '@/collectors/playstore';
import { collectReddit } from '@/collectors/reddit';
import { collectTrends } from '@/collectors/trends';
import { createDb } from '@/db/client';
import { startResearch } from '@/lib/run-research';
import { getRunView } from '@/lib/run-view';

async function main() {
  try {
    process.loadEnvFile('.env.local');
  } catch {
    // chưa có key Reddit: nguồn reddit sẽ báo MISSING_KEYS
  }

  const [seed = 'habit tracker', country = 'US'] = process.argv.slice(2);
  const db = createDb(join(mkdtempSync(join(tmpdir(), 'niche-smoke-')), 'smoke.db'));
  const started = Date.now();
  const { runId, done } = startResearch(
    {
      db,
      suggest: suggestPlayKeywords,
      collectors: { playstore: collectPlaystore, appstore: collectAppstore, trends: collectTrends, reddit: collectReddit },
    },
    seed,
    country,
  );
  await done;

  const v = getRunView(db, runId)!;
  console.log(`seed="${v.run.seed}" country=${v.run.country} (${Math.round((Date.now() - started) / 1000)}s)`);
  console.log('keywords:', v.keywords.map((k) => k.term).join(' | '));
  for (const j of v.jobs) console.log(`  ${j.source.padEnd(9)} ${j.status}${j.errorCode ? ` ${j.errorCode}: ${j.errorMessage}` : ''}`);
  console.log(`apps: play=${v.competitors.filter((c) => c.store === 'play').length} appstore=${v.competitors.filter((c) => c.store === 'appstore').length}`);
  console.log(`trends: ${v.trends.points.length} điểm, ${v.trends.top.length} top, ${v.trends.rising.length} rising`);
  console.log(`reddit: ${v.reddit.posts.length} bài (${v.reddit.posts.filter((p) => p.isAppRequest).length} xin app)`);
  console.log('stats:', v.stats);
}

// bọc trong main(): package.json không có "type": "module" nên không dùng top-level await được
main().catch((e) => {
  console.error(e);
  process.exit(1);
});
```

- [ ] **Step 2: Chạy smoke**

Run: `npm run smoke -- "habit tracker" US`
Expected (mất khoảng 1–3 phút vì Play phải gọi chi tiết từng app với nhịp 1 req/s):
- `playstore done`, `appstore done`, `apps: play>0 appstore>0`;
- `trends done` có ~52 điểm, hoặc `error RATE_LIMITED`. Lỗi này là hợp lệ, ghi lại;
- `reddit error MISSING_KEYS` nếu chưa có key, hoặc `done` + số bài.

Nếu shape dữ liệu thật khác fixture (ví dụ `gplay.app()` đổi tên trường): sửa hàm `normalize*` cho khớp, cập nhật fixture bằng bản ghi thật, chạy lại `npm test`.

- [ ] **Step 3: Ghi `README.md`**

````markdown
# niche-radar

Web tool chạy local: gõ một niche → tra Google Play, App Store, Google Trends, Reddit → xem đã có ai làm chưa theo từng keyword, kèm biểu đồ và số liệu.

## Chạy

```bash
npm install
cp .env.example .env.local   # điền key Reddit (tuỳ chọn)
npm run dev                  # http://localhost:3200
```

Database: `data/niche.db` (SQLite, tự tạo). Xoá file này là xoá sạch lịch sử.

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `npm run dev` | chạy web ở cổng 3200 |
| `npm test` | unit test (Vitest) |
| `npm run smoke -- "<niche>" [US]` | gọi thật 4 nguồn, in số dòng lấy được |
| `npm run db:generate` | sinh migration sau khi sửa `web/src/db/schema.ts` |

## Nguồn dữ liệu

| Nguồn | Cách lấy | Ghi chú |
|---|---|---|
| Google Play | `google-play-scraper` | có số cài dạng mốc (100K+) |
| App Store | iTunes Search API | không có số cài, chỉ có số rating |
| Google Trends | `google-trends-api` | không có API chính thức, hay bị chặn tạm → bấm Thử lại |
| Reddit | Reddit OAuth (app loại script) | cần key trong `.env.local` |

Kết quả cache 24 giờ theo niche + nước. Nút "Tra lại (bỏ cache)" để lấy mới.

Spec: `docs/superpowers/specs/2026-10-23-niche-radar-design.md`
````

- [ ] **Step 4: Kiểm toàn bộ**

Run: `npm test && npm run lint && npm run build`
Expected: test PASS hết, lint không lỗi, build xong.

Rồi mở preview, tra một niche mới (ví dụ `pomodoro timer`, nước `GB`) và kiểm đủ 6 khối của spec:
1. header + chip;
2. hàng số liệu;
3. bảng Keyword × Store;
4. đối thủ + 3 biểu đồ;
5. Trends;
6. Reddit.

Tra lại cùng niche trong 24h → mọi nguồn `done` gần như ngay lập tức (lấy từ cache). Chụp screenshot trang kết quả làm bằng chứng.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "chore: smoke script + README"
```
