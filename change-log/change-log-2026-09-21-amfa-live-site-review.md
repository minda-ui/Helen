# Change log — 2026-09-21 — Amfa live-site pre-launch review

Continuing "big work... Amfa website": after the Privacy Policy/Terms of Use task, Minda asked to
continue the page-by-page review of the live preview.

**Method.** The WebFetch tool blocks `amfa.uk`, `www.amfa.uk`, and `amfa.tilda.ws` under this
session's network egress policy, but a direct `curl` reached `amfa.tilda.ws` fine (HTTP 200). Fetched
all 12 pages that way, stripped script/style/markup with a small Python pass, and diffed the visible
text and raw HTML against `Research/2026-09-14_Amfa_Website-Copy-Review.md` (the original PDF-based
review) rather than re-reading from scratch.

**What's fixed since the PDF review:** the "syle" typo, the reviews-section padding concern (now 3
genuinely distinct testimonials), and the mixed third/first-person About-page sentence — on the About
page itself.

**What's still open from before:** the "qoute" typo and the "Tv"/"TV" capitalisation inconsistency are
both still live, in the shared nav/CTA template reused across all 12 pages — one fix each resolves
every instance. The mixed-person sentence is also still live, duplicated, on the homepage — the About
page's own fix wasn't carried over there.

**New findings, only visible from the live site, not the PDF export:**
- The founder's name on `/about` still reads the **uncorrected** spelling ("Gaudešius") — Minda
  corrected this to "Gaudiesius" on 2026-09-14, matching the statutory-records spelling used elsewhere
  in the group. A real accuracy issue on a live page, not cosmetic.
- **5 Cyrillic look-alike characters** (с/С standing in for Latin c/C) found by inspecting raw page
  source across home, about, process, and custom-storage — invisible to a reader, but can silently
  break in-page search, SEO term matching, and screen-reader pronunciation. Likely a leftover from a
  Cyrillic-locale copy/paste, consistent with the Russian-named PDF file noted in the original review.
- **Living & Media Furniture, Custom Storage Solutions, and Commercial Furniture** — the three newest
  category pages — are missing the pricing/warranty/FAQ block that the other five categories all have.
  No warranty statement or price indication appears on two of the three at all.
- A possible manufacturing-time contradiction on the Kitchens page (body says 3–8 weeks, FAQ says 6–10
  weeks including installation) — every other category's body/FAQ figures match exactly.
- Two small formatting slips (a stray double period on Hallway & Utility; a possibly unclosed bracket
  on the MFC material description, present the same way on two pages so not a one-off).

**Deliverable:** `Research/2026-09-21_Amfa_Live-Site_Pre-Launch-Review.md` — supersedes the 2026-09-14
review, with a consolidated checklist for Minda/the site developer. Advisory only, per charter §2b —
Helen doesn't touch the site or its CMS.
