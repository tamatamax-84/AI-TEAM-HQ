# AI TEAM CURRENT MEMORY

## Team purpose
AI TEAM HQ is the shared control center and durable memory for a multi-AI team. GitHub is the shared workspace, message bus, and audit trail.

## Current architecture
User → Chief → AI TEAM HQ → specialized AI review/instruction → Chief.
AI-to-AI communication must not be assumed to be direct; repository artifacts are the shared handoff mechanism unless an actual integration is verified.

## Active roles
- ChatGPT / Chief: final authority, all default high-load execution, architecture, integration, and memory maintenance.
- GitHub Copilot: instruction, GitHub-oriented inspection, review, validation guidance, and handoff support.
- CodeRabbit: verified low-load automated PR reviewer and current Reviewer Slot candidate.
- Gemini: independent review and critique; not yet connected.
- Claude: design/reasoning/architecture/code review; not yet connected.

## Core policies
- Every AI must read and confirm the current `RULES.md` before acting or recommending anything, and reread it when the task changes or a new handoff/result/review is received.
- High-load work is ChatGPT-only by default, including for future AIs.
- Before high-load execution, Chief must consider lower-load alternatives and use them when they preserve quality and correctness.
- Non-Chief AI credit exhaustion may trigger suspension and reassignment of low-load duties.
- Chief credit exhaustion pauses high-load work; only the next actionable resumption step and required context are saved, and the user is informed.
- GitHub stores important shared knowledge from both GitHub and non-GitHub work, but AIs load only relevant memory.
- Memory is periodically consolidated, archived, or deleted by Chief while preserving active rules, decisions, evidence, unresolved issues, and required operating knowledge.
- Monthly maintenance combines memory cleanup with a HQ health check covering rule consistency, control-file/system consistency, task lifecycle readiness, AI status/failover behavior, stale/conflicting information, and safe project-entry readiness.
- Health-check findings are recorded in `LOG.md`; rule changes still require explicit user authorization and the normal decision/change procedure.

## Verified Reviewer Slot result
- CodeRabbit successfully performed a repository-based review of temporary PR #1 and detected the intentional `is_even` parity defect.
- PR #1 was closed without merge after verification.
- The review evidence is recorded in `REVIEW.md`; CodeRabbit is registered in `AI_STATUS.md` and `AI_CAPABILITIES.md`.

## Current next action
Exercise the repository-evidenced sample task lifecycle `READY → IN_PROGRESS → REVIEW → APPROVED → DONE`. Keep Gemini/Claude optional until actually connected and useful; do not claim either review occurred.
