from pathlib import Path
from typing import cast

from compressor.management.commands import compress
from django.template import engines
from django.template.backends.django import DjangoTemplates
from django.template.loaders.app_directories import Loader


class CompressLoader(Loader):
    """Loader which only returns template paths inside this application."""

    def get_dirs(self) -> list[str | Path]:
        # app_dir = settings.BASE_DIR
        ds = super().get_dirs()

        a = [d for d in ds if "src" in str(d)]
        print(a)
        return a


class Command(compress.Command):
    """Compressor for only gregoirelayet templates."""

    def get_loaders(self) -> list[Loader]:
        template = cast(DjangoTemplates, engines["django"])
        return [CompressLoader(template.engine)]
