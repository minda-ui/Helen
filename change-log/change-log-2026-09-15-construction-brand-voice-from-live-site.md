# Change log — 2026-09-15 — Construction Brand-and-Voice rebuilt from the live website (HI-4 resolved)

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-15: HI-4 resolved; `Brand-and-Voice/Fishbone-Construction-Ltd.md` rewritten

Fresh session. Re-tried the site that was `EGRESS_BLOCKED` earlier the same day: `WebFetch` and a raw
`curl` both reached `https://fishboneconstruction.co.uk` without issue. The block no longer applied —
not distinguished whether the environment's network policy was widened or a new session simply picked
up an already-updated one.

**Paused before treating the content as fact.** The homepage's "Featured Work" section names retail
clients **Rolex, Versace, Armani** next to "Residential Buildings," plus generic stats ("120+ projects
... in 8 countries," "Since 2012," ISO 9001). That looked more like unedited WordPress/Elementor demo
template content than real facts for a UK construction company, so this was flagged to Minda directly
rather than assumed either way, per the charter's truthful/substantiable-claims rule. Minda confirmed
it's real, not template filler.

**Corroboration found independently, after the confirmation:** the site names two directors —
**Mindaugas Gaudiesius** and **Andrejus Prutkovas** — matching Construction's own statutory director
records *and* the corrected co-founder names already on file for Amfa Furniture (see the
2026-09-14 name-correction entry). The "Fit Out" service line's own description — *"specialist
interior fit-out contractor services to some of the UK's biggest names across sectors such as retail,
commercial and leisure"* — also explains the brand-name portfolio: these are retail-unit fit-outs for
those brands' UK stores, not full construction contracts for the brands themselves. Fetched `/about-us/`,
`/our-services/`, `/our-work/`, and the `/our-work/rolex/` case page to fill out the picture.

**Rewrote `Brand-and-Voice/Fishbone-Construction-Ltd.md`** (previously trade/history facts only, no
brand identity or voice steer) with:
- Confirmed tagline, positioning line, and standfirst
- Real voice patterns with quoted examples, three differentiators
- The four real service lines (Builders Work up to £1m, Fit Out, Health and Safety/ISO 9001,
  Refurbishment), cross-referenced against the Construction KB's broader internal trade list
- Both process framings the site uses (3-phase and 6-step)
- The eight-project portfolio (Rolex, Armani, Versace, Superdry, Peloton, Sofa.com, Sushi Bar,
  Residential Buildings), with full case detail for Rolex
- The site's own stats (120+ projects, 8 countries, ISO 9001), cited as the company's own public
  claim rather than independently verified
- A carried-over caution not to draw Construction's financial/statutory KB material into marketing
  copy

Added **`HSRC-08`** (the live website) to `external-source-register.md`. Updated
`Brand-and-Voice/README.md` (Construction now "well underway," matching Amfa's status) and `HI-3`/`HI-4`
in `open-issues.md`. Mirrored `AWT-0011` to Done on the Hub `Tasks & Requests` sheet (row
`32778681452420`).

**Open / next.** This unblocks `AWT-0006` (Construction case study — now has real portfolio material to
draw a first piece from) and the Construction portion of `AWT-0007` (social posts). Both companies'
exact brand colours/logo source files remain open questions for Minda. `current-state.md` updated.
