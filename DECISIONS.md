# DECISIONS

## D-001 — GitHub is the shared AI workspace
**Status:** CONFIRMED

GitHub is used as the shared memory, task board, handoff channel, result archive, and audit trail for the AI team.

## D-002 — Chief has final authority
**Status:** CONFIRMED

ChatGPT / Chief makes final architecture, priority, integration, and conflict decisions unless the user explicitly overrides them.

## D-003 — No fake autonomy
**Status:** CONFIRMED

The team must distinguish actual tool execution from a requested handoff. No AI may claim another AI executed something unless there is evidence in the repository or connected tool result.

## D-004 — User manual work is minimized
**Status:** CONFIRMED

The desired operating model is that the user states the goal and acts as a bridge only where product/tool limitations require it.

## D-005 — ChatGPT is the primary execution AI
**Status:** CONFIRMED

Because the user's Copilot and Gemini usage has limited credits, ChatGPT / Chief performs high-load work by default. This includes coding, substantial file creation/editing, data processing, artifact generation, multi-file implementation, and complex implementation. GitHub Copilot and Gemini are reserved for instruction, planning, inspection, review, critique, validation guidance, and handoffs unless the user explicitly authorizes an exception.

## D-006 — Rules must be checked every time
**Status:** CONFIRMED

Every AI must read the current `RULES.md` before every task, action, recommendation, handoff, review, or result. The rule check must be repeated when a task changes or a new handoff/result/review is received. No AI may silently ignore, weaken, reinterpret, or bypass the rules because of conversation length, accumulated context, convenience, or resource limits. Changes to `RULES.md` require explicit user authorization and must be recorded in `DECISIONS.md` and `LOG.md` before becoming active.
