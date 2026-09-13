# AI TEAM HQ

複数のAIを1つのチームとして動かすための司令部・共有メモリ。

## Current architecture

User → Chief → AI TEAM HQ → AI review / instruction → Chief

GitHubを共通の作業記憶・伝言板・監査ログとして利用する。AI同士が直接チャットできることは前提にしない。

## Team
- **ChatGPT / Chief** — 統括、最終判断、全高負荷作業、メモリ整理
- **GitHub Copilot** — GitHub確認、指示、レビュー、検証、ハンドオフ
- **Gemini** — 独立レビュー、別視点、リスク・仕様検証
- **Claude** — 設計、推論、アーキテクチャ、文書・コードレビュー

GeminiとClaudeは接続・検証が完了するまで `NOT_CONNECTED` として扱う。

## Non-negotiable operating principles
1. Every AI reads the current `RULES.md` before acting or recommending anything.
2. ChatGPT / Chief is the only default high-load executor, including for future AIs.
3. Before high-load execution, Chief checks for a lower-load alternative.
4. Non-Chief AI credit exhaustion can trigger suspension and low-load failover.
5. Chief credit exhaustion pauses high-load work; it is not transferred to another AI by default. Only the next actionable resumption step is preserved and the user is informed.
6. GitHub is durable shared memory for important work inside and outside GitHub, but AIs read only relevant memory.
7. Memory maintenance is owned by Chief; other AIs may identify cleanup candidates.
8. No AI may claim execution or direct communication without evidence.
9. User manual editing is minimized.

## Core control files
- `RULES.md` — highest-priority operating rules
- `ROLES.md` — role and permission boundaries
- `AI_TEAM_PROTOCOL.md` — universal operating sequence
- `AI_STATUS.md` — current AI availability
- `AI_FAILOVER.md` — credit-limit and availability handling
- `AI_CAPABILITIES.md` — working capability registry
- `AI_RETIREMENT.md` — suspension/recovery lifecycle
- `TASK.md` / `TASK_STATES.md` — task and completion control
- `HANDOFF.md` — handoff channel
- `RESULT.md` — result channel
- `REVIEW.md` — independent review channel
- `PROJECT_REGISTRATION.md` — project context standard
- `MEMORY/CURRENT.md` — concise current team state
- `DECISIONS.md` — confirmed decisions
- `LOG.md` — operational history

## Memory economy
Store durable knowledge, not every conversation. Prefer concise current state and useful decisions/results over raw transcripts. Archive or delete obsolete information during periodic Chief-led maintenance.

## Status
Protocol v1.4 — HQ foundation under validation

## Next
1. Validate the protocol with a small sample task.
2. Connect and verify Gemini.
3. Connect and verify Claude.
4. Run a multi-AI handoff/review test.
5. Only then expand to normal project work.
