from .base import HtmxPage
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel


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
