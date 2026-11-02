# Skill Reddit Q&A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Skill Claude Code `reddit-qa` dùng chung mọi sản phẩm: lái Chrome thật tìm câu hỏi Reddit → `queue.md` có điểm + trạng thái → nháp câu trả lời theo `profile.md` của sản phẩm.

**Architecture:** Phần lái Chrome và viết bài là chữ hướng dẫn trong `SKILL.md` (Claude làm bằng tool `claude-in-chrome`).
Phần cần lặp lại y hệt (bỏ trùng, chấm điểm, trạng thái, chọn bài kế) nằm trong một script Node không phụ thuộc gì: `scripts/queue.mjs`, có test `node --test`.
Dữ liệu của từng sản phẩm nằm trong repo sản phẩm, folder `marketing/reddit/`.

**Tech Stack:** Node 22 (ESM, `node:test`, `node:assert`), Markdown, tool `claude-in-chrome` của Claude Code (`claude --chrome`).

**Spec:** [Backlog 29 · Skill Reddit Q&A](../../web/phase-backlog-29-reddit-qa-skill.md)

## Global Constraints

- Skill nằm ở `~/.claude/skills/reddit-qa/` (folder này **không** phải git repo → task skill không có bước commit; chỉ commit phần nằm trong repo sản phẩm).
- Script không cài package nào, chỉ dùng `node:*`.
- Chrome chỉ **đọc**: không đăng bài, không comment, không vote, không nhắn tin, không join subreddit.
- Không đăng nhập, không nhập mật khẩu thay người dùng; gặp captcha / chặn → dừng, báo.
- ≤ 15 trang tìm / lượt, nghỉ 2–3 giây giữa 2 trang.
- Mỗi subreddit ≤ 2 bài đã đăng / tuần; mỗi lần viết, mỗi subreddit tối đa 1 bài.
- Bỏ bài bị khoá / lưu trữ / quá 12 tháng (trừ bài đã có trạng thái khác `mới`).
- Trạng thái đúng 4 chữ: `mới` · `đã nháp` · `đã đăng` · `bỏ qua`.
- Không bịa số: câu trả lời chỉ dùng số có trong `profile.md` (kèm nguồn).
- Hàng chờ và nháp nằm trong `marketing/reddit/` của repo sản phẩm, không nằm trong `docs/`.
- Chữ của skill + tài liệu bằng tiếng Việt; câu trả lời Reddit bằng tiếng Anh.

## File Structure

| File | Trách nhiệm |
|---|---|
| `~/.claude/skills/reddit-qa/scripts/queue.mjs` | hàm thuần (điểm, slug, đọc / ghi bảng, gộp, đổi trạng thái, chọn bài) + CLI `merge` · `set` · `next` |
| `~/.claude/skills/reddit-qa/scripts/queue.test.mjs` | test hàm thuần + CLI |
| `~/.claude/skills/reddit-qa/SKILL.md` | luồng 3 lệnh, cách lái Chrome, luật cứng |
| `~/.claude/skills/reddit-qa/references/queries.md` | 5 nhóm câu tìm + subreddit mặc định |
| `~/.claude/skills/reddit-qa/references/answer-rules.md` | luật + khung file nháp |
| `~/.claude/skills/reddit-qa/templates/profile.md` | khung hồ sơ sản phẩm |
| `<repo>/marketing/reddit/{profile.md,queue.md,raw/,drafts/}` | dữ liệu từng sản phẩm (skill tạo) |
| `niche-radar/marketing/README.md` | README folder mới theo khung repo |

Dạng 1 bài thô (mỗi file `raw/YYYY-MM-DD.json` là **mảng** các object này):

```json
{ "id": "1abc23", "title": "How do you find app ideas?", "subreddit": "SideProject",
  "upvotes": 42, "comments": 17, "created": "2026-10-20T08:00:00.000Z",
  "url": "https://www.reddit.com/r/SideProject/comments/1abc23/how_do_you_find_app_ideas/",
  "locked": false, "archived": false, "group": "build", "query": "app idea validation" }
```

Dạng 1 dòng hàng chờ (object trong JS):

```js
{ id, title, subreddit, upvotes, comments, created /* YYYY-MM-DD */, groups /* string[] */, hits /* số câu tìm khác nhau */,
  score /* 0–100 */, status, changed /* YYYY-MM-DD hoặc '-' */, url }
```

---

### Task 1: Hàm thuần — điểm, slug, đọc / ghi `queue.md`

**Files:**
- Create: `~/.claude/skills/reddit-qa/scripts/queue.mjs`
- Test: `~/.claude/skills/reddit-qa/scripts/queue.test.mjs`

**Interfaces:**
- Produces: `STATUSES: string[]`, `COLUMNS: string[]`, `scorePost({created, comments, upvotes, hits}, now:number) → number`,
  `slugify(title:string) → string`, `renderQueue(rows) → string`, `parseQueue(md:string) → rows`

- [ ] **Step 1: Viết test lỗi**

```js
// ~/.claude/skills/reddit-qa/scripts/queue.test.mjs
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { scorePost, slugify, renderQueue, parseQueue } from './queue.mjs'

const NOW = Date.parse('2026-11-02T00:00:00Z')
const row = (over = {}) => ({
  id: 'a1', title: 'How do I find app ideas?', subreddit: 'SideProject', upvotes: 42, comments: 17,
  created: '2026-10-20', groups: ['build'], hits: 1, score: 70, status: 'mới', changed: '-',
  url: 'https://www.reddit.com/r/SideProject/comments/a1/x/', ...over,
})

test('scorePost: bài mới, bàn vừa, khớp 2 câu → cao', () => {
  assert.equal(scorePost({ created: '2026-10-23', comments: 12, upvotes: 99, hits: 2 }, NOW), 95)
})

test('scorePost: bài cũ, quá đông comment, 0 upvote → thấp', () => {
  assert.equal(scorePost({ created: '2026-04-16', comments: 300, upvotes: 0, hits: 1 }, NOW), 20)
})

test('scorePost: upvote âm tính như 0, khớp tối đa 15', () => {
  assert.equal(scorePost({ created: '2026-10-23', comments: 0, upvotes: -5, hits: 9 }, NOW), 65)
})

test('slugify: bỏ dấu, ký tự lạ, cắt 60', () => {
  assert.equal(slugify('How do I find app ideas?!'), 'how-do-i-find-app-ideas')
  assert.equal(slugify('Tìm ý tưởng app'), 'tim-y-tuong-app')
  assert.equal(slugify('???'), 'post')
  assert.ok(slugify('a'.repeat(100)).length <= 60)
})

test('renderQueue → parseQueue giữ nguyên, kể cả dấu | trong tiêu đề', () => {
  const rows = [row(), row({ id: 'b2', title: 'Play vs App Store | which first?', groups: ['build', 'competitors'], hits: 2, changed: '2026-11-01', status: 'đã đăng' })]
  const md = renderQueue(rows)
  assert.match(md, /^# Hàng chờ Reddit/)
  assert.deepEqual(parseQueue(md), rows)
})
```

- [ ] **Step 2: Chạy test, thấy lỗi**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: FAIL, `Cannot find module` … `queue.mjs`

- [ ] **Step 3: Viết code**

```js
#!/usr/bin/env node
// Hàng chờ Reddit Q&A: gộp raw/*.json → queue.md, đổi trạng thái, chọn bài kế tiếp.
//   node queue.mjs merge <folder>
//   node queue.mjs set <folder> <id> <mới|đã nháp|đã đăng|bỏ qua>
//   node queue.mjs next <folder> [n]
// <folder> = marketing/reddit của repo sản phẩm. QUEUE_NOW=<ISO> để cố định "hôm nay" khi test.

export const STATUSES = ['mới', 'đã nháp', 'đã đăng', 'bỏ qua']
export const COLUMNS = ['id', 'tiêu đề', 'subreddit', 'upvote', 'comment', 'ngày đăng', 'nhóm', 'khớp', 'điểm', 'trạng thái', 'ngày đổi', 'link']
const DAY = 86400000
export const ageDays = (created, now) => Math.floor((now - Date.parse(created)) / DAY)

// Điểm 0–100: độ mới 40 · comment 25 (đông quá thì câu trả lời mới dễ chìm) · upvote 20 · số câu tìm cùng ra 15.
export function scorePost({ created, comments, upvotes, hits }, now) {
  const d = ageDays(created, now)
  const recency = d <= 30 ? 40 : d <= 90 ? 30 : d <= 180 ? 20 : 10
  const talk = comments === 0 ? 10 : comments <= 50 ? 25 : comments <= 200 ? 15 : 5
  const votes = Math.min(20, Math.round(Math.log10(Math.max(0, upvotes) + 1) * 10))
  return recency + talk + votes + Math.min(15, hits * 5)
}

export function slugify(title) {
  const s = title.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/gi, 'd').toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60).replace(/-+$/, '')
  return s || 'post'
}

const esc = (v) => String(v).replace(/\|/g, '\\|').replace(/\s*\n\s*/g, ' ')
const cells = (r) => [r.id, r.title, r.subreddit, r.upvotes, r.comments, r.created, r.groups.join(', '), r.hits, r.score, r.status, r.changed, r.url]

export function renderQueue(rows) {
  const head = `| ${COLUMNS.join(' | ')} |\n|${COLUMNS.map(() => '---').join('|')}|\n`
  return `# Hàng chờ Reddit\n\nFile do \`queue.mjs\` ghi — đổi trạng thái bằng \`/reddit-qa đã đăng <id>\`, không sửa tay.\n\n${head}${rows.map((r) => `| ${cells(r).map(esc).join(' | ')} |`).join('\n')}\n`
}

export function parseQueue(md) {
  return md.split('\n').filter((l) => l.startsWith('| ') && !l.startsWith('| id |')).map((l) => {
    const c = l.slice(2, -2).split(' | ').map((v) => v.replace(/\\\|/g, '|'))
    return {
      id: c[0], title: c[1], subreddit: c[2], upvotes: Number(c[3]), comments: Number(c[4]), created: c[5],
      groups: c[6] ? c[6].split(', ') : [], hits: Number(c[7]), score: Number(c[8]), status: c[9], changed: c[10], url: c[11],
    }
  })
}
```

Kiểm số test: 10 ngày → 40, 12 comment → 25, `round(log10(100)*10)` = 20, 2 câu → 10 ⇒ **95**.
200 ngày → 10, 300 comment → 5, 0 upvote → 0, 1 câu → 5 ⇒ **20**. 0 comment → 10, 9 câu → 15 ⇒ 40 + 10 + 0 + 15 = **65**.

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: PASS 5/5

---

### Task 2: Gộp, đổi trạng thái, chọn bài kế

**Files:**
- Modify: `~/.claude/skills/reddit-qa/scripts/queue.mjs` (thêm cuối file)
- Test: `~/.claude/skills/reddit-qa/scripts/queue.test.mjs` (thêm cuối file)

**Interfaces:**
- Consumes: `scorePost`, `ageDays`, `STATUSES` (Task 1)
- Produces: `sortRows(rows) → rows`, `mergeRaw(existing:rows, rawPosts:object[], now) → rows`,
  `setStatus(rows, id, status, today:'YYYY-MM-DD') → rows` (throw nếu sai), `pickNext(rows, n, now) → rows`

- [ ] **Step 1: Viết test lỗi**

```js
import { mergeRaw, setStatus, pickNext, sortRows } from './queue.mjs'

const raw = (over = {}) => ({
  id: 'a1', title: 'How do I find app ideas?', subreddit: 'SideProject', upvotes: 42, comments: 17,
  created: '2026-10-20T08:00:00.000Z', url: 'https://www.reddit.com/r/SideProject/comments/a1/x/',
  locked: false, archived: false, group: 'build', query: 'app idea validation', ...over,
})

test('mergeRaw: bỏ trùng theo id, đếm câu tìm khác nhau, số mới nhất thắng', () => {
  const rows = mergeRaw([], [raw(), raw({ query: 'find app idea', group: 'ai', upvotes: 50 }), raw({ query: 'find app idea' })], NOW)
  assert.equal(rows.length, 1)
  assert.equal(rows[0].hits, 2)
  assert.deepEqual(rows[0].groups, ['ai', 'build'])
  assert.equal(rows[0].upvotes, 42)
  assert.equal(rows[0].created, '2026-10-20')
  assert.equal(rows[0].status, 'mới')
})

test('mergeRaw: giữ trạng thái + ngày đổi của dòng cũ', () => {
  const old = [row({ status: 'đã nháp', changed: '2026-11-01' })]
  const [r] = mergeRaw(old, [raw({ upvotes: 80 })], NOW)
  assert.equal(r.status, 'đã nháp')
  assert.equal(r.changed, '2026-11-01')
  assert.equal(r.upvotes, 80)
})

test('mergeRaw: bỏ bài khoá / lưu trữ / quá 12 tháng nếu còn mới', () => {
  const rows = mergeRaw([], [raw({ id: 'l', locked: true }), raw({ id: 'z', archived: true }), raw({ id: 'o', created: '2025-10-01T00:00:00Z' }), raw({ id: 'ok' })], NOW)
  assert.deepEqual(rows.map((r) => r.id), ['ok'])
})

test('mergeRaw: dòng đã đăng không còn trong raw vẫn giữ; dòng mới không còn thì bỏ', () => {
  const old = [row({ id: 'p', status: 'đã đăng', changed: '2026-10-30' }), row({ id: 'n' })]
  assert.deepEqual(mergeRaw(old, [], NOW).map((r) => r.id), ['p'])
})

test('sortRows: mới lên đầu, điểm cao trước', () => {
  const rows = sortRows([row({ id: 'x', status: 'đã nháp', score: 99 }), row({ id: 'y', score: 40 }), row({ id: 'z', score: 80 })])
  assert.deepEqual(rows.map((r) => r.id), ['z', 'y', 'x'])
})

test('setStatus: đổi trạng thái + ngày, sai thì báo', () => {
  const [r] = setStatus([row()], 'a1', 'đã đăng', '2026-11-02')
  assert.equal(r.status, 'đã đăng')
  assert.equal(r.changed, '2026-11-02')
  assert.throws(() => setStatus([row()], 'a1', 'posted', '2026-11-02'), /trạng thái/)
  assert.throws(() => setStatus([row()], 'zz', 'đã đăng', '2026-11-02'), /không có id/)
})

test('pickNext: 1 bài / subreddit, bỏ subreddit đã đăng 2 bài trong 7 ngày', () => {
  const rows = [
    row({ id: 'a', subreddit: 'SaaS', score: 90 }), row({ id: 'b', subreddit: 'saas', score: 85 }),
    row({ id: 'c', subreddit: 'androiddev', score: 80 }), row({ id: 'd', subreddit: 'startups', score: 70 }),
    row({ id: 'p1', subreddit: 'androiddev', status: 'đã đăng', changed: '2026-10-30' }),
    row({ id: 'p2', subreddit: 'androiddev', status: 'đã đăng', changed: '2026-11-01' }),
    row({ id: 'p3', subreddit: 'startups', status: 'đã đăng', changed: '2026-10-01' }),
  ]
  assert.deepEqual(pickNext(rows, 3, NOW).map((r) => r.id), ['a', 'd'])
  assert.deepEqual(pickNext(rows, 1, NOW).map((r) => r.id), ['a'])
})
```

- [ ] **Step 2: Chạy test, thấy lỗi**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: FAIL, `does not provide an export named 'mergeRaw'`

- [ ] **Step 3: Viết code (thêm cuối `queue.mjs`)**

```js
export const sortRows = (rows) =>
  [...rows].sort((a, b) => (a.status === 'mới' ? 0 : 1) - (b.status === 'mới' ? 0 : 1) || b.score - a.score)

// rawPosts đọc theo thứ tự file (cũ → mới): số của lần sau đè lần trước.
export function mergeRaw(existing, rawPosts, now) {
  const byId = new Map()
  for (const p of rawPosts) {
    const cur = byId.get(p.id) ?? { groups: new Set(), queries: new Set() }
    Object.assign(cur, { id: p.id, title: p.title, subreddit: p.subreddit, upvotes: p.upvotes, comments: p.comments, created: p.created, url: p.url, locked: p.locked, archived: p.archived })
    cur.groups.add(p.group)
    cur.queries.add(p.query)
    byId.set(p.id, cur)
  }
  const old = new Map(existing.map((r) => [r.id, r]))
  const rows = []
  for (const p of byId.values()) {
    const prev = old.get(p.id)
    old.delete(p.id)
    const status = prev?.status ?? 'mới'
    if (status === 'mới' && (p.locked || p.archived || ageDays(p.created, now) > 365)) continue
    const hits = p.queries.size
    rows.push({
      id: p.id, title: p.title, subreddit: p.subreddit, upvotes: p.upvotes, comments: p.comments, created: p.created.slice(0, 10),
      groups: [...p.groups].sort(), hits, score: scorePost({ ...p, hits }, now), status, changed: prev?.changed ?? '-', url: p.url,
    })
  }
  for (const r of old.values()) if (r.status !== 'mới') rows.push(r)
  return sortRows(rows)
}

export function setStatus(rows, id, status, today) {
  if (!STATUSES.includes(status)) throw new Error(`trạng thái phải là: ${STATUSES.join(' · ')}`)
  if (!rows.some((r) => r.id === id)) throw new Error(`không có id ${id} trong queue.md`)
  return rows.map((r) => (r.id === id ? { ...r, status, changed: today } : r))
}

export function pickNext(rows, n, now) {
  const posted = {}
  for (const r of rows) {
    if (r.status === 'đã đăng' && r.changed !== '-' && now - Date.parse(r.changed) <= 7 * DAY) {
      const k = r.subreddit.toLowerCase()
      posted[k] = (posted[k] ?? 0) + 1
    }
  }
  const used = new Set()
  const out = []
  for (const r of sortRows(rows)) {
    const k = r.subreddit.toLowerCase()
    if (r.status !== 'mới' || used.has(k) || (posted[k] ?? 0) >= 2) continue
    out.push(r)
    used.add(k)
    if (out.length === n) break
  }
  return out
}
```

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: PASS 12/12

---

### Task 3: CLI `merge` · `set` · `next`

**Files:**
- Modify: `~/.claude/skills/reddit-qa/scripts/queue.mjs` (thêm import đầu file + khối CLI cuối file)
- Test: `~/.claude/skills/reddit-qa/scripts/queue.test.mjs` (thêm cuối file)

**Interfaces:**
- Consumes: mọi hàm của Task 1–2
- Produces (SKILL.md gọi):
  - `node queue.mjs merge <folder>` → đọc `<folder>/raw/*.json` (xếp theo tên) + `<folder>/queue.md` (nếu có), ghi `queue.md`, in `queue.md: <N> dòng · <M> mới`
  - `node queue.mjs set <folder> <id> <trạng thái>` → ghi `queue.md`, in `<id> → <trạng thái>`; sai → exit 1, in lỗi ra stderr
  - `node queue.mjs next <folder> [n=1]` → in JSON mảng các dòng, mỗi dòng thêm `slug` = `<hôm nay>-<slugify(title)>`

- [ ] **Step 1: Viết test lỗi**

```js
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const SCRIPT = path.join(path.dirname(fileURLToPath(import.meta.url)), 'queue.mjs')
const run = (...args) => spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8', env: { ...process.env, QUEUE_NOW: '2026-11-02T00:00:00Z' } })

test('CLI: merge → set → next', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'reddit-qa-'))
  fs.mkdirSync(path.join(dir, 'raw'))
  fs.writeFileSync(path.join(dir, 'raw', '2026-11-02.json'), JSON.stringify([raw(), raw({ id: 'b2', subreddit: 'SaaS', comments: 0 })]))

  const m = run('merge', dir)
  assert.equal(m.status, 0, m.stderr)
  assert.match(m.stdout, /queue\.md: 2 dòng · 2 mới/)

  const s = run('set', dir, 'a1', 'đã nháp')
  assert.equal(s.status, 0, s.stderr)
  assert.match(fs.readFileSync(path.join(dir, 'queue.md'), 'utf8'), /\| đã nháp \| 2026-11-02 \|/)

  const n = run('next', dir, '3')
  assert.deepEqual(JSON.parse(n.stdout).map((r) => [r.id, r.slug]), [['b2', '2026-11-02-how-do-i-find-app-ideas']])

  const bad = run('set', dir, 'a1', 'posted')
  assert.equal(bad.status, 1)
  assert.match(bad.stderr, /trạng thái/)
})
```

- [ ] **Step 2: Chạy test, thấy lỗi**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: FAIL ở `CLI: merge → set → next` (`m.status` khác 0 hoặc stdout rỗng)

- [ ] **Step 3: Viết code**

Thêm ngay dưới khối chú thích đầu `queue.mjs`:

```js
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
```

Thêm cuối file:

```js
function readRows(dir) {
  const f = path.join(dir, 'queue.md')
  return fs.existsSync(f) ? parseQueue(fs.readFileSync(f, 'utf8')) : []
}
const writeRows = (dir, rows) => fs.writeFileSync(path.join(dir, 'queue.md'), renderQueue(rows))

function main([cmd, dirArg, ...rest]) {
  if (!cmd || !dirArg) throw new Error('usage: node queue.mjs <merge|set|next> <folder> ...')
  const dir = path.resolve(dirArg.replace(/^~/, process.env.HOME))
  const now = process.env.QUEUE_NOW ? Date.parse(process.env.QUEUE_NOW) : Date.now()
  const today = new Date(now).toISOString().slice(0, 10)
  if (cmd === 'merge') {
    const rawDir = path.join(dir, 'raw')
    const files = fs.existsSync(rawDir) ? fs.readdirSync(rawDir).filter((f) => f.endsWith('.json')).sort() : []
    const posts = files.flatMap((f) => JSON.parse(fs.readFileSync(path.join(rawDir, f), 'utf8')))
    const rows = mergeRaw(readRows(dir), posts, now)
    writeRows(dir, rows)
    console.log(`queue.md: ${rows.length} dòng · ${rows.filter((r) => r.status === 'mới').length} mới`)
  } else if (cmd === 'set') {
    const [id, ...words] = rest
    const status = words.join(' ')
    writeRows(dir, setStatus(readRows(dir), id, status, today))
    console.log(`${id} → ${status}`)
  } else if (cmd === 'next') {
    const picked = pickNext(readRows(dir), Number(rest[0] ?? 1), now)
    console.log(JSON.stringify(picked.map((r) => ({ ...r, slug: `${today}-${slugify(r.title)}` })), null, 2))
  } else throw new Error(`lệnh lạ: ${cmd}`)
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { main(process.argv.slice(2)) } catch (e) { console.error(e.message); process.exit(1) }
}
```

`set` nối các chữ còn lại bằng dấu cách để `set <folder> a1 đã đăng` (không ngoặc) vẫn chạy.

- [ ] **Step 4: Chạy test, thấy xanh**

Run: `node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: PASS 13/13

---

### Task 4: Chữ của skill — `SKILL.md`, câu tìm, luật trả lời, khung hồ sơ

**Files:**
- Create: `~/.claude/skills/reddit-qa/SKILL.md`
- Create: `~/.claude/skills/reddit-qa/references/queries.md`
- Create: `~/.claude/skills/reddit-qa/references/answer-rules.md`
- Create: `~/.claude/skills/reddit-qa/templates/profile.md`

**Interfaces:**
- Consumes: CLI của Task 3 (đúng tên lệnh + dạng JSON thô ở mục File Structure)

- [ ] **Step 1: Viết `SKILL.md`**

````markdown
---
name: reddit-qa
description: Tìm câu hỏi trên Reddit quanh chuyện chọn niche app / soi đối thủ Google Play – App Store / Google Trends / dùng AI (Claude) research niche / keyword cạnh tranh bao nhiêu đối thủ — bằng Chrome thật của người dùng (Claude in Chrome, không gọi API Reddit), gom thành hàng chờ queue.md có điểm + trạng thái, rồi viết nháp câu trả lời tiếng Anh theo hồ sơ sản phẩm (profile.md) để người dùng tự copy lên Reddit. Dùng chung cho mọi sản phẩm. Dùng khi user nói "/reddit-qa", "tìm câu hỏi reddit", "reddit research", "hàng chờ reddit", "viết câu trả lời reddit", "viết 3 bài reddit", "đã đăng reddit", "kéo traffic từ reddit".
---

# Reddit Q&A — câu hỏi thật → câu trả lời giúp được → người dùng tự đăng

Plan gốc: repo niche-radar, `docs/web/phase-backlog-29-reddit-qa-skill.md`.

| Cái gì | Ở đâu |
|---|---|
| Dữ liệu sản phẩm | `<repo>/marketing/reddit/` (gọi là `<f>`): `profile.md` · `queue.md` · `raw/` · `drafts/` |
| Câu tìm + subreddit | `references/queries.md` (+ phần "Câu tìm thêm" trong `<f>/profile.md`) |
| Luật trả lời + khung nháp | `references/answer-rules.md` |
| Khung hồ sơ | `templates/profile.md` |
| Script | `node ~/.claude/skills/reddit-qa/scripts/queue.mjs <merge|set|next> <f> ...` |

`<repo>` = repo đang mở. Không phải repo sản phẩm (không có README / package.json mô tả sản phẩm) → hỏi user sản phẩm nào.

## Luật cứng

- Chrome chỉ **đọc**: không đăng bài, không comment, không vote, không nhắn tin, không join subreddit.
- Không đăng nhập, không nhập mật khẩu thay user. Gặp trang đăng nhập / captcha / "blocked" → dừng, báo user, không vượt.
- ≤ 15 trang tìm / lượt, nghỉ 2–3 giây giữa 2 trang (`computer` action `wait`).
- Không sửa tay `queue.md` — mọi thay đổi qua `queue.mjs`.
- Không bịa số trong câu trả lời: chỉ số có trong `profile.md`.

## Bước 0 — mỗi lần chạy

1. Phiên có tool `mcp__claude-in-chrome__*` không (loaded hoặc deferred)? Không → báo
   "Mở lại Claude Code bằng `claude --chrome` (cần extension Claude in Chrome)", dừng. Có → load một lần:
   `ToolSearch select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__computer`
2. Chưa có `<f>/profile.md` → chép `templates/profile.md` sang, điền thử từ README / docs của `<repo>`
   (chỉ điều có thật trong repo, số nào không có nguồn thì bỏ), tạo `<f>/raw/` + `<f>/drafts/`,
   rồi **dừng**: đưa user đọc, sửa, gõ "ok profile". Chưa có "ok" thì không tìm, không viết.

## `/reddit-qa tìm [nhóm...]`

Nhóm: `build` · `competitors` · `trends` · `ai` · `keywords` (bỏ trống = cả 5). Lấy câu tìm của nhóm từ
`references/queries.md` + `profile.md`; chọn tối đa 15 cặp (câu tìm × nơi tìm), ưu tiên trộn đều nhóm.
Nơi tìm: cả Reddit, hoặc 1 subreddit trong danh sách của profile.

Mỗi cặp:

1. Mở (một tab riêng, tạo bằng `tabs_create_mcp` lần đầu, dùng lại cho các lần sau):
   - cả Reddit: `https://www.reddit.com/search/?q=<câu tìm encode>&type=posts&t=year&sort=relevance`
   - 1 subreddit: `https://www.reddit.com/r/<sub>/search/?q=<câu tìm encode>&restrict_sr=1&type=posts&t=year&sort=relevance`
2. Cách (a) — đọc JSON của chính trang đó, cùng cookie (`javascript_tool`):
   ```js
   const u = location.pathname.replace(/\/$/, '') + '.json' + location.search + '&limit=25'
   const j = await fetch(u, { credentials: 'include' }).then((r) => r.json())
   j.data.children.map(({ data: d }) => ({ id: d.id, title: d.title, subreddit: d.subreddit, upvotes: d.score,
     comments: d.num_comments, created: new Date(d.created_utc * 1000).toISOString(),
     url: 'https://www.reddit.com' + d.permalink, locked: d.locked, archived: d.archived }))
   ```
3. Cách (a) lỗi (không phải JSON, 403, 429) → cách (b): `get_page_text`, tự đọc từng bài ra cùng các trường;
   trường nào trang không hiện thì: `upvotes`/`comments` = 0, `locked`/`archived` = false, `created` = ngày trang ghi (đổi về ISO).
   429 hoặc trang chặn 2 lần liền → dừng cả lượt, lưu những gì đã có.
4. Gắn `group` + `query` cho mỗi bài, nghỉ 2–3 giây.

Xong: ghi tất cả vào `<f>/raw/<hôm nay>.json` (đã có file hôm nay → đọc ra, nối thêm, ghi lại), rồi
`node …/queue.mjs merge <f>`. Báo user: số trang đã mở, cách (a) hay (b), dòng `queue.md: N dòng · M mới`, 5 bài `mới` điểm cao nhất (tiêu đề + subreddit + link).

## `/reddit-qa viết [1|3]`

1. `node …/queue.mjs next <f> <n>` (mặc định 1). Mảng rỗng → báo "hết bài mới hoặc các subreddit đã đủ 2 bài tuần này", gợi ý `/reddit-qa tìm`.
2. Mỗi bài: mở `url` → đọc bài gốc + comment đứng đầu (cách (a): `fetch(url + '.json')`; (b): `get_page_text`).
   Đọc luật subreddit: `https://www.reddit.com/r/<sub>/about/rules.json` (hoặc trang `/r/<sub>/about/rules`).
3. Bài đã bị trả lời đủ ý / không hợp sản phẩm / subreddit cấm mọi kiểu nhắc → `set <f> <id> bỏ qua`, ghi lý do cho user, lấy bài kế.
4. Viết theo `references/answer-rules.md` + `<f>/profile.md`, lưu `<f>/drafts/<slug>.md` (`slug` có sẵn trong JSON của `next`),
   rồi `node …/queue.mjs set <f> <id> đã nháp`.
5. Báo user: đường dẫn từng file nháp + câu trả lời đầy đủ trong chat (để copy ngay).

## `/reddit-qa đã đăng <id>` · `/reddit-qa bỏ qua <id>`

`node …/queue.mjs set <f> <id> đã đăng` (hoặc `bỏ qua`). In lại dòng kết quả. Skill không tự kiểm bài đã lên Reddit chưa.
````

- [ ] **Step 2: Viết `references/queries.md`**

```markdown
# Câu tìm mặc định

Câu tìm tiếng Anh, sửa / thêm riêng cho sản phẩm ở `profile.md` → "Câu tìm thêm".

## build — tôi nên build gì
- what app should I build
- app idea validation
- how to find a niche for an app
- profitable app ideas 2026
- how do you validate an app idea before building

## competitors — đối thủ trên Google Play / App Store làm gì
- how to research competitors google play
- app store competitor research
- how to see competitor app downloads
- how to find what apps are making money

## trends — người dùng đang tìm gì trên Google Trends
- google trends app idea
- how to use google trends for app ideas
- validate demand google trends

## ai — dùng Claude / AI để research
- use claude for market research
- AI niche research
- chatgpt find app idea
- can AI find a profitable niche

## keywords — keyword cạnh tranh ra sao, bao nhiêu đối thủ
- ASO keyword competition
- how many competitors for app store keyword
- keyword difficulty app store
- how to find low competition app keywords

## Subreddit mặc định
r/SideProject · r/indiehackers · r/androiddev · r/iOSProgramming · r/SaaS · r/Entrepreneur · r/startups · r/AppBusiness
```

- [ ] **Step 3: Viết `references/answer-rules.md`**

````markdown
# Luật viết câu trả lời Reddit

1. **Giúp người hỏi trước.** Bỏ hết link đi câu trả lời vẫn dùng được: có bước làm cụ thể, ví dụ thật, công cụ miễn phí nếu có.
2. **Nhắc sản phẩm chỉ khi nó giải đúng câu hỏi**, tối đa 1 lần, cuối bài, ghi rõ "I built this" (hoặc "disclosure: I'm the dev").
   Subreddit cấm tự quảng cáo → không nhắc, không link.
3. **Không bịa số.** Chỉ số trong `profile.md` → "Số đã đo" (nêu nguồn ngắn nếu tự nhiên). Không có số → nói định tính.
4. Không trùng ý comment đã đứng đầu — thêm góc khác hoặc bổ sung chỗ họ thiếu.
5. Không giả làm người dùng khác, mỗi thread chỉ 1 câu trả lời.
6. Giọng tự nhiên như dev nói chuyện: ngắn (thường 80–250 từ), đoạn ngắn hoặc gạch đầu dòng, không tiêu đề kiểu blog,
   không emoji tràn lan, không câu mở "Great question!".
7. Tránh chữ sáo: delve, leverage, seamless, game-changer, unlock, supercharge, "in today's fast-paced".

## Khung file nháp `drafts/<slug>.md`

```markdown
# <tiêu đề thread>

- Thread: <url> · r/<sub> · đọc ngày <YYYY-MM-DD>
- Hỏi gì: <1 câu>
- Comment đứng đầu đã nói: <1 câu>
- Nhắc sản phẩm: có / không — <vì sao>
- Luật subreddit về tự quảng cáo: <tóm tắt 1 câu, hoặc "không ghi">

## Câu trả lời

<câu trả lời Markdown của Reddit>

## Trước khi đăng

- [ ] Bỏ hết link vẫn dùng được
- [ ] Số nào cũng có trong profile.md
- [ ] Có "I built this" nếu nhắc sản phẩm
- [ ] r/<sub> tuần này mới đăng < 2 bài
- [ ] Đăng xong: `/reddit-qa đã đăng <id>`
```
````

- [ ] **Step 4: Viết `templates/profile.md`**

```markdown
# Hồ sơ Reddit · <tên sản phẩm>

> Skill đọc file này mỗi lần viết. Chỉ ghi điều có thật. Sửa xong gõ "ok profile".

## Sản phẩm
- Tên · link: 
- Làm gì (1–2 câu, chữ thường dân):
- Cho ai:
- Giá / miễn phí:
- Không làm được gì (để không hứa quá):

## Kinh nghiệm thật của người viết
- (chuyện đã làm, đã thử, đã sai — viết gạch đầu dòng, mỗi dòng 1 ý)

## Số đã đo (nguồn + ngày)
| Số | Nguồn | Ngày |
|---|---|---|

## Khi nào nhắc sản phẩm
- Nhắc khi:
- Không nhắc khi:

## Subreddit
- Tìm ở: (để trống = dùng danh sách mặc định)
- Không đăng ở:

## Câu tìm thêm
- (nhóm: câu tìm)
```

- [ ] **Step 5: Kiểm skill được nhận**

Run: `head -4 ~/.claude/skills/reddit-qa/SKILL.md && node --test ~/.claude/skills/reddit-qa/scripts/queue.test.mjs`
Expected: thấy `name: reddit-qa`; test PASS 13/13. Mở phiên Claude Code mới, gõ `/` thấy `reddit-qa` trong danh sách.

---

### Task 5: Folder `marketing/reddit/` cho Niche Radar + tài liệu repo

**Files:**
- Create: `niche-radar/marketing/README.md`
- Modify: `niche-radar/README.md` (bảng folder), `niche-radar/CLAUDE.md` (bảng "Đồ nằm ở đâu"), `niche-radar/docs/cach-dung.md` (mục Gap hỏi đáp), `niche-radar/CHANGELOG.md` (`[Unreleased]`)

- [ ] **Step 1: Viết `marketing/README.md` theo khung README folder**

```markdown
# Niche Radar · Marketing

**Dữ liệu để kéo người dùng về Niche Radar: hàng chờ câu hỏi Reddit, nháp câu trả lời, hồ sơ sản phẩm cho skill.**

> Một phần của [Niche Radar](../README.md). Cập nhật lần cuối: **02/11/2026**.

| | Phần | Có gì | Mở |
|---|---|---|---|
| 💬 | **Reddit** | `profile.md` hồ sơ sản phẩm · `queue.md` hàng chờ · `raw/` kết quả tìm thô · `drafts/` nháp câu trả lời | [reddit/](reddit/) |

## Bắt đầu

Mở Claude Code bằng `claude --chrome` ở gốc repo, rồi:

- `/reddit-qa tìm` — tìm câu hỏi (lần đầu skill viết `profile.md` cho bạn sửa)
- `/reddit-qa viết 1` hoặc `viết 3` — nháp câu trả lời
- `/reddit-qa đã đăng <id>` — đánh dấu sau khi tự đăng

## Lưu ý

- Skill chỉ đọc Reddit, không tự đăng. Bạn tự copy lên.
- Không sửa tay `reddit/queue.md`, dùng lệnh của skill.
- Folder này không nằm trong `docs/` nên không bị sync ra ngoài.

## Liên quan

[Backlog 29 · Skill Reddit Q&A](../docs/web/phase-backlog-29-reddit-qa-skill.md) · [Gap hỏi đáp trong app](../docs/cach-dung.md)
```

- [ ] **Step 2: Thêm 1 dòng vào bảng folder ở `README.md` gốc và bảng "Đồ nằm ở đâu" ở `CLAUDE.md`**

Dòng cho `CLAUDE.md` (cùng 3 cột `Folder | Có gì | Chạy lệnh ở`):

```markdown
| `marketing/` | dữ liệu kéo người dùng: `reddit/` (hồ sơ, hàng chờ, nháp của skill `/reddit-qa`) | gốc repo, `claude --chrome` |
```

`README.md` gốc: đọc bảng folder trước, thêm dòng cùng khung cột với nội dung tương đương.

- [ ] **Step 3: Thêm 1 dòng cuối mục "Gap hỏi đáp" của `docs/cach-dung.md`**

```markdown
Muốn **trả lời** câu hỏi Reddit để kéo người dùng: skill `/reddit-qa` (Claude Code mở bằng `claude --chrome`) tìm câu hỏi,
gom hàng chờ ở `marketing/reddit/queue.md` và viết nháp — bạn tự đăng. Chi tiết: [Backlog 29](web/phase-backlog-29-reddit-qa-skill.md).
```

- [ ] **Step 4: Thêm dòng `CHANGELOG.md` dưới `## [Unreleased]`**

```markdown
- Repo: folder mới `marketing/` — `reddit/` chứa hồ sơ, hàng chờ, nháp của skill `/reddit-qa` (skill nằm ngoài repo, dùng chung mọi sản phẩm); README folder + dòng ở README gốc, `CLAUDE.md`, `docs/cach-dung.md`.
```

- [ ] **Step 5: Build docs**

Run: `npm run docs:build` (gốc repo)
Expected: `Documentation built`, không WARNING mới.

- [ ] **Step 6: Commit (chỉ file của task này)**

`README.md`, `CLAUDE.md`, `docs/cach-dung.md`, `CHANGELOG.md` đang có thay đổi khác chưa commit → hỏi user trước: commit chung hay chỉ `marketing/README.md`.
Nếu user cho commit chung:

```bash
git add marketing/README.md README.md CLAUDE.md docs/cach-dung.md CHANGELOG.md
git commit -m "docs(repo): folder marketing/ cho skill reddit-qa"
```

---

### Task 6: Chạy thật với Niche Radar + điền bảng thử

**Files:**
- Create (skill tạo): `niche-radar/marketing/reddit/{profile.md,queue.md,raw/2026-11-xx.json,drafts/*.md}`
- Modify: `niche-radar/docs/web/phase-backlog-29-reddit-qa-skill.md` (mục 7 Bảng thử)

- [ ] **Step 1:** Mở Claude Code bằng `claude --chrome` ở gốc niche-radar, gõ `/reddit-qa tìm build`.
  Expected: skill tạo `marketing/reddit/profile.md` điền từ README / docs, rồi dừng chờ "ok profile".
- [ ] **Step 2:** User sửa `profile.md`, gõ "ok profile", chạy lại `/reddit-qa tìm build`.
  Expected: ≤ 15 trang, `raw/<hôm nay>.json` có bài, `queue.md` đúng 12 cột, dòng `mới` xếp theo điểm giảm dần.
- [ ] **Step 3:** Ghi lại: cách (a) JSON có chạy không / bị chặn không · cách (b) đủ trường không · 15 trang mất bao lâu, có captcha không.
  Điền 3 dòng mục 7 của Backlog 29 (kết quả + ngày), đổi chip đầu trang thành "đang làm".
- [ ] **Step 4:** `/reddit-qa viết 1`. Expected: 1 file `drafts/<slug>.md` đúng khung `answer-rules.md`, dòng đó thành `đã nháp`.
  Đọc nháp, soát đủ checklist "Trước khi đăng"; số nào không có trong `profile.md` → sửa skill / luật, viết lại.
- [ ] **Step 5:** `npm run docs:build` xanh; hỏi user trước khi commit (`marketing/reddit/` + Backlog 29).

---

### Task 7: Thử với sản phẩm thứ hai (không sửa skill)

**Files:**
- Create (skill tạo): `<repo sản phẩm thứ 2>/marketing/reddit/profile.md`, `queue.md`, `raw/…`

- [ ] **Step 1:** Hỏi user sản phẩm thứ hai (ví dụ repo shotmatic). Mở `claude --chrome` ở repo đó, `/reddit-qa tìm keywords`.
- [ ] **Step 2:** Viết / duyệt `profile.md`, chạy lại. Expected: `queue.md` ra bài, **không** phải sửa file nào trong `~/.claude/skills/reddit-qa/`.
  Phải sửa skill → sửa cho chung (không gắn tên sản phẩm), chạy lại test `node --test …/queue.test.mjs` xanh.
- [ ] **Step 3:** Ghi 1 dòng kết quả vào mục "Xong khi" của Backlog 29 (đánh dấu đã đạt + ngày). Không commit vào repo sản phẩm kia nếu user chưa đồng ý.
