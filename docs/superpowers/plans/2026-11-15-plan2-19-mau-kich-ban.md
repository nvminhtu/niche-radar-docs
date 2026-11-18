# Plan 2 · 19 · Soi kênh: làm theo kênh bằng mẫu kịch bản — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Soi 1 kênh hiện tiêu đề video đúng ngôn ngữ của nước đã chọn, và có khối **Làm theo kênh**: tick video đã chứng minh → đọc phụ đề → ✦ ra 1 mẫu kênh + ✦ 1 mẫu cốt truyện cho mỗi video, lưu trong app, copy Markdown.

**Architecture:**
(A) Collector đọc thêm tab Videos bằng 1 phiên InnerTube nói ngôn ngữ của nước (`lang = hl`), chỉ lấy `id → tiêu đề`, ghép đè lên danh sách đọc bằng phiên tiếng Anh (số view / ngày đăng vẫn đọc tiếng Anh).
(B) Hàm thuần `lib/story-template.ts` (chọn sẵn video, 2 câu hỏi AI, ghép Markdown) + component `client/ChannelTemplates.tsx`. Lưu mẫu bằng `magic-notes` có sẵn (2 task + 2 kiểu scope mới), đi đúng luồng ✦ → khung Hỏi AI → nháp → Dùng / Bỏ / Hỏi lại. Nâng giới hạn câu hỏi chat từ 4000 lên 12000 ký tự (câu hỏi đi qua stdin, không vướng giới hạn dòng lệnh).

**Tech Stack:** TypeScript, youtubei.js (InnerTube), Hono, React, Tailwind v4, Vitest.

Spec: `docs/web/phase-plan2-19-mau-kich-ban.md`.

## Global Constraints

- **Bắt đầu sau khi mục 18 đã commit.** Mục 18 đang sửa chưa commit đúng các file `web/src/collectors/youtube-channel.ts` và `web/src/client/YoutubeChannel.tsx`. Chạy `git status` ở gốc repo; còn file `M` của mục 18 thì dừng, báo anh.
- Mọi chữ trong `tr('…')` / `tx('…')` phải có bản tiếng Anh trong `web/src/locales/en-text-social.ts` (test `tests/i18n-text.test.ts` đỏ nếu thiếu), giữ đúng `{biến}`.
- Không bịa số: số đo ghi kèm ngày, chưa đo ghi `chưa đo`.
- Chọn sẵn = × kênh ≥ 1 **và** `ageDays` ≥ 7 (`BASE_MIN_AGE_DAYS`); tối đa 10 video (`TRANSCRIPT_BATCH_MAX`).
- Câu hỏi AI viết tiếng Anh (như các câu ✦ khác), yêu cầu AI trả lời bằng ngôn ngữ giao diện app; câu trích phụ đề giữ tiếng gốc; không viết kịch bản đầy đủ.
- Layout: đứng được từ 960px tới 1920px, không cuộn ngang cả trang; mặt thẻ `bg-surface`, màu xám `zinc-*`; soát cả sáng + tối, cả tiếng Việt + English.
- Trước khi xong: `npm run check` ở gốc repo xanh; `npm run docs:build` xanh.
- Commit: `feat(web): …` / `docs(web): …` chữ thường tiếng Anh, kết bằng dòng `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Chỉ `git add` đúng file của task.

## File structure

| File | Việc |
|---|---|
| `web/src/collectors/youtube.ts` | thêm `ytLocalSession(gl)` (phiên InnerTube `lang = hl`) |
| `web/src/collectors/youtube-channel.ts` | `channelFull(id, gl)`, `localTitles`, `withLocalTitles`, `needsLocalTitles`, ghép trong `collectChannelAudit` |
| `web/src/lib/ai/magic-notes.ts` | task `channel-template` / `story-template`, scope `ytchannel:` / `ytvideo:` |
| `web/src/server/app.ts` | giới hạn câu hỏi chat 4000 → 12000 (`CHAT_MAX`) |
| `web/src/lib/story-template.ts` (mới) | `isProven`, `pickProven`, origin 2 loại mẫu, 2 câu hỏi, `templatesMarkdown` |
| `web/src/client/ChannelTemplates.tsx` (mới) | khối Làm theo kênh |
| `web/src/client/YoutubeChannel.tsx` | ô tick trong bảng Từng video + gắn khối |
| `web/src/locales/en-text-social.ts`, `en-text-sweep.ts` | bản tiếng Anh |
| Test | `tests/channel-local-titles.test.ts`, `tests/story-template.test.ts` (mới), thêm ca vào `tests/magic-notes.test.ts` |

---

### Task 0: Đo trước — phiên `lang = vi` có trả tiêu đề gốc không

Không commit gì. Cách sửa phần A dựa trên giả định `lang` đổi được tiêu đề — phải đo trước.

**Files:**
- Create (tạm, xoá cuối task): `web/scripts/tmp-measure-titles.ts`

- [ ] **Step 1: Lấy link kênh** — kênh lịch sử tiếng Việt trong ảnh anh gửi (có video "Tư Mã Ý…", "Bắc Tề (550–577)…"). Không biết link thì hỏi anh.

- [ ] **Step 2: Viết script đo**

```ts
// Tạm (Plan 2 · 19, Task 0): so tiêu đề tab Videos giữa phiên lang=en và lang=<hl>. Xoá sau khi đo.
import { Innertube, Log } from 'youtubei.js';

const [input, gl = 'vn', hl = 'vi'] = process.argv.slice(2);
Log.setLevel(Log.Level.NONE);
/* eslint-disable @typescript-eslint/no-explicit-any */
async function titles(lang: string) {
  const yt = await Innertube.create({ retrieve_player: false, lang, location: gl.toUpperCase() });
  const id = /^UC[\w-]{22}$/.test(input) ? input : String(((await yt.resolveURL(input)) as any)?.payload?.browseId);
  const list: any = await (await yt.getChannel(id)).getVideos();
  return new Map<string, string>((list.videos ?? []).slice(0, 15).map((x: any) => [String(x.content_id ?? x.id), String(x.metadata?.title?.text ?? x.title?.text ?? x.title)]));
}
const t0 = Date.now();
const en = await titles('en');
const t1 = Date.now();
const local = await titles(hl);
const t2 = Date.now();
let diff = 0;
for (const [id, t] of en) {
  const l = local.get(id) ?? '(không có)';
  if (l !== t) diff++;
  console.log(`${id}\n  en: ${t}\n  ${hl}: ${l}`);
}
console.log(`\nkhác nhau: ${diff}/${en.size} · en ${t1 - t0} ms · ${hl} ${t2 - t1} ms`);
```

- [ ] **Step 3: Chạy**

Run (ở `web/`): `npx tsx scripts/tmp-measure-titles.ts "https://www.youtube.com/@<handle>" vn vi`
Kỳ vọng: các video tiếng Anh trong ảnh ("The Complete History of Africa…", "The Entire Life of Napoleon…") ra tiếng Việt ở dòng `vi`; dòng cuối `khác nhau: N/15` với N > 0.

- [ ] **Step 4: Quyết**
  - N > 0 và dòng `vi` là tiếng Việt → ghi số đo (N/15, ms, ngày 2026-11-xx) để chép vào spec ở Task 5, làm tiếp Task 1.
  - N = 0 (2 phiên ra y hệt) → **dừng Task 1**, báo anh kèm output: `lang` không đổi được tiêu đề, cần cách khác. Task 2–5 vẫn làm được.

- [ ] **Step 5: Xoá script** — `rm web/scripts/tmp-measure-titles.ts`

---

### Task 1: Tiêu đề đúng ngôn ngữ nước đã chọn

**Files:**
- Modify: `web/src/collectors/youtube.ts` (sau hàm `client`, khoảng dòng 116–128)
- Modify: `web/src/collectors/youtube-channel.ts` (type `ChannelClient` ~dòng 43, `readChannel` ~dòng 108, `channelClient` ~dòng 145, `collectChannelAudit` ~dòng 232)
- Test: `web/tests/channel-local-titles.test.ts`

**Interfaces:**
- Produces: `ytLocalSession(gl: YtCountry): Promise<Innertube>` · `needsLocalTitles(gl: YtCountry): boolean` · `withLocalTitles(videos: ChVideo[], titles: Record<string, string>): ChVideo[]` · `ChannelClient.localTitles?: (id: string, gl: YtCountry) => Promise<Record<string, string>>` · `ChannelClient.channelFull: (id: string, gl?: YtCountry) => Promise<ChInfo>`.

- [ ] **Step 1: Viết test đỏ** — `web/tests/channel-local-titles.test.ts`

```ts
// Plan 2 · 19 (A): tiêu đề video theo ngôn ngữ của nước đã chọn. Không gọi mạng — client giả.
import { describe, expect, it } from 'vitest';
import { collectChannelAudit, needsLocalTitles, withLocalTitles, type ChannelClient, type ChInfo, type ChVideo } from '../src/collectors/youtube-channel';

const ID = 'UCaaaaaaaaaaaaaaaaaaaaaa';
const vid = (id: string, title: string): ChVideo => ({ id, title, views: 1000, published: '9 days ago', ageDays: 9, duration: '10:00' });
const info = (): ChInfo => ({
  id: ID, name: 'Kênh Sử', handle: '@kenhsu', avatar: null, subs: 10_000, videoCount: 2, totalViews: 1, joinedDays: 100, country: null,
  description: null, links: [], videos: [vid('v1', 'The Entire Life of Napoleon'), vid('v2', 'Tư Mã Ý giả ngu')],
});
function fake(over: Partial<ChannelClient> = {}): ChannelClient & { calls: string[] } {
  const calls: string[] = [];
  return {
    calls,
    resolve: async () => ID,
    channelFull: async (id, gl = 'us') => { calls.push(`channel:${id}@${gl}`); return info(); },
    suggest: async () => [],
    search: async () => ({ videos: [], total: 0 }),
    localTitles: async (id, gl) => { calls.push(`local:${id}@${gl}`); return { v1: 'Cuộc đời Napoleon', v9: 'video khác' }; },
    ...over,
  };
}

describe('tiêu đề theo ngôn ngữ nước', () => {
  it('chỉ đọc thêm khi ngôn ngữ nước khác tiếng Anh', () => {
    expect(needsLocalTitles('vn')).toBe(true);
    expect(needsLocalTitles('jp')).toBe(true);
    expect(needsLocalTitles('us')).toBe(false);
    expect(needsLocalTitles('ph')).toBe(false);
  });

  it('ghép theo id, giữ nguyên số và video không có bản dịch, bỏ tiêu đề rỗng', () => {
    const out = withLocalTitles([vid('v1', 'A'), vid('v2', 'B'), vid('v3', 'C')], { v1: 'Á', v2: '  ', v9: 'Z' });
    expect(out.map((v) => v.title)).toEqual(['Á', 'B', 'C']);
    expect(out[0]).toMatchObject({ id: 'v1', views: 1000, ageDays: 9 });
  });

  it('soi kênh VN: đọc kênh theo VN, tiêu đề ra tiếng Việt', async () => {
    const c = fake();
    const r = await collectChannelAudit(ID, c, 'vn');
    expect(c.calls).toContain(`channel:${ID}@vn`);
    expect(c.calls).toContain(`local:${ID}@vn`);
    expect(r.channel.videos.map((v) => v.title)).toEqual(['Cuộc đời Napoleon', 'Tư Mã Ý giả ngu']);
  });

  it('soi kênh US: không đọc thêm', async () => {
    const c = fake();
    await collectChannelAudit(ID, c, 'us');
    expect(c.calls.some((x) => x.startsWith('local:'))).toBe(false);
  });

  it('đọc thêm lỗi: giữ tiêu đề cũ, ghi lỗi, lượt soi vẫn chạy', async () => {
    const r = await collectChannelAudit(ID, fake({ localTitles: async () => { throw Error('boom'); } }), 'vn');
    expect(r.channel.videos[0].title).toBe('The Entire Life of Napoleon');
    expect(r.errors.some((e) => e.includes('boom'))).toBe(true);
  });
});
```

- [ ] **Step 2: Chạy test, thấy đỏ**

Run (ở `web/`): `npx vitest run tests/channel-local-titles.test.ts`
Expected: FAIL — `needsLocalTitles` / `withLocalTitles` không được export.

- [ ] **Step 3: Thêm phiên theo ngôn ngữ** — `web/src/collectors/youtube.ts`, ngay sau hàm `client(...)`:

```ts
const ytsLocal = new Map<string, Promise<Innertube>>();
/**
 * Phiên InnerTube nói ngôn ngữ của nước (hl) — CHỈ để đọc chữ hiển thị (tiêu đề video). Số view / ngày đăng luôn đọc bằng
 * `ytSession` (tiếng Anh) vì parseAge / parseCount chỉ hiểu tiếng Anh. Plan 2 · 19.
 */
export function ytLocalSession(gl: YtCountry): Promise<Innertube> {
  let yt = ytsLocal.get(gl);
  if (!yt) {
    Log.setLevel(Log.Level.NONE);
    yt = Innertube.create({ retrieve_player: false, lang: YT_COUNTRIES[gl].hl, location: gl.toUpperCase() }).catch((e) => { ytsLocal.delete(gl); throw e; });
    ytsLocal.set(gl, yt);
  }
  return yt;
}
```

- [ ] **Step 4: Sửa collector** — `web/src/collectors/youtube-channel.ts`

4a. Import: đổi dòng import từ `./youtube` thành

```ts
import { parseAge, parseCount, parseJoined, YT_COUNTRIES, youtubeClient, ytLimit, ytLocalSession, ytSession, type YtClient, type YtCountry } from './youtube';
```

4b. Trong `ChannelClient`, đổi dòng `channelFull` và thêm `localTitles`:

```ts
  channelFull: (id: string, gl?: YtCountry) => Promise<ChInfo>;
  /** Plan 2 · 19 — id → tiêu đề theo ngôn ngữ nước. Không có (client giả cũ) thì giữ tiêu đề tiếng Anh. */
  localTitles?: (id: string, gl: YtCountry) => Promise<Record<string, string>>;
```

4c. Thêm 2 hàm thuần ngay trên `readChannel`:

```ts
/** Nước có ngôn ngữ khác tiếng Anh → đọc thêm tiêu đề theo ngôn ngữ đó (Plan 2 · 19). */
export const needsLocalTitles = (gl: YtCountry) => YT_COUNTRIES[gl].hl !== 'en';
/** Đè tiêu đề theo id; id không có / tiêu đề rỗng thì giữ bản cũ. Số view, ngày đăng không đổi. */
export function withLocalTitles(videos: ChVideo[], titles: Record<string, string>): ChVideo[] {
  return videos.map((v) => {
    const t = titles[v.id]?.trim();
    return t ? { ...v, title: t } : v;
  });
}
```

4d. `readChannel` nhận nước — đổi chữ ký và dòng đầu:

```ts
async function readChannel(id: string, pages: number, gl: YtCountry = 'us'): Promise<ChInfo> {
  const ch: any = await (await ytSession(gl)).getChannel(id);
```

4e. Trong `channelClient`: đổi `channelFull` và thêm `localTitles` ngay dưới:

```ts
  channelFull: (id, gl = 'us') => ytLimit(() => readChannel(id, CH_VIDEO_PAGES, gl)),
  // cùng số trang với channelFull, chỉ lấy id + tiêu đề (thời gian thêm: xem số đo Task 0)
  localTitles: (id, gl) => ytLimit(async () => {
    const ch: any = await (await ytLocalSession(gl)).getChannel(id);
    const out: Record<string, string> = {};
    let list: any = await ch.getVideos();
    for (let page = 0; page < CH_VIDEO_PAGES && list; page++) {
      for (const x of (list.videos ?? []) as any[]) {
        const v = readChannelVideo(x);
        if (v?.title) out[v.id] = v.title;
      }
      list = list.has_continuation && page + 1 < CH_VIDEO_PAGES ? await list.getContinuation().catch(() => null) : null;
    }
    return out;
  }),
```

4f. Trong `collectChannelAudit`: đổi `const channel = await c.channelFull(id);` thành

```ts
  const channel = await c.channelFull(id, gl);
  if (c.localTitles && needsLocalTitles(gl)) {
    const titles = await c.localTitles(id, gl).catch((e: Error) => { errors.push(`local titles ${gl}: ${e.message}`); return null; });
    if (titles) channel.videos = withLocalTitles(channel.videos, titles);
  }
```

(Phải nằm trước bước rút keyword `channelKeywordCandidates(...)` để keyword cũng ra tiếng địa phương.)

- [ ] **Step 5: Chạy test, thấy xanh** — cả test cũ của kênh

Run: `npx vitest run tests/channel-local-titles.test.ts tests/channel-audit.test.ts tests/channel-related.test.ts tests/channel-trends.test.ts tests/youtube-hunt.test.ts`
Expected: PASS hết.

- [ ] **Step 6: Typecheck** — Run: `npx tsc --noEmit -p .` · Expected: không lỗi.

- [ ] **Step 7: Commit**

```bash
git add web/src/collectors/youtube.ts web/src/collectors/youtube-channel.ts web/tests/channel-local-titles.test.ts
git commit -m "feat(web): show channel video titles in the picked country's language"
```

---

### Task 2: Chỗ lưu mẫu + câu hỏi dài hơn

**Files:**
- Modify: `web/src/lib/ai/magic-notes.ts:10,19`
- Modify: `web/src/server/app.ts:476`
- Modify: `web/src/locales/en-text-sweep.ts:701`
- Test: `web/tests/magic-notes.test.ts`

**Interfaces:**
- Produces: `MagicTask` có thêm `'channel-template' | 'story-template'`; scope hợp lệ thêm `ytchannel:UC<22 ký tự>` và `ytvideo:<11 ký tự>`; `/api/ai/chat` nhận câu hỏi tới 12000 ký tự.

- [ ] **Step 1: Viết test đỏ** — thêm vào cuối `describe` đầu tiên trong `web/tests/magic-notes.test.ts`:

```ts
  it('Plan 2 · 19: lưu mẫu kênh + mẫu cốt truyện theo kênh / video YouTube', async () => {
    const { app, call } = setup();
    const ch = 'ytchannel:UCaaaaaaaaaaaaaaaaaaaaaa';
    const vd = 'ytvideo:dQw4w9WgXcQ';
    expect((await call('POST', '/api/ai/notes', { scope: ch, task: 'channel-template', text: 'mẫu kênh' })).status).toBe(200);
    expect((await call('POST', '/api/ai/notes', { scope: vd, task: 'story-template', text: 'mẫu video' })).status).toBe(200);
    expect((await (await app.request(`/api/ai/notes/channel-template?scope=${encodeURIComponent(ch)}`)).json()).note.text).toBe('mẫu kênh');
    expect((await (await app.request(`/api/ai/notes/story-template?scope=${encodeURIComponent(vd)}`)).json()).note.text).toBe('mẫu video');
    // id sai dạng → 400
    expect((await app.request(`/api/ai/notes/story-template?scope=${encodeURIComponent('ytvideo:abc')}`)).status).toBe(400);
    expect((await app.request(`/api/ai/notes/channel-template?scope=${encodeURIComponent('ytchannel:xyz')}`)).status).toBe(400);
  });

  it('Plan 2 · 19: câu hỏi chat tới 12000 ký tự, hơn thì từ chối', async () => {
    const { call } = setup();
    const r = await call('POST', '/api/ai/chat', { message: 'a'.repeat(12_001) });
    expect(r.status).toBe(400);
    expect((await r.json()).error).toContain('12000');
  });
```

- [ ] **Step 2: Chạy, thấy đỏ** — Run: `npx vitest run tests/magic-notes.test.ts` · Expected: FAIL (400 ở scope `ytchannel:`, lỗi chứa `4000`).

- [ ] **Step 3: Sửa `magic-notes.ts`**

```ts
export const MAGIC_TASKS = ['health', 'project-health', 'decision', 'expand', 'gap-ideas', 'channel-template', 'story-template'] as const;
```

```ts
/** `run:12` · `project:3` · `explore:5` · `gap` · `ytchannel:UC…` (mẫu kênh) · `ytvideo:<id 11 ký tự>` (mẫu cốt truyện) — Plan 2 · 19 */
export const isMagicScope = (v: unknown): v is string => typeof v === 'string'
  && /^(?:(?:run|project|explore):[1-9]\d*|gap|ytchannel:UC[\w-]{22}|ytvideo:[\w-]{11})$/.test(v);
```

Cũng trong `saveMagicNote`, đổi `b.question.slice(0, 4000)` thành `b.question.slice(0, 12_000)` (để Hỏi lại từ ghi chú đã lưu không bị cụt câu hỏi).

- [ ] **Step 4: Sửa `app.ts`** — trên `api.post('/ai/chat', …)` thêm hằng và đổi dòng kiểm:

```ts
/** Câu hỏi đi qua stdin của CLI (chat.ts) nên không vướng giới hạn dòng lệnh. 12000 đủ cho phụ đề 10 video (Plan 2 · 19). */
const CHAT_MAX = 12_000;
```

```ts
    if (!message || message.length > CHAT_MAX) return bad(tr('Câu hỏi phải có 1–12000 ký tự'), 400);
```

- [ ] **Step 5: Sửa bản tiếng Anh** — `web/src/locales/en-text-sweep.ts:701` đổi cả khoá lẫn giá trị:

```ts
  "Câu hỏi phải có 1–12000 ký tự": "The question must be 1–12000 characters",
```

- [ ] **Step 6: Chạy, thấy xanh** — Run: `npx vitest run tests/magic-notes.test.ts tests/i18n-text.test.ts` · Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add web/src/lib/ai/magic-notes.ts web/src/server/app.ts web/src/locales/en-text-sweep.ts web/tests/magic-notes.test.ts
git commit -m "feat(web): store channel and story templates as ai notes, allow longer chat questions"
```

---

### Task 3: Hàm thuần `story-template.ts`

**Files:**
- Create: `web/src/lib/story-template.ts`
- Modify: `web/src/locales/en-text-social.ts` (thêm chữ của file này)
- Test: `web/tests/story-template.test.ts`

**Interfaces:**
- Consumes: `MagicOrigin` (`@/lib/magic-notes-client`), `VideoPlanRow` (`@/lib/channel-strategy`), `Transcript`, `transcriptSample`, `TRANSCRIPT_BATCH_MAX` (`@/lib/transcript`), `BASE_MIN_AGE_DAYS` (`@/lib/youtube-score`), `Lang`, `tr` (`@/lib/i18n`), task/scope ở Task 2.
- Produces:
  - `type TemplateVideo = Pick<VideoPlanRow, 'id' | 'title' | 'views' | 'multiplier' | 'duration' | 'published' | 'url'>`
  - `isProven(v: { multiplier: number | null; ageDays: number | null }): boolean`
  - `pickProven(rows: VideoPlanRow[], max?: number): string[]`
  - `channelTemplateOrigin(channelId: string): MagicOrigin` · `storyTemplateOrigin(videoId: string): MagicOrigin`
  - `channelTemplateQuestion(channel: string, items: { v: TemplateVideo; t: Transcript }[], lang: Lang, max?: number): string`
  - `storyTemplateQuestion(v: TemplateVideo, channel: string, t: Transcript, channelTemplate: string | null, lang: Lang, max?: number): string`
  - `templatesMarkdown(channel: { name: string; url: string }, channelText: string | null, videos: { v: TemplateVideo; text: string | null }[]): string`
  - `TEMPLATE_Q_MAX = 11_500`

- [ ] **Step 1: Viết test đỏ** — `web/tests/story-template.test.ts`

```ts
// Plan 2 · 19 (B): chọn sẵn video đã chứng minh, câu hỏi ✦ mẫu kênh / mẫu cốt truyện, ghép Markdown.
import { describe, expect, it } from 'vitest';
import type { VideoPlanRow } from '../src/lib/channel-strategy';
import type { Transcript } from '../src/lib/transcript';
import {
  channelTemplateOrigin, channelTemplateQuestion, isProven, pickProven, storyTemplateOrigin, storyTemplateQuestion, templatesMarkdown, TEMPLATE_Q_MAX,
} from '../src/lib/story-template';

const row = (id: string, multiplier: number | null, ageDays: number | null): VideoPlanRow => ({
  id, title: `Video ${id}`, views: 5000, published: `${ageDays} days ago`, ageDays, duration: '20:00', multiplier, perSub: null,
  url: `https://www.youtube.com/watch?v=${id}`, pillar: null, format: null, length: 'mid', call: 'normal',
});
const tr = (id: string, words: number): Transcript => ({
  videoId: id, lang: 'vi', auto: true, fetchedAt: 0,
  segments: Array.from({ length: words }, (_, i) => ({ t: i * 1000, text: i === 0 ? 'Mở đầu: năm 550' : `câu ${i}` })),
});

describe('chọn sẵn video đã chứng minh', () => {
  it('× ≥ 1 và đủ 7 ngày; không rõ tuổi / chưa có × thì không chọn', () => {
    expect(isProven({ multiplier: 1, ageDays: 7 })).toBe(true);
    expect(isProven({ multiplier: 0.9, ageDays: 30 })).toBe(false);
    expect(isProven({ multiplier: 3, ageDays: 6 })).toBe(false);
    expect(isProven({ multiplier: 3, ageDays: null })).toBe(false);
    expect(isProven({ multiplier: null, ageDays: 30 })).toBe(false);
  });
  it('xếp × cao trước, tối đa 10', () => {
    const rows = [row('aaaaaaaaaaa', 1.3, 9), row('bbbbbbbbbbb', 0.2, 9), row('ccccccccccc', 3, 9), row('ddddddddddd', 2.1, 3)];
    expect(pickProven(rows)).toEqual(['ccccccccccc', 'aaaaaaaaaaa']);
    const many = Array.from({ length: 15 }, (_, i) => row(`v${String(i).padStart(10, '0')}`, 1 + i, 10));
    expect(pickProven(many)).toHaveLength(10);
    expect(pickProven(many)[0]).toBe('v0000000014');
  });
});

describe('chỗ lưu', () => {
  it('scope theo kênh / video', () => {
    expect(channelTemplateOrigin('UCaaaaaaaaaaaaaaaaaaaaaa')).toEqual({ scope: 'ytchannel:UCaaaaaaaaaaaaaaaaaaaaaa', task: 'channel-template' });
    expect(storyTemplateOrigin('dQw4w9WgXcQ')).toEqual({ scope: 'ytvideo:dQw4w9WgXcQ', task: 'story-template' });
  });
});

describe('câu hỏi mẫu kênh', () => {
  it('đủ 8 mục, số thật từng video, ngôn ngữ trả lời, không quá giới hạn kể cả 10 phụ đề dài', () => {
    const items = Array.from({ length: 10 }, (_, i) => ({ v: row(`v${String(i).padStart(10, '0')}`, 1.5, 9), t: tr(`v${i}`, 3000) }));
    const q = channelTemplateQuestion('Kênh Sử', items, 'vi');
    for (const h of ['Genre', 'Audience', 'Narration voice', 'Story pattern', 'Title formula', 'First-30-seconds formula', 'Typical length', 'never does']) expect(q).toContain(h);
    expect(q).toContain('Vietnamese');
    expect(q).toContain('Video v0000000009');
    expect(q).toContain('× 1.5');
    expect(q).toContain('Mở đầu: năm 550');
    expect(q).toContain('Do NOT write a full script');
    expect(q.length).toBeLessThanOrEqual(TEMPLATE_Q_MAX);
  });
  it('thiếu số thì ghi not measured', () => {
    const q = channelTemplateQuestion('K', [{ v: { ...row('aaaaaaaaaaa', null, 9), views: null }, t: tr('a', 5) }], 'en');
    expect(q).toContain('not measured');
    expect(q).toContain('English');
  });
});

describe('câu hỏi mẫu cốt truyện', () => {
  it('đủ mục, 2 hướng làm, kèm mẫu kênh khi có, không quá giới hạn', () => {
    const q = storyTemplateQuestion(row('aaaaaaaaaaa', 2, 9), 'Kênh Sử', tr('a', 5000), 'GIỌNG: hài, ngôi thứ 3', 'vi');
    for (const h of ['Premise', 'Hook', 'Acts', 'Ending', 'Same frame', 'Similar feel']) expect(q).toContain(h);
    expect(q).toContain('GIỌNG: hài, ngôi thứ 3');
    expect(q).toContain('[00:00]');
    expect(q.length).toBeLessThanOrEqual(TEMPLATE_Q_MAX);
  });
  it('chưa có mẫu kênh thì không nhắc', () => {
    expect(storyTemplateQuestion(row('aaaaaaaaaaa', 2, 9), 'K', tr('a', 5), null, 'vi')).not.toContain('Channel template');
  });
});

describe('Markdown copy cả bộ', () => {
  it('mẫu kênh trước, rồi từng video có link; video chưa có mẫu thì ghi rõ', () => {
    const md = templatesMarkdown({ name: 'Kênh Sử', url: 'https://www.youtube.com/@kenhsu' }, 'Thể loại: lịch sử', [
      { v: row('aaaaaaaaaaa', 2, 9), text: 'Premise: …' },
      { v: row('bbbbbbbbbbb', 1.2, 9), text: null },
    ]);
    expect(md.indexOf('Thể loại: lịch sử')).toBeLessThan(md.indexOf('Video aaaaaaaaaaa'));
    expect(md).toContain('https://www.youtube.com/watch?v=aaaaaaaaaaa');
    expect(md).toContain('Premise: …');
    expect(md).toMatch(/Chưa có mẫu|No template yet/); // tr() theo ngôn ngữ đang bật lúc chạy test
  });
});
```

- [ ] **Step 2: Chạy, thấy đỏ** — Run: `npx vitest run tests/story-template.test.ts` · Expected: FAIL (không tìm thấy module).

- [ ] **Step 3: Viết `web/src/lib/story-template.ts`**

```ts
// Plan 2 · 19 — Làm theo kênh: chọn sẵn video đã chứng minh, câu hỏi ✦ mẫu kênh + mẫu cốt truyện từ phụ đề THẬT, ghép Markdown copy.
// Hàm thuần, không gọi mạng. Mẫu lưu ở magic-notes (scope ytchannel:/ytvideo:), không viết kịch bản đầy đủ.
import type { VideoPlanRow } from '@/lib/channel-strategy';
import type { MagicOrigin } from '@/lib/magic-notes-client';
import { tr, type Lang } from '@/lib/i18n';
import { TRANSCRIPT_BATCH_MAX, transcriptSample, type Transcript } from '@/lib/transcript';
import { BASE_MIN_AGE_DAYS } from '@/lib/youtube-score';

export type TemplateVideo = Pick<VideoPlanRow, 'id' | 'title' | 'views' | 'multiplier' | 'duration' | 'published' | 'url'>;
/** Dưới giới hạn chat 12000 (server/app.ts CHAT_MAX), chừa chỗ cho ngữ cảnh khung chat tự gửi kèm. */
export const TEMPLATE_Q_MAX = 11_500;
const LANG_NAME: Record<Lang, string> = { vi: 'Vietnamese', en: 'English', es: 'Spanish' };
const n = (x: number | null) => (x === null ? 'not measured' : String(x));
const clip = (s: string, max: number) => (s.length > max ? `${s.slice(0, max - 1)}…` : s);
const mmss = (ms: number) => `${String(Math.floor(ms / 60_000)).padStart(2, '0')}:${String(Math.floor(ms / 1000) % 60).padStart(2, '0')}`;

/** Đã chứng minh = vượt hoặc bằng view nền (× ≥ 1) và đủ BASE_MIN_AGE_DAYS ngày tuổi. Không rõ tuổi / chưa có × → chưa chứng minh. */
export const isProven = (v: { multiplier: number | null; ageDays: number | null }) =>
  v.multiplier !== null && v.multiplier >= 1 && v.ageDays !== null && v.ageDays >= BASE_MIN_AGE_DAYS;

/** Id video tick sẵn: đã chứng minh, × cao trước, tối đa `max`. */
export function pickProven(rows: VideoPlanRow[], max = TRANSCRIPT_BATCH_MAX): string[] {
  return rows.filter(isProven).sort((a, b) => b.multiplier! - a.multiplier!).slice(0, max).map((r) => r.id);
}

export const channelTemplateOrigin = (channelId: string): MagicOrigin => ({ scope: `ytchannel:${channelId}`, task: 'channel-template' });
export const storyTemplateOrigin = (videoId: string): MagicOrigin => ({ scope: `ytvideo:${videoId}`, task: 'story-template' });

const facts = (v: TemplateVideo, t: Transcript) =>
  `${v.title} · views ${n(v.views)} · × ${n(v.multiplier)} · length ${v.duration ?? '?'} · published ${v.published ?? '?'} · captions ${t.lang}${t.auto ? ' (auto)' : ''}`;

/** ✦ Mẫu kênh: phụ đề cắt gọn (đầu–giữa–cuối) của mọi video đã tick, chia đều phần chữ còn lại. */
export function channelTemplateQuestion(channel: string, items: { v: TemplateVideo; t: Transcript }[], lang: Lang, max = TEMPLATE_Q_MAX): string {
  const head = `Build a reusable CHANNEL TEMPLATE for the YouTube channel "${channel}" from the REAL transcripts of ${items.length} proven videos `
    + '(each matched or beat the channel baseline, × = views ÷ channel baseline; the middle of each transcript is cut where marked […]). '
    + 'Use only what is in the transcripts and numbers below; write "not in the transcripts" when unsure. Do NOT write a full script.\n'
    + `Write in ${LANG_NAME[lang]}; keep quotes from the transcripts in their original language.\n`
    + 'Answer with these headings: 1) Genre. 2) Audience (age, what they care about). 3) Narration voice (point of view, pace, humour vs serious). '
    + '4) Story pattern that repeats across the videos. 5) Title formula. 6) First-30-seconds formula. 7) Typical length. 8) What this channel never does.\n';
  const lines = items.map(({ v, t }, i) => `\n### ${i + 1}. ${facts(v, t)}\n`);
  const room = max - head.length - lines.reduce((s, l) => s + l.length, 0);
  const each = Math.max(200, Math.floor(room / Math.max(1, items.length)) - 20);
  return clip(head + items.map(({ t }, i) => lines[i] + transcriptSample(t.segments, each)).join(''), max);
}

/** Phụ đề có mốc thời gian [mm:ss] để AI chia hồi; dài quá thì giữ đầu + cuối, cắt giữa. */
function timedText(t: Transcript, budget: number): string {
  const full = t.segments.map((s) => `[${mmss(s.t)}] ${s.text}`).join(' ');
  if (full.length <= budget) return full;
  const head = Math.floor(budget * 0.6);
  return `${full.slice(0, head)} […] ${full.slice(full.length - (budget - head - 7))}`;
}

/** ✦ Mẫu cốt truyện 1 video: phụ đề dài có mốc thời gian + mẫu kênh đã lưu (nếu có) để cùng giọng. */
export function storyTemplateQuestion(v: TemplateVideo, channel: string, t: Transcript, channelTemplate: string | null, lang: Lang, max = TEMPLATE_Q_MAX): string {
  const ctx = channelTemplate ? `Channel template already agreed (keep the same voice):\n${clip(channelTemplate, 2500)}\n` : '';
  const head = `Write a STORY TEMPLATE for one proven video of the YouTube channel "${channel}" from its REAL transcript (timestamps in [mm:ss]; `
    + 'the middle may be cut where marked […]). Use only what is in the transcript; write "not in the transcript" when unsure. Do NOT write a full script.\n'
    + `Write in ${LANG_NAME[lang]}; keep quotes from the transcript in their original language.\n`
    + 'Answer with these headings: 1) Premise in one sentence. 2) Hook: the first 30 seconds, quoting the real words. '
    + '3) Acts in order with timestamps — for each: what happens, what the viewer feels, the twist if any. 4) Ending + call to action. '
    + '5) Two ways to make my own: "Same frame" (keep the structure, change the characters / event) and "Similar feel" (same emotions, different topic).\n'
    + ctx + `Video: ${facts(v, t)}\nTranscript:\n`;
  return head + timedText(t, Math.max(500, max - head.length));
}

/** Markdown copy cả bộ: mẫu kênh rồi từng video (link + mẫu, chưa có thì ghi rõ). */
export function templatesMarkdown(channel: { name: string; url: string }, channelText: string | null, videos: { v: TemplateVideo; text: string | null }[]): string {
  const none = `_${tr('Chưa có mẫu')}_`;
  const parts = [`# ${tr('Mẫu kênh · {name}', { name: channel.name })}`, channel.url, '', channelText?.trim() || none];
  for (const { v, text } of videos) parts.push('', `## ${tr('Mẫu cốt truyện · {title}', { title: v.title })}`, `${v.url} · × ${v.multiplier ?? '—'}`, '', text?.trim() || none);
  return `${parts.join('\n')}\n`;
}
```

- [ ] **Step 4: Thêm bản tiếng Anh** — cuối object trong `web/src/locales/en-text-social.ts`:

```ts
  "Chưa có mẫu": "No template yet",
  "Mẫu kênh · {name}": "Channel template · {name}",
  "Mẫu cốt truyện · {title}": "Story template · {title}",
```

- [ ] **Step 5: Chạy, thấy xanh** — Run: `npx vitest run tests/story-template.test.ts tests/i18n-text.test.ts` · Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add web/src/lib/story-template.ts web/src/locales/en-text-social.ts web/tests/story-template.test.ts
git commit -m "feat(web): build channel and story template questions from real transcripts"
```

---

### Task 4: Khối Làm theo kênh + ô tick trong bảng Từng video

**Files:**
- Create: `web/src/client/ChannelTemplates.tsx`
- Modify: `web/src/client/YoutubeChannel.tsx` (`VideoPlanSection` ~dòng 333–446)
- Modify: `web/src/locales/en-text-social.ts`

**Interfaces:**
- Consumes: mọi export của Task 3; `AiMagic`, `AiMagicNote`, `useMagic` (`@/components/AiMagic`); `loadMagicNote`, `magicEntry` (`@/lib/magic-notes-client`); `Section`, `LabeledMagic`, `chip` (`./social-ui`); `Button`; `activeLang`, `tr`.
- Produces: `ChannelTemplates({ channel, picked, subs, busy, onRead })` với `channel: { id: string; name: string; url: string }`, `picked: VideoPlanRow[]`, `subs: Record<string, Transcript | 'none' | 'error'>`, `busy: boolean`, `onRead: (ids: string[]) => void`.

- [ ] **Step 1: Viết `web/src/client/ChannelTemplates.tsx`**

```tsx
// Plan 2 · 19 — khối Làm theo kênh: video đã tick → đọc phụ đề → ✦ Mẫu kênh → ✦ Mẫu cốt truyện từng video → copy Markdown.
import { useMemo, useState } from 'react';
import { AiMagic, AiMagicNote, useMagic } from '@/components/AiMagic';
import { Button } from '@/components/Button';
import type { VideoPlanRow } from '@/lib/channel-strategy';
import { activeLang, tr } from '@/lib/i18n';
import { loadMagicNote, magicEntry } from '@/lib/magic-notes-client';
import { channelTemplateOrigin, channelTemplateQuestion, storyTemplateOrigin, storyTemplateQuestion, templatesMarkdown } from '@/lib/story-template';
import type { Transcript } from '@/lib/transcript';
import { chip, LabeledMagic, Section } from './social-ui';

type TrState = Transcript | 'none' | 'error';
const copy = (text: string) => navigator.clipboard?.writeText(text).then(() => true, () => false) ?? Promise.resolve(false);

function CopyButton({ get }: { get: () => Promise<string | null> }) {
  const [done, setDone] = useState(false);
  return (
    <Button variant="secondary" onClick={() => void get().then(async (t) => { if (t && await copy(t)) { setDone(true); setTimeout(() => setDone(false), 1500); } })}>
      {done ? tr('Đã copy') : tr('Copy Markdown')}
    </Button>
  );
}

/** 1 video đã tick: tiêu đề + ✦ Mẫu cốt truyện + thẻ mẫu (nháp / đã lưu). */
function StoryRow({ r, t, channel, channelText }: { r: VideoPlanRow; t: Transcript; channel: string; channelText: string | null }) {
  const origin = storyTemplateOrigin(r.id);
  const note = useMagic(origin);
  const question = useMemo(() => storyTemplateQuestion(r, channel, t, channelText, activeLang()), [r, channel, t, channelText]);
  return (
    <li className="space-y-2 border-t border-zinc-100 pt-3">
      <div className="flex min-w-0 items-center gap-3">
        <a className="min-w-0 flex-1 truncate font-medium hover:underline" href={r.url} target="_blank" rel="noreferrer" title={r.title}>{r.title}</a>
        <span className={`${chip} shrink-0 border-zinc-200 text-zinc-600`}>× {r.multiplier ?? '—'}</span>
        {note?.saved && <span className="shrink-0"><CopyButton get={async () => note.saved?.text ?? null} /></span>}
        <span className="shrink-0"><LabeledMagic label={tr('Mẫu cốt truyện')}><AiMagic label={tr('AI đọc phụ đề thật: premise, hook 30 giây, các hồi theo thời gian, kết, 2 hướng làm (y chang · hao hao)')} question={question} origin={origin} /></LabeledMagic></span>
      </div>
      <AiMagicNote origin={origin} />
    </li>
  );
}

export function ChannelTemplates({ channel, picked, subs, busy, onRead }: {
  channel: { id: string; name: string; url: string }; picked: VideoPlanRow[]; subs: Record<string, TrState>; busy: boolean; onRead: (ids: string[]) => void;
}) {
  const ready = picked.filter((r) => typeof subs[r.id] === 'object');
  const unread = picked.filter((r) => !subs[r.id] || subs[r.id] === 'error').map((r) => r.id);
  const noSubs = picked.filter((r) => subs[r.id] === 'none').length;
  const chOrigin = channelTemplateOrigin(channel.id);
  const chNote = useMagic(chOrigin);
  const chText = chNote?.saved?.text ?? null;
  const question = useMemo(() => channelTemplateQuestion(channel.name, ready.map((v) => ({ v, t: subs[v.id] as Transcript })), activeLang()), [channel.name, ready, subs]);
  const all = async () => {
    await Promise.all(ready.map((v) => loadMagicNote(storyTemplateOrigin(v.id))));
    return templatesMarkdown(channel, chText, ready.map((v) => ({ v, text: magicEntry(storyTemplateOrigin(v.id)).saved?.text ?? null })));
  };
  return (
    <Section id="ch-templates" icon="compass" title={tr('Làm theo kênh')} count={picked.length}
      sub={tr('Tick video đã chứng minh trong bảng Từng video → đọc phụ đề → ✦ mẫu kênh → ✦ mẫu cốt truyện từng video')}
      hint={tr('App tick sẵn video × kênh ≥ 1 và đăng đủ 7 ngày, tối đa 10. AI chỉ viết mẫu từ phụ đề thật, không viết kịch bản đầy đủ. Bấm Dùng để lưu mẫu; mở lại kênh mẫu vẫn còn.')}>
      <div className="flex flex-wrap items-center gap-2 text-sm text-zinc-600">
        <span>{tr('Đã tick {n} · có phụ đề {d}', { n: picked.length, d: ready.length })}</span>
        {noSubs > 0 && <span className={`${chip} border-zinc-200`}>{tr('{n} video không có phụ đề', { n: noSubs })}</span>}
        <span className="ml-auto flex shrink-0 flex-wrap items-center gap-2">
          {unread.length > 0 && <Button variant="secondary" disabled={busy} onClick={() => onRead(unread)}>{tr('Đọc phụ đề {n} video', { n: unread.length })}</Button>}
          {ready.length > 0 && <CopyButton get={all} />}
          {ready.length > 0
            ? <LabeledMagic label={tr('Mẫu kênh')}><AiMagic label={tr('AI đọc phụ đề các video đã tick: thể loại, người xem, giọng kể, kiểu story, công thức tiêu đề + 30 giây đầu, độ dài, điều kênh không làm')} question={question} origin={chOrigin} /></LabeledMagic>
            : <span className="text-xs text-zinc-500">{picked.length ? tr('Đọc phụ đề trước rồi mới tạo mẫu') : tr('Chưa tick video nào')}</span>}
        </span>
      </div>
      <AiMagicNote origin={chOrigin} />
      {ready.length > 0 && <ol className="space-y-3">
        {ready.map((r) => <StoryRow key={r.id} r={r} t={subs[r.id] as Transcript} channel={channel.name} channelText={chText} />)}
      </ol>}
    </Section>
  );
}
```

Kiểm trước khi viết: `Section` nhận `children` và các prop trên (`web/src/client/social-ui.tsx:67`); `LabeledMagic` nhận `{ label, children }`; `Button` có `variant="secondary"` (đã dùng trong `YoutubeChannel.tsx`). Nếu chữ ký khác thì theo chữ ký thật.

- [ ] **Step 2: Gắn vào `VideoPlanSection`** — `web/src/client/YoutubeChannel.tsx`

2a. Import thêm:

```ts
import { pickProven } from '@/lib/story-template';
import { ChannelTemplates } from './ChannelTemplates';
```

2b. Trong `VideoPlanSection`, ngay dưới `const ids = useMemo(...)`:

```ts
  // Plan 2 · 19: video tick để làm mẫu — tick sẵn video đã chứng minh, đổi kênh thì tick lại
  const [picked, setPicked] = useState<string[]>(() => pickProven(plan));
  useEffect(() => { setPicked(pickProven(plan)); }, [ids]); // eslint-disable-line react-hooks/exhaustive-deps -- ids đổi = plan đổi
  const togglePick = (id: string) => setPicked((p) => (p.includes(id) ? p.filter((x) => x !== id) : p.length >= TRANSCRIPT_BATCH_MAX ? p : [...p, id]));
```

2c. Đổi `return (` của component thành bọc Fragment, khối Làm theo kênh đứng trên:

```tsx
  return (
    <>
      <ChannelTemplates channel={v.channel} picked={plan.filter((r) => picked.includes(r.id))} subs={subs} busy={busy.length > 0} onRead={(want) => void read(want)} />
      <Section id="ch-videos" …giữ nguyên…>
        …giữ nguyên…
      </Section>
    </>
  );
```

2d. Trong ô Video (cột sticky, `<span className="flex min-w-0 items-center gap-3">`), thêm ô tick làm phần tử đầu tiên:

```tsx
                      <input type="checkbox" className="h-4 w-4 shrink-0 accent-[var(--accent)]" checked={picked.includes(r.id)}
                        disabled={!picked.includes(r.id) && picked.length >= TRANSCRIPT_BATCH_MAX} onChange={() => togglePick(r.id)}
                        aria-label={tr('Chọn video này để làm mẫu')} title={tr('Chọn để làm mẫu (tối đa {n})', { n: TRANSCRIPT_BATCH_MAX })} />
```

- [ ] **Step 3: Thêm bản tiếng Anh** — `web/src/locales/en-text-social.ts`:

```ts
  "Đã copy": "Copied",
  "Copy Markdown": "Copy Markdown",
  "Mẫu cốt truyện": "Story template",
  "AI đọc phụ đề thật: premise, hook 30 giây, các hồi theo thời gian, kết, 2 hướng làm (y chang · hao hao)": "AI reads the real transcript: premise, 30-second hook, timed acts, ending, 2 ways to make yours (same frame · similar feel)",
  "Làm theo kênh": "Follow this channel",
  "Tick video đã chứng minh trong bảng Từng video → đọc phụ đề → ✦ mẫu kênh → ✦ mẫu cốt truyện từng video": "Tick proven videos in the Each video table → read transcripts → ✦ channel template → ✦ story template per video",
  "App tick sẵn video × kênh ≥ 1 và đăng đủ 7 ngày, tối đa 10. AI chỉ viết mẫu từ phụ đề thật, không viết kịch bản đầy đủ. Bấm Dùng để lưu mẫu; mở lại kênh mẫu vẫn còn.": "The app pre-ticks videos at × channel ≥ 1 that are at least 7 days old, up to 10. AI only writes templates from real transcripts, not full scripts. Press Use to save a template; it stays when you reopen the channel.",
  "Đã tick {n} · có phụ đề {d}": "{n} ticked · {d} with transcripts",
  "{n} video không có phụ đề": "{n} videos have no transcript",
  "Đọc phụ đề {n} video": "Read transcripts of {n} videos",
  "Mẫu kênh": "Channel template",
  "AI đọc phụ đề các video đã tick: thể loại, người xem, giọng kể, kiểu story, công thức tiêu đề + 30 giây đầu, độ dài, điều kênh không làm": "AI reads the ticked videos' transcripts: genre, audience, voice, story pattern, title + first-30-seconds formula, length, what the channel never does",
  "Đọc phụ đề trước rồi mới tạo mẫu": "Read transcripts first, then make templates",
  "Chưa tick video nào": "No video ticked yet",
  "Chọn video này để làm mẫu": "Pick this video for a template",
  "Chọn để làm mẫu (tối đa {n})": "Pick for a template (up to {n})",
```

Nếu khoá nào đã có sẵn trong file en-text khác (test báo trùng / TypeScript báo trùng khoá) thì bỏ dòng đó.

- [ ] **Step 4: Chạy test + typecheck + lint**

Run (ở `web/`): `npx vitest run tests/i18n-text.test.ts tests/story-template.test.ts && npx tsc --noEmit -p . && npx eslint src/client/ChannelTemplates.tsx src/client/YoutubeChannel.tsx`
Expected: PASS, không lỗi.

- [ ] **Step 5: Xem tận mắt trong browser** (preview_start dev server của web, mở trang YouTube → Soi 1 kênh)
  - Soi kênh lịch sử tiếng Việt của anh với nước **VN**: tiêu đề trong bảng Từng video ra tiếng Việt.
  - Khối Làm theo kênh đứng trên bảng, video × ≥ 1 và đủ 7 ngày đã tick sẵn, dòng "Running" không tick.
  - Bấm Đọc phụ đề → ✦ Mẫu kênh → khung Hỏi AI chạy → nháp về khối → Dùng → tải lại trang, mẫu vẫn còn.
  - ✦ Mẫu cốt truyện 1 video → Dùng → Copy Markdown dán ra có mẫu kênh + mẫu video.
  - Tick quá 10 thì ô thứ 11 xám.
  - Soát 960px + 1340px, sáng + tối, tiếng Việt + English: không cuộn ngang cả trang, tiêu đề dài `truncate`, nút không bị đẩy ra ngoài. Chụp screenshot đã Read.

- [ ] **Step 6: Commit**

```bash
git add web/src/client/ChannelTemplates.tsx web/src/client/YoutubeChannel.tsx web/src/locales/en-text-social.ts
git commit -m "feat(web): add follow-this-channel block with channel and story templates"
```

---

### Task 5: Tài liệu + soát cuối

**Files:**
- Modify: `docs/web/phase-plan2-19-mau-kich-ban.md`, `docs/web/index.md` (chip mục 19), `CHANGELOG.md`

- [ ] **Step 1: Cập nhật spec** — `docs/web/phase-plan2-19-mau-kich-ban.md`:
  - chip đầu trang → `<span class="chip chip--done">Code 2026-11-xx · chưa commit</span>` (hoặc "đã commit" nếu đã commit);
  - mục A: thay dòng `Thời gian thêm: chưa đo …` bằng số đo Task 0 (N/15 tiêu đề khác, ms, ngày, kênh);
  - thêm mục **Đã code** liệt kê file + test như trang mục 18;
  - thêm dòng giới hạn: câu hỏi chat nâng 4000 → 12000 ký tự.
- [ ] **Step 2: Chip mục 19 ở `docs/web/index.md`** đổi theo Step 1.
- [ ] **Step 3: `CHANGELOG.md`** dưới `[Unreleased]` thêm 1 dòng:

```md
- Web: Soi 1 kênh hiện tiêu đề video theo ngôn ngữ nước đã chọn + khối Làm theo kênh (✦ mẫu kênh, ✦ mẫu cốt truyện từng video, copy Markdown) — Plan 2 · 19.
```

- [ ] **Step 4: Soát cuối** — Run (gốc repo): `npm run check && npm run docs:build` · Expected: xanh cả hai.
- [ ] **Step 5: Commit**

```bash
git add docs/web/phase-plan2-19-mau-kich-ban.md docs/web/index.md CHANGELOG.md
git commit -m "docs(web): record what shipped for channel story templates"
```
