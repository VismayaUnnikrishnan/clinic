# Generated by Django 5.0 on 2024-01-11 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health", "0008_patient_p_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("appointment_date", models.DateField()),
                (
                    "doctor",
                    models.CharField(
                        choices=[("dr_smith", "Dr. Smith"), ("dr_jones", "Dr. Jones")],
                        max_length=20,
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="health.patient"
                    ),
                ),
            ],
        ),
    ]