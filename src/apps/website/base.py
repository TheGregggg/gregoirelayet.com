from typing import Any, cast

from django.http import HttpRequest
from django_components.component import Component
from wagtail.blocks import StructBlock
from wagtail.models import Page


class HtmxPage(Page):
    class Meta:
        abstract = True

    def get_context(
        self, request: HttpRequest, *args: tuple[object], **kwargs: dict[object, object]
    ) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context(request, *args, **kwargs)

        if request.htmx:  # type: ignore
            base_template = "partial.html"
        else:
            base_template = "base.html"
        context["base_template"] = base_template
        return context


class ComponentBlock(Component):
    def get_context_data(self, **kwargs):
        return kwargs


class StructBlockRenderingAsComponent(StructBlock):
    class Meta:
        component: None | type[ComponentBlock] = None

    def render(self, value: dict[Any, Any], context: None = None) -> str:
        if self.meta.component:
            return cast(str, self.meta.component.render(kwargs=value))
        return ""
