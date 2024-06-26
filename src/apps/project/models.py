from django.db import models
from django.http import HttpRequest
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, FieldRowPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale

from apps.website.base import HtmxPage


class ProjectsPage(HtmxPage):
    subpage_types = ["ProjectPage"]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["projects"] = ProjectPage.objects.filter(
            locale=Locale.get_active()
        ).live()
        return context


class ProjectPage(HtmxPage):
    short_description = RichTextField(
        "Project's short description, to show on list item", default=""
    )
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
        FieldPanel("show_on_home_page"),
        FieldPanel("short_description"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("technologies"),
        FieldRowPanel(
            (
                FieldPanel("website_link"),
                FieldPanel("repo_link"),
            )
        ),
    ]

    parent_page_types = ["ProjectsPage"]
