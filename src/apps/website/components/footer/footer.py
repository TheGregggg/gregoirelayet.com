from django_components import component
from apps.website.models.components.footer import Footer as FooterModel


@component.register("footer")
class Footer(component.Component):
    template_name = "footer/template.html"

    def get_context_data(self):
        data = FooterModel.load(request_or_site=self.outer_context["request"])
        return {"data": data}

    class Media:
        css = "footer/style.css"
