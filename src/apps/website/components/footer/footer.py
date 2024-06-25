from django_components import component
from apps.website.models.components.footer import Footer as FooterModel
from django.http import HttpRequest


@component.register("footer")
class Footer(component.Component):
    template_name = "footer/template.html"

    def get_context_data(self, request: HttpRequest):
        data = FooterModel.load(request_or_site=request)
        return {"data": data}

    class Media:
        css = "footer/style.css"
        js = "footer/script.js"
