from django_components import component

from apps.project.models import ProjectPage


@component.register("project")
class Project(component.Component):
    template_name = "project/template.html"

    def get_context_data(self, project: ProjectPage):
        return {
            "project": project,
        }

    class Media:
        css = "project/style.css"
