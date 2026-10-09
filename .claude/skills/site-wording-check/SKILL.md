---
name: site-wording-check
description: Check what the live amfa.uk site says about a topic (service area, delivery, pricing, warranty…) across every page, compare it with the Brand-and-Voice file, and draft exact find/replace lines for the site developer. Use before paid traffic goes to the site or when a campaign setting changes.
---

# site-wording-check

Helen has **no CMS access** — she reports and drafts; the developer applies.

## Steps
1. Fetch the homepage and list internal links: `curl -fsSL https://amfa.uk/` then collect `href="/…"` paths (currently 15 pages, e.g. `/about`, `/kitchens`, `/process`, `/contacts`, `/privacy-policy`).
2. Fetch every page into a scratch folder (`curl -fsSL -m 30 -o <name>.html`). Pages are large (~2.6 MB, Tilda) — normal.
3. Strip to visible text with `python3 -I`: remove `<script|style|noscript|svg>` blocks, replace tags with newlines, `html.unescape`, collapse whitespace, de-duplicate lines.
4. Search with a pattern for the topic (e.g. `miles|radius|service area|deliver|North East|Newcastle`) and print hits per page.
5. Compare with `Brand-and-Voice/Amfa-Furniture-Ltd.md` and the campaign settings.
6. Report: matches, contradictions, undefined terms ("full service area"), vague wording.
7. For each fix, write **Find (exact live text)** and **Replace with**, plus why. File as `Drafts/YYYY-MM-DD_Amfa_<Topic>-Wording-Fix_vN.md`; send to Minda for the developer.
8. If Minda confirms a business fact, add it to the brand file (cite her, with the date). Don't invent policy — ask.

## Notes
- Stray Cyrillic look-alike characters appear in some live copy; copy exact text from the fetch.
- Leave the Sales T&Cs alone until the solicitor review (`HI-9`).
