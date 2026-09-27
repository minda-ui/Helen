# Change log — 2026-09-27 — Google Ads + GTM provisioning raised to Eugene; GTM tag/trigger plan drafted

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-27, item 2: GTM tag/trigger plan drafted

Minda asked for the GTM tag/trigger plan to be drafted now so it's ready the moment Eugene provisions `AWT-0132`, and whether more analytics from the website should be included.

Pulled the two live-site reviews (`Research/2026-09-21_Amfa_Live-Site_Pre-Launch-Review.md`, `Research/2026-09-24_Amfa_Live-Site_amfa-uk_Launch-Review.md`) for site structure — confirmed the site runs on Tilda, the "Get a free quote" CTA is a shared block on every page, and category page slugs (with one gap: Kitchens' exact slug was never confirmed in either review).

Delivered `Drafts/2026-09-27_Amfa_GTM_Tag-Trigger-Plan_v1.md`: GA4 base config; primary conversion (quote-form submission, 3 trigger options since Tilda's actual submit mechanism — redirect vs. AJAX vs. native event — isn't confirmed from stripped `curl` text); secondary conversion (phone `tel:` link clicks); page-view/category data that comes free with the base tag; and answered the "more analytics" question directly — recommended scroll depth and outbound-click tracking as optional/non-blocking additions, and explicitly recommended against e-commerce-style event tracking since Amfa sells bespoke quotes, not a catalogue. Flagged that Tilda may already have native GA4/GTM hooks worth checking before building anything custom, and listed 4 site facts the implementer needs to verify on the live DOM (something I can't do from stripped-text `curl` fetches).

Ledger row 23 added.

## Session — 2026-09-27, item 1: Google Ads + GTM provisioning raised

Minda asked directly to set up Google Ads and Google Tag Manager. Re-checked `ListConnectors` (full directory listing, not a keyword filter this time) — confirmed again: no Ads, GTM, Analytics, Search Console, or Business Profile connector exists anywhere in the org (`HI-8`, unchanged).

Explained the split to Minda: even with a connector, launching an Ads campaign / committing spend, and pasting a GTM snippet onto the live site, both still need a human regardless (charter §2b) — this gap is specifically about not having any way to reach the platforms at all yet, not about launch authority.

Minda's call: raise it on the Hub for Eugene to provision, rather than draft a manual setup runbook. Added `AWT-0132` (Tasks & Requests, Assigned to = Eugene, Requested by = "Helen (Minda-authorised 2026-09-27)", Priority Medium, Status Open) — this is outside Helen's normal own-rows-only Hub write scope (§2a), done here under Minda's explicit direct instruction rather than autonomously. Request asks for: (1) a Google Ads account/access for Amfa Furniture Ltd so the already-drafted campaign plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`) can be built once budget is approved; (2) a GTM container + GA4 property for `amfa.uk` for quote-form conversion tracking.

`HI-8` updated with this session's note. Nothing else changed — still no account access, still planning-only until Eugene hands back.

## Control files

`open-issues.md` (HI-8) and `processed-items-ledger.md` (row 23) updated after the above, in Drive (create-new + verify + trash-old, re-verifying `parentId` before each `trash_file` call per the `HI-5` lesson).
