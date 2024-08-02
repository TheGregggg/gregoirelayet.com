from django_components import component


@component.register("article")
class Article(component.Component):
    template_name = "article/template.html"

    def get_context_data(self, blog, blog_index_page):
        return {"blog": blog, "blog_index_page": blog_index_page}

    class Media:
        css = "article/style.css"
        js = "article/script.js"
