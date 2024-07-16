import os

from config.settings.base import *  # noqa

STATIC_ROOT = os.path.join(BASE_DIR, "static_build")  # noqa

STORAGES["staticfiles"] = {  # noqa
    "BACKEND": "pipeline.storage.PipelineStorage",
}
