# What a complete design system contains

A team's Figma library has hundreds of items. A system with ten components and a palette is a style sheet, not a system: every new screen will invent the rest. Build the library below. For mobile, follow the platform's own component set first (Apple's iOS UI Kit) and style it; only add custom components the product needs.

The gallery (`gallery.html`) is the library: one page per group, every item shown in every variant and state, light and dark, with its token names. An item that is not in the gallery does not exist.

## 1. Foundations

| Item | What to show |
|---|---|
| Colour ramps | Every hue as a ramp (50–900), light and dark |
| Semantic colours | Backgrounds (primary, secondary, grouped), labels (primary to quaternary), fills, separators, tint, the domain family, status (success, warning, error, info), each with its ramp source |
| Accessibility pairs | Every text-on-colour pair with its contrast ratio |
| Type | Every text style in regular and emphasised, with size, leading, tracking and the Dynamic Type range (xSmall to AX5) |
| Numbers | Big numbers, units, tabular figures, durations and dates in the product's format |
| Layout | Screen margins, safe areas, the grid for each device class (small phone, large phone, iPad if any), list insets |
| Spacing | The scale with examples of use |
| Shape | Radii (continuous), nesting rule, capsules, borders and hairlines |
| Elevation and material | Levels, shadows, glass (Liquid Glass) and blur, scrims |
| Iconography | The icon set (SF Symbols names), sizes, weights, rendering modes, custom glyphs, filled vs outline rule |
| Illustration and imagery | Whether any exists, the style, where it may appear, photo treatment, empty-state art |
| Brand | Wordmark, app icon (light, dark, tinted, clear), splash, the one brand colour |
| Motion | Each named motion playing, its curve and spring values, its Reduce Motion form |
| Haptics and sound | The vocabulary with when each plays |
| Voice | Sample lines for greeting, success, error, empty, permission, notification |

## 2. Components (iOS baseline)

Each with: anatomy, variants, sizes, states (default, pressed, focused, disabled, loading, error, selected), dark mode, Dynamic Type at AX sizes, VoiceOver label, do and don't.

- **Actions:** button (filled, tinted, gray, plain, destructive; small, medium, large), icon button, glass button, link, menu, context menu, share
- **Navigation:** navigation bar (large and inline title), tab bar, toolbar, search bar, segmented control, page control, back and close
- **Inputs:** text field, text area, composer (text, voice, photo), toggle, slider, stepper, picker, date picker, checkbox and radio (if any), chips
- **Containers:** list (plain, inset grouped), cell variants (title, subtitle, value, accessory, swipe actions), card, sheet (detents), popover, full-screen cover
- **Feedback:** alert, action sheet, toast or banner, progress (bar, ring, indeterminate), skeleton, activity indicator, empty state, error state, offline state
- **Content:** avatar, badge, tag, divider, image and photo frame, video, map snippet, chart primitives (the product's own data shapes)
- **System surfaces:** notification, Live Activity, widget (small, medium, large), Lock Screen widget, share card, App Clip or permission prompts

## 3. Product components

The components only this product has (for a coach: a coach message, a reply card, a meal card, a plan card, a week view, a goal view). Each gets the same documentation as the baseline.

## 4. Patterns

Flows made of components: onboarding, sign-in, permissions, first run, empty, loading, error and retry, offline, editing and undo, deleting, search, settings, notifications, sharing, paywall if any.

## 5. Signature

This is where the magic is. A complete but plain library is still forgettable. Define, design and show:

- **The signature moment:** the one interaction people remember and describe to a friend. Storyboard it frame by frame, then build it.
- **The signature component:** one component no competitor has, that carries the concept (it must still read at a glance, not decorate).
- **The signature motion:** the physics people feel in every screen (how things arrive, settle, respond), named and tuned.
- **The signature detail:** small delights that reward attention: a number that counts with a haptic tick, a sound on the one big moment, an icon that animates once, copy that notices something.
- **Brand presence:** how the brand shows on a plain screen without decoration (the accent, the motion, the voice).

Show the signature items first in the gallery, playing.
