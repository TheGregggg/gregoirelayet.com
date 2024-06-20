from django.db import models
from wagtail import blocks
from wagtail.fields import StreamField


class Footer(models.Model):
    pages = StreamField([("Page", blocks.PageChooserBlock(can_choose_root=True))])
    github_link = models.URLField(blank=True, null=True)
    github_username = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "Footer"
