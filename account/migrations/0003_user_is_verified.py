# Generated by Django 5.0.2 on 2024-02-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]
