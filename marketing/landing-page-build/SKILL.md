---
name: landing-page-build
description: Use when building a landing, waitlist or launch page for one of Rahul's products in code, or getting one ready to go live. Covers the page facts to gather, type and spacing tokens, motion implementation, every state, SEO and sharing tags, and the pre-launch checklist. Not for other UI work. The landing-page skill owns the story, look and copy; use both together.
---

# Landing page build

Forked from elayadesign/ai-design-skills `landing-page-design` (MIT). Part A keeps the useful structure; Part B is replaced with Rahul's values. See `_upstream/landing-page-design/CHANGES.md`.

A landing page wins one intent: **one product, one audience, one action** (usually joining the waitlist).

If the `landing-page` skill is available, it decides the story, the look and the hero. This skill decides how it is built and what must be true before it ships. When the two disagree, `landing-page` wins.

---

## Part A — Before building

### A1. Facts

Get these first. Read the repo, README, docs and earlier pages before asking. Ask once, in one message, only for what is still missing. If there's no answer, assume, state it in one line, and continue.

- The one action and what the visitor gets for it.
- Who it is for, and the change in their life.
- Real proof that exists: numbers, names, artwork, recordings. Nothing else may appear.
- Where it will be indexed or shared (search, X, WhatsApp, ads).

### A2. Conversion rules that hold

- One primary action. No competing CTAs above the fold, no nav.
- Be specific. "Learn the solo in Comfortably Numb" beats "master guitar faster".
- Proof sits beside the claim it supports, if there is proof at all.

### A3. Build order

Say in a few lines what you will build, then build in the order of the story: the first frame first, because a stranger decides there. Render after each section at desktop and 390px width and look at it. Never regenerate the whole page to change one section.

### A4. SEO and AEO

- **Index** the evergreen product page: `<title>` with the brand name, a meta description that states the promise plainly, canonical URL, and links from Rahul's other sites if they exist.
- **Noindex** ad-only or time-limited pages.
- If a FAQ exists, write it as plain question and answer and add FAQ schema. Don't add a FAQ only for SEO.
- `og:image` is a crafted 1200×630 frame of the page's strongest moment, not a screenshot of the hero with text cropped.

### A5. Pitfalls

- Vague value ("streamline", "optimise").
- Feature lists with no change in the user's life.
- A phone layout where the action is below the first screen.
- No clear next step after the form.

---

## Part B — Visual system (Rahul's values)

Every value resolves through tokens. Nothing is invented inline.

### B1. Type

- Define one type scale and a small set of named styles (`display`, `heading`, `body`, `caption`, `button`) as tokens. No ad-hoc sizes like `text-[19px]`.
- One typeface for the page. A warm serif or custom lowercase wordmark is allowed alongside it.
- Warm ink rather than pure black; give text a bit more air than the default.
- `text-wrap: balance` on headings, `text-wrap: pretty` on body. Break hero lines where the thought breaks.
- Never ultra-black weights for body text. Type must earn its place: if a line can go, it goes.

### B2. Spacing and radius

- Spacing comes from one token scale (4px base). Nothing between steps.
- Nested radius: when a shape sits inside another with a gap under 32px, `inner = outer − gap`, applied only when the result is above 2px.

### B3. Surfaces

- Flat colour surfaces with real texture or material where it helps (paper, felt, glass that refracts correctly).
- Soft edges: fades and progressive blur instead of hard bands between sections.
- Gradients only when executed at top quality and on purpose. No gradient text, no inner shadows, no plain drop shadow where glass belongs.
- Colour over black and white. Small splashes of colour carry the fun.

### B4. Hero

- The brand name, lowercase wordmark if there is one, not a slogan.
- One CTA, a button only. The email form comes after the click.
- No nav, no scroll indicator, no "Early access · Invite only" badge.

### B5. Icons and imagery

- Flat colour icons from one set. Icons replace words for controls.
- Real artwork, real logos kept faithful, specific subjects. Code-drawn art only if it is simple and crafted; otherwise leave it out.
- Nothing cropped, restraint in zoom and scale.

### B6. Motion

Character:
- Spatial continuity: one object turns into the next. Scroll plays like a film with a continuous camera; each section leads into the next.
- Each element reacts on its own to cursor and click, with stretch and bounce. A click should feel appreciated.
- Every animation says something. If it doesn't, remove it.

Implementation:
- Animate only `transform` and `opacity` (and `filter` for blur, sparingly). Never `top`, `left`, `width`, `height`.
- No browser default curves. Base: `cubic-bezier(0.22, 1, 0.36, 1)`, ~500ms for movement, 200–300ms for colour and opacity. Springs for interactive elements.
- Scroll work through `IntersectionObserver`, scroll-driven animations, or one listener throttled through `requestAnimationFrame`. Never an unthrottled scroll listener.
- `prefers-reduced-motion`: replace movement with a plain fade or the final state.
- No jank: check 60fps on a mid-range phone profile. A glitchy entrance is worse than none.

### B7. Content truth

- **Never invent facts.** Prices, numbers, users, testimonials and logos come from Rahul or a real source. When missing, use a marked placeholder like `{{waitlist_count}}` and list it in your message.
- No filler: "revolutionize", "supercharge", "cutting edge", "effortless", "seamless", "unlock", "harness the power", "next level", "world class".
- Sentence case. Warm, human, positive. No guilt, no gatekeeping.
- System messages are calm and specific. Errors say what happened and what to do. No exclamation marks.
- Use the `ui-copy` skill for the text pass if available.

### B8. States

Design every state; empty and loading are where premium shows.

- Hover, active (`scale(0.98)` or a 1px press), visible focus ring.
- Form: idle, typing, invalid (inline, specific), submitting, success (the warm close), already-joined, offline or server error.
- Loading: skeletons shaped like the real layout, never a bare spinner.
- Dark mode if the page supports it, designed, not inverted.
- No dead links. A button to `#` is either wired or not there.

### B9. Ship checklist

- [ ] `<title>`, meta description, canonical, `og:image`, Twitter card, favicon, apple-touch-icon
- [ ] Alt text on meaningful images; decorative ones `alt=""`
- [ ] Semantic HTML (`main`, `section`, `footer`), skip link, keyboard reachable form
- [ ] Privacy link in the footer; cookie consent only where required (no tracking means no banner)
- [ ] Email validation client-side and server-side; double submit prevented
- [ ] Branded 404 with a way back
- [ ] 390px and desktop: no horizontal overflow, action visible in the first screen
- [ ] Lighthouse performance and accessibility ≥ 90; images in AVIF/WebP with sizes; fonts preloaded and subset
- [ ] Scroll and capture several positions, not just the first frame

Domain, DNS, hosting, the form backend and analytics accounts are outward-facing: give Rahul a short checklist or a script, don't set them up.

---

## Your message to Rahul

About 60 words: what you built, screenshots at desktop and phone width, and any `{{placeholders}}` he needs to fill.
