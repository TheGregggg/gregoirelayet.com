from django_components import component


@component.register("experience")
class Experience(component.Component):
    template_name = "experience/template.html"

    def get_context_data(self, title: str, year: str, description: str):
        return {
            "title": title,
            "year": year,
            "description": description,
        }

    class Media:
        css = "experience/style.css"
