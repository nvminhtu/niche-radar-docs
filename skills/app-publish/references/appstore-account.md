# The Apple account — what it costs, how long it takes, when you can sell

> Nguồn: Game-AI-Skills `game-ship/references/appstore-account.md` (2026-09-08). Khác biệt với app subscription:
> app bán subscription **luôn cần** Paid Apps Agreement + thuế + ngân hàng ("Clock B") — bắt đầu từ ngày mua tài khoản.

Everything upstream of the store page. `game-listing` writes the words,
`game-ship` builds the binary — **neither can start the clock on this**, and this
is the part with real waiting in it. Read it before the first game is finished,
not after.

Verified against Apple's own pages on **2026-09-08**:
[Apple Developer Program](https://developer.apple.com/programs/),
[enrollment help](https://developer.apple.com/help/account/membership/program-enrollment),
[Paid Apps agreement / banking](https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information/),
[tax forms](https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information/),
[App Review](https://developer.apple.com/app-store/review/).
Everything marked *(community)* is second-hand and drifts — re-check it.

---

## 1. Getting the account

### There is exactly one legitimate route: enroll it yourself

**Do not buy, rent, or share a second-hand developer account.** Apple's Developer
Program License Agreement binds the account to the named legal person or entity;
transferred and rented accounts are terminated, and the apps on them go with the
account. It is also the single most common way a whole catalogue disappears
overnight. If someone offers you a "ready-made, already-approved" account, the
thing being sold is the risk. The agent will not help set one up.

An **app** can be transferred legitimately, later, between two accounts that each
enrolled properly (App Store Connect ▸ App ▸ Transfer App). That is the only
legal "buying" in this space, and it moves one app, not an account.

### The two enrollment types

| | Individual / Sole Proprietor | Organization |
|---|---|---|
| **Fee** | **$99 USD / year** | **$99 USD / year** (Enterprise Program is $299 and is *not* for the App Store) |
| Seller name on the store | your **personal legal name** | your company name |
| Needs a legal entity | no | **yes** — no DBAs, trade names, or branches |
| Needs a [D-U-N-S Number](https://developer.apple.com/enroll/duns-lookup/) | no | **yes** — free from Dun & Bradstreet, 9 digits |
| Also needs | Apple Account with **2FA**, legal age of majority | work email on the company domain, a **real public website**, legal binding authority |
| Verification time | Apple: confirmation **within 24 hours** of purchase | *(community)* **1–2 weeks**, sometimes longer; may need notarized documents |

**Which one.** For a solo indie shipping arcade games, **Individual** — it is the
same $99, it clears in a day instead of two weeks, and it needs no company. The
cost is that your personal legal name is printed as the seller on every product
page. If that matters (a pen-name studio, a name you do not want public), that is
the reason — and the only reason — to pay for a company first and enroll as an
Organization. You cannot fake it: Apple checks the D-U-N-S record against a real
registered entity.

### The enrollment steps

1. Apple Account with **two-factor authentication** on. Use one you control
   permanently — this account *is* the catalogue.
2. Enroll at [developer.apple.com/programs/enroll](https://developer.apple.com/programs/enroll/),
   or in the **Apple Developer** iOS app (the app route can verify identity with
   your passport/ID on-device and is usually the faster one for individuals).
3. Pay the $99. Renewal is annual and **lapsing pulls your apps off the store** —
   set a calendar reminder, do not rely on the email.
4. Wait for the confirmation email → you now have a **Team ID** (10 characters).
   `game-ship` Phase 2 needs that string; nothing else in the pipeline does.

> **Money note.** $99/yr is per *account*, not per app. Fifty arcade games ship
> under one membership. That is the whole reason this pipeline is worth running
> more than once.

---

## 2. How long until you can upload — and until you can be paid

Two clocks, and they are independent. People conflate them and then panic.

### Clock A — upload and go live

| Step | Gate | Realistic time |
|---|---|---|
| Membership active | payment cleared + identity verified | individual **~24h**; organization **1–2 weeks** *(community)* |
| Create the app record in App Store Connect | membership active, bundle id registered | minutes |
| Upload a build (Xcode Organizer / Transporter) | membership active + Distribution signing | minutes; processing 5–60 min |
| TestFlight internal testing | build processed | **immediate**, no review, up to 100 internal testers |
| TestFlight external testing | build processed | needs a **Beta App Review** (usually < 48h) |
| Submit for App Review | listing + screenshots + privacy answers complete | — |
| **App Review verdict** | — | Apple: ~**90% within 24h**; *(community)* a **first submission from a new account is realistically 2–5 days**, and December / September are slower |
| Release | approved | immediate, or scheduled, or phased |

So the honest answer to *"how long after buying the account can I upload?"* is
**about a day for an individual**, and the first *approval* lands a few days after
that. Budget **one week from paying Apple to being live** for the first title, and
about **48 hours** for every title after it.

**Rejection is the normal case, not the disaster case.** A rejected build is
re-submitted the same day and re-reviewed on the same clock. The arcade-game
rejections that actually recur: missing **privacy policy URL** (Guideline
5.1.1(i) — a game that collects nothing still needs one), an ad SDK with **no
`PrivacyInfo.xcprivacy`** manifest (see `game-money`), screenshots that are not
of the real app, and a placeholder Support URL.

### Clock B — getting paid

This one is *slower and separate*, and it only exists if money moves.

| You ship | Needs Paid Apps agreement? | Who pays you |
|---|---|---|
| Free game, no ads | **no** | nobody — Clock B does not apply |
| Free game with ads | **no** (Apple takes nothing) | **AdMob/your ad network** pays you — set banking up *there*, not in App Store Connect |
| Paid game, or any IAP | **yes** | Apple, monthly, ~30 days after month end |

The order is fixed and each step blocks the next:

1. **Sign the Paid Apps agreement** (App Store Connect ▸ Business).
2. **Submit the tax forms** — a US form is required of every developer
   (W-8BEN for an individual outside the US, W-8BEN-E for a foreign entity), plus
   any local ones. **You cannot enter banking before the tax forms are in.**
3. **Enter banking** — the account holder name must match the legal entity on the
   agreement, or it bounces.
4. Contract shows **Active**, generally within ~24 hours of the setup being
   complete — but **tax form processing can take up to 90 days** in the bad case.

> ⚠️ A paid app or an IAP cannot go on sale while the Paid Apps contract is
> "Pending". Apps have sat in *Waiting for Review* for weeks purely because of
> this. **If the first title is a paid game, start Clock B on day one — in
> parallel with building it.**
>
> **Vietnam / non-US sellers:** US-source income is subject to US withholding
> unless a tax treaty reduces it, and the **US–Vietnam treaty is signed but not
> in force**, so assume withholding on the US share and ask a local accountant
> before quoting yourself a net royalty. This file does not give tax advice.

**The practical sequencing for this pipeline:** ship the first game **free with
ads** (`game-money` default). It skips Clock B entirely — Apple pays you nothing,
AdMob does — so the only wait that matters is the ~1 week of Clock A.

---

## 3. What the agent will and will not do

| | |
|---|---|
| **Never** | enter your Apple ID or password, pay the $99, complete enrollment, sign agreements, enter tax or banking details, create the App Store record, upload a build, submit for review |
| **Never** | help acquire, rent, or share someone else's developer account |
| Will | tell you exactly which box to fill and in what order (`appstore-runbook.md`), write every string you paste (`game-listing`), build and export the binary (`game-ship`) |

These are your credentials and your legal agreements. The pipeline stops at the
form and hands you the values.
