# Generated by Django 4.2.4 on 2023-08-17 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_advetisements", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertisement",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
            preserve_default=False,
        ),
    ]
