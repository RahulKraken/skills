---
name: test-as-a-user
description: Use before saying any feature, fix or change is done, and whenever asked to test, check or verify something works. Make sure to use this even when unit tests pass, and whenever about to write "done", "works", "ready" or "fixed" about user-facing behaviour.
---

# Test as a user

## Context

Rahul's definition of done: it works when a real person uses it, in every state, and nothing that used to work broke. Passing tests are not that. Across Pillar and Meusic, Rahul repeatedly caught work called done that had never been run: "Are you not running this in the simulator?", "I thought you were going to test by hand for at least five of these people", "regression happening over and over again with every new build". Each of those cost a round of trust.

## What to do

1. **Run the real thing.** The simulator, the browser, the CLI, the actual endpoint. Not a mock, and not only the test suite.
2. **Use realistic, messy input**, the way people actually type or behave: typos, extra spaces, other units, an empty field, a very long value, the same action twice. Rahul's users type "did 3x5 squats 100kg", not a schema.
3. **Walk it as personas.** At least these, adapted to the product:
   - a first-time user who arrived from an ad and is skeptical,
   - someone a few days in,
   - a long-time user with lots of data.
   For flows that unfold over time, walk a day and a week in their life.
4. **Check every state**: empty, loading, error, first use, edge values, and what happens on refresh or relaunch.
5. **Check for regressions**: re-run the paths that worked before your change.
6. **Fix what you find, then walk it again.**
7. **Wrong data saved silently is worse than an error.** When input can't be understood with confidence, fail clearly or ask; never store a guess as fact (a parser that saves "squats felt good" as the exercise name is broken, even though nothing crashed).

## How to report

Lead with what you tried and what happened, in a few lines: the inputs and personas, what broke, what you fixed, and every known gap that's still there. Keep it short; a list of inputs beats paragraphs. Attach screenshots or output as proof. If you couldn't run something (no device, no credentials), say so plainly; never imply it was tested.

## Keep the Mac light

One simulator or browser at a time, no sound, and stop servers and simulators when you're done. Rahul is usually using the same machine.

## Where this bends

- For a library or backend function, "the user" is its caller: exercise it through the real entry point with realistic calls, not only unit tests.
- If Rahul says "rough first, polish later", test that the core path works end to end and say what you skipped.
