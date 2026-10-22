# Architecture

## Purpose

The J.A.R.V.I.S. architecture separates frontend, backend, desktop shell, automation bridge, and remote/mobile surfaces while keeping a shared contract layer for provider interfaces, connectors, agents, and skills.

## Layered design

1. Frontend
   - React + TypeScript + Vite + Tailwind
   - Routes and modules for dashboard, chat, memory, settings, automation, trading, etc.

2. Backend API
   - FastAPI service layer
   - SQLite repositories
   - provider abstraction and connector manager
   - orchestration services and permission checks

3. Desktop shell
   - Electron container for Windows desktop runtime
   - local lifecycle management, tray behavior, startup controls, notifications

4. Local bridge
   - explicit Windows automation interface with sandboxed execution and permission checks

5. Mobile remote
   - authenticated remote dashboard and pairing workflow

6. Shared configuration and schemas
   - provider adapter definitions
   - agent definitions
   - connector metadata
   - safe permission policy documents

## Core services

- provider_registry.py
- agent_registry.py
- connector_manager.py
- skill_registry.py
- task_orchestrator.py
- file_service.py
- research_service.py
- trading_service.py
- voice_service.py
- monitoring_service.py

## Design principles

- typed contracts across layers
- explicit approvals for high-risk actions
- local-first data persistence
- secure credential storage
- modular plugin architecture
