from django.http import HttpRequest
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale

from apps.project.models import ProjectPage
from apps.website.base import HtmxPage
from apps.website.components.experience.experience import ExperienceBlock
from apps.website.components.other_passion.other_passion import OtherPassionBlock


class HomePage(HtmxPage):
    about_me = RichTextField(blank=True)
    experiences = StreamField([("Experience", ExperienceBlock())], blank=True)
    other_passions = StreamField([("Passion", OtherPassionBlock())], blank=True)

    content_panels = HtmxPage.content_panels + [
        FieldPanel("about_me"),
        FieldPanel("experiences"),
        FieldPanel("other_passions"),
    ]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["projects"] = ProjectPage.objects.filter(
            show_on_home_page=True, locale=Locale.get_active()
        ).live()
        return context


class StaticPage(HtmxPage):
    body = RichTextField("Corps de la page")

    content_panels = HtmxPage.content_panels + [
        FieldPanel("body"),
    ]

    parent_page_types = ["HomePage"]

    class Meta:
        verbose_name = "Static page to use for legals pages"
