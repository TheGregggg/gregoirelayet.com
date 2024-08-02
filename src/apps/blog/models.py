from django.db import models
from django.http import HttpRequest
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import ItemBase, TagBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale, Page, TranslatableMixin
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from apps.website.base import HtmxPage

from .streamblock import BlogBlock


@register_snippet
class BlogTag(TagBase, TranslatableMixin):
    name: "models.CharField" = models.CharField(verbose_name="Name", max_length=100)
    slug: "models.SlugField" = models.SlugField(
        verbose_name="slug",
        max_length=100,
        allow_unicode=True,
    )
    free_tagging = False

    class Meta(TranslatableMixin.Meta):
        verbose_name = "tag"
        verbose_name_plural = "tags"

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]


class BlogPageTag(ItemBase):
    tag = models.ForeignKey(
        BlogTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey("BlogPage", related_name="post_tags")


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
    body = StreamField(BlogBlock())

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
