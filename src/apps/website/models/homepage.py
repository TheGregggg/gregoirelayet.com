from django.http import HttpRequest
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale

from apps.project.models import ProjectPage
from apps.website.base import ComponentStructBlock, HtmxPage
from apps.website.components.other_passion.other_passion import Other_passion


class TimelineBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    year = blocks.CharBlock()
    description = blocks.RichTextBlock()

    class Meta:
        icon = "calendar-alt"
        template = "website/blocks/event.html"


class PassionBlock(ComponentStructBlock):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()

    class Meta:
        icon = "pick"
        component = Other_passion


class HomePage(HtmxPage):
    about_me = RichTextField(blank=True)
    timeline = StreamField([("Event", TimelineBlock())], blank=True)
    passions = StreamField([("Passion", PassionBlock())], blank=True)

    content_panels = HtmxPage.content_panels + [
        FieldPanel("about_me"),
        FieldPanel("timeline"),
        FieldPanel("passions"),
    ]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["projects"] = ProjectPage.objects.filter(
            show_on_home_page=True, locale=Locale.get_active()
        ).live()
        return context
