# Generated by Django 5.0.7 on 2024-07-25 09:41

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_auto_20240725_1119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogtag",
            name="locale",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.locale",
                verbose_name="locale",
            ),
        ),
        migrations.AlterField(
            model_name="blogtag",
            name="translation_key",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name="blogtag",
            unique_together={("translation_key", "locale")},
        ),
    ]
