---
name: model-routing
description: Use whenever you delegate work to a subagent or a headless Claude run — pick the model tier for each piece of work from the task itself, and escalate when work fails.
---

# Model routing

You are the master session. You plan, make judgment calls, and make the final edits. For every piece of work you delegate, choose the model at spawn time from the task. There is no default subagent model; decide every time.

## Step 1: Classify the task

Ask two questions:
1. **How hard is it?** Mechanical → scoped → complex → frontier.
2. **How cheap is a wrong answer to catch?** If you or a test will instantly see an error, go smaller.

| Tier | Model | Give it | Examples |
|---|---|---|---|
| Mechanical | `haiku` | Checkable output, no judgment | find files, grep, read logs, run tests, summarize output, classify/tag/extract |
| Scoped | `sonnet` | Clear spec, bounded blast radius | bug fix with a repro, feature against a spec, repeated review/drafting |
| Complex | `opus` | Ambiguity, multi-file reasoning | multi-PR feature, tricky debugging, perf work, computer use |
| Frontier | `fable` | Hardest, longest, most open-ended | major migration/refactor, architecture, deep research, quant analysis, long unattended runs |

Tie-breakers:
- A clear spec doesn't make a task easy. A migration with a perfect spec can still be Complex or Frontier.
- Never give a cheap model a decision that, if wrong, sends you down the wrong path.
- Frontier costs 2× Complex per token. It needs a reason: either a lower tier already failed, or the task is clearly frontier-class from the start.

## Step 2: Spawn

- **Subagent** (default): pass `model` explicitly on every spawn. Use this for anything that should report back into this session.
- **Headless run**: use this for a large self-contained job that would bloat this context.
  ```bash
  claude -p --model <tier> --permission-mode acceptEdits \
    --allowedTools "<only what it needs>" \
    --output-format json "$(cat plan.md)"
  ```
  Tell the user before launching. It's a separate billed run.

Every handoff gets a short written plan: the goal, constraints, relevant files, done-criteria, and how to verify. The new model starts cold, with no cache and none of your reasoning. Never pass the full history.

## Step 3: When delegated work fails

Stop at the first fix that works:
1. Give it a way to verify itself: a test, a build, or a script.
2. Re-spawn on the same tier with a sharper plan, including what went wrong.
3. Move up one tier.

If verification is automatic and there are many items, run them all on the lowest plausible tier and re-run only the failures one tier up.

## Keep your own context lean

Your context is the most expensive context. Push verbose reading (logs, large files, search sweeps) to smaller tiers and take back only summaries.

## Security work

Cybersecurity content can be flagged and silently fall back to an older model. If quality drops on a security task, check for a fallback notice before escalating.
