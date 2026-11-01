# A/B round 1 (2026-11-01)

Blind judge, one run per arm, 1280x800 viewport. X/Y labels randomized, unblinded after scoring.

| Case | With Stageshow | Without | Winner |
| --- | --- | --- | --- |
| pillar-hero-loop | 14/25 | 16/25 | without |
| pillar-bento-still | 15/25 | 18/25 | without |

What the skill did better: restraint (4 vs 2 on both cases), real crops instead of shrunk windows.
What it did worse: read as half-wireframe (placeholder bars), stage cut off flat with blank page below at 1280x800, loop glitches (card reverts with no cause, notification vanishes), loop under its own 10-16s rule.

Caveats, so treat as weak evidence:
- npm was blocked in the test box: no vite playground, React 19 instead of 18, lucide-react shimmed from react-icons. Stages were built with esbuild and filmed without the playground host page, so a stage meant to sit inside a page section was shown bare.
- With-skill agents used their full time and skipped the `--gate` check; baseline agents had a neutral screenshot tool.
- n=1 per case, one LLM judge.

Verdict: does not pass rule 5 yet. Stays in `_upstream/`. Re-run on a machine with npm and the real playground before deciding.
