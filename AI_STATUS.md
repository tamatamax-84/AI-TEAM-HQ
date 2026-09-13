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
| GitHub Copilot | ACTIVE | Instruction / review hub / Reviewer Slot candidate | NO |
| CodeRabbit | ACTIVE | Automated PR reviewer / Reviewer Slot | NO |
| Gemini | NOT_CONNECTED | Reviewer Slot candidate / independent reviewer | NO |
| Claude | NOT_CONNECTED | Reviewer Slot candidate / design & review specialist | NO |

## Reviewer Slot
- `REVIEWER_SLOT.md` defines the interchangeable independent-review role.
- The slot prefers a verified active reviewer with usable free quota and suitable review capability.
- Do not create billing credentials or paid usage merely to fill the slot.
- If one reviewer is unavailable or its usable quota is exhausted, another eligible reviewer may be selected without changing the task or authority structure.
- A reviewer must be actually available and must produce evidence before its review is recorded as completed.
- CodeRabbit is now an evidence-verified Reviewer Slot candidate based on PR #1. Its verified role is automated low-load PR review only.
- If no eligible reviewer is available, the review remains pending/unavailable; do not claim completion.

## Status rules
- Credit exhaustion or availability problems must be reflected here when known.
- Non-Chief AIs may be rested and their low-load work reassigned to another available AI.
- High-load work remains with ChatGPT / Chief by default even when another AI has available credits.
- If ChatGPT / Chief is unavailable for high-load work, pause the overall high-load task and preserve only the next actionable resumption step as required by `RULES.md`.
- Do not claim an AI is connected, available, or exhausted without evidence.
