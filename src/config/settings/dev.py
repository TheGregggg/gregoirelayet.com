import os
from pathlib import Path

from config.settings.base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-s$fe++l8)hr1&k@^r3t!lw79w(hacm(&&oucvx4+@kl&bnq*2g"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WSGI_APPLICATION = "config.wsgi.app"

with open(
    os.path.join(
        Path(__file__).resolve().parent.parent.parent.parent,
        "secrets/db_user_password.txt",
    )
) as f:
    DATABASES["default"]["PASSWORD"] = f.read().strip()  # noqaO

if not TESTING and False:  # noqa
    INSTALLED_APPS += [  # noqa
        "debug_toolbar",
    ]
    MIDDLEWARE += [  # noqa
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    # Don't show the toolbar on admin previews
    def show_toolbar(request):
        request.META["wsgi.multithread"] = True
        request.META["wsgi.multiprocess"] = True
        excluded_urls = ["/pages/preview/", "/pages/preview_loading/", "/edit/preview/"]
        excluded = any(request.path.endswith(url) for url in excluded_urls)
        return DEBUG and not excluded

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
