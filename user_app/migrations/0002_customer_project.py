# Generated by Django 5.1 on 2024-09-01 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("customer_name", models.CharField(max_length=255)),
                ("customer_first_name", models.CharField(max_length=255)),
                ("customer_last_name", models.CharField(max_length=255)),
                ("customer_designation", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("email_id", models.EmailField(max_length=254, unique=True)),
                ("contact_phone", models.CharField(max_length=20)),
                ("contact_type", models.CharField(max_length=100)),
                ("contract_start_date", models.DateField()),
                ("contract_end_date", models.DateField()),
                ("msa_location", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "master_project_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("child_project_id", models.CharField(max_length=50, unique=True)),
                ("project_name", models.CharField(max_length=255)),
                (
                    "project_type",
                    models.CharField(
                        choices=[
                            ("T&M", "Time & Material"),
                            ("Fixed Price", "Fixed Price"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "service_offering",
                    models.CharField(
                        choices=[
                            ("Product Engineering", "Product Engineering"),
                            ("Staff Augmentation", "Staff Augmentation"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "project_status",
                    models.CharField(
                        choices=[
                            ("Active", "Active"),
                            ("On Hold", "On Hold"),
                            ("Completed", "Completed"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="user_app.customer",
                    ),
                ),
            ],
        ),
    ]
