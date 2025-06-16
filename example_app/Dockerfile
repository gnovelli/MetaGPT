FROM python:3.9-slim

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app

CMD ["poetry", "run", "python", "-m", "app.main"]
