from django_components import component
from wagtail.blocks import CharBlock, ChoiceBlock

from apps.website.base import ComponentBlock, StructBlockRenderingAsComponent


@component.register("header_block")
class HeaderBlockComponent(ComponentBlock):
    template_name = "header_block/template.html"

    class Media:
        css = "header_block/style.css"


class HeadingBlock(StructBlockRenderingAsComponent):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        component = HeaderBlockComponent
