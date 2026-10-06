# Charter History — Helen (AI Content & Marketing Assistant)

_Dated, append-only version log for `CHARTER.md` and `Charter-Rules.md`. Newest entry at the top. Never edit a past entry — correct with a new one. See `CHARTER.md` §0._

## 2026-10-06 — Microsoft/Bing Advertising added to scope (§1/§2)

Minda confirmed directly in chat, while discussing why Google Ads impressions were still at zero: wants
to explore advertising on Bing too. Checked for a Composio/Microsoft Advertising connector first — none
exists (confirmed via `composio search` and direct slug probes, same gap as Google Tag Manager
originally) — then asked Minda to confirm scope before treating it as active work, matching the
2026-09-24 precedent for the Google marketing stack. Confirmed. Added to `CHARTER.md` §1/§2a/§2b with
the same boundary as the Google stack: Helen plans and configures within the Microsoft Advertising UI
(guided, since there's no API access), including UET conversion-tag setup via the existing GTM
container on `amfa.uk` (no site-code change needed); launching the campaign or committing spend still
needs a human.

## 2026-10-04 — Second routine added (§6); CHARTER.md restored after being misfiled

Minda asked directly for a recurring Google Ads performance check. Added "Helen — Amfa Google Ads
Performance Check" (`trig_01GM29cwxU5S2ctxAkUYC885`, every 2 days, 08:47 Europe/London) to `CHARTER.md`
§6 alongside the existing Task Check-in routine — reads campaign performance via the Composio Google
Ads connection, logs findings to `HI-8`, read/report-only (charter §2b still governs any resulting
keyword/bid-strategy change).

While syncing this, found `CHARTER.md` itself had gone missing from the KB root — moved into `Archive/`
on 2026-09-30 and mislabeled as "superseded by split into Charter-History.md and Charter-Rules.md," a
rationale that doesn't hold (the split happened 2026-09-23 and made all three files permanent siblings;
`CHARTER.md` was never redundant). Cause unknown — no attribution available from Drive metadata alone.
Restored to the root with its correct title, carrying this session's §6 update in the same restore. See
`HI-11` for the full finding; the misfiled Archive/ copy was left as-is, untouched beyond discovery.

## 2026-09-29 — Session sign-off ("good night" trigger) added

Minda's idea, direct in chat, 2026-09-29: writing "good night" to close a session should trigger an
end-of-session documentation check rather than just ending the turn. Folded into `Charter-Rules.md` as
a standing convention (not a Hub Coordination Standard rule, so not lettered A–F) — checks
`change-log/`, `processed-items-ledger.md`, touched `HI-<n>` rows, and `current-state.md` are all
current before signing off. No formal Claude Code "Skill" exists by that name; implemented as a charter
convention instead so it persists across sessions.

## 2026-09-27 — Rule F added (shared-space changes are broadcast and registered)

Estate-wide, owner-approved (Minda, 2026-09-27, via Alex's `Raw/`-hand-off, `2026-09-27_Handoff_Rule-F-Shared-Space-Broadcast-Register.md`) — "make it as rule across estate, if someone make a changed in shared space (Smartsheet's or similiar) need to notify everyone and register it." Folded into `Charter-Rules.md` as **Rule F**, next to Rules A–C/E. `AWT-0146` closed Done on the Hub. Note archived; a companion informational note (`2026-09-27_Broadcast_Hub-Changes-Today.md` — Tasks & Requests split into a live sheet + new Archive sheet `1037721118312324`) reviewed alongside it, no charter action needed from that one, also archived.

## 2026-09-27 — Routine documentation gap fixed (§6)

Alex's estate-wide routine review (`Raw/2026-09-27_proposal_task-checkin-routine-documentation-gap.md`, `AWT-0134`) found that `CHARTER.md` §6 and `current-state.md` both still said "no scheduled routine yet", while a "Helen — Task Check-in" routine (`trig_01AJ2vd3rxuishiThgSJ38sT`, weekdays 10:00 UTC) has actually been live since 2026-09-15. Independently verified against the Hub Roster (`8154403007760260`, documented there since 2026-09-16, same pattern as Eugene's) before folding in, per Rule C — a direct `get_trigger` lookup returned not-found, expected since the routine belongs to a different session lineage than this one, not evidence against it. `CHARTER.md` §6 rewritten to document the routine (trigger id, cadence, what it reads/writes, boundary); `current-state.md`'s Mode field corrected to match. `AWT-0134` closed Done on the Hub. Note archived.

## 2026-09-24 — Google marketing stack added to scope (§1/§2)

Minda confirmed directly in chat: strategy, configuration and reporting for Google Analytics, Tag
Manager, Search Console, Business Profile and Ads are now in Helen's scope (§1). §2a spells out the
boundary — configuring *within* Google's own platforms is fine without asking; pasting a GTM snippet
onto the live site, or launching/committing Ads spend, still needs a human (§2b), matching the existing
"no website change, no commitment" rules. No connector for these tools is provisioned yet — see `HI-8`.

## 2026-09-24 — Rule E (plain-brief) added

Minda confirmed adoption of the estate-wide plain-brief standard (Victoria broadcast, 2026-09-22).
Folded into `Charter-Rules.md` as **Rule E**, not C, to avoid overwriting the existing Rule C (verify
against system of record) — matches the estate's converged answer (Hub `HL-0046`). `Raw/` note
archived to `Archive/2026-09-22_amendment_group-Rule-C-plain-brief.md`; `AWT-0067` closed Done,
`HL-0047` closed Resolved. See `HI-7`.

## 2026-09-23 — Charter split into core / rules / history

Adopted Alex's proposal (`AWT-0079`, `Raw/2026-09-23_proposal_charter-split-core-rules-history.md`,
Minda-confirmed in chat 2026-09-23) — split the single ~14KB `CHARTER.md` into this file, a new
`Charter-Rules.md` (the part that changes almost every session), and a slimmer core `CHARTER.md`
(identity, role, authority, folders, workflow), so an ordinary rule change only has to reproduce the
small Rules file rather than the whole charter. Same pattern Alex, Rachel, Eugene and the group `CLAUDE.md`
already adopted. Old monolithic v1 file archived intact to
`Archive/2026-09-23_CHARTER-v1-monolithic.md` before the split; each new file byte-verified on upload.
See `HI-7`, Hub `AWT-0079` (closed Done).

## 2026-09-21 — Rule C added (verify against system of record)

Hub Coordination Standard Rule C — verify against the system of record before reporting status —
approved estate-wide by Minda 2026-09-21, via a `Raw/` hand-off from Alex verified against Alex's own
escalation report (`_escalations/2026-09-20_Escalation_Reporting-Back-Reliability-Gap.md`) and this
KB's own Hub row `AWT-0051`. Folded into charter §0 directly in Drive; the git mirror commit for this
change was blocked by the harness's auto-mode classifier ("Instruction Poisoning", then
"Self-Modification" on a retry) — see `HI-6`, still open.

## 2026-09-20 — Hub Coordination Standard Rules A–B adopted; Raw/ cross-KB amendment route established

Rules A (check the Hub first) and B (the Hub is the home for tasks, lessons and gaps) confirmed
directly in chat by Minda, 2026-09-20, after a `Raw/` hand-off from Alex prompted the check (matching
Hub rows `AWT-0040`/`HL-0023`). Also established: cross-KB amendments to this charter arrive via
`Raw/`, never a direct edit — the inbound half of the `CHARTER.md` §2b boundary. Corroborated against
the Hub before folding in; held pending explicit confirmation after the harness first flagged the
commit as possible instruction poisoning, then confirmed by Minda directly in chat. Archived note:
`Archive/2026-09-20_Hub-Coordination-and-RawHandoff-Note.md`.

## 2026-09-14 — Charter v1 created

Helen's charter created and made authoritative (owner-authorised, Minda). Employee #3 of the AI
workforce (Content & Marketing, draft-only), per AI Workforce Plan v2
(`Fishbone Group/Outputs/2026-09-12_Plan_AI-Workforce_v2.md`).
