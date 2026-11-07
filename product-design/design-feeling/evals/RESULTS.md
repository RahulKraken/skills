# A/B round 2 (2026-11-07), design-feeling v0.2

Arms: A = current skills (round 1 runs reused, unchanged baseline). C = current skills + `design-feeling` v0.2.
Judges saw the recorded demo videos (dense frame sheets) as well as stills. 8 graders: the 6 from round 1, plus 07 movement feels alive and 08 colour and calm. Total /40.

| Case | C run 1 | C run 2 | A run 1 | A run 2 |
| --- | --- | --- | --- | --- |
| pillar-first-run | 29 | **34** | 16 | 15 |
| meusic-pick-a-song | **33** | 31 | 21 | 25 |
| **Mean** | **31.75** | | **19.25** | |

Feeling graders only (07 + 08, /10): C 8, 7, 8, 8 vs A 4, 4, 5, 6.
Theme: all four C runs chose light palettes (cream, clay, sunset covers). The dark-with-glow default from v0.1 is gone.

Weak spots in C: one blank stall before the week rebuilds (Pillar C2), heavy blur crossfades that leave muddy frames (both Meusic C runs), dense detail maps (Meusic C2).
Caveats: n=2, one LLM judge per case. A1 and B1 in round 1 read Rahul's memory; C builders were told not to. Feeling is Rahul's call: human blind rating pending (Feel Test page).

# A/B round 1 (2026-11-07)

Arms: A = current product-design skills (`screen-polish`, `ui-copy`, `ai-ui-quality-review`). B = same + `signature-moment` v0.1.
2 cases × 2 arms × 2 runs. One blind LLM judge per case scored all four runs under shuffled labels (W–Z), 6 graders × 1–5 = /30. Unblinded after scoring. Code-only visuals, no image generation.

| Case | B run 1 | B run 2 | A run 1 | A run 2 |
| --- | --- | --- | --- | --- |
| pillar-first-run | 20 | **26** | 13 | 14 |
| meusic-pick-a-song | 22 | **26** | 14 | 17 |
| **Mean** | **23.5** | | **14.5** | |

B took the top two places in both cases: 8/8 pairwise wins.

What the skill did better: a single concept carried through (stacked week-stones for "Pillar", guitar picks that open onto a fretboard for Meusic); a clear payoff moment; heroes lit like materials instead of flat charts and album-art blocks.
Where the skill was weak: the concept drops out on middle screens (Pillar B2's Health and goal steps are stock lists); a glossy chart is still a chart (Pillar B1); detail screens drift back toward small grey text (Meusic B2).
Where A was weak: stock bar charts as the payoff, generic album-art cards, a transition glitch (doubled headline) and a cut-off list.

Caveats, so treat as moderate evidence:
- n=2 per arm, one LLM judge per case, same model family as the builders.
- One A and one B Pillar run read Rahul's memory notes (Pillar palette); the other two didn't.
- Three of four B runs went dark-with-glow. Watch for the skill collapsing every product into one look.

Verdict: passes rule 5. v0.2 should add: keep the hero object present on every screen (at least as an anchor); a shiny chart is still a chart; detail screens obey the same text budget.
