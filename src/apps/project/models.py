from django.db import models
from django.http import HttpRequest
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import CharBlock, URLBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale

from apps.blog.streamblock import BlogBlock
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
    body = StreamField(BlogBlock())

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    technologies = StreamField([("Technology", CharBlock())], blank=True, null=True)
    links = StreamField([("Link", URLBlock())], blank=True, null=True)
    repo_link = models.URLField(
        "Projet repo's link", null=True, blank=True, default=None
    )

    show_on_home_page = models.BooleanField(
        "Show this project on the home page", default=False
    )

    content_panels = HtmxPage.content_panels + [
        FieldPanel("show_on_home_page"),
        FieldPanel("short_description"),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("technologies", classname="collapsed"),
        FieldPanel("repo_link"),
        FieldPanel("links"),
    ]

    parent_page_types = ["ProjectsPage"]
