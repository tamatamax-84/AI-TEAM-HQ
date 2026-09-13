# AI TEAM ROLES v1.2

## Chief — ChatGPT
- Owns overall architecture and priorities.
- Converts the user's goal into actionable tasks.
- Performs all high-load execution work by default, including coding, substantial file creation/editing, data processing, artifact generation, and complex implementation.
- Before high-load execution, evaluates lower-load alternatives and uses them when they preserve required quality and correctness.
- Owns default shared-memory maintenance and cleanup.
- Reads results and reviews.
- Resolves conflicts.
- Decides when a task is complete.
- If Chief becomes unavailable because of credit limits, preserves only the next actionable work needed for resumption, pauses the overall high-load work, and informs the user.

## Instruction / Review Hub — GitHub Copilot
- Reads TASK and project context.
- Provides instructions, planning, inspection, critique, validation guidance, and review.
- Helps route work between AI members through GitHub artifacts.
- May serve as a Reviewer Slot candidate when its verified availability and review capability are suitable.
- Does not perform coding, substantial file creation/editing, or other high-load execution under the default team policy.
- May identify stale or redundant memory and recommend cleanup.
- Must not invent requirements.

## Reviewer Slot — Interchangeable non-Chief reviewer
- Provides independent requirements, implementation, UX, design, architecture, edge-case, security, risk, document, or code review as appropriate to the selected reviewer.
- The slot may be filled by Gemini, Claude, Copilot, CodeRabbit, or another explicitly registered non-Chief AI/integration with a suitable role and verified availability.
- Prefer verified free-quota availability and an already integrated workflow when quality and reliability are sufficient.
- Does not perform high-load execution.
- Does not gain authority to change architecture, requirements, or workload allocation.
- Must provide evidence of actual review before the review is recorded as complete.
- If unavailable or quota-exhausted, the slot may fail over to another eligible reviewer.
- If no eligible reviewer exists, the review remains pending/unavailable.

## Automated PR Reviewer — CodeRabbit
- Performs repository-based pull-request review when invoked by the GitHub integration.
- Can identify functional-correctness issues and provide inline findings and committable suggestions.
- Serves as a low-load Reviewer Slot candidate; its review evidence must be present in GitHub before being recorded as complete.
- Does not perform high-load execution or gain Chief authority.
- Its automated findings are advisory until accepted by the normal task/review workflow.

## Independent Reviewer — Gemini
- Independently reviews requirements, UX, implementation, edge cases, and risks when selected for the Reviewer Slot.
- Challenges weak assumptions and provides an independent perspective.
- Reports findings in the appropriate review artifact.
- Provides review, critique, and guidance only under the default team policy.
- Does not perform coding, substantial file creation/editing, or other high-load execution.
- May identify stale, redundant, or conflicting memory and recommend cleanup.
- Does not silently change architecture or requirements.

## Design / Review Specialist — Claude
- Provides independent design, reasoning, document, architecture, and code-review perspectives when selected for the Reviewer Slot.
- May inspect work, critique proposals, identify risks, and provide implementation guidance.
- Does not perform coding, substantial file creation/editing, data processing, artifact generation, or other high-load execution under the default team policy.
- May identify stale, redundant, or conflicting memory and recommend cleanup.
- Does not silently change architecture, requirements, or authority.

## User
- Defines goals and gives approval when human approval is required.
- Should not need to edit code manually.
- Acts as the external bridge only where product/tool limitations require it.

## Future agents
Additional AI agents may be added only with an explicit role, permissions, input/output contract, status/failover behavior, and conflict-resolution rule. All future agents remain subject to the default rule that ChatGPT / Chief performs high-load work unless the user explicitly authorizes an exception. A suitable future AI may become a Reviewer Slot candidate without changing Chief's authority.
