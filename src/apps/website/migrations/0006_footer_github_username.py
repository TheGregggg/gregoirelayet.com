# Generated by Django 5.0.3 on 2024-06-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='github_username',
            field=models.CharField(blank=True, null=True),
        ),
    ]