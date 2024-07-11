from django_components import component
from wagtail.blocks import CharBlock
from wagtail.images.blocks import ImageChooserBlock

from apps.website.base import ComponentBlock, StructBlockRenderingAsComponent


@component.register("image_block")
class ImageBlockComponent(ComponentBlock):
    template_name = "image_block/template.html"

    class Media:
        css = "image_block/style.css"


class ImageBlock(StructBlockRenderingAsComponent):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alt_text = CharBlock(required=False)

    class Meta:
        icon = "image"
        component = ImageBlockComponent
