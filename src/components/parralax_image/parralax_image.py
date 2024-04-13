from django_components import component


@component.register("parralax_image")  # type: ignore
class Parralax_image(component.Component):
    template_name = "parralax_image/template.html"

    def get_context_data(self, image):
        return {
            "image": image,
        }

    class Media:
        css = "parralax_image/style.css"
        js = "parralax_image/script.js"
