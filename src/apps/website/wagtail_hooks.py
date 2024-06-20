from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from apps.website.models.components.footer import Footer


class FooterViewSet(SnippetViewSet):
    model = Footer

    panels = [
        FieldPanel("pages"),
        FieldPanel("github_link"),
        FieldPanel("github_username"),
        FieldPanel("email"),
    ]


register_snippet(FooterViewSet)
