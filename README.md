# J.A.R.V.I.S.

J.A.R.V.I.S. is a modular, secure, extensible AI desktop assistant monorepo for Windows.

## Phase 1 foundations

This repository currently includes the architecture, backend skeleton, frontend shell, and implementation plan for the first project milestone.

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```
