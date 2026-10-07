# Pre-launch review — Amfa Furniture Ltd live site preview (amfa.tilda.ws)

| Field | Value |
|---|---|
| Company | Amfa Furniture Ltd |
| Channel | Website (pre-launch preview, live at `amfa.tilda.ws` — bare `amfa.uk`/`www.amfa.uk` are not yet resolving, or at least not reachable from this session) |
| Brief | Minda, 2026-09-21: "It is nearly complete and you already had a preview" — full pre-launch review of the actual live site, superseding the 2026-09-14 advisory review of the 9 PDF page exports |
| Status | Advisory review only — Helen does not edit the site or its CMS (charter §2b); findings for Minda/the site developer to action |
| Method | Fetched all 12 pages directly via `curl` (the WebFetch tool's own proxy blocks `amfa.tilda.ws` and `amfa.uk`/`www.amfa.uk`; direct `curl` from this session reached them fine), stripped script/style/markup, and diffed the visible text and raw HTML against the findings in `Research/2026-09-14_Amfa_Website-Copy-Review.md` |
| Supersedes | `Research/2026-09-14_Amfa_Website-Copy-Review.md` (the PDF-based review) — that review's findings are re-checked below rather than repeated as new |

---

## 1. What's changed since the PDF review — resolved

- **"Modern syle" typo — fixed.** The differentiators list ("Modern style") now reads correctly
  everywhere it's used (home, about, and reused in every category page's advantages block).
- **Reviews section — resolved, better than expected.** The PDF export showed one testimonial
  (Elizabeth S.) apparently duplicated to fill a carousel. The live homepage now shows **three
  distinct, named reviews** (Andrew — fitted furniture; Sarah — bespoke kitchen; John — bespoke
  kitchen), each with different text. The "is this padding?" concern from the original review is
  resolved — genuinely more than one testimonial exists.
- **About-page third/first-person mixing — fixed on the About page itself.** The original awkward
  line *"AMFA – is a furniture company with our own production facility..."* has been rewritten
  cleanly on `/about` into separate, consistent sentences (see §2 below for where it's *not* fixed).
- **Footer nav "doubling" artifacts** ("Hallway Hallway & Utility...") — confirmed these were a PDF
  export flattening quirk, not a real site bug, as suspected in the original review. Not present
  anywhere in the live HTML.
- **Three new category pages now exist** that weren't in the original 9-PDF set: Wardrobe & Bedroom
  Storage, Living & Media Furniture, and Commercial Furniture all have live pages now (`/wardrobe-bedroom`,
  `/living-furniture`, `/commercial-furniture`) — see §3 for a structural gap on two of these.

## 2. Still open from the original review

- **"Get a free qoute" typo — still live, site-wide.** Appears in the shared "Let's find the right
  solution for your space" call-to-action block, which is reused on **all 12 pages** (every category
  page, About, Portfolio, Process, and the homepage). One fix in the source template resolves all 12
  instances.
- **"Media & Tv units" lowercase-v — still inconsistent, site-wide.** The mega-menu dropdown (reused
  on every page) still reads "Media & Tv units" in one nav instance while the correctly-capitalised
  "Media walls & TV units" appears elsewhere on the same pages (services list, footer). Same
  inconsistency flagged before, not yet standardised.
- **The mixed third/first-person "AMFA – is a furniture company..." line — fixed on About, but still
  live and duplicated on the Homepage.** It appears twice in a row in the homepage's About-teaser
  section, unchanged from the original PDF version. Worth applying the same About-page fix here.

## 3. New findings from the live site (not visible in the PDF export)

**a) Founder name still shows the uncorrected spelling.** The `/about` page reads *"founded in 2024 by
Andrejus Prutkovas and Mindaugas **Gaudešius**"* — Minda corrected this exact spelling on 2026-09-14
(`Brand-and-Voice/Amfa-Furniture-Ltd.md`) to **Mindaugas Gaudiesius**, matching the statutory-records
spelling used elsewhere in the group (including Construction's own director listing). This is a real
name-accuracy issue on a live, public page, not a cosmetic typo — worth prioritising.

**b) Cyrillic look-alike characters in three places (invisible on screen, real underneath).** Found by
inspecting the raw page source rather than reading visually — these are Cyrillic Unicode characters
(с U+0441, С U+0421) standing in for the visually-identical Latin "c"/"C", most likely a leftover from
a Cyrillic-locale copy/paste (consistent with the Russian-named `Главная страница.pdf` file noted in
the original PDF review):
- Homepage + `/process`: "A **с**lear process, managed at every step" (Cyrillic с)
- Homepage + `/custom-storage`: "**С**heck out all projects" (Cyrillic С)
- `/custom-storage`: "our **с**ustom storage solutions" (Cyrillic с)
- `/about`: "**С**o-founder" (Cyrillic С), appearing twice
These render identically to a reader but can silently break in-page search (Ctrl+F), search-engine
term matching, and screen-reader pronunciation. A find-and-replace across the source content for these
specific Cyrillic characters would catch all instances at once.

**c) Missing pricing / warranty / FAQ sections on 3 of 8 category pages.** Kitchens, Wardrobe & Bedroom,
Bathroom, Home Office, and Hallway & Utility all follow the same template: a "materials, finishes and
hardware" section, then "manufacturing time, pricing and warranty" (with the "up to 10 years" warranty
statement and a "Prices from £X" figure), then an FAQ block. **Living & Media Furniture** has the
materials section but not the pricing/warranty/FAQ block; **Custom Storage Solutions** and **Commercial
Furniture** have neither — no pricing indication, no warranty statement, and no FAQ on either page.
Since this is the warranty promise a customer would otherwise read on every other category, its absence
on these three reads as unfinished rather than intentional. Worth confirming whether this is content
still being written for these three (plausible, since they're the newest pages) or a genuine choice not
to price/warranty these categories the same way.

**d) A possible manufacturing-time contradiction on the Kitchens page.** The main body states kitchens
take *"3–8 weeks"* to manufacture. The page's own FAQ answers a different question — *"How long does it
take to make a kitchen?"* — with *"production and installation take 6–10 weeks."* These aren't
necessarily wrong (the FAQ figure explicitly includes installation, the body figure doesn't), but as
worded a reader could easily read them as two different answers to the same question. Every other
category page's body and FAQ manufacturing-time figures match each other exactly (Bathroom 2–8/2–8,
Wardrobe & Bedroom 4–8/4–8). Worth either aligning the wording or making the "installation adds time"
distinction explicit.

**e) Small formatting slip.** Hallway & Utility page: *"...has been approved.. Production time
depends on"* — a stray double period. Cosmetic, one-character fix.

**f) Possible missing closing bracket.** Kitchens and Wardrobe & Bedroom pages both read *"High-quality
MFC (Melamine Faced Chipboard"* with no closing parenthesis, while Bathroom, Home Office, and Living &
Media all correctly close it — *"(Melamine Faced Chipboard)"*. Confirmed present the same way across
multiple pages (so not a one-off), but flagging as "possible" since it's the kind of thing worth a
visual double-check against the live rendered page rather than relying solely on extracted text.

## 4. Not re-checked this pass

Didn't re-verify the specific claims flagged for "confirm before launch" in the original review
(warranty length, exact pricing floors, manufacturing-time ranges, the 50-mile free-measuring radius) —
those are the same figures on the live site as in the PDF, so the original ask (Minda to confirm each
is still accurate at go-live) still stands; this review didn't have a new source to check them against.

## Summary checklist for the site developer / Minda

- [ ] Fix "qoute" → "quote" in the shared CTA block (fixes all 12 pages at once)
- [ ] Standardise "TV" capitalisation in the mega-menu (currently "Tv" there vs "TV" elsewhere)
- [ ] Apply the About page's third/first-person fix to the homepage's duplicated About-teaser text too
- [ ] **Correct the founder's name on `/about`: "Gaudešius" → "Gaudiesius"** (real accuracy issue, not
      cosmetic)
- [ ] Find-and-replace the Cyrillic с/С characters with Latin c/C (5 known instances across home,
      about, process, custom-storage)
- [ ] Confirm whether Living & Media, Custom Storage, and Commercial Furniture are meant to have a
      pricing/warranty/FAQ section like the other 5 categories, and add if so
- [ ] Reconcile or clarify the Kitchens page's two different manufacturing-time figures (3–8 weeks vs.
      6–10 weeks in the FAQ)
- [ ] Fix the double period on the Hallway & Utility page
- [ ] Check the MFC bracket on Kitchens/Wardrobe & Bedroom pages against the live rendered page
- [ ] Reconfirm warranty/pricing/manufacturing-time/measuring-radius figures are still accurate at
      go-live (carried over from the original PDF review, not yet re-verified against a newer source)

## Sources

- `amfa.tilda.ws` — all 12 live pages (Home, Kitchens, Wardrobe & Bedroom, Bathroom, Living & Media,
  Home Office, Hallway & Utility, Custom Storage, Commercial Furniture, About, Portfolio, Process),
  fetched directly via `curl` 2026-09-21 (WebFetch tool's proxy blocks this domain).
- `Research/2026-09-14_Amfa_Website-Copy-Review.md` — the prior PDF-based review this supersedes.
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` — confirmed founder name spelling, pricing floors, and
  warranty terms used as the baseline for comparison.
