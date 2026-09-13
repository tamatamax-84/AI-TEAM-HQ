# AI STATUS

This file is the shared operational status registry for AI TEAM HQ.

## Status values
- `ACTIVE` — available for assigned role.
- `LIMITED` — available with meaningful restrictions.
- `SUSPENDED` — intentionally resting or paused.
- `UNAVAILABLE` — currently unable to perform its role.
- `NOT_CONNECTED` — not yet connected to the team.

## Current status

| AI | Status | Default role | High-load execution |
|---|---|---|---|
| ChatGPT / Chief | ACTIVE | Chief / execution / memory maintenance | YES |
| GitHub Copilot | ACTIVE | Instruction / review hub | NO |
| Gemini | NOT_CONNECTED | Independent reviewer | NO |
| Claude | NOT_CONNECTED | Design / review specialist | NO |

## Status rules
- Credit exhaustion or availability problems must be reflected here when known.
- Non-Chief AIs may be rested and their low-load work reassigned to another available AI.
- High-load work remains with ChatGPT / Chief by default even when another AI has available credits.
- If ChatGPT / Chief is unavailable for high-load work, pause the overall high-load task and preserve only the next actionable resumption step as required by `RULES.md`.
- Do not claim an AI is connected, available, or exhausted without evidence.
