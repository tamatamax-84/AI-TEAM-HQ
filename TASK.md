# TASK

## Status
READY

## Objective
Complete validation of the AI TEAM HQ collaboration protocol before using it as the shared control center for future projects.

## Current phase
Repository-evidenced sample lifecycle test.

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
- Interchangeable Reviewer Slot architecture
- CodeRabbit repository-based Reviewer Slot validation
- Gemini retirement from normal team routing

## Validation performed by Chief
- Re-read the current `RULES.md` before continuing.
- Checked the task lifecycle definition against the operating protocol.
- Checked that high-load execution, optimization, evidence, handoff, failover, and memory rules are mutually aligned.
- Checked that task completion requires evidence rather than an AI assertion.
- Verified CodeRabbit performed an actual repository-based review of temporary PR #1.
- Verified CodeRabbit detected the intentional parity-check defect in `tests/coderabbit_review_demo.py`.
- Closed PR #1 without merging it after verification.
- Recorded CodeRabbit review evidence in `REVIEW.md` and registered it in the Reviewer Slot status/capability registries.
- Verified Gemini is retired and excluded from routing/review.
- Verified Claude remains optional and is not claimed as connected.

## Current review gate
The Reviewer Slot is verified with repository evidence through CodeRabbit. The remaining test is the state-machine lifecycle itself.

## Lifecycle test target
Exercise this exact sequence with repository evidence:
`READY → IN_PROGRESS → REVIEW → APPROVED → DONE`

## Lifecycle test criteria
- Each state transition is represented by a repository commit.
- `REVIEW` is reached only after execution is sufficiently complete for checking.
- `APPROVED` is explicit and precedes `DONE`.
- `DONE` is recorded only after evidence and required checks support completion.
- No direct `REVIEW → DONE` transition is used.

## Constraints
- User should not manually edit code or protocol files.
- Do not create external credentials or secrets.
- Do not assume direct AI-to-AI chat exists.
- GitHub is the shared memory and message bus.
- High-load execution is ChatGPT / Chief only by default.
- Other AI credits are reserved for low-load instruction, review, inspection, critique, validation, and handoff work.

## Completion condition
The protocol is internally consistent, every active AI can enter/exit work using the defined lifecycle, credit-limit behavior is unambiguous, and this sample task moves from READY through review to DONE using repository evidence.
