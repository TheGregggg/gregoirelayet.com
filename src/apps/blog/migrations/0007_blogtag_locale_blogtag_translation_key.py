# Generated by Django 5.0.7 on 2024-07-25 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogtag_alter_blogpagetag_content_object_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogtag",
            name="locale",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.locale",
            ),
        ),
        migrations.AddField(
            model_name="blogtag",
            name="translation_key",
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
