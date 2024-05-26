from django.http import HttpRequest
from .base import HtmxPage
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

from apps.project.models import ProjectPage


class TimelineBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    year = blocks.CharBlock()

    class Meta:
        icon = "calendar-alt"


class PassionBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()

    class Meta:
        icon = "pick"


class HomePage(HtmxPage):
    about_me = RichTextField(blank=True)
    timeline = StreamField([("Event", TimelineBlock())])
    passions = StreamField([("Passion", PassionBlock())])

    content_panels = HtmxPage.content_panels + [
        FieldPanel("about_me"),
        FieldPanel("timeline"),
        FieldPanel("passions"),
    ]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["projects"] = ProjectPage.objects.filter(show_on_home_page=True).live()
        return context
