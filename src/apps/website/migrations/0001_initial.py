# Generated by Django 5.0.3 on 2024-04-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_order', models.PositiveSmallIntegerField(db_index=True, default=0)),
            ],
            options={
                'ordering': ['category_order'],
            },
        ),
    ]