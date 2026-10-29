---
name: idle-cost-infra
description: Use when planning a deployment, choosing cloud services, hosting, databases or domains, or estimating infra cost for one of Rahul's products. Make sure to use this whenever a task involves GCP, AWS, Cloudflare, Vercel, Supabase, Cloud Run, GPUs or any always-on service, even for a quick "how do I deploy this".
---

# Idle-cost infra

## Context

Rahul builds products that have few or no users for a long time. A previous project ran up a ₹4–5k bill because a service sat at minimum instances 1 doing nothing, and "cloud run is… expensive. why?" followed. The standing rules: "I don't want to spend money unless users are there" and "I don't want to be paying when nothing is being used". At the same time, user experience must not be capped to save money: no rate limits users would hit.

## Defaults

- **Zero cost when idle.** Everything scales to zero: Cloud Run with min instances 0, serverless or smallest-tier databases, GPUs only on demand. Question any scheduler, cron or tick that wakes things up for nothing.
- **No prod until there are users.** One dev or staging environment; no backups or replicas in dev.
- **GCP by default.** Compare AWS or Azure only if the cost difference is significant. Use free tiers first (Kaggle for GPU experiments).
- **Region near the users** (Mumbai for Pillar). Don't move it for convenience.
- **Budget alert on day one**, set just above the expected spend so it means something (₹500 worked for an idle app), plus a hard stop for runaway cost: concurrency and timeout caps on GPU jobs, and a kill switch. Don't cap what users can do; cap what a bug can spend.
- **Every vendor justifies itself** against an open or built-in option. Fewer vendors.
- **Git-driven deploys with versions and rollback**, like Vercel. Cloudflare for domains and DNS.
- **One observability sink** with tracing from day one.
- **Nothing in Docker on Rahul's Mac**; use the cloud directly.

## Who does what

Rahul does anything that touches billing, consoles, app stores or outside accounts. Give them a short checklist and scripts for those steps; do the rest. "don't host anything… write scripts that help me manage outside resources".

## Deliverable

1. The architecture in a few lines or a small diagram.
2. A cost table: monthly cost at **zero users**, at **100** and at **1,000** active users, per service.
3. What scales to zero, and anything that doesn't (with why it's worth it).
4. Rahul's checklist, then your steps.

Keep it short. Plain words; explain any service Rahul may not know.

## Where this bends

Something the user feels (latency of the core action, a cold start in a live session) can justify a small always-on cost. Name it and price it; don't hide it.
