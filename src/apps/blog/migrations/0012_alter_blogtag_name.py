# Generated by Django 5.0.7 on 2024-07-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_blogpagetag_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogtag",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Name"),
        ),
    ]
