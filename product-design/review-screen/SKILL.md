---
name: review-screen
description: Use after building or changing any screen, flow, mock or component, before showing it to Rahul or calling it done. Make sure to use this whenever UI work is about to be reported as finished, including HTML mocks, SwiftUI views and web pages, even if nobody asked for a review.
---

# Review screen

## Why

Claude judges its UI from the code and stops at "close enough". It almost never watches its own motion, so snaps, ghosting and blank frames reach Rahul. This skill makes Claude look and watch first, and check the work against the product's own system, not against generic taste.

## 1. Look and watch

Record the screen or flow before judging it.

- **Web or HTML mock:** `python3 scripts/record_web.py <page.html or URL> <out-dir> [--demo "window.__demo()"]`. It writes a still, a video cropped to the phone if there is one, and a frame sheet of the motion (`frames.jpg`, 6 frames a second). Read the still and the frame sheet. It also prints any stretch of half a second or more where the screen is nearly blank (`blank.txt`): fix each one unless it is a deliberate splash.
- **iOS:** `scripts/record_ios.sh <out-dir> [seconds]` records the booted simulator and makes the same frame sheet. Drive the flow while it records (UI test, `simctl` URL, or by hand).

Look at the frame sheet transition by transition. Two rounds of fix and re-record at most, then show Rahul with the recording.

## 2. Check against the product

Read the project's DESIGN.md first. If there is none, say so and use `design-system` to make one.

1. **Tokens only.** No raw colour, size, radius, duration or curve that is not a token or a named motion. List each one with the token it should use.
2. **Feeling.** Does it feel like the three feeling words? Name the frame where it breaks.
3. **Motion.** Every motion is a named motion with a visible cause. Nothing pops, snaps, ghosts, doubles, flashes blank or stops dead. Things carry into the next screen.
4. **States.** Empty, loading, error, offline, long content, large text, dark: each one exists or is listed as missing.
5. **Rules.** Every rule in DESIGN.md section 11 holds.
6. **Generic test.** Would this screen pass for a competitor's? Is there one thing only this product would do?
7. **Words.** Every visible line earns its place (`ui-copy`).
8. **Access.** Contrast, target sizes, Reduce Motion, Dynamic Type or zoom.

## Output

- **Verdict:** one line, ready or not, and why.
- **Fixes:** ranked by what Rahul would notice first, each with the frame or line and the concrete change.
- Fix them when the task was to build; otherwise propose. Send the recording with the result.
