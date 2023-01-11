# Generated by Django 4.1.4 on 2022-12-25 20:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conf_app', '0008_alter_conference_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='speaker',
            field=models.ManyToManyField(related_name='speaker', to=settings.AUTH_USER_MODEL),
        ),
    ]
