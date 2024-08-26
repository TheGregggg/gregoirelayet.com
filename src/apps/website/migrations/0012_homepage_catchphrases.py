# Generated by Django 5.0.7 on 2024-08-26 14:33

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_homepage_hero_image_homepage_hero_image_alt"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="catchphrases",
            field=wagtail.fields.StreamField(
                [("catchphrase", 0)],
                blank=True,
                block_lookup={0: ("wagtail.blocks.CharBlock", (), {"max_length": 150})},
            ),
        ),
    ]