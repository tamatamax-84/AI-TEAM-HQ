# TASK STATES

## Lifecycle
`IDEA` → `READY` → `IN_PROGRESS` → `REVIEW` → `APPROVED` → `DONE`

Possible exception states:
- `BLOCKED` — cannot proceed because required information, access, approval, or capability is missing.
- `PAUSED` — intentionally stopped, including Chief credit exhaustion.
- `CANCELLED` — explicitly cancelled by the user or Chief under an approved decision.

## State rules
- `IDEA`: captured but not yet approved for execution.
- `READY`: objective, constraints, and completion criteria are sufficiently defined.
- `IN_PROGRESS`: assigned work is actively being executed.
- `REVIEW`: execution is complete enough for independent checking.
- `APPROVED`: review requirements are satisfied and Chief accepts the result.
- `DONE`: implementation, required tests/checks, review, documentation, and handoff requirements are complete.
- `BLOCKED`: record the blocker and the exact information/action required to unblock.
- `PAUSED`: record only the information required to resume efficiently; do not accumulate unnecessary context.
- `CANCELLED`: preserve the reason and any reusable result when useful.

## Review rejection / rework
- If review finds a correctable issue, the task returns from `REVIEW` to `IN_PROGRESS` with a recorded rework request and updated completion criteria if needed.
- After rework, the task returns to `REVIEW` for another independent check.
- A task must not move directly from `REVIEW` to `DONE`.
- `APPROVED` is the explicit gate between successful review and `DONE`.

## Completion gate
A task must not be marked `DONE` merely because an AI says it is done. Evidence and required checks must support completion.
