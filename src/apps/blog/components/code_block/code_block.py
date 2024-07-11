from django_components import component
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from wagtail.blocks import BooleanBlock, ChoiceBlock, TextBlock

from apps.website.base import ComponentBlock, StructBlockRenderingAsComponent

LANGUAGE_CHOICES = [
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
]


@component.register("code_block")
class CodeBlockComponent(ComponentBlock):
    template_name = "code_block/template.html"

    class Media:
        css = "code_block/style.css"


class CodeBlock(StructBlockRenderingAsComponent):
    language = ChoiceBlock(
        choices=LANGUAGE_CHOICES,
        group="language_and_lines",
    )
    show_lines = BooleanBlock(default=False, required=False)
    code = TextBlock()
    rendered_code = TextBlock(blank=True, required=False)

    class Meta:
        icon = "code"
        form_template = "code_block/admin_form.html"
        component = CodeBlockComponent

    def clean(self, value):
        result = super().clean(value)

        lexer = get_lexer_by_name(result["language"], stripall=True)
        formater = HtmlFormatter(linenos=result["show_lines"])

        result["rendered_code"] = highlight(result["code"], lexer, formater)

        return result
