# Generated by Django 5.0.7 on 2024-07-25 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_blogpagetag_locale_blogpagetag_translation_key_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="blogpagetag",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="blogpagetag",
            name="locale",
        ),
        migrations.RemoveField(
            model_name="blogpagetag",
            name="translation_key",
        ),
    ]
