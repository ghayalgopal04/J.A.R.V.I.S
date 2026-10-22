# J.A.R.V.I.S.

J.A.R.V.I.S. is a modular, secure, extensible AI desktop assistant monorepo for Windows. This repository establishes the foundation for a future-ready autonomous assistant with a React + TypeScript frontend, Python FastAPI backend, local SQLite persistence, configurable provider abstraction, desktop shell scaffolding, and Windows automation bridge.

## Repository status

This repository starts from a clean project scaffold and implements the foundation phase of the master specification. The codebase intentionally preserves a clear separation between:

- frontend/
- backend/
- desktop/
- bridge/
- mobile_remote/
- config/
- docs/
- scripts/
- tests/

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

### Windows setup

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup.ps1
```

## Current implementation scope

Implemented or scaffolded in this repo:

- Architecture and repo structure
- FastAPI health endpoint and configuration
- SQLite database bootstrap
- Provider registry abstraction and agent registry stubs
- React + Vite + TypeScript dashboard with sidebar navigation skeleton
- Security and credential guidance
- GitHub Actions CI configuration
- Windows PowerShell scripts
- Traceability and implementation plan documentation

## Known limitations

- No live AI provider credentials are supplied.
- No Windows automation hardware or host integration is configured in this environment.
- Full phase-by-phase delivery of every feature from the master prompt is a multi-release effort; this repository preserves the required architecture and a working foundation for continued implementation.
- Runtime verification was limited to static repository creation because command execution tools are not available in this session.

## Contributing

This project is intentionally structured so future modules can be added via typed interfaces and registry-driven services rather than hard-coded branches.
