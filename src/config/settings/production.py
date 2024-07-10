import os
from pathlib import Path

from config.settings.base import *  # noqa

DEBUG = False

with open(
    os.path.join(Path(__file__).resolve().parent.parent, "secrets/secret.txt")
) as f:
    SECRET_KEY = f.read().strip()

DNS_NAME = "gregoirelayet.com"

ALLOWED_HOSTS = [DNS_NAME]
CSRF_TRUSTED_ORIGINS = [f"https://{DNS_NAME}"]

WSGI_APPLICATION = "config.wsgi.app"

COMPRESS_ENABLED = True
