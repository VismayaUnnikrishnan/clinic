# Generated by Django 5.0 on 2024-01-03 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("p_name", models.CharField(max_length=100)),
                ("p_email", models.EmailField(max_length=254)),
                ("p_password", models.CharField(max_length=100)),
                ("p_username", models.CharField(max_length=50)),
                ("p_mobile", models.CharField(max_length=15)),
                (
                    "past_medical_history",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "p_gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=10
                    ),
                ),
                ("p_city", models.CharField(max_length=50)),
                ("p_state", models.CharField(max_length=50)),
                ("p_address", models.TextField()),
                ("p_code", models.CharField(max_length=10)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
