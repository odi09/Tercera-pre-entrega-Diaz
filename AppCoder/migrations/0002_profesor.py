# Generated by Django 5.0.3 on 2024-04-02 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppCoder", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profesor",
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
                ("nombre", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("materia", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
            ],
        ),
    ]
