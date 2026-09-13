# HANDOFF

## Message metadata
- From: Chief
- To: Protocol validation / next available review AI
- Status: READY

## Mission
Validate the current AI TEAM HQ protocol before Gemini and Claude are used for normal work.

## Read first
- RULES.md
- ROLES.md
- TASK.md
- TASK_STATES.md
- DECISIONS.md
- AI_STATUS.md
- AI_TEAM_PROTOCOL.md

## Required actions
1. Check protocol consistency and role boundaries.
2. Verify that credit-limit and failover behavior is unambiguous.
3. Verify that high-load work remains ChatGPT-only by default.
4. Verify that high-load work requires a lower-load alternative check before execution.
5. Verify that memory is selectively loaded and periodically maintained by Chief.
6. Identify any contradictions, missing gates, stale instructions, or unsafe assumptions.
7. Do not perform high-load implementation.
8. Record findings in the appropriate review/result artifact.

## Output contract
Report:
- status
- files inspected
- findings
- contradictions or gaps
- recommended changes
- checks performed
- remaining risks
- recommendation for the next agent

## Important
If Gemini or Claude is not actually available through the current environment, do not pretend the review occurred. Record the exact review handoff needed instead.
