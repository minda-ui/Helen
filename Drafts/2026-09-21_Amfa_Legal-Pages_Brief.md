# Draft brief — Amfa Furniture Ltd: Privacy Policy + Terms of Use

**Company:** Amfa Furniture Ltd (11259604)
**Channel:** Website legal pages (footer links "Privacy policy" / "Terms of use" already exist on the
live preview at `amfa.tilda.ws` — currently unlinked/empty button placeholders, no content behind them).
**Brief:** Minda, 2026-09-21 — "we need to create Privacy policy and Terms of use. prepare them for
export in .txt".
**Status:** Ready for review — **not legal advice, needs a solicitor's sign-off before publishing.**
**Files:**
- `Drafts/2026-09-21_Amfa_Privacy-Policy_v1.txt`
- `Drafts/2026-09-21_Amfa_Terms-of-Use_v1.txt`

---

## Important caveat — read before using these

Helen is a marketing/content drafter, not a solicitor. UK data protection law (UK GDPR, the Data
Protection Act 2018, PECR) and consumer law (Consumer Rights Act 2015, Consumer Contracts Regulations
2013) carry real compliance obligations and, for data protection, real regulatory penalties if a
policy misstates what a business actually does. These drafts are a **structurally sound, factually
grounded starting point** — real company details, real confirmed facts about the site's actual
analytics setup — but they are **not a substitute for legal review**, and several specific points are
explicitly flagged in the text itself as `[TO CONFIRM before publishing]` rather than guessed. Please
have a solicitor (or at minimum Minda's own judgement on the flagged items) review both before they go
live.

## What's genuinely confirmed vs. flagged as unknown

**Confirmed, used as fact (cite, never invent — per this KB's charter):**
- Legal name, company number (11259604), registered office (6 Beverley Place, Wallsend NE28 7BH) —
  group KB `Org-Amfa-Furniture-Ltd.md`.
- Trading/showroom address, phone, email — already confirmed in `Brand-and-Voice/Amfa-Furniture-Ltd.md`
  and cross-checked live on the site itself.
- The site is built on Tilda and runs Tilda's own built-in analytics **with cookies explicitly
  disabled** (`window.tildastatcookie='no'` in the live page source) — checked directly in the site's
  HTML, not assumed. No Google Analytics, Facebook Pixel, or similar third-party tracker found on the
  homepage.
- The site is a quote/enquiry generator (a "Get a free quote" form), **not an e-commerce checkout** —
  no payment collection on-site, confirmed by browsing the live pages.

**Flagged, not invented — four specific gaps, marked inline in the drafts:**
1. **Data retention period** for enquiries that don't convert to an order — no source for this; needs
   a real answer from Minda/Amfa's own practice, not a made-up number.
2. **Delivery/installation subcontractors** who might see a customer's contact details — not confirmed
   whether any exist or who they are.
3. **International data transfers** — whether Tilda or any other supplier processes data outside the
   UK/EEA. Genuinely don't know; flagged rather than asserting either way.
4. **Whether a separate, more detailed Sales Terms/Terms & Conditions of Sale is needed** — these Terms
   of Use only cover using the website and submitting an enquiry; the actual furniture order (deposit,
   delivery timescale, cancellation rights, warranty claims) is a different, more detailed contract
   that typically needs its own document once a quote is accepted. Flagged in the draft rather than
   silently expanded into something this brief wasn't asked to cover.

## Sources

- `Org-Amfa-Furniture-Ltd.md` (group KB) — company number, registered office, rename history.
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` (this KB) — showroom address, phone, email, warranty,
  pricing structure.
- Live site `amfa.tilda.ws` — homepage HTML fetched directly (`curl`, since the WebFetch tool's own
  proxy blocks this domain) and inspected for cookie/analytics scripts and the existing "Privacy
  policy"/"Terms of use" footer buttons.
