# Change log — 2026-09-21 — Amfa Privacy Policy + Terms of Use drafted

Minda: "First task. we need to create Privacy policy and Terms of use. prepare them for export in .txt"

This came up while reviewing Amfa's near-final website preview (`amfa.tilda.ws` — reachable via direct
`curl`, though blocked through the WebFetch tool's own proxy; the footer already has "Privacy policy"
and "Terms of use" buttons with nothing behind them yet).

**Sourced, not invented.** Pulled real, confirmed facts before drafting: legal name, company number
(11259604), and registered office from the group KB's `Org-Amfa-Furniture-Ltd.md`; trading address,
phone, and email already confirmed in this KB's `Brand-and-Voice/Amfa-Furniture-Ltd.md`. Checked the
live site's own HTML directly rather than assuming a standard cookie-consent boilerplate: it runs
Tilda's built-in analytics with cookies explicitly disabled (`window.tildastatcookie='no'`), no Google
Analytics or Facebook Pixel present, and no payment/checkout flow — it's a quote-request site, not
e-commerce. All of that is reflected accurately in the drafts.

**Flagged rather than guessed.** Four things a privacy policy or terms page would normally state that
I have no real source for: the data-retention period for enquiries that don't convert, whether any
delivery/installation subcontractors see customer contact details, whether any supplier (Tilda
included) processes data outside the UK/EEA, and whether a separate, more detailed Sales Terms
document is needed for the point an order is actually confirmed (these Terms of Use only cover the
website itself). Each is marked inline as `[TO CONFIRM before publishing]` rather than filled in with
a plausible-sounding guess.

**Deliverables:**
- `Drafts/2026-09-21_Amfa_Privacy-Policy_v1.txt` — clean, ready-to-export UK GDPR-style policy.
- `Drafts/2026-09-21_Amfa_Terms-of-Use_v1.txt` — clean, ready-to-export website terms.
- `Drafts/2026-09-21_Amfa_Legal-Pages_Brief.md` — the standard brief/sources/status header, carrying
  the one caveat that matters most here: **these are not legal advice.** UK data protection and
  consumer law carry real regulatory consequences for getting them wrong, and Helen is a content
  drafter, not a solicitor. Recommended a solicitor's review before either goes live, on top of
  resolving the four flagged gaps.

**Status:** Ready for review — not published, nothing applied to the live site (charter §2b).
