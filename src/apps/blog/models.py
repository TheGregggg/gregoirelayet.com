from django.db import models
from django.http import HttpRequest
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Locale, Page
from wagtail.search import index

from apps.website.base import HtmxPage

from .blocks.streamfield import blogStreamField


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogsIndexPage(HtmxPage):
    parent_page_types = ["website.HomePage"]
    subpage_types = ["BlogPage"]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["blog_pages"] = BlogPage.objects.filter(
            locale=Locale.get_active()
        ).live()
        return context


class BlogPage(HtmxPage):
    parent_page_types = ["BlogsIndexPage"]
    date = models.DateField("Post date")
    intro = RichTextField(max_length=250)
    body = blogStreamField

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("tags"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
