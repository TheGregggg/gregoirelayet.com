FROM python:3.12-slim AS builder

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir app

# install pipenv and creating the virtual env
RUN pip install "pipenv"

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /app/

WORKDIR /app

RUN pipenv sync


FROM python:3.12-slim AS runtime

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    netcat-traditional && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add user that will be used in the container.
RUN useradd gerg

# Port used by this container to serve HTTP.
EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

RUN mkdir -v -p /app/.venv && chown gerg:gerg /app

COPY --from=builder /app/.venv/ /app/.venv/

WORKDIR /app/

COPY --chown=gerg:gerg src .

COPY --chown=gerg:gerg ./entrypoint.sh .

USER gerg

# Building static files from Django Pipeline...
#  Collect files using whitenoise
RUN ./.venv/bin/python manage.py collectstatic --no-input -c --settings config.settings.build && \
    ./.venv/bin/python manage.py collectstatic --noinput -c --settings config.settings.whitenoise && \
    chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD set -xe; ./.venv/bin/gunicorn config.wsgi:app