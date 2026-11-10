---
name: design-feeling
description: Use when designing or building any consumer screen, flow or component, especially onboarding, a first-run, a reveal, a pick or choose step, a plan, a booking, a loading or waiting state, a splash or a completion. Make sure to use this alongside screen-polish whenever a screen is being designed or coded, and whenever a design could feel generic, static, heavy or "fine but forgettable", even if the request never mentions motion, colour or feeling.
---

# Design feeling

## What this is for

The screens Rahul admires share a feeling more than a look. Things move and settle. The screens feel light. The colour is chosen, not defaulted. They stay calm even when the content is complex. Some are dark (a vinyl app, a cinema), many are light (a keychain app, an outfit picker, Quest's cards). What they share is that every choice serves one emotion.

This skill starts each design from the feeling it should create, then makes motion, colour, density and one standout moment serve it. These are principles to apply with judgement, not rules. The few hard lines are at the end. `screen-polish` still owns layout, controls and states, and `ui-copy` owns the words.

## 1. Name the feeling, then the concept

If the product has a `DESIGN.md`, its Feeling section, tokens and named motions come first: design inside them, and propose a change to the system instead of working around it (`design-system`). If not, before any layout, write down:
- **Three feeling words**: how the user should feel, for example "light, held, curious" or "focused, warm, unhurried". Use feelings, not styles: "premium", "modern" and "clean" are not feelings.
- **The peak**: the one moment in the flow where that feeling should be strongest.
- **The concept**: the real-world object or action this product is (a stack of stones, a guitar pick, a letter, a seat in a cinema). Pick one that is specific to this product, not to its category.

Check every later choice against the three words: does this make it feel more like that?

## 2. Movement: what makes it feel alive

In every sample, nothing simply appears. Things travel, settle and react.

- **Continuity.** An element becomes the next thing instead of being replaced. What was tapped grows into the next screen; the chosen object flies to where it will live. Keep the concept present on every screen, even if only as a small anchor, so the thread never breaks.
- **Weight and settle.** Objects move on springs: a slight overshoot, then rest. UI eases out. Nothing starts or stops dead, and nothing moves linearly.
- **Arrive as a group.** Related parts arrive slightly staggered, like a group that walks in together rather than a block that drops in.
- **Answer the touch at once.** A press gives instant feedback (a slight scale or tint). While dragging or holding, the visual follows the finger; on release, a self-running animation finishes it. On a phone, the moments that matter get a crisp, short haptic from the product's vocabulary, never a long buzz.
- **Light motion.** Short distances, opacity together with a small move, a soft blur that resolves into focus. Heavy motion uses long distances, hard cuts and everything moving at once.
- **Calm motion.** One thing leads and the rest follows or waits. If three things compete, choreograph them into an order.
- **A little ambient life.** A slow breath, a glint crossing a material, light drifting. It should be barely noticed and never noisy.
- **Act out the concept.** Ask what the object would physically do here (stack, press, flip, strum, unfold). That is the animation. If there is no answer, use a quiet crossfade.

Starting points, tuned by watching and not by numbers: presses around 150 ms, UI transitions 300–500 ms, object moments 500–900 ms on a spring, brand moments under 3 s.

## 3. Colour: chosen for the emotion

- **Derive the palette from the feeling and the concept's material**: morning paper and ink, brass and walnut, pool water and chalk. Light or dark is a decision for each product, never a default. Calm, health and daytime products often want light. Night, cinema and music may want dark. Do not reach for dark-with-glow because it looks dramatic.
- **One temperature family and one meaningful accent.** The accent marks what matters (the new chord, today, the choice). It is not decoration.
- **Colour as light.** Tints and soft gradients that behave like light falling on something, not flat fills or rainbows.
- **No cream by reflex.** "Warm" in a brief is not a reason for a cream or paper background with a terracotta accent; that is the most common AI look. Warmth comes from words, motion, photos and the accent. System white or grouped grey is often the most confident base for a native app.
- **Contrast is a hierarchy.** High contrast only for what matters now; everything secondary sits quietly at low contrast.
- **Squint test.** Blur your eyes at the screen: does the colour alone still say the three words?

## 4. Calm, even when it's complex

- **One idea per screen at a time.** Detail appears on tap, never as a wall.
- **Complex data becomes one shape.** Render it as a single object people read at a glance (a week as a stack, a song as a path), then use words for meaning. A glossy chart is still a chart: if it reads as bars, rings or a calendar strip, it isn't a shape yet.
- **Hierarchy through size and light, not boxes.** Fewer cards, borders and dividers. Let space do the grouping.
- **Air.** More spacing than feels necessary. Lightness is mostly empty space that is doing work.
- **Words.** A headline and at most one line of support. Turn numbers into human phrases ("Playing it by Wednesday", "the same 25 km you're used to"). Detail screens keep the same text budget as hero screens.

## 4b. Professional first

It must look like a shipped app from a great team, not a design experiment. Rahul picked a plain, native-feeling Groove screen over three more "designed" ones because it "looks like a professional app and not some science project done by a designer", and still disliked its decorative graphic. So: native structure and stock-feeling chrome first; character comes from colour, type, motion and words; a graphic appears only where it carries meaning a person needs, and must be crafted enough to sit next to Apple's own art. When in doubt, leave the graphic out.

## 5. The peak

Spend most of the craft on the peak from section 1. It usually comes from one of these:
- **Preview before commit**: show the outcome of a choice before the user pays for it.
- **The wait as a show**: processing or connecting becomes visible progress toward the payoff.
- **The object becomes the next thing**: a logo grows into a scene, picks open onto a fretboard, stones stack into a week.

Every other screen stays quiet so the peak lands.

## 6. The hero, drawn in code

No generated images unless Rahul says so, and he calls flat developer art "trash", so a code-drawn hero must look made:
- Choose geometry that code draws well: discs, stones, cards, strings, light, type and paths. Avoid people, animals and complex props.
- Light it like a material: layered gradients (base, shade, highlight, rim), a soft shadow, fine grain or texture, and one consistent light source.
- Give it depth with perspective, parallax between layers and reflections where the surface would have them.
- Or let type be the hero. Never use emoji, icon glyphs or grey placeholders as the hero.

## 7. Check by feel

Record the flow, watch it at real speed, then step through it slowly:
1. Does it feel like the three words? Name the moment that breaks it.
2. Does anything pop, snap, jump, flash, ghost or stop dead?
3. Does it feel light, or heavy, crowded and slow?
4. Is it calm? Does one thing lead at a time?
5. Cover the peak: does the flow go flat? If not, the peak isn't doing work.
6. Would the palette and concept fit a competitor unchanged?
7. **Hunt the jolts.** Look for the small seams people feel but can't name: a corner whose curvature kinks, two radii or spacings that almost match, a shadow from a different light, an element that lands a frame late, a number that jumps instead of counts, a keyboard that shoves the layout. Fix the ones you have stopped noticing.

Fix what you find and watch again.

## Hard lines

- Under `prefers-reduced-motion`, keep the meaning with short fades or instant changes.
- Animate transform and opacity, and keep it smooth on modest devices.
- Motion never blocks the user from acting or continuing.
- Text stays readable (WCAG AA), including over glows and gradients.

## Source and status

Distilled from a private reference pack (7 Nov 2026) on Vincent Nallatamby's thread about Quest's designer working in Claude Code (https://x.com/VNallatamby/status/2118811242592907427) and ten posts by Harshit (https://x.com/oiharshit), plus Rahul's notes on what he wants designs to feel like. Principles only; no assets, layouts or copy are reused.

- v0.1 (as `signature-moment`): concept, one hero moment, motion with a cause. Won A/B round 1 (23.5 vs 14.5 of 30) but pushed three of four runs to dark-with-glow and did not address feeling, lightness or colour.
- v0.2: rewritten feeling-first: three feeling words, movement, colour per product, calm with complex content. Removed the dark-ground default.
