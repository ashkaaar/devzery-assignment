# Generated by Django 4.2.2 on 2023-07-12 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_link_go_live_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-id'], 'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]