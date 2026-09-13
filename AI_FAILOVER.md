# AI FAILOVER PROTOCOL

## Purpose
Keep the AI team operational when a non-Chief AI becomes unavailable, while protecting ChatGPT / Chief's role as the only default high-load executor.

## Non-Chief AI unavailable
If Copilot, Gemini, Claude, or another non-Chief AI reaches a credit limit or becomes unavailable:
1. Mark the AI `SUSPENDED` or `UNAVAILABLE` in `AI_STATUS.md` when evidence is available.
2. Reassign only its normal instruction/review/inspection responsibilities to another available non-Chief AI when practical.
3. Preserve the original task, constraints, evidence requirements, and authority structure.
4. Do not allow the replacement AI to perform high-load work merely because it is available.
5. Restore the AI to `ACTIVE` only after availability is verified.

## ChatGPT / Chief unavailable
If ChatGPT / Chief reaches a credit limit or otherwise cannot continue:
1. Save only the next actionable task, required context, constraints, and completion criteria needed for Chief to resume.
2. Stop the overall high-load work.
3. Do not transfer high-load execution to another AI by default.
4. Inform the user that the project is paused for Chief's return.
5. Other AIs may still perform independent low-load review or inspection only if it does not advance the paused high-load execution.
6. Resume from the saved next action when Chief becomes available.

## Priority
`RULES.md` always takes precedence over this protocol.
