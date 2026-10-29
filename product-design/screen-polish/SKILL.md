---
name: screen-polish
description: Use when building, redesigning or reviewing any app or web screen, sheet, flow or component for Rahul's products, such as a logging screen, settings, onboarding, a detail page or a home screen. Make sure to use this whenever a screen is being designed or coded, including HTML mockups, even if the request only says "make the X screen".
---

# Screen polish

## Context

Rahul builds calm consumer products (Pillar, a health coach; Meusic, a guitar teacher) and judges screens by using them. Across those projects, most rejections came from the same few things: generic AI-looking layouts, clutter, controls in the wrong place, hidden actions, missing states, and screens that only worked on the happy path. "Calm" never means less capability: the models are the Claude, ChatGPT and Cursor apps, "packed with functionality but at the same time, so clean".

## Work in two phases

1. **Design** the screen fully, then render it and look at it.
2. **Text pass:** edit only the words with the `ui-copy` skill (its script lists every visible line).

Keep them apart. Polishing words while designing made designs thinner in testing.

# Phase 1: Design

## Before drawing

- **Look at real references first**: Gentler Streak, Apple's own apps, ChatGPT, Claude, Flighty, GarageBand, Mobbin. Note the principle you take from each, not the look. "I'm not saying copy it, but principles." Without references, Claude draws the average.
- **Name the most frequent action** on this screen. Everything is arranged around making it fast.

## Layout rules (each one came from a rejection)

- **One dominant object; use the whole screen.** "one huge guitar and everything happening over there". Empty space that holds nothing is a fault.
- **Controls live in a top or bottom bar, never over the content**, and near the thumb on phones. "all settings go either on a top bar or at bottom bar".
- **Icons over words for controls**, with a hint on hover or long-press. Words are for teaching and feedback.
- **Fewest taps for the most frequent action.** "To take a snap right now there's two taps… just have dedicated camera button". Capture and go: no celebrations in the way.
- **Visible actions, nothing hidden in menus** ("putting things inside menus i hate it"). But secondary or destructive actions are quiet: an icon or a long-press, never a loud button. Tapping something shows its details, never triggers the risky action.
- **Smart inline UX instead of toggles and settings.** "not toggles, all these need to be smart ux, easy to add but not cluttered". Good behaviour is the default, not an option.
- **The user can override the system**, and the screen shows what the change will do.
- **One shared flow.** No separate one-off pages that break the product's layout ("why separate page? I want to experience the product").
- **Every element earns its place.** If its purpose isn't obvious at a glance, cut it or redesign it.

## States are where premium lives

Design every state, not just the happy one: empty, loading, first use, error, long content, dark mode. "nothing states… are the spots to add premiumness and polish". Every interaction gets feedback: a press state, motion on fields and buttons, something that shows the app is listening or working. Nothing appears or vanishes abruptly.

## Native feel

Follow the platform (Apple's guidance, Liquid Glass on iOS) and check it before inventing: "is this approved apple way?". Glass for chrome and sheets, not content cards.

## Check it renders

Render the screen (browser pane, or `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --window-size=1280,2400 --screenshot=out.png file.html`), read the image, crop at real size, and check:
- The mockup page fits the viewport you render at (1280px): phones wrap to a new row instead of overflowing, and nothing is clipped.
- At real size, is the main action obvious in two seconds?
- Every state renders: icons, fonts, data. Nothing blank, clipped or overlapping.
- It looks finished next to the references, with a real device frame and real-looking content, not grey placeholder blocks.

Fix and look again. "Don't do half work."

# Phase 2: Text pass

Use the `ui-copy` skill on the finished screen: list every visible line, keep only insight, milestone, next step or needed facts, and change words without touching the design. Then write your message to Rahul: about 60 words, your pick and the user-facing reason.

## Where this bends

- If Rahul names a reference to follow closely ("just copy garage band here"), follow it.
- Tools and dashboards (a profiler) trade some calm for precision; readable data comes first.
