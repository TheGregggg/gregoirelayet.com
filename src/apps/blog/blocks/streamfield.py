from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField

from .base_block import HeadingBlock, ImageBlock
from .code_block import CodeBlock

blogStreamField = StreamField(
    block_types=[
        ("heading_block", HeadingBlock()),
        (
            "paragraph_block",
            RichTextBlock(
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
            ),
        ),
        ("image_block", ImageBlock()),
        (
            "embed_block",
            EmbedBlock(
                help_text="Insert a URL to embed.",
                icon="media",
            ),
        ),
        ("code_block", CodeBlock()),
    ],
    blank=True,
)
