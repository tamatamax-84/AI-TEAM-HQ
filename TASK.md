# TASK

## Status
APPROVED

## Objective
Complete validation of the AI TEAM HQ collaboration protocol before using it as the shared control center for future projects.

## Current phase
Sample lifecycle review completed and accepted by Chief.

## Lifecycle test evidence
- READY: commit `2c8bc2eb00bc2c3ca347039e62ac9b594e568458`
- IN_PROGRESS: commit `1ad5e9316da7ff3f496bddeedbe068389d90f1ab`
- REVIEW: commit `dc80eb87656b10c6d53c156b3249b931d77fa9ef`
- The test did not use a direct `REVIEW → DONE` transition.
- `TASK_STATES.md` requires explicit `APPROVED` before `DONE`.
- Reviewer Slot evidence exists from CodeRabbit PR #1, which detected the intentional parity defect and was closed without merge.
- Chief re-read `RULES.md` and accepted the lifecycle evidence.

## Approval decision
**APPROVED by Chief.**

The repository evidence demonstrates the required ordered lifecycle through `READY → IN_PROGRESS → REVIEW`, and the explicit approval gate is now recorded before completion.

## Completion criteria
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
