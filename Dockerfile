FROM python:3.12-slim-bookworm

# Add user that will be used in the container.
RUN useradd glwagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \ 
    netcat-traditional \
 && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==22.0.0"

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Install the project requirements.
COPY requirements.txt ./
RUN pip install -r ./requirements.txt


# Set this directory to be owned by the "glwagtail" user.
RUN chown glwagtail:glwagtail /app

# Copy the source code of the project into the container.
COPY --chown=glwagtail:glwagtail src .

# Use user "wagtail" to run the build commands below and the server itself.
USER glwagtail

COPY --chown=glwagtail:glwagtail ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD set -xe; gunicorn config.wsgi:app