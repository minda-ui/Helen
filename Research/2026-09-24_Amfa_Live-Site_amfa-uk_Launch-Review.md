# Review — Amfa live site at `amfa.uk` (launch re-check)

**Company:** Amfa Furniture Ltd
**Status:** Site is live at the real domain `amfa.uk` (previously `amfa.tilda.ws`). All 15 pages fetched via `curl` and checked against the row 12 copy-fixes document and row 9 legal pages.
**Bottom line:** One urgent issue (unresolved legal-page placeholders, live and public). None of the 8 ready-to-apply copy fixes from `Drafts/2026-09-21_Amfa_Copy-Fixes_v1.md` were applied except one. The pricing/warranty/FAQ deliverable (row 11) **is** live correctly.

---

## Urgent — fix today

**Privacy Policy and Terms of Use are live with internal drafting notes still visible to the public.**

5 instances of literal `[TO CONFIRM before publishing: ...]` bracketed text — Helen's own internal
flags from the draft, never meant to be published — are live on the real pages:

- Privacy Policy (4): whether this policy needs updating if analytics/marketing tools are added later;
  the specific delivery/installation subcontractors who'd see customer data; the actual data-retention
  period; whether Tilda or another supplier processes data outside the UK/EEA.
- Terms of Use (1): whether Amfa wants a separate Sales Terms document.

These are exactly the 4 gaps flagged in the original brief (`Drafts/2026-09-21_Amfa_Legal-Pages_Brief.md`)
as needing your and the solicitor's input before publishing — the draft carried them as visible flags
on purpose, for review, not for the live site. Whoever built the page copied the draft text wholesale.
**Needs either the real answers filled in, or the bracketed sentences removed, today** — a live privacy
policy with "[TO CONFIRM before publishing]" in it looks unprofessional and may not be legally adequate
as-is. Flagging as Helen's most urgent finding this pass.

## Copy fixes (row 12 document) — 7 of 8 not applied

| # | Fix | Status |
|---|---|---|
| 1 | "qoute" → "quote" | **Not applied** — still live, every page |
| 2 | "Media & Tv" → "Media & TV" (mega-menu) | **Not applied** — still live, every page |
| 3 | Homepage duplicate mixed-person paragraph | **Not applied** — old text still live, twice |
| 4 | Founder name `Gaudešius` → `Gaudiesius` | **Not applied** — old spelling still live on `/about` |
| 5 | 5 Cyrillic homoglyph instances | **Not applied** — all still live: `Сo-founder` ×2 (`/about`), `Сheck` (`/`, `/custom-storage`), `сustom` (`/custom-storage`), `сlear` (`/`, `/process`) |
| 6 | Kitchens manufacturing-time reword | **Not applied** — still reads "production and installation take 6–10 weeks", the contradictory version |
| 7 | Hallway & Utility double period | **Fixed** ✓ |
| 8 | MFC bracket (Kitchens, Wardrobe & Bedroom) | **Not applied** — still `MFC (Melamine Faced Chipboard` with no closing `)` |

(The `Raw/`-style Cyrillic-character scan also confirmed the hundreds of other Cyrillic characters on
every page are Tilda's own bundled JS comments (Russian-language developer comments, e.g. "close all
menus at this level") — platform boilerplate, not visible page content, not a site issue.)

## What did land correctly

- **Pricing/warranty/FAQ sections** (`Drafts/2026-09-21_Amfa_Missing-Pricing-Warranty-FAQ-Sections_v1.md`,
  row 11) are live and correct on all 3 previously-missing pages — Living & Media (now `/living-furniture`),
  `/custom-storage`, `/commercial-furniture` — FAQ question headings, pricing floors, and warranty text
  all match the confirmed draft.
- **Legal-page facts** are correct where not bracketed: company number `11259604`, registered office
  `6 Beverley Place, Wallsend` — matches the confirmed source facts.

## Site structure changes since the last review

Slugs changed and 3 new pages added since the `amfa.tilda.ws` preview:

- `/hallway-and-utility` → now `/hallway-furniture`
- `/living-and-media` → now `/living-furniture`
- **New:** `/bathroom`, `/home-office`, `/portfolio` — not covered by any prior Helen review; a first
  pass on these (voice, facts, typos) would be a reasonable next step but wasn't in scope for this
  fixes-verification pass.

## Sources

- `https://amfa.uk/` and all 15 linked pages — fetched directly via `curl`, 2026-09-24.
- `Drafts/2026-09-21_Amfa_Copy-Fixes_v1.md` — the 8-item fix list checked against.
- `Drafts/2026-09-21_Amfa_Missing-Pricing-Warranty-FAQ-Sections_v1.md` — the FAQ deliverable checked against.
- `Drafts/2026-09-21_Amfa_Privacy-Policy_v1.txt`, `Terms-of-Use_v1.txt`, `Legal-Pages_Brief.md` — the legal drafts checked against.
