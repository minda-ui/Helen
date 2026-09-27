# Draft — Branded email signatures for the team

**Company:** Group-wide (all seven entities + the AI Workforce roster) — not a single-company piece.
**Channel:** Internal deliverable (email client signature blocks), not published content.
**Brief:** AI Workforce Hub Tasks & Requests `AWT-0038` ("CREATE BRANDED EMAIL SIGNATURES FOR THE TEAM",
owner request, Minda 2026-09-20, via Victoria). Source-and-brief doc: `Outputs/Brand/2026-09-20_Signature-Source-and-Brief-for-Helen.md`
(Drive `1_WokhYqNDO7GNG0h03ZfwoIsrqn3lUo4`).
**Status:** Ready for review. **Draft-only (charter §2b) — nothing applied to any mailbox.** Victoria +
Minda review and release.

**Sources (cite, never copy):**
- Signature brief above — real signatures in use (Construction, Properties), roster, owner decisions.
- `Wiki/Topic-Brand-Assets.md` (group KB) — palette (`#74cc00` brand green), typography, logo file
  and licence.
- `Brand-and-Voice/Fishbone-Construction-Ltd.md` (this KB) — `enquiries@fishboneconstruction.co.uk`.
- Group `Wiki/Org-Fishbone-Waste-Ltd.md` — confirms Waste's own domain `fishbonewaste.co.uk`
  (`info@` mailbox on that domain).
- `Brand-and-Voice/Amfa-Furniture-Ltd.md` — `enquiries@amfa.uk`.
- Group `Wiki/Org-Fishbone-Holdings-Ltd.md`, `Org-Fishbone-Commercial-Properties-Ltd.md`,
  `Org-Fishbone-SSAS.md` — read for a contact email; **none found** for any of the three (see §3).

---

## 0. Decisions made while drafting (flagged for Victoria/Minda to confirm)

The brief left a few things for judgement rather than spelling them out. Flagging each rather than
guessing silently:

1. **Field-label style.** The brief noted two styles mixed in the wild (`Phone:` vs `e:`/`p:`) and
   asked to pick one. Chose **`e:` / `p:`** — it's compact, already used correctly in Irina's own
   Properties block, and reads as the more current convention of the two.
2. **"Kind regards," sign-off.** Construction's real block includes it; Properties' doesn't. Treating
   it as **part of the email body, not the reusable signature snippet** — the signature starts at the
   logo/name. (Easy to add back if you'd rather it be baked into the template.)
3. **Victoria's title contains "AI".** The roster lists her as *"CEO's Assistant / AI Workforce
   Coordinator"* — the second half contains the word the owner decision says to drop ("no 'AI' /
   'AI assistant' descriptor"). Used **"CEO's Assistant"** alone in her signature to follow the rule
   literally, since it's her own title that has the conflict. **Flagging for Victoria to confirm** —
   happy to use the full compound title instead if that's not what was meant.
4. **"Company they act for" for group-level AI seats.** The brief says AI signatures should carry
   "Fishbone Group + the company they act for." Six of the eight AI roles (Victoria, Rachel, Peter,
   Alex, Eugene, Helen) are group-wide by their own job titles — no single subsidiary to name, so those
   use **"Fishbone Group"** alone. Two look company-specific from their titles/KB alone: **John**
   ("Properties Operations Assistant" → Fishbone Properties Ltd) and **Darius** ("Workshop Operations
   Assistant" — his KB is titled "Workshop of Furniture Making," which points to Amfa). Both are
   **inferred from role title/KB naming, not independently confirmed** — flagged in §2, not stated as
   settled fact.
5. **No AI seat has a personal mailbox.** Per the brief, "don't invent contact details." None of the
   eight AI members has a confirmed individual email address in any KB read for this. Used
   `[shared address — TBC]` as an explicit placeholder in each AI signature rather than guess one — see
   §2.
6. **Three of the seven companies have no findable contact email** anywhere in their own KBs
   (Commercial Properties, Holdings, SSAS) — flagged, not invented. See §3.

---

## 1. House signature template

One system, grounded in the two real signatures on file (§1 of the brief) and the group brand
(`Topic-Brand-Assets.md`: brand green `#74cc00`, logo `Outputs/Brand/Little logo.jpg`). Structure:
**Name (bold) / Role or Title / Company / e: / p: (only if the person has one)**, a thin brand-green
rule under the name, small logo to the left.

### Plain-text

```
[Full Name]
[Role/Title]
[Company Name]
e: [address]
p: [phone]        <- omit this line entirely if the person has none (never invent one)
```

### HTML

Table-based markup (safest across email clients — no external CSS, no flexbox/grid). Logo `src` is a
placeholder pointing at the Drive file; swap for a hosted URL when this goes live (Drive links aren't
reliably embeddable in outgoing mail).

```html
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#16201a;">
  <tr>
    <td style="padding-right:14px;vertical-align:top;">
      <img src="[LOGO_HOSTED_URL]" alt="Fishbone Group" width="48" height="48" style="display:block;">
    </td>
    <td style="border-left:3px solid #74cc00;padding-left:14px;vertical-align:top;">
      <div style="font-weight:bold;font-size:14px;color:#16201a;">[Full Name]</div>
      <div style="color:#5aa300;">[Role/Title]</div>
      <div>[Company Name]</div>
      <div>e: <a href="mailto:[address]" style="color:#16201a;text-decoration:none;">[address]</a></div>
      <div>p: [phone]</div> <!-- omit this <div> entirely if the person has none -->
    </td>
  </tr>
</table>
```

Notes: brand green (`#74cc00`) used only as the thin accent rule, per the house-style rule that colour
stays restrained in a signature (§0 point 2 of `Topic-Brand-Assets.md`'s own tone guidance: "a signature
is not a billboard," per the brief). Typography follows the group's Manrope/Source Serif system in
spirit, but email clients strip web fonts reliably, so the HTML falls back to `Arial/Helvetica` — safer
than a font that silently fails.

---

## 2. Individual signatures

Humans use their real, on-file details. AI members use the plain-role convention (owner decision,
Minda 2026-09-20): `Name / Role (plain, no "AI") / Fishbone Group (+ company if applicable) / shared
address (TBC, not invented) / no personal phone`.

### Humans

**Minda**
```
Mindaugas Gaudiesius
Managing Director
Fishbone Construction Ltd
e: minda@fishboneconstruction.co.uk
p: +44 7855 463292
```
*(Brief notes Minda is also MD across the group companies generally — kept the Construction line since
that's her real, on-file signature; a group-level variant is easy to add if wanted.)*

**Irina**
```
Irina Fedonina
Property Manager
Fishbone Properties Ltd
e: info@fishboneproperties.co.uk
p: +44 7974 362998
```
*(This is Irina's own correct block — the fix for the finding in §3 of the source brief: some of her
Properties emails currently go out carrying Minda's Managing Director block instead of this one.)*

### AI team members (no personal phone; no "AI" descriptor)

```
Victoria
CEO's Assistant                          [see §0.3 — title flagged]
Fishbone Group
e: [shared address — TBC]

Rachel
Finance Assistant
Fishbone Group
e: [shared address — TBC]

John
Properties Operations Assistant
Fishbone Group — Fishbone Properties Ltd   [company inferred from role title, see §0.4]
e: [shared address — TBC]

Peter
Data Assistant
Fishbone Group
e: [shared address — TBC]

Alex
Housekeeping & Operations Steward
Fishbone Group
e: [shared address — TBC]

Eugene
IT & Engineering Assistant
Fishbone Group
e: [shared address — TBC]

Helen
Content & Marketing Assistant
Fishbone Group
e: [shared address — TBC]

Darius
Workshop Operations Assistant
Fishbone Group — Amfa Furniture Ltd        [company inferred from KB naming, see §0.4]
e: [shared address — TBC]
```

**HTML worked examples** (Minda and Helen, to show the template filled in — the other eight follow the
identical structure once the address gaps below are resolved):

```html
<!-- Minda -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#16201a;">
  <tr>
    <td style="padding-right:14px;vertical-align:top;">
      <img src="[LOGO_HOSTED_URL]" alt="Fishbone Group" width="48" height="48" style="display:block;">
    </td>
    <td style="border-left:3px solid #74cc00;padding-left:14px;vertical-align:top;">
      <div style="font-weight:bold;font-size:14px;">Mindaugas Gaudiesius</div>
      <div style="color:#5aa300;">Managing Director</div>
      <div>Fishbone Construction Ltd</div>
      <div>e: <a href="mailto:minda@fishboneconstruction.co.uk" style="color:#16201a;text-decoration:none;">minda@fishboneconstruction.co.uk</a></div>
      <div>p: +44 7855 463292</div>
    </td>
  </tr>
</table>

<!-- Helen -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#16201a;">
  <tr>
    <td style="padding-right:14px;vertical-align:top;">
      <img src="[LOGO_HOSTED_URL]" alt="Fishbone Group" width="48" height="48" style="display:block;">
    </td>
    <td style="border-left:3px solid #74cc00;padding-left:14px;vertical-align:top;">
      <div style="font-weight:bold;font-size:14px;">Helen</div>
      <div style="color:#5aa300;">Content & Marketing Assistant</div>
      <div>Fishbone Group</div>
      <div>e: [shared address — TBC]</div>
    </td>
  </tr>
</table>
```

---

## 3. Per-company variants (all seven entities)

Company-level signature block (for a generic company mailbox, not a named person), with the correct
legal name and a real contact address where one exists:

| Company | Contact address | Status |
|---|---|---|
| Fishbone Construction Ltd | `enquiries@fishboneconstruction.co.uk` | Confirmed (Brand-and-Voice, HSRC-08) |
| Fishbone Properties Ltd | `info@fishboneproperties.co.uk` | Confirmed (Irina's real signature) |
| Amfa Furniture Ltd | `enquiries@amfa.uk` | Confirmed (Brand-and-Voice, uploaded site copy) |
| Fishbone Waste Ltd | `info@fishbonewaste.co.uk` | Confirmed — company owns this domain (`Org-Fishbone-Waste-Ltd.md`: "Own email domain fishbonewaste.co.uk; Drive folders owned by lana@ and info@ at that domain") |
| Fishbone Commercial Properties Ltd | **None found** | Its own KB and the group Org article were checked — no company mailbox on file, only professional advisers' addresses (RMT, Studio Structure, etc.). Flagging rather than inventing one. |
| Fishbone Holdings Ltd | **None found** | Pure holding company, no trade, no email domain or mailbox found in its KB or the group Org article. May genuinely not need one — flagging for Minda to confirm rather than assume. |
| Fishbone SSAS | **Not applicable** | A pension trust, not a company — per this charter (§4) it's "not a marketing subject." Its own administrator (Empowered Pensions, `admin@empoweredpensions.co.uk`) handles its correspondence; no Fishbone-branded signature needed here unless Minda says otherwise. |

Each confirmed company variant uses the house template from §1 with `[Company Name]` and `e:` filled in,
and no personal name line (for a shared/generic mailbox) — e.g.:

```
Fishbone Construction Ltd
e: enquiries@fishboneconstruction.co.uk
```

---

## 4. Summary for Victoria + Minda

- House template (plain-text + HTML) done, grounded in the two real signatures and the group palette.
- All 10 people on the roster have a signature drafted; **8 AI members are missing a real contact
  address** — genuinely not found anywhere in the KBs, not invented. Need those (or confirmation that
  a specific shared mailbox should be used) before these can be finalised.
- **3 of 7 companies have no findable contact email** (Commercial Properties, Holdings; SSAS is N/A).
  Same — need a real address or confirmation none exists yet.
- **4 judgement calls flagged in §0** (field-label style, "Kind regards," Victoria's title, John/Darius's
  company attribution) — happy to revise any of these on steer.
- Nothing has been applied to any mailbox. This is a draft set for review only.
