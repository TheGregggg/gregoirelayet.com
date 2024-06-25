from django.db import models
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel


@register_setting
class Footer(BaseGenericSetting):
    pages = StreamField([("Page", blocks.PageChooserBlock(can_choose_root=True))])
    github_link = models.URLField(blank=True, null=True)
    github_username = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    panels = [
        FieldPanel("pages"),
        FieldPanel("github_link"),
        FieldPanel("github_username"),
        FieldPanel("email"),
    ]
