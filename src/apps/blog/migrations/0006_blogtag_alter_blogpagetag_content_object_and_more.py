# Generated by Django 5.0.7 on 2024-07-25 09:19

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blogpage_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="name"),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        max_length=100,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
            },
        ),
        migrations.AlterField(
            model_name="blogpagetag",
            name="content_object",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_tags",
                to="blog.blogpage",
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogPageTag",
                to="blog.BlogTag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="blogpagetag",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tagged_blogs",
                to="blog.blogtag",
            ),
        ),
    ]
