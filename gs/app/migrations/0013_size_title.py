# Generated by Django 4.1.4 on 2023-07-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="size",
            name="title",
            field=models.CharField(default="XL", max_length=20),
        ),
    ]
