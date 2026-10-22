from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config import get_settings
from backend.app.db import init_db
from backend.app.services.agent_registry import load_agent_registry
from backend.app.services.connector_manager import load_connectors
from backend.app.services.provider_registry import load_provider_registry
from backend.app.services.skill_registry import load_skills


app = FastAPI(title='J.A.R.V.I.S.', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
def startup_event() -> None:
    init_db()
    get_settings()
    load_provider_registry()
    load_connectors()
    load_agent_registry()
    load_skills()


@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'J.A.R.V.I.S. backend is online.'}


@app.get('/health')
def health() -> dict[str, object]:
    return {
        'status': 'ok',
        'service': 'backend',
        'environment': get_settings().app_env,
        'version': '0.1.0',
    }


@app.get('/api/v1/health')
def api_health() -> dict[str, object]:
    return {
        'status': 'ok',
        'module': 'api',
        'provider_registry': 'loaded',
        'agent_registry': 'loaded',
        'connector_manager': 'loaded',
        'skill_registry': 'loaded',
    }
