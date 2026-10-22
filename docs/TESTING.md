# Testing

## Test strategy

This project uses a layered testing strategy:

- backend unit tests for routes, configuration, and service logic
- integration tests for database and API flows
- frontend build checks for TypeScript correctness and Vite build success
- security checks for prompt redaction and configuration handling
- workflow tests for CI pipeline integrity

## Current state

The repository contains the initial test scaffolding but full runtime verification requires an environment with the necessary toolchain and credentials.

## Suggested commands

```bash
cd backend
pytest -q

cd frontend
npm run build
npm run test -- --run
```
