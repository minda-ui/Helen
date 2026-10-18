# Amfa quote-form tracking — event spec and one-enquiry test plan (v1)

Status: **ready for review (Minda / Eugene)** — draft only. Hub row: AWT-0828 (Eugene's guide: AWT-0827).
Sources: `Drafts/2026-09-28_Amfa_GTM_Tag-Trigger-Plan_v2.md` (GA4 property `amfa.uk`, `G-NGNVVHFEB5`, Enhanced Measurement on; `form_submit` seen as unverified), Hub row AWT-0828.

## 1. Measure Helen owns
**Qualified enquiries per week** from the quote form on amfa.uk.

## 2. Event spec (for Eugene's guide)
- **Event name:** `generate_lead` (GA4 recommended event; mark as a **key event**; import into Google Ads as the conversion action).
- **Why not rely on Enhanced Measurement `form_submit`:** it fires on any form on the site and is unverified for Tilda. A dedicated event on the quote form's success state counts only real enquiries.
- **Parameters:** `form_name` = `quote_request`; `form_location` = page path; `currency` = `GBP` only if a value is later agreed (do not invent a lead value). No personal data (name, email, phone, message text) in any parameter.
- **Fire condition:** on successful submission of the quote form only (thank-you state / Tilda success event), not on form_start or failed submits. Eugene to choose the trigger mechanism and confirm it in the guide.
- Fallback if `generate_lead` cannot be wired: key-event the existing `form_submit` filtered to the quote form, and say so on the row.

## 3. One-enquiry test plan (Minda or developer runs it; Helen only reads)
1. **Before:** open GA4 → Admin → DebugView (or Reports → Realtime) in one tab; GTM Preview optional.
2. **Enter in the live form (clearly marked TEST):** Name `TEST – Do Not Contact`; message `TEST ENQUIRY – tracking check, please ignore, 2026-10-xx`; product/field choices: any; **email/phone: a Fishbone-owned inbox Minda nominates (e.g. her own)** — not a customer's. Minda to confirm the address and phone to use.
3. Submit once, from a normal browser on amfa.uk (not logged-in admin tools, no ad blocker), noting the time.
4. **Helen then checks (read-only):**
   - GA4 Realtime/DebugView: one `generate_lead` event with `form_name=quote_request`, no duplicate, no personal data in parameters.
   - GA4 Admin → Events: `generate_lead` marked as a key event.
   - Google Ads (after ≥24h): conversion action present/imported, status receiving data; expected 0 ad-attributed conversions since the test is not from an ad click.
5. Afterwards Minda removes/flags the test enquiry in whatever inbox/CRM receives it, so it is not counted as a real lead.

## 4. Not done / boundary
No GTM change, no site change, no spend. Pasting the GTM changes and any live-site step stay with Minda/developer. No extra budget until impressions > 0.
