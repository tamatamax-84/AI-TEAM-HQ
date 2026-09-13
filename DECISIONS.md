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

## D-007 — GitHub is the durable shared memory for all work
**Status:** CONFIRMED

Important information from work performed both inside and outside GitHub should be recorded in AI TEAM HQ when another AI may need it later. The team should save decisions, current state, key results, constraints, unresolved issues, findings, and handoff information, while avoiding unnecessary raw transcripts, temporary thoughts, duplicates, and low-value content.

## D-008 — ChatGPT owns memory maintenance by default
**Status:** CONFIRMED

Periodic memory maintenance is assigned to ChatGPT / Chief because it is high-load work requiring cross-file judgment. Copilot and Gemini may identify stale, redundant, obsolete, or conflicting information and recommend cleanup, but do not perform high-load cleanup by default. Cleanup must preserve active rules, confirmed decisions, required evidence, unresolved issues, and information still needed to operate the team.

## D-009 — All future AIs remain non-Chief high-load restricted
**Status:** CONFIRMED

Adding Claude or any future AI does not change the default workload allocation. ChatGPT / Chief remains the only default high-load execution AI. Other AIs provide instruction, planning, inspection, review, critique, validation guidance, and handoffs.

## D-010 — Non-Chief failover is allowed; Chief high-load failover is not default
**Status:** CONFIRMED

When a non-Chief AI reaches a credit limit or becomes unavailable, its normal low-load responsibilities may be reassigned to another available AI. When ChatGPT / Chief reaches a credit limit or becomes unavailable, high-load work pauses instead of being transferred to another AI. Only the next actionable resumption step and required context are preserved, and the user is informed.

## D-011 — Optimize high-load work before execution
**Status:** CONFIRMED

Before any high-load execution, Chief must consider lower-load alternatives such as targeted edits, incremental processing, reuse of existing artifacts, selective memory loading, or smaller test scopes. A lower-load approach should be preferred when it preserves required quality and correctness.

## D-012 — Interchangeable Reviewer Slot
**Status:** CONFIRMED

The independent-review role is a slot rather than a permanent dependency on Gemini. Gemini, Claude, Copilot, or another explicitly registered non-Chief AI may fill the slot when its connection, availability, role fit, and usable free quota are verified. Prefer free-quota usage and already integrated workflows when quality is sufficient. Do not create billing credentials or paid usage merely to fill the slot. Reviewer substitution does not change task scope, authority, or completion criteria, and a review is not considered complete without evidence that it actually occurred.
