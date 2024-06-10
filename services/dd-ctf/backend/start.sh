#!/bin/bash
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Starting the application..."
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8082
