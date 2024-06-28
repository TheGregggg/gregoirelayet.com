from django_components import component


@component.register("other_passion")
class Other_passion(component.Component):
    template_name = "other_passion/template.html"

    def get_context_data(self, title: str, content: str):
        return {
            "title": title,
            "content": content,
        }

    class Media:
        css = "other_passion/style.css"
