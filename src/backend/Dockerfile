FROM python:3.10-slim

WORKDIR /backend

COPY poetry.lock ./
COPY pyproject.toml ./

RUN pip install --no-cache-dir poetry

RUN poetry install --no-root --no-dev

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
