---
name: product-thinking
description: Use whenever deciding what to build, whether a product idea or feature is worth it, why users aren't converting or retaining, or how to read user feedback and metrics. Make sure to use this before starting to build a new idea, when someone says "users loved it", "let's just build it", "should I build X" or "why isn't this working", even if they never mention strategy.
---

# Product thinking

## Context

Product bets are analysis under uncertainty, and the analyst's own mind is the biggest source of error. Knowing about biases doesn't fix them; only process does. This skill is that process: treat every bet as a hypothesis to falsify, not an idea to defend. Lessons below grow over time, each with its source.

## What to do

1. **Write competing hypotheses first.** For any bet or diagnosis, list at least three explanations before favoring one, including the boring ones (wrong audience, no real pain, pricing, onboarding). Never build on the first framing.
2. **Weigh evidence by diagnosticity.** For each piece of evidence ask: is this more likely under one hypothesis than the others? If it fits all of them, drop it however vivid it is. Praise, "I'd use that" and waitlist signups fit both "real need" and "being polite".
3. **Prefer behavior over words.** Paying, switching, repeat use and existing workarounds are diagnostic. Opinions are not.
4. **Ask what's missing.** "If this were true, what should we already be seeing?" A real pain usually has workarounds (spreadsheets, scripts, paid hacks). No workarounds is a red flag.
5. **Pick the hypothesis with the least evidence against it**, not the most evidence for it.
6. **Don't buy confidence with more data.** Before another round of interviews or dashboards, check whether the model itself needs rethinking.
7. **Pre-register before building.** Write the prediction ("I expect X% to do Y within Z, because…") and the kill criteria (what result makes us stop or pivot), while nothing is invested yet.
8. **Name the expert blind spot.** Deep domain knowledge hides how newcomers see the problem. Plan to watch a non-expert use it.
9. **Decide the feeling before the scope.** Once a bet passes, write the experience it must give (three feeling words) and the 3–5 moments users touch most (first open, first value, the daily action, confirmation, the return). Spend effort there; elsewhere "fine" is fine. Let the feeling set the engineering constraints, not the reverse. Hand the details to `design-system` and `design-feeling`; check the whole with `product-review`.

## How to report

Short. A small table of hypotheses × key evidence (consistent / inconsistent / neutral), then: the leading hypothesis, the cheapest test that would kill it, the prediction, and the kill criteria. Flag which evidence was dropped as non-diagnostic. Don't start building until the test and criteria are agreed.

## Where this bends

- Small, cheap, reversible changes: skip the table, just state the prediction and ship.
- When Rahul says "just build it, I've decided", note the riskiest assumption and its kill criterion in one line, then build.

## Lessons

Add new lessons here: one line, the behavior it changes, and the source.

- Awareness of bias doesn't remove it; use structured methods instead. (Heuer, *Psychology of Intelligence Analysis*, 1999)
- Evidence consistent with every hypothesis is worthless. (Heuer, ch. 8 ACH)
- More information raises confidence faster than accuracy. (Heuer, ch. 5)
- First impressions anchor; delay judgment on ambiguous early data. (Heuer, ch. 2)
- Absence of expected evidence is evidence. (Heuer)
- Hindsight inflates how right you were; write predictions down. (Heuer, ch. 13)
- Quality is mostly the absence of small frictions users feel but can't name; plan for removing jolts, not adding features. (Apple design teardown, Aman, Mar 2026)
- Over-invest at the few high-contact moments (Apple's unboxing, the Face ID tick); they set the impression of the whole product. (same)
- A moat is many small processes tuned together over years (Apple's colour, material, finish), not one trick a rival can copy. Prefer bets that compound. (same)
- Apple chose the feel first (one-hand lid, unibody) and then solved the hard engineering it forced. Decide the experience, then the build. (same)
