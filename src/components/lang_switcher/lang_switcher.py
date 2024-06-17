from django_components import component


@component.register("lang_switcher")
class Lang_switcher(component.Component):
    template_name = "lang_switcher/template.html"

    class Media:
        css = "lang_switcher/style.css"
        js = "lang_switcher/script.js"
