from wagtail.blocks import RichTextBlock, StreamBlock
from wagtail.embeds.blocks import EmbedBlock

from .components.code_block.code_block import CodeBlock
from .components.header_block.header_block import HeadingBlock
from .components.image_block.image_block import ImageBlock


class BlogBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow",
        features=[
            "bold",
            "italic",
            "link",
            "ol",
            "ul",
            "code",
            "superscript",
            "subscript",
            "strikethrough",
            "blockquote",
        ],
    )

    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed.",
        icon="media",
    )

    code_block = CodeBlock()
