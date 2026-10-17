---
name: ads-ui-apply-guide
description: Walk Minda through applying an approved Google Ads Change Request in the Ads UI, one screen at a time from her screenshots — right screen, paste from the CR, clear Google's AI prefills and sitelinks, fix the default final URL, check text line by line, then verify what actually saved with a read-only query and record any differences in the CR. Use after Minda approves a CR-GA-<n> and starts applying it.
---

# ads-ui-apply-guide

Rule G: **Minda applies, Helen guides and verifies.** Never click, type or save for her; never run a `MUTATE` call. Pair with `change-request-draft` (the CR) and `google-ads-readonly-check` (verification).

## Before she starts
Give her the exact route and the text to paste (plain code blocks, one item per line). Name the screens she should **not** open.

| Change | Route in the Ads UI |
|---|---|
| New ad group in an existing campaign | **Campaigns → click the campaign name → Ad groups → blue + → New ad group** |
| Negative keywords | campaign → **Keywords → Negative keywords → + → choose Campaign level**, match as the CR says |
| Radius location | campaign → **Locations → Edit locations → Advanced search → Radius targeting** (postcode, radius, **mi** not km) |
| Add keywords to an ad group | **Ad groups → click the ad group → Keywords → + → Keywords** |

**Wrong screens seen:** Overview → **New campaign** (starts a new campaign and leaves a "Resume campaign draft"). A new-campaign URL has `campaigns/new`; an ad-group URL has `adgroups/new` and `campaignId=24298119348`. If she is on the wrong one, say Cancel and give the route.

## Check each screenshot against the CR
Read the URL, then the fields. Say what is right, what is wrong, and what to do next. Ask for the top and bottom of long lists; count the characters shown (e.g. 26/30) against the CR.

## Known traps (ad group + ad)
1. **Ad type:** leave **Standard**. Rename "Ad group 2" to the CR name.
2. **Keywords:** paste in quotes for phrase match. Leave "Search term matching" on *Using only your keywords and match types*. Do **not** click "Update keyword suggestions"; ignore the product chips.
3. **Final URL defaults to the homepage** — set the CR's URL.
4. **Google AI prefills** headlines and descriptions from the site (e.g. "…Future-Proofed - Newcastle Furniture Experts"). Click **Clear prefills**, then paste only the CR's copy. "Excellent" ad strength with prefills is not our copy. Ignore the keyword-idea links for other products.
5. **AI-suggested sitelinks** are attached unless removed — delete them with the bin icons. Leave Messages and Business name alone (campaign level).
6. Never touch the budget or campaign settings. Click **Done**, then **Save/Create** only on the ad-group flow.

## After she saves — verify read-only, never trust the screen
- Ad groups and their `primaryStatus`; the RSA's approval, final URL, every headline and description (script-check lengths against the CR).
- **Keywords per ad group** — the first save once created an ad group with **0 keywords** (found only by this check). If empty, give the route to add them.
- **Negatives:** level and match type — the UI put 3 at ad-group level, broad, when the CR said campaign, phrase.
- Budget, locations, radius, existing negatives unchanged.

## Record
Fill CR section 6 truthfully: "Applied (where/when)", every difference from the CR, and anything Google flagged (e.g. `RARELY_SERVED` / low search volume). Set the status line and review dates. Log with `session-logging`. Next check ~48 h later with `google-ads-readonly-check`.
