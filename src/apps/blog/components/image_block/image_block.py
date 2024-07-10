from django_components import component


@component.register("image_block")
class ImageBlock(component.Component):
    template_name = "image_block/template.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        css = "image_block/style.css"
        js = "image_block/script.js"
