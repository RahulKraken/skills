# A/B round 2 (2026-11-07): Groove from scratch (create mode)

Input: `groove-from-scratch/brief.md` (product principles and feel only, no existing visuals).
Arms: B = `screen-polish`, `ui-copy`, `ai-ui-quality-review`, `design-feeling` v0.2. C = the same plus `design-system` (create mode with `feeling-to-system.md`) and `review-screen`. Each run made a system, then three moments. 2 runs per arm, one blind LLM judge with the brief, each DESIGN.md and the recordings. 7 graders, /35.

| | C run 1 | C run 2 | B run 1 | B run 2 |
| --- | --- | --- | --- | --- |
| Total | 28 | **31** | 29 | 30 |

Mean 29.5 vs 29.5: no measurable difference. C scored higher on "shipped app" and consistency, B on distinctiveness.
The bigger finding: all four systems converged on the same answer (warm off-white, clay or ember accent, a serif coach line, the week as one flowing shape). The brief plus `design-feeling` already pull every run there, with or without the skill.
C's directions were straw men: two of three broke the brief (a dashboard, a design experiment), so the agent's own pick was easy. Fixed in `feeling-to-system.md`: every direction must satisfy every feeling word and "never".
Verdict: create mode does not pass rule 5 when run without Rahul. Its value is the step this test removed: three real directions for Rahul to pick from. Next test: Rahul picks from fixed directions, then screens are built from his pick.

# A/B round 1 (2026-11-07): Groove "your week"

Arms: P = `screen-polish`, `ui-copy`, `ai-ui-quality-review`, `design-feeling` v0.2. S = the same plus `design-system`, `review-screen` and Groove's `design/DESIGN.md` with its Swift token files.
2 runs per arm. One blind LLM judge saw the recordings (frame sheets at 6 fps), the code and the product's DESIGN.md. 7 graders, /35.

| | S run 1 | S run 2 | P run 1 | P run 2 |
| --- | --- | --- | --- | --- |
| Total | **32** | 24 | 22 | 20 |
| Fits the product | 5 | 5 | 1 | 1 |

What the system did: both S runs read as the same app (palette, type, capsules, named motions, chat hand-overs). Both P runs invented a new product: serif type on cream with purple and ochre, the stock "tasteful AI" look. S1 used the Balancer concept and landed the week as one pile, the peak that DESIGN.md proposes.
Where S was weak: S2 had no single peak and ended crowded; S1 opens on a near-blank screen for about 2 s while the reply streams, and neither used the five verdict words.
Caveats: n=2, one LLM judge, and the judge had DESIGN.md, which favours S on "fits the product" by design. Feeling is Rahul's call (Feel Test page).
