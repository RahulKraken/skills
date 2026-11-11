# skills

Things I learn, converted into Claude skills. Notes tell me something; a skill changes what Claude does.

## Rules

1. A skill must change an output. If I can't say "Claude does X differently because of this", it stays in `_inbox/`.
2. Organize by when Claude should trigger, not by topic. The `description` is the trigger, so write it carefully.
3. Keep skills narrow. Many sharply described skills beat a few broad ones.
4. Forks start in `_upstream/` with source, license, and a note on what I changed and why. Mature ones graduate into a domain folder.
5. Test before keeping: same prompt with and without the skill, keep it only if the output improves.
6. Nothing confidential from work goes in here.

## Layout

```
_inbox/           raw daily learnings, promoted weekly or dropped
_upstream/        other people's skills I forked from
global/           CLAUDE.md, my always-on rules (symlinked to ~/.claude/CLAUDE.md)
product/          <skill-name>/SKILL.md
product-design/   <skill-name>/SKILL.md
engineering/
architecture/
hardware/
market-research/
sales/
marketing/
```

Domain folders are created when the first skill needs them.

## Workflow

Capture in `_inbox/` daily. Once a week, promote what passes rule 1 into a skill and delete the rest.

## Use

Claude Code reads user-level skills from `~/.claude/skills/`. Symlink the skill folders you want:

```
ln -s "$PWD/product-design/ai-ui-quality-review" ~/.claude/skills/ai-ui-quality-review
```

## Skills

| Skill | Domain | Status |
| --- | --- | --- |
| `product-thinking` | product | draft v0.2, untested |
| `product-review` | product | draft v0.1, untested |
| `ai-ui-quality-review` | product-design | draft v0.2 |
| `data-graphics` | product-design | v6, tested |
| `ui-copy` | product-design | v1, tested |
| `screen-polish` | product-design | v1, tested |
| `design-feeling` | product-design | v0.2, tested (2 rounds) |
| `design-system` | product-design | v0.3, tested (3 rounds) |
| `review-screen` | product-design | v0.1, used in every round |
| `landing-page` | marketing | v1, tested |
| `landing-page-build` | marketing | v1, tested (fork of elayadesign) |
| `test-as-a-user` | engineering | v1, tested |
| `paid-generation` | engineering | v1, tested |
| `model-routing` | engineering | draft v0.1, untested |
| `mcp-design` | engineering | v1, tested |
| `idle-cost-infra` | architecture | v1, tested |
| `lean-refactor` | architecture | v1, tested |
| `stageshow` | _upstream (Benji Taylor, MIT) | A/B round 1 lost 0/2 (weak test, see evals/RESULTS.md) |

"Tested" means one blind A/B round: the same prompt with and without the skill, judged without knowing which was which. Test cases live in each skill's `evals/`.

## Design workflow

The design skills chain. Each one says when to hand over to the next.

1. `design-system`: a new product starts here. From a brief (what it is, how it should feel, what it must never feel like) it makes three directions, then writes the picked one as `DESIGN.md`, tokens in code and a gallery library. It also extracts a system from an existing product and extends it as screens are built.
2. `design-feeling`: each screen or flow, inside that system. Feeling words, the peak moment, motion, colour.
3. `screen-polish` and `ui-copy`: layout, states and words.
4. `review-screen`: before any UI is called done. Records the flow, checks the frame sheet and blank frames, and checks against `DESIGN.md`.

Test results are in each skill's `evals/RESULTS.md`.

