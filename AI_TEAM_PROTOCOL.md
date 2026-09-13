# AI TEAM PROTOCOL

## Standard operating sequence
1. Read and confirm the current `RULES.md`.
2. Check `AI_STATUS.md` and confirm the AI's current status and role.
3. Read only the relevant `TASK.md`, `HANDOFF.md`, memory, decisions, and project context.
4. Confirm that the requested action is permitted for the AI's role.
5. If the task is high-load, ChatGPT / Chief owns execution by default.
6. Before high-load execution, evaluate lower-load alternatives and choose one when it preserves required quality and correctness.
7. Perform only the assigned work.
8. Record actual results and evidence in the appropriate HQ artifact.
9. If an independent review is required, use the `REVIEWER_SLOT.md` routing policy and select an eligible reviewer based on verified availability, role fit, and free-quota preference.
10. Create a precise handoff when another AI must act next.
11. If a credit or availability limit is encountered, follow `AI_FAILOVER.md` and, for review work, use the Reviewer Slot when another eligible reviewer is available.
12. If Chief is unavailable, preserve only the next actionable resumption step and pause high-load work.
13. Reread `RULES.md` whenever the task changes or a new handoff/result/review is received.

## Core principle
The team optimizes for reliable completion with minimum user effort and minimum unnecessary AI credit/compute usage. More AIs do not mean more simultaneous execution; they provide redundancy, independent review, and specialized perspectives.

## Reviewer principle
The team does not depend on Gemini, Claude, Copilot, or any single reviewer by name. The review role is interchangeable. Prefer verified free availability and GitHub-integrated workflows where they reduce user intervention, but never invent a connection or claim a review that did not occur.
