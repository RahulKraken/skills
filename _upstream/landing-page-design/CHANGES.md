# What I changed and why

Result: `marketing/landing-page-build/`. It is a companion to my tested `landing-page` skill, not a replacement. `landing-page` owns the story, the look and the copy. `landing-page-build` owns the build and the launch checklist.

## Trigger

- **Upstream:** any landing page, marketing site, web UI, component, dashboard or prototype, and "always consult it" before any font, spacing or colour choice. It would take over every UI task and override my other product-design skills.
- **Mine:** only when a landing, waitlist or launch page for one of my products is being built in code or made ready to go live.

## Part A (strategy and structure)

| Upstream | Decision | Why |
| --- | --- | --- |
| A1 intake | Kept, cut down | Useful facts to have before building. Cut ICP, objections and traffic source. Ask once, assume and state the rest, pull from my repos and docs first. |
| A2 page structure (screenshot hero, benefits, how it works, testimonials, FAQ) | Dropped | This is the feature page I have rejected ~15 times. `landing-page` owns structure. |
| A3 layout types | Dropped | Same reason. |
| A4 conversion rules | Kept two | One primary action, no competing CTAs. Benefit-first and risk-reversal sections go: I sell the life change, not features. |
| A5 headline formulas | Dropped | They produce slogans. I want the brand name in the hero. |
| A6 build order | Replaced | Build in the order of the story, render after each section. |
| A7 SEO and AEO | Kept | Nothing in my skills covered it. |
| A8 pitfalls | Kept the objective ones | |

## Part B (visual system), replaced with my values

| Upstream | Mine |
| --- | --- |
| B1 font allowlist and banlist, no italics, no hyphens, Tailwind-only type scale, 26 named text styles | One defined type scale and named tokens, no ad-hoc sizes. Warm serif wordmark allowed, warm ink instead of pure black, a bit more air. Kept `text-wrap: balance / pretty`. |
| B2 fixed spacing table | Kept the principle (tokens only, no invented values), dropped the table. |
| B3 nested radius formula | Kept as is. |
| B4 no gradients ever, fixed dark palette | Gradients only at top quality. Soft edges (fades, progressive blur) instead of hard bands. No inner shadows. |
| B5 gradient hero text, 680px cap | No gradient text. Brand name in the hero, button-only CTA. Kept meaningful line breaks. |
| B6 icon allowlist | Flat colour icons from one set. Real logos, kept faithful. |
| B7 motion curve and nav | Kept the technical rules (transform and opacity only, no default curves, reduced motion, IntersectionObserver or rAF). Dropped the floating nav (I want no nav). Added spatial continuity, film-like scroll and per-element micro-interactions. |
| B8 content realism | Kept "never invent facts", marked placeholders, banned filler words and calm system messages. Dropped invented testimonials and logos. |
| B9 states | Kept, plus my rule that empty and loading states are where premium shows. |
| B10 ship requirements | Kept. Added: deploy, domain and form backend are mine to do, as a checklist. |
| B11 mandatory tagline reveal | Dropped. I don't want taglines. |
| Output format (outline, benefits, FAQ before code) | Dropped. Say what you'll build in a few lines, then build. |

## Test, 2026-11-01

One blind A/B on `evals/encognition-launch`, both runs with `landing-page`, one adding `landing-page-build`. With the skill: 4 of 6 graders vs 1 of 6. It added full sharing tags, every form state and marked placeholders; the baseline faked success with no endpoint. Both missed a real launch checklist and the skill run dropped dark mode, so v1 now requires both.
