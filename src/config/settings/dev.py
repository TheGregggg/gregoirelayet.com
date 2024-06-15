from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-s$fe++l8)hr1&k@^r3t!lw79w(hacm(&&oucvx4+@kl&bnq*2g"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["localhost"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WSGI_APPLICATION = "config.wsgi.app"
