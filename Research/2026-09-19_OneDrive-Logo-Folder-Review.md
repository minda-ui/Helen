# Research note — OneDrive `/LOGO` folder review

| Field | Value |
|---|---|
| Requested by | Minda, 2026-09-19 — "check folder /Logo on OneDrive to get more information about the available groups Logo's" |
| Source | `HSRC-09` — Group OneDrive/SharePoint `/LOGO` folder (`fishbonedrylining-my.sharepoint.com/personal/info_fishbonedrylining_onmicrosoft_com/Documents/LOGO`), via the Microsoft 365 connector |
| Purpose | Close the "exact brand colours/logo file" gap flagged in `Brand-and-Voice/README.md` for Construction and Amfa |
| Outcome | Logo files confirmed for **Construction** (both by Minda) and found (unconfirmed but well-labelled) for **Properties**. Nothing for **Amfa**. Two unfinished concepts for **Waste**. Several apparent leads ruled out as unrelated noise. |

---

## What's in `/LOGO`

**Fishbone Construction Ltd** — confirmed by Minda, 2026-09-19:
- `Fishbone Logo.tif` — the master file. Created 2019-04-07, minutes after the `/LOGO` folder itself was created — clearly the original.
- `Little logo.jpg` — a small version of the same logo, per Minda. Visually a fishbone-skeleton icon motif in green and grey.

Neither file's exact colour values (hex/Pantone) have been extracted — the `.tif` isn't directly viewable through the connector used to check it, and eyeballing a `.jpg` isn't a substitute for real values. Filed the gap as still open in `Brand-and-Voice/Fishbone-Construction-Ltd.md`.

**Fishbone Properties Ltd** — well covered, not yet owner-confirmed but unambiguous from filenames:
`Fishbone Properties Logo 2021.pdf`, `Fishbone Properties Logo 2021 small.pdf`, plus JPG variants
(`Fishbone Properties Logo 2021 small.jpg`, `small 2.jpg`, `Fishbone properties logo1 (1).jpg`).

**Fishbone Construction — templates, not raw logo files:** `Fishbone Construction Main template 2026.pdf`,
`Fishbone Construction Main template 2024.pdf`, and the predecessor-era `Fishbone Drylining Main Template 2021.pdf`
(matches the pre-rename company name recorded in `Brand-and-Voice/Fishbone-Construction-Ltd.md`). These are
branded document templates that presumably embed the logo, not a standalone source file — the two files above
are the actual raw logo assets.

**Fishbone Waste Ltd** — a `/LOGO/Fishbone waste/Waste removal working files/` subfolder holds two unfinished
logo concepts: `Logo with single circle.ai` and `Logo with double circle.ai` (+ a `.pdf` export of the
double-circle version), plus `White and transparent background.ai`. Read as design proofs/variants, not a
finalised mark — Waste is dormant per the charter anyway, so not pursued further.

**Amfa Furniture Ltd** — no Amfa-named file anywhere in this folder. Consistent with Amfa being a 2024
company; this OneDrive looks like the older Fishbone Drylining-era file store. Amfa's logo gap stays open;
would need a different source (Minda directly, or wherever Amfa's own materials live).

## Ruled out (initially ambiguous, opened and checked individually)

Several generically-named files matched a loose "logo" search but turned out unrelated on inspection:
- `logo.png` ×2 — both the **1&1 IONOS** hosting-company logo
- `logo.jpg` — a **"Mad 4 Toys"** retail toy-brand logo
- `logo.bmp` — a leftover file from an old *Transport Tycoon Deluxe* game install (per its own webUrl path: `.../Desktop/old computer storage drives/.../Transport Tycoon Deluxe/logo.bmp`)

Also excluded as noise without opening (search-only signal, generic ad/stock names, no Fishbone connection):
`criteo_logo_2021.svg`, `game-logo.png`, `sa_logo_300x250.png`, `atostogos 470.jpg`, four `WhatsApp Image...jpg` files.

## Method note

The Microsoft 365 connector's `sharepoint_folder_search`/`sharepoint_search` tools don't reliably restrict
results to one folder — a `folderName` filter still surfaced unrelated files from elsewhere on the drive
(tax/SSAS financial documents, mortgage statements) when searching broadly for "logo". Those were not
opened or used — irrelevant to this task and, for the SSAS/financial ones, outside what Helen should ever
touch per charter §2b regardless. Reliable folder-scoped results came from resolving the `/LOGO` folder's
own item and cross-referencing `webUrl` paths that explicitly confirmed `/Documents/LOGO/...`.

## Sources

- `HSRC-09` — Group OneDrive `/LOGO` folder, Microsoft 365 connector, checked 2026-09-19
