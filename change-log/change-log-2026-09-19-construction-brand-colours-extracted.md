# Change log — 2026-09-19 — Construction brand colours extracted from logo file

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-19: pixel-extracted green/grey from Little logo.jpg

Minda asked Helen to extract the brand colours from the confirmed Construction logo file. Retried
`Fishbone Logo.tif` (the master) once more via the Microsoft 365 connector — still returns empty content,
can't be opened this way. Worked instead from `Little logo.jpg`, which was already downloaded locally
from the earlier OneDrive check.

**Method:** downloaded image analysed with Python/Pillow (installed this session) — not a visual guess.
Filtered out near-white background pixels, separated the remainder into a green family (G channel
dominant) and a grey family (near-neutral R≈G≈B), then computed the most-repeated (modal) tone in each
family as the representative colour.

**Result:**
- Green: `#74C800` (RGB 116, 200, 0) — dominant, most-repeated tone, a bright lime/apple green.
- Grey: `#A8A8A8` (RGB 168, 168, 168) — a mid-tone pick. The file actually renders the grey as a glossy
  gradient from `#808080` (shadow) to `#DCDCDC` (highlight), not one flat tone, so this is a
  representative midpoint rather than a single measured flat colour.

**Caveat flagged clearly:** `Little logo.jpg` is a glossy 3D sticker-style rendering (gradient shading
per icon), not a flat vector logo — so these hex values are the best extractable estimate from this
specific file, not confirmed "official" brand colours. The master `.tif` couldn't be cross-checked. Asked
Minda to confirm these as final before they're treated as locked brand colours.

**Updated:**
- `Brand-and-Voice/Fishbone-Construction-Ltd.md` — full colour table + method + caveat added to the
  "Logo & visual identity" section
- `external-source-register.md` (`HSRC-09`) — colour extraction noted
- `Brand-and-Voice/README.md` — Construction's status line updated (colours now extracted, pending
  owner sign-off)
- `open-issues.md` (`HI-3`) — Construction's Brand-and-Voice gap now reads as fully closed, with the
  colour-confirmation caveat noted

**Open / next.** Get Minda's sign-off that `#74C800`/`#A8A8A8` are usable as final brand colours, or
have her supply official values if a canonical brand guideline exists elsewhere. Amfa's logo/colour gap
is still open and untouched by this session.
