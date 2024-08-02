from django_components import component


@component.register("blog_tags")
class Blog_tags(component.Component):
    template_name = "blog_tags/template.html"

    def get_context_data(self, blog_index_page, tags, attrs: dict | None = None):
        if attrs is None:
            attrs = {}
        return {
            "blog_index_page": blog_index_page,
            "tags": tags,
            "attrs": attrs,
        }

    class Media:
        css = "blog_tags/style.css"
