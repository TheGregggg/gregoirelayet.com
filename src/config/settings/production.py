import os
from pathlib import Path

from decouple import config

from config.settings.base import *  # noqa

DEBUG = False

SECRET_KEY_FILE = config(
    "SECRET_KEY_FILE",
    default=os.path.join(Path(__file__).resolve().parent.parent, "secrets/secret.txt"),
)
with open(SECRET_KEY_FILE, "r") as f:
    SECRET_KEY = f.read().strip()

with open(config("DB_PASSWORD_FILE"), "r") as f:
    DATABASES["default"]["PASSWORD"] = f.read().strip()  # noqa

DATABASES["default"]["HOST"] = config("DB_HOST")  # noqa
DATABASES["default"]["PORT"] = config("DB_PORT")  # noqa

FQDN = config("DNS_NAME", default="127.0.0.1")

ALLOWED_HOSTS = [
    FQDN,
]
CSRF_TRUSTED_ORIGINS = [f"https://{FQDN}"]
