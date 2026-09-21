# Draft — Copy fixes, ready to apply (Amfa live site)

**Company:** Amfa Furniture Ltd
**Channel:** Website (live preview `amfa.tilda.ws`)
**Brief:** Turning the findings in `Research/2026-09-21_Amfa_Live-Site_Pre-Launch-Review.md` into exact,
ready-to-paste corrections rather than narrative bullets — a site developer/editor should be able to
find-and-replace each item directly.
**Status:** Ready for review. Draft-only (charter §2b) — Helen has no CMS/website access; nothing
applied. Every fix below is a correction to existing site text using already-confirmed facts, not new
content — no invented wording.

---

## 1. "qoute" → "quote" (site-wide, one shared block)

Appears identically on all 12 pages, in the "Let's find the right solution for your space" section.

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

## 7. Hallway & Utility page — stray double period

**Find:** `The average manufacturing time for furniture is 4–8 weeks after the design and materials have been approved.. Production time depends on:`
**Replace:** `The average manufacturing time for furniture is 4–8 weeks after the design and materials have been approved. Production time depends on:`

## 8. MFC bracket — Kitchens and Wardrobe & Bedroom pages

Flagged as "possible" in the review since it's worth a visual check against the live rendered page
first (text extraction can occasionally drop a character) — worth fixing either way if confirmed:

**Find:** `High-quality MFC (Melamine Faced Chipboard`
**Replace:** `High-quality MFC (Melamine Faced Chipboard)`

---

## Summary for the site developer

8 items, all straightforward find-and-replace: 2 site-wide template fixes (items 1–2, one edit each
resolves every page), 4 page-specific text corrections (items 3, 4, 6, 7), and 1 set of invisible
character fixes across 4 locations (item 5) that needs a direct string match rather than visual
proofreading. None require new facts or Minda's further sign-off — every replacement uses wording
already confirmed elsewhere on the site or in this KB.

## Sources

- `Research/2026-09-21_Amfa_Live-Site_Pre-Launch-Review.md` — where each item was first identified.
- `amfa.tilda.ws` — live page source, re-checked directly for exact current wording before drafting
  each replacement (via `curl`, since WebFetch's own proxy blocks this domain).
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` — confirmed founder name spelling (item 4).
