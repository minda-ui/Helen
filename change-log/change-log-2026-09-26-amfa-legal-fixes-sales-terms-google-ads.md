# Change log — 2026-09-26 — Amfa legal-page fix, Sales T&Cs drafted, Google Ads campaign plan

_Append-only dated session file. Newest notes at the top. See `current-state.md` and `CHARTER.md`._

## Session — 2026-09-26: three pieces of work, in order

### 1. Fixed the live `amfa.uk` legal-page placeholder text (ledger row 20)

Row 16 (2026-09-24) had flagged 5 internal `[TO CONFIRM before publishing]` drafting notes live and
public on the Privacy Policy and Terms of Use. Re-verified via `curl` (WebFetch's own proxy blocks this
domain) before touching anything — all 5 still present, unchanged.

Resolved 2 of the 5 without needing new input: the analytics-note placeholder (Privacy Policy §3) was
just an internal drafting aside, not a missing fact, so it was simply removed; the delivery-subcontractor
placeholder (§5) was resolved from the already-confirmed fact that Amfa's delivery/installation is
in-house (`Brand-and-Voice/Amfa-Furniture-Ltd.md`), so there's no third-party subcontractor to name.

The remaining 3 needed either a fact or a business decision only Minda could supply — asked directly
rather than inventing:
- **Retention period** (Privacy Policy §6): 24 months for unconverted enquiries.
- **International transfers** (Privacy Policy §10): a generic safeguards clause, rather than waiting on
  a definitive answer from Tilda (researched: Tilda's data controller is Dubai-based with an EU rep in
  Portugal — suggestive of transfers, not conclusive).
- **Separate Sales Terms document** (Terms of Use §4): yes, wanted next — opened `HI-9`.

Filed corrected full-page text (`Drafts/2026-09-26_Amfa_Privacy-Policy_v2.txt`,
`_Terms-of-Use_v2.txt`) plus a developer-ready fix brief with exact find/replace instructions
(`Drafts/2026-09-26_Amfa_Legal-Pages_Placeholder-Fixes_v1.md`). **Helen has no CMS/website access
(charter §2b)** — draft-only; a human/developer still has to apply it, and neither this fix nor the
original pages has ever had a solicitor review.

### 2. Drafted the Amfa Sales Terms & Conditions of Sale (ledger row 21, `HI-9`)

Follow-up from item 1's §4 decision. 16-section document: how a contract forms, price/payment, order
changes, manufacturing lead time, delivery/installation and site-access responsibilities, risk/ownership
transfer, snagging, cancellation rights, warranty, liability, force majeure, governing law.

Asked Minda directly for the 3 genuine business/legal-policy decisions rather than inventing them:
50% deposit (bank transfer or card), balance due before delivery, and reliance on the statutory
bespoke-goods cancellation exemption (Consumer Contracts Regulations 2013, reg 28(1)(b)) over a
voluntary cooling-off period. Two commercial defaults (30-day quote validity, 14-day snagging window)
flagged as reasonable proposals, not confirmed facts.

Filed `Drafts/2026-09-26_Amfa_Sales-Terms-and-Conditions_v1.txt` + brief `_Sales-Terms_Brief.md`.
Ready for review — like the other two Amfa legal pages, still needs a solicitor's sign-off before
publishing; none of the three has ever had one.

**Paused, not completed further** — Minda moved to Google Ads (item 3) before this went past drafting.
`HI-9` stays open.

### 3. Drafted an Amfa Google Ads campaign plan (ledger row 22, `HI-8`)

Minda's direct ask, no live Hub task. Checked first, per Rule A/C discipline: `Get Sheet Summary` on
the Hub Tasks & Requests sheet filtered to Assigned to = Helen — nothing Ads-related; `ListConnectors`
— confirmed (again) no Google Ads/Analytics/Tag Manager/Search Console connector exists anywhere in the
org's directory, not even listed as "not connected"; a broad Drive search for any prior Google Ads
brief or budget decision — none found. (That search also surfaced files from Peter's own KB/Archive —
unrelated, a different AI employee's sister KB, not touched beyond reading metadata.)

Clarified scope with Minda first (company, objective, deliverable) rather than guessing: **Amfa**,
**lead generation** (quote requests via the site's "Get a free quote" form), **full campaign plan**
(structure, keywords, ad copy, budget guidance).

Delivered `Drafts/2026-09-26_Amfa_Google-Ads_Campaign-Plan_v1.md`:
- Geography: 50-mile Newcastle radius, matching the confirmed free-measuring-visit area.
- 8-ad-group structure by the real service lines — 4 marked launch priority (Bespoke Kitchens, Fitted
  Kitchens, Wardrobes, Bathroom Vanity), Commercial Furniture flagged for its own future campaign
  given the different B2B buyer.
- Keyword themes and negatives — explicitly flagged as informed themes grounded in real service
  categories, not verified search-volume/CPC data (no Keyword Planner access).
- Full Responsive Search Ad copy (15 headlines + 4 descriptions each) for both Kitchens ad groups,
  every claim traced to confirmed warranty/pricing/manufacturing/process facts — no invented
  statistics or unbacked superlatives.
- Ad extensions, landing-page recommendations, illustrative budget guidance (£600–£1,500/month
  starting range, explicitly caveated as unvalidated).

Flagged two things Minda should weigh before spending anything: the live site's still-unapplied
legal-placeholder fix (item 1) and copy-fixes doc (row 16/17, 7 items) mean paid traffic would land on
a site with visible issues right now; and conversion tracking needs GTM/GA4 (`HI-8`, same missing
connector) before any campaign could be measured properly.

**No account access exists to build any of this from** — planning-only, per `HI-8` and charter §2b
(launching/spending needs a human regardless of access).

## Control files

`open-issues.md` (HI-8, HI-9), `processed-items-ledger.md` (rows 20–22), and `current-state.md`
(clean rewrite per charter §7) updated after each of the three items above, in Drive (create-new +
verify + trash-old, re-verifying `parentId` before each `trash_file` per the `HI-5` lesson) and git.

Git: `minda-ui/Helen@18e336f` (item 1), `@0871ff1` (item 2), `@cf342c1` (item 3).
