# Generated by Django 5.0.7 on 2024-07-25 09:19

from django.db import migrations
from wagtail.models import BootstrapTranslatableModel


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_blogtag_locale_blogtag_translation_key"),
    ]

    operations = [
        BootstrapTranslatableModel("blog.BlogTag"),
    ]
