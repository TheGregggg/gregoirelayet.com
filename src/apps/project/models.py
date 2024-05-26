from apps.website.base import HtmxPage
from django.db import models
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel


class ProjectsPage(HtmxPage):
    subpage_types = ["ProjectPage"]


class ProjectPage(HtmxPage):
    description = RichTextField("Project's description", default="")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    technologies = StreamField(
        [("Technology", blocks.CharBlock())], blank=True, null=True
    )
    website_link = models.URLField(
        "Projet website's link", null=True, blank=True, default=None
    )
    repo_link = models.URLField(
        "Projet repo's link", null=True, blank=True, default=None
    )

    show_on_home_page = models.BooleanField(
        "Show this project on the home page", default=False
    )

    content_panels = HtmxPage.content_panels + [
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("technologies"),
        FieldPanel("website_link"),
        FieldPanel("repo_link"),
        FieldPanel("show_on_home_page"),
    ]

    parent_page_types = ["ProjectsPage"]
