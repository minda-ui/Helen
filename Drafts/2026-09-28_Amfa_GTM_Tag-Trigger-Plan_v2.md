# GTM/GA4 setup — Amfa Furniture Ltd, amfa.uk — as built (v2)

**Company:** Amfa Furniture Ltd
**Status:** GA4 property and GTM container are live and configured. Only step remaining: install snippet on the site (developer/CMS task, not Helen's — no CMS access, charter §2b). Supersedes `Drafts/2026-09-27_Amfa_GTM_Tag-Trigger-Plan_v1.md` (archived), which was a blind plan written before GA4/GTM access existed — this file records what was actually built, 2026-09-28, guided live in-browser with Minda.

---

## 1. What's live

- **GA4 property:** account "Amfa Furniture Ltd", property `amfa.uk`, Measurement ID `G-NGNVVHFEB5`. Enhanced Measurement **on** — auto-tracks page views, scrolls, outbound clicks, site search, video engagement, file downloads, and **form interactions** (form_start/form_submit).
- **GTM container:** `GTM-WLTMKHP5`. One tag, **"GA4 - Base Configuration"** (type "Google Tag" — Google's current name for what used to be "GA4 Configuration"), Tag ID `G-NGNVVHFEB5`, trigger **Initialization - All Pages**. Published as Version 2, live.
- **Composio Google Analytics connection** (`helen-google-analytics`, ACTIVE) — Helen can pull real GA4 reports once data starts flowing. No equivalent for GTM — Composio has no GTM toolkit at all (checked, confirmed absent).

## 2. What's still needed

**The install snippets.** Admin → Install Google Tag Manager in the GTM UI gives two code blocks (`<head>` and post-`<body>`). These need pasting into `amfa.uk` by whoever holds CMS/Tilda access — Helen has none. Nothing tracks until this happens.

## 3. Conversion tracking — likely already solved, verify before building anything custom

The original plan (v1) assumed custom GTM triggers would be needed for the quote-form submission, with three fallback options because Tilda's exact submit mechanism was unconfirmed. **That's probably unnecessary now**: GA4's Enhanced Measurement `form_submit` event fires on the browser's native form submit event regardless of what JS handles it underneath (AJAX or not), so it should catch the quote-form submission automatically, with zero custom trigger work.

**After the install snippet is live, verify rather than assume:**
1. Submit a real test quote-form request on `amfa.uk`.
2. Check GA4 **Realtime** reports for a `form_submit` event.
3. **If it fires** — done. Mark `form_submit` as a GA4 conversion event (Admin → Events → toggle "Mark as conversion"), or use GA4's own suggested `generate_lead` event if the Enhanced Measurement event carries enough context to map to it. No GTM work needed.
4. **If it doesn't fire reliably** — fall back to the v1 plan's custom-trigger options (thank-you page URL, Tilda's own dataLayer event if it has one, or GTM's Form Submission trigger) — see the archived v1 draft for the full detail on each.

Phone clicks (`tel:` links) are covered the same way — Enhanced Measurement's outbound-click tracking catches these automatically; verify with a real click and check Realtime for a `click` event with the phone link URL.

## 4. Once Ads access clears (still payment-blocked, see `HI-8`)

1. Link the GA4 property to the Google Ads account (Ads UI → Tools → Linked accounts).
2. Import the conversion event (`form_submit` or `generate_lead`) as a Google Ads conversion action.
3. Set Ads bidding/reporting against that imported conversion, not raw clicks — matches the "switch to Maximize Conversions once tracking is live" guidance in the campaign plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` §7).

## Sources

- Live build session, 2026-09-28 — GA4 property/GTM container/tag creation, guided step-by-step via screenshots.
- `Drafts/2026-09-27_Amfa_GTM_Tag-Trigger-Plan_v1.md` (archived) — original blind plan; the "what to check on the live site" and naming-convention sections there still apply if custom triggers turn out to be needed.
- `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` — ad-group structure, the conversion-tracking gap this closes.
- `open-issues.md` `HI-8` — full history of the GA4/GTM/Ads access saga.
