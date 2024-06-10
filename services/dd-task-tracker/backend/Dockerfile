FROM python:3.11-slim

RUN pip install poetry

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root

COPY ./app /app/app
COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
