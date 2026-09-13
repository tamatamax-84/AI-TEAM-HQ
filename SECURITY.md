# AI TEAM HQ SECURITY

## Purpose
Keep the shared AI workspace free of secrets and unnecessary sensitive information.

## Rules
- Never commit passwords, API keys, access tokens, private keys, session cookies, or other authentication secrets.
- Do not place secrets in `TASK.md`, `HANDOFF.md`, `RESULT.md`, `REVIEW.md`, `LOG.md`, memory files, issues, or other shared artifacts.
- If a secret is accidentally exposed, do not copy it into another file. Stop, report the exposure to the user, and rotate/revoke the credential through the appropriate provider.
- Store only the minimum personal or confidential information required to operate the team.
- Review generated artifacts before committing them to ensure secrets and unnecessary sensitive data are absent.
- Treat repository history as durable: deleting a secret from the latest file does not necessarily remove it from Git history.

## Scope
This file supplements `RULES.md`. If there is a conflict, `RULES.md` takes precedence.

## Future hardening
Consider repository-level secret scanning and CI checks before the HQ stores more sensitive project information. Such automation should be introduced by Chief without weakening the existing rules.
