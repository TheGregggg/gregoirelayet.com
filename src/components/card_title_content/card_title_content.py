from django_components import component


@component.register("card_title_content")
class CardTitleContent(component.Component):
    template_name = "card_title_content/template.html"

    def get_context_data(self, title: str):
        return {
            "title": title,
        }

    class Media:
        css = "card_title_content/style.css"
