#!/bin/bash
set -e

echo "Starting the application..."
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080
