import os

from config.settings.base import *  # noqa

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_build")]  # noqa
