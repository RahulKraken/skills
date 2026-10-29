---
name: ui-copy
description: Use whenever writing or reviewing words that appear inside a product UI, such as headlines, labels, buttons, empty states, errors, onboarding, paywalls, notifications, widget text, tooltips or waitlist copy. Make sure to use this for any screen, widget or page mockup that has text on it, even if the request is about design and never mentions copy.
---

# UI copy

## Context

Rahul's most repeated complaint across every project is text: too much of it, and not good enough. "any text which doesn't need to exist shouldn't exist", and "text is going to be read and it carries concrete meaning so use text when absolutely necessary and it must make clear sense". Claude's default is to label, caption, add a legend and explain itself, because text feels safe. Every extra word competes with the design that should carry the meaning, and a weak line makes a polished screen feel unfinished.

Rules alone didn't fix this in testing. What worked was listing every visible line and judging each one, as a separate pass after the design is done.

## The bar

**A line earns its place only if it gives the user an insight, a milestone, the next thing to do, or a fact they need**, in words they would say themselves. Everything else goes.

## Voice

- **Warm, forward, human.** "We're ironing out the rough edges, join the waitlist and we'll let you know when it's ready" instead of "Invite only". "Your week starts tonight" instead of "No data yet".
- **A coach, not a judge.** Short is "short", not "missed". No guilt, no streak-shaming.
- **Direct about hard numbers, and respectful.** "We should not shy away from the numbers because these numbers mean things." Don't over-hedge, and don't play doctor.
- **Explain why, never just no.** "Never say no, always tell why your goal is unrealistic and what would make it achievable."
- **Specific, never stock.** "2 km ahead of plan", not "On track". No "Hi, I'm your coach" openers.

## The budget

- One headline per surface at most. Short labels only where they name a fact on the design itself.
- No eyebrow labels ("SLEEP · LAST 7 NIGHTS"), legends that colour can teach, captions, status chips that repeat the headline, usage hints ("Tap to see more"), "(optional)" tags or scaffolding like "Why:" and "Next:".
- Icons over words for controls; words for teaching and feedback.
- Empty states: one short, warm line. Errors: what happened and what to do, in one sentence.

## The five ways text goes wrong

Real lines from Rahul's projects and test runs, each with its fix. Check for each pattern by name.

1. **Describing the design.** "Your whole plan, and where you stand in it" → cut. "Follow your week back into your sleep zone" → cut.
2. **A label instead of a sentence.** "This week" → cut. "21 km week" (actual or target?) → "21 of 22 km · 1 to go".
3. **Machine numbers.** "Tempo 5.0 km" → "5 km tempo". "Cached 84,843,384" → "85M cached". "Bed by 10:55" → "Asleep by 11".
4. **The insight in the wrong place.** "5 of 7 nights hit 7½h" (a scoreboard) → "Both short nights started after midnight" (why).
5. **Filler around the work.** Justifying the design, explaining how it works, housekeeping. In messages to Rahul too: pick plus reason, about 60 words.

## Procedure

1. Write the design first. Draft words quickly; don't polish while designing, because in testing that made designs thinner.
2. List every visible line: `python3 <this skill's folder>/scripts/visible_text.py page.html` (renders the page and prints each string). For non-HTML work, list the strings by hand.
3. Mark each line **keep**, **rewrite** or **cut** against the bar and the five patterns. Write the list down so nothing is skipped.
4. Change only the words, never the design. If cutting a line would lose a fact the user needs, rewrite it instead.
5. Run the list again until every line is a keep.
6. **Your message to Rahul follows the same bar: about 60 words.** Say what you made and the one choice that matters, in user terms. Don't restate the screens or justify the approach; the mockup shows them. In testing, this was the rule most often broken even when the screen copy was excellent.

## Where this bends

- **Data in tools** (names, values, column headers in a profiler) is content, not copy. Judge the words around it.
- **Legal and consent text** has to say what it has to say. Make it plain, not short.
- **First use of a new control** can carry one word next to its icon.

## Good lines from Rahul's projects

"Half your spend came from 5 sessions". "Sunday · 8 km, your longest run yet". "Asleep by 11 tonight". "Your week starts tonight". "We're ironing out the rough edges. Join the waitlist and we'll let you know when it's ready for you."
