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
| `ai-ui-quality-review` | product-design | draft v0.2 |
