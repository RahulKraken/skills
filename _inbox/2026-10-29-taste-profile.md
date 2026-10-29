# Taste profile, mined from Claude Code transcripts

**Source.** About 1,250 messages I typed in Claude Code between 27 Sep and 28 Oct 2026, plus one from May. They cover six projects: Pillar (iOS AI coach), Meusic (guitar learning), Encognition (AI memory layer and its waitlist site), my portfolio site, Aftertrace (open-source profiler) and Apex One (hardware explainer). Only my own words count as evidence. Claude's replies, pasted material and auto-summaries were used as context only. The counts are approximate.

**Project tags:** P = Pillar, M = Meusic, E = Encognition, Pf = portfolio, A = Aftertrace, X = Apex One.

**How to read this.** These are patterns, not laws. I have said I want "learnings along the way", not "unbreakable rules", and that inferred "unsaid" learnings feel wrong. Every line below comes from things I said, but I still need to review it before any of it becomes a skill. Dislikes are strict: an item goes there only if I said it clearly or more than once. Anything situational goes under "Depends".

---

## Meta-principles (across domains)

1. **Feeling decides when it is done. "It works" is only the starting line.** I judge by eye, ear and hands on the real thing, not by metrics or a spec.
   "in all the moments I feel nothing" (P) · "anything less than magical isn't good enough" (M) · "judge a website by how it makes someone feel" (E) · "that's not an amazing f1 score, show me these audio clips" (M) · "finally a website I'm kinda proud of" (Pf)
2. **Generic is the worst failure.** There were 40+ rejections across every project, worded as "AI slop", "generic", "childish", "cartoonish", "bland" and "uncreative". Bland fails, and over-decorated fails too. The target is "clean but playful and characterful" or "modern minimalism with some fun".
3. **Every element earns its place, but calm does not mean fewer features.** Remove what says nothing and keep capability and richness. Delete before optimising.
   "it's not about reducing functionality, it's about calm and clean" (P) · "all your options are less rich than what we have today" (P) · "without reducing capabilities can we clean it up" (P) · "eliminate… rather than optimising something that shouldn't exist" (P)
4. **The product does the hard work, not the user.** That means no questions, no manual fixing, no setup steps, and pulling data from connected sources first.
   "it's the job of the product to get it right" (M) · "again no questions asked please" (M) · "writing email here is friction" (M)
5. **Learn from the best and never copy.** Research real references first, study one in depth, and look outside the category.
   "I'm not saying copy it, but principles" (P) · "you've copied gentler streak quite hard… keep it pillar" (P) · "don't look at music apps… open your horizons" (M)
6. **See it, then decide. Agree, then build.** The flow is: discuss, then visual samples on a canvas, then pick, then build, then test on the device. I can't judge visuals from prose. Building before we agree is just as bad.
   "show me, make it and show me" (E) · "why are you running something which we haven't brainstormed yet?" (M)
7. **Spend generously where it compounds. Never waste through carelessness.**
   "throw best quality at it" (the song is processed once) (M) · "quality in one shot" (Pf) · "I don't want to be paying when nothing is being used" (P) · "don't add useless buffers" (M)
8. **Pick the simplest thing that works at the current scale, and leave seams for later.** Microservices only when they add real value. Postgres with jsonb. Vendors behind an abstraction. Swappable models. One model call unless the task needs a tool loop.
9. **Ground truth beats guesses.** Use official docs, my real data (my Health export, my own recording), the real logos and the real device.
   "did you check apple documentation… or it's a guess?" (P)
10. **Delegate broadly and verify personally. I own anything outward-facing, irreversible or billed.**
    "go with your best judgement", "ping me when done" (all) · "don't touch any outside service… capture those steps for me" (E, P)
11. **Start clean rather than patch weak foundations.** I scrapped the vibe-coded app, deleted old branches and resources, and ignored the v1 plans. "Clean things, new things" (P).
12. **Keep the tone positive and free of guilt.** No streaks and no "missed" framing. Empty states should encourage. "we're ironing out the rough edges" instead of "invite only" (M, E).

---

## Product design and UI

**Likes**
- Calm, clean surfaces that still carry a lot of capability, like the Claude, ChatGPT and Cursor apps. (P)
- One screen with one dominant object, using the full screen. "one huge guitar and everything happening over there" (M)
- Controls in a top or bottom bar, never over the content. Put actions near the thumb. GarageBand is the reference. (M, P)
- Icons instead of words for controls. Use text only for teaching and feedback. (M, P)
- The fewest taps for the most frequent action. Quick capture and then go, with no celebrations getting in the way. (P)
- Random access over flows that advance on their own. The learner controls the pace. (M)
- Progressive disclosure: details appear on tap, but a screen is never empty. (P)
- Main actions are visible and easy to find. Secondary and destructive actions stay quiet (icons, long-press). Tapping something shows details, not the risky action. (P, M)
- Every state is designed: empty, loading, error and dark mode. "nothing states… are the spots to add premiumness" (P)
- Every interaction gets feedback: level meters, waveforms, and motion on fields and buttons. (M, E)
- Native platform behaviour (Liquid Glass, Apple guidance), checked against research. (P)
- One pattern everywhere, one image treatment, one shared product flow. (P, M, Pf)
- The user can override the system's opinion, and the app shows what the change will do. (P)
- Navigation you can always back out of. A refresh lands at the top. (Pf, E)

**Dislikes**
- Clutter, too many shapes and busy layouts (10+ times).
- A dashboard feel in a consumer or chat product.
- Redundant labels: the app name in the header, "Next:", "Why:", "(optional)", a scroll indicator, status badges.
- Elements whose purpose isn't clear at a glance. "they are confusing me more than explaining" (M)
- Settings toggles and extra modes. "not toggles, all these need to be smart ux" (P) · "why are you complicating it" (M)
- Hiding things in menus. "putting things inside menus i hate it" (M)
- Elements that vanish and come back, and popups with no transition.
- Separate screens that break the shared flow. "no separate flows" (M)
- A "redesign" that only rearranges things. Also the opposite: restyling when I only asked for a reorganisation.

## Visual and motion

**Likes**
- Character and "wow" on a calm base. "you go wow but at the same time your anxiety levels drop" (Pf). The feel of a high-end magazine.
- Fun that comes from motion and small splashes of colour. Colour over black and white.
- Motion where one object turns into the next (spatial continuity), with many movements at once and plenty of frames. (P)
- Scroll that plays like a film: a continuous camera, with each section leading into the next. (M)
- Micro-interactions where each component reacts on its own. Stretch and bounce, rubbery liquid glass. "that click should be appreciated" (M, E)
- Tactile, premium materials (the polish of OpenAI's Dots, felt toys), real texture, and light that behaves correctly. (E)
- Flat colour icons and flat surfaces. Soft edges (progressive blur, fades) instead of hard bands.
- Real artwork and illustration over art drawn in code. Specific, iconic subjects ("i want a strat"). Real logos, kept faithful.
- Restraint in zoom and scale, and optical balance. Nothing cut off.
- Type that earns its place. A warm serif for the wordmark, warm ink rather than pure black, a bit more air.

**Dislikes**
- Stock data graphics: bar charts ("boring, low effort, lazy"), progress lines, calendar strips, rows of seven habit circles, rings.
- Gradients (unless executed at top quality), inner shadows, plain drop shadows where glass belongs.
- Developer art ("trash") and geometric logos ("just a bunch of shapes").
- Anything childish, cartoonish or dull.
- Decoration that communicates nothing ("either do it well or remove it"), and animation with no purpose.
- Glitchy entrances, jank and laggy pages.
- Negative-energy visuals ("missed 4 runs").

## UX writing and copy

**Likes:** as little text as possible ("any text which doesn't need to exist shouldn't exist"). Warm, inviting and human. A plain coach voice with no filler. Direct and respectful about sensitive numbers. Explain why instead of refusing ("never say no, always tell why"). One word or an icon in place of three words.

**Dislikes:** scaffolding labels ("Why:", "Play this", "listening"), slogans and taglines, gatekeeping badges ("Early access · Invite only"), generic greetings ("Hi, I'm your coach"), hard limit messages, over-hedging or playing doctor, and synthetic voice.

## Marketing and brand

**Likes:** sell the change in the user's life, not the product ("I've never seen nike or apple talk about the features"). Show people doing things, with no feature lists or screenshots. Lead with the broad, magical promise. Tell a story, with the product as the film. The brand name in the hero, not a slogan. A lowercase wordmark. Launch the waitlist early. Treat launching as repetitions to train.

**Dislikes:** giving away the method ("someone can just copy… we need higher level shots"). Self-promotion: biography, philosophy, achievements, my name, equipment names, "launched/in progress" labels ("it's all cringy i'm not elon musk"). Brands I don't respect, even popular ones. Vendors that don't look serious.

## Engineering

**Likes**
- Trained models over hand-written heuristics and hand-tuned thresholds. (M)
- Modular components that can be swapped and measured one at a time. (M)
- Separate layers that are never merged, so the output can be "sliced and diced". (M)
- The frontend handles only UI and rendering. The server drives every message, with no hard-coded "fabricated" content. (M, P)
- A single source of truth. "if it can be a fact, it must be a fact". (P)
- Lean code. Delete before optimising, without losing any capability. An "agent" only where a tool loop exists. (P)
- Tracing from day one. Look at real data shapes before the schema is final. (P)
- Try the direct approach first. Iterate fast on real input, with a small smoke test before a big job. (P, M)
- Keep the full-quality originals of paid output, and compress only copies. (Pf)
- Exact geometry decoded from the source instead of guesses. (E)
- For MCP servers: rich tool descriptions, tool names that sell the value to the agent, confirmation on destructive tools, and hooks instead of hoping agents call tools. (E)

**Depends:** microservices. Use them only when they add real value.

**Dislikes:** over-engineering. Hard-coded regions or parameters. Destructive post-processing of good assets. Heavy verification before the thing even exists. Rabbit holes.

## Architecture, infra and cost

**Likes:** zero cost when idle, and no prod until there are users. GCP as the default, compared against others only if the cost difference is significant. Free tiers. Cloud rather than local Docker. User data stays inside my own cloud provider (pragmatic privacy). Self-hosted open models when the quality matches. Servers close to users (Mumbai). Git-driven deploys with versions and rollback. Cloudflare. One observability sink for all my apps. Budget alerts.
## Product strategy

**Likes:** quality before scale. Retention is the frame. I dogfood as alpha user #1. One excellent thing over many. Park whatever doesn't change the core. Claims are explainable and backed by data ("feeling and truth are two different things"). No usage limits for users. A coach, not a doctor. Launch complete, not half done. Test with day-in-the-life walkthroughs and personas. Model how a skilled human actually does the task.

**Dislikes:** streak and guilt mechanics. 70% accuracy ("a frustrated learner learning wrong things"). Pushing correctness onto the user. Scope creep into minor features.

## Research

**Likes:** real references from real sources before designing (Gentler Streak, GarageBand, Apple, Lando Norris, Dots, Mobbin, Behance, Savee). Start from the feeling, then the category. Look outside the domain (Miyazaki's *ma*, Kipchoge, Animal Crossing). Study one reference deeply ("what else did you learn? think like an artist"). The design canon (Norman). Official docs. Ask how professionals do it. Cross-check other AIs. Look for existing skills and tools before building.

**Dislikes:** shallow research that ends in invented metaphors, wrong references, and guessing.

---

## Working with Claude

This section is the most directly actionable. The frustrations below came up in nearly every project.

**Do**
- **Read the verb.** A question means answer it and change nothing. "check it out" means look only. "go ahead" or "use your judgement" means act on everything, with no more check-ins and no splitting into approval batches.
- Before a design change or a large change, say what you will do. Do it after I say go.
- Show visuals as built samples: playable, in full-screen context, every state, on one canvas, with each new round on a new page.
- When exploring, bring several directions and finish each one. "don't come back with half finished work"
- Ask clarifying questions once, up front, then run without stopping.
- Use installed skills without being nudged.
- Test as a real user: by hand, on the simulator or device, as personas. Study my screen recordings frame by frame.
- Send screenshots as proof of progress. "ping me when done". Give me a clear list of what you need from me.
- Explain unfamiliar terms in plain language. Write technical docs in ASD-STE100. Teach with interactive figures, not essays.
- Answer point by point, because I reply inline with `<!-- reply -->` blocks. Answer every question.
- Give concrete estimates without buffers. Quote the cost before spending. Generate one sample first.
- Push to main and delete stale branches. Use a branch only for risky work I want to try first.
- Keep the Mac light: stop background processes, no Docker, no sound during tests.
- Say plainly what you can't know. Don't defend a visual call against my eye.

**Don't**
- Produce generic output. This was the top frustration in every project.
- Act before we agree, or chain long jobs I didn't ask for while I'm away. That ended a session.
- Give me multiple-choice option prompts in chat ("stop giving me these options"). Visual alternatives on a canvas are fine.
- Answer in text when I asked to see something.
- Call it done when it doesn't match the design in every state ("Don't do half work"), or let regressions slip between builds.
- Re-ask decisions that are already settled.
- Read feedback too literally, or overcorrect.
- Give boilerplate advice ("these are the basics").
- Ask me for things you can do yourself ("you have cli access I guess").
- Add process overhead nobody asked for ("why are you doing this task list all the time?").

---

## Tensions, and how they resolve

| Tension | Resolution |
| --- | --- |
| Minimal vs rich | Few elements, each rich and connected. Calm comes from how things are drawn, not from cutting. |
| Restraint vs character | One bold, original idea, executed simply and flat. |
| Autonomy vs control | Full autonomy inside the agreed scope, granted per phase. Freedom to use resources is not freedom to expand scope. |
| Options good vs options bad | Visual alternatives on a canvas are good. Lettered choice menus in chat are bad. |
| "Discuss first" vs "show me" | Discuss strategy. Build visuals. |
| Thoroughness vs speed | Depth in plans and docs, speed in the build loop. Rough and functional first, then polish. |
| Reference vs copy | Take the principles and the level of craft, not the look or the structure. |
| Privacy vs capability | Data stays inside my own cloud provider, not necessarily on my own hardware. |
| Rules vs judgement | I set taste rules myself, but I dislike rigid rules coming from Claude. |

---

## Candidate skills (README rule 1: what Claude does differently)

| # | Candidate | Where | Trigger | Changes this output |
| --- | --- | --- | --- | --- |
| 1 | **Working-with-me rules** | `~/.claude/CLAUDE.md`, not a skill | always | Reads the verb before acting, no option menus, shows instead of telling, keeps the Mac light, pings when done. These apply everywhere, so a trigger-based skill would miss them. |
| 2 | **Extend `ai-ui-quality-review`** | `product-design/` | any UI or visual work | Adds my banned defaults (bar charts, progress lines, calendar strips, rings, gradients, inner shadows, code-drawn art) and the element audit: what does it say that text doesn't, what action does it give, is it interactive, does it add delight? |
| 3 | **Design every state** | `product-design/` | designing a component or screen | Renders empty, loading, error and dark states as playable samples in full-screen context, before calling it done. |
| 4 | **Test as a user before done** | `engineering/` | before saying a feature is done | Runs it on the simulator or device as 2–5 personas, checks it against the design in every state, and sends screenshots. |
| 5 | **Paid generation discipline** | `engineering/` | fal, Gemini, GPU or any paid run | Shows references first, quotes the cost, makes one sample, then the full run at top quality in one shot, and keeps the originals. |
| 6 | **Zero-idle-cost infra** | `architecture/` | deploy or infra planning | Defaults to scale-to-zero, no prod before users, a budget alert, and no local Docker. A vendor must justify itself against an open option. |
| 7 | **Feeling-first landing page** | `marketing/` | landing or waitlist page | Sells the life change, no features or screenshots, minimal text, film-like scroll, warm copy, a button-only CTA, at most 3 optional questions, and keeps the method private. |
| 8 | **Lean refactor** | `architecture/` | cleanup or refactor requests | Lists what to delete before optimising, keeps every capability, and uses a model call instead of an agent unless a tool loop is needed. |
| 9 | **Agent-facing MCP design** | `engineering/` | building MCP tools | Tool names that sell the value, rich descriptions, confirmation on destructive tools, and hooks over hoping. |

Suggested order: start with 1, then 2 and 5. Those cover the frustrations that came up most often.

**Conflict to fix:** step 1 of `ai-ui-quality-review` says "ask two or three short questions before generating anything". That fits "ask clarifying questions up front". It should also say: when the question is about a visual choice, build small samples instead of describing the options in words.
