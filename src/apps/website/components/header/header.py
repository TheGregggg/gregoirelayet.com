from django_components import component

from apps.website.models.components.header import Header as HeaderModel


@component.register("header")
class Header(component.Component):
    template_name = "header/template.html"

    def get_context_data(self):
        data = HeaderModel.load(request_or_site=self.outer_context["request"])
        return {"data": data}

    class Media:
        css = "header/style.css"
        js = "header/script.js"
