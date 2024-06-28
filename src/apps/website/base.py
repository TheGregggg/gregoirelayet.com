from django.http import HttpRequest
from django_components.component import Component
from wagtail.blocks import StructBlock
from wagtail.models import Page


class HtmxPage(Page):
    class Meta:
        abstract = True

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if request.htmx:  # type: ignore
            base_template = "partial.html"
        else:
            base_template = "base.html"
        context["base_template"] = base_template
        return context


class ComponentStructBlock(StructBlock):
    class Meta:
        component: None | Component = None

    def render(self, value, context=None):
        if self.meta.component:
            return self.meta.component.render(kwargs=value)
        return ""
