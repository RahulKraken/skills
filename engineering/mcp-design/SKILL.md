---
name: mcp-design
description: Use when designing, building or reviewing an MCP server, agent tools or tool schemas that other AI agents will call. Make sure to use this whenever tool names, tool descriptions or tool parameters are being written, even inside a larger backend task.
---

# MCP design

## Context

From Encognition, Rahul's memory layer for AI agents. The tools are only valuable if agents choose to call them, and agents choose from names and descriptions alone. Generic names like "Get Context" and "Search Memory" give an agent no reason to call them: "Otherwise, why would I need to call these tools?"

## Names and descriptions

- **Name tools by what the agent can't get otherwise.** "Understand how the user thinks" or "Get the user's taste", not `get_context`. The name is persuasion aimed at the agent.
- **Describe in detail**: what it returns, when to call it, when not to, and a short example of a good call. "It's always a good idea to have as much detail about a tool as possible… so that agents know exactly what to call and how."
- **Few tools, each justified.** If two tools would be called together every time, merge them.

## Behaviour

- **Don't rely on agents behaving well.** "we are using tools and hoping that AI agents are going to write relevant memories to us. What if, instead… hooks?" Where it matters, capture with hooks or server-side processing instead of hoping the agent calls a tool.
- **Do the intelligence on the server.** Extraction and ranking server-side cost the user no tokens and get better over time.
- **Explicit user confirmation on anything destructive or that changes stored memory.** "management tools must need explicit user confirmations".
- **A real agent only where there's a loop.** If something isn't calling tools in a loop, it's a single model call or a tool, not an agent.

## Data and cost

- Keep user data inside your own cloud provider; no extra outside AI vendor without a reason ("It's people's memories").
- Every dependency justifies itself against an open option ("what does voyage do which open embedding models can't do?").

## Deliverable

Tool definitions (name, description, parameters with types and examples), which flows use hooks instead of tools, and which tools need confirmation. Keep any explanation to Rahul short; the definitions should speak for themselves.
