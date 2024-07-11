from django_components import component
from wagtail import blocks

from apps.website.base import ComponentBlock, StructBlockRenderingAsComponent


@component.register("other_passion")
class OtherPassion(ComponentBlock):
    template_name = "other_passion/template.html"

    class Media:
        css = "other_passion/style.css"


class OtherPassionBlock(StructBlockRenderingAsComponent):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()

    class Meta:
        icon = "pick"
        component = OtherPassion
