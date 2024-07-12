import os
from pathlib import Path

from config.settings.base import *  # noqa

DEBUG = False

with open(
    os.path.join(Path(__file__).resolve().parent.parent, "secrets/secret.txt")
) as f:
    SECRET_KEY = f.read().strip()

with open(os.path.join("/", "run", "secrets", "db_user_password")) as f:
    DATABASES["default"]["PASSWORD"] = f.read().strip()  # noqa
DATABASES["default"]["HOST"] = os.environ.setdefault("DB_HOSTNAME", "")  # noqa
DATABASES["default"]["PORT"] = os.environ.setdefault("DB_PORT", "")  # noqa

DNS_NAME = "gregoirelayet.com"

ALLOWED_HOSTS = [DNS_NAME, "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = [f"https://{DNS_NAME}"]

WSGI_APPLICATION = "config.wsgi.app"

COMPRESS_ENABLED = True
