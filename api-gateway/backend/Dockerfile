FROM python:3.11-slim

RUN pip install poetry

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
COPY ./app /app/app

RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]