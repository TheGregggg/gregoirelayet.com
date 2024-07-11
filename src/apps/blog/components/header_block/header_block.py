from django_components import component


@component.register("header_block")
class HeaderBlock(component.Component):
    template_name = "header_block/template.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        css = "header_block/style.css"
