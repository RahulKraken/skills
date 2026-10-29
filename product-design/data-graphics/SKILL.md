---
name: data-graphics
description: Use before drawing, designing or critiquing any graphic that shows data, progress or status inside a product, such as a widget, chart, stat, progress indicator, streak, weekly view, timeline, goal tracker or level meter. Make sure to use this whenever a screen needs to show numbers, trends or progress visually, even if nobody says "chart", and especially before reaching for a bar chart, ring, progress bar or calendar strip.
---

# Data graphics

## Context

Rahul builds calm consumer products: a health coach, a guitar teacher, a memory layer. In these products, a data graphic is the one place where the product can make progress felt instead of just reporting it. The text next to it already states the number, so the graphic has to earn its place by doing something the text can't.

Left alone, Claude picks the most common chart for the shape of the data: bars for counts, a ring or bar for progress, a row of days for a week. These charts are correct and familiar, and that is the problem. Every app has them, so they make this product look like every app. On Pillar, about ten default metaphors were rejected in a row. Rahul's words: "I hate bar charts… it's boring, it's low effort, it's lazy", and a progress line was "the most uncreative way I have seen of showing progress".

## Work in two phases

1. **Design** the graphic at full richness, and check it renders.
2. **Text pass:** edit only the words, following `references/text-pass.md`.

Keep them apart. In testing, trying to cut and polish text while designing made the graphics thinner every time, and design scores dropped as text scores rose. Designing first and editing words second lets each get full attention. During phase 1, draft the words quickly and don't polish them; phase 2 will fix them.

# Phase 1: Design

## Before drawing: three questions

1. **What does this graphic tell the user that the text doesn't?** If the answer is nothing, don't draw it. A good sentence beats a decorative chart. ("it must show something which isn't already mentioned in the text")
2. **What does it prompt the user to do next?** A graphic that only shows status is a dashboard. One that shows where you're heading and what's next is a coach. (Rahul picked a widget "because it also gives you an action: what is coming next".)
3. **Does it add a delight that text can't?** ("does the widget add an element of delight which text won't?")

If the honest answer to all three is no, use text. These are the tests Rahul has applied themselves, so asking them first saves rounds of rejection.

## Look at real references before drawing

Before writing any code, look at how the best products show this kind of data. Use the references Rahul trusts where they fit: Gentler Streak, Apple Fitness and Health, Strava, Flighty and GarageBand. Search for others where they don't: Mobbin, Dribbble, award-winning apps. For each reference you use, note to yourself (not in the mockup) the principle you're taking from it in one line, such as "Gentler shows effort as a soft band you stay inside, not a bar to fill".

The reason: without references, Claude draws from memory, and memory gives the average. Rahul's pattern is research first, and they push back when a design shows no trace of it ("What did you learn from GarageBand? I don't see anything here"). Take principles, not looks: "I'm not saying copy it, but principles."

## Finding the form

- **Answer the request's main question in the graphic itself.** If the user asked "target vs actual", the gap between them must be visible at a glance in the shape, not only in a number. A beautiful metaphor that hides the answer has failed.
- **Start from the product's own world, not from the chart catalogue.** Ask what object or motion this domain already has. Pillar's day is time passing, so a time map with a fixed needle and a moving map worked. Meusic is sound, so waveforms and level meters feel native. A form taken from the domain is specific to the product. A form taken from the catalogue is generic.
- **Encode with colour and position before size.** "color does a better job, imagine traffic info on google maps rather than thickness". Lengths and areas are what make a graphic read as a stock chart.
- **Keep it rich.** Removing data is rarely the fix for a dull graphic: "all your options are less rich than what we have today". Put the facts in the graphic as markers, milestones, axes and states, and reveal detail on tap so the surface stays calm.
- **Use one idea per graphic, drawn simply and flat.** Over-built mechanics, such as sliding strips, rolling numbers or a needle on a one-line widget, were rejected as "overcomplicated". Use flat colour. Avoid gradients unless they are executed at top quality.
- **Keep the energy positive.** Show what's there and what's next, not what was missed. ("missed 4 runs… negative energy. we want positive energy")
- **Motion should carry meaning.** Good motion grows an object into its detail view, or draws a line as time passes. Don't animate a graphic to make up for it having nothing to say.
- **Finish matters as much as the idea.** A good concept drawn as thin lines, dots and tiny labels still reads as a developer's diagram, and Rahul has called code-drawn art "trash". Give the graphic real visual weight: a clear type hierarchy, labels no smaller than 11pt on a phone, generous spacing, soft shapes, colour with intent, a finished device frame and real-looking surroundings rather than grey placeholder cards. Hold it to the polish of the references you looked at.

## Where this bends

- **Precision tools** (a profiler, a debugging or cost view): readability comes first, and a familiar form is fine if it is the clearest one. It still has to be intuitive at a glance, and it should hint at why, not only which. A dense trace waterfall was rejected as "too hard to make any sense out of".
- **Familiar forms that signal instantly.** In Meusic, GarageBand-style level bars were right because they say "I'm listening" with no learning. The test is whether the familiar form is the fastest way to the meaning, not whether it was the default.
- **An explicit ask.** If Rahul asks for a specific standard chart, make it, and make it well.
- **References are for principles, not copying.** Gentler Streak sets the bar for craft, not a look to clone.

## How to present

Build 2 or 3 genuinely different directions as viewable samples (HTML is fine). Put each one in its screen context, and include its empty state. Rahul judges visuals by seeing them, so a written description of a graphic isn't something they can review. Don't end with a menu of lettered options.

**Only show directions you'd defend.** If you would tell Rahul to drop a direction, don't make it. Two strong directions beat three where one is filler, because a weak option wastes a review and drags down trust in the strong ones.

## Check the design renders

Render every mockup and look at the result yourself. Use the browser pane if you have one, or take a headless screenshot:

`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --window-size=1280,2400 --screenshot=out.png file.html`

Then read the image, crop each graphic at its real size, and check:
- **The glance test.** At real size, can you answer the request's main question in two seconds (such as "am I hitting my targets?" or "which session cost the most?")? If not, make that answer the biggest thing on the graphic.
- Every direction and every state actually renders: icons, fonts and data, in every state. Nothing is blank, overlapping, clipped or stuck mid-animation.
- It looks finished next to the references, not like a diagram.

Fix what you find and look again. Code that parses is not the same as a graphic that works, and a broken mockup costs more trust than a missing one. Rahul's rule is "Don't do half work". Keep the final screenshot: phase 2 compares against it.

# Phase 2: Text pass

When the design is done and renders, edit the words as a separate pass. Read `references/text-pass.md` and follow it. Its one rule is to change text and never the design.

If you can start a subagent, hand it the mockup path, the final screenshot and `references/text-pass.md`, and let it do the pass with fresh eyes. Otherwise do it yourself, after the design is finished. Write your message to Rahul after the text pass, under its rules: about 60 words, your pick and the user-facing reason.

## Examples from Rahul's projects

Rejected, and why:
- A row of 7 circles for a week of habits: "extremely boring and generic". Every habit app has it.
- A progress line or bar for a goal: "the most uncreative way I have seen of showing progress".
- A calendar strip for today's sessions: "again one of the most uncreative ways".
- Bar charts anywhere in the app: "boring, low effort, lazy".
- A dot and a flag on a curve: "what is it communicating? Nothing really".

Loved:
- The time map with a fixed needle while the map moves: "I really like the time map with the needle".
- The "swigly lines" for today: "much more creative".
- A Strava-style route line on a plain background, with no map tiles under it.
- Level bars that move with the sound, to show the app is listening (the familiar form that was right).
