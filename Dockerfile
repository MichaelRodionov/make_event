FROM python:3.10-slim

WORKDIR /event_app

COPY poetry.lock pyproject.toml ./
COPY core/. ./core
COPY events/. ./events
COPY organizations/. ./organizations
COPY make_event/. ./make_event
COPY manage.py .
COPY README.md .

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev