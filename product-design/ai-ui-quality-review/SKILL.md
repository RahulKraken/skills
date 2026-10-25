---
name: ai-ui-quality-review
description: Use when building, reviewing, or polishing any UI, landing page, product screen, or visual asset made with AI, and when output risks feeling generic, templated, or "done too early". Make sure to use this whenever the user asks to "make it look good", "polish", "review this design", "does this feel generic", "critique this page", or starts a new UI from a one-line prompt, even if they never mention quality or design systems.
---

# AI UI Quality Review

LLMs return the most probable answer, which for UI means the average of what already exists. They also make things look finished in seconds. The result is generic, interchangeable software ("zombie UI"). This skill adds the two things the model won't supply on its own: a point of view before building, and an editor's pass before calling anything done.

## 1. Before building: establish a point of view

Without one, the model fills the gap with the statistical default. Gather these first, from the user, existing brand or design-system files, or the codebase:

- Who the users are and what they care about (not only what they say they want)
- The brand's personality in a few concrete words, and what each word means in practice (color, tone of copy, motion, density)
- What "good" means here, and what the product must never feel like

If a design system or brand guide exists, read it first and follow its templates and flows, not just its components. If none exists and the answer isn't obvious, ask two or three short questions before generating anything. A specific brief produces a specific result; "a website for my restaurant" produces the average restaurant site.

## 2. While building: specificity over defaults

- Put the point of view into the prompt and the code: real copy in the brand's voice, deliberate color and type choices, no lorem ipsum.
- Anticipate the user's context. Design the empty, error, and loading states. Put troubleshooting where the user will get stuck. Show the small things that prove someone thought about them, such as today's date on a calendar tab.
- Treat motion, spacing, and radii as decisions, not defaults.

## 3. Before calling it done: the editor pass

Done is not good. Quality filtering used to happen throughout the process; with AI it all lands after the build, when it is hardest to say no. Experience the result as a user would, end to end, then run these checks:

1. **Swap test.** Replace the brand name with a competitor's or an unrelated one. If nothing else needs to change, it is generic.
2. **Problem test.** Does it solve the user's actual problem, in the way they think about it?
3. **Coherence test.** Do the screens hold together as one journey, or only look good in isolation?
4. **Detail test.** Go one level deeper than a customer could see. Flag arbitrary choices (a color that could just as well have been another) and fix or justify them.
5. **Surprise test.** Is there at least one detail that shows the maker anticipated a need?
6. **Contrast test.** Is there one deliberate move (a color, a jump in scale, a break in the grid) that the rest of the design is built around? Cover it with your hand: if the screen goes flat, it was doing real work. Good surprise is a deliberate choice that resolves, not randomness.
7. **Echo test.** Do motifs such as radius, spacing, motion, and copy tone repeat at several levels in ways a user feels but can't name? Subtle, numerous echoes make a design feel like one thing; a single obvious repeat does not.
8. **Ownership test.** Would someone want to maintain this? Disposable output is a smell.

For anything important, ask a separate agent to critique the result adversarially, then keep pushing yourself. Expect several iterations; the first version is a draft.

## Output when reviewing

Keep it short:

- **Verdict:** one line on whether it reads as intentional or generic, and why.
- **Fixes:** the top issues ranked by impact, each with a concrete change.
- Apply the fixes when the user asked for polish, otherwise propose them.

## Source and status

Synthesized from two sources:

- Katie Dill (Stripe), "How to scale intent, quality, and artistry with AI", Lenny and Friends Summit, September 2026: https://www.youtube.com/watch?v=GLvFTMtw4Jk. The framing (point of view, encoded standards, editor pass) follows the talk.
- Nabeel Qureshi, "What Makes Art Great?": https://nabeelqu.substack.com/p/what-makes-art-great. The contrast and echo tests come from its surprise and echoes sections, using its Fra Angelico and Chartres rose window examples.

The eight checks are my own condensation of both.

Status: draft v0.2, untested. Add changes below with a one-line reason.

- v0.2: added contrast and echo tests from the Qureshi article.
