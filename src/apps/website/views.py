from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Any

from .service import get_all_skills_categories


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


async def index(request):
    skills_categories = await get_all_skills_categories()

    return htmx_render(
        request, "website/home.html", {"skills_categories": skills_categories}
    )


def projects(request):
    return htmx_render(request, "website/projects.html")
