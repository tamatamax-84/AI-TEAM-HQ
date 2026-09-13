# HANDOFF

## Message metadata
- From: Chief
- To: Next available review AI / Reviewer Slot
- Status: READY

## Mission
Support normal AI TEAM HQ operation and independent review when a suitable non-Chief reviewer is actually available.

## Read first
- RULES.md
- ROLES.md
- TASK.md
- TASK_STATES.md
- DECISIONS.md
- AI_STATUS.md
- AI_TEAM_PROTOCOL.md
- REVIEWER_SLOT.md

## Required actions for a review handoff
1. Check the current `RULES.md` before acting.
2. Check current AI status and role boundaries.
3. Inspect only the minimum relevant project/task context.
4. Check protocol consistency, requirements, implementation, risks, edge cases, or other review scope assigned by Chief.
5. Do not perform high-load implementation.
6. Record findings in the appropriate review/result artifact.
7. Provide evidence and a review status of `PASS`, `WARN`, `FAIL`, or `NOT_PERFORMED`.

## Output contract
Report:
- status
- reviewer
- files/context inspected
- review scope
- findings
- severity / priority
- recommended changes
- checks performed
- evidence or repository reference
- remaining risks / unknowns
- recommendation for the next agent

## Important
Only claim a review occurred when the reviewer was actually available and produced evidence. Claude is currently `NOT_CONNECTED`; Gemini is `RETIRED`. CodeRabbit is the currently verified Reviewer Slot candidate. If no eligible reviewer is available, record the review as pending/unavailable rather than claiming completion.
