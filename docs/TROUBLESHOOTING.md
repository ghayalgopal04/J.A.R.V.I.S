# Troubleshooting

## Missing dependencies

- Ensure Python 3.12 is installed.
- Ensure Node.js 20 LTS is installed.
- Reinstall backend dependencies from `backend/requirements.txt`.
- Reinstall frontend dependencies from `frontend/package.json`.

## DB issues

- Delete local SQLite files only after confirming no sensitive data is needed.
- Re-run migrations or reinitialize the database using the backend bootstrap script.

## Provider errors

- Validate the API key in the `.env` file or secure vault.
- Confirm the provider is selected in the configuration and the model name is valid.
- Confirm network access and rate limits.

## Windows automation issues

- Grant the application the relevant permissions.
- Ensure the desktop bridge is running.
- Confirm the script is not blocked by Execution Policy.
