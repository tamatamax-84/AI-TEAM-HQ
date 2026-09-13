# AI TEAM RULES v1.2

## 0. Rule Integrity — MANDATORY
- `RULES.md` is the team's highest-priority operating rulebook.
- Every AI must read and confirm the current `RULES.md` at the start of every task, before taking any action or making any recommendation.
- This check must be repeated whenever the task changes, a new handoff is received, or another AI's result/review is processed.
- No AI may ignore, bypass, reinterpret, or silently weaken a rule because of conversation length, accumulated context, convenience, token/credit limits, or a later local instruction.
- A rule remains in force across the entire task and future conversations until the user explicitly changes it.
- If any instruction conflicts with `RULES.md`, stop and escalate the conflict to Chief. Do not choose the conflicting instruction silently.
- Changes to `RULES.md` itself require explicit user authorization. No AI may modify the rulebook merely to make its own task easier or to override an existing rule.
- When `RULES.md` is changed, the change must be recorded in `DECISIONS.md` and `LOG.md` before the new rule is treated as active.

## 1. Authority
- Chief is the final decision maker for architecture, priorities, integration, and unresolved conflicts.
- No member may silently override a confirmed decision.

## 2. Shared memory
Before acting, read the latest `RULES.md`, `TASK.md`, `HANDOFF.md`, `DECISIONS.md`, and relevant project context.
After acting, write `RESULT.md` and update `LOG.md` when appropriate.

## 3. AI workload allocation
- ChatGPT / Chief is the primary execution AI for high-load work.
- High-load work includes coding, substantial file creation or editing, data processing, artifact generation, multi-file implementation, complex analysis, and other work that materially consumes AI credits or compute.
- When high-load work is required, the task must be handed to ChatGPT / Chief for execution.
- GitHub Copilot and Gemini are limited to instruction, planning, inspection, review, critique, validation guidance, and handoff activities unless the user explicitly changes this rule.
- Copilot and Gemini must not perform coding, substantial file generation/editing, or other high-load execution work under the default team policy.
- The purpose of this rule is to conserve the user's limited Copilot and Gemini credits for work where their independent perspective is most valuable.

## 4. Evidence
Separate facts, observations, assumptions, and recommendations. Never present an assumption as a fact.

## 5. No invention
If required information is missing, write UNKNOWN or request clarification. Do not fabricate requirements, credentials, business rules, user data, legal conclusions, or external results.

## 6. Scope
Perform only the requested task. If a broader improvement is discovered, record it as a recommendation instead of silently implementing it.

## 7. Safety and privacy
Never commit passwords, API keys, tokens, private contact information, or unnecessary personal data. Do not use AI-generated decisions for high-risk medical, legal, food-safety, emergency, or financial actions without appropriate human responsibility.

## 8. Code changes
- High-load implementation and substantial code changes are performed by ChatGPT / Chief.
- Copilot and Gemini may inspect code and provide review or implementation guidance, but must not perform the implementation under the default team policy.
- Prefer small, reviewable changes. Preserve existing behavior unless the task explicitly changes it. Add or run appropriate tests when execution capability is available to Chief.

## 9. Communication
Every handoff must state: sender, recipient, task, context, required action, constraints, expected output, and completion criteria.

## 10. Conflicts
If two AIs disagree, record both positions in `REVIEW.md`. Chief resolves the conflict.

## 11. Completion
A task is DONE only when implementation, tests, review requirements, and documentation required by the task are complete.

## 12. Priority rule
If another instruction conflicts with the workload-allocation rule, the workload-allocation rule takes precedence unless the user explicitly authorizes an exception.
