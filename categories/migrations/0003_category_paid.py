# Generated by Django 3.2.14 on 2022-07-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_rename_title_category_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]
