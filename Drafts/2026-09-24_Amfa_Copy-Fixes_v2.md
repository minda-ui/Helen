# Draft — Copy fixes, ready to apply (Amfa live site)

**Company:** Amfa Furniture Ltd
**Channel:** Website (live at `amfa.uk`)
**Brief:** Refresh of `Drafts/2026-09-21_Amfa_Copy-Fixes_v1.md` against the real live domain — re-checked
2026-09-24, confirmed 7 of the original 8 items are still live and unfixed (only the Hallway & Utility
double period was applied). Domain updated throughout; the double-period item is dropped.
**Status:** Ready for review. Draft-only (charter §2b) — Helen has no CMS/website access; nothing
applied. Every fix below is a correction to existing site text using already-confirmed facts, not new
content — no invented wording.

---

## 1. "qoute" → "quote" (site-wide, one shared block)

Appears identically on all pages, in the "Let's find the right solution for your space" section.

**Find:** `Get a free qoute`
**Replace:** `Get a free quote`

One fix in the shared source block resolves every instance.

## 2. "Tv" → "TV" (mega-menu, site-wide, one shared block)

**Find:** `Media & Tv units`
**Replace:** `Media & TV units`

Matches the correct capitalisation already used elsewhere on the same pages ("Media walls & TV units").

## 3. Homepage — mixed third/first-person paragraph

This was already fixed on the About page but the original, awkward version is still live on the
homepage (appears twice, likely two responsive-breakpoint copies of the same element).

**Find:**
> AMFA – is a furniture company with our own production facility in Newcastle upon Tyne. We create
> kitchens, wardrobes, walk-in closets, and other made-to-measure furniture, combining style,
> functionality, and durability

**Replace:**
> AMFA is a furniture company with its own production facility in Newcastle upon Tyne, creating
> kitchens, wardrobes, walk-in closets, and other made-to-measure furniture that combines style,
> functionality, and durability.

(Consistent third-person phrasing, same approach already live and working on the About page — no new
claims, just the grammar fix.)

## 4. Founder name — `/about` page

Minda corrected this spelling on 2026-09-14 (`Brand-and-Voice/Amfa-Furniture-Ltd.md`), matching the
statutory-records spelling used elsewhere in the group. The live page still has the old spelling.

**Find:** `Mindaugas Gaudešius`
**Replace:** `Mindaugas Gaudiesius`

Confirmed live in the page's main heading: *"AMFA is a modern furniture company, founded in 2024 by
Andrejus Prutkovas and Mindaugas Gaudešius"* — appears at least twice on `/about` (heading + co-founder
credit block); check both.

## 5. Cyrillic look-alike characters (5 instances, invisible on screen)

These are Cyrillic Unicode characters standing in for the visually-identical Latin letter. A simple
find-and-replace on the specific character won't catch them via a normal text search (they look
identical) — this needs either a direct string replace in the source, or the site's own search-and-
replace tool set to match on the exact string below (copy-paste it rather than retyping).

| Page(s) | Find (Cyrillic) | Replace (Latin) |
|---|---|---|
| Homepage, `/process` | `A сlear process, managed at every step` | `A clear process, managed at every step` |
| Homepage, `/custom-storage` | `Сheck out all projects` | `Check out all projects` |
| `/custom-storage` | `our сustom storage solutions` | `our custom storage solutions` |
| `/about` (×2) | `Сo-founder` | `Co-founder` |

## 6. Kitchens page — manufacturing-time wording

Not a factual error (both figures are real, live numbers), but the two mentions read as contradictory
side by side. Reworded rather than changing either number, so nothing needs Minda's re-confirmation.

**Find (FAQ):**
> On average, production and installation take 6–10 weeks after the design has been approved.

**Replace:**
> On average, manufacturing takes 3–8 weeks, plus professional installation, after the design has been
> approved.

(Keeps both real figures — 3–8 weeks manufacturing, matching the rest of the page — while making clear
installation is the additional time, rather than presenting a second, seemingly different total.)

## 7. MFC bracket — Kitchens and Wardrobe & Bedroom pages

Confirmed live on both pages (2026-09-24 re-check) — the closing bracket is genuinely missing, not a
text-extraction artefact.

**Find:** `High-quality MFC (Melamine Faced Chipboard`
**Replace:** `High-quality MFC (Melamine Faced Chipboard)`

---

## Summary for the site developer

7 items, all straightforward find-and-replace: 2 site-wide template fixes (items 1–2, one edit each
resolves every page), 3 page-specific text corrections (items 3, 4, 6), 1 page-specific bracket fix
(item 7), and 1 set of invisible character fixes across 4 locations (item 5) that needs a direct string
match rather than visual proofreading. None require new facts or Minda's further sign-off — every
replacement uses wording already confirmed elsewhere on the site or in this KB. The Hallway & Utility
double-period fix from the v1 list is already live — dropped from this refresh.

## Sources

- `Research/2026-09-24_Amfa_Live-Site_amfa-uk_Launch-Review.md` — the launch re-check confirming which
  v1 items are still outstanding.
- `Drafts/2026-09-21_Amfa_Copy-Fixes_v1.md` — original source of all 7 remaining items.
- `amfa.uk` — live page source, re-checked directly for exact current wording, 2026-09-24 (via `curl`,
  since WebFetch's own proxy blocks this domain).
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` — confirmed founder name spelling (item 4).
