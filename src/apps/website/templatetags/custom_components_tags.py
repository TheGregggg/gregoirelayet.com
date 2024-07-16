from typing import TYPE_CHECKING, cast

from django import template
from django.core.cache import cache
from django.utils.safestring import SafeString, mark_safe
from django_components.component_registry import ComponentRegistry
from django_components.component_registry import registry as component_registry

if TYPE_CHECKING:
    from django_components.component import Component

register = template.Library()


def get_components_from_registry(registry: ComponentRegistry) -> list["Component"]:
    """Returns a list unique components from the registry."""

    unique_component_classes = list(registry.all().values())
    unique_component_classes.sort(key=lambda component: component.__name__)

    components = []
    for component_class in unique_component_classes:
        components.append(component_class(component_class.__name__))

    return components


@register.simple_tag(name="custom_component_css_dependencies")
def component_css_dependencies_tag() -> SafeString:
    """Marks location where CSS link tags should be rendered."""
    cached = cache.get("custom_component_css_dependencies")
    if cached:
        return cast(SafeString, cached)

    rendered_dependencies = []
    for component in get_components_from_registry(component_registry):
        rendered_dependencies.append(component.render_css_dependencies())

    to_cache = mark_safe("\n".join(rendered_dependencies))
    cache.set("custom_component_css_dependencies", to_cache)
    return to_cache


@register.simple_tag(name="custom_component_js_dependencies")
def component_js_dependencies_tag(preload: str = "") -> SafeString:
    """Marks location where JS script tags should be rendered."""
    cached = cache.get("custom_component_js_dependencies")
    if cached:
        return cast(SafeString, cached)

    rendered_dependencies = []
    for component in get_components_from_registry(component_registry):
        rendered_dependencies.append(component.render_js_dependencies())

    to_cache = mark_safe("\n".join(rendered_dependencies))
    cache.set("custom_component_js_dependencies", to_cache)
    return to_cache
