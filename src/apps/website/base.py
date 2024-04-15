from wagtail.models import Page
from django.http import HttpRequest


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
