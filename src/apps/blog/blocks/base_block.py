from wagtail.blocks import CharBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock

from apps.website.base import ComponentStructBlock

from ..components.header_block.header_block import HeaderBlock as HeaderBlockComponent
from ..components.image_block.image_block import ImageBlock as ImageBlockComponent


class ImageBlock(ComponentStructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alt_text = CharBlock(required=False)

    class Meta:
        icon = "image"
        component = ImageBlockComponent


class HeadingBlock(ComponentStructBlock):
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
