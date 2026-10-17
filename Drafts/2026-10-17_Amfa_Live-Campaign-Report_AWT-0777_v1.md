# Amfa live campaign report — AWT-0777

**Company:** Amfa Furniture Ltd · **For:** Minda (via Victoria) · **Date:** 2026-10-17 · **By:** Helen · **Status:** ready for review
**Method:** read-only checks of the Google Ads account and GA4 via Composio, and of the live site. Nothing changed anywhere.

## Bottom line
The campaign has run for 18 days and has **shown no ads: 0 impressions, 0 clicks, £0 spend.** The website has **no way to count enquiries**: no conversion event for the quote form exists, and the form's submit event has never fired. So today we can't measure qualified enquiries per week, and the paid campaign isn't the cause of any traffic.

## 1. What is running
- **Account:** AMFA Furniture Ltd (`146-806-8988`), enabled, billing approved.
- **Campaign:** "Amfa - Bespoke Kitchens - Search" — the only one. Search, live since 30 Sept, **£25/day**, Maximise Clicks (no CPC cap).
- **Targeting:** 7 named locations plus a 50-mile radius around NE28 6HA; English; all devices. 11 negative keywords.
- **Ad groups and keywords:** "Ad group 1" — 13 keywords, 7 `ELIGIBLE`, 6 `RARELY_SERVED`. **"Fitted Kitchens"** — added today, 7 phrase keywords, 4 `ELIGIBLE`, 3 `RARELY_SERVED`, all still under review.
- **Ads:** 2 responsive ads, both `APPROVED`. **Landing pages:** `amfa.uk` homepage (Bespoke ad group) and `amfa.uk/kitchens` (Fitted Kitchens).

## 2. Results to date
**Impressions 0 · clicks 0 · CTR – · CPC – · spend £0.00 · conversions 0.** No day since launch has any activity. Every layer I can read is healthy; the likeliest cause is very low search volume for these terms, but that is unproven. See `HI-8`.

## 3. Tracking
- **GA4:** property for `amfa.uk` (`556194113`), receiving data since 29 Sept — 272 sessions, 223 users.
- **GTM:** container `GTM-WLTMKHP5` and the GA4 tag (`G-NGNVVHFEB5`) are installed on the pages I checked (home, kitchens, contacts).
- **Conversion events: none that matter.** GA4's 3 key events are Google's defaults — `purchase`, `qualify_lead`, `close_convert_lead` — none is a quote-form enquiry. Google Ads holds the same 3, all hidden.
- **Does the form fire? No evidence it does.** GA4 recorded `form_start` twice (1–2 Oct) and **`form_submit` zero times** in 18 days. This is likely a measurement gap, not proof of no enquiries: the site's form is a Tilda form, and Tilda's submit may not be detected automatically. I can't prove either way without a real test enquiry.
- **GA4 ↔ Ads link:** linked on 30 Sept. GA4 shows no Ads campaign or ad-group names on any session, which fits zero clicks.

## 4. Enquiries
- **How many, from where:** **I can't see this.** The enquiry mailbox is outside my access, and GA4 has no conversion to count. Please ask whoever sees `enquiries@amfa.uk` for the number since 30 Sept and where each came from (form, phone, WhatsApp, Instagram).
- **Is `enquiries@amfa.uk` connected, and who sees it?** I can't check. The form's recipient is set inside Tilda, which I can't open.
- **Cost per enquiry:** not applicable — spend is £0.

**The traffic that does exist (29 Sept – 17 Oct):** 258 of 272 sessions are "direct". About 130 sessions landed on a Tilda preview address (`/?ref=…tilda.cc…`) — likely site-editing, previews or bots, not customers (unverified). 4 sessions came from Instagram, 1 from organic search. 8 are labelled "google / cpc" (Paid Search): all desktop, no country, none engaged — consistent with Google's crawlers checking the landing pages after launch (likely, not proven), **not real ad clicks**. Few visits reach a product page.

## 5. Recommendation (one measure: qualified enquiries per week)
1. **Fix measurement first.** Add a quote-form conversion event in GTM (via the form's success event or a thank-you page), mark it a GA4 key event, then import it to Ads. Then run **one real test enquiry** and confirm it fires. Until then the measure can't be read. I can write the exact GTM steps; you or the developer apply them.
2. **Get the Ads facts.** Ad preview and diagnosis on `kitchens Newcastle`, plus Keyword Planner volumes (plan steps 1–2, still open). They show why nothing is showing.
3. **Don't add budget yet.** Funding from 21 Oct is your call; with 0 impressions, more money buys nothing. The right order is: impressions → clicks → measured enquiries → then spend.
4. **Keep testing breadth.** Fitted Kitchens (live today) and Wardrobes (`CR-GA-0003`, awaiting you) test other terms on the same budget.
5. **Before more traffic:** the site developer should apply the copy and legal-page fixes (ledger rows 16/17/20) and the delivery wording.
6. **If the answer is still no impressions after 2–3 weeks,** treat Google Search as the wrong channel for this niche and discuss Instagram/Meta, which is already sending a few visitors, and Google Business Profile.

## What I could not see or check
- Enquiries: the mailbox, the form's recipient, and phone or WhatsApp enquiries.
- Inside GTM: no connector exists, and Google's published container file is blocked for this session, so I only know the container is installed, not what tags and triggers it holds.
- Whether the form fires: needs a real test enquiry. I will not submit one on the live site myself.
- Meta/Instagram activity, and the Tilda admin.

_Sources: Google Ads account `1468068988` and GA4 property `556194113` (read-only, 2026-10-17); live `amfa.uk`; `open-issues.md` `HI-8`; `Drafts/2026-10-09_Amfa_GoogleAds_Impressions-Plan_v1.md`; hand-off notes in `Raw/` dated 2026-10-15._
