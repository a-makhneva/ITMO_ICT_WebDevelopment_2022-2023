# Generated by Django 4.1.3 on 2022-11-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carowner",
            name="birthday",
            field=models.DateField(null=True),
        ),
    ]
