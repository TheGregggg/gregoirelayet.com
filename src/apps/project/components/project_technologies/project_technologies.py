from django_components import component


@component.register("project_technologies")
class Project_technologies(component.Component):
    template_name = "project_technologies/template.html"

    def get_context_data(self, technologies, attrs: dict = None):
        if attrs is None:
            attrs = {}
        return {
            "technologies": technologies,
            "attrs": attrs,
        }

    class Media:
        css = "project_technologies/style.css"
