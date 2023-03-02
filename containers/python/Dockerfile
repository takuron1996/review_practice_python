ARG RUNTIME_VERSION="3.11.1"
FROM python:${RUNTIME_VERSION}
WORKDIR /application
RUN pip install --upgrade pip && pip install poetry
COPY application/pyproject.toml ./
RUN poetry install