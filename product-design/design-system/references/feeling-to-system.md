# From a feeling to a system

A feeling only becomes consistent when each layer of the system expresses it. For each layer, decide from the brief, then write one line on **why this choice makes it feel like the brief**. If you can't write that line, the choice is a default: change it.

Read the brief's "must never feel" list as hard limits. Most generic results come from defaults that break one of them.

## Banned defaults

These are what models reach for when a brief says "warm", "calm" or "premium". They make every product look like every other AI-made product. Do not use them unless Rahul names one:

- Cream, linen, parchment or "warm paper" backgrounds with a terracotta, clay, ember or rust accent.
- A serif for "the coach", "the voice" or headlines to make it feel human or editorial.
- Near-black with one acid green, lime or vermilion accent.
- Purple-to-blue gradients; sunset gradient blobs; a "wellness wave".
- Inter, Space Grotesk or a random Google font as the main face of a native app.
- Data drawn as an abstract blob, wave or ribbon that looks nice but does not read.

**Warmth does not come from a cream background.** It comes from words, motion, photography, the accent and how the product treats the person. A white, native app (Apple Fitness, Things, Airbnb) can feel very warm.

## Colour

- **Base:** the page and surfaces carry most of the mood. Pure system white or system grouped grey reads native and confident; a tinted base is a strong statement and needs a reason beyond "warm"; true black reads dramatic. Light or dark is a choice per product.
- **Ink:** the platform's label colours on native apps; otherwise a dark that shares the base's temperature.
- **Ramps:** each colour gets a full ramp (for example 50 to 900) so tints, fills, text-on-tint and dark-mode values come from one source, like a real Figma library.
- **Accent:** one or two, chosen from the product's world and meaning. Decide what earns an accent (an action, a domain, a moment) and what never does.
- **Semantic colours:** domains or categories get colours that read as a family (same lightness and saturation), never a rainbow. Status colours are separate and rare.
- **Check:** squint at a screen. Does the colour alone say the feeling words? Does any colour break a "never" (alarm red for a bad day breaks "no guilt")?

## Type

- **Native first.** On iOS the main face is SF Pro, set with Apple's text styles (Large Title, Title 1–3, Headline, Body, Callout, Subheadline, Footnote, Caption 1–2) at their default sizes and weights, scaling with Dynamic Type. SF Pro has optical sizes and size-specific tracking: in the app the system applies them; in a web mock use `-apple-system` and the matching letter-spacing, never a substitute font as the design.
- **Personality comes from use, not from a new font:** weight contrast (a heavy number next to regular text), SF Pro Rounded for numbers, SF Pro Expanded or Condensed for one display role, tight line lengths, and generous space around the one big line. A second family needs a reason a person would notice.
- **Scale:** few sizes with big jumps. Numbers are a role of their own (tabular, often rounded or heavy).
- **Check:** at real size on a phone, is the hierarchy obvious in one second, and does nothing look like a template?
- **Render with the real fonts.** A mock judged in a fallback font (Inter, Charter, DejaVu) is not judged. If the machine lacks SF Pro, say so, and have Rahul view the published page on his iPhone or Mac.

## Shape language

- Radius is personality: tight radii feel precise and serious; large continuous radii feel soft and friendly; capsules feel tappable. Choose one family and nest radii consistently (inner = outer minus padding).
- Decide what has a container at all. Fewer boxes feel calmer.

## Space and density

- Calm and light come mostly from space: generous edges, one idea per screen, detail on tap.
- Decide the spacing scale and the edge once. Dense products (tools) take a tighter scale on purpose.

## Depth and material

- Decide where depth exists: glass for chrome (iOS 26), flat surfaces for content, shadows only for things that float. Texture, grain and light only where they serve the concept.

## Motion personality

The same named motions feel different with different physics. Set the personality, then name the motions.

| Feeling | Physics |
|---|---|
| Calm | No overshoot (bounce 0), a little longer (0.4–0.5 s), one thing leads |
| Light | Short travel, quick response (0.25–0.35 s), opacity with small moves, soft blur |
| Warm, friendly | A small bounce (0.1–0.2) on things that land, never on things that leave |
| Alive | Things carry into the next state; a slow ambient breath on one element at most |
| Premium | Restraint: interruptible springs, no gratuitous loops, perfect settle |

Then define: press, appear, leave, move, sheet, push or page, the hand-over between screens, and the one or two signature moments. A screen names a motion; it never writes a curve.

## Haptics and sound

Small vocabulary, mapped to meaning: a tick for choices, a tap when something lands, success when a thing the person asked for is done, one rare "moment" for the peaks. Silence by default.

## Icons, illustration and imagery

- Icons: one set, one weight, monochrome by default.
- Illustration: decide whether the product has any. "Premium and real" usually means none on everyday screens and a few crafted ones in the peaks. Graphics must earn their place; a decorative graphic that reads as a design experiment breaks "shipped app".
- Imagery: the person's own photos and data are often the best imagery.

## Voice

Write five sample lines (a greeting, a good day, a bad day, an error, an empty state) in the brief's voice. The type and colour must suit these lines.

## Directions

Make three directions that are **different answers to the same brief**, not three palettes of one idea. **Each one must satisfy every feeling word and every "never".** A direction that breaks the brief (a dashboard when the brief says "never a dashboard", an experiment when it says "shipped app") is a straw man: it makes the pick easy and teaches nothing. Vary what the brief leaves open instead: which feeling leads, light or dark, the concept, the type voice, how much colour, how much motion. **The three must start from different bases**: one native (system white or grouped grey), one dark, one led by a bold brand colour. If two directions share a base and accent family, replace one. For example, for a calm, warm, capable health coach: calm-led and almost native; warm-led with an editorial coach voice; capable-led with a bolder accent and quicker motion, still calm. Each direction is a full mini-system (base, ink, accents, type, radius, motion physics) shown on the same key screen, in motion, side by side. Name each direction with its trade-off.
