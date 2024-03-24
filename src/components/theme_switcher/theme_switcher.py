from django_components import component


@component.register("theme_switcher")
class Theme_switcher(component.Component):
    template_name = "theme_switcher/template.html"

    class Media:
        css = "theme_switcher/style.css"
        js = "theme_switcher/script.js"
