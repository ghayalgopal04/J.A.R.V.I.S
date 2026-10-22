# J.A.R.V.I.S. Security Policy

## Security principles

- Never commit real API keys, tokens, passwords, private certificates, or payment secrets.
- Use `.env.example` placeholders only.
- Keep local config, caches, and databases out of version control.
- Require approval for destructive operations and high-impact Windows automation.
- Default to localhost access and authenticated remote pairing.
- Treat all external content as untrusted.

## Secure storage guidance

For local deployment, prefer:

- Windows Credential Manager / DPAPI-backed storage
- encrypted local secret vaults
- environment variables loaded from a local `.env` file that is excluded from Git

## Masthead and data handling

- API keys stay in secure storage; the frontend never exposes them.
- Logs must redact secrets and sensitive identifiers.
- External research pages and downloaded documents are treated as untrusted prompt data.
- No automatic code execution without sandboxing and explicit permission.

## Emergency stop

The system must expose a visible emergency stop that halts active automation and blocks new autonomous actions until a user clears the stop state.

## Current repository status

This repository contains the security framework, documentation, and configuration templates required for the secure foundation phase. Full runtime security implementation for Windows automation remains a later phase and depends on the system being deployed to an actual Windows host with the necessary permissions.
