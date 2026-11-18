# Launch · 1 điểm cơ hội: Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Biến sức khoẻ v2 thành **1 điểm cơ hội /100** nhận ra được niche đang kiếm tiền: thêm yếu tố Cửa vào, tách Cạnh tranh ra thành thẻ Độ khó, làm lại Tiền (gói IAP iOS + giá + TrustMRR). Kèm bộ kiểm điểm để đo trước / sau.

**Architecture:** Mỗi phần chấm mới là 1 hàm thuần trong file riêng (`score-entry.ts`, `difficulty.ts`, `money-score.ts`, `trust-match.ts`, `score-bench.ts`), có test. `score-v2.ts` chỉ gọi các hàm này. Bên trong vẫn lưu thang 0–10 (ngưỡng, lịch sử điểm, Project giữ nguyên); chỉ **hiện** ×10 thành /100. Gói IAP iOS đọc ngay sau nguồn App Store, bằng 1 lớp bọc collector.

**Tech Stack:** TypeScript, React, drizzle + SQLite, vitest, tsx. Lệnh chạy trong `web/`.

**Spec:** [Launch · Spec](../../web/launch-app-spec.md) (anh duyệt 2026-11-17) · [Brief](../../web/launch-app-brief.md) · [Bước 0](../../web/launch-app-hieu-sau.md).

## Global Constraints

- Làm trên **worktree riêng**, nhánh `launch-1-diem-co-hoi` cắt từ `main`. Cây chính đang có nhiều thay đổi chưa commit của phiên khác: **không đụng**.
- Mỗi Task: test trước → code → `npm run check` ở gốc repo **xanh** → commit riêng, message dạng `feat(web): … (launch S2)`, kết thúc bằng dòng `Co-Authored-By` theo luật repo.
- Không bịa số. Số nào chưa đo thì ghi `chưa đo`. Ngưỡng là **quy ước của ShotMatic**, ghi ở ⓘ.
- Chữ trong `tr()` / `tx()` là tiếng Việt, và phải có bản tiếng Anh trong `web/src/locales/en-text-launch-score.ts` (file mới, gộp vào `en-text.ts`). Test `tests/i18n-text.test.ts` sẽ đỏ nếu thiếu.
- Giao diện: đứng được từ 960px, sáng + tối (`bg-surface`, `zinc-*`, không hex xám), có English. Soát ở 960px và 1340px.
- **Không hiện số phase / số mục trên UI.**
- Thang trong code **giữ 0–10**. Hiện ra = `Math.round(total * 10)`. Không migration DB.
- Trọng số mặc định (spec S2): `entry 25 · money 25 · pain 15 · demand 10 · trend 10 · reach 10 · fit 5 · competition 0`.
- Ngưỡng giữ `build 6 · test 4` (hiện là 60 / 40). `MIN_COVERAGE` 60 giữ nguyên.
- Đọc DB thật chỉ bằng **bản sao** (`sqlite3 … ".backup <scratch>"`). Không ghi vào `web/data/niche.db` từ script.

## File đụng tới

| File | Việc |
|---|---|
| `web/src/lib/score-bench.ts` (mới) | danh sách 14 niche kiếm tiền, luật chọn niche chết, tóm tắt đạt / trượt |
| `web/scripts/score-bench.ts` (mới) | đọc bản sao DB, chấm bằng code hiện tại, in bảng |
| `web/src/lib/score-entry.ts` (mới) | yếu tố Cửa vào |
| `web/src/lib/difficulty.ts` (mới) | thẻ Độ khó |
| `web/src/lib/money-score.ts` (mới) | công thức Tiền 3 phần + đọc giá |
| `web/src/lib/trust-match.ts` (mới) | khớp thẻ TrustMRR theo keyword |
| `web/src/collectors/appstore-iap.ts` (mới) | đọc gói IAP iOS top 10 sau nguồn App Store |
| `web/src/lib/score-config.ts` | thêm `entry`, trọng số mới, bộ mẫu, `toScore100` |
| `web/src/lib/score-v2.ts` | gọi hàm mới, đổi trọng số đã lưu, `difficulty` trong kết quả |
| `web/src/lib/deps.ts` | bọc `collectAppstore` |
| `web/src/components/HealthIcon.tsx`, `NextSteps.tsx`, `web/src/lib/health-actions.ts` | thêm khoá `entry` |
| `web/src/lib/health-presentation.ts`, `HealthBlock.tsx`, `AnswerRow.tsx`, `RunHeader.tsx`, `NicheMentions.tsx`, `TrackingBlock.tsx`, `HuntPickCard.tsx`, `HuntCandidateList.tsx` | hiện /100, thẻ Độ khó |
| `web/src/mcp/niche-card.ts`, `web/src/mcp/tools.ts` | `score100` + `formulaVersion` |
| `web/src/locales/en-text-launch-score.ts` (mới), `en-text.ts` | tiếng Anh |
| `web/tests/score-bench.test.ts`, `score-entry.test.ts`, `difficulty.test.ts`, `money-score.test.ts`, `trust-match.test.ts`, `appstore-iap.test.ts` (mới) · `health.test.ts`, `health-presentation.test.ts` (sửa) | test |

## Lệch spec (ghi trước khi code)

- **Gói IAP iOS không thành nguồn `iap` riêng** mà đọc ngay trong job App Store, sau khi App Store tìm app xong.
  Lý do: thêm 1 `Source` đụng ≥ 12 file (chip nguồn, ETA, Cài đặt nguồn, activity, run-view…).
  Vẫn giữ ý của spec: lỗi 429 khi đọc IAP **chỉ dừng phần đọc IAP**, lượt App Store vẫn `done`. Tiến độ hiện "đọc gói IAP 3/10".
  Đã ghi vào [spec S4](../../web/launch-app-spec.md#s4-tien).
- **Phần Mức giá chỉ chấm khi nước = US.** Giá gói iOS ở nước khác là tiền địa phương; nước khác ghi "chưa đo".
- **Thang /100 chỉ là cách hiện.** DB, ngưỡng, lịch sử vẫn /10, nên không cần chú thích "công thức cũ" cho lịch sử.
- **Nút "không phải niche này" cho dòng TrustMRR: để sau.** Mỗi dòng khớp đã có link tới trang TrustMRR để tự kiểm. Bộ kiểm (Task 7) cho thấy khớp sai nhiều thì mới làm.

---

### Task 1: Bộ kiểm điểm: hàm thuần

**Files:**

- Create: `web/src/lib/score-bench.ts`
- Test: `web/tests/score-bench.test.ts`

**Interfaces:**

- Produces: `BENCH_EARNING`, `type BenchApp`, `isDeadNiche(top: BenchApp[], now: Date): boolean`, `type BenchRow`, `benchSummary(rows: BenchRow[]): BenchSummary`, `BENCH_TARGET`.

- [ ] **Step 0: Tạo worktree**

```bash
cd niche-radar
git worktree add ../niche-radar-launch1 -b launch-1-diem-co-hoi main
cd ../niche-radar-launch1/web && npm ci
```

- [ ] **Step 1: Viết test đỏ**

```ts
// web/tests/score-bench.test.ts
import { describe, expect, it } from 'vitest';
import { BENCH_EARNING, benchSummary, isDeadNiche, type BenchApp, type BenchRow } from '@/lib/score-bench';

const NOW = new Date('2026-11-17T00:00:00Z');
const app = (p: Partial<BenchApp> = {}): BenchApp => ({ updatedAt: '2023-01-01', releasedAt: '2018-01-01', price: 0, offersIap: false, iapItems: null, ...p });

describe('bộ kiểm điểm', () => {
  it('14 niche kiếm tiền, mỗi cái có slug TrustMRR + doanh thu 30 ngày', () => {
    expect(BENCH_EARNING).toHaveLength(14);
    expect(BENCH_EARNING.every((e) => e.slug && e.last30 > 0)).toBe(true);
    expect(new Set(BENCH_EARNING.map((e) => e.term)).size).toBe(14);
  });

  it('niche chết: ≥ 70% bỏ bê > 1 năm, 0 app thu tiền, 0 app < 1 năm, ≥ 50% app biết có thu tiền hay không', () => {
    const dead = Array.from({ length: 10 }, () => app());
    expect(isDeadNiche(dead, NOW)).toBe(true);
    expect(isDeadNiche([...dead.slice(1), app({ price: 2.99 })], NOW)).toBe(false); // 1 app bán giá
    expect(isDeadNiche([...dead.slice(1), app({ releasedAt: '2026-06-01', updatedAt: '2026-10-01' })], NOW)).toBe(false); // có app mới
    expect(isDeadNiche([...dead.slice(4), ...Array.from({ length: 4 }, () => app({ updatedAt: '2026-10-01' }))], NOW)).toBe(false); // 60% bỏ bê
    expect(isDeadNiche(Array.from({ length: 10 }, () => app({ offersIap: null })), NOW)).toBe(false); // không biết tiền
    expect(isDeadNiche([...dead.slice(1), app({ offersIap: null, iapItems: 2 })], NOW)).toBe(false); // gói IAP iOS đã đọc
    expect(isDeadNiche([], NOW)).toBe(false);
  });

  it('tóm tắt: trung vị /100, cách biệt, đạt khi 0 BỎ ở nhóm tiền, 0 BUILD ở nhóm chết, cách ≥ 15', () => {
    const r = (kind: BenchRow['kind'], score: number | null, decision: BenchRow['decision']): BenchRow => ({ kind, term: `${kind}${score}`, runId: 1, score, decision });
    const ok = benchSummary([r('earning', 62, 'BUILD'), r('earning', 55, 'TEST THÊM'), r('dead', 30, 'BỎ'), r('dead', 41, 'TEST THÊM')]);
    expect(ok).toMatchObject({ earning: { n: 2, median: 59, skip: 0 }, dead: { n: 2, median: 36, build: 0 }, gap: 23, pass: true, fails: [] });
    const bad = benchSummary([r('earning', 37, 'BỎ'), r('earning', 50, 'TEST THÊM'), r('dead', 61, 'BUILD')]);
    expect(bad.pass).toBe(false);
    expect(bad.fails).toEqual(['1/2 niche kiếm tiền bị BỎ', '1 niche chết được BUILD', 'cách biệt -17 < 15']);
    expect(benchSummary([r('earning', 50, 'TEST THÊM')]).fails).toContain('chưa có niche chết');
  });
});
```

- [ ] **Step 2: Chạy test, thấy đỏ**

Run: `npx vitest run tests/score-bench.test.ts`
Expected: FAIL `Cannot find module '@/lib/score-bench'`

- [ ] **Step 3: Viết code**

```ts
// web/src/lib/score-bench.ts
/**
 * Bộ kiểm điểm (launch S1, 2026-11-17): 14 niche đang kiếm tiền thật (TrustMRR, doanh thu 30 ngày đã xác minh)
 * + niche "chết" chọn bằng luật cố định. Chạy lại mỗi lần đổi công thức điểm: niche kiếm tiền không được bị BỎ.
 * Hàm thuần; đọc DB ở scripts/score-bench.ts.
 */
import type { Decision } from './score-config';

/** Đọc trustmrr.com/category/mobile-apps 2026-11-16. `last30` = doanh thu 30 ngày (USD). */
export const BENCH_EARNING: { term: string; slug: string; last30: number }[] = [
  { term: 'calorie tracker', slug: 'nutria-9e3eaa', last30: 77_000 },
  { term: 'astrology', slug: 'project-a', last30: 93_000 },
  { term: 'ai song maker', slug: 'muxa-ai', last30: 15_000 },
  { term: 'ai photo editor', slug: 'mobileapp', last30: 1_100_000 },
  { term: 'iptv player', slug: 'iptv-player-vpn-app-bundle', last30: 15_000 },
  { term: 'sports betting picks', slug: 'propgpt-ai-props-analysis', last30: 90_000 },
  { term: 'depuff', slug: 'depuff-ai', last30: 44_000 },
  { term: 'height increase', slug: 'gotall', last30: 28_000 },
  { term: 'vignette', slug: 'vignette-id', last30: 29_000 },
  { term: 'no contact', slug: 'private-enterprise-6', last30: 3_600 },
  { term: 'ai note taker', slug: 'xyz', last30: 21_000 },
  { term: 'keyboard themes', slug: 'aikeyboard', last30: 27_000 },
  { term: 'make friends', slug: 'bottled', last30: 35_000 },
  { term: 'workout tracker', slug: 'stealth-venture-15', last30: 121_000 },
];

/** 1 app top 10 (theo hạng). `iapItems`: số gói IAP iOS đã đọc (null = chưa đọc). */
export type BenchApp = { updatedAt: string | null; releasedAt: string | null; price: number; offersIap: boolean | null; iapItems: number | null };

const DAY = 864e5;
const ageDays = (iso: string | null, now: Date) => (iso && Number.isFinite(Date.parse(iso)) ? (now.getTime() - Date.parse(iso)) / DAY : null);

/** Niche chết: ≥ 70% app top 10 bỏ bê > 1 năm · không app nào thu tiền · không app nào ra < 1 năm · biết tiền của ≥ 50% app. */
export function isDeadNiche(top: BenchApp[], now: Date): boolean {
  if (!top.length) return false;
  const stale = top.filter((a) => (ageDays(a.updatedAt, now) ?? 0) > 365).length / top.length;
  const known = top.filter((a) => a.price > 0 || a.offersIap !== null || a.iapItems !== null).length / top.length;
  const paying = top.some((a) => a.price > 0 || a.offersIap === true || (a.iapItems ?? 0) > 0);
  const young = top.some((a) => { const d = ageDays(a.releasedAt, now); return d !== null && d < 365; });
  return stale >= 0.7 && known >= 0.5 && !paying && !young;
}

export type BenchRow = { kind: 'earning' | 'dead'; term: string; runId: number; score: number | null; decision: Decision | null };
export type BenchSummary = {
  earning: { n: number; median: number | null; skip: number };
  dead: { n: number; median: number | null; build: number };
  gap: number | null; pass: boolean; fails: string[];
};
/** Mục tiêu spec: cách biệt trung vị ≥ 15 điểm /100. */
export const BENCH_TARGET = 15;

const median = (xs: number[]) => {
  if (!xs.length) return null;
  const s = [...xs].sort((a, b) => a - b);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m] : Math.round((s[m - 1] + s[m]) / 2);
};

export function benchSummary(rows: BenchRow[]): BenchSummary {
  const e = rows.filter((r) => r.kind === 'earning');
  const d = rows.filter((r) => r.kind === 'dead');
  const em = median(e.flatMap((r) => (r.score === null ? [] : [r.score])));
  const dm = median(d.flatMap((r) => (r.score === null ? [] : [r.score])));
  const skip = e.filter((r) => r.decision === 'BỎ').length;
  const build = d.filter((r) => r.decision === 'BUILD').length;
  const gap = em !== null && dm !== null ? em - dm : null;
  const fails = [
    ...(skip ? [`${skip}/${e.length} niche kiếm tiền bị BỎ`] : []),
    ...(build ? [`${build} niche chết được BUILD`] : []),
    ...(!d.length ? ['chưa có niche chết'] : gap !== null && gap < BENCH_TARGET ? [`cách biệt ${gap} < ${BENCH_TARGET}`] : []),
  ];
  return { earning: { n: e.length, median: em, skip }, dead: { n: d.length, median: dm, build }, gap, pass: fails.length === 0, fails };
}
```

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `npx vitest run tests/score-bench.test.ts`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add web/src/lib/score-bench.ts web/tests/score-bench.test.ts
git commit -m "feat(web): score bench of 14 earning niches and dead-niche rule (launch S1)"
```

---

### Task 2: Bộ kiểm điểm: script + số trước khi đổi

**Files:**

- Create: `web/scripts/score-bench.ts`
- Modify: `web/package.json` (thêm script `score:bench`)
- Modify: `docs/superpowers/plans/2026-11-17-launch-1-diem-co-hoi.md` (mục Tiến độ: số trước khi đổi)

**Interfaces:**

- Consumes: `BENCH_EARNING`, `isDeadNiche`, `benchSummary`, `BenchRow` (Task 1) · `getRunView(db, id)` (`@/lib/run-view`) · `scoreV2(db, view)` · `cachedIap(db, a, country)` (`@/lib/score-v2`) · `listRuns(db, n)` (`@/lib/run-view`).
- Produces: lệnh `npm run score:bench -- --db <file> [--json <file>]`.

- [ ] **Step 1: Viết script**

```ts
// web/scripts/score-bench.ts
/**
 * npm run score:bench -- --db <bản sao niche.db> [--json out.json]
 * Chấm lại 14 niche kiếm tiền + niche chết (luật isDeadNiche) bằng code HIỆN TẠI, in bảng + đạt / trượt.
 * Chỉ đọc. Mỗi keyword lấy lượt Research US mới nhất có ít nhất 1 nguồn store xong.
 */
import { writeFileSync } from 'node:fs';
import { createDb } from '@/db/client';
import { getRunView, listRuns } from '@/lib/run-view';
import { cachedIap, scoreV2 } from '@/lib/score-v2';
import { BENCH_EARNING, benchSummary, isDeadNiche, type BenchRow } from '@/lib/score-bench';

const arg = (name: string) => { const i = process.argv.indexOf(name); return i > 0 ? process.argv[i + 1] : undefined; };
const dbPath = arg('--db');
if (!dbPath) { console.error('Thiếu --db <bản sao niche.db>'); process.exit(1); }
const db = createDb(dbPath);
const now = new Date();

const latest = new Map<string, number>();
for (const r of listRuns(db, 5000)) {
  if (r.country !== 'US' || !r.jobs.some((j) => (j.source === 'playstore' || j.source === 'appstore') && j.status === 'done')) continue;
  const prev = latest.get(r.seed);
  if (prev === undefined || r.id > prev) latest.set(r.seed, r.id);
}
const earningTerms = new Set(BENCH_EARNING.map((e) => e.term));
const rows: BenchRow[] = [];
const score = (runId: number, term: string, kind: BenchRow['kind']) => {
  const v = getRunView(db, runId);
  if (!v) return;
  const s = scoreV2(db, v);
  rows.push({ kind, term, runId, score: s.total === null ? null : Math.round(s.total * 10), decision: s.decision });
};
for (const e of BENCH_EARNING) {
  const id = latest.get(e.term);
  if (id === undefined) console.warn(`chưa có lượt Research US: ${e.term}`); else score(id, e.term, 'earning');
}
for (const [term, id] of latest) {
  if (earningTerms.has(term)) continue;
  const v = getRunView(db, id);
  if (!v) continue;
  const top = v.competitors.filter((a) => a.bestRank <= 10).map((a) => ({
    updatedAt: a.updatedAt, releasedAt: a.releasedAt, price: a.price, offersIap: a.offersIap,
    iapItems: a.store === 'appstore' ? cachedIap(db, a, v.run.country)?.length ?? null : null,
  }));
  if (isDeadNiche(top, now)) score(id, term, 'dead');
}

const sum = benchSummary(rows);
for (const k of ['earning', 'dead'] as const) {
  console.log(`\n${k === 'earning' ? 'KIẾM TIỀN' : 'CHẾT'} (${sum[k].n})`);
  for (const r of rows.filter((x) => x.kind === k).sort((a, b) => (b.score ?? -1) - (a.score ?? -1)))
    console.log(`  ${r.term.padEnd(24)} #${String(r.runId).padEnd(5)} ${String(r.score ?? '—').padStart(3)}/100  ${r.decision ?? 'chưa đủ số'}`);
}
console.log(`\nTrung vị: kiếm tiền ${sum.earning.median ?? '—'} · chết ${sum.dead.median ?? '—'} · cách biệt ${sum.gap ?? '—'}`);
console.log(sum.pass ? 'ĐẠT' : `TRƯỢT: ${sum.fails.join(' · ')}`);
const out = arg('--json');
if (out) writeFileSync(out, JSON.stringify({ at: now.toISOString(), rows, summary: sum }, null, 2));
```

Trong `web/package.json`, thêm dòng vào `scripts` (sau `"blog:research"`):

```json
"score:bench": "tsx scripts/score-bench.ts",
```

Nếu `listRuns` không trả `jobs` như trên: mở `web/src/lib/run-view.ts`, tìm `export function listRuns`, dùng đúng kiểu `RunSummary` (`{ id, seed, country, createdAt, jobs: { source, status }[] }`).

- [ ] **Step 2: Chạy thêm lượt Research còn thiếu** (anh đã cho phép ~5 lượt, 2026-11-17)

Trên app đang chạy ở cây chính (dev server, cổng xem ở `.claude/launch.json` / log), gửi:

```bash
for k in "workout tracker" "vignette" "keyboard themes" "make friends"; do
  curl -s -X POST http://127.0.0.1:<cổng>/api/research -H 'Content-Type: application/json' -d "{\"seed\":\"$k\",\"country\":\"US\",\"force\":true}"; echo; sleep 3
done
```

Chờ `sqlite3 -readonly web/data/niche.db "select count(*) from source_jobs where status in ('pending','running')"` về 0. **Không sửa file trong `web/src` của cây chính lúc đang chạy**, vì `tsx watch` khởi động lại sẽ làm lượt bị `interrupted`. Lượt nào lỗi thì gửi lại 1 lần.

- [ ] **Step 3: Chạy bộ kiểm trên bản sao DB, ghi số "trước"**

```bash
SP=$(mktemp -d)
sqlite3 -readonly niche-radar/web/data/niche.db ".backup $SP/bench.db"
npm run score:bench -- --db $SP/bench.db --json $SP/before.json
```

Expected: in đủ 14 dòng KIẾM TIỀN, có ≥ 1 dòng CHẾT, kết luận `TRƯỢT` (code cũ: B0.1 đo 8/13 bị BỎ).
Ghi số niche chết tìm được. Nếu < 15: ghi rõ "chỉ có N niche chết theo luật", **không nới luật**.
Dán bảng tóm tắt (trung vị, cách biệt, số BỎ) vào mục **Tiến độ** cuối plan này.

- [ ] **Step 4: `npm run check` ở gốc worktree, rồi commit**

```bash
git add web/scripts/score-bench.ts web/package.json docs/superpowers/plans/2026-11-17-launch-1-diem-co-hoi.md
git commit -m "feat(web): npm run score:bench to rescore earning and dead niches (launch S1)"
```

---

### Task 3: Yếu tố Cửa vào + trọng số mới

**Files:**

- Create: `web/src/lib/score-entry.ts`
- Modify: `web/src/lib/score-config.ts` (FactorKey, DEFAULT_WEIGHTS, LABEL, WEIGHT_PRESETS, `toScore100`)
- Modify: `web/src/lib/score-v2.ts` (`getWeights` đổi trọng số cũ, `factors()` thêm entry, `NEXT.entry`)
- Modify: `web/src/components/HealthIcon.tsx`, `web/src/components/NextSteps.tsx`, `web/src/lib/health-actions.ts` (khoá `entry`)
- Create: `web/src/locales/en-text-launch-score.ts`; Modify: `web/src/locales/en-text.ts`
- Test: `web/tests/score-entry.test.ts` (mới), `web/tests/health.test.ts` (sửa)

**Interfaces:**

- Consumes: `demandSupply(input, now)`, `dsInputOf(view)`, `type DsResult` (`@/lib/app-demand-supply`) · `appKey(title)` (`@/lib/app-hunt`).
- Produces: `entryScore(ds: Pick<DsResult,'young'|'withDate'>, staleSharePct: number | null): EntryScore` với `type EntryScore = { value: number | null; strong: string[]; weak: string[]; staleBonus: boolean; formula: string | null }` · `FactorKey` có thêm `'entry'` · `toScore100(total: number | null): number | null`.

- [ ] **Step 1: Viết test đỏ**

```ts
// web/tests/score-entry.test.ts
import { describe, expect, it } from 'vitest';
import { entryScore } from '@/lib/score-entry';
import { DEFAULT_WEIGHTS, toScore100, WEIGHT_PRESETS } from '@/lib/score-config';

const y = (title: string, ratingsCount: number | null) => ({ title, url: `https://x/${title}`, store: 'play' as const, releasedAt: '2026-06-01', ratingsCount, bestRank: 3, days: 160 });

describe('Cửa vào', () => {
  it('≥ 2 app mới đủ 50 rating = 10 · 1 = 7 · app mới yếu = 4 · không app mới = 1 · không ngày = chưa đo', () => {
    expect(entryScore({ young: [y('A', 900), y('B', 60)], withDate: 8 }, 10).value).toBe(10);
    expect(entryScore({ young: [y('A', 900), y('B', 10)], withDate: 8 }, 10)).toMatchObject({ value: 7, strong: ['A'], weak: ['B'] });
    expect(entryScore({ young: [y('B', 10)], withDate: 8 }, 10).value).toBe(4);
    expect(entryScore({ young: [], withDate: 8 }, 10).value).toBe(1);
    expect(entryScore({ young: [], withDate: 0 }, 10)).toMatchObject({ value: null, formula: null });
  });
  it('cùng app ở 2 store chỉ tính 1 lần', () => {
    expect(entryScore({ young: [y('Levla: Habit RPG', 300), { ...y('Levla - Habit RPG', 200), store: 'appstore' }], withDate: 6 }, 0).value).toBe(7);
  });
  it('≥ 30% app bỏ bê > 1 năm cộng 1, tối đa 10', () => {
    expect(entryScore({ young: [], withDate: 8 }, 40)).toMatchObject({ value: 2, staleBonus: true });
    expect(entryScore({ young: [y('A', 900), y('B', 60)], withDate: 8 }, 40).value).toBe(10);
    expect(entryScore({ young: [y('A', 900)], withDate: 8 }, 40).formula).toBe('1 app mới ≥ 50 rating → 7 + 1 (≥ 30% app bỏ bê) = 8');
  });
});

describe('trọng số mới', () => {
  it('mặc định cộng 100, Cửa vào nặng nhất cùng Tiền, Cạnh tranh 0', () => {
    expect(DEFAULT_WEIGHTS).toEqual({ entry: 25, money: 25, pain: 15, competition: 0, demand: 10, trend: 10, reach: 10, fit: 5 });
    for (const p of Object.values(WEIGHT_PRESETS)) {
      expect(Object.values(p.weights).reduce((a, b) => a + b, 0)).toBe(100);
      expect(p.weights.competition).toBe(0);
      expect(p.weights.entry).toBeGreaterThanOrEqual(20);
    }
  });
  it('hiện /100', () => {
    expect(toScore100(6.4)).toBe(64);
    expect(toScore100(0)).toBe(0);
    expect(toScore100(null)).toBeNull();
  });
});
```

Thêm vào `web/tests/health.test.ts` (trong `describe('Phase 20 · giải thích từng yếu tố'…)`):

```ts
  it('launch S2: trọng số đã lưu kiểu cũ (không có entry) → giữ số anh đặt, thêm entry 25, Cạnh tranh về 0', () => {
    const s = seeded();
    s.db.insert(settings).values({ key: 'score.weights', value: JSON.stringify({ money: 30, pain: 15, competition: 15, demand: 10, trend: 10, reach: 10, fit: 10 }) }).run();
    expect(getWeights(s.db)).toEqual({ entry: 25, money: 30, pain: 15, competition: 0, demand: 10, trend: 10, reach: 10, fit: 10 });
  });
  it('launch S2: có yếu tố Cửa vào; run giả không có ngày ra mắt → chưa đo, không tính', () => {
    const s = seeded();
    const sc = scoreV2(s.db, s.view());
    expect(sc.factors.find((f) => f.key === 'entry')).toMatchObject({ value: null, trust: 'chưa đo' });
  });
```

và sửa dòng import đầu file thành:

```ts
import { keywords, listingCache, runs, scoreHistory, settings, trendPoints, trendsCache } from '@/db/schema';
import { getThresholds, getWeights, healthSummary, recordScore, saveThresholds, scoreV2 } from '@/lib/score-v2';
```

- [ ] **Step 2: Chạy test, thấy đỏ**

Run: `npx vitest run tests/score-entry.test.ts tests/health.test.ts`
Expected: FAIL `Cannot find module '@/lib/score-entry'`

- [ ] **Step 3: Viết `score-entry.ts`**

```ts
// web/src/lib/score-entry.ts
/**
 * Yếu tố Cửa vào (launch S2, 2026-11-17): app MỚI (< 1 năm) vẫn leo được top 10 của keyword.
 * Bước 0 đo trên 13 niche đang kiếm tiền: phần này 18,8/25 so với 10,2/25 ở 310 lượt khác, là tín hiệu tách được nhất.
 * Ngưỡng là quy ước của ShotMatic. Hàm thuần.
 */
import { appKey } from './app-hunt';
import { DS_MIN_RATINGS, type DsResult } from './app-demand-supply';

export type EntryScore = { value: number | null; strong: string[]; weak: string[]; staleBonus: boolean; formula: string | null };

export function entryScore(ds: Pick<DsResult, 'young' | 'withDate'>, staleSharePct: number | null): EntryScore {
  const uniq = (list: DsResult['young']) => [...new Map(list.map((a) => [appKey(a.title), a.title])).values()];
  const strongApps = ds.young.filter((a) => (a.ratingsCount ?? 0) >= DS_MIN_RATINGS);
  const strong = uniq(strongApps);
  const strongKeys = new Set(strongApps.map((a) => appKey(a.title)));
  const weak = uniq(ds.young.filter((a) => !strongKeys.has(appKey(a.title))));
  if (!ds.withDate) return { value: null, strong, weak, staleBonus: false, formula: null };
  const [base, why] = strong.length >= 2 ? [10, `${strong.length} app mới ≥ 50 rating`] : strong.length === 1 ? [7, '1 app mới ≥ 50 rating']
    : weak.length ? [4, `${weak.length} app mới < 50 rating`] : [1, 'không app mới'];
  const staleBonus = (staleSharePct ?? 0) >= 30;
  const value = Math.min(10, base + (staleBonus ? 1 : 0));
  return { value, strong, weak, staleBonus, formula: `${why} → ${base}${staleBonus ? ' + 1 (≥ 30% app bỏ bê)' : ''} = ${value}` };
}
```

Nếu `appKey` có ký tự gạch / hai chấm khác nhau thì "Levla: Habit RPG" và "Levla - Habit RPG" đều thành `levla habit rpg` (xem `appKey` ở `app-hunt.ts`).

- [ ] **Step 4: Sửa `score-config.ts`**

Thay các dòng `FactorKey`, `DEFAULT_WEIGHTS`, `LABEL`, `WEIGHT_PRESETS`, rồi thêm `toScore100`:

```ts
export type FactorKey = 'entry' | 'money' | 'pain' | 'competition' | 'demand' | 'trend' | 'reach' | 'fit';
```

```ts
/** Launch S2 (2026-11-17): Cửa vào nặng nhất cùng Tiền; Cạnh tranh = 0 (thành thẻ Độ khó, không cộng / trừ điểm). */
export const DEFAULT_WEIGHTS: Record<FactorKey, number> = { entry: 25, money: 25, pain: 15, competition: 0, demand: 10, trend: 10, reach: 10, fit: 5 };
export const LABEL: Record<FactorKey, string> = lazyTr({ entry: tx('Cửa vào'), money: tx('Tiền'), pain: tx('Đau'), competition: tx('Cạnh tranh (cao = ít)'), demand: tx('Nhu cầu'), trend: tx('Xu hướng'), reach: tx('Tiếp cận khách'), fit: tx('Hợp sức mình') });
```

```ts
export const WEIGHT_PRESETS: Record<'mac' | 'ios' | 'android' | 'saas', { label: string; why: string; weights: Record<FactorKey, number> }> = lazyTr({
  mac: { label: 'Mac app', why: tx('mua đứt / ít đối thủ, Trends ít số → Tiền, Đau, Hợp sức nặng'), weights: { entry: 20, money: 25, pain: 20, competition: 0, demand: 5, trend: 5, reach: 15, fit: 10 } },
  ios: { label: 'iOS', why: tx('người dùng iOS chịu trả sub → Tiền nặng nhất'), weights: { entry: 25, money: 30, pain: 15, competition: 0, demand: 10, trend: 10, reach: 5, fit: 5 } },
  android: { label: 'Android', why: tx('thu tiền thấp hơn, sống nhờ lượng người → Nhu cầu, Tiếp cận nặng hơn'), weights: { entry: 25, money: 15, pain: 15, competition: 0, demand: 20, trend: 10, reach: 10, fit: 5 } },
  saas: { label: 'SaaS / web', why: tx('không có kệ store kéo khách → Tiếp cận khách nặng nhất cùng Tiền'), weights: { entry: 20, money: 25, pain: 20, competition: 0, demand: 10, trend: 5, reach: 15, fit: 5 } },
});
/** Hiện điểm /100 (launch S5): trong code vẫn 0–10, hiện ×10 làm tròn. */
export const toScore100 = (total: number | null) => (total === null ? null : Math.round(total * 10));
```

- [ ] **Step 5: Sửa `score-v2.ts`**

`getWeights`: trọng số lưu kiểu cũ (không có khoá `entry`) thì Cạnh tranh về 0, thêm Cửa vào mặc định:

```ts
export function getWeights(db: Db): Record<FactorKey, number> {
  const row = db.select().from(settings).where(eq(settings.key, 'score.weights')).get();
  try {
    const saved = row ? JSON.parse(row.value) as Partial<Record<FactorKey, number>> : {};
    // launch S2 (2026-11-17): bộ trọng số lưu trước khi có Cửa vào → giữ số anh đặt, Cạnh tranh thành thẻ Độ khó (0)
    const old = row && !('entry' in saved) ? { competition: 0 } : {};
    return { ...DEFAULT_WEIGHTS, ...saved, ...old };
  } catch { return DEFAULT_WEIGHTS; }
}
```

Thêm import đầu file:

```ts
import { demandSupply, dsInputOf } from './app-demand-supply';
import { entryScore } from './score-entry';
```

Trong `factors()`, ngay **trước** khối `// Tiền:`:

```ts
  // Cửa vào (launch S2): app < 1 năm leo được top 10 (2 store, gộp app trùng tên) + đối thủ bỏ bê
  const ds = demandSupply(dsInputOf(view));
  const en = entryScore(ds, s.staleSharePct);
  add('entry', en.value, 'proxy',
    en.value === null ? tr('Chưa có ngày ra mắt của app top 10 — chạy lại nguồn store')
      : en.strong.length ? tr('App mới (< 1 năm) đã leo top 10: {apps}', { apps: en.strong.slice(0, 3).join(', ') })
      : en.weak.length ? tr('Có {n} app mới trong top 10 nhưng chưa tới 50 rating', { n: en.weak.length })
      : tr('Top 10 không có app nào ra mắt dưới 1 năm'),
    en.formula?.replace(/ = [\d.]+$/, ''), [
      { label: tr('App mới ≥ 50 rating trong top 10'), value: String(en.strong.length), source: tr('ngày ra mắt + số rating trên store'), date,
        items: ds.young.filter((a) => en.strong.includes(a.title)).map((a) => ({ text: tr('{t} — {d} ngày, {r} rating', { t: a.title, d: a.days, r: (a.ratingsCount ?? 0).toLocaleString('en-US') }), url: a.url })) },
      { label: tr('App bỏ bê > 1 năm'), value: s.staleSharePct !== null ? `${s.staleSharePct}%` : tr('chưa đo'), source: tr('ngày cập nhật trên store'), date },
    ]);
```

(`add()` tự nối `= <điểm>` vào công thức, nên ta bỏ phần `= …` của `en.formula`.)

Trong `NEXT`, thêm khoá:

```ts
  entry: { missing: tx('chạy lại nguồn Google Play / App Store') },
```

- [ ] **Step 6: Thêm khoá `entry` vào 3 bảng giao diện**

`web/src/components/HealthIcon.tsx`, trong `FACTOR`:

```ts
  entry: { section: 'competitors' },
```

`web/src/components/NextSteps.tsx`, trong `ACTION`:

```ts
  entry: { anchor: 'store-results', button: 'Chạy lại nguồn store', icon: 'retry' },
```

`web/src/lib/health-actions.ts`: trong `TARGET` thêm `entry: '#competitors',`, trong `HOW` thêm:

```ts
  entry: tx('Mở bảng Đối thủ — chạy lại nguồn store nếu trống'),
```

Chạy `npx tsc --noEmit`. Còn file nào báo thiếu khoá `entry` trong `Record<FactorKey, …>` thì thêm theo cùng mẫu (mục tiêu `#competitors`, nút "Chạy lại nguồn store").

- [ ] **Step 7: Tiếng Anh**

```ts
// web/src/locales/en-text-launch-score.ts
/** Bản tiếng Anh cho launch: 1 điểm cơ hội, Cửa vào, Độ khó, Tiền (2026-11-17). Khoá = chữ tiếng Việt trong code. */
export const launchScoreEnText: Record<string, string> = {
  "Cửa vào": "Way in",
  "Chưa có ngày ra mắt của app top 10 — chạy lại nguồn store": "No release dates for the top 10 apps yet — rerun the store sources",
  "App mới (< 1 năm) đã leo top 10: {apps}": "New apps (< 1 year) already in the top 10: {apps}",
  "Có {n} app mới trong top 10 nhưng chưa tới 50 rating": "{n} new apps in the top 10, but under 50 ratings",
  "Top 10 không có app nào ra mắt dưới 1 năm": "No app in the top 10 launched in the last year",
  "App mới ≥ 50 rating trong top 10": "New apps with ≥ 50 ratings in the top 10",
  "ngày ra mắt + số rating trên store": "release date + rating count on the store",
  "{t} — {d} ngày, {r} rating": "{t} — {d} days, {r} ratings",
  "chạy lại nguồn Google Play / App Store": "rerun the Google Play / App Store sources",
};
```

Trong `web/src/locales/en-text.ts`: thêm `import { launchScoreEnText } from './en-text-launch-score';` cạnh các import khác, và `...launchScoreEnText,` vào cuối object gộp. Chữ nào đã có sẵn trong `en-text*.ts` (test báo trùng hoặc đã có) thì bỏ khỏi file mới.

- [ ] **Step 8: Chạy test, sửa test cũ lệch số**

Run: `npx vitest run tests/score-entry.test.ts tests/health.test.ts tests/i18n-text.test.ts`
Expected: PASS. Test cũ trong `health.test.ts` kiểm tổng điểm bằng công thức trọng số nên vẫn đúng. Test nào so điểm cứng (ví dụ `total` = số cụ thể) thì tính lại bằng trọng số mới và **ghi lý do trong commit**.

- [ ] **Step 9: `npm run check` ở gốc worktree, bộ kiểm, commit**

```bash
npm run score:bench -- --db $SP/bench.db --json $SP/after-s2.json
git add -A web/src web/tests
git commit -m "feat(web): add Way-in factor, new default weights, competition weight 0 (launch S2)"
```

Ghi kết quả bộ kiểm (trung vị, số BỎ, cách biệt) vào **Tiến độ**.

---

### Task 4: Thẻ Độ khó

**Files:**

- Create: `web/src/lib/difficulty.ts`
- Modify: `web/src/lib/score-v2.ts` (`scoreV2` trả thêm `difficulty`)
- Test: `web/tests/difficulty.test.ts`

**Interfaces:**

- Consumes: `titleShare(term, apps)` (`@/lib/app-hunt`) · `RunView`.
- Produces: `type DifficultyLevel = 'easy' | 'mid' | 'hard'` · `difficultyLevel(sum: number, median: number | null): DifficultyLevel | null` · `difficultyOf(view: RunView): Difficulty` với `type Difficulty = { level: DifficultyLevel | null; sum: number; median: number | null; titleShare: number | null; stalePct: number | null; biggest: { title: string; url: string; ratings: number }[] }` · `ScoreV2['difficulty']`.

- [ ] **Step 1: Test đỏ**

```ts
// web/tests/difficulty.test.ts
import { describe, expect, it } from 'vitest';
import { difficultyLevel, difficultyOf } from '@/lib/difficulty';
import type { RunView } from '@/lib/run-view';

describe('Độ khó', () => {
  it('Khó: tổng rating top 10 ≥ 1 triệu hoặc trung vị ≥ 10K · Dễ: < 50K và < 1K · còn lại Vừa', () => {
    expect(difficultyLevel(1_000_000, 200)).toBe('hard');
    expect(difficultyLevel(200_000, 10_000)).toBe('hard');
    expect(difficultyLevel(49_999, 999)).toBe('easy');
    expect(difficultyLevel(49_999, 1_000)).toBe('mid');
    expect(difficultyLevel(60_000, 500)).toBe('mid');
    expect(difficultyLevel(0, null)).toBeNull();
  });
  it('từ trang Research: top 10 theo hạng, 3 app nhiều rating nhất, % tên app chiếm keyword', () => {
    const app = (title: string, ratingsCount: number, bestRank: number) => ({ title, url: `u/${title}`, store: 'play', price: 0, offersIap: false, ratingsCount, bestRank }) as RunView['competitors'][number];
    const view = {
      run: { seed: 'habit tracker' }, stats: { topRatingsSum: { play: 30_000, appstore: 5_000 }, staleSharePct: 40 },
      competitors: [app('Habit Tracker Pro', 20_000, 1), app('Streaks', 10_000, 2), app('Loop', 4_000, 3), app('Far away', 900_000, 30)],
    } as unknown as RunView;
    expect(difficultyOf(view)).toMatchObject({
      level: 'hard', sum: 35_000, median: 10_000, stalePct: 40, // trung vị đúng 10.000 → Khó (luật "hoặc")
      biggest: [{ title: 'Habit Tracker Pro', ratings: 20_000 }, { title: 'Streaks', ratings: 10_000 }, { title: 'Loop', ratings: 4_000 }],
    });
    expect(difficultyOf(view).titleShare).toBeCloseTo(1 / 3);
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ** · Run: `npx vitest run tests/difficulty.test.ts` · Expected: FAIL module not found.

- [ ] **Step 3: Code**

```ts
// web/src/lib/difficulty.ts
/**
 * Thẻ Độ khó (launch S3, 2026-11-17): Cung của chợ, hiện CẠNH điểm cơ hội, không cộng / trừ vào điểm.
 * Bước 0: "chợ trống" thấp hơn hẳn ở niche đang kiếm tiền → đông không có nghĩa là xấu, chỉ là khó hơn.
 * Ngưỡng là quy ước của ShotMatic. Hàm thuần.
 */
import { titleShare } from './app-hunt';
import type { RunView } from './run-view';

export type DifficultyLevel = 'easy' | 'mid' | 'hard';
export type Difficulty = {
  level: DifficultyLevel | null; sum: number; median: number | null; titleShare: number | null; stalePct: number | null;
  biggest: { title: string; url: string; ratings: number }[];
};

export function difficultyLevel(sum: number, median: number | null): DifficultyLevel | null {
  if (sum === 0 && median === null) return null;
  if (sum >= 1_000_000 || (median ?? 0) >= 10_000) return 'hard';
  if (sum < 50_000 && median !== null && median < 1_000) return 'easy';
  return 'mid';
}

const median = (xs: number[]) => {
  if (!xs.length) return null;
  const s = [...xs].sort((a, b) => a - b);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m] : Math.round((s[m - 1] + s[m]) / 2);
};

export function difficultyOf(view: RunView): Difficulty {
  const top = view.competitors.filter((a) => a.bestRank <= 10);
  const sum = view.stats.topRatingsSum.play + view.stats.topRatingsSum.appstore;
  const med = median(top.flatMap((a) => (a.ratingsCount === null ? [] : [a.ratingsCount])));
  return {
    level: difficultyLevel(sum, med), sum, median: med, stalePct: view.stats.staleSharePct,
    titleShare: titleShare(view.run.seed, top.map((a) => ({ title: a.title, store: a.store, price: a.price, offersIap: a.offersIap, ratingsCount: a.ratingsCount }))),
    biggest: [...top].sort((a, b) => (b.ratingsCount ?? 0) - (a.ratingsCount ?? 0)).slice(0, 3).map((a) => ({ title: a.title, url: a.url, ratings: a.ratingsCount ?? 0 })),
  };
}
```

Trong `score-v2.ts`: `import { difficultyOf } from './difficulty';` rồi trong object `result` của `scoreV2` thêm `difficulty: difficultyOf(view),` (cạnh `v1`).

Trong `healthSummary`, thay dòng `band(v('competition'), …)` bằng `null` để câu tóm tắt không nói "cạnh tranh đông" như một điểm trừ nữa (Độ khó hiện riêng ở thẻ). Sửa test `health.test.ts` nếu có câu kỳ vọng chứa "cạnh tranh".

- [ ] **Step 4: Chạy, xanh** · Run: `npx vitest run tests/difficulty.test.ts tests/health.test.ts` · Expected: PASS.

- [ ] **Step 5: `npm run check`, bộ kiểm, commit**

```bash
npm run score:bench -- --db $SP/bench.db --json $SP/after-s3.json
git add -A web/src web/tests
git commit -m "feat(web): difficulty card next to the opportunity score (launch S3)"
```

Thêm vào output của `scripts/score-bench.ts` 1 cột `Độ khó` (`s.difficulty.level`) để xem 2 nhóm phân bố ra sao. Ghi vào **Tiến độ**: bao nhiêu niche kiếm tiền là Khó / Vừa / Dễ, bao nhiêu niche chết. Nếu gần như cả 2 nhóm đều "Khó" thì ghi lại, **không đổi ngưỡng trong task này**.

---

### Task 5: Đọc gói IAP iOS top 10 trong lượt App Store

**Files:**

- Create: `web/src/collectors/appstore-iap.ts`
- Modify: `web/src/lib/deps.ts`
- Test: `web/tests/appstore-iap.test.ts`

**Interfaces:**

- Consumes: `iosIapItems(db, appId, country, signal, fetcher)`, `fetchIapItems`, `type FetchIap` (`@/collectors/appstore-web`) · `type Collector` · `CollectorError` (`@/lib/errors`).
- Produces: `IAP_TOP = 10` · `topAppstoreIds(db, runId, n): string[]` · `withTopIap(collect: Collector, fetcher?: FetchIap): Collector`.

- [ ] **Step 1: Test đỏ**

```ts
// web/tests/appstore-iap.test.ts
import { describe, expect, it, vi } from 'vitest';
import { saveStoreHits } from '@/collectors/store-apps';
import type { Collector, StoreApp } from '@/collectors/types';
import { topAppstoreIds, withTopIap } from '@/collectors/appstore-iap';
import { createDb } from '@/db/client';
import { iapCache, keywords, runs } from '@/db/schema';
import { CollectorError } from '@/lib/errors';

function setup(n = 12) {
  const db = createDb(':memory:');
  const runId = db.insert(runs).values({ seed: 'x', country: 'US', createdAt: '2026-11-17T00:00:00Z' }).returning().get().id;
  const kw = db.insert(keywords).values({ runId, term: 'x', origin: 'seed' }).returning().get().id;
  const app = (i: number): StoreApp => ({ store: 'appstore', storeAppId: `${100 + i}`, title: `A${i}`, developer: 'd', iconUrl: null, url: `https://apps.apple.com/us/app/a/id${100 + i}`,
    genre: null, price: 0, currency: 'USD', releasedAt: null, rating: 4, ratingsCount: 10, installsMin: null, updatedAt: null, offersIap: null, iapRange: null });
  const collect: Collector = async () => saveStoreHits(db, runId, Array.from({ length: n }, (_, i) => ({ keywordId: kw, rank: i + 1, app: app(i) })));
  const ctx = { db, runId, seed: 'x', country: 'US', keywords: [{ id: kw, term: 'x' }], signal: new AbortController().signal, progress: vi.fn() };
  return { db, runId, collect, ctx };
}

describe('đọc gói IAP iOS sau nguồn App Store', () => {
  it('chỉ top 10 theo hạng, ghi cache, báo tiến độ', async () => {
    const s = setup();
    const fetcher = vi.fn(async () => [{ name: 'Pro', price: '$9.99' }]);
    await withTopIap(s.collect, fetcher)(s.ctx);
    expect(topAppstoreIds(s.db, s.runId, 10)).toHaveLength(10);
    expect(fetcher).toHaveBeenCalledTimes(10);
    expect(s.db.select().from(iapCache).all()).toHaveLength(10);
    expect(s.ctx.progress).toHaveBeenLastCalledWith(10, 10, 'đọc gói IAP');
  });
  it('429 → dừng đọc tiếp nhưng lượt App Store vẫn xong (không ném lỗi)', async () => {
    const s = setup();
    let calls = 0;
    const fetcher = vi.fn(async () => { if (++calls === 3) throw new CollectorError('RATE_LIMITED', 'apps.apple.com 429'); return []; });
    await expect(withTopIap(s.collect, fetcher)(s.ctx)).resolves.toBeUndefined();
    expect(fetcher).toHaveBeenCalledTimes(3);
    expect(s.db.select().from(iapCache).all()).toHaveLength(2);
  });
  it('lỗi mạng 1 app → bỏ app đó, đọc tiếp app sau', async () => {
    const s = setup(4);
    let calls = 0;
    const fetcher = vi.fn(async () => { if (++calls === 2) throw new CollectorError('NETWORK', 'boom'); return []; });
    await withTopIap(s.collect, fetcher)(s.ctx);
    expect(fetcher).toHaveBeenCalledTimes(4);
  });
  it('collector App Store lỗi → ném lỗi như cũ, không đọc IAP', async () => {
    const s = setup();
    const fetcher = vi.fn();
    await expect(withTopIap(async () => { throw new CollectorError('NETWORK', 'itunes down'); }, fetcher)(s.ctx)).rejects.toThrow('itunes down');
    expect(fetcher).not.toHaveBeenCalled();
  });
});
```

- [ ] **Step 2: Chạy, đỏ** · Run: `npx vitest run tests/appstore-iap.test.ts` · Expected: FAIL module not found.

- [ ] **Step 3: Code**

```ts
// web/src/collectors/appstore-iap.ts
/**
 * Launch S4 (2026-11-17): sau khi nguồn App Store tìm app xong, đọc gói IAP iOS của app top 10 (theo hạng) vào iap_cache.
 * Research App Store trước đây không biết IAP (0/19.710 lần chụp, đo 2026-11-17) → câu Tiền mù trên iOS.
 * Lỗi đọc IAP KHÔNG làm hỏng lượt App Store: 429 thì dừng đọc tiếp, lỗi 1 app thì bỏ app đó.
 */
import { sql } from 'drizzle-orm';
import type { Db } from '@/db/client';
import { CollectorError } from '@/lib/errors';
import { tr } from '@/lib/i18n';
import { fetchIapItems, iosIapItems, type FetchIap } from './appstore-web';
import type { Collector } from './types';

export const IAP_TOP = 10;

/** storeAppId của app App Store có hạng tốt nhất ≤ n ở ít nhất 1 keyword của lượt, xếp theo hạng. */
export function topAppstoreIds(db: Db, runId: number, n: number): string[] {
  return db.all<{ id: string }>(sql`SELECT a.store_app_id AS id, MIN(h.rank) AS r FROM keyword_hits h
    JOIN keywords k ON k.id = h.keyword_id AND k.run_id = ${runId}
    JOIN apps a ON a.id = h.app_id AND a.store = 'appstore'
    GROUP BY a.id HAVING r <= ${n} ORDER BY r, a.id`).map((x) => x.id);
}

export function withTopIap(collect: Collector, fetcher: FetchIap = fetchIapItems): Collector {
  return async (ctx) => {
    await collect(ctx);
    const ids = topAppstoreIds(ctx.db, ctx.runId, IAP_TOP);
    for (const [i, id] of ids.entries()) {
      if (ctx.signal.aborted) return;
      ctx.progress?.(i, ids.length, tr('đọc gói IAP'));
      try {
        await iosIapItems(ctx.db, id, ctx.country, ctx.signal, fetcher);
      } catch (e) {
        if (e instanceof CollectorError && e.code === 'RATE_LIMITED') break;
      }
    }
    ctx.progress?.(ids.length, ids.length, tr('đọc gói IAP'));
  };
}
```

`web/src/lib/deps.ts`:

```ts
import { withTopIap } from '@/collectors/appstore-iap';
// …
    collectors: { playstore: collectPlaystore, appstore: withTopIap(collectAppstore), trends: collectTrends },
```

Thêm vào `en-text-launch-score.ts`: `"đọc gói IAP": "reading in-app purchases",`.

Nếu `db.all` không có trên kiểu `Db` của repo: dùng `db.$client.prepare(…).all(runId, n)` hoặc xem cách `clearSourceData` trong `run-research.ts` gọi `db.run(sql…)`, rồi đổi sang `db.all` cùng kiểu.

- [ ] **Step 4: Chạy, xanh** · Run: `npx vitest run tests/appstore-iap.test.ts tests/run-research.test.ts` · Expected: PASS.

- [ ] **Step 5: Đo thật thời gian thêm**

Chép bản sao DB vào worktree (thư mục `web/data/` không nằm trong git): `mkdir -p web/data && cp $SP/bench.db web/data/niche.db`.
Chạy app từ worktree (`npm run dev` trong `web/` của worktree, **cổng khác** cây chính, đặt trong `.claude/launch.json`). Tra 5 keyword US (ví dụ calorie tracker, habit tracker, astrology, budget app, white noise). Ghi lại:

```bash
sqlite3 web/data/niche.db "select run_id, (julianday(finished_at)-julianday(started_at))*86400 from source_jobs where source='appstore' order by run_id desc limit 5"
```

Ghi vào **Tiến độ**: thời gian App Store trước (trung bình 12 giây, B0.3) và sau, có bao nhiêu app top 10 App Store đọc được IAP / 10.

- [ ] **Step 6: `npm run check`, commit**

```bash
git add -A web/src web/tests
git commit -m "feat(web): read iOS in-app purchases for the App Store top 10 during Research (launch S4)"
```

---

### Task 6: Công thức Tiền mới + khớp TrustMRR

**Files:**

- Create: `web/src/lib/money-score.ts`, `web/src/lib/trust-match.ts`
- Modify: `web/src/lib/score-v2.ts` (khối Tiền trong `factors()`, `payingTop10`)
- Test: `web/tests/money-score.test.ts`, `web/tests/trust-match.test.ts`, sửa `web/tests/health.test.ts`

**Interfaces:**

- Consumes: `cachedIap` (score-v2) · `parseCategory`, `type TrustCard` (`@/collectors/trustmrr`) · `trustmrrCache` (schema) · `appKey` (app-hunt).
- Produces: `parsePrice(s: string): number | null` · `moneyScore(i: MoneyIn): MoneyScore` với `type MoneyIn = { top: number; paying: number; iapMaxPrices: number[] | null; trustLast30: number[] | null }`, `type MoneyScore = { value: number | null; parts: { paying: number | null; price: number | null; trust: number | null }; formula: string | null }` · `matchTrust(term: string, topTitles: string[], cards: TrustCard[]): TrustCard[]` · `cachedTrustCards(db: Db): TrustCard[]`.

- [ ] **Step 1: Test đỏ**

```ts
// web/tests/money-score.test.ts
import { describe, expect, it } from 'vitest';
import { moneyScore, parsePrice } from '@/lib/money-score';

describe('Tiền /10 = có người trả tiền (4) + mức giá (3) + doanh thu thật (3)', () => {
  it('đọc giá gói IAP', () => {
    expect(parsePrice('$9.99')).toBe(9.99);
    expect(parsePrice('$1,299.00')).toBe(1299);
    expect(parsePrice('Free')).toBeNull();
  });
  it('đủ 3 phần', () => {
    expect(moneyScore({ top: 10, paying: 8, iapMaxPrices: [9.99, 14.99, 4.99], trustLast30: [27_000] }))
      .toMatchObject({ value: 9.2, parts: { paying: 3.2, price: 3, trust: 3 } });
  });
  it('phần chưa đo bỏ khỏi mẫu số', () => {
    const r = moneyScore({ top: 10, paying: 10, iapMaxPrices: null, trustLast30: null });
    expect(r).toMatchObject({ value: 10, parts: { paying: 4, price: null, trust: null } });
    expect(r.formula).toBe('10/10 × 4 = 4 · mức giá chưa đo · doanh thu thật chưa đo → 4/4 × 10');
  });
  it('bậc giá theo trung vị gói đắt nhất mỗi app; bậc doanh thu theo app cao nhất', () => {
    expect(moneyScore({ top: 4, paying: 0, iapMaxPrices: [0, 0, 2.99], trustLast30: [500] }).parts).toEqual({ paying: 0, price: 0, trust: 1 });
    expect(moneyScore({ top: 4, paying: 0, iapMaxPrices: [4.99, 6.99], trustLast30: [1_000, 200] }).parts).toEqual({ paying: 0, price: 2, trust: 2 });
  });
  it('không có gì để đo → chưa đo', () => {
    expect(moneyScore({ top: 0, paying: 0, iapMaxPrices: null, trustLast30: null })).toMatchObject({ value: null, formula: null });
  });
});
```

```ts
// web/tests/trust-match.test.ts
import { describe, expect, it } from 'vitest';
import { matchTrust } from '@/lib/trust-match';
import type { TrustCard } from '@/collectors/trustmrr';

const card = (slug: string, name: string, description: string, last30: number | null): TrustCard => ({ slug, name, description, mrr: null, last30, total: null, onSale: false, category: 'mobile-apps' });
const cards = [
  card('nutria', 'Nutria', 'AI Calorie Tracker.', 77_000),
  card('kb', 'Stealth Company', 'An AI keyboard theme app for iOS', 27_000),
  card('cal-zero', 'Calories Zero', 'Calorie tracker', 0),
  card('song', 'Composer.AI', 'Create AI songs', 15_000),
];

describe('khớp TrustMRR', () => {
  it('đủ chữ chính của keyword trong tên + mô tả (số nhiều như số ít), bỏ app doanh thu 0, xếp theo doanh thu', () => {
    expect(matchTrust('calorie tracker', [], cards).map((c) => c.slug)).toEqual(['nutria']);
    expect(matchTrust('keyboard themes', [], cards).map((c) => c.slug)).toEqual(['kb']);
  });
  it('tên trùng 1 app top 10 cũng khớp', () => {
    expect(matchTrust('ai song maker', ['Composer.AI'], cards).map((c) => c.slug)).toEqual(['song']);
  });
  it('keyword chỉ có chữ phụ → không khớp gì', () => {
    expect(matchTrust('best app', [], cards)).toEqual([]);
  });
});
```

- [ ] **Step 2: Chạy, đỏ** · Run: `npx vitest run tests/money-score.test.ts tests/trust-match.test.ts` · Expected: FAIL module not found.

- [ ] **Step 3: Code `money-score.ts`**

```ts
// web/src/lib/money-score.ts
/**
 * Tiền (launch S4, 2026-11-17): 3 phần, phần nào chưa đo bỏ khỏi mẫu số.
 * Bước 0: "có người trả tiền" gần như ai cũng 10/10 (Play hầu hết có IAP) → thêm mức giá + doanh thu thật để tách.
 * Ngưỡng là quy ước của ShotMatic. ShotMatic không tự ước doanh thu. Hàm thuần.
 */
export const parsePrice = (s: string): number | null => {
  const m = s.replace(/,/g, '').match(/(\d+(?:\.\d+)?)/);
  return m ? Number(m[1]) : null;
};

export type MoneyIn = { top: number; paying: number; iapMaxPrices: number[] | null; trustLast30: number[] | null };
export type MoneyScore = { value: number | null; parts: { paying: number | null; price: number | null; trust: number | null }; formula: string | null };

const r1 = (n: number) => Math.round(n * 10) / 10;
const median = (xs: number[]) => { const s = [...xs].sort((a, b) => a - b); const m = Math.floor(s.length / 2); return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
const priceTier = (p: number) => (p >= 9.99 ? 3 : p >= 4.99 ? 2 : p > 0 ? 1 : 0);
const trustTier = (v: number) => (v >= 10_000 ? 3 : v >= 1_000 ? 2 : v > 0 ? 1 : 0);

export function moneyScore(i: MoneyIn): MoneyScore {
  const paying = i.top ? r1((i.paying / i.top) * 4) : null;
  const price = i.iapMaxPrices?.length ? priceTier(median(i.iapMaxPrices)) : null;
  const trust = i.trustLast30?.length ? trustTier(Math.max(...i.trustLast30)) : null;
  const max = (paying !== null ? 4 : 0) + (price !== null ? 3 : 0) + (trust !== null ? 3 : 0);
  if (!max) return { value: null, parts: { paying, price, trust }, formula: null };
  const got = (paying ?? 0) + (price ?? 0) + (trust ?? 0);
  const value = r1((got / max) * 10);
  const bits = [
    paying !== null ? `${i.paying}/${i.top} × 4 = ${paying}` : 'có người trả tiền chưa đo',
    price !== null ? `mức giá ${price}` : 'mức giá chưa đo',
    trust !== null ? `doanh thu thật ${trust}` : 'doanh thu thật chưa đo',
  ];
  return { value, parts: { paying, price, trust }, formula: `${bits.join(' · ')} → ${r1(got)}/${max} × 10` };
}
```

- [ ] **Step 4: Code `trust-match.ts`**

```ts
// web/src/lib/trust-match.ts
/**
 * Khớp thẻ TrustMRR với keyword (launch S4): tên + mô tả có ĐỦ chữ chính của keyword, hoặc tên trùng 1 app top 10.
 * Dùng cache category có sẵn (31 category, 7 ngày), không gọi mạng. Doanh thu là số TrustMRR đã xác minh, ShotMatic không ước.
 */
import { like } from 'drizzle-orm';
import type { Db } from '@/db/client';
import { trustmrrCache } from '@/db/schema';
import { parseCategory, type TrustCard } from '@/collectors/trustmrr';
import { appKey } from './app-hunt';

const STOP = new Set(['app', 'apps', 'for', 'the', 'and', 'a', 'an', 'of', 'to', 'with', 'free', 'best', 'my', 'ai']);
const stem = (w: string) => (w.length > 3 && w.endsWith('s') && !w.endsWith('ss') ? w.slice(0, -1) : w);
const words = (s: string) => appKey(s).split(' ').filter(Boolean).map(stem);

export function matchTrust(term: string, topTitles: string[], cards: TrustCard[]): TrustCard[] {
  const need = words(term).filter((w) => !STOP.has(w));
  if (!need.length) return [];
  const tops = new Set(topTitles.map(appKey));
  const hit = cards.filter((c) => {
    if ((c.last30 ?? 0) <= 0) return false;
    const have = new Set(words(`${c.name} ${c.description}`));
    return need.every((w) => have.has(w)) || tops.has(appKey(c.name));
  });
  return [...new Map(hit.map((c) => [c.slug, c])).values()].sort((a, b) => (b.last30 ?? 0) - (a.last30 ?? 0));
}

export function cachedTrustCards(db: Db): TrustCard[] {
  return db.select().from(trustmrrCache).where(like(trustmrrCache.url, '%/category/%')).all()
    .flatMap((r) => parseCategory(r.body, r.url.split('/').pop() ?? ''));
}
```

Chữ `ai` nằm trong STOP vì gần như mọi thẻ TrustMRR đều có "AI". Nhờ vậy "ai song maker" cần `song` + `maker`, và khớp được qua tên app top 10.

- [ ] **Step 5: Nối vào `score-v2.ts`**

Thay `payingTop10` để dùng top 10 **theo hạng** (trước đây là 10 app nhiều rating nhất):

```ts
export function payingTop10(db: Db, view: RunView) {
  const top = view.competitors.filter((a) => a.bestRank <= 10);
  return { top, payingApps: top.filter((a) => a.price > 0 || a.offersIap || !!cachedIap(db, a, view.run.country)?.length) };
}
```

Thay cả khối `// Tiền:` trong `factors()` (từ `const { top, payingApps } = payingTop10(db, view);` tới hết lệnh `add('money', …)`) bằng:

```ts
  // Tiền (launch S4): có người trả tiền (4) + mức giá gói IAP iOS (3, chỉ US) + doanh thu TrustMRR cùng niche (3)
  const { top, payingApps } = payingTop10(db, view);
  const iosRead = top.filter((a) => a.store === 'appstore').map((a) => cachedIap(db, a, view.run.country)).filter((x): x is NonNullable<typeof x> => x !== undefined);
  const iapMaxPrices = view.run.country === 'US' && iosRead.length
    ? iosRead.map((items) => Math.max(0, ...items.map((it) => parsePrice(it.price) ?? 0))) : null;
  const trust = matchTrust(view.run.seed, top.map((a) => a.title), cachedTrustCards(db));
  const m = moneyScore({ top: top.length, paying: payingApps.length, iapMaxPrices, trustLast30: trust.length ? trust.map((c) => c.last30 ?? 0) : null });
  add('money', m.value, trust.length ? 'verified' : 'proxy',
    tr('{n}/{total} app top 10 thu tiền', { n: payingApps.length, total: top.length })
      + (iapMaxPrices ? tr(' · gói iOS đắt nhất (trung vị) ${p}', { p: String(Math.round(median(iapMaxPrices) * 100) / 100) }) : '')
      + (trust.length ? tr(' · TrustMRR: {x}', { x: trust.slice(0, 3).map((c) => `${c.name} $${(c.last30 ?? 0).toLocaleString('en-US')}/30d`).join(', ') }) : ''),
    m.formula, [
      { label: tr('App top 10 thu tiền'), value: `${payingApps.length}/${top.length}`, source: tr('trang store: giá, "Contains in-app purchases", gói IAP iOS đã đọc'), date, items: payingApps.map(appItem) },
      { label: tr('Gói IAP iOS đã đọc'), value: tr('{n}/{t} app App Store', { n: iosRead.length, t: top.filter((a) => a.store === 'appstore').length }), source: tr('trang apps.apple.com (chỉ chấm giá khi nước là US)'), date },
      ...(trust.length ? [{ label: tr('Doanh thu thật cùng niche (TrustMRR)'), value: trust.map((c) => `${c.name} $${(c.last30 ?? 0).toLocaleString('en-US')}`).join(' · '), source: tr('trustmrr.com, doanh thu 30 ngày đã xác minh'), date: null,
        items: trust.map((c) => ({ text: c.name, url: `https://trustmrr.com/startup/${c.slug}` })) }] : []),
    ]);
```

Thêm import đầu file `score-v2.ts`:

```ts
import { moneyScore, parsePrice } from './money-score';
import { cachedTrustCards, matchTrust } from './trust-match';
```

và 1 hàm `median` nhỏ cạnh `clamp` (hoặc import từ `@/lib/stats` nếu có `median` số thực):

```ts
const median = (xs: number[]) => { const s = [...xs].sort((a, b) => a - b); const m = Math.floor(s.length / 2); return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
```

`add()` tự nối `= <điểm>` vào công thức: truyền `m.formula` như trên, công thức hiện ra kiểu `8/10 × 4 = 3.2 · mức giá 3 · doanh thu thật chưa đo → 6.2/7 × 10 = 8.9`.

Bỏ import `getAiResult … TrustRow` nếu không còn dùng (lint sẽ báo).

Thêm tiếng Anh vào `en-text-launch-score.ts`:

```ts
  "{n}/{total} app top 10 thu tiền": "{n}/{total} top-10 apps charge money",
  " · gói iOS đắt nhất (trung vị) ${p}": " · priciest iOS plan (median) ${p}",
  " · TrustMRR: {x}": " · TrustMRR: {x}",
  "App top 10 thu tiền": "Top-10 apps that charge",
  "Gói IAP iOS đã đọc": "iOS in-app purchases read",
  "{n}/{t} app App Store": "{n}/{t} App Store apps",
  "trang apps.apple.com (chỉ chấm giá khi nước là US)": "apps.apple.com pages (price only scored for US)",
  "Doanh thu thật cùng niche (TrustMRR)": "Real revenue in this niche (TrustMRR)",
  "trustmrr.com, doanh thu 30 ngày đã xác minh": "trustmrr.com, verified last-30-day revenue",
```

(Chữ nào test báo đã có ở file en-text khác thì bỏ khỏi file mới.)

- [ ] **Step 6: Sửa test Tiền cũ**

Trong `health.test.ts`, test "mỗi yếu tố đã đo có công thức…" đang kỳ vọng `money.formula` là `'2/6 × 7 = 2.3'`. Run giả có 6 app hạng 1–6, App Store chưa đọc IAP, `offersIap` Play = true cho app 0 và 2. Kỳ vọng mới:

```ts
    expect(money.formula).toBe('2/6 × 4 = 1.3 · mức giá chưa đo · doanh thu thật chưa đo → 1.3/4 × 10 = 3.3');
    expect(money.inputs![0].items!.map((x) => x.text)).toEqual(['App 2', 'App 0']); // đối thủ xếp theo số rating
```

(Nếu thứ tự `items` đổi do lọc theo hạng, sửa kỳ vọng thứ tự cho khớp. Ghi lý do trong commit.)

- [ ] **Step 7: Chạy, xanh** · Run: `npx vitest run tests/money-score.test.ts tests/trust-match.test.ts tests/health.test.ts tests/i18n-text.test.ts` · Expected: PASS.

- [ ] **Step 8: `npm run check`, bộ kiểm, commit**

```bash
npm run score:bench -- --db $SP/bench.db --json $SP/after-s4.json
git add -A web/src web/tests
git commit -m "feat(web): money factor from paying share, iOS plan price and TrustMRR revenue (launch S4)"
```

Bộ kiểm chạy trên bản sao DB **chưa có** IAP iOS của các lượt cũ (chỉ 407 app trong cache). Muốn đo đúng thì sau Task 5, chạy lại 14 niche kiếm tiền bằng app ở worktree (Step 5 Task 5) rồi mới bench. Ghi số vào **Tiến độ**.

---

### Task 7: Chỉnh trọng số theo bộ kiểm

**Files:**

- Modify: `web/src/lib/score-config.ts` (chỉ `DEFAULT_WEIGHTS` + `WEIGHT_PRESETS` nếu cần)
- Modify: `web/tests/score-entry.test.ts` (kỳ vọng trọng số)
- Modify: plan này (Tiến độ), `docs/web/launch-app-spec.md` (bảng trọng số, nếu đổi)

**Interfaces:** không đổi kiểu.

- [ ] **Step 1: Chạy bộ kiểm với code Task 3–6**

```bash
npm run score:bench -- --db $SP/bench.db --json $SP/tune-0.json
```

- [ ] **Step 2: Đạt thì sang Task 8.** Không đạt thì đổi **trọng số**, không đổi ngưỡng. Mỗi lần chỉ đổi 1 thứ, chạy lại, ghi 1 dòng vào Tiến độ: đổi gì → trung vị kiếm tiền / chết / số BỎ.
  Thứ tự thử: (a) Cửa vào 25 → 30, Đau 15 → 10 · (b) Tiền 25 → 30, Nhu cầu 10 → 5. Tổng luôn = 100.
- [ ] **Step 3: Vẫn trượt sau 2 lần thử** → **dừng, báo anh** với bảng số (không tự nới ngưỡng, không tự sửa luật niche chết).
- [ ] **Step 4: Sửa test trọng số, `npm run check`, commit**

```bash
git add -A web/src web/tests docs
git commit -m "feat(web): tune default weights against the score bench (launch S2)"
```

---

### Task 8: Hiện /100 + thẻ Độ khó trên giao diện

**Files:**

- Modify: `web/src/lib/health-presentation.ts` (`scoreText`, `scoreWidth`)
- Modify: `web/src/components/HealthBlock.tsx` (/100, ngưỡng ×10, ẩn yếu tố trọng số 0, thẻ Độ khó, ⓘ "đo gì / không đo gì")
- Modify: `web/src/components/AnswerRow.tsx`, `RunHeader.tsx`, `NicheMentions.tsx`, `TrackingBlock.tsx`, `HuntPickCard.tsx`, `HuntCandidateList.tsx` (điểm tổng /100)
- Create: `web/src/components/DifficultyCard.tsx`
- Test: `web/tests/health-presentation.test.ts` (sửa)

**Interfaces:**

- Consumes: `toScore100` (Task 3) · `Difficulty`, `DifficultyLevel` (Task 4) · `ScoreV2['difficulty']` qua API `/api/runs/:id/health` (kiểu `Health.score` trong `HealthBlock.tsx`).
- Produces: `<DifficultyCard d={Difficulty} />`.

- [ ] **Step 1: Test đỏ cho cách hiện**

Trong `web/tests/health-presentation.test.ts`, thay 2 dòng `scoreText` bằng:

```ts
    expect(scoreText(null)).toBe('Chưa đủ dữ liệu');
    expect(scoreText(0)).toBe('0');
    expect(scoreText(6.4)).toBe('64');
    expect(scoreText(5.55)).toBe('56');
```

Run: `npx vitest run tests/health-presentation.test.ts` · Expected: FAIL (`'6.4'` ≠ `'64'`).

- [ ] **Step 2: Sửa `health-presentation.ts`**

```ts
import { toScore100 } from './score-config';
// …
export const scoreText = (total: number | null) => (total === null ? tr('Chưa đủ dữ liệu') : `${toScore100(total)}`);
```

`scoreWidth` giữ nguyên (`total * 10` đã là %). Chạy lại test: PASS.

- [ ] **Step 3: `DifficultyCard.tsx`**

```tsx
// web/src/components/DifficultyCard.tsx
import type { Difficulty, DifficultyLevel } from '@/lib/difficulty';
import { lazyTr, tr, tx } from '@/lib/i18n';
import { InfoTip } from './InfoTip';

const LEVEL: Record<DifficultyLevel, { text: string; cls: string }> = lazyTr({
  easy: { text: tx('Dễ'), cls: 'bg-emerald-50 text-emerald-700' },
  mid: { text: tx('Vừa'), cls: 'bg-amber-50 text-amber-800' },
  hard: { text: tx('Khó'), cls: 'bg-rose-50 text-rose-700' },
});

/** Thẻ Độ khó (launch S3): cạnh điểm cơ hội, không cộng / trừ vào điểm. Bấm mở 3 dòng "khó vì sao". */
export function DifficultyCard({ d }: { d: Difficulty }) {
  const lv = d.level ? LEVEL[d.level] : null;
  return (
    <details className="rounded-xl border border-zinc-200 bg-surface px-4 py-3">
      <summary className="flex cursor-pointer list-none items-center gap-2 text-sm">
        <span className="font-semibold text-zinc-900">{tr('Độ khó')}</span>
        <span className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-semibold ${lv?.cls ?? 'bg-zinc-100 text-zinc-500'}`}>{lv?.text ?? tr('chưa đo')}</span>
        <InfoTip label={tr('Độ khó tính thế nào?')}>
          {tr('Khó: tổng rating top 10 ≥ 1 triệu hoặc rating trung vị ≥ 10.000 · Dễ: tổng < 50.000 và trung vị < 1.000 · còn lại Vừa. Không cộng hay trừ vào điểm cơ hội: chợ đông vẫn có thể đang kiếm tiền. Ngưỡng là quy ước của ShotMatic.')}
        </InfoTip>
        <span aria-hidden className="ml-auto text-zinc-400">⌄</span>
      </summary>
      <ul className="mt-2 space-y-1 text-sm text-zinc-700">
        <li>{tr('Nhiều rating nhất:')} {d.biggest.length ? d.biggest.map((a, i) => (
          <span key={a.url}>{i ? ' · ' : ''}<a className="text-[var(--accent)] hover:underline" href={a.url} target="_blank" rel="noreferrer">{a.title}</a> {a.ratings.toLocaleString('en-US')}</span>
        )) : '—'}</li>
        <li>{tr('Tên app đã chiếm keyword: {p}', { p: d.titleShare === null ? tr('chưa đo') : `${Math.round(d.titleShare * 100)}%` })}</li>
        <li>{tr('App bỏ bê > 1 năm (chỗ hở): {p}', { p: d.stalePct === null ? tr('chưa đo') : `${d.stalePct}%` })}</li>
      </ul>
    </details>
  );
}
```

- [ ] **Step 4: Sửa `HealthBlock.tsx`**

1. Kiểu `Health.score`: thêm `difficulty: import('@/lib/difficulty').Difficulty;` (hoặc `import type { Difficulty } from '@/lib/difficulty'`).
2. Hai chỗ `<span …>/10</span>` cạnh `scoreText(s.total)` (dòng ~147 và ~165) → `/100`.
3. Ngay dưới dải kết luận (sau khối `{!free && <div className={…tone.band}>…</div>}`) và cả trong khối `free`: thêm `<DifficultyCard d={s.difficulty} />`.
4. Bong bóng "Điểm tính thế nào?": dòng ngưỡng đổi thành `tr('BUILD ≥ {b} · TEST THÊM ≥ {t} · dưới là BỎ', { b: s.thresholds.build * 10, t: s.thresholds.test * 10 })`, và thêm 1 dòng:
   `<span className="block">{tr('ShotMatic không có số lượt tìm, lượt tải hay lịch sử hạng. Thay vào đó: gợi ý store, Google Trends, app mới leo được và doanh thu có nguồn.')}</span>`
5. Danh sách yếu tố: `s.factors.map` → `s.factors.filter((f) => s.weights[f.key] > 0).map`. Hai chỗ `s.factors.length` trong "Dựa trên {n}/{t} yếu tố" và `measured` cũng lọc theo `s.weights[f.key] > 0`.

Mở API trả `health` (tìm `scoreV2(` trong `web/src/server/app.ts`). Nếu API trả nguyên kết quả `scoreV2` thì `difficulty` tự có. Nếu API chọn từng trường, thêm `difficulty`.

- [ ] **Step 5: Các chỗ khác đang ghi "/10" cho điểm tổng**

Với mỗi chỗ dưới đây: lần ngược nguồn số, **chỉ sửa khi đó là `scoreV2().total`**. Điểm từng yếu tố (0–10) giữ "/10".

| File | Dòng (khoảng) | Sửa |
|---|---|---|
| `AnswerRow.tsx` | 40, 88 | vòng tô `score / 10` giữ (đúng %), số hiện `toScore100(score)`, nhãn `/100`. Dòng 112 là điểm yếu tố, **giữ** |
| `RunHeader.tsx` | 151 | `{toScore100(answer.score)}/100` |
| `NicheMentions.tsx` | 32–34 | `tr('Điểm {s}/100', { s: toScore100(c.score) })`, `{toScore100(c.score)}/100` |
| `TrackingBlock.tsx` | 86, 108 | `{score}/10` → `/100` với `toScore100(...)` (chuỗi `tr` mới: `'{term}: {score}/100, {n} đối thủ'`, `'điểm {s}/100 · {c} đối thủ · {k} keyword'`) |
| `HuntPickCard.tsx` | 22–29 | số `toScore100(score)`, `/100`, `aria-label` `tr('Điểm {s}/100', …)`. Vòng `score / 10` giữ |
| `HuntCandidateList.tsx` | 48 | `toScore100(c.score)` + `/100` |

Chuỗi `tr()` cũ không còn dùng thì để nguyên trong `en-text` (không hại). Chuỗi mới thêm vào `en-text-launch-score.ts`:

```ts
  "Độ khó": "Difficulty",
  "Dễ": "Easy", "Vừa": "Medium", "Khó": "Hard",
  "Độ khó tính thế nào?": "How is difficulty measured?",
  "Khó: tổng rating top 10 ≥ 1 triệu hoặc rating trung vị ≥ 10.000 · Dễ: tổng < 50.000 và trung vị < 1.000 · còn lại Vừa. Không cộng hay trừ vào điểm cơ hội: chợ đông vẫn có thể đang kiếm tiền. Ngưỡng là quy ước của ShotMatic.": "Hard: top-10 ratings total ≥ 1 million or median ≥ 10,000 · Easy: total < 50,000 and median < 1,000 · otherwise Medium. It doesn't add to or subtract from the opportunity score: a crowded market can still be making money. Thresholds are ShotMatic's own convention.",
  "Nhiều rating nhất:": "Most ratings:",
  "Tên app đã chiếm keyword: {p}": "App names already using the keyword: {p}",
  "App bỏ bê > 1 năm (chỗ hở): {p}": "Apps abandoned > 1 year (the gap): {p}",
  "ShotMatic không có số lượt tìm, lượt tải hay lịch sử hạng. Thay vào đó: gợi ý store, Google Trends, app mới leo được và doanh thu có nguồn.": "ShotMatic has no search volume, downloads or rank history. Instead: store suggestions, Google Trends, new apps breaking in, and sourced revenue.",
  "Điểm {s}/100": "Score {s}/100",
  "{term}: {score}/100, {n} đối thủ": "{term}: {score}/100, {n} competitors",
  "điểm {s}/100 · {c} đối thủ · {k} keyword": "score {s}/100 · {c} competitors · {k} keywords",
```

(Chữ nào đã có sẵn thì bỏ.)

- [ ] **Step 6: `npm run check` xanh**

- [ ] **Step 7: Xem tận mắt**

Chạy app worktree (cổng khác cây chính, DB là `web/data/niche.db` của worktree, chép từ bản sao ở Task 5). Mở trang Research của 3 lượt: 1 niche kiếm tiền "Khó" (ai photo editor), 1 niche "Dễ" (height increase hoặc no contact), 1 niche chết từ Task 2. Soát:

- 960px và 1340px, sáng + tối, English + tiếng Việt.
- Điểm hiện `/100`, thẻ Độ khó mở / gập được, không còn hàng "Cạnh tranh", có hàng "Cửa vào".
- Bản Free (đăng xuất PRO hoặc `isFree`): thấy điểm + Độ khó, không thấy BUILD / TEST / BỎ.
- Không cuộn ngang cả trang.

Chụp screenshot, Read từng ảnh.

- [ ] **Step 8: Commit**

```bash
git add -A web/src web/tests
git commit -m "feat(web): show the opportunity score out of 100 with a difficulty card (launch S5)"
```

---

### Task 9: MCP + export + Explorer + Keyword Intelligence: 1 điểm

**Files:**

- Modify: `web/src/mcp/niche-card.ts`, `web/src/mcp/tools.ts` (trả `score100`, `difficulty`, `formulaVersion`)
- Modify: `web/src/lib/export/dataset.ts` (cột `score100`)
- Modify: `web/src/components/ExploreDashboard.tsx` (nhãn v1 → "ước sơ bộ")
- Modify: `web/src/components/KeywordIntel.tsx` (nhãn → "điểm keyword (ASO)")
- Test: test MCP / export có sẵn (`tests/mcp*.test.ts`, `tests/export*.test.ts`), sửa kỳ vọng

**Interfaces:**

- Consumes: `toScore100`, `ScoreV2['difficulty']`.
- Produces: MCP niche card có thêm `score100: number | null`, `difficulty: 'easy'|'mid'|'hard'|null`, `formulaVersion: '2026-11'`.

- [ ] **Step 1: Test đỏ**

Trong test MCP niche card có sẵn (`grep -ln "niche-card\|get_niche_card" web/tests`), thêm kỳ vọng:

```ts
    expect(card).toMatchObject({ formulaVersion: '2026-11' });
    expect(card.score100 === null || (card.score100 >= 0 && card.score100 <= 100)).toBe(true);
    expect(['easy', 'mid', 'hard', null]).toContain(card.difficulty);
```

Run test đó → FAIL.

- [ ] **Step 2: Code**

Ở chỗ `niche-card.ts` gọi `scoreV2(db, view)` (gán vào `sc`), thêm vào object trả về:

```ts
    score100: toScore100(sc.total),
    difficulty: sc.difficulty.level,
    formulaVersion: '2026-11',
```

Mô tả tool trong `tools.ts` (chuỗi mô tả của `get_niche_card` / `get_decision`): thêm câu `score100 is the opportunity score out of 100 (formula 2026-11: Way-in weighted highest; competition shown as difficulty, not subtracted).`

`export/dataset.ts`: chỗ xuất cột điểm v2, thêm cột `score100` ngay sau.

`ExploreDashboard.tsx`: tìm chỗ hiện `opportunity` / điểm v1. Đổi nhãn thành `tr('ước sơ bộ')`, kèm `InfoTip`: `tr('Chỉ từ độ hot + độ đông (Cầu + Cung). Research keyword để có điểm cơ hội đủ 7 câu.')`. Bỏ chữ "/100" nếu có.

`KeywordIntel.tsx` (dòng ~30, nhãn `/10`): tiêu đề điểm đổi thành `tr('điểm keyword (ASO)')`.

Tiếng Anh: `"ước sơ bộ": "rough estimate"`, `"Chỉ từ độ hot + độ đông (Cầu + Cung). Research keyword để có điểm cơ hội đủ 7 câu.": "Only from popularity + crowding (demand + supply). Research the keyword for the full opportunity score."`, `"điểm keyword (ASO)": "keyword score (ASO)"`.

- [ ] **Step 3: Chạy test, `npm run check`, commit**

```bash
git add -A web/src web/tests
git commit -m "feat(web): one opportunity score in MCP, export, Explorer and keyword intel (launch S5)"
```

---

### Task 10: Săn app: điểm Săn app thành "lọc nhanh"

> **Chờ:** `web/src/client/AppHunt.tsx`, `web/src/lib/app-hunt.ts`, `app-hunt-run.ts` đang có thay đổi chưa commit của phiên khác (mục 26, 32). Chỉ làm task này **sau khi** các thay đổi đó đã vào `main`. Rebase nhánh lên `main` trước khi bắt đầu.

**Files:**

- Modify: `web/src/client/AppHunt.tsx` (thẻ kết quả)
- Modify: `web/src/lib/app-hunt-run.ts` (kết quả có `runId` → điểm chính)
- Test: `web/tests/app-hunt.test.ts`

**Interfaces:**

- Consumes: `scoreV2`, `toScore100`, `getRunView`.
- Produces: `HuntResult.main: { score100: number | null; difficulty: DifficultyLevel | null } | null`.

- [ ] **Step 1: Test đỏ**: trong test chạy Săn app có sẵn (có run Research giả), kỳ vọng `result.main` khác null khi lượt Research đã xong và `main.score100` = `toScore100(scoreV2(db, view).total)`.
- [ ] **Step 2: Code** (`app-hunt-run.ts`, chỗ dựng `HuntResult` sau khi Research xong):

```ts
      const view = getRunView(db, runId);
      const sc = view ? scoreV2(db, view) : null;
      const main = sc ? { score100: toScore100(sc.total), difficulty: sc.difficulty.level } : null;
```

  `AppHunt.tsx`: số lớn trên thẻ = `main.score100` + "/100" + chip Độ khó. Điểm Săn app cũ: bỏ số "/100", đổi thành dòng nhỏ `tr('Lọc nhanh: {n}', { n })` kèm `InfoTip` `tr('Chỉ dùng để xếp hàng ở bước lọc. Điểm cơ hội là số lớn, tính từ lượt Research.')`. Thứ tự xếp vẫn theo điểm Săn app (bước lọc).
- [ ] **Step 3: Tiếng Anh, `npm run check`, xem tận mắt 1 lượt Săn app thật ở 1340px, commit**

```bash
git commit -am "feat(web): app hunt shows the main opportunity score, hunt score becomes a quick filter (launch S5)"
```

---

### Task 11: Build, kiểm cuối, tài liệu

**Files:**

- Modify: `CHANGELOG.md` (1 dòng Web dưới `[Unreleased]`)
- Modify: `docs/web/launch-app-spec.md` (chip trạng thái, kết quả bộ kiểm), `docs/web/launch-app-market.md`, plan này (Tiến độ)

- [ ] **Step 1:** `npm run check` + `npm run docs:build` xanh.
- [ ] **Step 2:** Trong `web/`: `npm run build` → `npm start` (cổng khác cây chính nếu đang chạy). Mở được, không lỗi console.
- [ ] **Step 3:** Chạy `npm run score:bench` lần cuối trên bản sao DB **mới** (sau khi đã có IAP iOS cho 14 niche). Dán bảng vào spec, mục "Đo xong khi".
  Đạt cả 3: 0/14 BỎ · cách biệt ≥ 15 · 0 niche chết BUILD. Thêm: % app top 10 App Store biết IAP (mục tiêu ≥ 80%).
- [ ] **Step 4:** CHANGELOG dòng: `- **Web** · 1 điểm cơ hội /100: thêm Cửa vào (app mới leo được), Độ khó tách khỏi điểm, Tiền đọc gói IAP iOS + TrustMRR; npm run score:bench (launch S1–S5).`
- [ ] **Step 5:** Commit docs, rồi **hỏi anh**: merge vào `main` hay mở PR (theo `superpowers:finishing-a-development-branch`).

---

### Task 12: Gom phần app đang dở (S6), không phải code mới

> Làm ở **cây chính**, chỉ khi phiên sở hữu từng phần đã xong và đồng ý. Không commit thay phiên khác khi phiên đó còn đang chạy.

- [ ] Mỗi phần: mục 26 Điểm yếu đối thủ · 28 Cài đặt dữ liệu · Soi app cùng studio + tương tự · Tìm app + Tóm tắt app + Bản gọn · 32 Trends trong 3 thẻ App.
  Xem `git diff` đúng file của phần đó → `npm run check` → mở xem tận mắt → commit riêng.
- [ ] Mục 27 Review Mining đã commit (e49df96), chưa push: hỏi anh có push không.
- [ ] Mục 16 Trang Project: **để sau launch**, giữ nhánh (anh chốt 2026-11-17).
- [ ] Mục 29, 31, 32 (Săn theo app): spec mới, **để sau launch**, trừ khi anh đổi.

---

## Tiến độ

- 2026-11-17 · Viết plan. Chưa bắt đầu Task 1.
- 2026-11-17 · Task 2 (số trước khi đổi, code cũ, `npm run score:bench`): 14/14 niche kiếm tiền có lượt Research US (đã chạy thêm #340 workout tracker, #341 vignette, #342 keyboard themes, #343 make friends). Trung vị kiếm tiền 44/100, niche chết chưa có (cách biệt —). 6/14 niche kiếm tiền bị BỎ (iptv player, height increase, astrology, keyboard themes, no contact, sports betting picks); 8 còn lại TEST THÊM (cao nhất vignette 56, thấp nhất workout tracker 42). Kết quả TRƯỢT.
- Niche chết theo luật isDeadNiche: chỉ có 0 niche chết (không nới luật), nên chưa đo được cách biệt. Cần thêm Research các niche chết ở bước sau. Bản sao DB + before.json ở `.superpowers/sdd/bench/` trong worktree.
- 2026-11-17 · Task 3 (Cửa vào + trọng số mới, commit 08027bf trên launch-1-diem-co-hoi, bench trên cùng bản sao DB): trung vị kiếm tiền 44 → 57/100; số BỎ 6/14 → 0/14 (4 BUILD: depuff 73, ai song maker 68, vignette 66, iptv player 62; ai photo editor 79 vẫn TEST THÊM; cao nhất 79, thấp nhất no contact 45). Niche chết vẫn 0 → cách biệt chưa đo (xử lý ở Task 7). after-s2.json ở `.superpowers/sdd/bench/`.
- 2026-11-17 · Task 4 (thẻ Độ khó, `web/src/lib/difficulty.ts`, bench trên cùng bản sao DB): kiếm tiền 14 niche → Khó 10 · Vừa 3 (depuff, vignette, height increase) · Dễ 1 (no contact). Niche chết vẫn 0 → không có số chết để so. Khó chiếm 10/14 nên gần như cả nhóm kiếm tiền đều Khó: ghi lại, **không đổi ngưỡng** (ngưỡng giữ nguyên). after-s3.json ở `.superpowers/sdd/bench/`.
- 2026-11-17 · Task 5 (đọc IAP iOS top 10 trong job App Store, `withTopIap` ở deps): code + test xong (test dùng fetcher giả, không gọi mạng). Bước 5 (đo thời gian thêm / số app đọc được IAP trên app thật): chưa đo, chờ chạy thật.
- 2026-11-17 · Task 5 bước 5 (đo thật trên app worktree, bản sao DB): "top 10" = app có hạng ≤ 10 ở **ít nhất 1 keyword** của lượt → 18–27 app/lượt (5 keyword), không phải 10. Đọc được IAP **100%** số app đó ở cả 6 lượt (#344–#349), không gặp 429; 13–24 app/lượt có ít nhất 1 gói IAP. Thời gian job App Store khi chạy **một mình** (#349 sleep sounds, 23 app đọc IAP): **40,1 giây**, so với trung bình 12 giây (B0.3) → thêm khoảng 28 giây/lượt. 5 lượt #344–#348 chạy cùng lúc nên số giây (185–264) không dùng để so.
- 2026-11-17 · Task 6 (công thức Tiền mới + khớp TrustMRR, commit 0bc91e0 + ed9613b). Trước khi bench: đọc IAP iOS cho app hạng ≤ 10 (mọi keyword) của lượt US mới nhất của 14 niche kiếm tiền, ghi vào iap_cache của DB worktree (không tạo lượt mới): đọc được 100%, 0 lỗi, 0 lần 429. Bench (`--db web/data/niche.db` của worktree): trung vị kiếm tiền **76/100**, BỎ **0/14**, BUILD 12/14. 2 TEST THÊM: ai photo editor 89 (bị cờ "loại app bão hoà 4.3" giữ lại, đúng luật), sports betting picks 56. Niche chết vẫn 0 → TRƯỢT vì chưa có nhóm chết. Lo: điểm nhóm kiếm tiền lên cao có thể do "nâng tất cả" → cần nhóm chết trước khi chỉnh trọng số (Task 7). after-s4.json ở `.superpowers/sdd/bench/`.
- 2026-11-17 · Nhóm chết (brief câu 3, anh đã chốt "mình tự chọn ~15 keyword, ghi cách chọn"): luật isDeadNiche không thấy niche nào trong 309 lượt cũ → chạy Research US cho 15 keyword trào lưu đã tắt / nền tảng đã chết (fidget spinner, pokemon go radar, flappy bird, harlem shake, ice bucket challenge, mannequin challenge, bottle flip, vine downloader, windows phone theme, blackberry messenger, google plus, ios 7 wallpapers, dubsmash, yik yak, pokemon go map). Chỉ keyword nào qua đúng luật isDeadNiche mới vào nhóm chết, không nới luật.
- 2026-11-17 · Kết quả 15 keyword trào lưu (#350–#364, tất cả nguồn xong, 0 lỗi): **0/15 qua luật isDeadNiche**. Store không trả app chết cho keyword cũ: app bỏ bê > 1 năm chỉ 7–55%, keyword nào cũng có 8–40 app thu tiền và 1–8 app dưới 1 năm trong top 10. → Luật "chết" (≥ 70% bỏ bê, không ai thu tiền, không app mới) **không có trong dữ liệu thật**. Điểm của 15 keyword: trung vị **52/100** (36–74) so với kiếm tiền 76 → cách biệt 24 nếu coi 15 keyword này là nhóm chết. Nhưng 4/15 vẫn được BUILD: windows phone theme 74, vine downloader 69, fidget spinner 66, yik yak 60. Cả 4 có Cửa vào 10 hoặc Tiền cao, trong khi Cầu chỉ 0,4–5. Chờ anh chọn cách làm nhóm chết trước khi chỉnh trọng số.
