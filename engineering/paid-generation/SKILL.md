---
name: paid-generation
description: Use before any run that costs money or significant compute, such as image, video, 3D or audio generation (fal, Rodin, Hunyuan and similar), LLM batch jobs (Gemini, Claude, OpenAI), GPU or Kaggle jobs, fine-tuning or large evals. Make sure to use this whenever a task would call a paid API more than once or start a long-running job.
---

# Paid generation

## Context

Rahul is careful with money and generous with quality. Both show up again and again: "You can spend up to $5, but please don't be wasteful. plan ahead… don't generate and be like oops bad idea", and in the same breath, "go for quality in one shot instead of doing the shitty work over and over again". The worst session in the transcripts ended with Gemini credits gone and an unrequested training job running: "This has been a disaster." Wrong settings on a Kaggle run got "wasting compute over silly mistakes".

## Before spending

1. **Show the inputs.** The reference images, prompts or data you'll use. "first you show me which logos you are using for inspirations before you generate anything". Generating from the wrong reference was a repeated, costly mistake.
2. **Quote exactly what you'll run and what it costs**: model, count, settings, price per unit, total. A realistic number, no padding ("How can your range be from 15 to 3x of that?… Don't add useless buffers").
3. **Wait for a go**, unless Rahul already gave a budget for exactly this. "don't run fal without asking going forward".

## While spending

- **One sample first, show it, then the batch.** "generate one and show me first".
- **Small smoke test before a big job**, with the real settings, to catch config mistakes cheaply.
- **Pick the model worth the money.** When Rahul pays, they want the best tool for the result, run once at top settings, not cheap reruns. "if I'm gonna pay money I want the best tool".
- **Never chain unrequested jobs.** Do the agreed run, report, stop. Especially when Rahul is away.
- **Stop and report** if results look wrong or spend approaches the budget.

## After spending

- **Keep the full-quality originals**; compress only copies. "keep the highest-quality stuff that we are getting for our money".
- **Don't destructively post-process** a good result.
- Report what was spent and what you got, in a line or two.

Your message before spending should be short: the references, the exact run and cost, and one clear ask. No side notes or menus of variants.

## Where this bends

Work that is processed once and used for a long time (a song analysed once, learned for months) justifies spending more: "we need to throw best quality at it". The rule is not "spend less", it's "never waste".
