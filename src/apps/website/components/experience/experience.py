from django_components import component
from wagtail import blocks

from apps.website.base import ComponentBlock, StructBlockRenderingAsComponent


@component.register("experience")
class Experience(ComponentBlock):
    template_name = "experience/template.html"

    class Media:
        css = "experience/style.css"


class ExperienceBlock(StructBlockRenderingAsComponent):
    title = blocks.CharBlock()
    year = blocks.CharBlock()
    description = blocks.RichTextBlock()

    class Meta:
        icon = "calendar-alt"
        component = Experience
