from django_components import component


@component.register("code_block")
class CodeBlock(component.Component):
    template_name = "code_block/template.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        css = "code_block/style.css"
