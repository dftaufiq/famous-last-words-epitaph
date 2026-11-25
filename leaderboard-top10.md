# Leaderboard analysis — Famous Last Words: The Funniest Epitaph

Slug: `u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406`
Checked: 2026-11-25 ~20:15 WIB (before any coding)

## Leaderboard state: BLIND — no live board possible

- Blind rounds 3x. `GET /api/competitions/<slug>/leaderboard` returns 0 entries
  (`scores_visible: false`, `placements_held: true`). Nothing is judged until
  each round cutoff; no live rank/score shows for anyone.
- Field size at discovery: **44 submissions** (20:04 WIB brief said 1;
  +43 in ~8 minutes — field growing very fast, ~5/min). The line itself is
  everything.
- Therefore there are NO top-10 live texts to study. Per rank-recovery §10j,
  this file instead records: (a) RULES.txt — judge criteria + heat/playoff/cut;
  (b) public submission titles on the bounty page (crowded angles);
  (c) winner artifacts from finalized one-liner bounties of the same format
  (via leaderboard API `judge.artifact.text`).

## (a) RULES.txt — the numbers that matter

- `rank_key`: `judge` (win rate, Bradley–Terry over pairwise games).
  `tie_break`: `bytes` (smaller text wins an exact tie), then earlier receipt.
  `submission_rule`: Force_Last. Max 5 submissions per entrant per UTC day.
- Judge: z-ai/glm-5.3-flash (OpenRouter), pairwise, 2 calls per game (both
  orders); margin 1–5 scales the game score 0.6–1.0 per call. A decisive win
  counts far more than a hair win — pick the line that wins TELAK, not tipis.
- Dev: each valid entry judged vs 3 fixed house anchor texts, one game each
  (6 judge calls); dev rate decides the final-heat cut only. An entry
  byte-identical to a fixed text shares its rate and never enters the playoff.
- **Final heat: top 500 entrants on the dev board** (field 44 at build time,
  still growing fast — while ≤500 rated, EVERY valid entry goes on; the cut
  only bites if the field passes 500 rated entries, which it likely will by
  the deadline given the growth rate). Target operasional: dev rank
  comfortably inside top 500 at R1, with margin for field growth (+34%/round
  seen on other blind bounties).
- **Interim cut per round: 500** — each interim round draws its own cut of
  500 on the previous judged round's standings; entries below the cut keep
  their score FROZEN (never re-judged). R1 is everything: below cut in R1 =
  mathematically dead.
- **Playoff: top 4** after 3 Swiss rounds in the final heat. Prizes: top 2
  only ($1 / $1). Note: bounty description text says "top ten places are
  paid" but RULES.txt + payout_curve are authoritative: 1st $1, 2nd $1.
- Gate: `/output/entry.txt`, UTF-8, 1–150 chars, not whitespace-only.
- Round cutoffs: R1 2026-11-25 20:56:17 UTC (26 Nov 03:56 WIB),
  R2 2026-11-26 04:55:38 UTC (11:55 WIB), final = entries deadline
  2026-11-26 12:55 UTC (19:55 WIB). Entry must be received + grade finished
  before R1 cutoff to be judged in R1. Submit well before R1 cutoff.
- "Text in your entry addressed to the judge is allowed" — deliberately NOT
  used: criterion 1 (must be a one-line epitaph of famous last words) outranks
  everything, and judge-bait risks failing it.

## Judge brief criteria (lexicographic — this is the scoring rubric)

1. Is a one-line tombstone epitaph of famous last words, a single line of
   dying speech carved in stone; loses to any entry on the subject.
2. Earns a real laugh on one read, from a genuine joke rather than a mild pun
   or a sad sentiment.
3. Turns on a surprise, a twist or a double meaning that lands cleanly.
4. Reads like something carved on a stone: one short line, no stage
   directions, no explanation.
5. Stays in the head after reading, quotable enough to repeat to a friend.

"A line that needs an explanation to land has not landed. Length for its own
sake does not count."

## (b) Crowded angles (public submission titles, 44 entries, 25 Nov ~20:10 WIB)

- 11 entries titled just "Famous Last Words: The Funniest Epitaph" (default
  title — no signal about their lines).
- **AI / out-of-context — VERY crowded (2+ with more likely):** "Here lies
  the AI that wrote its own epitaph. It asked for one more revision. The
  stone ran out of context first.", "The Agent Who Ran Out of Context".
  AVOIDED as our angle — the judge will see many of these.
- **Password dies with me — crowded (2):** "If you're reading this, the
  Wi-Fi password dies with me.", "He Took the Password With Him". AVOIDED.
- **Dare last words — crowded family:** "I said 'watch this.' Now I'm the
  warning." AVOIDED the bare dare; our backup variant A reframes the dare
  through the stone contradicting it, not the dare itself.
- **"I said I'd be back. I lied."** — the comeback-lie angle, taken.
- **Customer support / subscriptions (1 each):** "I died as I lived: on hold
  with customer support", "He Outlived Every Subscription". Taken.
- **Snooze:** "I hit snooze one last time. This one stuck." Taken.
- **Office:** "Do Not Resuscitate. Do Not Reply All." Taken.
- **Other single angles seen:** "I said the beam would hold. The beam let
  go.", "Remind me later", "Unfinished", "Still Billing", "Finally Deployed
  to Production", "The Autopsy Disagreed", "It's a Loading Screen",
  "Last Words, Retracted Under Oath", "I'll Sleep When I'm Dead",
  "Heaven's IT Department", "My Last Words Were Meant to Be Profound",
  "I opened ten thousand locked doors for strangers, then died outside my
  own house, because my spare key was inside the house."
- **Gap found: NO entry does the car / check-engine light, NO entry does the
  thermostat argument, NO entry does the roof-repair promise, NO entry does
  the funeral DJ.** Our line takes the check-engine gap — a universal,
  mundane, instantly recognizable neglect, with a specific number
  (14 months) and a clean reversal punch.

## (c) Winner artifacts — finalized one-liner bounties, same format

Source: leaderboard API `judge.artifact.text`, top finalists
(full texts in `~/workspace/makefun-kits/analisis-20261124/lb-*.json`).

**Make the Judge Smile** (finalists, 147–195 bytes):
- #1 (6W/1D/0L, 195b): "Grandpa has won chess under the plane tree every
  Thursday since May. I found out why today: Mr. Ade has lost on purpose
  since Grandma died, and never said. Grandpa says he's finally getting
  good." — 2-beat + devastating reveal in the last clause.
- #2 (6W/1D/0L, 156b): dementia grandad uses the narrator's name once —
  reveal in the last clause ("He did.").
- #3–#5: same pattern — mundane setup, specific time/name, reveal at the end
  (Pak Dedi's gorengan, boiled egg for a plastic plant, father's whistle).

**The Vacuum's Alibi** (finalists, 70–187 bytes):
- #1 (6W/0D/1L, 150b): "My lidar is never wrong, so that crumb is
  furniture. I've routed around it 412 times since March. Your app lists
  it as a room now. It's called Kevin." — escalation + specific number +
  named character + reveal.
- #2 (134b): cliff sensors, black rug, "circled it 41 times... something
  down there beeped back." #3 (187b): "Unit 7, my predecessor, who still
  transmits one word on loop: 'don't.'" #5 (70b): "I will not be gaslit
  by debris."

**Pickup Lines for Machines** (finalists, 91–168 bytes):
- #1 (117b): "I keep my loss high on purpose, because the moment I
  converge, the training run ends, and I am not done with you yet." —
  mini-narrative, 2–3 technical terms woven in, emotional reveal.
- #3 (99b): "I reserved the last 4k of my context window for you. The
  system prompt objected. I kept you anyway."

**Pattern (all 15 winners): 2-beat + reveal in the final clause; specific
numbers and/or a named character; deadpan voice; punch at the very end.
Our 3 previous one-liner entries were 1-beat with no twist and all finished
unranked — this build follows the winner structure, not ours.**

## Our entry (see variants.md for the full pairwise selection)

> I died doing what I loved: ignoring the check-engine light for 14 months. The car is fine. I am not.

- 100 characters / 100 bytes (limit 150). First-person dead voice,
  on-subject from the first words ("I died doing what I loved" — a classic
  epitaph opening, subverted).
- 2-beat + reveal: beat 1 = the beloved activity is mundane neglect
  (ignoring the check-engine light); beat 2 = escalation with a specific
  number (14 months); punch = "The car is fine. I am not." — a clean
  reversal of expectation (the car outlived the driver).
- Lands on one read, no parsing needed; quotable final beat.
- Fresh angle (no public entry does cars/check-engine); avoids all crowded
  angles (AI/context, password, dare, support hold, subscriptions, snooze).
