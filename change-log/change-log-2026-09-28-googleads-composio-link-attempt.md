# Change log — 2026-09-28 — Google Ads Composio link attempt; live campaign build assisted; GA4/GTM built

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-28 (continued): GA4 + GTM built live, Composio Analytics connected

While Ads sat paused on payment verification, Minda moved to Google Analytics and Tag Manager setup — both proceed independently since neither needs billing.

**GA4:** guided the full account/property creation flow (Account creation → Property creation → Business details → Business objectives → Data collection). Account "Amfa Furniture Ltd", property `amfa.uk`, UK timezone/GBP, industry Home & Garden, objective "Generate leads", Web platform, Measurement ID `G-NGNVVHFEB5`. Enhanced Measurement left on (auto-tracks page views, scrolls, outbound clicks, form interactions — a real finding: this likely makes the elaborate custom-trigger plan in the original GTM draft unnecessary, since GA4's built-in `form_submit` event should catch the quote-form submission automatically regardless of Tilda's exact submit mechanism).

**Composio Google Analytics connection**: linked (`helen-google-analytics`), status `ACTIVE` — unlike the Ads connection, no hold. Verified it actually works via `GOOGLE_ANALYTICS_LIST_ACCOUNT_SUMMARIES`, which returned the real Amfa account and `amfa.uk` property (`properties/556194113`). `HI-8` updated: GA4 read/report access is now genuinely live for Helen.

**Checked for a Composio Google Tag Manager toolkit — confirmed none exists.** `composio search` for GTM returns nothing toolkit-specific; every plausible slug (`googletagmanager`, `google_tag_manager`, `tagmanager`, `gtm`) fails to even create a pending connection (unlike real toolkits, which show a connection object before authorization); a broader capability search turns up nothing relevant. Not a session-side bug — Composio simply doesn't offer this integration.

**GTM built directly in the browser instead.** Container `GTM-WLTMKHP5` under the same "Amfa Furniture Ltd" account. Guided one tag: "GA4 - Base Configuration", type "Google Tag" (Google's current name for what used to be called "GA4 Configuration" — the UI has changed; the other option, "GA4 Event", is for custom events and needs the base tag already present, so a wrong first pick got corrected). Tag ID `G-NGNVVHFEB5`, trigger "Initialization - All Pages" (auto-populated). Hit one generic "stale data" error mid-build — resolved by refresh-and-retry per Google's own error message. **Published as Version 2, live.**

Only step left: the two install snippets (`<head>`/`<body>`) need pasting into `amfa.uk` by whoever holds CMS access — Helen has none (charter §2b). Rewrote the GTM tag/trigger plan as `Drafts/2026-09-28_Amfa_GTM_Tag-Trigger-Plan_v2.md` — an "as-built" record replacing the blind v1 plan, with the key instruction to verify `form_submit` fires in GA4 Realtime after install before building any custom triggers, rather than assuming the v1 plan's complexity is still needed. `Drafts/2026-09-27_Amfa_GTM_Tag-Trigger-Plan_v1.md` archived (superseded, not deleted).

`open-issues.md` (`HI-8`) updated throughout with each step. Ledger row 27 covers the whole session (Ads build + pause, GA4/GTM build).

## Session — 2026-09-28 (continued): live campaign build in Google Ads UI, budget confirmed

Despite the Composio API connection sticking at `INITIATED` (see below — a Google-side hold on the API/OAuth route specifically), Minda had separate direct browser access to the Google Ads UI (`ads.google.com`) and worked through "Create your first campaign" live, sharing screenshots at each step for guidance. Assisted end-to-end: campaign goal/type, bid strategy (Clicks, not Maximize Conversions — no conversion tracking live), locations (caught it defaulting to United States — corrected to Newcastle/UK), networks (Search only, Display unchecked), keywords (phrase match, from the campaign plan), the Bespoke Kitchens ad (headlines/descriptions), a WhatsApp message asset, and all 6 sitelinks with descriptions.

**Errors caught along the way:**
- **Character-count errors in the original campaign plan** — 5 Bespoke Kitchens headlines, 1 Fitted Kitchens headline, and 4 descriptions across both were over Google's actual limits (30/headline, 90/description). Re-counted every one character-by-character and corrected `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` in place (Drive + git). See separate ledger row.
- **Sitelink typo**: "Get a Free Qoute" caught and fixed to "Get a Free Quote" before save — same typo already flagged as an unapplied site-copy fix elsewhere in this KB, apparently recurring independently.
- **WhatsApp number (07392592864) flagged, then confirmed genuine** — live on the `amfa.uk` site header alongside the landline (01916052945). Not a stale number.
- **Kitchens landing pages resolved**: not separate pages as assumed — `amfa.uk/kitchens` with anchors `#bespokekitchen`/`#fittedkitchen`. Fetched via `WebFetch` and passed on; also gave the "Get a Free Quote" sitelink URL (`amfa.uk/contacts`).

**Budget confirmed by Minda: £25/day** for the Bespoke Kitchens ad group (only ad group live so far; Fitted Kitchens/Wardrobe/Bathroom Vanity still to be added), toward the lower end of the campaign plan's illustrative £600–£1,500/month range since only one of the four launch ad groups is running. `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` §7 updated to record this as a real, confirmed decision rather than illustrative guidance.

Campaign build then paused at "Enter payment details" — Google Ads blocking the payment method, likely the same new-account verification pattern as the Composio hold. Everything else in the campaign is fully built and saved.

## Session — 2026-09-28: Composio Google Ads link attempt, 5-day hold

Handed over the Amfa Google Ads campaign plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`) for Minda's first-campaign setup. She then asked to try connecting Google Ads via Composio directly (parallel route to `AWT-0132`, the provisioning request already sitting with Eugene).

No existing Google Ads connection anywhere in the org (`composio link googleads --list` → empty). Started a fresh link (`--alias helen-googleads --no-browser --no-wait`); Minda authorised via the printed URL. Checked status (`composio connections list --toolkit googleads`) — stuck at `INITIATED`, never reached `ACTIVE`. Minda reports Google's own flow told her a 5-day wait applies before proceeding further — a Google-side account/API review hold, not a Composio or Helen-side failure.

`open-issues.md` (`HI-8`) updated with this finding. Both routes to Ads access — Eugene's `AWT-0132` provisioning and this Composio link — may now be gated behind the same Google-side wait; nothing to configure from either until one clears. **Note (later same day):** this hold appears specific to the API/OAuth connection — Minda has separate, working direct browser access to the Google Ads UI and built the campaign there instead (see above).
