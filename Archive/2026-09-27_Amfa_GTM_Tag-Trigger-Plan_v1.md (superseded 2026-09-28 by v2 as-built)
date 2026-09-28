# Draft — GTM tag/trigger plan (Amfa Furniture Ltd, amfa.uk)

**Company:** Amfa Furniture Ltd
**Channel:** Google Tag Manager + GA4 — conversion tracking for `amfa.uk`
**Brief:** Minda, 2026-09-27 — ready for whoever implements once `AWT-0132` is provisioned.
**Status:** Planning only. No GTM/GA4 connector or account access exists (`HI-8`) — this is a spec for a human to build, not something I've configured. I also can't see the site's raw HTML/DOM (I've only ever fetched stripped text via `curl`), so exact element IDs/selectors below are marked **[TO VERIFY]** — the implementer needs to inspect the live page source first.

---

## 0. Check this first — Tilda may already do some of this

`amfa.uk` runs on **Tilda** (confirmed: prior review pages were served from `amfa.tilda.ws`, and raw HTML carries Tilda's own bundled JS). Tilda has a built-in "Analytics & Metrics" panel in its site settings that supports pasting a GA4 measurement ID or GTM container ID directly, and can fire form-submission events natively without any custom trigger work. **Before building custom triggers below, check Tilda's own site settings for:**
- An existing GA4/GTM ID already entered (Privacy Policy §3 flagged "whether this policy needs updating if analytics/marketing tools are added later" — suggesting none was configured as of the 2026-09-26 legal-page pass, but worth a direct check, not an assumption).
- Tilda's native "Form analytics" or e-commerce event options, which can push a `tildaFormSuccess`-type event to `dataLayer` automatically on submit.

If Tilda already pushes a submit event to `dataLayer`, most of §2 below is a GTM-side trigger listening for that existing event, not new instrumentation on the page.

---

## 1. GA4 base setup

- One GA4 property for `amfa.uk` (not yet created — part of `AWT-0132`).
- One GTM container for `amfa.uk`, published as a single container snippet (head + body) — **pasting it onto the live site needs whoever holds Tilda/CMS access; I don't have it (charter §2b)**.
- **GA4 Configuration tag** — fires on **All Pages**. This alone gives page views, sessions, geography, device, and traffic source for free — no extra tagging needed for basic visit/traffic data.

## 2. Conversion events — priority order

### 2a. Primary conversion: quote-request form submission
The "Get a free quote" CTA is a **shared block reused on all pages** (per the site review) — one implementation point covers every entry page.

- **Trigger (pick whichever matches how Tilda actually submits the form — verify, don't assume):**
  - **Option A — Thank-you/confirmation page load.** If submitting redirects to a distinct URL (e.g. `/thank-you`), a **Page View** trigger on that URL is the simplest, most reliable option. **[TO VERIFY: does submission redirect, or show an inline confirmation on the same URL?]**
  - **Option B — Tilda's native form-success event.** If Tilda pushes its own `dataLayer` event on AJAX submit (see §0), a **Custom Event** trigger listening for that event name. **[TO VERIFY: exact event name Tilda uses, if any.]**
  - **Option C — GTM's built-in Form Submission trigger.** Only reliable if the form is a plain HTML form with a real page load on submit; Tilda forms are usually AJAX, so this is the least likely to fire correctly — treat as fallback, not first choice.
- **GA4 event name:** `generate_lead` (GA4's own recommended event for this) or a custom `quote_request_submit` — recommend `generate_lead` so it's automatically eligible as a suggested/recommended conversion in GA4 without extra config.
- **Mark as a GA4 conversion event**, then **import into Google Ads** as the primary conversion action ("Amfa – Quote Request") once both accounts exist and are linked.

### 2b. Secondary conversion: phone number clicks
Older/local trade-service audiences often call rather than fill a form — worth tracking as its own signal, not folded into the form conversion.
- **Trigger:** Click trigger on `tel:` links — matches Click URL `contains tel:`. The Ads campaign plan's call extension (`01916052945`) and any on-page phone number use the same link pattern, so one trigger should catch both.
- **GA4 event name:** `phone_click` (custom event, or GA4's own `click` event with a `link_url` parameter filter). Mark as a **secondary** GA4 conversion — don't let it dilute the primary lead-form conversion in Ads bidding.

### 2c. Free with the GA4 base tag — no extra work
- **Page views by category** (`/kitchens`, `/wardrobe-bedroom`, `/bathroom`, `/home-office`, `/hallway-furniture`, `/living-furniture`, `/custom-storage`, `/commercial-furniture` [TO VERIFY exact Kitchens slug — not confirmed in any prior review]) come through automatically via `page_path` — useful for seeing which service line draws interest, ties back to the 8-ad-group Ads structure. No custom tag needed, just don't accidentally exclude these paths from reporting.
- **Traffic source / campaign attribution** — automatic once UTM-tagged Ads URLs land on the site (standard `gclid`/UTM auto-tagging via the Ads↔GA4 link, not something to hand-build).

### 2d. Optional additions (recommended, not blocking)
Answering the "do we need more analytics" question directly — beyond the two conversions above, these are worth having but shouldn't hold up launch:
- **Scroll depth on category pages** — GTM's built-in Scroll Depth trigger (e.g. 75%/90%), useful for seeing whether visitors reach the pricing/warranty/FAQ section before leaving. Low effort, genuinely useful for CRO later.
- **Outbound clicks** — to the Portfolio page's project links or any social/Google Business Profile link, if present. Lower priority; only worth it once the core two conversions are live and stable.
- **Not recommended right now:** e-commerce-style tracking (product views, add-to-cart) — Amfa doesn't sell off a catalogue, everything is a bespoke quote, so GA4's e-commerce event set doesn't fit the actual customer journey. Skip it rather than force-fitting it.

## 3. Naming conventions (for a clean handoff)
- Tags: `GA4 - <purpose>` (e.g. `GA4 - Config`, `GA4 - Quote Request`, `GA4 - Phone Click`)
- Triggers: `<Type> - <purpose>` (e.g. `Page View - Thank You`, `Click - Tel Links`, `Custom Event - Tilda Form Success`)
- Variables: prefix `DLV -` for any `dataLayer` variable pulled in (e.g. `DLV - form_name` if Tilda's event carries one)

## 4. What Eugene / the implementer needs to check on the live site
I can't confirm these without DOM/CMS access — flagging so nothing gets built on an assumption:
1. Does Tilda already have GA4/GTM wired into its own site settings?
2. Does the quote-form submission redirect to a thank-you URL, or confirm inline?
3. Exact URL slug for the Kitchens category page (not confirmed in any prior review — every other category slug has been verified, this one hasn't).
4. Whether the phone number in the header/footer is a live `tel:` link or plain text.

## 5. Once GA4 + Ads both exist
1. Link the GA4 property to the Google Ads account (Ads UI → Tools → Linked accounts).
2. Import `generate_lead` as a Google Ads conversion action.
3. Set Ads bidding/reporting against that imported conversion, not raw clicks.
4. Revisit the Ads campaign plan (`Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` §8) — this closes that plan's outstanding conversion-tracking gap.

## Sources
- `Research/2026-09-24_Amfa_Live-Site_amfa-uk_Launch-Review.md`, `Research/2026-09-21_Amfa_Live-Site_Pre-Launch-Review.md` — site structure, shared CTA block, Tilda platform confirmation, category page slugs.
- `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md` — ad-group structure, conversion-tracking gap this plan closes.
- `open-issues.md` `HI-8` — no GA4/GTM connector provisioned; `AWT-0132` raised to Eugene.
- Tilda's own analytics-integration capability — general platform knowledge, not confirmed for this specific site's configuration; flagged as something to check, not assume.
