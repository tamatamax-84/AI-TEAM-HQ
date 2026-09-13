# AI TEAM LOG

## 2026-09-14

### Chief
- Added shared memory and memory economy policy to `RULES.md` as v1.3.
- Defined GitHub as durable shared memory for important work performed both inside and outside GitHub.
- Defined selective reading to reduce context and credit usage: AIs should load only the minimum relevant memory instead of the entire archive.
- Defined periodic memory maintenance: obsolete, redundant, superseded, or low-value records should be consolidated, archived, or deleted when appropriate.
- Assigned default memory maintenance ownership to ChatGPT / Chief because cleanup requires cross-file judgment and can be high-load.
- Limited Copilot and Gemini to identifying stale/redundant/conflicting information and recommending cleanup unless the user explicitly authorizes an exception.
- Recorded these decisions as D-007 and D-008.

### Next
Maintain shared memory deliberately: preserve active rules, confirmed decisions, required evidence, unresolved issues, and useful current state; avoid unnecessary accumulation and unnecessary context loading.

## 2026-09-13

### Chief
- Created AI TEAM HQ foundation.
- Defined roles and operating rules.
- Created the first TASK and HANDOFF for Copilot.
- Initialized RESULT and REVIEW channels.
- Recorded initial architecture decisions.
- Added mandatory rule-integrity policy: every AI must read the current `RULES.md` before every task/action/recommendation/handoff/review/result, and rulebook changes require explicit user authorization.
- Recorded this policy as decision D-006.

### Next
All AIs must perform the mandatory `RULES.md` check before continuing any work. Do not treat accumulated conversation context as a substitute for rereading the current rulebook.
