---
name: product-review
description: Use to review a whole product or a full journey as a user would live it, checking whether it creates the intended feeling across every surface, not one screen. Make sure to use this before a launch, a beta, a TestFlight or a demo, when Rahul asks "does this feel right", "review the product", "is it ready" or "why does it feel off", and after several screens or features land, even if each one already passed review-screen.
---

# Product review

## Why

Every screen can pass `review-screen` and the product can still feel wrong. The feeling lives in the seams: the store page promises one thing and the first open says another, onboarding is calm and the first notification is shouty, the app is fast and the email link opens a slow web page, design is careful and an error dumps a stack trace. Users feel the product as one thing. This skill reviews it as one thing: design, engineering, copy, performance and everything outside the app, against the feeling it is meant to create.

## 1. Set the bar

Read the product's DESIGN.md Feeling section (three feeling words, the "never" list, the peak moments). If there is none, write a proposal from what Rahul has said, mark it `Proposed`, and review against that. A review without a stated feeling is only taste.

## 2. Map the journey

List every touchpoint a real user meets, in order, including the ones outside the app:

1. **Before:** store page or landing page, icon, screenshots, first link someone shares.
2. **First open:** launch, permissions, onboarding, sign-in.
3. **First value:** the moment the product first does its job for this person. Time it.
4. **The daily loop:** the most frequent action, start to finish.
5. **Reaching out:** notifications, emails, widgets, share sheets, links back in.
6. **When it breaks:** errors, offline, empty, slow network, bad input, a permission denied.
7. **Money:** paywall, trial end, receipt, cancel.
8. **The return:** opening after a week away, after an update, on a second device.
9. **Leaving:** sign out, delete account, export.

Mark the 3–5 high-contact moments (the peaks and the daily loop). They get most of the scrutiny.

## 3. Walk it as a user

Use the real build (simulator, device or browser), on a fresh account, at real speed. Record it (`review-screen` scripts). Do the boring things too: deny a permission, go offline mid-action, come back to a stale screen, type a long name. Note the time to first value and every wait over about half a second.

## 4. Judge each touchpoint against the feeling

For each one, answer in a line:

- **Feeling:** does it feel like the three words? Which word does it break?
- **Promise:** does it deliver what the touchpoint before it promised?
- **One system:** same corner curve, spacing, type, motion vocabulary, voice and haptics as the rest? Surfaces built by different tools (email templates, web pages, store art, system dialogs) drift first.
- **Jolts:** any small friction a user feels but can't name: a lag, a layout shove, a flash, a double tap needed, a keyboard covering the button, a copy tone change, a number that disagrees with another screen.
- **Effort match:** is the craft where the contact is? A polished settings page next to a rough daily loop is effort in the wrong place.

## 5. Judge the whole

- **The one-sentence test:** after the walk, how would a user describe the product to a friend? Does that sentence contain the feeling words?
- **The peak:** does the peak land, and does every other moment stay quiet enough to let it?
- **The weakest seam:** the single transition (between two touchpoints) that most breaks the feeling. A product feels as good as its worst seam on the daily path.
- **Compounding:** which fixes are system fixes (one token, one shared component, one voice rule) that improve many touchpoints at once? Prefer them.

## Output

Short. Lead with the verdict.

- **Verdict:** one line: does the product create the feeling, and where it breaks first.
- **Journey table:** touchpoint · feeling words held or broken · the jolt (if any). High-contact rows first.
- **Fixes:** ranked by what a user would feel first, each with the touchpoint, the evidence (frame, timing or line) and the concrete change. Mark system fixes. Five at most; the rest go in a list at the end.
- **Not reviewed:** touchpoints that could not be reached (store page not live, no email set up), so the gaps are visible.

Do not fix during the review unless Rahul asked for fixes. Outward-facing changes (store listing, emails to real users) are Rahul's to make: give him the change, not the action.

## How this fits

`product-thinking` decides whether to build and which moments matter. `design-system` and `design-feeling` make each screen right. `review-screen` checks one screen. This skill checks that it all adds up.

## Source and status

v0.1, untested. Built 10 Nov 2026 from the Apple design teardown (Aman, "Why Apple Products Just Look So Good?", Mar 2026): quality is the absence of small jolts, one primitive enforced across every surface, extra care at the touchpoints, and a moat made of many processes tuned together.
