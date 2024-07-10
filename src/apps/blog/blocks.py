from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    RawHTMLBlock,
    StructBlock,
    TextBlock,
)
from wagtail.images.blocks import ImageChooserBlock

from apps.website.base import ComponentStructBlock

from .components.header_block.header_block import HeaderBlock as HeaderBlockComponent
from .components.image_block.image_block import ImageBlock as ImageBlockComponent


class ImageBlock(ComponentStructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False, group="text")
    attribution = CharBlock(required=False, group="text")

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


class CodeBlock(StructBlock):
    language = ChoiceBlock(
        choices=[
            ("bash", "Bash/Shell"),
            ("css", "CSS"),
            ("diff", "diff"),
            ("html", "HTML"),
            ("javascript", "Javascript"),
            ("json", "JSON"),
            ("python", "Python"),
            ("yaml", "YAML"),
            ("django", "Django/Jinja"),
            ("docker", "Dockerfile"),
        ],
        group="language_and_lines",
    )
    show_lines = BooleanBlock(default=False, group="language_and_lines")
    code = TextBlock()
    rendered_code = RawHTMLBlock(blank=True, required=False)

    class Meta:
        icon = "code"
        form_template = "blog/block_forms/code_block.html"

    def clean(self, value):
        result = super().clean(value)

        lexer = get_lexer_by_name(result["language"], stripall=True)
        formater = HtmlFormatter(linenos=result["show_lines"])

        result["rendered_code"] = highlight(result["code"], lexer, formater)

        return result
