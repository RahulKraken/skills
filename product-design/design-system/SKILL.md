---
name: design-system
description: Use to create, extract or extend a product's design system as an agent-readable DESIGN.md plus tokens in code. Make sure to use this when starting a new product or app, when a project has no DESIGN.md, when screens drift or look inconsistent, when Rahul says "set up the design", "codify this" or "make this consistent", and before designing any screen in a project whose DESIGN.md is missing or stale.
---

# Design system

## Why

Claude designs well for one screen and forgets everything by the next. Each screen invents its own colours, spacing and timings, and its own idea of what the product feels like. A design system fixes that by writing the decisions down once, where every session reads them. For an agent it does two jobs: it is the **memory** (what this product looks, moves and sounds like) and the **constraint** (use these values, not new ones).

Code holds the values. `DESIGN.md` holds the meaning: what each value is for, what the product should feel like, and the rules with their reasons. An agent reads `DESIGN.md` first and the token files second.

## The anatomy

Every DESIGN.md has these sections, in this order. Template: `references/DESIGN.template.md`.

1. **Feeling**: three feeling words, what it must never feel like, the concept (the real-world object or action the product is), and the peak moments. This is the layer most systems skip, and it is the one that makes screens feel like one product. `design-feeling` explains how to find it.
2. **Principles**: three to six, each one sentence plus its reason.
3. **Colour**: semantic tokens (what each is for), the accent rules (when a colour may appear), light and dark.
4. **Type**: the styles, what each is for, Dynamic Type or zoom behaviour.
5. **Space, shape and material**: spacing scale, radii, control sizes, elevation, glass or blur, texture, light.
6. **Motion language**: the named motions (one vocabulary, no screen writes its own curve), how screens hand over to each other, the signature moments, Reduce Motion.
7. **Visual language**: icons, illustration, imagery, where artwork may appear.
8. **Components**: each with its job, when not to use it, its states and where it is drawn.
9. **Blocks**: sections made from components that recur on real screens.
10. **Voice**: a pointer to the voice and copy rules.
11. **Rules everywhere**: one sentence each, with the reason after it.
12. **Open decisions**: what is not decided. An agent asks Rahul before it fills one.
13. **Sources and changelog**: the token files that hold the values, the canvas or boards, and dated changes.

## Choose the mode

### Extract: the product already has screens or code

1. Find what exists: token files (colours, type, spacing, motion), component code, design boards, notes, tests, and decisions in commit messages. Code is the truth when code and a board disagree; list each disagreement under Open decisions.
2. Write sections 2 to 13 from that evidence only. Name each source. Document only what exists: a documented variant that is not built makes agents use it.
3. Write the Feeling section as a **proposal**: infer the words and concept from what the product already does, mark it `Proposed, ask Rahul`, and say what evidence you used. Never present an inferred feeling as decided.
4. List the gaps (no colour personality, no signature moment, motion that is only functional) under Open decisions.

### Create: a new product

1. Run `design-feeling` section 1 with Rahul: three feeling words, the concept, the peaks. One short exchange, not a questionnaire.
2. Build two or three directions as rendered samples of the same key screen, each a full answer to the feeling (palette, type, one signature motion). Put them side by side on one page and let Rahul pick. He judges visuals, not descriptions.
3. Write the picked direction as tokens in code (CSS custom properties, a Swift `Palette`/`Motion`/`Metrics`, or the platform's equivalent) and as DESIGN.md.
4. Build one real screen from the system and record it (`review-screen`). Fix the system, not only the screen.

### Extend: during normal work

- Before designing a screen, read DESIGN.md. Use its tokens and named motions. Do not invent a value; if one is missing, add a token (and say so) or ask.
- When a pattern appears on a second screen, make it a block in section 9.
- When Rahul corrects something, write a rule: what Claude did, what he wanted, and why, as one sentence plus its reason in section 11.
- When a decision is made, move it from Open decisions to its section and add a dated line to the changelog.

## Keep it true

- One place for each value. DESIGN.md names the token and its source file; when it shows values for quick reading, it says which file wins.
- Short beats complete. An agent reads every word, every time. Put long catalogues (all 192 boards) in the sources, not in DESIGN.md.
- Use the project's own language rules for the file (for example ASD-STE100 for technical documents).
- After a change to tokens in code, update DESIGN.md in the same commit.

## Done means

DESIGN.md exists at the path the project uses (`design/DESIGN.md` or the root), the project's agent file (`AGENTS.md` or `CLAUDE.md`) points to it, every section is filled or listed under Open decisions, and one screen built from it passes `review-screen`.
