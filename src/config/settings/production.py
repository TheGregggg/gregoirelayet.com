from config.settings.base import *

DEBUG = False

with open(os.path.dirname(os.path.abspath(__file__)) + "/secret.txt") as f:
    SECRET_KEY = f.read().strip()

DNS_NAME = "gregoirelayet.com"

ALLOWED_HOSTS = [DNS_NAME]
CSRF_TRUSTED_ORIGINS = [f"https://{DNS_NAME}"]

ASGI_APPLICATION = "config.settings.asgi.app"
