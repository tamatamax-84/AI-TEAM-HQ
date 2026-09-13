# TASK

## Status
REVIEW

## Objective
Complete validation of the AI TEAM HQ collaboration protocol before using it as the shared control center for future projects.

## Current phase
Repository-evidenced sample lifecycle test.

## Lifecycle test
- READY: commit `2c8bc2eb00bc2c3ca347039e62ac9b594e568458`
- IN_PROGRESS: commit `1ad5e9316da7ff3f496bddeedbe068389d90f1ab`
- REVIEW: execution phase completed; protocol evidence is now under review.

## Review evidence
- `TASK_STATES.md` explicitly requires `REVIEW → APPROVED → DONE` and prohibits direct `REVIEW → DONE`.
- The Reviewer Slot is evidence-verified through CodeRabbit's actual PR #1 review.
- CodeRabbit detected the intentional parity defect in `tests/coderabbit_review_demo.py`, demonstrating that repository-based review evidence can catch a real issue.
- PR #1 was closed without merge after verification.
- Chief re-read `RULES.md` before this lifecycle test and verified the completion/evidence requirements.

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
