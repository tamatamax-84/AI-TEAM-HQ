# TASK

## Status
REVIEW

## Objective
Complete validation of the AI TEAM HQ collaboration protocol before using it as the shared control center for future projects.

## Current phase
Protocol validation — Chief execution/check phase complete; independent review pending.

## Completed foundation
- Rule integrity and mandatory rule rereading
- Chief-only default high-load execution
- High-load optimization check
- Shared memory / memory economy
- Chief-specific credit exhaustion pause behavior
- Non-Chief AI failover behavior
- AI status and suspension/recovery lifecycle
- AI capability registry
- Universal team operating protocol
- Task lifecycle and completion gates
- Project registration standard
- Claude role definition
- Concise current-state memory
- Monthly memory cleanup + HQ health-check cycle

## Validation performed by Chief
- Re-read the current `RULES.md` before continuing.
- Checked the task lifecycle definition against the operating protocol.
- Checked that high-load execution, optimization, evidence, handoff, failover, and memory rules are mutually aligned.
- Checked that the current handoff explicitly prevents claiming an unavailable Gemini/Claude review.
- Checked that task completion requires evidence rather than an AI assertion.

## Current review gate
The protocol is ready for independent review. Gemini and Claude are still `NOT_CONNECTED`, so no independent AI review is claimed as completed.

## Remaining validation
- Obtain an actual independent review from an available non-Chief AI.
- Resolve and record any findings.
- Verify the full sample lifecycle reaches APPROVED and DONE with repository evidence.
- Connect and verify Gemini.
- Connect and verify Claude.
- Run a small multi-AI rule-compliance and handoff test.
- Fix any issues discovered during the test before normal project work.

## Ongoing maintenance
- Monthly maintenance combines shared-memory cleanup with an AI TEAM HQ health check.
- The health check reviews rule consistency, system/control-file consistency, task lifecycle readiness, AI status/failover behavior, stale or conflicting information, and whether a new project can safely enter the workflow.
- Findings are recorded in `LOG.md`; proposed rule changes require explicit user authorization and the normal decision/change procedure.
- Chief owns the monthly maintenance by default. Other AIs may flag issues during low-load review but do not perform high-load cleanup by default.

## Constraints
- User should not manually edit code or protocol files.
- Do not create external credentials or secrets.
- Do not assume direct AI-to-AI chat exists.
- GitHub is the shared memory and message bus.
- High-load execution is ChatGPT / Chief only by default.
- Other AI credits are reserved for low-load instruction, review, inspection, critique, validation, and handoff work.

## Completion condition
The protocol is internally consistent, every active AI can enter/exit work using the defined lifecycle, credit-limit behavior is unambiguous, and a sample task can move from READY through review to DONE using repository evidence.
