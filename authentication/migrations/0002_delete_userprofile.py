# Generated by Django 4.2.2 on 2024-01-16 17:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
