# Store design — screenshots and icon, from capture to upload

> Nguồn: Game-AI-Skills `game-listing/references/store-assets.md` (2026-09-08). Với app Flutter: chụp bằng
> `python3 scripts/run_app.py shot <slug> --platform ios --name 01` (đã override status bar 9:41 + bỏ alpha), lưu `apps/ACTIVE/<slug>/source/store/`.
> Chỗ nhắc Godot / `--demo-frame` → đưa app về trạng thái có dữ liệu mẫu đẹp trước khi chụp.

`aso-2026.md` says what the frames must *sell* and what pixel sizes Apple
accepts. This file is the **production route**: how the PNGs actually get made,
the paste-ready prompts, and the tools worth using instead of hand-drawing
anything.

`game-listing` writes the plan (`## Screenshots`, `## Icon` in `listing.md`).
This file turns that plan into `games/<slug>/store-assets-prompt.md` — a batch of
paste-ready prompts plus a capture script — the same shape `game-assets` already
uses for sprites.

Snapshot date: **2026-09-08**. Sizes here are the ones verified in `aso-2026.md`;
do not restate them from memory, read that table.

---

## The one rule that decides the whole approach

> **A store screenshot must be a picture of the real app.** Apple rejects
> marketing art posing as gameplay (Guideline 2.3.3). So the *frame* is captured,
> never generated; only the **background, caption band and device frame around
> it** are designed.

That splits the work into two jobs with two different tools:

| Layer | Where it comes from | Tool |
|---|---|---|
| The gameplay pixels | the running game | `xcrun simctl io <udid> screenshot` |
| Background, caption, device frame, layout | designed | a framing tool, or an image model for the background plate only |
| The 1024² icon | fully generated art | an image model — this one *is* art (see `game-assets`) |

---

## Step 1 — capture the raw frames (AGENT can do this)

Build to a simulator whose native resolution **is** the required size, so nothing
is ever upscaled. For the required iPhone 6.9″ set (1320 × 2868) that is an
iPhone 17 Pro Max / 16 Pro Max simulator.

```bash
UDID=$(xcrun simctl list devices available | grep -m1 'iPhone 17 Pro Max' | grep -oE '[0-9A-F-]{36}')
xcrun simctl boot "$UDID"
xcrun simctl status_bar "$UDID" override --time "9:41" --batteryState charged --batteryLevel 100 --cellularBars 4
xcrun simctl install "$UDID" <path>/<slug>.app
xcrun simctl launch "$UDID" <bundle-id>
# play to the moment, then:
xcrun simctl io "$UDID" screenshot raw/01-chain-reaction.png
```

`status_bar override` is the detail that separates a store set from a debug dump
— every professional set shows 9:41 and a full battery. Verify each capture is
exactly 1320 × 2868 (`sips -g pixelWidth -g pixelHeight raw/*.png`) before
composing; a wrong-sized source is the most common silent failure.

**Getting to the right moment.** A chain reaction or a near-death board will not
happen on demand. Add a debug scene or a `--demo-frame N` boot flag to the Godot
project that sets the board up deterministically — cheaper than replaying the
game twenty times, and `game-build` can add it as a task.

## Step 2 — the frame narrative (write this before opening any tool)

Six frames, in this order. Most installs are decided on 1–2, so frame 1 carries
the whole pitch.

| # | Role | Caption pattern | Example |
|---|---|---|---|
| 1 | **The hook** — the single most spectacular moment | the promise, ≤ 5 words | *One shot, whole grid* |
| 2 | **The mechanic** — what your thumb does | the verb | *Aim the bounce* |
| 3 | **The tension** — a near-loss state | the stakes | *One row from over* |
| 4 | **The progression** — score / streak / unlock | the reward | *Beat your own record* |
| 5 | **The variety** — a second mode or later level | the depth | *Levels that fight back* |
| 6 | **The frictionless close** | the objection killer | *Free. Offline. One hand.* |

Rules that hold across every set: captions in the **top third** (thumbnails crop
the bottom), ≤ 5 words each, one benefit per frame, sentence case, never a feature
list, never a wall of UI. Localise the captions before localising anything else.

## Step 3 — compose (pick one route)

| Route | Use when | Cost |
|---|---|---|
| **A. Framing tool** (`fastlane frameit`, or a GUI below) | the standard set; repeatable, scriptable | free |
| **B. Agent skill** (`shots`, `store-screenshots` — table below) | you want the agent to do steps 2+3 end-to-end | free |
| **C. Hosted editor** (AppMockUp, Previewed, Screenshots.pro) | one-off, want templates and no local setup | free tier → paid |
| **D. Hand-composed** (Pillow / Canva / Figma) | a look none of the above gives | your time |

Route A is the default for this pipeline: it is scriptable, so the whole set
regenerates when the art changes, and it needs no account.

### Paste-ready prompts (background plate only — never the gameplay)

Write these into `games/<slug>/store-assets-prompt.md`, one per style, and feed
them to whichever image generator is available. The output is a **plate the
screenshot sits on**, so it must be empty in the middle.

```
Vertical mobile marketing background plate, 1320x2868, [brand colour] to
[secondary colour] soft gradient, subtle [motif from the game: bubbles / dino
scales / rock texture] pattern at 10% opacity around the edges, large empty
centre area reserved for a phone mockup, clean top band reserved for a short
headline, no text, no letters, no device, no UI, flat vector, high contrast,
app store marketing style
```

```
Playful arcade key-art background, 1320x2868 portrait, [mascot] peeking in from
the bottom-left corner only, [brand colour] saturated flat background, confetti
and motion streaks in the corners, centre 60% left completely empty and clean,
no text, no letters, no phone, no UI elements, bold cartoon style, thick outlines
```

**Prompt hygiene that actually matters:** always say `no text, no letters` (image
models write garbled words that get the set rejected as sloppy), always reserve
the centre, and always state the exact pixel ratio. Generate the plate **once**
and reuse it across all six frames — a set that shares one background reads as a
set; six different backgrounds read as six unrelated apps.

### The icon prompt lives elsewhere

The 1024² icon is generated art and its prompt template is in
`aso-2026.md` §Icon (character-led, no text, no alpha, no rounded corners) — pass
it to `game-assets`, which owns image generation. Do not duplicate it here.

## Step 4 — verify before upload

```bash
sips -g pixelWidth -g pixelHeight -g hasAlpha shots/*.png
```

Every file must be **1320 × 2868** and **`hasAlpha: no`**. An alpha channel is an
upload-time rejection, and it is what every PNG exporter produces by default.
Strip it: `sips -s format png --setProperty hasAlpha false in.png --out out.png`
(or `magick in.png -alpha off out.png`).

---

## Tools and services — verified 2026-09-08

Star counts and licences read from the GitHub API on that date; hosted services'
pricing drifts, re-check before paying.

### Open source (repos)

| Repo | ★ | Licence | What it is |
|---|---|---|---|
| [fastlane/fastlane](https://github.com/fastlane/fastlane) | 42.1k | MIT | The baseline. `snapshot` captures, **`frameit`** puts captures in device frames with a title/subtitle from a `Framefile.json`, `deliver` uploads metadata + screenshots to App Store Connect. Scriptable, CI-friendly, needs ImageMagick |
| [hypersocialinc/shots](https://github.com/hypersocialinc/shots) | 236 | — | **A Claude Code / agent skill** for producing App Store screenshots with an image model. Closest existing thing to "a screenshot skill" — study it before writing our own |
| [realZachi/shotluma](https://github.com/realZachi/shotluma) | 119 | MIT | Local-first AI screenshot editor, no upload |
| [dotnetdreamer/open-screenshot-generator](https://github.com/dotnetdreamer/open-screenshot-generator) | 91 | MIT | "Open-source Canva" for App Store / Play screenshots |
| [hebertporto/appstore-forge](https://github.com/hebertporto/appstore-forge) | 82 | MIT | Local Mac app; device frames drawn as canvas primitives (no bitmap mockups to license), panorama sets, nothing leaves the machine |
| [LeeHueeng/store-screenshots](https://github.com/LeeHueeng/store-screenshots) | 81 | MIT | **Agent skill** (Claude Code + Codex): raw captures → framed, branded, captioned store images at exact sizes; can drive the simulator itself |
| [ParthJadhav/ios-marketing-capture](https://github.com/ParthJadhav/ios-marketing-capture) | 259 | MIT | Multi-locale marketing asset automation |
| [goodwhale/AspirinShot](https://github.com/goodwhale/AspirinShot) | 131 | — | Compose screenshots in SwiftUI inside Xcode |
| [timoa/cdkit.appstore.design](https://github.com/timoa/cdkit.appstore.design) | 33 | MIT | Node CLI, themed App Store / Play screenshot sets |

**Two of these are agent skills doing exactly the job this pipeline needs**
(`shots`, `store-screenshots`). Before writing a `game-screenshots` skill from
scratch, read both — the honest options are *install one of them alongside this
pipeline* and let `game-listing` hand it the frame plan, or vendor the ideas and
keep everything in-repo. Neither is a dependency today; this file is the
in-repo route.

### Hosted services

| Service | Free tier | Notes |
|---|---|---|
| [AppMockUp Studio](https://app-mockup.com/) | yes, generous | Browser, templates, exports all required App Store sizes. The usual no-account answer |
| [Previewed](https://previewed.app/) | limited | Templates + 3D device mockups, video previews |
| [Screenshots.pro](https://screenshots.pro/) | trial | Template-driven store sets |
| [Screenshots.live](https://screenshots.live/) | trial | REST API + fastlane output, for CI |
| [Canva](https://www.canva.com/) | yes | Free-form; you set the 1320×2868 canvas yourself |
| [Figma](https://www.figma.com/) | yes | Full control, and Apple ships [official device frames + design resources](https://developer.apple.com/design/resources/) |

### Source material

| Resource | Use |
|---|---|
| [Apple Design Resources](https://developer.apple.com/design/resources/) | official device bezels, Sketch/Figma libraries — the only device frames guaranteed current and licensed for this |
| [Apple screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications) | the pixel table; re-verify before every launch |
| [App Store Marketing Guidelines](https://developer.apple.com/app-store/marketing/guidelines/) | what you may and may not put around Apple hardware and badges |
| [App Review Guidelines 2.3.3](https://developer.apple.com/app-store/review/guidelines/#accurate-metadata) | the "screenshots must show the app in use" rule |
| `game-assets/references/asset-sources.md` | CC0 fonts and textures for caption bands and plates |

---

## Writing `games/<slug>/store-assets-prompt.md`

Same shape as `game-assets`' `assets-prompt.md`, so one habit covers both:

```markdown
# Store design — <Game Name>

## Capture list (raw, 1320x2868, simulator: iPhone 17 Pro Max)
| # | File | Game state to reach | How to reach it |
|---|---|---|---|
| 1 | raw/01-hook.png | six blocks breaking mid-volley | --demo-frame 1 |
...

## Background plate prompt
```
<the prompt>
```

## Captions
| # | Caption (≤5 words) |
|---|---|
...

## Icon
→ handed to game-assets; direction in listing.md ## Icon

## Compose + verify
<the frameit / composition command, then the sips check>
```
