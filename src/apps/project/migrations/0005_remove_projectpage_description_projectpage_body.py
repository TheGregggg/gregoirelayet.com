# Generated by Django 5.0.3 on 2024-07-11 12:48

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0004_projectpage_short_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectpage",
            name="description",
        ),
        migrations.AddField(
            model_name="projectpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading_text",
                                    wagtail.blocks.CharBlock(
                                        form_classname="title", required=True
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("", "Select a heading size"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                        ],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "paragraph_block",
                        wagtail.blocks.RichTextBlock(
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
                            icon="pilcrow",
                        ),
                    ),
                    (
                        "image_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                ("caption", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                ("alt_text", wagtail.blocks.CharBlock(required=False)),
                            ]
                        ),
                    ),
                    (
                        "embed_block",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Insert a URL to embed.", icon="media"
                        ),
                    ),
                    (
                        "code_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("css", "CSS"),
                                            ("diff", "diff"),
                                            ("html", "HTML"),
                                            ("javascript", "Javascript"),
                                            ("json", "JSON"),
                                            ("python", "Python"),
                                            ("yaml", "YAML"),
                                            ("django", "Django/Jinja"),
                                            ("docker", "Dockerfile"),
                                        ],
                                        group="language_and_lines",
                                    ),
                                ),
                                (
                                    "show_lines",
                                    wagtail.blocks.BooleanBlock(default=False),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                                (
                                    "rendered_code",
                                    wagtail.blocks.TextBlock(
                                        blank=True, required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
