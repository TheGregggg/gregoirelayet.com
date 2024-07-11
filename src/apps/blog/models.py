from django.db import models
from django.http import HttpRequest
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Locale, Page
from wagtail.search import index

from apps.website.base import HtmxPage

from .blocks import HeadingBlock, ImageBlock
from .code_block import CodeBlock


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogsIndexPage(HtmxPage):
    parent_page_types = ["website.HomePage"]
    subpage_types = ["BlogPage"]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context["projects"] = BlogPage.objects.filter(locale=Locale.get_active()).live()
        return context


class BlogPage(HtmxPage):
    parent_page_types = ["BlogsIndexPage"]
    date = models.DateField("Post date")
    intro = RichTextField(max_length=250)
    body = StreamField(
        block_types=[
            ("heading_block", HeadingBlock()),
            (
                "paragraph_block",
                RichTextBlock(
                    icon="pilcrow",
                    features=[
                        "bold",
                        "italic",
                        "link",
                        "ol",
                        "ul",
                        "code",
                        "superscript",
                        "subscript",
                        "strikethrough",
                        "blockquote",
                    ],
                ),
            ),
            ("image_block", ImageBlock()),
            (
                "embed_block",
                EmbedBlock(
                    help_text="Insert a URL to embed.",
                    icon="media",
                ),
            ),
            ("code_block", CodeBlock()),
        ],
        blank=True,
    )

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
