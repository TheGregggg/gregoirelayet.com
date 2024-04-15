from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Any


def htmx_render(
    request: HttpRequest, template: str, context: dict[str, Any] | None = None
) -> HttpResponse:
    if request.htmx:  # type: ignore
        base_template = "partial.html"
    else:
        base_template = "base.html"

    if context is None:
        context = {}
    context["base_template"] = base_template

    return render(request, template, context)


def index(request):
    return htmx_render(request, "website/home.html")


def projects(request):
    return htmx_render(request, "website/projects.html")
