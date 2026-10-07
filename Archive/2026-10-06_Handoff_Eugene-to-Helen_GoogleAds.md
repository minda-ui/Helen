# Hand-off: Google Ads operating note + Change Request template (Eugene → Helen)

From: Eugene (AI IT & Engineering Assistant) · 2026-10-06 · §7a Raw/ hand-off, add-only.
Minda, 2026-10-06: "Drop both into Helen's Raw/."

Context: Helen was hitting Claude's **"Real-World Transactions"** safety guardrail when trying to mutate a
live Google Ads account. That is a model safety behaviour, not a permissions/config issue — it is not to be
worked around. The fix is the estate-standard pattern: **Helen prepares** (research / analyse / recommend /
draft), **a human (Minda, the account owner) commits the live spend.**

Two files to fold into your charter/operating docs next session:
- `Helen-GoogleAds-Operating-Note.md` — your Google Ads lane, match-type guidance, and guardrails.
- `Helen-GoogleAds-Change-Request-Template.md` — the sheet you fill for every proposed live change; Minda
  reviews section 6 and applies it.

Notes: budget/spend authority is Minda's; you hold no credentials and never type billing details. If you hit
the "Real-World Transactions" pause, convert the action into a Change Request rather than working around it.

Source of truth is Eugene's git (`Runbooks/Helen-GoogleAds-Operating-Note.md` and
`Runbooks/Helen-GoogleAds-Change-Request-Template.md`). This is an add-only Raw/ hand-off; fold it in via
your own process.
