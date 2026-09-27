# Draft — Legal-pages placeholder fixes, ready to apply (Amfa live site)

**Company:** Amfa Furniture Ltd
**Channel:** Website (live at `amfa.uk` — `/privacy-policy`, `/terms-of-use`)
**Brief:** Minda flagged 2026-09-24 that 5 internal `[TO CONFIRM before publishing: ...]` drafting notes from `Drafts/2026-09-21_Amfa_Privacy-Policy_v1.txt` / `Terms-of-Use_v1.txt` are live and public on the site. Re-verified live 2026-09-26 (via `curl` — WebFetch's own proxy blocks this domain) — all 5 still present, unchanged.
**Status:** Ready for the developer to apply. **Draft-only (charter §2b) — Helen has no CMS/website access; nothing applied to the live site.**

---

## What changed and why

Four of the five placeholders needed either a real fact or a business decision that only Minda could supply. She resolved all three open points directly (2026-09-26); the fifth was already just an internal drafting note, not a missing fact.

| # | Page | Section | Resolution |
|---|---|---|---|
| 1 | Privacy Policy | §3 Cookies and Analytics | Editorial note only, no fact needed — removed. |
| 2 | Privacy Policy | §5 Sharing Your Data | Delivery/installation confirmed **in-house** (`Brand-and-Voice/Amfa-Furniture-Ltd.md`) — no third-party subcontractor sees customer data, so the placeholder is replaced with that fact. |
| 3 | Privacy Policy | §6 How Long We Keep Your Data | Minda: unconverted enquiries kept **24 months**. |
| 4 | Privacy Policy | §10 International Transfers | Minda opted for a safe generic safeguards clause rather than waiting on a definitive answer from Tilda. (Researched: Tilda's data controller is Dubai-based with an EU representative in Portugal — suggestive of transfers, not conclusive; contact `gdpr@tilda.cc` if a more precise statement is ever needed.) |
| 5 | Terms of Use | §4 Enquiries and Quotes | Minda wants a separate Terms & Conditions of Sale document drafted next (follow-up task, not blocking this fix) — phrased generically so this section doesn't reference a document that doesn't exist yet. |

**Simplest way to apply:** replace the full body text of each page with the corresponding file below (headings/section numbers unchanged, so it's a straight swap, not a restructure).

- `Drafts/2026-09-26_Amfa_Privacy-Policy_v2.txt` → replaces `/privacy-policy`
- `Drafts/2026-09-26_Amfa_Terms-of-Use_v2.txt` → replaces `/terms-of-use`

## Exact find/replace, if applying section-by-section instead

**Privacy Policy §3** — find the bracketed sentence and delete it:
> [TO CONFIRM before publishing: whether this remains accurate if analytics/marketing tools are added later — this policy should be updated to match at that point.]

**Privacy Policy §5** — find:
> We do not sell your personal data. We may share it with:
> - trusted contractors and delivery/installation partners, where needed to fulfil your order;
> - our professional advisers (for example, accountants or IT providers), where necessary for running our business;
> - law enforcement or regulators, where we are required to by law.
>
> [TO CONFIRM before publishing: the specific delivery/installation partners or subcontractors, if any, who would see customer contact details, so they can be named or described accurately here.]

Replace with:
> We do not sell your personal data. Delivery and installation are carried out in-house by Amfa's own team, not third-party subcontractors. We may share your data with:
> - our professional advisers (for example, accountants or IT and website service providers), where necessary for running our business;
> - law enforcement or regulators, where we are required to by law.

**Privacy Policy §6** — find:
> We keep your personal data for as long as necessary to respond to your enquiry, fulfil any order, and meet our legal and accounting obligations. [TO CONFIRM before publishing: a specific retention period — e.g. how long unconverted quote enquiries are kept before being deleted.]

Replace with:
> We keep your personal data for as long as necessary to respond to your enquiry, fulfil any order, and meet our legal and accounting obligations. Where an enquiry or quote request does not lead to an order, we keep that data for up to 24 months before deleting it, unless you ask us to delete it sooner or we are required to keep it longer to meet a legal obligation.

**Privacy Policy §10** — find:
> [TO CONFIRM before publishing: whether Tilda (our website platform) or any other supplier processes data outside the UK/EEA, so this section can state that accurately rather than being left blank.]

Replace with:
> Some of the suppliers we use to run this website and our business (for example, our website hosting platform) may store or process personal data outside the UK. Where this happens, we ensure appropriate safeguards are in place, such as contractual protections recognised under UK data protection law, so your data continues to receive an equivalent standard of protection.

**Terms of Use §4** — find:
> A contract for the design, manufacture, supply, and/or installation of furniture is only formed once we have separately confirmed a quote and order with you in writing.
>
> [TO CONFIRM before publishing: whether Amfa wants a separate, more detailed "Terms and Conditions of Sale" document covering the actual point of order — deposit/payment terms, delivery timescales, cancellation rights under the Consumer Contracts Regulations, and warranty claims — since these Terms of Use only cover using the website itself, not the sale contract that follows a confirmed order.]

Replace with:
> A contract for the design, manufacture, supply, and/or installation of furniture is only formed once we have separately confirmed a quote and order with you in writing, including the terms of that order such as pricing, deposit, delivery timescale, cancellation rights, and warranty.

## Still outstanding (not blocking this fix)

- **No solicitor has reviewed either page.** The original brief (`2026-09-21_Amfa_Legal-Pages_Brief.md`) flagged this as needed before publishing; the site went live without it. Minda's own judgement on the three flagged points above is a reasonable interim call, but a solicitor pass is still recommended given real regulatory exposure (UK GDPR).
- **Sales Terms & Conditions of Sale** — Minda wants this drafted as a follow-up (deposits, delivery timescales, cancellation rights, warranty claims for a confirmed order). Not started yet — see `open-issues.md` `HI-9`.

## Sources

- `Drafts/2026-09-21_Amfa_Legal-Pages_Brief.md`, `_Privacy-Policy_v1.txt`, `_Terms-of-Use_v1.txt` — original drafts and the four flagged gaps.
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` — confirmed in-house delivery/installation (resolves §5).
- Minda, 2026-09-26 (this session) — retention period (24 months), international-transfers approach, and Sales T&Cs follow-up decision.
- Web search, 2026-09-26 — Tilda's data controller (Dubai HQ, EU representative in Portugal); not conclusive enough to state definitively, hence the generic safeguards clause.
- `amfa.uk` (`/privacy-policy`, `/terms-of-use`) — live page source, re-checked directly 2026-09-26 confirming all 5 placeholders still present, unchanged since the 2026-09-24 review.
