# Text pass

This is phase 2 of the data-graphics skill. The design is finished and renders. Your job now is the words, and only the words.

## The one rule of this pass

**Change text, never the design.** Don't remove, resize, restyle or move any visual element: shapes, markers, axes, layers, colours, states. In testing, every attempt to fix the text while designing made the graphic thinner. This pass exists so that can't happen. If cutting a line would lose a fact the user needs and the graphic doesn't already show it, rewrite the line instead of cutting it.

## Why it matters

Rahul's most repeated complaint across every project is text: too much of it, and not good enough. "any text which doesn't need to exist shouldn't exist", and "text is going to be read and it carries concrete meaning so use text when absolutely necessary and it must make clear sense". Claude's default is to label, caption, add a legend and explain itself, because text feels safe. In a graphic, every extra word competes with the shape that should carry the meaning.

**A line earns its place only if it gives the user an insight, a milestone, the next thing to do, or a number they need**, in words they would use. Everything else goes.

## Procedure

1. List every line the user will see:
   `python3 <skill folder>/scripts/visible_text.py mockup.html`
2. Go through the list one line at a time. Mark each line **keep**, **rewrite** or **cut**, checking it against the five patterns below. Write the list down (for example in `text-audit.md`) so nothing is skipped.
3. Edit only the text nodes in the HTML, then run the script again. Repeat until every remaining line is a keep.
4. Re-render and compare against the screenshot from before the pass. The graphic should look the same apart from the words. If anything visual changed, put it back.
5. Write the message to Rahul last, under the same rules.

## The budget

- **Inside the graphic:** one headline at most, plus short labels that name facts on the graphic itself. A two-word label on a marker ("First 10k") is information, not clutter. Leave out eyebrow labels ("SLEEP · LAST 7 NIGHTS"), legends that colour can teach on first use, captions, status chips that repeat the headline, usage hints ("Tap a week for its numbers") and coaching paragraphs.
- **Empty state:** one short, warm line at most.
- **On the mockup page:** each direction's name and nothing else. No tagline under the name, intro paragraph, reference cards, bullet lists or explanation boxes.
- **In the message:** about 60 words. Your pick and the user-facing reason in one line, plus one line for each other direction.

## The five ways text goes wrong

These are real lines from earlier test runs that Rahul judged low quality, each with its fix. Check for each pattern by name.

1. **Describing the design.** Taglines that explain how the graphic works, or sound nice and say nothing.
   "Your whole plan, and where you stand in it" → cut. "Follow your week back into your sleep zone" → cut. "Biggest share, biggest tile" → cut. A direction name like "The climb" is fine on the mockup page, but not inside the product.
2. **A label instead of a sentence.** It names a box instead of telling the user something.
   "This week" → cut. "Before the first run" → cut. "12-week plan" → cut. "7½h and up" → cut, and let colour teach it. "21 km week" (actual or target?) → "21 of 22 km · 1 to go".
3. **Machine numbers.** Precision a person wouldn't say.
   "Friday · Easy 3.3 km" → "Friday · easy 3 km". "Tempo 5.0 km" → "5 km tempo". "Cached 84,843,384" → "85M cached". "21.0 / 20 km" → "21 km · 1 over". "Bed by 10:55" → "Asleep by 11".
4. **The insight is in the wrong place.** The best line ends up in the message to Rahul, not on the screen for the user.
   "5 of 7 nights hit 7½h" (a scoreboard) → "Both short nights started after midnight" (why it happened). "Half of it came from 5 of your 41 sessions" → "Half your spend came from 5 sessions".
5. **Message filler.** Justifying, explaining the mechanism, housekeeping.
   "It's a profiler, so reading the screen fast matters more than a new look" → cut. "Weekly km in back, long runs in front, and a needle on week 5" → cut, the mockup shows it. "The sleep data is invented" → cut.

Also: warm and forward, never a verdict ("Your week starts tonight", not "No sleep yet"; "short", not "missed"), and specific rather than stock ("2 km ahead of plan", not an "On track" chip).

Good lines from earlier runs, for the tone: "2 km ahead of plan". "Sunday · 8 km, your longest run yet". "Asleep by 11 tonight". "Your week starts tonight". "Half your spend came from 5 sessions".
