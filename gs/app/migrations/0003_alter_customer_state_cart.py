# Generated by Django 4.1.4 on 2023-06-18 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0002_rename_customer1_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("Andhra Pradesh", "Andhra Pradesh"),
                    ("Arunachal Pradesh ", "Arunachal Pradesh "),
                    ("Assam", "Assam"),
                    ("Bihar", "Bihar"),
                    ("Chhattisgarh", "Chhattisgarh"),
                    ("Goa", "Goa"),
                    ("Gujarat", "Gujarat"),
                    ("Haryana", "Haryana"),
                    ("Himachal Pradesh", "Himachal Pradesh"),
                    ("Jammu and Kashmir ", "Jammu and Kashmir "),
                    ("Jharkhand", "Jharkhand"),
                    ("Karnataka", "Karnataka"),
                    ("Kerala", "Kerala"),
                    ("Madhya Pradesh", "Madhya Pradesh"),
                    ("Maharashtra", "Maharashtra"),
                    ("Manipur", "Manipur"),
                    ("Meghalaya", "Meghalaya"),
                    ("Mizoram", "Mizoram"),
                    ("Nagaland", "Nagaland"),
                    ("Odisha", "Odisha"),
                    ("Punjab", "Punjab"),
                    ("Rajasthan", "Rajasthan"),
                    ("Sikkim", "Sikkim"),
                    ("Tamil Nadu", "Tamil Nadu"),
                    ("Telangana", "Telangana"),
                    ("Tripura", "Tripura"),
                    ("Uttar Pradesh", "Uttar Pradesh"),
                    ("Uttarakhand", "Uttarakhand"),
                    ("West Bengal", "West Bengal"),
                    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
                    ("Chandigarh", "Chandigarh"),
                    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
                    ("Daman and Diu", "Daman and Diu"),
                    ("Lakshadweep", "Lakshadweep"),
                    (
                        "National Capital Territory of Delhi",
                        "National Capital Territory of Delhi",
                    ),
                    ("Puducherry", "Puducherry"),
                ],
                default="Maharashtra",
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]