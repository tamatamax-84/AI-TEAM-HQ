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
- Added strict workload policy in `RULES.md` v1.4: ChatGPT / Chief is the only default high-load executor, including after new AIs are added.
- Added AI availability, credit-limit, suspension, recovery, and failover rules.
- Defined special handling for Chief credit exhaustion: preserve only the next actionable resumption step, pause high-load work, and inform the user instead of transferring execution.
- Added mandatory pre-execution optimization: consider lower-load alternatives before starting high-load work.
- Added Claude as a future team role and created AI status, failover, capability, retirement/recovery, and universal protocol documents.
- Recorded these decisions as D-009, D-010, and D-011.

### Next
Connect Gemini and Claude when ready, then verify that each AI can follow the current `RULES.md` and shared-memory protocol before assigning normal team work.

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
