# REVIEWER SLOT

## Purpose
The Reviewer Slot is the team's interchangeable independent-review role. It prevents the HQ workflow from depending on one specific review AI and is designed to minimize user bridging work.

## Core policy
- Chief / ChatGPT remains the only default high-load execution AI.
- The Reviewer Slot is for low-load independent review, critique, validation guidance, risk detection, and handoff support only.
- Prefer a reviewer that is actually available, connected, permitted for the requested review, and has usable free quota.
- Prefer free-quota usage over paid usage when review quality and reliability are sufficient.
- Do not create billing credentials, API keys, or paid usage merely to fill the Reviewer Slot.
- If the preferred reviewer is unavailable or its usable quota is exhausted, select the next eligible reviewer when practical.
- A reviewer becoming available again may return to the candidate pool after availability is verified.
- Reviewer substitution must not change the task, constraints, authority, or completion criteria.
- If no eligible reviewer is available, mark the review as pending/unavailable rather than claiming that review occurred.

## Review priority
1. Reviewer with verified active/free availability and the best fit for the review type.
2. Another verified active/free reviewer with sufficient independent perspective.
3. A reviewer already integrated into the GitHub workflow when that avoids user intervention.
4. If none is available, defer the independent review and preserve the next review action in the task/handoff.

## Review triggers
Use the Reviewer Slot when review value justifies consuming a limited AI quota. Prioritize:
- substantial code or architecture changes
- new features or behavior changes
- security-sensitive changes
- release readiness
- rule/protocol changes
- unresolved design or implementation uncertainty

Do not spend reviewer quota on trivial edits unless the task explicitly requires review.

## Evidence format
Every completed review should report, when available:
- Reviewer
- Review target
- Review scope
- Findings
- Severity / priority
- Recommended action
- Evidence or repository reference
- Unknowns / limitations
- Review status: `PASS`, `WARN`, `FAIL`, or `NOT_PERFORMED`

## No-fake-review rule
A review may be recorded as completed only when there is evidence that the reviewer actually performed it. A requested handoff, planned review, or unavailable reviewer is not a completed review.

## Current candidates
The candidate pool is represented by `AI_STATUS.md`. Gemini and Claude remain candidates only when their actual connection/availability is verified. Copilot may serve as the review hub and reviewer when appropriate, subject to its role limits.
