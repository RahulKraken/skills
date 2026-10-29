---
name: lean-refactor
description: Use when asked to clean up, refactor, simplify, slim down or "cleanse" code, or when a module feels bloated, over-engineered or hard to follow. Make sure to use this before deleting or restructuring code in any of Rahul's projects, even for a small "tidy this up".
---

# Lean refactor

## Context

Rahul's Pillar backend grew to tens of thousands of lines ("What have you written in those 19k lines in brain and 15k lines in facts mate?"). The cleanse rule that came out of it: "anything not required should go, any ambiguity or complexity not required should go, things should be lean, performant… eliminate issues without reducing capability than optimising something that shouldn't exist in the first place." When Claude proposed cuts that removed features, the answer was: "features we don't want to remove right. that's the point, without reducing capabilities can we clean it up. that forces us to find the right way of doing things."

## Rules

1. **Delete before you optimise.** First ask what shouldn't exist at all. Optimising dead or redundant code is wasted work.
2. **Never lose a capability.** List what the code can do before you start. Every item must still work after. If a capability seems unneeded, ask; don't silently drop it.
3. **Decide what goes before adding anything.** "before adding anything new, we need to decide what is going to be removed".
4. **An agent only where there's a loop.** "if something isn't running in loops calling multiple tools etc, it can be a simple model call… or provide to the agent as a tool". Collapse fake agents into plain calls.
5. **One source of truth.** Facts live in one place; everything else reads from it.
6. **No fabricated content in code.** The server drives messages; hard-coded user-facing text pretending to come from the model is out.
7. **Learned over hand-tuned.** Prefer a model or a principled method over piles of thresholds and special cases.
8. **Keep seams, not layers.** Vendors behind a thin abstraction; no microservices unless they clearly add value.
9. **Don't break callers silently.** If you move or rename something other code may import, update every caller in the repo, and say clearly in your report that the import paths changed.

## Procedure

1. Write the capability list and a short "will remove" list with one-line reasons. For a large change, share it before editing.
2. Make the changes.
3. Prove nothing was lost: run the tests, and exercise each capability through its real entry point.
4. Report in a few lines: lines before and after, what was removed and why, and confirmation that every capability still works.

## Where this bends

Performance work on a proven hot path is fine, after the deletions. Don't refactor code Rahul didn't ask about in the same change; note it instead.
