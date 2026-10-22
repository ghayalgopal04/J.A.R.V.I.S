# Setup for Windows

## Prerequisites

- Windows 11 or Windows 10
- Python 3.12+
- Node.js 20 LTS+
- Git
- VS Code recommended

## First-time setup

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

## Start backend and frontend

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start.ps1
```

## Stop services

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\stop.ps1
```

## Diagnostics

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\diagnostics.ps1
```

## Notes

- API credentials are not committed.
- Windows automation bridge installs require administrator approval and explicit user consent.
- Local voice features require sound device access and driver support.
