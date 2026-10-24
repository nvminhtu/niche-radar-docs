# ASO after the first paste — the part that compounds

> Nguồn: Game-AI-Skills `game-listing/references/aso-advanced.md` (2026-09-08). Viết cho game nhưng cơ chế xếp hạng,
> PPO, Custom Product Pages, In-App Events áp dụng cho mọi app. Chỗ nhắc `ux-retention.md` / `game-*` → với app xem `/app-grow`.

`aso-2026.md` is the **field-limit playbook**: what fits in each box on day one.
This file is the **system**: how the ranking actually works in 2026, which of the
four store surfaces to spend effort on, how to get keyword data instead of
guessing it, and what to change on each release so the numbers move.

Read it when a game is live, or when writing a listing you intend to iterate
(which should be all of them).

**Verification status.** Everything in §2 was read off Apple's own pages on
**2026-09-08** and is exact. §1 cites Apple's own published research. Anything
marked *(vendor)* comes from ASO tool vendors who sell against these numbers —
directionally useful, never quote it as fact.

---

## 1. What Apple's ranker actually optimises

Apple published how it ranks: **"Scaling Search Relevance: Augmenting App Store
Ranking with LLM-Generated Judgments"** ([arXiv 2602.23234](https://arxiv.org/abs/2602.23234),
SIGIR 2026). Two things in it change how you should write a listing:

1. The production ranker is trained on **two complementary objectives** —
   **behavioural relevance** (what people click and download for a query) and
   **textual relevance** (how well the listing *semantically* fits the query).
2. Apple augmented training with LLM-generated relevance judgments and shipped it
   — the A/B test moved downloads store-wide.

The practical consequence, and it is the single most important idea in this file:

> **The store now reads your page the way a language model reads it.** A term you
> never typed can still match a query if the page is genuinely *about* that thing;
> a term you stuffed in eight times cannot rescue a page that is about nothing.

So the winning move is not more keyword variants. It is a page whose **name,
subtitle, keyword line, description and screenshot captions all describe the same
game in the same vocabulary a player would use** — dense, specific, consistent.
That is also exactly what converts a human. The two audiences finally agree.

**Behavioural signals dominate after the click** *(vendor consensus, and
consistent with the paper's behavioural objective)*: install-from-search
conversion, download velocity, retention and engagement, rating volume and
recency. Which means **`ux-retention.md` is an ASO document too** — a game that
holds players outranks a game with better keywords, and there is no listing trick
that survives a D1 of 12%.

---

## 2. The four surfaces — verified limits, and what each is for

Most indies use one of these (the default product page) and leave three unused.

| Surface | Hard limits (Apple, 2026-09-08) | What it buys you |
|---|---|---|
| **Default product page** | see `aso-2026.md` | the baseline; the only one indexed by the name/subtitle/keyword fields |
| **Product Page Optimization (PPO)** | **up to 3 treatments + original**, max **90 days** per test, you set the traffic %, tests icon / screenshots / app previews, results reported as impressions, conversion rate, % improvement and **confidence (aim ≥ 90%)** | the only *causal* read you will ever get on your icon and first screenshot |
| **Custom Product Pages (CPP)** | **up to 70** pages; each takes its own screenshots, app previews, promotional text, **assignable keywords**, and a **deep link (iOS 18+)**; each has its own URL; reviewed independently of an app update | one landing page per traffic source and per audience — and extra *indexed* keyword surface |
| **In-App Events** | **10 published at once**, **15 approved** in App Store Connect; name **30 chars**, short description **50**, long description **120**; event card 16:9 (1920×1080–3840×2160), details page 9:16 (1080×1920–2160×3840); appear on the product page, **in search results**, and in editorial/personalised placements | the only way to add indexed text and a second search result **without shipping a build** |

Sources: [Product Page Optimization](https://developer.apple.com/app-store/product-page-optimization/),
[Custom Product Pages](https://developer.apple.com/app-store/custom-product-pages/),
[In-App Events](https://developer.apple.com/app-store/in-app-events/).

### The order to actually use them

1. **Ship the default page.** Nothing else matters until it exists.
2. **First 10 In-App Events, day one-ish.** A weekly challenge, a seasonal mode, a
   score reset, a new level pack — an arcade game can honestly run one a week.
   Each carries 30 + 50 indexed characters and can surface as its own search
   result. Cheapest indexed text on the store and it needs no build.
3. **PPO on the icon** as soon as there is any install volume. Icon first because
   it is the only asset that appears in *search results*, not just on the page —
   it is upstream of every other conversion lever.
4. **PPO on screenshot 1** next. Never test icon and screenshots in the same test;
   you will not know which moved it.
5. **CPPs** when you have traffic to point at them — one per channel (TikTok clip,
   Reddit thread, Apple Ads campaign), and one per *audience wording* ("bubble
   shooter" vs "one-handed game for the commute") with the keywords assigned.

> **Discipline rule.** One variable per test, and stop reading a PPO result before
> its confidence reaches ~90% — an early "winner" at 60% confidence is noise, and
> acting on it is worse than not testing.

---

## 3. Getting real keyword data (four sources, ranked)

Never fill the 100-byte box from imagination. Ranked by how much the data is
worth per unit of effort:

| # | Source | How | Quality |
|---|---|---|---|
| 1 | **Apple Ads search terms report** | run a tiny Search Match / discovery campaign ($5–10/day for a week) and read the *search terms* it actually matched | **the only first-party demand data an indie can buy.** Worth running purely as research even if the ads lose money |
| 2 | **App Store search autocomplete** | type the stem in the App Store app; suggestions are ordered by real search volume | free, directional, immediate |
| 3 | **Competitor teardown** | §4 below | tells you the vocabulary of the category |
| 4 | **Review mining** | read 1–3★ reviews of the top 10 competitors; players describe the game in their own words, and describe what is missing | gives you both keywords *and* the subtitle/caption angle — same trick as `book-research` |

**Building the line.** Take the terms, drop every word already in the App Name or
Subtitle (the store searches those separately — repeating them buys nothing),
drop anything under 3 characters (dropped by the store), and pack the rest with
**no space after the commas** (a space costs a byte and buys nothing). Prefer
**two-word phrases you can also justify in the description** — semantic
consistency is what the 2026 ranker rewards.

**What to rotate.** Keep the 3–4 terms that the game genuinely *is* forever.
Rotate the speculative tail every release and watch category rank. Keyword
changes require a version submission; **Promotional Text does not** — it is the
only field you can edit without review, so it is where seasonal wording lives.

---

## 4. Competitor teardown — 30 minutes, once per title

Take the top 10 results for your two main queries and record, in a table:

| Column | Why it matters |
|---|---|
| App Name + how the genre word is placed | tells you the naming convention players expect |
| Subtitle | the category's promise vocabulary — and what is already claimed |
| Icon: character / object / abstract, colour, does it read at 60px | your icon must be *legible next to these*, not merely nice |
| Screenshot 1: gameplay / key art / caption-led | what the category has trained the thumb to expect |
| Rating count (not the average) | a rough proxy for install volume — the only public one |
| Update cadence (version history) | a category where the top 10 all shipped this month is not a category to enter idle |
| The 1–3★ complaints | your differentiator, and your subtitle |

The two decisions this makes for you: **which convention to match** (so you look
like a real member of the category) and **which one to break** (so you are picked
out of it). Matching everything is invisible; breaking everything is unranked.

---

## 5. The funnel — read the number, then fix the right thing

App Store Connect ▸ Analytics gives you three numbers. Each has exactly one owner:

| Symptom | The broken lever | Fix |
|---|---|---|
| Few **impressions** | discovery: name, subtitle, keyword line, category, in-app events | §3, and add events |
| Impressions fine, few **product page views** | the **icon** and the title as they appear *in the search list* | PPO the icon |
| Page views fine, few **downloads** | **screenshot 1–2**, the first 150 chars, ratings | PPO screenshots; ask for ratings properly (`post-launch.md`) |
| Downloads fine, low **retention** | the game | `ux-retention.md` — and this now costs you rank too |

Diagnosing in this order stops the usual indie failure: rewriting keywords for a
month when the actual problem is an icon nobody can parse at thumbnail size.

---

## 6. Localisation — the highest ROI per hour on this list

Each localisation you add gets **its own name, subtitle, keyword field, and
screenshots**, indexed separately in that storefront. For an arcade game the text
is a few dozen words, so it is genuinely cheap.

Start with the locales where a casual arcade game has volume and the translation
burden is near zero: **Spanish (Mexico), Portuguese (Brazil), German, French,
Japanese, Korean, Simplified Chinese, Turkish, Vietnamese.** Localise the
**screenshot captions** with the metadata — a localised page with English
screenshots converts worse than either done properly.

*(Community practice, unverified by Apple: adding English (UK) / English
(Australia) as extra localisations gives you extra keyword fields that can
surface in those storefronts. Cheap to try, do not build a plan on it.)*

---

## 7. The release calendar

| Cadence | Do |
|---|---|
| Every week | one In-App Event; reply to every new 1–3★ review |
| Every release | rotate the speculative keyword tail; refresh *What's New* with a real line, not "bug fixes"; check the funnel table |
| Every 90 days | one finished PPO test → adopt the winner → start the next one on a different asset |
| Twice a year | re-run the competitor teardown; re-check Apple's field limits (they move) |
| Never | change name + subtitle + keywords + icon in one release; you lose the read on all four |

## 8. What wastes bytes, rank or review time

| Anti-pattern | Why |
|---|---|
| Repeating App Name / Subtitle words in the keyword field | already indexed; pure waste of the 100 bytes |
| Spaces after commas in the keyword line | each one costs a byte |
| Competitor names or trademarks as keywords | rejection, and Apple removes them |
| "Best", "#1", "top" as keywords | not queries; unsupported superlatives also fail review |
| Keyword-stuffed description | not indexed for search *and* reads as spam to the human and to a semantic ranker |
| Screenshots that are pure key art | Guideline 2.3.3 — must show the app in use (`store-assets.md`) |
| Chasing a head term you cannot rank for | pick the phrase where the top 10 have ratings in the hundreds, not the millions |
| Reading a PPO result below ~90% confidence | noise; you will "optimise" your way downhill |
