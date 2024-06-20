from django_components import component
from django.db.models import Model
from apps.website.components_models.footer import Footer as FooterModel
from wagtail.models import Page, Locale
from typing import cast


@component.register("footer")
class Footer(component.Component):
    template_name = "footer/template.html"

    def get_context_data(self):
        data = FooterModel.objects.first()
        return {"data": data}

    class Media:
        css = "footer/style.css"
        js = "footer/script.js"
